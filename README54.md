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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f71e29b-189b-3990-b809-57b8ebe08e82 | -6.11951 | -57.69284 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca6841bd-8749-3b75-b9e6-966217f3bc3c | -6.8798 | -56.50962 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2873951b-d3e9-399b-bbfb-2b3931fd975a | -4.94914 | -47.65646 | 2026-09-01 05:16:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9400bfe8-06f8-30df-b8df-07a2e29c8a47 | -10.03087 | -44.69426 | 2026-09-01 05:16:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cd935b9e-db9f-319b-ac9b-5733142f1d48 | -6.24951 | -55.4306 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd674a77-c21f-3406-abbd-b5fa59922b04 | -8.27715 | -54.92517 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7fbf6987-4b0a-386e-b5e6-e976a09f1fc5 | -7.25704 | -61.10931 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b52b4fe-748f-399b-a76e-f9d6e4bded19 | -7.02772 | -55.64245 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4db4c210-b923-3c98-834c-8fac4f348842 | -6.22578 | -55.4945 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7de6caa2-b5b1-32bb-b903-37ea908e4883 | -9.47145 | -57.02684 | 2026-09-01 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c153ada9-ace4-3bfe-9ea3-0831756cc9ca | -6.96016 | -55.64257 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e84c817c-bf79-39bc-9cb3-596ce6f351d5 | -7.34878 | -60.58643 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f648e792-5682-37a7-927e-2af22da00d2d | -6.93466 | -55.63141 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b427aa2-3cac-37a4-9fd9-f4ff5638be70 | -10.0233 | -44.69221 | 2026-09-01 05:16:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 03229dcb-713a-35a6-8496-2261548c360a | -10.78146 | -50.5065 | 2026-09-01 05:16:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3b8a79e-394a-3580-a52a-95877c511360 | -7.35821 | -60.57799 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 256dfdd8-5e42-3c67-8bd4-3f677c577e4a | -3.11936 | -61.23739 | 2026-09-01 05:16:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2c1faea6-d33a-3d9c-9111-e5dfafc9fee7 | -7.40108 | -55.15553 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16ded19d-61ac-345f-9f78-3bc76123ff54 | -5.95985 | -57.68214 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3ffffd70-0348-31fd-99e4-9e960a7087f4 | -7.19228 | -60.68054 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 159230f9-dc6c-3c04-b40f-798269837b50 | -11.48618 | -45.10223 | 2026-09-01 05:16:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 217f067a-84d1-3c6c-8655-b835225508da | -6.70227 | -63.18606 | 2026-09-01 05:16:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb0c81b8-28d8-3c11-b78b-593d4e55dcb7 | -6.13469 | -55.64008 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 059e23da-670e-3120-bffa-fbb1ccc0e1ea | -6.95073 | -55.63752 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5c206ab-f1c0-3428-8f6a-32bccf832e4f | -8.61149 | -54.81633 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ad671ff-b0eb-335a-a2be-de8b665f9fb1 | -6.81813 | -59.4449 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a3efac1e-3080-3596-b358-f960369d980b | -7.41036 | -48.00573 | 2026-09-01 05:16:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 630a57dd-c339-30d6-92ef-f50781657406 | -3.547 | -54.71737 | 2026-09-01 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fccece0-f627-3ae8-a365-ed0d0e17e036 | -10.02901 | -44.69868 | 2026-09-01 05:16:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb0eb246-4139-32e4-bd8e-77fdea70a46b | -8.21352 | -54.93377 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 777d293c-a04e-3fb2-83a2-25ee3c878b46 | -7.68784 | -55.34105 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b4ed2e9-f896-3b61-8c95-dc9139012ab6 | -4.2927 | -49.10374 | 2026-09-01 05:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5f793fd-26bc-3272-868c-ca60d45575eb | -7.56681 | -61.36954 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8798d44-455d-3f89-a3f5-47aba29797bb | -7.58759 | -60.47607 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| c93fab52-1301-3a59-ace1-972bf990d5e6 | -6.79575 | -59.3968 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| be5522c3-67db-3f65-8f31-2be973eb016d | -5.2497 | -55.88633 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ced84f5-ded8-36a1-8321-33ed5691b15a | -8.12799 | -54.96473 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7a5e0a42-c54b-3a23-b263-99c40d980fe3 | -7.28723 | -49.8336 | 2026-09-01 05:16:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1481aae5-c687-3278-9828-a7ade9f18924 | -3.62017 | -60.55796 | 2026-09-01 05:16:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0f926760-b1a3-3e97-b835-b6b15c575c37 | -3.65744 | -58.9104 | 2026-09-01 05:16:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5b836478-77fd-30c5-8646-aa1bcad58431 | -6.91649 | -55.7034 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd35687c-3574-3f1f-9299-c2f26e8571ea | -5.88991 | -57.75192 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c3faf6f-645f-3f96-9bdb-3b09d5422bda | -6.20627 | -53.58934 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9249cb95-f85a-30c2-8ab8-72f39f8e1401 | -5.25026 | -55.90417 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8ab3840-f1b7-30f6-8f57-438a21ac2084 | -6.12591 | -57.67488 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2f67c43-2d86-3d6a-85f0-6d81f7b9ccdc | -5.85412 | -57.55913 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 471d7249-4e22-31b8-8f06-81c4c664f107 | -6.91981 | -55.70392 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26d475ed-2906-3537-908f-4b8385344d59 | -5.57196 | -60.18939 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a307baa5-8bba-3cad-81a5-ac7a6e1d56a8 | -6.31011 | -53.54945 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0b6a406-687b-3308-9998-3dbb68ad236d | -6.60274 | -58.59102 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5d73fc1d-4b95-3b74-a4ec-e2da138dcb67 | -6.91371 | -55.69939 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33e2f038-89a5-3eb1-8ea6-2101c4fd1544 | -5.25414 | -55.90123 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26b77083-6ec3-317d-937b-e8e6a7254159 | -6.56356 | -58.56408 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43dccf50-8778-3d31-893d-0052728bd05f | -6.13082 | -55.64302 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f292b24c-00c5-302b-8384-7f5df000c018 | -6.16079 | -57.77913 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0da646e9-0061-3ead-af25-1728d5c69e61 | -8.78701 | -62.48806 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07ec6cc9-c18c-315d-9a7a-109f60adb4ab | -6.05349 | -57.64414 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 371c07ee-15ab-34eb-9825-c5e84bbba68c | -10.4578 | -46.73791 | 2026-09-01 05:16:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 805c435b-8fed-3759-98bc-8ca8cfe7f379 | -10.82333 | -50.71955 | 2026-09-01 05:16:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d09fe10-18d7-3768-8e04-475010dd22e3 | -11.4868 | -45.09721 | 2026-09-01 05:16:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26d9715b-bf25-350a-a5f8-03603d1b372b | -6.12307 | -57.67064 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9290ea2-fb57-318e-8169-0917e815f506 | -8.93106 | -63.2882 | 2026-09-01 05:16:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee7a6081-25c4-30aa-8a96-3dc89f46a7cb | -4.85941 | -55.83204 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc787617-b5b4-3b66-82f4-acefbce45bfa | -6.86922 | -59.40283 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ee5857c-cfab-392e-ae0f-46ee40610d6b | -9.96408 | -53.93998 | 2026-09-01 05:16:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5f22a28-187e-3a14-a557-79d43d50b777 | -7.54674 | -47.32588 | 2026-09-01 05:16:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd8a6827-dfcd-3d55-b055-e4dfa9d77f22 | -6.65979 | -59.42866 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6e126ce4-af83-353b-9ef6-519a3cee9b54 | -7.35882 | -60.59845 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e45005b-1387-386d-b40e-8ff10d63c086 | -7.2836 | -60.66238 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9bf177ec-1488-304a-8cbb-fbf5431bc0b6 | -9.48255 | -57.02143 | 2026-09-01 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 250bc554-4a37-34bf-b00b-d2225bb6a5ea | -7.6806 | -55.34351 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef44d13b-824d-3048-8af8-0618446ba89f | -7.56906 | -60.46812 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 420d7d8a-6f3b-30d0-8d30-fedcc8e64119 | -10.32898 | -49.95063 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 245b9bcd-04d7-34aa-80d0-a3d403bfe5c2 | -6.34491 | -44.09475 | 2026-09-01 05:16:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bf4e79dc-d4d5-3f94-8aae-eee8e069cd49 | -6.68463 | -55.5844 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f31cef6f-407a-39cb-a6b8-90c0abdc61a0 | -10.32345 | -49.95651 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a4308c7-ca20-310b-8c62-4dd6622a1834 | -5.97359 | -57.68433 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 80add0a4-2156-360b-9021-930fa9234ec3 | -6.72405 | -56.34214 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22946bde-c0ce-3972-9402-5e6d9a280e35 | -4.92325 | -55.76744 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce277d30-8fea-34af-9136-d741c2ada0fc | -6.79943 | -59.3974 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6fafdb41-a11b-3222-be08-5ed47bcdb3cb | -9.14755 | -59.53418 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb713062-453f-3ed0-86a8-c2e0a8d24266 | -9.71316 | -54.3351 | 2026-09-01 05:16:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 555c9df4-8a8f-3960-ad21-e62f9f1b8ff9 | -9.16175 | -60.28759 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 96316a85-13e3-32c0-8d69-20bc973969b3 | -4.3667 | -47.77221 | 2026-09-01 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0cb0ed74-fe0c-3296-afaf-b0719fa77ee4 | -8.59112 | -54.76799 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25e08118-3e9f-3c4e-a040-baa51ddd4d62 | -6.94021 | -55.63942 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cae6f71f-b829-342f-905e-5a161dd33bf2 | -11.26106 | -45.11339 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 78b604f1-2a94-3870-8d0b-203c4b2502e9 | -9.98247 | -53.92973 | 2026-09-01 05:16:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0f8df72-1124-387c-a7a1-562c1d677c8d | -6.42017 | -52.20115 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a099cd01-4876-39fe-8206-fcb2c66d6382 | -4.21382 | -48.60928 | 2026-09-01 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2db40eb3-c538-3751-a32c-938ffeb03090 | -6.16018 | -57.78285 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02f8b950-304a-3ef6-8cf2-e8c3d3e0326e | -9.19331 | -59.44731 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 00425bb7-4e9f-3eb6-838f-a597ad26122b | -6.98356 | -59.59437 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f78c8258-735a-338e-a4a5-849afe7b3fcd | -6.12129 | -57.68172 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dfa62e87-e6b0-32b4-9432-32f801a2bc60 | -6.26058 | -55.42523 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c887b123-c38a-3803-8eb8-21be51fd0adb | -11.22054 | -46.09547 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d88c8b68-f817-3f5f-83d7-d286b0a1f742 | -5.86784 | -57.77925 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea93e90d-5529-3ec5-b7d9-4875f7b4bfef | -5.85754 | -57.5597 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34572092-ab0c-32c8-8daf-9dec5f70d283 | -6.88758 | -59.40588 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a85872b5-2400-35dc-b56b-02341672385c | -9.15183 | -59.53065 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README55.md)
