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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4077b2aa-24ce-309b-9c20-de2490658a36 | -11.5678 | -46.35669 | 2025-08-30 03:30:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b86c5e4-33e2-347e-b410-3ee20c0c1765 | -8.45614 | -43.64015 | 2025-08-30 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2919603d-a8c3-3cda-aa3f-e2209087bdec | -11.85922 | -46.45106 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 12197bdb-cd26-35d6-864d-9b9dd5679dc7 | -9.10895 | -46.04864 | 2025-08-30 03:30:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c62f91c6-39f6-39c6-aae7-b3b96ce56b95 | -9.21865 | -46.75506 | 2025-08-30 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a9bd7758-cce6-34fc-a4e1-4e24baa9b126 | -11.8564 | -46.38458 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2d99d361-ea8d-390d-b3ee-7744353820b4 | -11.32379 | -43.63057 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed89a18c-e205-3aa1-a3f3-eee3da1a005b | -11.92088 | -46.69386 | 2025-08-30 03:30:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 24b1ab30-b078-3a95-b6aa-ba0b8b087ad3 | -7.64344 | -42.65811 | 2025-08-30 03:30:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9f259530-9d7c-3c66-a690-23f4818dcf3a | -11.84196 | -46.38712 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 34832e05-a6ad-3187-ae61-2cc6793f278f | -7.6814 | -44.9922 | 2025-08-30 03:30:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 72a903e7-c817-3212-9d5d-9f9ed40caa6f | -10.99379 | -46.95298 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4919460e-7747-3ba8-9559-33cc797a839d | -7.08881 | -44.30387 | 2025-08-30 03:30:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c3761ae9-bbf2-33e1-a5a8-7789afb94f53 | -11.84734 | -46.39476 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| afafffb8-f012-30dc-a959-10cc408741e4 | -12.55863 | -44.80657 | 2025-08-30 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f4f2179-6254-384c-a42c-7791bafde3b5 | -9.4948 | -37.96228 | 2025-08-30 03:30:00 | NOAA-20 | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e96e012b-94db-3e6b-ae9c-80c723bd4b0b | -9.21718 | -46.76249 | 2025-08-30 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4affe615-1a62-3fdb-9388-9fc5a38ec173 | -10.71819 | -47.01234 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34c773c2-71e2-34e7-98e0-ebcbebc3d7ce | -11.86413 | -46.44866 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ac506ed2-42b3-3f42-94a5-1d4492cff866 | -11.30427 | -43.63946 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ba7db71-39a6-344f-8ec9-9ae52b3e67e9 | -11.86757 | -46.39796 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4a148111-9f4e-36d8-a9ef-427b3159219f | -11.15522 | -47.14661 | 2025-08-30 03:30:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e847b57-f1dd-3424-95fd-3dab4e725d79 | -7.1201 | -44.60498 | 2025-08-30 03:30:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e97f63c2-912e-33ee-96ec-d4c0cee2ee0b | -11.34943 | -43.58979 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b89cbf88-bb34-3716-9cbe-191c9bb00adb | -11.35887 | -43.57149 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 260f14dc-edce-3061-9f23-b630e35f1f97 | -7.16777 | -44.16128 | 2025-08-30 03:30:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4cbd5d50-c0a0-39f3-9a7b-9876a225bfe7 | -11.8629 | -46.45466 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7fc0379a-6842-32dd-9bf8-aef63f5c2704 | -8.45046 | -43.64785 | 2025-08-30 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5920196c-463c-3ee7-82b1-5d865bfdc524 | -7.40997 | -42.06425 | 2025-08-30 03:30:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5680b0e6-421b-3934-ae77-b2e2721e5c78 | -11.82929 | -46.86027 | 2025-08-30 03:30:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d00ff6b-3249-3251-a838-2e991d2dfe75 | -11.85541 | -46.43612 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d317636d-058f-37ce-b806-23d6d8e4abd7 | -11.87074 | -46.38246 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1ccee686-68fe-3d10-99c1-edcbfeafeffb | -8.4493 | -43.64354 | 2025-08-30 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b26263b-a685-36b6-80ba-bd6bf0596b6f | -7.40105 | -45.92888 | 2025-08-30 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6e5c2bf0-e463-3fb3-a820-ea7f3742ef74 | -7.63704 | -42.6608 | 2025-08-30 03:30:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ef65c6ee-2847-337b-8c9d-1e54ef4cafac | -11.32687 | -43.61473 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5672b92e-df12-3f17-b287-0a42d9d1c949 | -7.1017 | -44.5914 | 2025-08-30 03:30:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 50c243d7-ed6d-30e6-8571-6b673cdbd42f | -9.69116 | -47.06009 | 2025-08-30 03:30:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6a018082-ca86-3ef2-8db3-f4c206143516 | -11.9299 | -46.69122 | 2025-08-30 03:30:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8c59a84-947c-33e3-8adf-90ac72b65450 | -11.35812 | -43.57538 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e61da055-8948-3bf4-b50c-7a8f09bbf91b | -11.84329 | -46.38068 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a6e464bd-a8a0-3387-8ce8-7840b0ccbd15 | -11.86627 | -46.38504 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 47bea18e-87fd-37fc-877c-3957393f3450 | -7.09334 | -44.31507 | 2025-08-30 03:30:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 3790c50c-f8bf-3aa5-9bca-196fbcb8b8a3 | -11.31259 | -43.6577 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 850d0e8e-58e1-303d-891b-aedf8ec208f3 | -11.57018 | -46.34497 | 2025-08-30 03:30:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af51dca2-eb1b-3758-87f9-964486a276d2 | -11.8709 | -46.42892 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61a12a9e-657d-3ffd-92b3-8f79ac5f1feb | -11.35961 | -43.56759 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ae1644a-663b-31ef-8255-e0b433c1546b | -11.22177 | -45.02725 | 2025-08-30 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccbd88d7-c996-3298-a788-48be53664e3d | -11.83959 | -46.39855 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 12484da4-3179-326b-94c4-c13bac9a6837 | -11.35018 | -43.58591 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 88a13b5c-a79b-322e-9c03-ab6f024da921 | -11.31415 | -43.64966 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2b1fe90-d8d9-329e-bc61-3a785d06d940 | -11.34225 | -43.59637 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2e237fb-aad9-30c8-80ea-45e88f3630df | -11.30345 | -43.64362 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae097727-85d3-3149-8dab-859467a917ea | -11.35585 | -43.58715 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 557fbffa-e26f-3128-a525-ca37f169ee19 | -11.3253 | -43.62283 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3bfa1def-7aca-3d6d-aee6-f7d2d3e2b3d1 | -13.47265 | -42.48434 | 2025-08-30 03:30:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f7bc84e5-aea9-3f52-af8a-ee8a2e0b2f73 | -11.86779 | -46.37787 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5f93980e-8ec3-3579-aed5-e14387a5cc13 | -11.0004 | -46.85996 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ece5b59a-6c3f-3699-a702-605da2dfcd7e | -8.45137 | -43.64308 | 2025-08-30 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a05a98c-5d2e-38ec-bb92-97fc7b834abd | -7.59749 | -42.71518 | 2025-08-30 03:30:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 304cdba3-4c0e-3023-8ad3-27c21ee765eb | -8.04936 | -45.41229 | 2025-08-30 03:30:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1aea0bcf-f83a-39ec-956a-5852f1e9f05b | -12.56462 | -44.80787 | 2025-08-30 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8ce986d-10d8-3440-a9df-b4d0ac3fe387 | -7.16549 | -44.15103 | 2025-08-30 03:30:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6f16eb86-0be6-3cbf-82b2-8500aa96ecee | -11.83368 | -46.46085 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| d31afd30-0c73-38ff-8605-65cfc5d5c0b5 | -9.0265 | -40.52098 | 2025-08-30 03:30:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2f0bf8f7-8994-3865-9882-79b3daaea3e4 | -7.60397 | -42.71223 | 2025-08-30 03:30:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| da074451-a165-33a6-8db1-2a3df0a8ea4e | -10.99906 | -46.86644 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| be61b37e-a6bc-3949-b0b3-d39dee8715c5 | -11.29616 | -43.65057 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c33d6d12-6874-3f9d-a7f1-380f4873e40b | -11.34149 | -43.60031 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36f8febc-f368-3f9f-8294-54469cbd6ee5 | -11.86436 | -46.42685 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ec8d16b4-32a1-370f-9f96-1efc27c82d34 | -7.19899 | -43.71083 | 2025-08-30 03:30:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c4f221f9-b160-34a4-bd62-8d7c82874e0b | -11.31987 | -43.65076 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f17f621-89e5-3450-b88c-3f2977268a9f | -7.61899 | -42.72755 | 2025-08-30 03:30:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 044bc6bb-73ad-3136-92ac-2e9691407088 | -7.40014 | -44.28757 | 2025-08-30 03:30:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b1c346a4-a3d9-3b06-8425-29fdbd733bf7 | -10.99933 | -46.96121 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 551f1392-536e-3ad5-8f53-f91eb20a29a6 | -7.3949 | -45.93301 | 2025-08-30 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cbefcd90-d060-3a4d-80e6-7e27b1360a81 | -11.82791 | -46.86685 | 2025-08-30 03:30:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac93f77a-c3f0-39ec-af36-abb3e2bb8d3b | -11.30841 | -43.64865 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 642c0d2e-a570-3b94-862b-37d2fe8c328a | -7.14895 | -44.90622 | 2025-08-30 03:30:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 72abf8ed-2ab3-3d07-b738-59d9b9a05411 | -11.31959 | -43.6217 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 100fd47b-7d21-3f9c-ab5b-e8102d4ad7e4 | -11.8737 | -46.44866 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8612c6e-28cd-334e-bcfb-07614b20520c | -11.30765 | -43.65255 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0904fa6a-d4aa-3a22-ab59-40c51d4e2f74 | -11.86917 | -46.39016 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd268654-7aa5-31af-8542-f348047bf16f | -11.35737 | -43.57927 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2de209a5-a23f-3b43-8868-31f86df57413 | -7.16676 | -44.16683 | 2025-08-30 03:30:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d15b8bc0-94a3-3e5e-a2e5-ab3eabfa6126 | -11.30687 | -43.65653 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8db235fe-f6df-390b-9428-2cb5bb567e67 | -10.99785 | -46.96821 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fcfca536-3818-3eca-9094-da69d7e2f0d8 | -11.32767 | -43.61058 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c71391f5-8ebd-3b8f-84b0-8fe161422b55 | -7.60252 | -42.72016 | 2025-08-30 03:30:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d9348cfa-4aec-3b14-81c0-3c7063d0ae38 | -9.02867 | -40.51909 | 2025-08-30 03:30:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b06bbfc3-afc1-3e04-aa30-99aa53284baa | -11.8612 | -46.39509 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e6ea887d-5a71-373f-83f2-f5c1ff2dc9e5 | -11.3116 | -43.63226 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f38caa0-0c92-3505-84b5-de202d10e2c9 | -11.8671 | -46.44687 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b43e8a0-82d9-3366-8be7-4141263eda67 | -11.85497 | -46.39152 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0f6530e1-840a-3484-8f37-e634a0ffb273 | -11.31809 | -43.62942 | 2025-08-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df0f5765-aa04-3f01-abd8-7144090ef183 | -8.45824 | -43.63971 | 2025-08-30 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc340fc8-4a9a-38e2-9063-45adc3665fa6 | -10.99328 | -46.96514 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1de371d-d22e-347d-836a-89a295e0c015 | -9.02285 | -40.52369 | 2025-08-30 03:30:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0834e0ac-df69-36d7-9c2c-c9112ca37ae1 | -11.83497 | -46.45462 | 2025-08-30 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 311361fb-9562-396c-99c8-126484f86dfb | -11.77676 | -47.56575 | 2025-08-30 03:30:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README14.md)
