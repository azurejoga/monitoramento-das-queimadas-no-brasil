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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2cdabd6b-5c9a-3544-aeca-2ec263db79cb | -13.11106 | -47.40403 | 2026-09-29 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70c3c359-5f47-3614-a4e8-df93ec8f5450 | -10.40902 | -53.82409 | 2026-09-29 05:12:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd6371cc-56e1-3702-a3ac-9a26ee7420a0 | -13.20453 | -48.56305 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 60a422aa-57a6-319e-b223-1db0a427e8c3 | -9.78926 | -48.20435 | 2026-09-29 05:12:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c5a2d8f-dcd4-3654-95aa-904bd862fbf8 | -11.35272 | -54.10721 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c57e009f-2d26-3a1d-ae8d-94c0a7d8e783 | -12.78378 | -54.02245 | 2026-09-29 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58bb3f45-756d-3f35-9496-56bade45486c | -10.92556 | -47.59091 | 2026-09-29 05:12:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddf28f9d-0069-30ba-9247-192840813f90 | -12.78743 | -54.023 | 2026-09-29 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfc8e894-518b-3f4e-805a-be6fcd45d96d | -11.40156 | -45.41701 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31ac60c4-1e03-330f-ab16-587455fa2037 | -9.92909 | -60.72184 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c962dd19-77d2-3a2c-bfe0-266d660a9f50 | -10.24973 | -44.60468 | 2026-09-29 05:12:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5579d493-e4de-3986-9806-8bc75f8f4bdb | -12.31656 | -46.41108 | 2026-09-29 05:12:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20da9791-4366-32b3-94b4-e3b054a50c96 | -11.44702 | -43.48255 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1076d3af-3668-3cbb-9849-2917b0d1cde7 | -10.72318 | -53.99463 | 2026-09-29 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd3b1434-c282-3b45-9229-6a025c8183d6 | -12.77886 | -54.03057 | 2026-09-29 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 169e5bd9-c468-3a8b-b303-91f44019ee09 | -11.79782 | -49.05788 | 2026-09-29 05:12:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7424a16d-9628-3d49-a4c6-559d2c6c8992 | -11.38286 | -54.05239 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3c1a535-6b7b-374a-8282-273f2d90cdcd | -11.08195 | -47.50451 | 2026-09-29 05:12:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1b64cfa-58aa-3f13-baa9-262d475ebb13 | -12.04023 | -50.94044 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 98605ad5-c3be-39d5-ac06-a74a449f036f | -8.28559 | -54.70658 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a218ab2b-a194-3a89-a90a-58c3dc7b8ae7 | -12.75413 | -50.67044 | 2026-09-29 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d34ad941-5204-3636-a489-ad05ffdd22a8 | -11.95646 | -50.93306 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ab702b71-b7c0-3962-9a9f-a67c01d12720 | -8.28955 | -54.70343 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f23bf8f-368a-3d0e-b117-1ae7e1d0d87a | -11.16967 | -44.80297 | 2026-09-29 05:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| e3208413-edf4-3ae3-a899-1d56a34f6eb6 | -13.06537 | -47.45187 | 2026-09-29 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e653311-3dbd-3c68-8751-782d24b05fe7 | -12.90672 | -52.03999 | 2026-09-29 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d34cc7c1-b411-318d-b5ec-d5ecf162ec13 | -12.01368 | -50.97167 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e19875f8-d7cd-3204-9b38-20e850a9bb78 | -13.53412 | -49.17747 | 2026-09-29 05:12:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f619ea2e-875c-317e-be88-04ea69233c74 | -12.04225 | -50.95821 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4598caa1-13e0-36b8-a489-4cbe637998b2 | -12.60498 | -47.28927 | 2026-09-29 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 825b31c2-fefa-338c-bdaf-a5153cc4ec32 | -12.90723 | -52.03622 | 2026-09-29 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc02100a-5cdd-3cd2-933f-fb17922477ed | -10.412 | -53.82879 | 2026-09-29 05:12:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 556a4813-665a-30eb-8dc3-e11c01b469c5 | -11.14469 | -49.05257 | 2026-09-29 05:12:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 79325d91-989b-38a5-80d3-f8e71382a3b9 | -11.90504 | -50.61002 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fb8e75b3-9f77-386a-9d99-11c70ed1823c | -12.77315 | -52.81408 | 2026-09-29 05:12:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f005a210-6f8c-3422-aa3a-15f38e55b235 | -13.55855 | -48.93871 | 2026-09-29 05:12:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b25b8b0e-db16-3c98-97c9-6c0f41055fd6 | -13.17313 | -48.55898 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c700e74-1dcf-302a-8134-ea9627b2b87a | -11.34017 | -54.11792 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f77c61f8-4f65-339d-928d-7ded826390b0 | -11.4164 | -43.43729 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dea4fb80-442d-34f4-89f7-bb59e7c499d7 | -11.35896 | -54.04023 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 069fff28-216a-3434-9349-5fcc8d73453c | -7.49939 | -55.03379 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc2f3baa-7a56-3fe5-87e6-2e2c30c2760e | -11.50462 | -47.39934 | 2026-09-29 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9f3918d6-02ae-3a19-92c6-4cfb30be9751 | -12.55707 | -47.16011 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f47b1b3-34d2-305f-a15c-0088f5624f04 | -9.54071 | -56.15995 | 2026-09-29 05:12:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c818761a-1fa5-3867-ac0c-90eecf992c09 | -10.39079 | -61.2644 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3dd49ee-8af4-35dc-afa9-128f49a060de | -11.42264 | -43.46613 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 80e5a985-8324-3fa1-bdb3-9a7e12d3feeb | -10.38696 | -61.26366 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cf9808c-1228-3743-af5c-1ba212a25ef5 | -12.74154 | -47.27565 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b5f454f5-9214-393a-8736-471e15cbea7d | -11.43052 | -43.4389 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5c789cb9-7bd5-39e4-b59b-19bf6d4c9a79 | -13.53341 | -49.18318 | 2026-09-29 05:12:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2dd674ed-dc13-31d9-8501-18d6645b7a1b | -13.06141 | -47.45624 | 2026-09-29 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d5a84186-4d2e-366b-b351-c53bc4ac1139 | -9.68702 | -58.1216 | 2026-09-29 05:12:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 44fafd6a-8dd7-3bdc-b03d-8a0fe19be428 | -11.33598 | -54.12148 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb41567e-8dc1-3c19-9358-1f9a8ccae1c4 | -11.38051 | -54.0435 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c95fc00-65a4-3ce0-a89f-28e6001a7705 | -10.39237 | -61.25536 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 26cf96f9-3de2-3561-bf25-98483355685a | -10.71852 | -44.43697 | 2026-09-29 05:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c60a1ba6-128d-3689-a23f-79b085b9e7f1 | -12.24115 | -50.43023 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4a764c80-bdd8-3148-8918-f8b87c05f1d4 | -11.42666 | -43.47341 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| fcc2959d-7710-3a1c-94db-a2cf9eb7fecd | -11.40857 | -43.44355 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a74a6a2-0412-39af-8cde-e9c6bd95b879 | -10.42365 | -53.77504 | 2026-09-29 05:12:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fea51e74-c2ab-303b-97e2-d0bad76a3683 | -9.09123 | -49.88687 | 2026-09-29 05:12:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abeebcf1-742a-3ee4-88c2-5b3e27ef0bb6 | -9.82445 | -54.66679 | 2026-09-29 05:12:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec404b0d-aed6-3cd9-9517-7ac8007376e7 | -12.94898 | -46.64281 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 87955915-f5d0-3573-818c-9c176581bec3 | -12.56088 | -47.15675 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ad4f972-c364-307f-a543-204e1e8a34f6 | -12.74017 | -47.28677 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b98870ba-29a3-3f4c-8247-40ac032aeabf | -11.80278 | -49.05856 | 2026-09-29 05:12:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f143cbd0-6b75-3855-851b-ed88963e1637 | -9.16486 | -61.41214 | 2026-09-29 05:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e962827-8f5d-3320-a50a-9ec8cb68d5cf | -7.46379 | -55.00648 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cb00bf3-e9f9-31dc-8613-90826446d12e | -11.38831 | -54.04043 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b44377e-e864-300a-bba7-cf4c8f6b88ff | -12.17696 | -50.69431 | 2026-09-29 05:12:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22a0417f-7cdc-34de-b352-ea51f217ca95 | -12.90261 | -52.03933 | 2026-09-29 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aca710a5-713e-38b4-bff7-beec8dccd4f0 | -13.20975 | -48.56385 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5f2cfbec-c91e-3405-becf-d659e215215a | -11.50687 | -60.73745 | 2026-09-29 05:12:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b89579e2-782e-3ec4-8c06-aef45926efaf | -11.08737 | -47.50547 | 2026-09-29 05:12:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 216178fc-7dc8-3879-826c-6dc97b827dee | -11.33362 | -54.11271 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45c0e555-ddb6-3823-b360-09396a049223 | -11.54694 | -54.50079 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6524602-f4a7-35ae-afd4-7daf705fdcc3 | -8.28275 | -54.70236 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 018fe9fe-1b9d-3978-b662-2546c390e943 | -11.95703 | -50.92875 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 958f908c-7439-3e9b-8f2c-f29d6e354c4d | -11.99976 | -51.0088 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10c68121-fc52-3b4c-964c-0119a93e6f5f | -11.3763 | -54.04709 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34be4022-a717-36a2-94aa-9524a8eecb90 | -10.81767 | -48.71632 | 2026-09-29 05:12:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cfb9ee93-f070-363a-8113-61b9315bfbbc | -10.42573 | -53.83519 | 2026-09-29 05:12:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 045361f4-1a93-3771-a813-9d3a2d6ea9da | -10.82209 | -48.72152 | 2026-09-29 05:12:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 011f834c-43ef-3072-908b-f809c21c702e | -13.54447 | -49.17668 | 2026-09-29 05:12:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1c4168de-0168-3549-a7a9-c6f2d074dbdb | -11.99909 | -50.9478 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7768cab-fe1d-3203-b51c-2efdc891e509 | -9.96339 | -50.16769 | 2026-09-29 05:12:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3209c816-afa8-361f-8aa6-b3d6930094f1 | -12.72394 | -46.98935 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 42451cd5-f74b-3fb0-9f0d-5473632faf5d | -10.3987 | -61.24172 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b81c47ec-b95d-3142-bf57-2fd33b672750 | -10.26792 | -57.69881 | 2026-09-29 05:12:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59423fbf-8ee0-3c16-8450-902ee9f2161f | -12.79538 | -54.01974 | 2026-09-29 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b14bca62-2c37-3ab7-a804-9873f6b9dd35 | -11.05401 | -54.20015 | 2026-09-29 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24302230-c921-374b-b24c-fef71dccc63f | -12.74337 | -47.28506 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1df43411-b7d4-34b2-999c-c5ff63bcc6d1 | -11.96079 | -50.93115 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d0dd11f-c491-3062-9870-7f3f34599bb9 | -12.02213 | -50.94229 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7b558ee0-c362-3938-9617-18683fec2593 | -11.4164 | -43.45855 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c63315bf-6a3c-3c18-8322-3389ffd02383 | -11.35774 | -54.04852 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ad5b65e-7b54-367e-b442-d773da0e7b27 | -11.80848 | -49.05342 | 2026-09-29 05:12:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e2301036-8c0d-3bfe-898f-b96170d62c60 | -11.98482 | -50.95453 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b35bf636-c70e-37bf-83b8-7a4331341780 | -10.81224 | -48.71885 | 2026-09-29 05:12:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d6c48a7-ba5d-3344-a261-5535f9547d1d | -10.7972 | -48.75585 | 2026-09-29 05:12:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README62.md)
