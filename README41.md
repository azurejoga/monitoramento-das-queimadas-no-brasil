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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6af909b1-8d73-3dc1-9a52-e431dc513694 | -10.7771 | -50.82679 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a91a71aa-7cf3-3508-87ef-68455fafef0f | -10.4742 | -46.28905 | 2026-09-21 04:21:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0dd1af5-86ce-391f-a2c3-f0e080b9cf7c | -13.34344 | -51.30304 | 2026-09-21 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aec7b997-7d24-38b4-8b11-06826814a11b | -10.48977 | -50.30951 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0be0cdcd-4f71-3dab-b90e-d0e39db721ff | -11.95216 | -46.49748 | 2026-09-21 04:21:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e1dc7f3b-bea0-38d2-87cd-9565538498dc | -11.05047 | -54.9166 | 2026-09-21 04:21:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c018727-e77e-35ae-a0c2-fd865fda9d36 | -12.29344 | -50.16547 | 2026-09-21 04:21:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d17eef3b-6bbf-319f-8084-9d6a92c4c81f | -10.5842 | -57.49881 | 2026-09-21 04:21:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 029662fa-41a4-37f9-ba35-fe69f51cdc5a | -9.68169 | -54.332 | 2026-09-21 04:21:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65eacbaf-15ed-3f22-8ffc-8f27d8344c9e | -15.46468 | -48.47376 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bdd0b768-165e-393f-bce7-c2a411917540 | -8.16917 | -54.76736 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fd913574-4802-3997-b8a2-5307bb5ff385 | -15.17319 | -48.16872 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82324a81-29aa-3b01-8f6f-0689d810bbc4 | -12.1745 | -47.01922 | 2026-09-21 04:21:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 058e618e-67ef-3911-8983-1dee60ee99b1 | -12.32023 | -50.69786 | 2026-09-21 04:21:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 41cfa641-41b3-36d7-8dc8-1906c30ceb08 | -10.88053 | -53.97653 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d6c5b39-1218-343b-9102-af01df8593c0 | -10.75338 | -46.31885 | 2026-09-21 04:21:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae577ba8-feaf-307c-8750-aa7da0c3d6a3 | -10.14718 | -47.67935 | 2026-09-21 04:21:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f3899e9-6514-34cb-832d-f0a96a4da686 | -10.70504 | -50.77571 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 760fc352-905a-3fcc-ad3f-74467a7ce18d | -10.46368 | -50.29281 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0411ad0-ec93-3d83-bb13-0e08d47f0038 | -10.09407 | -48.41093 | 2026-09-21 04:21:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6181e80c-2e9d-3f93-867a-af38b86caf24 | -15.86002 | -49.90115 | 2026-09-21 04:21:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4804c3e0-09ad-3c00-bb79-c088b34e9770 | -9.67938 | -54.34426 | 2026-09-21 04:21:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6f92b83-bb14-3aba-af61-23f441b1a3de | -10.37467 | -48.90952 | 2026-09-21 04:21:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7a14e72-3c02-3580-bb14-53e5ab0d2f2c | -12.1717 | -47.01456 | 2026-09-21 04:21:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c98b7a98-0a50-3b7c-96d3-8020138342e9 | -16.04096 | -52.5175 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| a3ed2bad-1fe9-366f-8cba-1379a3175574 | -11.95434 | -46.50555 | 2026-09-21 04:21:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 59bfccf4-1f0e-3b2f-a425-dfa345ceaecd | -10.77864 | -50.74136 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 035efa16-a335-3c57-885b-a6765f20e714 | -16.05708 | -52.5377 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d40f99c0-cda1-37b3-9ad8-76358ac8ae8d | -8.18014 | -54.74195 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a428df6-00a0-3d40-9ee2-426d286e7cab | -10.69777 | -50.76532 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e25f693-6fd0-3a8b-a4e2-c82cc8aaf44b | -10.40743 | -50.23598 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 94806c71-ab5a-3b58-bda1-0e81dfa0ab65 | -16.10263 | -49.81541 | 2026-09-21 04:21:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5005698-6c5f-3424-bc5d-8ac94e874918 | -14.03989 | -52.07683 | 2026-09-21 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bdf25a2b-95db-3c42-a553-29f86061b4f0 | -11.04488 | -54.15535 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b89a4c03-51b2-3be3-ab5c-c28dc02ab9d5 | -12.17806 | -50.86096 | 2026-09-21 04:21:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8427fa28-4e87-34b7-b1ad-3b78db6d1634 | -13.32683 | -51.29537 | 2026-09-21 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d34073f2-0f27-35f3-a351-39e0005a8268 | -10.88331 | -50.93452 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07bf22bb-1488-3fbe-8d38-d3221a7d841a | -11.0856 | -54.02887 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bd0d068-e377-3bbb-99d3-f0855ccf21ce | -11.79991 | -49.8107 | 2026-09-21 04:21:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 4a3ccc56-7e99-3d7a-a7ce-5039f6e020d7 | -11.79435 | -51.13169 | 2026-09-21 04:21:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d9b36ec4-75cc-3c6b-8ada-432f508d4188 | -10.38753 | -50.22393 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2860b43d-a6f6-39a6-beca-c6af911a61f3 | -10.88594 | -53.97768 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f339af12-01a3-31ea-8ba1-ecf2b744f68d | -10.15659 | -44.82832 | 2026-09-21 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 01647cd8-c6ab-3c6b-9a38-d8d40291bf22 | -11.0493 | -46.56674 | 2026-09-21 04:21:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 46dc7ea7-3cdf-3d5e-ba66-0058ed65ef62 | -12.30082 | -50.7323 | 2026-09-21 04:21:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e5f1d24-fb50-3b3f-9981-7c4a6f9f4447 | -11.43263 | -47.31182 | 2026-09-21 04:21:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89f5b26d-0657-35e1-abb1-525a6d27c09f | -11.31479 | -47.29978 | 2026-09-21 04:21:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8dcf6042-cfd8-351a-9e69-f6926b49575e | -14.41065 | -47.26992 | 2026-09-21 04:21:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d21cae8-fb86-3408-a650-ae3b875971fe | -11.93384 | -46.50197 | 2026-09-21 04:21:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b7d01b3-4552-32ca-8d7d-483c7ec73c15 | -11.88935 | -49.00564 | 2026-09-21 04:21:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59098b28-6aa6-3e18-b255-dbf233a08dcb | -10.48548 | -50.30872 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a43ff77f-0ee1-3171-98a1-99197278268c | -11.31833 | -47.30044 | 2026-09-21 04:21:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed21e7e7-a022-39f0-997b-e99d36ef1446 | -16.04541 | -52.5255 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 896b3fc8-9e26-3337-8a89-fe024752f0c7 | -8.17431 | -54.77295 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f36b3367-be3a-3aaa-a3e2-2f897ba76481 | -11.2779 | -54.12991 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0282163c-05fd-33e7-8709-a78cb4df7691 | -10.53435 | -57.45005 | 2026-09-21 04:21:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1cedec2d-54b6-35a2-87e7-dbdd42d843a0 | -12.91396 | -50.97303 | 2026-09-21 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a3422f23-46e4-3342-a049-17ac83a7c041 | -9.73448 | -48.15179 | 2026-09-21 04:21:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93772951-c01b-3b10-896e-b1c625434141 | -10.39889 | -50.23442 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3c48d526-b1de-3e09-a4da-d1f4ebebc257 | -11.89018 | -48.99366 | 2026-09-21 04:21:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 039d9146-6c14-33ff-8d04-08bd149b6360 | -10.87068 | -54.0565 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 950ebae5-25e9-38f0-ab24-bceb367fe900 | -10.4188 | -50.24649 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0be035e0-ccad-3c45-8b12-fba3efdb87dd | -12.3677 | -43.85894 | 2026-09-21 04:21:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe166531-24da-3281-8335-82e74e9387bc | -10.5816 | -57.50282 | 2026-09-21 04:21:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 55c5c099-7794-3e64-825f-6a81039df20b | -9.76432 | -46.06148 | 2026-09-21 04:21:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc5970e3-551d-31b6-a506-c4a0a943f9e6 | -9.82235 | -48.42752 | 2026-09-21 04:21:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a8aa477-7d42-37e1-a436-18ebec7460d7 | -13.89373 | -48.56639 | 2026-09-21 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e071ba3b-5d25-3a6a-b7e5-abe64e409a76 | -10.78303 | -50.74219 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e8f4ef36-6096-3b46-b9e7-646715b534a3 | -10.7014 | -50.77052 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc4fe6e8-5af1-3d36-88aa-b6b5a87a7f66 | -14.04495 | -52.07045 | 2026-09-21 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc970e0a-06dc-35e5-83b2-ae872edb7262 | -9.98115 | -50.26513 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b63ab5b3-9d7c-348a-9978-ecc93ddb5090 | -15.52136 | -42.65492 | 2026-09-21 04:21:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| b719760c-74d6-3f01-a4f5-a7efe3013164 | -10.67523 | -50.73857 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d38acd07-cc5a-3066-9234-9823d8fa5f4a | -11.03057 | -54.14091 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bdfdc91-add4-3191-ae6b-f47415b1c030 | -16.18758 | -51.12016 | 2026-09-21 04:21:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ff2e026-fb0b-36cf-8ed3-c218313eec7c | -16.04183 | -52.51284 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| c86206d6-1a91-34ac-8ff1-7b775234439e | -10.90223 | -53.9809 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1012b2e3-d334-3c29-8f86-832b51513e44 | -13.72684 | -48.79269 | 2026-09-21 04:21:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 323f13fd-22a3-3da6-9889-b40ccaa503fb | -11.0876 | -54.01818 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6ca93e8-87e7-39b4-8218-c123e640450e | -10.72912 | -50.71423 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a0729d80-37a3-3700-8075-95dfa826b45f | -11.04476 | -54.91525 | 2026-09-21 04:21:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 034f2b13-4ee2-3a97-8dab-b64393b2c309 | -12.79845 | -54.05547 | 2026-09-21 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21dda8e2-8796-3eb9-92f3-cc429b106922 | -10.88121 | -53.97305 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 458d9134-7a40-3ccb-85f6-2f9575542806 | -11.94936 | -46.49311 | 2026-09-21 04:21:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69ae6621-e630-3b34-b972-596a35e2912f | -10.78665 | -50.74736 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b6ecdb1f-6883-3051-8ca8-b03227e68617 | -13.32957 | -51.30481 | 2026-09-21 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1d7cc0d3-d56d-3377-8b61-a1db3d16d62e | -11.09339 | -48.31275 | 2026-09-21 04:21:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 826ebe14-3f8f-357d-ad2b-e4ced94930db | -7.58394 | -57.69801 | 2026-09-21 04:21:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4184c767-3e5e-3737-80fc-5ea7b9358762 | -10.75455 | -50.7999 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| eb340b96-b6cc-330d-8d0b-6484a0a35ef1 | -9.68096 | -54.33587 | 2026-09-21 04:21:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 625da31a-4e52-3e85-b065-35b0372135ec | -11.0415 | -54.90147 | 2026-09-21 04:21:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4a98016-6901-3481-9171-d0ab4ec568dd | -11.95837 | -46.50246 | 2026-09-21 04:21:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b60d59a3-ad9a-38e7-8350-b06b19e7acdc | -9.65898 | -54.32771 | 2026-09-21 04:21:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f11ac79-26a2-3814-8926-925f30edb37c | -9.82284 | -48.44752 | 2026-09-21 04:21:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21e9a80c-6e37-3f1d-a3d7-8b89658b724e | -9.82368 | -48.44268 | 2026-09-21 04:21:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ffcf5f44-2cb5-366c-88cf-1dbb3892d970 | -13.27561 | -51.76488 | 2026-09-21 04:21:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8f31957-71bd-3ad7-bc01-44a961747a99 | -16.02575 | -52.50654 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 24fc4101-7ca9-30c5-86fe-199395240fae | -16.16952 | -43.76775 | 2026-09-21 04:21:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82c16004-2987-3788-b961-8494465aa7e7 | -11.02552 | -48.32212 | 2026-09-21 04:21:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d1ebc086-0f64-3757-8fa0-3db3c1185c0e | -11.0457 | -54.15228 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README42.md)
