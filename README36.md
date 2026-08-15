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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f7affef-38dd-3cda-b062-969134024d83 | -6.20422 | -57.76915 | 2026-08-15 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 217cd836-6581-3749-ae53-17a870574346 | -6.61834 | -59.07956 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0870a74-da9f-3739-9dbb-89419a1cbbaf | -6.6966 | -58.9555 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83aecebb-94cb-300f-8a63-18f51b083626 | -8.03286 | -55.13441 | 2026-08-15 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 842f3e31-1214-31e4-96d7-83a53deea35d | -3.94804 | -59.62567 | 2026-08-15 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1c4f4e3-7e61-34df-81b7-e54b89b96743 | -6.79125 | -55.689 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19d2c19c-c65f-30bf-a88c-22eadaa1bfe4 | -7.39213 | -59.99993 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| debee0a3-61b9-3cd6-a65f-467f7ffbfd42 | -6.82911 | -56.43298 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| daaa185e-17eb-3242-a5d3-2b4e457955db | -6.02288 | -57.84101 | 2026-08-15 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbeee9e9-ec27-3437-ac56-47b4c8c0708e | -6.84772 | -56.44089 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ae10837-8441-338f-b894-d211856b52d0 | -6.652 | -56.41231 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07193ad5-dad4-3c99-a425-5d0d10d6143b | -7.70094 | -55.17037 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 181ab157-5efe-308d-9ac1-4877c72c3814 | -6.95054 | -59.29821 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29cc236e-fb5a-391a-b315-e084c5e9ada1 | -6.61947 | -59.04977 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d2079aeb-0a33-36ca-8782-228deae47a1d | -6.59732 | -56.35472 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfe97143-a850-3074-ab0a-dc665a913b50 | -6.94248 | -62.88227 | 2026-08-15 05:33:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1bb5205-ec74-3c85-b625-e4195eb8f31e | -6.86142 | -56.40301 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3c44750-d510-321f-be80-a897f08e1b35 | -6.96074 | -59.27747 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa34a768-c211-32ff-a295-ad8ccdf8b889 | -6.62345 | -59.04664 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6c6b320e-d15f-35a6-9ecf-b678fff4a15b | -6.84948 | -56.43296 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 64dbba9a-31ae-37fe-bba4-3340ca816898 | -6.7888 | -58.74462 | 2026-08-15 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1a276d0-64cb-3e2e-af2d-bc0a2f0e9514 | -4.31201 | -59.46466 | 2026-08-15 05:33:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27dab444-2d01-35e7-b6a6-74d56971201c | -6.78822 | -58.74838 | 2026-08-15 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee12ef0c-24e7-37a3-a8d2-8d262c99e8d3 | -6.62402 | -59.04298 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9d635f2b-9b0e-3ca7-868c-47a1d74e65bb | -6.788 | -55.85082 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb2738ef-085a-3409-bfad-efd42fc8a812 | -7.69564 | -55.15852 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fca9bb77-bc7d-34a1-97eb-bf26d3513e4e | -6.8509 | -56.42318 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4e699eb0-e781-3739-9aeb-d7f1a0b1e975 | -6.95393 | -59.29873 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ddd7341-0749-3015-a586-b0535986628d | -6.93072 | -62.87738 | 2026-08-15 05:33:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a57c8a5-15eb-3443-99f8-a40d087a00d2 | -4.10748 | -50.99504 | 2026-08-15 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c12db221-f078-3f81-b2d6-a7db1b12954d | -3.74731 | -59.33033 | 2026-08-15 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f883552-fa11-386a-a4a3-6279b400e34e | -7.59524 | -60.87645 | 2026-08-15 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c92880e-7b31-3659-aa89-5bbe872c3a78 | -7.59192 | -60.87592 | 2026-08-15 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94034a02-c306-3c19-a51c-b76c9d8c06ac | -6.62118 | -58.99366 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 484031d0-61b1-33f4-aa13-06e2f96d9830 | -6.69604 | -58.95916 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1623364f-7e96-30fb-93a2-e3a22d0fa64e | -6.85993 | -56.4128 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c8c59b1-d99c-3c65-ab98-b0ee22f385c7 | -6.79461 | -55.83398 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3369603b-65bc-325d-8ce1-a206233168ba | -6.9362 | -62.87738 | 2026-08-15 05:33:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19170208-b679-32cb-99af-2f798c1c938e | -6.84845 | -56.43605 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba665228-ce37-3eb3-b760-065907c5eb9b | -5.95902 | -52.26105 | 2026-08-15 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 181ec00a-9fbb-3feb-acab-3c6f99298ef0 | -6.14047 | -57.89947 | 2026-08-15 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cdcddfd-66df-3a80-b7a2-ad27ece8969e | -6.61719 | -58.99683 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 189232cd-3a93-3bf5-bd66-d5a2e9599559 | -6.81288 | -56.43556 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 218517ea-017c-346f-a656-0af6208bfcfc | -6.62061 | -59.04246 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3830a20c-ae8c-359f-9839-908fbda993e5 | -7.40514 | -59.99436 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 381b7a04-67ce-3193-8240-b36f30db5021 | -7.0593 | -56.52064 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec53302d-0415-3cea-9ee4-7b0323431973 | -6.83517 | -56.41911 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9073ad0b-1486-3c10-8d7b-7f2fca11d930 | -6.59971 | -56.36524 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2cb65b9-661d-31fc-aa3e-ca6f47bc0c31 | -6.85918 | -56.41768 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| daef8895-a4b0-3e3b-ae07-148de2a15ca5 | -6.8313 | -56.41847 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1360bf85-21fc-3178-bcad-303384a7dc32 | -6.79654 | -55.84859 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f4ec09f-35b8-3961-b053-4c7d0a22df49 | -2.80874 | -48.59003 | 2026-08-15 05:33:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31517f82-095e-38e6-b947-c2f64483d350 | -6.85456 | -56.42198 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7e144a34-36d4-37e6-955e-cb5ce5fd5b29 | -6.61437 | -59.06021 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3f0bb50a-502e-3c61-b2a7-51ef753cafc3 | -6.24682 | -55.62011 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 32a1a09b-e374-30af-8cb6-efcfc3eb31de | -6.61664 | -59.06804 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5a83d8ff-ce2e-3676-9f24-4bc38d1ec22a | -3.59578 | -58.62245 | 2026-08-15 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 791f2f72-6787-3e55-8a31-cc3ed797c58f | -3.27585 | -60.17 | 2026-08-15 05:33:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83457799-4fb5-3167-b2f5-48be33a13153 | -6.77385 | -58.75002 | 2026-08-15 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6fbf66d-2f3c-3b97-aeae-4ce57c5f4831 | -6.93682 | -62.8736 | 2026-08-15 05:33:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 55c1d068-6322-3c0e-af72-3da0ea5a8163 | -6.0253 | -57.82507 | 2026-08-15 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 38bc3045-9c7d-3459-8321-a11969097b19 | -6.60359 | -56.36583 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93dd14d2-2af9-36b3-8acc-021c4a97d3bf | -4.10798 | -50.99154 | 2026-08-15 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f9b6f447-2f92-3d24-9039-6dbdfd236b94 | -6.79513 | -55.83047 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7c61498-52cd-38b8-bbd5-c68eb575e3e7 | -1.78317 | -55.52936 | 2026-08-15 05:33:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3624ed2d-6e7e-3493-bcc0-cbf7438ff1f6 | -7.45884 | -55.30218 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ca63b350-634a-3e06-ad42-2843feceb125 | -3.94417 | -59.62861 | 2026-08-15 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de9cbfc2-2d9c-3ca5-b8cb-80b5a2ac051e | -6.78709 | -55.82925 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f842db57-5f51-340b-8140-bf4010496485 | -6.93275 | -62.87681 | 2026-08-15 05:33:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d57e8950-e2b9-369b-b3f6-87e54bd9d88d | -6.53918 | -55.17873 | 2026-08-15 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c342e63-2193-3d3b-a047-a7a244baa5c7 | -6.85478 | -56.42376 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f53dda1b-9433-32a3-9dd8-5618bcf79f5e | -6.61093 | -58.9921 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d0a898bb-1eb6-397f-87c7-63240a8786eb | -6.84606 | -56.4257 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 32477095-2ec7-35fd-886c-37dab7b5ac95 | -6.88968 | -59.0189 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68ca9b9f-fdad-3dbd-b7f9-85fd5cc21f57 | -6.96185 | -59.29252 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07b802a1-e877-3ff0-8613-03d8f090f1eb | -8.03228 | -55.13854 | 2026-08-15 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fa910073-1b16-3f4c-84fb-043cd8e3ce8d | -6.61435 | -58.99262 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0454bc48-a4b9-3ddb-9ebc-3f60af84993e | -6.96662 | -59.28913 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e22181d-b19d-3e36-8387-ee21c3921d4b | -6.95678 | -59.28059 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c507b3ea-4884-3c29-8d47-e68c1b868e24 | -8.02798 | -55.13801 | 2026-08-15 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d1667dbf-b6e4-3ca0-9cd1-ff84139e560f | -6.58572 | -56.35271 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6ce328e-01d9-3aed-af9e-a43d18e5e49c | -6.86009 | -56.41455 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 44110f37-869f-3668-8937-e9c686d6f5a8 | -6.61322 | -59.04507 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 780c5602-07f2-3caa-82cc-c3b0968bcdf0 | -6.79059 | -55.83337 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df3e3d49-b2e1-3ca3-85cc-56a82aaf8915 | -6.63078 | -56.26423 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9da3d456-a068-386f-bfcb-e3134e64ae1f | -6.6012 | -56.35531 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb71aec9-b3d6-3bdc-948f-6ccc33d599de | -8.02053 | -55.12863 | 2026-08-15 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1067f206-7309-38b1-a3aa-4c51a898a830 | -6.01993 | -57.83647 | 2026-08-15 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f115e377-e3b1-3ff3-97ed-e34f15695504 | -6.60045 | -56.36035 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74fb7290-0555-31ed-88a1-139bf009768a | -6.79074 | -55.69249 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd0b5825-9f14-3582-b2f7-0922a5f4acdf | -6.02175 | -57.82454 | 2026-08-15 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8076548d-788d-3ee0-a318-362afb4c9e23 | -6.79479 | -55.69311 | 2026-08-15 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d2f2692-042f-31cf-82d8-d9f22e003041 | -6.53557 | -55.17417 | 2026-08-15 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15feb19f-38e7-329d-a00b-ffafca707b9b | -6.70345 | -58.95652 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 22df8ba7-9cfd-3644-9e4a-db7e6582297b | -6.61948 | -59.07223 | 2026-08-15 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e0c95d50-114c-3ccd-9f4d-74ab797ef4b0 | -6.86067 | -56.40792 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3730fa7f-1570-3bd5-b8b4-c189f8318e85 | -3.23545 | -61.16817 | 2026-08-15 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 523cd1ea-0cae-345d-bd81-e4a6dc6cf585 | -6.59584 | -56.36462 | 2026-08-15 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 750edd9a-e69a-3a87-9abb-2f20a29dde2f | -3.76246 | -59.42905 | 2026-08-15 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0ee6f9b-71c3-31e8-a8f7-2601ae7b5889 | -5.95951 | -52.25778 | 2026-08-15 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README37.md)
