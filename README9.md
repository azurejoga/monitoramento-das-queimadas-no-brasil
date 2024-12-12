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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46a52da0-5f98-3ec7-a15d-c609a956b713 | -14.7655 | -52.6446 | 2024-12-12 02:20:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 6e8f2800-6f1a-3edc-acd0-9561afeb91e6 | -18.0464 | -52.9582 | 2024-12-12 02:30:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 88.1 |
| dd70df35-d949-3009-baa7-4c6315192f44 | -18.0659 | -52.9766 | 2024-12-12 02:30:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 75.5 |
| eb9dc532-92d0-3777-bed1-811d5c1b131e | -3.2502 | -46.8929 | 2024-12-12 02:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| f03c08e6-23c6-3550-88d0-d03d14df2978 | -18.0456 | -53.0013 | 2024-12-12 02:30:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 86.6 |
| acc02b6f-d393-360d-a5dd-dc4f26f77a90 | -11.2148 | -53.833 | 2024-12-12 02:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| d93be973-4278-3f7a-bbd0-3346bc95b9cf | -3.2503 | -46.8709 | 2024-12-12 02:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 119.0 |
| e9334dd8-309b-328a-aeb8-2f9d599f01c2 | -18.0663 | -52.955 | 2024-12-12 02:30:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 745fe6ba-1bbc-3479-9805-953ab63daff7 | -18.046 | -52.9798 | 2024-12-12 02:30:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 175.1 |
| a1d455ec-2905-3b85-862a-e3b665771b1b | -13.6933 | -54.7555 | 2024-12-12 02:30:00 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 53bf55ea-512d-3205-9412-9d1584f2b58e | -3.2317 | -46.8716 | 2024-12-12 02:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 47330ed2-741c-32b8-8e92-5c8758124665 | -18.0261 | -52.9829 | 2024-12-12 02:30:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 2fb624f3-e807-3c51-9977-88304de93913 | -11.1959 | -53.8348 | 2024-12-12 02:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 0b1f3e69-842b-37ca-876f-25b87b237143 | -6.9161 | -43.4952 | 2024-12-12 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 69addc7d-86fe-34ae-ab59-ae94117ca3b9 | -6.9344 | -43.5401 | 2024-12-12 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 204.8 |
| d3a0f64e-0dc4-35e0-a20e-4041b057459f | -11.2148 | -53.833 | 2024-12-12 02:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| f1f25029-6624-3c94-b3c0-9f388ba9124e | -18.0261 | -52.9829 | 2024-12-12 02:40:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| d5bed942-81e9-3f25-9fa4-0cc8a67b8bda | -6.9158 | -43.5185 | 2024-12-12 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 419.9 |
| 84f4eacc-e297-3498-be4c-73d5cea5b461 | -6.9156 | -43.5418 | 2024-12-12 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 175.7 |
| de4c1aba-807f-3a6a-855e-4d20dd9f3127 | -18.0456 | -53.0013 | 2024-12-12 02:40:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 1da42be3-c0e6-3b83-9993-d3453c172e6a | -3.2317 | -46.8716 | 2024-12-12 02:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| d72283ec-4516-303d-894c-76dddc9bfddc | -18.046 | -52.9798 | 2024-12-12 02:40:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 0a6dd37f-488a-3ce1-a3dc-9b5d2ab56216 | -11.1959 | -53.8348 | 2024-12-12 02:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| e6398491-16f9-3f03-bfbd-c0c0a0a9f4ce | -3.2503 | -46.8709 | 2024-12-12 02:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 127.6 |
| 7bd69f55-3138-34c4-ab0a-0103aae0a1e7 | -6.9346 | -43.5168 | 2024-12-12 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 475.8 |
| cd81b503-583e-3dfc-acba-a1953e0bcc00 | -18.0663 | -52.955 | 2024-12-12 02:40:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 36958c8a-4847-38ac-953f-2f7f98f254a4 | -18.0659 | -52.9766 | 2024-12-12 02:40:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 06245fb9-4f33-395b-90b9-d21228da407f | -11.2151 | -53.8125 | 2024-12-12 02:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| e9be194f-0ab2-3508-b06e-431eefe63f4d | -1.8788 | -54.6908 | 2024-12-12 02:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| cd2fd69d-b0fd-3f45-bc88-b1c45c2bfd7c | -6.9349 | -43.4934 | 2024-12-12 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 117.9 |
| c67ca1f7-bd51-3f71-b693-e32a43e21cf9 | -3.2502 | -46.8929 | 2024-12-12 02:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 37fac683-d713-3bb9-89d6-8fe3d26bfea7 | -3.2502 | -46.8929 | 2024-12-12 02:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 487b7af7-f325-3f77-841c-7fa8fa5bb9d3 | -6.9346 | -43.5168 | 2024-12-12 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 560.8 |
| c1f8fe13-db79-3fd2-ac57-e302e9118d25 | -6.9344 | -43.5401 | 2024-12-12 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 195.7 |
| 5bb15270-eb6d-36ba-857e-0898590502eb | -5.9185 | -48.0449 | 2024-12-12 02:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| f023060e-e604-34ed-bb98-7a1b8e10189c | -6.9156 | -43.5418 | 2024-12-12 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 6d69b28b-c4cd-3400-990b-292d3ec1aec7 | -6.9161 | -43.4952 | 2024-12-12 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| edc5775d-5156-357c-89b7-d83f5eb83b4e | -11.2151 | -53.8125 | 2024-12-12 02:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 968c59c4-7e8f-30f7-bf23-31fe6a5f3949 | -11.1959 | -53.8348 | 2024-12-12 02:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| f0100c2e-5f8a-3b05-ac3c-805479178335 | -6.9158 | -43.5185 | 2024-12-12 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 353.5 |
| f7d49cfc-475b-3c8d-bff0-3cfc9b0b94db | -3.2503 | -46.8709 | 2024-12-12 02:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| ef08d1cf-1d45-3bbe-a2a2-e972a765ff88 | -6.9349 | -43.4934 | 2024-12-12 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 118.8 |
| d29154d7-1029-3263-912e-0066c5cff1ea | -5.9369 | -48.0654 | 2024-12-12 02:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 5ce29437-3d71-3a10-bcde-cc35bcdc6b50 | -5.9183 | -48.0667 | 2024-12-12 02:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| a5117a64-44fe-3670-8dd9-66c5f6055629 | -11.2148 | -53.833 | 2024-12-12 02:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 2c03710a-b927-3bdd-8e1d-6a4f2b6a18dd | -5.9371 | -48.0437 | 2024-12-12 02:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 96bfb109-15ef-3d0a-92f2-04e57539a6a1 | -6.55007 | -35.20413 | 2024-12-12 02:57:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 0fbb4a90-15f5-3caa-9072-859f9e6a11b6 | -6.54645 | -35.18954 | 2024-12-12 02:57:00 | NPP-375D | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| ae8688a0-cef9-38e6-8fe9-c1f13116bfb2 | -7.74583 | -35.15028 | 2024-12-12 02:57:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9878dd18-4fbf-3a06-b3e2-c37092b34aef | -6.54561 | -35.19423 | 2024-12-12 02:57:00 | NPP-375D | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 59.5 |
| 044b7806-9e76-3da7-ace4-76a4b94253b2 | -6.5448 | -35.19875 | 2024-12-12 02:57:00 | NPP-375D | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 59.5 |
| af01487b-84c7-32a6-8f61-4ed3cab1583b | -8.34792 | -35.02477 | 2024-12-12 02:57:00 | NPP-375D | CABO DE SANTO AGOSTINHO | PERNAMBUCO | Brasil | 2602902 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 64393f76-d85a-3a4b-82b7-f23133764c7c | -7.75172 | -35.15136 | 2024-12-12 02:57:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| c07ea49b-85d8-3249-903b-4a768f6d15f3 | -6.55088 | -35.19958 | 2024-12-12 02:57:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 59.5 |
| d2aba4ec-bda3-3c15-9473-bfd8a7dcf427 | -6.55772 | -35.19621 | 2024-12-12 02:57:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| fdd5dbb8-9931-3988-a448-e256b4ce6f6d | -8.37661 | -35.32841 | 2024-12-12 02:57:00 | NPP-375D | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e2b281da-5563-30f0-b2fa-1beabbf5939a | -6.55089 | -35.20353 | 2024-12-12 02:57:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| e878b53c-54a0-3a7e-968a-05c18d705b31 | -7.69807 | -35.25862 | 2024-12-12 02:57:00 | NPP-375D | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 76a13978-1756-3240-8c42-81f7092cd4d6 | -7.74808 | -35.15219 | 2024-12-12 02:57:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d2942548-2b11-345f-bc19-817c9c32e669 | -9.39227 | -38.88084 | 2024-12-12 02:57:00 | NPP-375D | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7b1461c2-e40a-3376-8687-50695a2f4ffe | -6.5585 | -35.19181 | 2024-12-12 02:57:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ddd1fe6d-ff5f-35cd-aa4b-0e2ad1ce376c | -6.55251 | -35.19047 | 2024-12-12 02:57:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 210a36c4-283e-391a-ba18-06776d64ca42 | -8.91646 | -35.23378 | 2024-12-12 02:57:00 | NPP-375D | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 01b9aa15-5535-377f-b4b8-d8d25b67561b | -8.91771 | -35.23406 | 2024-12-12 02:57:00 | NPP-375D | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7874f281-69c9-3e69-be58-a234a000be25 | -6.55342 | -35.18992 | 2024-12-12 02:57:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 44cdf1f2-4539-367f-9ac5-bdbbce00c8dd | -8.70168 | -35.1447 | 2024-12-12 02:57:00 | NPP-375D | RIO FORMOSO | PERNAMBUCO | Brasil | 2611903 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 056409f9-c155-3de2-961d-881b7adb0e83 | -6.55173 | -35.19899 | 2024-12-12 02:57:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 171.7 |
| 26119092-aaff-3200-82ee-3bb9c609e342 | -6.55331 | -35.18597 | 2024-12-12 02:57:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| ca6d25c6-8736-3c64-b848-221a106b3e21 | -8.34867 | -35.02073 | 2024-12-12 02:57:00 | NPP-375D | CABO DE SANTO AGOSTINHO | PERNAMBUCO | Brasil | 2602902 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2fd81ef1-0e87-3a8a-8250-57524cfcf94d | -6.55425 | -35.18545 | 2024-12-12 02:57:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 1127d303-e2e0-3c3e-a938-fe0da1260b24 | -7.74888 | -35.14776 | 2024-12-12 02:57:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c0fb95d4-b552-322a-a29f-51ebc47895fc | -8.70243 | -35.14068 | 2024-12-12 02:57:00 | NPP-375D | RIO FORMOSO | PERNAMBUCO | Brasil | 2611903 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f9207345-5750-36df-b40d-ef2b0c9c7c1c | -9.38515 | -38.8793 | 2024-12-12 02:57:00 | NPP-375D | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 31fe7c60-30bf-3fcb-a3dc-d18ba6dcd8ad | -18.0668 | -52.9335 | 2024-12-12 03:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| cdb2c048-1ebf-3768-b9ed-2b6eeabdb63f | -3.2503 | -46.8709 | 2024-12-12 03:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 5f561a4e-e5a9-30b5-8c1a-453e5bd1b773 | -6.9344 | -43.5401 | 2024-12-12 03:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 256.5 |
| 5a4672ad-cd10-329e-b4d9-d4578d43cbf6 | -6.9161 | -43.4952 | 2024-12-12 03:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 72ae1731-5c45-3b38-8be5-049cfa22e9cf | -18.0659 | -52.9766 | 2024-12-12 03:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 183.4 |
| bf659237-0a21-3a75-9b79-3f4c43fdfc3e | -1.8788 | -54.6908 | 2024-12-12 03:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 3f1a3568-86c6-3676-ab14-b7ef06dc1d4d | -6.9158 | -43.5185 | 2024-12-12 03:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 254.8 |
| f052aa88-9a0c-3953-ac0a-dc6657207dc3 | -14.7461 | -52.6471 | 2024-12-12 03:00:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 1afbe6ea-1619-3588-805c-be56cf695244 | -3.2317 | -46.8716 | 2024-12-12 03:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 0c52e4f5-e0d4-3d50-97ad-0b521b807ac5 | -14.7655 | -52.6446 | 2024-12-12 03:00:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| a4060df1-d9b7-3d6f-860f-f9f0b0c1ed0b | -6.9156 | -43.5418 | 2024-12-12 03:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 9931c050-3639-359b-b90d-9075959d7e28 | -18.046 | -52.9798 | 2024-12-12 03:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 164.3 |
| e9e45dd6-f77e-3c17-babc-cad10a131dd3 | -11.2148 | -53.833 | 2024-12-12 03:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 3760733f-8e7c-352d-803b-e5e599ac2cd8 | -18.0456 | -53.0013 | 2024-12-12 03:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 90.5 |
| ac418a66-e817-3bee-9a81-2ff137a72866 | -6.9346 | -43.5168 | 2024-12-12 03:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 545.6 |
| abbe4fbf-3658-368e-9b58-7d047138a19c | -11.1959 | -53.8348 | 2024-12-12 03:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 55b75cb3-c8b6-320f-bd09-943e13b07057 | -14.7457 | -52.6683 | 2024-12-12 03:00:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 530acd24-1ac2-3c36-830f-189385dadff3 | -14.7651 | -52.6658 | 2024-12-12 03:00:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 6815d6d8-7abe-33f0-b86d-38ac83ba4694 | -6.9349 | -43.4934 | 2024-12-12 03:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 132.1 |
| ef84e711-2bf9-3a33-91d0-1d1011961a6d | -18.0464 | -52.9582 | 2024-12-12 03:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 104.0 |
| c2c96b07-b63c-313d-9f5a-75804879a81d | -18.0663 | -52.955 | 2024-12-12 03:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 232.7 |
| 0a117a09-2f24-3f3e-8bc5-7e99bce14235 | -3.2502 | -46.8929 | 2024-12-12 03:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 93b25612-29ef-33fa-b925-37f472d15705 | -6.92 | -43.52 | 2024-12-12 03:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 00d417dc-3f99-3d5a-9425-baa3750e0dc4 | -6.95 | -43.52 | 2024-12-12 03:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| da983d46-1e3c-3c77-ae3d-979098f5d71f | -6.92 | -43.47 | 2024-12-12 03:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d8c50850-69aa-33ac-947b-d49b73d0657b | -6.93 | -43.56 | 2024-12-12 03:00:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8ed969aa-d4ef-3de3-9188-fe317f3c2231 | -18.0456 | -53.0013 | 2024-12-12 03:10:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 84.0 |


[Clique aqui para ver as próximas entradas](README10.md)
