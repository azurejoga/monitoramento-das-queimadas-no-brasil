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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 040a46a2-ea82-3ce1-baed-abee75bcb5df | -10.13802 | -46.15279 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41b05edb-d105-32b1-acc2-6ccf2fdbf866 | -15.7956 | -52.22231 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c8bbea2-4143-31d3-9bec-87a3369d452c | -11.26803 | -45.29973 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c6d71ed-ced8-3f36-9623-7037eb0336d6 | -9.85043 | -43.15856 | 2025-09-15 04:21:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f31ee195-faae-3e1d-8dd0-00be00249bf0 | -11.49968 | -43.70421 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c1528fe-cdfc-36eb-a0c8-9353cd5d7550 | -10.66852 | -46.24188 | 2025-09-15 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4ad9444d-33cc-3437-877d-10b57266d529 | -10.76263 | -50.63774 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 235fe897-3ac9-3fbd-bbc5-fe2bcc84c7ed | -12.11896 | -44.82727 | 2025-09-15 04:21:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a43ea57b-42e4-3563-be03-784bffb4e679 | -12.43817 | -46.88612 | 2025-09-15 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24969c75-e045-3c5f-955e-c98cb97bccbf | -11.7912 | -46.65253 | 2025-09-15 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47ab3a76-e16c-35f7-9048-8e416700c695 | -12.67033 | -47.72552 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a14f52f9-5f54-3c76-8cb3-0c615b405208 | -11.85679 | -50.53304 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee94aafc-4e62-365e-ba77-9c8d05be1f4f | -11.87222 | -50.52287 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.9 |
| f0509305-579d-3407-bddf-9add1e54afe1 | -14.94028 | -46.5547 | 2025-09-15 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d5a91017-5c60-3b3e-8503-6cb83c011976 | -9.55157 | -45.94336 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c66265b-20cc-3e27-be4e-e78cd3e338a9 | -9.36376 | -45.38577 | 2025-09-15 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4b0622b5-95a7-31ee-b1a3-ba514169ba5d | -16.07486 | -47.96569 | 2025-09-15 04:21:00 | NOAA-21 | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30a88632-79d6-3da7-975a-5727b1867638 | -10.07737 | -47.1941 | 2025-09-15 04:21:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dacb4be6-991a-3f2a-a748-c0e8fe2730d4 | -12.12067 | -44.83858 | 2025-09-15 04:21:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce663846-8cbc-3a66-897f-4181dc97081c | -12.42468 | -47.80164 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10635843-2106-3bc8-a3f4-9b2102255db3 | -14.93092 | -46.57133 | 2025-09-15 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dd7af334-8015-3f35-80f7-31ce2d1082e7 | -10.79767 | -45.98396 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c1fc076-5cbe-38c3-85f8-33cdd3e093f5 | -11.08235 | -49.73022 | 2025-09-15 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f166cf4-d5eb-3793-a87c-61ebb9640467 | -11.12937 | -45.31694 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00dfdf0b-ab41-3751-addc-c9977e9b054a | -13.89454 | -44.87122 | 2025-09-15 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 587fb451-e04a-3105-a7de-5300f791fab4 | -11.77563 | -47.5583 | 2025-09-15 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7ec2a81b-26a5-3986-bac8-a5d56d22e0f6 | -10.89528 | -45.44519 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9edf3e30-fdd5-3106-8c86-51c969903720 | -14.25225 | -48.83617 | 2025-09-15 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 835e5ae4-07a5-36d0-861b-e5397623b9b5 | -13.93274 | -44.80093 | 2025-09-15 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83b1a874-d3f6-3876-8ce4-50644ee23524 | -12.96556 | -48.00472 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 07f808d9-d0c2-3ea9-ace2-cf3bb3b572d2 | -12.13847 | -44.8119 | 2025-09-15 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| de098fa4-f375-3ec0-bd73-4bfc95ed14c2 | -13.87253 | -48.13024 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b4678232-93b6-3bcd-825d-b9899f77efdf | -12.17384 | -44.09383 | 2025-09-15 04:21:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc17a876-aaa6-3b04-bcdc-cc0692cd92e3 | -10.74992 | -50.64082 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1b6bfe8f-8dfa-356e-bd7f-de60460716ff | -13.88602 | -48.13256 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 30e577fc-e520-33ab-a6bb-89774c3c6a1c | -13.89573 | -48.31413 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e8bd3be3-ed51-3de9-a04f-9b0bf0e1b584 | -12.55772 | -45.6462 | 2025-09-15 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de99ccbc-a2b9-393f-b7ee-e9a36c11fcdc | -10.63877 | -46.23715 | 2025-09-15 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 32e3d6e0-00b6-3073-93ed-7a272bae905d | -10.75607 | -50.65252 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a147eb7e-ef8a-3e90-afcf-80e98ca132b3 | -9.12914 | -46.95066 | 2025-09-15 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97553a7b-ee90-39d7-b5a2-3140a960ae7d | -15.09941 | -52.48116 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33363ddf-9b07-3eac-bf5e-f64bdc8caa2b | -11.27742 | -45.30482 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2180d04e-3bc5-34f5-953b-99fd9d73acd9 | -14.82363 | -51.62553 | 2025-09-15 04:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fb2e1047-9bbb-3b9a-8c49-eb5910b9baef | -11.7503 | -50.49587 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41d5d028-2060-3102-b99c-90343f9f921e | -14.94853 | -46.56693 | 2025-09-15 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 673e0a0a-a629-3469-a286-11ddc9e15206 | -17.3455 | -42.64713 | 2025-09-15 04:21:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b22485c9-17e6-32a4-b93b-30b4828051ea | -12.64606 | -47.93732 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6fcdd3c1-4303-3632-ac98-2b2be36c7faa | -9.71589 | -46.86052 | 2025-09-15 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13291f3f-9151-324a-bd7d-54140c5a2abe | -9.1413 | -46.98255 | 2025-09-15 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e16723ce-9942-3391-a561-70182aa5bd87 | -10.75141 | -44.69929 | 2025-09-15 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69455147-5d2d-3030-a48b-46dc71f54a0e | -9.17642 | -47.04436 | 2025-09-15 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 16b17619-4581-3967-8231-19fdb394c017 | -12.78384 | -47.97446 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d3d7b753-5bb5-3a0c-b35b-2082737d1af2 | -12.62012 | -44.2028 | 2025-09-15 04:21:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 139e2a8d-2f3a-35c0-bb41-d52aa94e9b8d | -11.13046 | -47.65628 | 2025-09-15 04:21:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da56dd07-cab4-3433-862c-f4aade2e7a33 | -12.59865 | -45.71065 | 2025-09-15 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1bc3e241-e4b4-33a4-a7f2-31a3d91508c0 | -10.75788 | -50.66021 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34ad87bd-b160-3a83-b069-d64406a3f1f3 | -11.08388 | -49.72117 | 2025-09-15 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49a9895c-c1b0-327a-aa9c-ced6a7e9ca3c | -10.15869 | -45.36997 | 2025-09-15 04:21:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28bb3f31-d08f-34be-87d9-71a77e5053a1 | -12.07806 | -47.55952 | 2025-09-15 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7234bb5d-afef-3ec3-9cf7-ccb0ccdbc341 | -16.28266 | -45.68233 | 2025-09-15 04:21:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b749235d-b795-3f3e-8a28-de9087567744 | -13.88675 | -48.30511 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7980cfd6-56f5-3bc2-bcfa-47bfb5b6364c | -12.41413 | -47.5032 | 2025-09-15 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b6621474-6a46-35c6-8acb-5691757be51b | -15.0734 | -47.90369 | 2025-09-15 04:21:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 08cc0268-a688-381b-bda1-0bf28ee28509 | -10.68668 | -46.25564 | 2025-09-15 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eadab24b-a4d7-3118-85d8-5deff8f57e02 | -11.12715 | -45.30937 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a6fed69-aa19-3e10-908f-cc3211c6b794 | -14.20269 | -48.77653 | 2025-09-15 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6f20d176-8502-31c4-beec-d670d737714d | -12.49803 | -44.6953 | 2025-09-15 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a5bf602-2289-3c79-8f05-db77b77003ce | -14.94248 | -46.56233 | 2025-09-15 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33da11e1-29a7-3c83-9e6a-da8e374eeda5 | -13.9031 | -48.31171 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6e853a1b-df2d-3278-acef-00a6b7be53f5 | -14.83452 | -51.63294 | 2025-09-15 04:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8a50c594-2a30-392f-aba3-1faf68303efb | -12.95605 | -48.25399 | 2025-09-15 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba81900a-61f3-3905-995c-8d1b1e534531 | -11.7156 | -50.48978 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 391300c5-35eb-3e98-b569-32b9efcc16a4 | -15.79626 | -52.19546 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00a6a416-22b1-361b-b52d-7e88148ec92b | -14.82665 | -51.63147 | 2025-09-15 04:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 09df73cf-301f-31df-a0cc-427fd7399049 | -14.28528 | -46.12766 | 2025-09-15 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c0bf999f-c6d2-3ae4-9179-228555e10218 | -14.25829 | -43.20339 | 2025-09-15 04:21:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8cb3b262-3c31-3f56-b37b-ad68b6134a5d | -11.26972 | -45.31079 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3dac8848-122c-30d9-9152-b72757620642 | -12.60254 | -45.72935 | 2025-09-15 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9765cf6-523b-3be3-8b07-6f30161a0bd2 | -12.00345 | -47.76214 | 2025-09-15 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 374a23b2-84e1-3cec-a79d-5e02608d4a07 | -12.96007 | -47.99589 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c5a8a68b-5975-355c-b7b0-226d54b99bfc | -14.12323 | -45.18683 | 2025-09-15 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a7833cc-1a98-37d2-8a35-a0b4fd64d2d7 | -12.05396 | -46.54001 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a13345e1-454f-3a02-81f1-21528f241a50 | -9.12973 | -46.94699 | 2025-09-15 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 692771da-a224-32f3-8df4-53738b6be79f | -15.79629 | -52.21847 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71a3771a-e33a-384a-8b2d-810801ed0988 | -13.93613 | -44.80148 | 2025-09-15 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9588d355-dde5-3291-8d99-4240bae40d37 | -13.28934 | -43.79047 | 2025-09-15 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c457ffa-2c64-3e71-8d31-88757f05ccbc | -10.75451 | -50.6331 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c6e78f1d-2f54-3167-b439-e1220e646955 | -11.75332 | -50.50146 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11ce17d1-9ebe-3146-9fac-569318ba13a4 | -13.64613 | -46.99445 | 2025-09-15 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2881003-3029-3f39-bc1c-410d8fc2c29b | -12.6731 | -47.72975 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 52bba141-8674-3e56-937e-91fba4f2206a | -13.86915 | -48.12967 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 617e2abf-8a6d-3ae7-9231-7fa6174c8b66 | -14.50862 | -47.35018 | 2025-09-15 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b988843-9376-368d-bd92-863f943ba5c2 | -14.30506 | -46.04336 | 2025-09-15 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e4046ba-cc24-3bb4-bf3a-9242b12267eb | -10.7615 | -50.63961 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 35015605-7b00-37ba-a616-5abe036e3bf5 | -11.47991 | -43.59825 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 238eb9c4-2cee-3805-ba4e-ab7873ebb8ce | -10.10124 | -48.34018 | 2025-09-15 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e55215b-aa60-3709-892e-ed7366462be2 | -11.99531 | -46.65334 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d304bb95-2656-3a5e-9c42-5a84dc9b1038 | -12.00799 | -46.65901 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6a461a2b-7bcd-3261-8e5f-8d6a42a2b1a7 | -13.93952 | -44.80203 | 2025-09-15 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 36741bb0-b831-31c9-bedf-315a2ed84906 | -13.94686 | -44.79937 | 2025-09-15 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README34.md)
