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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb8a1a0a-86d6-33e5-8fb3-db5ec3542f05 | -12.57987 | -41.28118 | 2025-09-29 04:08:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fb7cbee4-3570-3827-b6d8-37e84111cf26 | -14.83528 | -45.56898 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 381593f0-8c15-37dc-9778-866fb65e5361 | -13.76627 | -47.90997 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6ac41a58-098e-3247-ae88-1de73dd8c9bc | -9.30141 | -45.73013 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 002d312a-3ca6-3af8-9bd2-44c812cacb07 | -11.73185 | -45.23475 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16682515-7d1f-386c-9f78-8b62bdf7a49b | -14.56245 | -48.25883 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| eea5d9b1-7276-3deb-98c2-15712fde0070 | -11.7164 | -44.438 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67428c8e-12cc-3e96-90ac-1b132bce0914 | -8.66766 | -49.94029 | 2025-09-29 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67f63f44-81ee-3378-9d9d-f7cd95333b0b | -15.87128 | -46.22295 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b31ebb68-03a9-3166-bd9f-947eca81f6e8 | -7.90775 | -49.19881 | 2025-09-29 04:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20ae37da-9041-3faa-8605-a31563eaabf2 | -14.59064 | -45.01419 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c0f0e1a-56d5-32e0-9e46-67280d47a045 | -15.0602 | -45.05956 | 2025-09-29 04:08:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f9d52a25-3edb-3c20-977d-a3cf65828e7e | -10.08321 | -47.18143 | 2025-09-29 04:08:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f8396da8-98d8-395d-bcd7-1863aea14de0 | -11.9308 | -48.06818 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 39195b85-76a1-334b-9315-20f36c00fbbf | -15.49871 | -45.87974 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af1d48da-6713-397e-9d62-d7024a4520b9 | -12.1621 | -47.77594 | 2025-09-29 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b4953cd4-e0f0-32fe-a518-ae0ed8a56462 | -16.46944 | -43.49623 | 2025-09-29 04:08:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eadfaba8-7301-3ff1-9092-0c13451b5a51 | -15.19678 | -48.47771 | 2025-09-29 04:08:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d6569c6-220d-3484-8e47-442c9b62bebc | -13.22862 | -50.96011 | 2025-09-29 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cd6a393e-900e-3026-b1d2-1d60d0e8d9de | -9.31026 | -45.72259 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dad8444a-80df-3bd6-9ce9-42adf85a5520 | -15.47752 | -47.92808 | 2025-09-29 04:08:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 071f9e2e-a1a2-34d7-9c45-cc54ba9d93b2 | -15.71068 | -47.79995 | 2025-09-29 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa3a146d-137d-38fb-9e39-05f491d8d6c5 | -12.87552 | -46.78451 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f027352-0709-3e92-a85b-0b8ecd069048 | -10.04091 | -50.201 | 2025-09-29 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b4a90710-713e-3977-a65e-1aa1ac350d04 | -12.7589 | -46.85228 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8495fcb3-7a02-3921-9fe0-31b8f226e47e | -12.95763 | -47.20993 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1870b7b-2ea4-31ef-95c5-fa5d2dcc2574 | -9.35625 | -51.48927 | 2025-09-29 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2357c84-35e7-3612-ae0d-931209121f32 | -9.07797 | -47.63356 | 2025-09-29 04:08:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b260d1dd-fca4-31a7-8eb0-69173c9e2202 | -9.88041 | -45.94043 | 2025-09-29 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07cec5c8-2f8f-354b-ab2c-65834437d057 | -11.41628 | -44.91212 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f6858468-2255-3edb-bc76-f4ff1ad6e20e | -12.85009 | -46.97573 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 00ffe33e-39db-3e76-9c56-ebaab9d08847 | -15.2836 | -46.41832 | 2025-09-29 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bc683923-8c9c-328b-9dd7-68ec5ce823d6 | -13.37981 | -48.15335 | 2025-09-29 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| f4f9c333-d119-3bc6-803f-0db770609dcc | -11.26487 | -47.19462 | 2025-09-29 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| a44ad2fa-cfb9-33d7-b1c6-f354e721e4ec | -14.54952 | -48.42172 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42cdffc1-f061-3452-b09e-842404d1244f | -15.26696 | -48.76105 | 2025-09-29 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 94b11100-1385-3e05-aba0-50a160870d55 | -12.87146 | -47.10064 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a9d0e730-275d-3a7b-a840-1229e163f9bb | -8.68144 | -47.06935 | 2025-09-29 04:08:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| afdfef6e-4fa1-33c6-8f2c-09566d5dbbc3 | -10.79858 | -46.68186 | 2025-09-29 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6b55718-4e91-32c9-940b-609bd4c149c9 | -12.8033 | -47.74867 | 2025-09-29 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 425eb1dd-b9c4-3372-9042-06f4b7101fbe | -15.28092 | -49.49589 | 2025-09-29 04:08:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 260f1220-db45-33a9-8dc8-74bab4b06054 | -11.72505 | -44.42796 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a75fa625-ef9d-3e67-84f8-8de25c002d9c | -12.80422 | -47.74349 | 2025-09-29 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4acd597a-ceb3-3ecf-99d1-7c5e72b33f1e | -11.80531 | -51.80623 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5674aaf-5d6a-3024-91ab-40a8e6cc235a | -13.84764 | -47.9507 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b087e7c3-aab2-3d40-8a70-456df6c35a78 | -15.05743 | -45.05521 | 2025-09-29 04:08:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a40e166-3557-37fc-83fd-d92e155297e8 | -15.27944 | -49.50399 | 2025-09-29 04:08:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d74bf15d-032e-364c-a05d-61883a75dd37 | -13.417 | -48.20082 | 2025-09-29 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6dba80a3-b9b7-34de-a420-829a8305be99 | -12.58325 | -41.28171 | 2025-09-29 04:08:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5cb43c47-8999-3c8a-a144-420fbba13bed | -11.44123 | -44.97662 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8745e25a-15a2-3cd9-91d3-80bd72f5a0c0 | -15.40572 | -44.98435 | 2025-09-29 04:08:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6ed1429-d6f4-3e1f-be93-56dd94ad7a07 | -9.75683 | -47.80569 | 2025-09-29 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6a4c2bf-3214-3aa6-bf36-63787d5ac770 | -12.89666 | -47.10907 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 07ca2a13-359b-3f8a-9b67-13711c2a1883 | -16.37054 | -41.58994 | 2025-09-29 04:08:00 | NOAA-20 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 89204316-b21c-3a47-8caa-adf46c9e0713 | -9.44723 | -50.90326 | 2025-09-29 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddae4a4d-7486-332e-8829-9b9b1b7ab0f5 | -10.83174 | -45.4126 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71f8e442-cc3a-3797-aa00-bfe0082c6300 | -8.77839 | -44.94557 | 2025-09-29 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 063f38ea-342f-3581-8bad-96b8ad9239bb | -15.28746 | -49.50425 | 2025-09-29 04:08:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92ee1ee2-efc8-31e7-9d0c-6dd97f7c1328 | -11.92906 | -48.03004 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| eeb3165a-4b8d-344e-8b1c-e7477b6eff11 | -10.47886 | -49.3681 | 2025-09-29 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2139e116-69fb-39c8-af68-65875a5c0f36 | -11.83214 | -51.80611 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 36f170fd-b994-3112-95b8-ac72dedecc88 | -14.55332 | -48.40065 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 79f9cc7d-6ac7-31c3-8ed7-ea43a3f64f4c | -11.48716 | -43.21608 | 2025-09-29 04:08:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6e96b6a5-9864-31b6-9d70-68c5a221db52 | -11.76586 | -47.55532 | 2025-09-29 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c960a14-a68a-3dd3-b3cf-42bb5043c95a | -13.60945 | -48.06429 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 636d40d0-3fce-31e5-b52f-dec5bfa7c430 | -15.21331 | -50.11047 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e0b3add3-8639-3e6f-9400-cc0b08427e00 | -11.98978 | -46.5996 | 2025-09-29 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e59ee68-14f9-393e-a628-9680696a9c67 | -13.65033 | -48.06533 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 20bf3ce5-93df-3bef-9957-bab078f8a05e | -14.55282 | -48.42635 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| df4e3013-2584-36fd-8acc-02670cec3263 | -11.62093 | -52.8569 | 2025-09-29 04:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ad9353d5-bd00-38c7-ace1-9f3218421461 | -10.82799 | -45.39125 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6cda4c4c-525a-3843-bdbe-1d4d9e1cbd07 | -11.47979 | -43.51714 | 2025-09-29 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48dcf538-6b26-35e3-8f1e-ff7a9488f77f | -9.63589 | -48.12502 | 2025-09-29 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 386b953c-483a-36b2-9bd5-1ea7935f94dd | -12.21684 | -43.75254 | 2025-09-29 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70c6807e-b44c-349c-9e92-4d76c62bf3f0 | -11.8236 | -51.79406 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 205fd41b-f2e5-3ab5-a4a8-1b328dff1d3d | -11.99466 | -47.09494 | 2025-09-29 04:08:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 463160e0-8eb3-3f86-88b8-2d89d91ef53b | -14.65079 | -48.15239 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f83c6028-9aea-32fd-9504-6e7d9d59dafa | -11.26965 | -47.19032 | 2025-09-29 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 10817dda-f9ef-350c-9023-6c7003bdf74e | -15.61219 | -46.2545 | 2025-09-29 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4c2803e1-7e62-3d49-8376-4c6b238b06d2 | -8.77774 | -44.94955 | 2025-09-29 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c59c88ff-9124-39ba-b99f-6aa979ce45f0 | -13.80769 | -48.02144 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b0f4a0d-3a57-3b0d-89da-0f285454223e | -10.28407 | -45.19433 | 2025-09-29 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| a3ddfbdf-b2af-329c-adca-04faa1fe62fb | -13.74942 | -47.91342 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7db10026-4d40-3873-8673-0dbca627a8e9 | -15.60935 | -46.2499 | 2025-09-29 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eebbd008-8ef7-3d3f-a7e2-8fca379077f3 | -11.76097 | -47.55981 | 2025-09-29 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d010bccb-652c-39fd-be64-6116f41afff3 | -12.00355 | -46.61402 | 2025-09-29 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00a615df-917d-34d1-904b-e2266e585173 | -11.94402 | -47.89704 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed84c0ed-e077-33a6-add8-2dbcdd70a2d2 | -13.83008 | -47.93961 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc69f1f4-da4f-3712-9a4e-15e9d24a7652 | -11.21326 | -47.74819 | 2025-09-29 04:08:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a44543aa-e286-3179-981d-2281a464a1a1 | -13.58199 | -48.10233 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8774cc7f-2831-3f0a-a1b3-e11398131da1 | -12.94971 | -45.23681 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7708ac41-87b8-3e76-93fd-e3c935bc9c6b | -10.04324 | -50.2014 | 2025-09-29 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c6e7be97-f345-3dad-9d4e-98f0541aa22a | -12.86479 | -44.60117 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82b50251-fcc4-36fe-a557-4e09b16cce47 | -11.91774 | -47.97503 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 476741f1-695d-3ed2-ba22-ad3e29622486 | -15.28644 | -49.51374 | 2025-09-29 04:08:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 3d7463bf-443a-30f5-bed5-4e3deb4f2629 | -12.84929 | -46.98035 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b6e63e90-1a03-39f0-9c9b-7483c3294a5c | -11.83341 | -51.79956 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| dd439773-0870-33cf-a90c-b77d52cb01aa | -14.46781 | -42.17432 | 2025-09-29 04:08:00 | NOAA-20 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 5dde875c-4fa6-3cb3-a3c7-826ea6f6a3c2 | -11.86141 | -56.88921 | 2025-09-29 04:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| aae24734-4f97-327a-bbd0-6f7409fcafdc | -15.082 | -48.3298 | 2025-09-29 04:08:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README41.md)
