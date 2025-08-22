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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4dd70f3d-735e-3c33-b404-e7318b416fa4 | -7.86527 | -46.99258 | 2025-08-22 05:40:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| b4a3d030-3af4-340b-be1d-737b11a204f6 | -6.29384 | -43.88705 | 2025-08-22 05:40:00 | AQUA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 08bd6993-fab8-38d0-a53d-a55a507e5048 | -3.81459 | -41.56153 | 2025-08-22 05:40:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 4f02c6d0-dcb2-3db0-9b06-9a653d1622c3 | -6.51283 | -44.57361 | 2025-08-22 05:40:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0c5b68c9-65ec-3906-8efd-a681d720bb8a | -7.64885 | -45.24423 | 2025-08-22 05:40:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cb1649fc-21f4-3f4c-9eb5-4c40315e6707 | -14.74132 | -56.03928 | 2025-08-22 05:40:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f59c555-e1b8-34b8-8579-68680e3fa120 | -12.97854 | -56.88718 | 2025-08-22 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62242bfd-45f6-3aa7-85dc-6c63c7c710f8 | -14.74091 | -56.04282 | 2025-08-22 05:40:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ace49b5d-1d3c-3e8c-9a07-39b32766559f | -14.74173 | -56.03574 | 2025-08-22 05:40:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a701b6c6-bab1-3d69-9ad6-911bca12966c | -14.65293 | -54.91074 | 2025-08-22 05:40:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9c42131-93fe-3ffc-a5ab-fa6c90f0a6b7 | -14.75754 | -56.04136 | 2025-08-22 05:40:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1371a75f-e9d0-3091-9bcb-5d9d38ada041 | -12.49424 | -53.80631 | 2025-08-22 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebd8c07e-5722-3501-af9a-2c6e658560b8 | -14.76792 | -55.99992 | 2025-08-22 05:40:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 345f529f-5c23-3c58-8d26-402b0176ba1e | -12.97813 | -56.89352 | 2025-08-22 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2bde22fe-dd61-3561-a499-a8042046c1d0 | -12.98854 | -56.88828 | 2025-08-22 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 189ea423-8848-3bfc-8e25-9135c67f6af4 | -14.62476 | -54.8562 | 2025-08-22 05:40:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d47166ee-74aa-3fea-8d72-4313443d4528 | -15.02726 | -54.86108 | 2025-08-22 05:40:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e223235-85d5-36f8-93fb-fa47b8357801 | -14.67559 | -54.86665 | 2025-08-22 05:40:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5cb3415-c28f-35e5-a46b-a10c8d5b9354 | -12.99503 | -56.87739 | 2025-08-22 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06db1bd5-4270-39cc-90cc-e4938207aba9 | -14.67605 | -54.86257 | 2025-08-22 05:40:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a67f391-e391-3e3c-af44-eff0a450a5a1 | -13.13707 | -57.11728 | 2025-08-22 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e3d8571f-59a2-30aa-a02a-f2d41888d8fb | -12.58394 | -60.35579 | 2025-08-22 05:40:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5bbaed32-624d-3bee-8fc4-a281dceb8426 | -13.14201 | -57.1178 | 2025-08-22 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aa6c3669-cc44-3f5a-8a66-d205c43d74aa | -13.19353 | -59.16816 | 2025-08-22 05:40:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c1908a9-95c8-3249-80db-932d41305ed3 | -12.98206 | -56.89922 | 2025-08-22 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d887f21-7888-3d1c-be2e-bf86a0ac97e9 | -12.98383 | -56.88833 | 2025-08-22 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5e0d35a8-8329-3553-baa5-f9cbe69cd9fc | -14.62573 | -54.84788 | 2025-08-22 05:40:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 413ab357-a58d-3fd8-b640-0642706d86a3 | -14.63006 | -54.85084 | 2025-08-22 05:40:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b484663f-0a30-3552-be9e-c4b4673cbeea | -14.65458 | -56.5955 | 2025-08-22 05:40:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cc3c45a-cd46-37a7-bbd4-4acc958de272 | -12.98883 | -56.88889 | 2025-08-22 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3704b48-ff9b-3366-9bc6-4d9d4c8cb11b | -14.65494 | -56.59242 | 2025-08-22 05:40:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae5c9723-0b89-3394-821c-0ebb444faae7 | -14.63055 | -54.84631 | 2025-08-22 05:40:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8238272-c438-32b0-9f78-6d6210430ffa | -15.02146 | -54.85979 | 2025-08-22 05:40:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b26d40d5-c19b-3197-b647-64b5609eb9eb | -12.98428 | -56.88198 | 2025-08-22 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5bc3d12c-0781-3905-80ba-3de9d61bec60 | -12.9778 | -56.89293 | 2025-08-22 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3904f8f-9247-36b6-8cda-c49b12910115 | -12.98354 | -56.88773 | 2025-08-22 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2202a608-2650-3b49-9a6f-7948d407738f | -14.59232 | -54.77773 | 2025-08-22 05:40:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ae14321-34e5-3c94-9d43-57fd9b4971d8 | -12.98929 | -56.88255 | 2025-08-22 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d776786b-4343-3f12-93ed-0dcc07464d98 | -12.48761 | -53.81029 | 2025-08-22 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2992455d-a39e-3398-8a6a-6b17ff826bb3 | -14.79179 | -59.64988 | 2025-08-22 05:40:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f55788ac-bd91-3b27-b6ed-d7c6c88eb041 | -12.49367 | -53.8111 | 2025-08-22 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9ab4db3-8bd5-3fb5-b7c5-141070880cda | -14.78698 | -59.65365 | 2025-08-22 05:40:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5d4b305-4010-39bf-b7b6-056b67b68117 | -15.00508 | -54.86308 | 2025-08-22 05:40:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a41dadd-35f4-3b7f-a3f6-6ad73dc8a3da | -12.99453 | -56.88371 | 2025-08-22 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0c8fcfc-49d1-3c7b-a9cd-3774782c6de6 | -13.1491 | -54.9194 | 2025-08-22 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22cd9319-d92b-386b-a8e1-7396246ad4db | -14.62434 | -54.84909 | 2025-08-22 05:40:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0df7b553-214b-385a-9bf2-2060cfa7dc8e | -15.00461 | -54.86723 | 2025-08-22 05:40:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 868798f2-0911-3d35-9024-02269842a30b | -14.99923 | -54.86228 | 2025-08-22 05:40:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 899144b1-e888-3910-a55a-502a995a86d6 | -14.75255 | -56.03709 | 2025-08-22 05:40:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bee12ccc-3058-3064-b326-c25417306c0b | -14.7646 | -56.02801 | 2025-08-22 05:40:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2cee5c9-0e0f-3976-bcf8-efe843ff5335 | -14.58257 | -54.75888 | 2025-08-22 05:40:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c46c3c53-99e2-3c02-8cbf-5962168d7b79 | -15.02877 | -54.86352 | 2025-08-22 05:40:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6cc9ae9a-6992-3a34-bc45-ad1fe63031b6 | -14.62343 | -54.85738 | 2025-08-22 05:40:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9568ff9f-4fd1-3e73-96cb-a1f14e27f957 | -14.28209 | -60.38839 | 2025-08-22 05:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d823bd0-ba49-39e9-b475-0e1630526351 | -14.73632 | -56.03506 | 2025-08-22 05:40:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e910810-a843-394d-ac65-6e1b12971abc | -12.98953 | -56.88315 | 2025-08-22 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8926c03-205d-3b37-a0f5-4e7b749a7452 | -14.78754 | -59.64934 | 2025-08-22 05:40:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| effe6712-4b7f-3171-9456-344c0720176f | -14.75338 | -56.03005 | 2025-08-22 05:40:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92e2b3f6-5127-393c-afa2-48f4b172209f | -12.98313 | -56.89411 | 2025-08-22 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fc40db08-5a19-3d09-a2ee-a212275d1ca5 | -10.47806 | -67.92014 | 2025-08-22 05:40:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 932e7f95-79d3-3f87-8c74-e48632a2b897 | -13.1434 | -54.91866 | 2025-08-22 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8049af3-d96f-3d54-85e2-58905062aed5 | -13.14189 | -54.92033 | 2025-08-22 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b19ee23f-36e5-38c8-86f4-317d25669334 | -13.43508 | -57.17299 | 2025-08-22 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0e4ebb56-0868-33a0-bf1b-3a4e83acffec | -14.59766 | -54.78295 | 2025-08-22 05:40:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1b09c17e-dbd5-3106-854d-3351197d4204 | -14.7804 | -56.03378 | 2025-08-22 05:40:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 59e70f3d-4751-3c8b-b065-784907f74316 | -14.64664 | -54.91426 | 2025-08-22 05:40:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63ac1c4f-62a3-3c1a-b429-2f2a67373c43 | -14.58841 | -54.75978 | 2025-08-22 05:40:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ab6f209-10d8-31dd-ab51-ec685dff9ab7 | -15.02339 | -54.8586 | 2025-08-22 05:40:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc64dcd8-c2d2-3bc5-9f5e-241dad38155b | -10.37998 | -69.51646 | 2025-08-22 05:40:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fe60d46-9203-379d-b664-5c443741f9bc | -14.64756 | -54.906 | 2025-08-22 05:40:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc4c4245-44ed-33de-b0f7-5d954934ec22 | -15.01045 | -54.8681 | 2025-08-22 05:40:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 284f4c74-c01c-3f0a-a385-a4097a0b1745 | -14.6471 | -54.91013 | 2025-08-22 05:40:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36bf2f5a-49d4-3e54-9b78-f72bea5b4a6b | -13.14295 | -54.92252 | 2025-08-22 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b41fbe15-bd4d-3629-b214-343cf7505a25 | -12.49974 | -53.81184 | 2025-08-22 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02166706-e126-32c2-a08d-89ef6846e75d | -12.98453 | -56.88257 | 2025-08-22 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 39349c96-f4e9-3ffb-9a9e-e5aa51563b2d | -12.9828 | -56.89351 | 2025-08-22 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1199f2a1-3dd9-3057-88a4-9e5445fa6370 | -15.02687 | -54.86475 | 2025-08-22 05:40:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e803b544-d5b4-3410-a2d5-fcf1d5fdaf73 | -12.98779 | -56.89407 | 2025-08-22 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fa0b73a-9023-3e27-a466-a9e1c3825134 | -13.32688 | -54.39892 | 2025-08-22 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9601eb17-8794-3496-839e-bcfc91ea364d | -14.62523 | -54.85217 | 2025-08-22 05:40:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2e9d9b3-4791-3fbc-af62-25ea4d7712f5 | -14.99384 | -54.85745 | 2025-08-22 05:40:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29492d6b-ad38-34a4-8d22-6851c052aa7a | -14.62255 | -54.86537 | 2025-08-22 05:40:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 20482a56-6214-3ba6-885e-b1325a59b97c | -14.7625 | -55.99917 | 2025-08-22 05:40:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a18a3ec-ad52-3862-94e7-654ecd98ba0c | -14.78645 | -59.65775 | 2025-08-22 05:40:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1e50f2f-22f6-37c8-b3e8-9b05bb4dd013 | -12.99023 | -56.87741 | 2025-08-22 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdf8b567-5082-37f8-89c2-68f43db4dcbf | -12.49311 | -53.81582 | 2025-08-22 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ad3e61c-44fa-3169-b5ee-0c94e19a450c | -14.78541 | -59.66579 | 2025-08-22 05:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 42752f57-f676-32ae-8940-dc248238f17e | -12.99523 | -56.87799 | 2025-08-22 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d72397e3-fd31-36a7-9bea-86a1380d3d35 | -14.63151 | -54.84901 | 2025-08-22 05:40:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ce333b4-1f84-3c44-8777-bc6c84635d58 | -14.62387 | -54.85337 | 2025-08-22 05:40:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d5fbe08-f55c-3976-aba1-fd2010480485 | -14.63205 | -54.84443 | 2025-08-22 05:40:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7585e0e-dbb7-327f-872d-492f8a9406d1 | -12.99354 | -56.88885 | 2025-08-22 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99ad080d-8c5f-33b6-b940-774e7fea4bc2 | -14.78082 | -56.03027 | 2025-08-22 05:40:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 85c52a27-51ed-3368-80c5-331f3ec1fab8 | -12.99429 | -56.8831 | 2025-08-22 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01ebdb7f-a785-3f2b-8c7d-35ffca666e80 | -12.97883 | -56.88777 | 2025-08-22 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 10185a77-19b5-3aa0-994e-d301607da3f7 | -14.79071 | -59.6582 | 2025-08-22 05:40:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b746c49-1405-32d9-a54a-89fd244e2baa | -14.78124 | -56.02674 | 2025-08-22 05:40:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b3737086-8b86-3742-be15-5b1b69df031b | -13.14236 | -54.91648 | 2025-08-22 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 442df6c4-306b-326d-82e0-1e84c5209cb6 | -12.51507 | -57.65598 | 2025-08-22 05:40:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 773ba1d2-c15f-303e-a22e-d3e73243f62d | -13.43578 | -57.16742 | 2025-08-22 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README60.md)
