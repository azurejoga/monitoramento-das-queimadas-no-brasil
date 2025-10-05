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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a975342-7464-307d-9211-7eea521f3435 | -11.78659 | -47.9206 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25db754f-8def-3803-bc31-f3ad88c51c9c | -11.75909 | -44.74438 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 055e92ca-feb0-330e-be8f-c4574e48aeb7 | -13.72788 | -51.31518 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5724f5a-218f-3fa1-9d3d-9ab4f4758cad | -11.80541 | -46.85314 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9731d4ae-9e91-39b3-b220-a4ddabe802a8 | -11.91099 | -46.23666 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4295a257-f191-355e-a042-6ec092d112a4 | -13.26106 | -47.19914 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb13aa3c-836d-38c8-adaa-a886b2a1d9cc | -13.25851 | -47.81746 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| aecfc9a5-a5b5-360f-851f-8216f69d68eb | -14.66415 | -48.3504 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b33378cc-229d-3a2e-86f8-145a40f23d71 | -11.45345 | -51.52542 | 2025-10-05 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8182ba87-7eab-344c-a421-1c9f90c25009 | -13.31587 | -47.17664 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 470b65a8-fd04-30c2-9a08-fb6c237e2ac2 | -11.52763 | -47.23923 | 2025-10-05 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b1eb6f7-35ed-386d-a420-578ee071fcac | -11.81894 | -45.04106 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c95c9d38-406e-3bbf-a67e-9957bc99938e | -11.62277 | -47.74752 | 2025-10-05 03:55:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f522b285-27cc-3093-957a-ce68d86f8ec7 | -12.78059 | -48.82123 | 2025-10-05 03:55:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48dc3f8e-216c-3c57-b87e-1afad3151c90 | -11.69343 | -47.50032 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| af52679a-224d-3022-a87c-6488b6dcfbe9 | -13.0884 | -47.94267 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5d1d601b-714b-35b5-b79a-a183ebfcdf6b | -13.28729 | -47.5908 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d9fb5583-577f-368b-b799-9c3a1d4c6b7f | -16.53472 | -47.77952 | 2025-10-05 03:55:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 72642082-2483-334a-81f6-95efe09d01d9 | -12.97077 | -51.03716 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c854b72d-1ac2-3e8b-a637-9f9a027e3d78 | -14.29305 | -45.86696 | 2025-10-05 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e467d784-9382-3eab-a093-211bf4dfebb8 | -15.20772 | -46.38464 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe63c67b-1e36-3f25-ae33-f14ae4adb759 | -13.35684 | -47.24182 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a0272f83-76ef-3e75-995f-7d4b54f02b83 | -10.54056 | -47.80344 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e2017ce6-9f43-3059-88ee-30a002cd40c7 | -15.93215 | -48.98795 | 2025-10-05 03:55:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d04e2c14-3d45-3d69-8004-b544d1526cd3 | -11.09186 | -47.74192 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 540d1cf4-90ab-3f68-9b2f-e6392e277a4a | -12.69571 | -45.84705 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da09e2ef-9292-34be-9171-83a83532e23a | -14.6733 | -48.36518 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 25b4fd95-658f-3419-92ab-06bb87388d20 | -10.8423 | -47.96931 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| d8013e99-80f5-346d-8c9a-21a5a885c059 | -11.00079 | -46.51971 | 2025-10-05 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3dae1e7f-115c-3a9e-b15b-cc437b70e180 | -14.41789 | -46.17812 | 2025-10-05 03:55:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07da9381-dbae-3d63-a32f-b34a345759fe | -15.54962 | -49.2758 | 2025-10-05 03:55:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c1b2c7f-c48e-3ab4-9554-dbaf580c4244 | -11.80542 | -46.82621 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58ecf579-d3fb-35a8-8bee-06ad586bba45 | -11.75633 | -44.73635 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 79aeb530-d6ac-3953-b764-fb50da09756c | -16.0802 | -50.92028 | 2025-10-05 03:55:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9315eb1-fde6-36ee-8477-ae1f37fd7e2c | -10.84635 | -47.19899 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd634cd3-9101-3a1b-8f5f-0d1f92a5ef52 | -12.9362 | -46.36837 | 2025-10-05 03:55:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bfcefb66-ddad-323b-93bb-809424c82010 | -11.89663 | -44.98799 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 976a2fc1-c7ef-3037-bc2a-f1a327fa5089 | -10.83042 | -46.58001 | 2025-10-05 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78c0fdeb-36ae-34cb-be51-e22f6975e474 | -13.11961 | -47.80354 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55ab38b4-527a-3645-9837-4f1736efd0ea | -11.13518 | -47.92896 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a6f1a6d-ef5a-3e96-87cf-8ef817235822 | -12.98085 | -51.04893 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 58d70c57-fcb6-3327-942a-71346a4a233a | -10.79632 | -51.00488 | 2025-10-05 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 89a46254-c3c0-3ee6-ad60-c471710c9ebf | -13.51649 | -47.23983 | 2025-10-05 03:55:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c7651b22-6a5a-344f-8ca4-cfb3b7642aa9 | -11.12787 | -47.91168 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecdbafea-da52-3e25-af6a-940bd7e5fcd0 | -13.32582 | -47.57061 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6d2cf31-e02c-3908-9604-0e55b9498a29 | -11.82605 | -45.073 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da25605f-74d1-39b6-bc34-6dd5100d7d9f | -11.12282 | -47.91056 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de0e17ea-f0fc-3a68-becf-2bdaeaccdc71 | -14.66561 | -48.35251 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 00ada3e2-2719-3ad0-9ff1-1d74cbbf3cd4 | -13.09295 | -47.91845 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7b0da30a-a34e-32f9-9dc5-f3ad099f26f8 | -11.7604 | -44.73709 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b992ae71-d110-34eb-8f4e-32ad9be3b434 | -11.80079 | -46.82515 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 403e9988-babe-37c5-97ca-48a34eed0cb4 | -12.56619 | -48.16372 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a9ec048-a811-383f-9a9a-e143adad3a23 | -10.75517 | -46.61107 | 2025-10-05 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 24780db8-ce64-3329-8ffd-1deafdee501b | -10.7386 | -47.90379 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cbb7116-b811-3725-b1f0-5807a12377ab | -15.29696 | -47.32642 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43ead2e5-dd9a-393f-8fa8-2701bdcf55c4 | -13.24825 | -48.48221 | 2025-10-05 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0741699-b2ab-3e42-bf43-1e2f30a5deb7 | -13.44466 | -47.27625 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 321e2b13-9d65-3c1f-8e5f-ab4ace8694f3 | -13.73506 | -48.08239 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ba31202c-58f9-33ed-860e-dd1658383015 | -11.48291 | -45.04694 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e27a2c86-c62a-3642-a624-249fb4b351cb | -12.57681 | -48.16273 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 232ca143-8176-3d04-ab6e-b3750baa338a | -14.68969 | -48.3336 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 29e05972-d269-3405-bca1-ac2b7825982d | -11.43634 | -43.49134 | 2025-10-05 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6551c55d-5e82-3ea5-aa7a-827f1731d222 | -12.69496 | -45.8512 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 510ccdb8-e35f-316c-8883-35dd09e8c6cb | -13.3213 | -47.77804 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 057dcb99-3624-3928-a221-40b4803282ca | -13.72885 | -48.08813 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8a26dcfb-4803-3b4e-b3fe-021b2e5bbe4f | -13.47807 | -47.22578 | 2025-10-05 03:55:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cca6a641-4cee-3afa-9f12-46f5191d23a4 | -14.66668 | -48.31042 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 244506d9-5bf7-3d7f-860b-9c6475b4afc8 | -15.60128 | -52.49683 | 2025-10-05 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9fb3c246-6e21-31df-8465-87b4e0d6f468 | -12.99979 | -43.99878 | 2025-10-05 03:55:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d743e8dd-5b9a-355e-ac92-fe1887512366 | -10.82852 | -47.98592 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ce706822-93bc-3453-8969-e93fa5944a01 | -10.94466 | -47.08894 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b3b4770a-b4aa-34a5-9106-9ab1ddbb059d | -10.84732 | -47.97082 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e37132d3-2dcc-368f-ae15-b05c11d14856 | -12.39269 | -51.09803 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bceb3f54-9d64-3c74-b455-e8dc9c2f5909 | -13.16126 | -50.87599 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| daa5fbba-4acb-3380-98f9-5fc8b7b72f23 | -13.35308 | -47.58323 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 255b1750-e961-3e6d-8d44-9a06d1c8fd61 | -14.86865 | -48.15366 | 2025-10-05 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d33890ca-c8f0-37d9-a046-e580a74aed99 | -11.47531 | -45.04136 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e517348f-89d0-3905-8f39-d7ae06e7c165 | -14.99277 | -49.9878 | 2025-10-05 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e88a995-babf-3815-94d9-6b0948515241 | -17.35546 | -45.01099 | 2025-10-05 03:55:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 92548e6e-733f-3fd2-bfed-73eef7734baa | -14.87667 | -48.13799 | 2025-10-05 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51d9d786-f3f9-35f1-92c4-5a5d948fb8f6 | -17.551 | -42.38262 | 2025-10-05 03:55:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d9a592b-aada-3462-82cc-50ece83c606d | -11.12959 | -47.90246 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ebe13ef-7912-3f3d-9610-e8bedb2b0864 | -11.43715 | -43.48669 | 2025-10-05 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 691c99a0-54d3-3fbc-b223-9b93ad068f3f | -11.06522 | -47.77782 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fa2d5f7e-e936-310c-8f88-cc3e0f086d46 | -11.82082 | -44.89658 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3d40266-f436-332f-a9fd-a5dfa80c9ddd | -15.39082 | -47.95464 | 2025-10-05 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e9a2f542-eb1d-3027-8ebe-f62e34021424 | -10.57223 | -48.68805 | 2025-10-05 03:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f77954f-8317-3eb6-a951-1fcd91cf044d | -12.90544 | -47.31541 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 551f821d-c6c6-386f-88ec-979935acf33a | -15.31958 | -46.36877 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 486bbb41-1d6c-33b9-93d7-a86f7be28cd4 | -11.81543 | -46.86237 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 2932ac2b-c50e-38f3-9693-7bc122b66fdb | -10.56676 | -48.68742 | 2025-10-05 03:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0219adfa-3a9b-3d42-a9b0-e03690453803 | -11.81698 | -45.05194 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 39f8adab-6779-37b0-9e1f-f5d3669bf4d8 | -12.51559 | -42.89349 | 2025-10-05 03:55:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0d7bc712-39af-3606-8c02-6b6d070fa5c9 | -16.07088 | -51.08841 | 2025-10-05 03:55:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1f878fe-f837-37c8-8116-678bf4b82512 | -10.7362 | -47.90122 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01ba4bd4-f943-3cae-bcc2-98f862a48ca9 | -11.7101 | -45.35616 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71a89517-6aff-359d-b58d-16322c0e0559 | -13.29009 | -47.57627 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 70aa1119-c006-373a-8535-9070fb9c3d0f | -15.77645 | -49.09366 | 2025-10-05 03:55:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72b08879-8f5c-32b3-8d31-cb0ac0c5249e | -15.97965 | -50.91121 | 2025-10-05 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d876c000-c698-35e4-9c36-80dc8206f307 | -12.61075 | -48.12106 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README58.md)
