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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46fdd4cc-01f6-30ec-a7b2-e826b4d8742a | -9.51486 | -68.6068 | 2024-09-29 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45100d8b-624c-3ef6-b8f0-ac6a7fc98e16 | -9.51479 | -68.27155 | 2024-09-29 05:44:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f312cd8e-573d-36d9-b4f2-451f918048db | -9.51371 | -68.6075 | 2024-09-29 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e5b8d34-38ae-3e0a-bf14-b03f558bb8ca | -9.50744 | -68.51341 | 2024-09-29 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a506429d-6507-3ee5-af37-7d5558035de5 | -9.49475 | -68.50328 | 2024-09-29 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 983e06e1-df98-3b3f-83cd-66319d76d7af | -9.45013 | -68.55638 | 2024-09-29 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a04af995-68f0-3d37-8495-2f67a65497c2 | -9.42245 | -68.78952 | 2024-09-29 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e496861c-211d-39e2-a56f-c80906a67984 | -9.38757 | -68.75896 | 2024-09-29 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a861fea1-dfd1-31ee-8474-e8b682bfa87d | -10.11502 | -67.88904 | 2024-09-29 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0747fa2f-b78c-36dd-8580-2cc8c90b0465 | -10.11163 | -67.88848 | 2024-09-29 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a52499c5-5571-3fbb-95aa-3f6d536ed978 | -10.10544 | -67.88368 | 2024-09-29 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bde46fca-145b-3e5f-93ef-81ff14e2597c | -10.55729 | -68.02184 | 2024-09-29 05:44:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aaa65305-0619-32cd-85e1-79bbbfb10165 | -10.5539 | -68.02127 | 2024-09-29 05:44:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 58a8fab4-af33-3895-8376-3949b15ac020 | -10.52611 | -67.84991 | 2024-09-29 05:44:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83c4974b-a750-35d9-8dcc-608192390433 | -10.46889 | -67.76558 | 2024-09-29 05:44:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eeec23cc-1cb9-3dd5-9857-b37d420cc211 | -10.91224 | -68.87658 | 2024-09-29 05:44:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c1bd5c2-e159-3674-8126-502296c61dbe | -11.08374 | -52.4701 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5c6bfc6a-a25e-33b6-9d8f-72c0bc3012eb | -11.08083 | -52.45924 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59c49a79-d0cd-3974-8258-60694bcc446d | -11.08003 | -52.4663 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7525a884-7ecd-314a-93a2-93dcd159aef6 | -11.07922 | -52.47341 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 911e979a-2daf-3c67-9136-8c690aba7ba0 | -11.07888 | -52.44808 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25261f86-f3c0-3a80-a035-6f46006a5c55 | -11.0784 | -52.48065 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c0357c97-6176-36d7-be24-3ae94d8ce1c4 | -11.07812 | -52.45514 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ea82044-a7cd-31aa-84a5-1ec3111246e5 | -11.07759 | -52.48778 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 216394f4-3f47-339d-9ba5-439a06f3cdcf | -11.07736 | -52.46228 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a46a8054-ebf7-35ee-a19c-4f0f05006c46 | -11.07661 | -52.46938 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c66af1d1-478d-3f5f-a268-4ffeefbcfad9 | -11.07584 | -52.4766 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 014cb7c9-40e1-3646-8e93-1a9e2702f04d | -11.07507 | -52.48376 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| ba631589-0e73-3590-a065-486782bdd931 | -11.0745 | -52.45136 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 36d805ce-06b8-34be-8b3f-b901992a75d2 | -11.07433 | -52.49076 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 9efd8684-1796-386f-aaf9-5dea48894dbd | -11.07369 | -52.45857 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 78085a9c-0964-3f1d-91b1-6f3ca23814ca | -11.07359 | -52.49764 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| f5ac41c9-0fd0-35ca-8550-9cce05e9b60d | -11.07288 | -52.46572 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 67db203a-058d-3627-9f94-ae975eaafd6a | -11.07285 | -52.50455 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8634c9b-2897-3f0f-b197-70f620f88137 | -11.07208 | -52.47284 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 6e00fa3b-fa4a-3904-b398-596c7d6d6ffc | -11.07176 | -52.44714 | 2024-09-29 05:44:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27e0adbe-665e-35a2-860b-80c8543af2ab | -11.07127 | -52.48001 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 71546062-2814-361d-9c5f-873da23283c3 | -11.07099 | -52.45443 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a383e6da-eca8-3bb6-a62f-4e17a6d57834 | -11.07048 | -52.48699 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 59bf21bd-7d62-3d99-b691-c8ecf2ce1787 | -11.07022 | -52.46167 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c6eeabc4-f780-3b90-94e4-c77c5e90968c | -11.06971 | -52.4938 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 4d96b32d-f8d3-3dfa-9c07-80315ef9309a | -11.06946 | -52.46879 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| d3e62084-eb73-3fd2-8b29-788491bfb118 | -11.06893 | -52.50068 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| faa21d09-6da2-393d-a167-c40583fb72ea | -11.0687 | -52.47593 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 333dc392-7bf7-34fa-a402-f776d0581635 | -11.06796 | -52.48296 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 000e93f8-d5a8-3318-a571-84ccc716503e | -11.06737 | -52.45063 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a7ce1552-b325-3c00-9620-218fa3804c5b | -11.06723 | -52.48983 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 54511890-e883-317c-8528-a8ce91f1793a | -11.06655 | -52.45792 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 77eeea8f-94ab-3aa9-be29-3842663540fc | -11.06651 | -52.49659 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 7e281bc2-a37d-383f-bfe2-ce6eea162eba | -11.06577 | -52.50349 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 709a8126-de29-3562-80b8-2b0c42fb626f | -11.06574 | -52.46507 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b1915a4a-5570-30b9-94a6-9c9b1ae3d2c8 | -11.06495 | -52.47215 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 0bd08f1a-ddc1-304b-a3d8-01d04c0c8b16 | -11.06415 | -52.47923 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 39847e9c-d0f4-3380-9696-4612d05094a0 | -11.06337 | -52.48611 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| fc5ddfca-dcd7-3a1c-91c5-c94902acbc17 | -11.06262 | -52.49281 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| e172f399-0f2e-3108-a09b-c93bb760aa1e | -11.06186 | -52.49958 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 41679e42-5723-32a5-9e4c-16e468652ee5 | -11.05863 | -52.46423 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c10640f1-e3ff-3c88-9498-5cb113e4e034 | -11.05784 | -52.47128 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c66ada89-3598-36a9-b011-65feba4d6924 | -11.05705 | -52.47828 | 2024-09-29 05:44:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dc229f86-3a4d-3e69-b41b-04435e78c6e3 | -15.77976 | -54.18776 | 2024-09-29 05:44:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8aa1f0a6-3bee-3df8-b4ac-04674907bb0d | -15.77777 | -54.18367 | 2024-09-29 05:44:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c2939f1f-6837-3348-9c7b-c169111f5442 | -15.77715 | -54.18988 | 2024-09-29 05:44:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5417d77f-217e-3510-8e34-9f7a4b597740 | -15.77297 | -54.18716 | 2024-09-29 05:44:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ea6505d2-b02f-311f-9784-b8dc207eea51 | -15.77098 | -54.18305 | 2024-09-29 05:44:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa1da8a9-78d5-3195-8997-e2afe29441a6 | -15.77035 | -54.18938 | 2024-09-29 05:44:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da1e9d2c-600a-3366-8581-ea2f0a124977 | -10.37974 | -53.78115 | 2024-09-29 05:44:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 91da72e1-3c4f-3cb6-997d-c396ce561582 | -10.37906 | -53.78683 | 2024-09-29 05:44:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0257eda0-10a0-3b6a-bad3-6c5f28e342ec | -10.37838 | -53.79256 | 2024-09-29 05:44:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3775afc2-d368-3982-9e0b-fdaa90e67c9c | -10.37253 | -53.78598 | 2024-09-29 05:44:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3c1b7050-81b5-3385-8233-cc324f65f983 | -15.62343 | -57.46912 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 470a382c-1fae-3a3d-b01f-2a91421bd1dc | -15.61831 | -57.46503 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e6ec63a-2ce7-3816-a568-60398b6f005c | -15.6175 | -57.47218 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3085d2ab-4246-3d68-acfb-15ad2345105c | -15.61745 | -57.47257 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79250518-34e3-30dc-91a0-30ed1da10700 | -15.6171 | -57.47593 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe1edbf1-2df0-3be2-a451-60b708d22183 | -15.61278 | -57.46431 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1ba302e-baf6-3121-bceb-21807656a976 | -15.61197 | -57.47145 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1a46e97-707c-35bb-a590-99c307af77f9 | -15.60173 | -57.46289 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44b31432-f7c3-34e8-9b9e-5bf4ef435bac | -15.59536 | -57.46963 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 863a4b59-292e-341f-9817-5ad8b0217a0f | -15.5915 | -57.50389 | 2024-09-29 05:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7807250c-f10e-3de5-b4b3-5c34139816aa | -15.58941 | -57.47268 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 40803db0-78fd-392b-9c26-f57ae149ea40 | -15.57311 | -56.92491 | 2024-09-29 05:44:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af9eb829-ff7d-3c3b-8c80-40f06bd225c1 | -15.57259 | -56.9295 | 2024-09-29 05:44:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebe268a4-f401-3186-931b-6a9cea0282e3 | -15.5689 | -56.9262 | 2024-09-29 05:44:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7dbef56c-d17b-3a14-ac40-a4c1bbb1b37b | -15.56846 | -56.93046 | 2024-09-29 05:44:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e6cf9b7-b081-3864-b5a7-dbbd8a530f66 | -15.63328 | -57.48177 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c988ca13-f628-3807-a421-e1ae4ee375b7 | -15.62815 | -57.4773 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47722bf9-ba07-36a7-a05c-365fb86516f2 | -15.62808 | -57.47765 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a4854d34-78c9-3307-ba61-5934736690d1 | -15.62384 | -57.46574 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 83817f02-bc8a-3da0-ab31-3c46f75f3b4a | -15.62383 | -57.46535 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 65428b7f-3067-3eb4-a52a-f677f2b90025 | -15.62341 | -57.46951 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96c5c21b-b1a6-3629-9b36-417f56aa408b | -15.62302 | -57.47288 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 66b5d9f2-4485-3d53-b6a3-137dd3134071 | -15.62298 | -57.47326 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2778aa14-fac3-3190-a4d9-b2b5f50d90db | -15.62262 | -57.47663 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c8107eb-4251-3975-aa22-767acf35807b | -15.62255 | -57.47699 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f0dc76d-501d-3a7e-b48e-94e5a1e18c53 | -15.62222 | -57.48037 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d962404f-b093-39ef-9e78-a0c7bbb2416c | -15.62212 | -57.48071 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f99982c-0981-34b9-9504-5f9884bee884 | -15.6183 | -57.46462 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd71b7b7-e1c7-34a3-8f34-52d9a46884e4 | -15.6179 | -57.46841 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1cffcd6-d95d-3c23-a024-a105dad3b105 | -15.61788 | -57.46881 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f68ea20-cd21-3f11-a9a7-f92c576cc18c | -15.61277 | -57.46388 | 2024-09-29 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README66.md)
