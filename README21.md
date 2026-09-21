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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2147bb9c-ea00-364f-a892-c92bfe5da6e6 | -6.91224 | -42.93695 | 2026-09-21 04:00:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c7eca601-7c9a-3459-aeaf-d32c589ed0ef | -6.97882 | -42.16946 | 2026-09-21 04:00:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e53be140-2299-3787-bf99-a922fafe6f9f | -3.4115 | -39.2855 | 2026-09-21 04:00:00 | NPP-375D | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| acc638d2-e1ab-38f0-a1c8-3a4e1dd95846 | -6.55472 | -45.58187 | 2026-09-21 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f5f0fe00-4f29-3705-8885-ba3c8dfe553d | -3.64229 | -40.58848 | 2026-09-21 04:00:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fb3d32f2-97ea-3ac1-8987-ddfe7260380f | -8.38849 | -37.64488 | 2026-09-21 04:00:00 | NPP-375D | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| aa92ab91-dd5a-32b4-a2ee-68752a6dfeca | -6.90954 | -43.73651 | 2026-09-21 04:00:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa532324-b4e5-38eb-bb79-d63cb84f645e | -6.27137 | -41.65497 | 2026-09-21 04:00:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cb0e978f-6ca7-35ab-b20b-3be301cd57ef | -1.90427 | -45.80703 | 2026-09-21 04:00:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 89494ccb-aaac-3987-8962-82508f8cc9b5 | -6.35914 | -43.36197 | 2026-09-21 04:00:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8a490575-5194-349c-a266-fba27623c248 | -6.9732 | -42.58408 | 2026-09-21 04:00:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e5f534ec-e0f2-3ca6-838b-7f19cbeb5b98 | -1.90362 | -45.81085 | 2026-09-21 04:00:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6ac83d17-289f-3ec5-ab5f-a46413949bf7 | -6.89186 | -41.7004 | 2026-09-21 04:00:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 60bb6046-b560-3eb8-af0b-e90e962be240 | -6.37592 | -35.15697 | 2026-09-21 04:00:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d6e078e5-f1a2-34ba-a1a7-05aac50fac5a | -6.83241 | -46.04462 | 2026-09-21 04:00:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b2b88f9-9abc-37e6-a0b7-a42a0226e178 | -6.99441 | -42.20261 | 2026-09-21 04:00:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 81521b56-0d39-379a-a18a-176a794c82ec | -6.90504 | -42.92714 | 2026-09-21 04:00:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 07c24e12-4957-36e1-a628-ac1013e62d4f | -4.83043 | -43.5242 | 2026-09-21 04:00:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38b99a23-5661-371e-ac90-d25e1783e9c7 | -6.36286 | -43.36736 | 2026-09-21 04:00:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 6b34b044-c53f-3a2c-8911-51f28ce5168a | -7.2429 | -39.35805 | 2026-09-21 04:00:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cd170219-ca59-3ce8-a007-21c9bcc2c3df | -6.9133 | -43.74203 | 2026-09-21 04:00:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a08cec43-1cee-3958-8a47-95313c942877 | -6.90385 | -41.70228 | 2026-09-21 04:00:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3aaec08a-b9f5-3fd4-a2da-5714c4f7876f | -6.57107 | -42.5614 | 2026-09-21 04:00:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| e515a666-a363-3589-bd80-264fa698336d | -1.35898 | -49.30496 | 2026-09-21 04:00:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 96caefbf-4ab2-3768-885e-e48b27d80d93 | -3.6393 | -40.58225 | 2026-09-21 04:00:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 25507501-cd72-3d1c-94b5-54c19cf0bd8b | -6.56104 | -45.54654 | 2026-09-21 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31621da0-9630-3787-8f78-3477cddd6b2b | -6.91491 | -43.73268 | 2026-09-21 04:00:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e271e65b-adf0-3cba-be97-c63e062782c8 | -6.99573 | -43.36997 | 2026-09-21 04:00:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d7d44906-7fc1-30c8-9657-49c5a05a91c7 | -6.83833 | -46.04235 | 2026-09-21 04:00:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 96377463-c877-33bf-8c71-8b74d6ed6409 | -6.37251 | -35.15646 | 2026-09-21 04:00:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 890325bb-854b-3e81-9923-656a51c0a8a9 | -8.39126 | -37.64892 | 2026-09-21 04:00:00 | NPP-375D | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 914ccf90-e375-3829-a803-afebc1a2dca5 | -5.66362 | -42.63576 | 2026-09-21 04:00:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| aaa424f4-f214-3827-8f48-4a9b3f8eb527 | -6.36362 | -43.36284 | 2026-09-21 04:00:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 99493356-e3d9-38e8-a672-c607bcb76e3a | -6.35759 | -43.37116 | 2026-09-21 04:00:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5f58b689-679f-383b-8269-a817c7a50c34 | -7.03099 | -42.07656 | 2026-09-21 04:00:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3bce988b-2262-3d4e-b34a-542055287b23 | -7.10162 | -42.08072 | 2026-09-21 04:00:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b1692087-a9de-3cae-93a3-89df9432602e | -6.57176 | -42.55735 | 2026-09-21 04:00:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1d945f20-dc93-3786-a999-5d865d508296 | -6.47398 | -48.44636 | 2026-09-21 04:00:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bddfcd14-ca81-3c79-95c4-fb02509f6729 | -6.32456 | -43.37476 | 2026-09-21 04:00:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9c527b44-cf9f-3db8-9273-46d058329f88 | -6.98231 | -42.17382 | 2026-09-21 04:00:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 354ec298-5a06-3f2b-813b-2a807abb9a66 | -1.90997 | -45.80796 | 2026-09-21 04:00:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a0ade2e8-7dbb-3870-9ffc-ba0c6d46565c | -6.91587 | -42.94173 | 2026-09-21 04:00:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 653c72d3-badc-3a5c-8ef6-cc8a943348b1 | -6.91035 | -43.73186 | 2026-09-21 04:00:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 221b75e9-9126-3285-877d-4d14620c9388 | -6.92021 | -42.94242 | 2026-09-21 04:00:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 652da2af-aabb-3be4-8106-a2c66e519456 | -7.02567 | -42.08306 | 2026-09-21 04:00:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 642f6f34-c06c-3174-b754-331e7e1e42b3 | -6.28526 | -41.7696 | 2026-09-21 04:00:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 452eb2f6-e8e6-3b14-89db-431ec6359dd2 | -5.5964 | -37.83236 | 2026-09-21 04:00:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 488c93ce-a2e3-3a0f-9693-505557575ae2 | -6.56212 | -45.54049 | 2026-09-21 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8db5142f-d6bd-3ce8-91c0-1776c9853e09 | -6.47311 | -42.77229 | 2026-09-21 04:00:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 852a8db9-d216-35a3-bba3-e23762c40801 | -6.97386 | -42.58023 | 2026-09-21 04:00:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fef9a368-9d92-3b0f-9586-6177d6328207 | -5.99358 | -41.04337 | 2026-09-21 04:00:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3fd90214-189b-3144-8e82-36e8a4a9c2af | -6.89985 | -41.70166 | 2026-09-21 04:00:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 881bfedb-e0e3-33cd-8029-d5ca76ddd499 | -3.34436 | -42.76058 | 2026-09-21 04:00:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b046292-8bea-3637-9b63-136813c71952 | -4.59146 | -45.16375 | 2026-09-21 04:00:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42de599f-8ca9-3ddd-99a9-4177a4b02159 | -7.12786 | -42.07421 | 2026-09-21 04:00:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b81b1fa3-f091-38c4-a5b4-911314bb8676 | -7.0321 | -42.07736 | 2026-09-21 04:00:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f1c85b0a-213f-361e-b2f5-285f6a542e0a | -6.28932 | -41.77022 | 2026-09-21 04:00:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3b764aba-f3fb-370e-820e-860403b157ea | -4.1385 | -40.61618 | 2026-09-21 04:00:00 | NPP-375D | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 54c65064-2fe5-37f4-b5d2-0bde202479c1 | -1.90933 | -45.8118 | 2026-09-21 04:00:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b0874732-475e-350e-8b22-5128007a07e8 | -6.89585 | -41.70104 | 2026-09-21 04:00:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 364b8296-d41f-36a3-917d-4fa27ea4fc64 | -6.46922 | -42.7611 | 2026-09-21 04:00:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 57ace44e-fb96-33cc-92b7-9bdafb0d03cb | -2.82561 | -46.71013 | 2026-09-21 04:00:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6493fd40-7ed1-371c-8c60-31b8f98b7290 | -2.17177 | -48.32616 | 2026-09-21 04:00:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f2cbe92-12a7-332c-86a5-b7f85005a927 | -8.39182 | -37.64542 | 2026-09-21 04:00:00 | NPP-375D | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6bc897e6-2e0d-37bf-8714-ea000140d4e4 | -7.03037 | -42.08014 | 2026-09-21 04:00:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b1e7eb3d-6bff-389d-b3eb-51773ebf35fd | -6.88696 | -41.70504 | 2026-09-21 04:00:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f69cb7a9-afc6-3db8-90b6-ab2ab99567b4 | -6.47301 | -48.45156 | 2026-09-21 04:00:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6f9291e1-f2d0-3c31-a66c-eb0bc720726b | -7.34051 | -44.46927 | 2026-09-21 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 903270d6-8931-37fc-a190-1e81d2120733 | -6.90431 | -42.93131 | 2026-09-21 04:00:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 3870cd8a-80ad-3314-87c6-0ce2b0b820b1 | -6.35836 | -43.36657 | 2026-09-21 04:00:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e90eeb15-4e88-30d6-ab64-bb5495e26b10 | -4.33954 | -46.36828 | 2026-09-21 04:00:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb66f456-33cc-36ea-b18f-eed97a1f31cf | -2.82635 | -46.70586 | 2026-09-21 04:00:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8cf03b44-55ab-325e-a8b0-9ea6ef43f0e9 | -6.99497 | -43.37439 | 2026-09-21 04:00:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e204d3a9-2a2f-3251-8d50-4de23e1e88e3 | -7.42403 | -42.11767 | 2026-09-21 04:00:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4e44c1d4-e4db-3799-9377-b0640d215f13 | -6.37649 | -35.15331 | 2026-09-21 04:00:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 411602ce-325b-3f08-b430-d08f7f260ab3 | -3.33794 | -42.7664 | 2026-09-21 04:00:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0b443c87-d2d6-3f2c-baec-770068f48bbb | -4.00138 | -38.98731 | 2026-09-21 04:00:00 | NPP-375D | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 03ce210b-f91c-3afe-b56e-a697383026af | -6.69752 | -43.63332 | 2026-09-21 04:00:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 41e19894-eedf-371b-b94d-3e7e099e59bb | -6.44713 | -48.45126 | 2026-09-21 04:00:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bfde1eb-2148-3fcc-b164-fd5459dd4223 | -6.50131 | -43.89278 | 2026-09-21 04:00:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fbbce87b-6e87-3c2c-ade5-c84e6bc92178 | -6.83293 | -45.55751 | 2026-09-21 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5a2e631-2ec2-3598-bc5d-4f841a125fab | -3.64312 | -40.58337 | 2026-09-21 04:00:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6e028314-50fa-351c-a342-817bee2584c7 | -4.84708 | -40.52044 | 2026-09-21 04:00:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6fe7e181-fed4-313e-b4fa-4eaf0a7ca82e | -2.45592 | -49.22595 | 2026-09-21 04:00:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 19ea75e8-c900-315c-b308-baac9a5649da | -4.00203 | -38.98331 | 2026-09-21 04:00:00 | NPP-375D | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2200e404-6daa-32c1-b49b-3a92342c227c | -4.59201 | -45.16061 | 2026-09-21 04:00:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc2e83b3-27dd-3a91-a968-2a5f9936675d | -6.98036 | -45.81831 | 2026-09-21 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b26f1877-5c76-375a-8f01-77a79da82bc8 | -7.12846 | -42.07062 | 2026-09-21 04:00:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f6d517c2-39f6-3018-97a8-ba510c37b465 | -5.63389 | -40.87297 | 2026-09-21 04:00:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c011847c-6e8f-3d7c-95fc-60da4d82faaf | -6.83844 | -41.02119 | 2026-09-21 04:00:00 | NPP-375D | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 099ea3e0-54b4-3d19-8a69-55b83516dc07 | -4.68077 | -46.41805 | 2026-09-21 04:00:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd1a356a-6e68-3a17-bfb6-fe638ea98d79 | -4.68493 | -40.1441 | 2026-09-21 04:00:00 | NPP-375D | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4d83245e-44c6-3a89-919f-af0addd313c0 | -7.15191 | -39.33911 | 2026-09-21 04:00:00 | NPP-375D | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b2085d3d-8559-3d03-8e2e-586e65d8c7ec | -7.34144 | -44.46394 | 2026-09-21 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6f1e38e8-f8c9-3a40-82b4-39fc4f97ec3c | -7.12306 | -43.72221 | 2026-09-21 04:00:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc94d8de-3c82-336f-86b0-578ae4cf65c0 | -4.11507 | -46.39629 | 2026-09-21 04:00:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47a7a794-5a6c-36ce-a969-ea104edc51fa | -4.59091 | -45.16696 | 2026-09-21 04:00:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a38b413-bf3e-35a1-a874-e94f2e133b8a | -7.42809 | -42.11837 | 2026-09-21 04:00:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 30a3e062-13dc-3aec-8f0e-eae218053ba8 | -6.91572 | -43.72801 | 2026-09-21 04:00:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1ca40b0-8551-3491-9fb2-4e5cd2d277aa | -4.68285 | -46.41737 | 2026-09-21 04:00:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README22.md)
