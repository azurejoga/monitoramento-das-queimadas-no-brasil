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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1c10494-442a-398f-a8b9-99cbbf08f353 | -6.10394 | -45.94538 | 2025-09-14 05:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6aea1c19-c543-3547-aeb2-668dfe880f55 | -6.60918 | -51.0423 | 2025-09-14 05:06:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79fe1b50-1083-3cb8-99d1-372ea5ba70d2 | -6.88552 | -45.63212 | 2025-09-14 05:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4e62e5a-33c7-3419-83cf-7d20598c8061 | -6.67713 | -45.51764 | 2025-09-14 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d319d8bc-4948-3334-a5a7-dc2e01ae8e45 | -5.30175 | -56.10097 | 2025-09-14 05:06:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 25a961f1-8e85-3394-8f4e-129065d0a14d | -5.7334 | -49.3042 | 2025-09-14 05:06:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e9b4a20-679a-3062-9717-0fad315a6eb5 | -7.22467 | -49.31986 | 2025-09-14 05:06:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82562cb8-d082-37dc-a55d-317a1c770e01 | -6.80732 | -51.37804 | 2025-09-14 05:06:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2465735a-7a5c-34ff-a551-de207978bb2f | -1.23728 | -54.1009 | 2025-09-14 05:06:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 92ed4d51-cdad-339c-a9bc-93a7ab70e712 | -5.76654 | -52.36116 | 2025-09-14 05:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86c2a14c-7acd-3eff-a786-39ac30ed65d8 | -3.22476 | -47.13058 | 2025-09-14 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77d3d149-eeac-3045-8d6b-7a749e012528 | -8.14122 | -43.66759 | 2025-09-14 05:06:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7987b589-32ad-373c-86c3-93a4643f4db9 | -3.73347 | -55.94625 | 2025-09-14 05:06:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 205aded2-ca7e-3134-89aa-795f2d1c23b5 | -5.17139 | -46.15879 | 2025-09-14 05:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 201b2bbb-efca-308d-a716-3bda4925f026 | -7.52419 | -47.63956 | 2025-09-14 05:06:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eadcb4f1-bb53-33b6-82c7-753f8180a4b8 | -3.08542 | -49.46058 | 2025-09-14 05:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dc980028-e311-3ea9-9a10-ccb9bcd02225 | -6.98575 | -44.54481 | 2025-09-14 05:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d0ff127-bae5-3a80-87e8-376e6bba0f4c | -3.22834 | -47.62998 | 2025-09-14 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea209ac9-a1c6-354e-9e36-a21b782969ce | -1.4168 | -48.3839 | 2025-09-14 05:06:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| eeda5d37-6295-3b5f-99a1-b5295ed6e90e | -6.3337 | -43.87805 | 2025-09-14 05:06:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee989c39-6a7e-3606-8987-980ccc4baa1c | -6.11995 | -42.95395 | 2025-09-14 05:06:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 49e1134b-0e6f-3f82-bfec-59997083d9a2 | -3.74016 | -55.9473 | 2025-09-14 05:06:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca817db2-62ab-3dfa-a44a-31b410dcf96e | -5.76718 | -52.35692 | 2025-09-14 05:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c42f0287-a0db-3b93-8ecb-495dd694a3e8 | -4.13219 | -48.81225 | 2025-09-14 05:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9eda7de3-ab24-34b6-a6a0-10050ed602e1 | -6.12519 | -42.95522 | 2025-09-14 05:06:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a2eaaf9f-9607-3560-8587-69cd8356f346 | -6.89016 | -45.64114 | 2025-09-14 05:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ab11457-564d-3f22-8ff2-5a49e82e71d3 | -5.77118 | -57.57746 | 2025-09-14 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adac9408-77fe-3db0-8d70-04ca25f4c99d | -3.40653 | -52.72603 | 2025-09-14 05:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afc34b59-6f91-3be1-9ffc-d4d4acc994e8 | -6.88486 | -45.63692 | 2025-09-14 05:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f00ff7dd-63a2-3e4a-aed8-54a71a50f316 | -3.21863 | -47.63099 | 2025-09-14 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 82f119ad-b0e6-3be2-a22b-95d59616fd25 | -8.13857 | -43.66175 | 2025-09-14 05:06:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adbb1f08-707a-34b1-a970-ea6a453507b5 | -8.14446 | -43.66865 | 2025-09-14 05:06:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4897cded-6c3a-3c79-8b93-02b4a005cdd2 | -3.76443 | -52.06267 | 2025-09-14 05:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fe81585a-8a1f-36c8-bda0-a3d6d11232a9 | -1.23011 | -54.12463 | 2025-09-14 05:06:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0c236310-5ba4-3fca-a821-a1a8bc095d07 | -6.99086 | -44.53872 | 2025-09-14 05:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b1c621d-0bad-3718-ab21-fbc54af22bdf | -6.33221 | -43.87706 | 2025-09-14 05:06:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d17bebed-8ae5-3dc4-9d93-22b723c0c366 | -3.20957 | -49.10505 | 2025-09-14 05:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d6d7600-3b34-36b5-bcba-bf26d7a55c32 | -7.5195 | -47.63585 | 2025-09-14 05:06:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 883fcf5a-58c6-30f5-be2b-030649df5682 | -5.20483 | -44.31268 | 2025-09-14 05:06:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 119f025c-4f10-3fc5-a0ab-f647b5c2ceec | -6.98641 | -44.54007 | 2025-09-14 05:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 503afa94-4629-3b7d-81c7-525ff20f4d2e | -5.79545 | -43.89244 | 2025-09-14 05:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9be71be4-cf03-3c56-973c-a331ee45f0f8 | -5.79765 | -43.88836 | 2025-09-14 05:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f8422d4-9686-3c08-99af-99c4a808190c | -3.85345 | -52.16376 | 2025-09-14 05:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4650c004-7583-3869-9a91-1747e902af34 | -3.21488 | -47.12906 | 2025-09-14 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1b1b30db-449b-3bc0-8afa-4f91d962ed6b | -6.98335 | -44.54773 | 2025-09-14 05:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fbf2103-498a-3027-8a94-aea5646685b2 | -7.52969 | -47.63732 | 2025-09-14 05:06:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 256191e6-1055-330a-a26d-aa64900306f1 | -3.60752 | -51.04691 | 2025-09-14 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7b4ee54-4a41-3a98-890b-ff32ff832894 | -3.22278 | -47.63436 | 2025-09-14 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39163cfe-b714-3c7b-bb31-b3eaed5859c1 | -3.0072 | -47.83908 | 2025-09-14 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d3853f9-305d-3157-8c02-ad3f4bace657 | -3.73403 | -55.94276 | 2025-09-14 05:06:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 622cf541-7cee-3c06-8daa-dd1fe3939bb9 | -6.87888 | -45.63766 | 2025-09-14 05:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17eb2850-9d4a-3daf-a877-16465b86d166 | -1.23673 | -54.10436 | 2025-09-14 05:06:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96bf7c70-5c9d-32c6-a329-cca886c757f7 | -3.3221 | -54.90824 | 2025-09-14 05:06:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd93ace3-bce4-322b-9cf9-f2da867181b9 | -3.87036 | -52.38707 | 2025-09-14 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ba69c4f-a5c2-3b33-a935-5cccb8e4a385 | -6.80805 | -51.3731 | 2025-09-14 05:06:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5aed1050-062b-3ee5-b039-075b1e2723c4 | -5.76773 | -57.5769 | 2025-09-14 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccf09e84-1c12-3bac-844c-6a0d77b23c77 | -4.86518 | -49.3319 | 2025-09-14 05:06:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a5fc95c-d723-37a4-a596-abd88604aad5 | -3.59989 | -47.5234 | 2025-09-14 05:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 79da4054-37bc-34a5-b78e-2d6f0d7cd071 | -3.59583 | -47.5174 | 2025-09-14 05:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 162d3a64-b9ae-35c7-b072-37655530aacf | -1.9772 | -47.98045 | 2025-09-14 05:06:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8687bc9f-7289-32d6-a6ff-a692ce18d785 | -6.50681 | -52.23205 | 2025-09-14 05:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff539e81-76c0-340c-8d49-3e486b5dd83f | -6.98899 | -44.55274 | 2025-09-14 05:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99fa54a6-7a02-3585-875b-d9640ca11268 | -5.32547 | -55.88712 | 2025-09-14 05:06:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4c21d42-12e3-326c-aed2-c9e5a9ebce17 | -7.47856 | -46.12275 | 2025-09-14 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 468ee95a-c75b-33e8-81c1-52c77a81ad98 | -3.59506 | -47.52264 | 2025-09-14 05:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 73a973f5-4399-3c03-b5f9-765293a23856 | -6.3329 | -43.8721 | 2025-09-14 05:06:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0989a5ff-b83c-38df-8b69-8b1b439184f4 | -1.42121 | -48.38454 | 2025-09-14 05:06:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| badb69a7-a0b4-34d4-a805-1a1bd7c7eadd | -3.80955 | -52.08237 | 2025-09-14 05:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43ad97da-1dbf-3ff6-8147-217a834d7f3d | -6.14016 | -55.78809 | 2025-09-14 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a865b18-7a5d-38c2-9eeb-4e00a9702132 | -3.22559 | -47.12504 | 2025-09-14 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7684487c-344e-316a-93c2-2bb1038187e7 | -5.96653 | -43.21975 | 2025-09-14 05:06:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9e049d51-252d-36d9-909b-4434d38fdf8c | -6.1167 | -45.9359 | 2025-09-14 05:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e476600-d79a-3a01-9cf1-d81081b0baba | -3.32488 | -54.91221 | 2025-09-14 05:06:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36b65d03-5b7e-31b0-936d-84e1fe041f84 | -3.21982 | -47.12981 | 2025-09-14 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e6382da0-5916-3e13-9409-99296ad3cd74 | -5.7702 | -52.3617 | 2025-09-14 05:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8818c5c7-8308-3abf-9529-3a3ea7ce144b | -7.47805 | -46.12647 | 2025-09-14 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 75cc8371-a508-3d41-9bfe-b66d249a0df1 | -3.80033 | -47.58356 | 2025-09-14 05:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ba3087f-f709-3d3d-a936-81a2ec5a5979 | -6.56233 | -50.87771 | 2025-09-14 05:06:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1eeda10b-1a87-3315-988c-da51ad86a47b | -5.79699 | -43.89322 | 2025-09-14 05:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00f87534-101d-30c2-b205-456ec261db5e | -4.50839 | -55.70802 | 2025-09-14 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31718e92-6658-3b72-8f69-f961fc9d6d8f | -3.21804 | -47.63344 | 2025-09-14 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec013e3f-d7b7-3843-b07b-6338ad502adb | -6.80341 | -51.37744 | 2025-09-14 05:06:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c031630d-1823-338c-841d-7887b06f19de | -6.11618 | -45.93953 | 2025-09-14 05:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 412a7988-bfba-381b-87b5-e0d7a6f99fc2 | -5.76782 | -52.35267 | 2025-09-14 05:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa40b8d0-ea59-331d-943c-e34f4c899273 | -6.56179 | -50.8813 | 2025-09-14 05:06:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93d444ee-267b-3e24-93ca-6a2f2c18d4ee | -4.13155 | -48.81657 | 2025-09-14 05:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4c457f62-d3c1-3925-96d0-7e1eb6a0f636 | -3.59099 | -47.51667 | 2025-09-14 05:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9846c2d3-7e8c-34fe-919b-366cfcb71d8b | -6.99024 | -44.54335 | 2025-09-14 05:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb41ec5d-3543-32da-a7a2-c2985720573e | -5.96886 | -43.22 | 2025-09-14 05:06:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 095a3784-df7b-35dd-8e73-bbaf3d232c47 | -6.98509 | -44.54951 | 2025-09-14 05:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f57340f-ffb9-3cb2-8140-89f073ad58e2 | -7.3778 | -44.35251 | 2025-09-14 05:06:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c020985-58d1-37fe-b2d9-60c0a30f33e4 | -6.33503 | -43.86813 | 2025-09-14 05:06:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8be08adb-6c60-31da-805b-858614b032da | -7.37717 | -44.35722 | 2025-09-14 05:06:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83df34cd-6ab5-386e-8bfb-b072c5cd1724 | -6.1267 | -42.95498 | 2025-09-14 05:06:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3a131d84-c40e-3f92-bbed-e06e18204442 | -4.41436 | -47.60839 | 2025-09-14 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5a5b8304-6f92-3112-956a-1e66c7833a4f | -4.57907 | -56.24857 | 2025-09-14 05:06:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 979ca297-f51c-3d14-869f-07d7cb141c17 | -1.22679 | -54.12411 | 2025-09-14 05:06:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7fcada71-a52b-3dfb-a933-ce84ea3afb98 | -13.89584 | -48.30262 | 2025-09-14 05:08:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1cc3d58f-c8bf-3d27-b121-6c68b9d7d158 | -14.47609 | -47.32214 | 2025-09-14 05:08:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1cdf88f5-0010-3fc9-9fe3-3916f81c71ff | -8.10975 | -50.16694 | 2025-09-14 05:08:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README54.md)
