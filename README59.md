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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d44833b-ba98-336e-8920-6f28951978ef | -10.5115 | -44.87008 | 2026-09-23 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9518339b-01c7-3f12-bba6-20dc30ad939d | -7.18773 | -47.44182 | 2026-09-23 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ee152fe-ddde-39cc-b2cd-d7d690af42f9 | -10.1185 | -46.08726 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc0cb76a-10e2-3538-8c4d-132c19875630 | -12.184 | -50.12206 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac685778-4cd4-367b-a64e-7545e0be4fe5 | -6.63325 | -59.92781 | 2026-09-23 04:27:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 030f5a60-d3ec-39d4-894e-9833488752af | -8.30801 | -50.81272 | 2026-09-23 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 52318eac-c326-3afb-a5b4-7a03cd2c8057 | -9.60111 | -43.95503 | 2026-09-23 04:27:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fee3dceb-f89a-343b-8911-fd801ca5627d | -14.60457 | -45.62212 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e183d3c0-a129-3107-b47d-30616a99850a | -8.83504 | -50.48933 | 2026-09-23 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3366986d-4cf9-31de-8b7f-32a3938cf3f4 | -11.65849 | -43.47492 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 46d21c9c-29ca-35ff-b219-76f65fb4f5c8 | -6.92734 | -46.56538 | 2026-09-23 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e85f27f-e604-3166-bb2e-acf2c34286ee | -10.87231 | -50.15121 | 2026-09-23 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27b89c17-7c9c-32aa-8728-2a51ba1f6e3f | -11.28523 | -51.33435 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ffc0d3a-c0ba-37ec-ac14-5b51280058fc | -7.41831 | -42.64651 | 2026-09-23 04:27:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bceee633-eb90-3b89-a0b0-cfb24814b4cc | -12.69383 | -47.00565 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3d23522-ebab-3761-8cb7-9ada0e3ea667 | -11.93392 | -38.28812 | 2026-09-23 04:27:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 51abf40e-d09d-32b9-9dc1-49d9d864df3a | -10.25114 | -50.00215 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dbf81d9e-78d9-33fe-a4e7-8d22a8d39d50 | -11.87902 | -49.94468 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b93e921-34c3-3caa-a001-5348a93cc81c | -8.44916 | -55.02418 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45db5bc4-d441-3141-a89a-8c4f4e8ee633 | -11.70815 | -44.50633 | 2026-09-23 04:27:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 892a1ebe-5f47-3d77-8e92-1d15316701d4 | -9.94422 | -48.47326 | 2026-09-23 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7b3b92be-d1b4-38a6-8913-353cdba7ad1f | -8.4972 | -57.61627 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ac750445-e2f4-3c35-a412-6656bb66e400 | -11.40018 | -46.73235 | 2026-09-23 04:27:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5dff57a9-93ad-360d-96e5-e2a66cd5172f | -8.35807 | -45.62194 | 2026-09-23 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9671ec87-41c2-35a0-9e0e-9ab6a1c7d5fb | -11.65603 | -43.46484 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b865776-e317-3876-aa05-1dbb5de0a48d | -6.66403 | -55.06441 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f3304338-f629-337b-a187-a62332597f13 | -6.66757 | -55.06292 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1d3a1c0e-f142-39ea-89a7-b3289b67d70c | -8.33853 | -47.24344 | 2026-09-23 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70506eb8-74d1-32c4-a3e8-a1871dbf4784 | -6.09774 | -57.67395 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 76f3aad4-1ab8-3572-aa67-09c01cdf448a | -11.15551 | -42.8399 | 2026-09-23 04:27:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ce93537d-1510-3e81-b6d0-6f4dd9b81612 | -12.74408 | -50.8875 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d7a0eefe-05e3-3322-aa49-b2ac81d9dce4 | -13.03734 | -46.91282 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfeff584-445a-3ccb-af33-f7e98c407787 | -11.89078 | -45.76425 | 2026-09-23 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 543fa7d8-47cb-3937-93d4-60fb7ca4f8e9 | -6.66868 | -55.0679 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25f4ba91-0077-3c91-b2b2-93ee605dee01 | -6.9404 | -52.60274 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d8b8426-4735-3873-b52a-16928f5a7d60 | -7.5621 | -55.02183 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b068bcd2-c0bd-3853-bade-e268f459788f | -11.46399 | -47.37746 | 2026-09-23 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1d52165e-f1fc-3fa5-ae42-406f46f72866 | -14.59165 | -45.63686 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebd33c94-e5fd-33f3-8856-1958980670f7 | -6.62752 | -59.995 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8671aa6e-df6f-31b6-992b-0b3595fbd157 | -11.43217 | -47.38309 | 2026-09-23 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4782b6e6-e46c-3a7d-9ed2-c47195d2eb03 | -11.12267 | -51.05064 | 2026-09-23 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d46f977d-cd48-35c3-80a7-095148d4ebb9 | -14.63757 | -45.64707 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7e1d2f2-6316-39fe-b5fd-54999fd277db | -14.63033 | -45.64273 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 9f5c09e7-0b30-3c81-b10d-1d496557fda7 | -9.35379 | -50.09243 | 2026-09-23 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6582d06e-e48b-3e52-bf80-40a8a368b90f | -5.88612 | -53.62042 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69733120-a0b6-371f-9945-b35e094bf1d4 | -11.13564 | -42.77972 | 2026-09-23 04:27:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 299a4c83-b65c-3a07-b8eb-9beb4e9fbf17 | -7.82047 | -46.63907 | 2026-09-23 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9335d895-68da-32c3-aab9-9f6d5e5ed2e0 | -6.73512 | -55.09654 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 157b5984-efac-3e75-884e-58ad1d8caa91 | -11.09785 | -48.34295 | 2026-09-23 04:27:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36ae721c-dfff-356f-af92-5b2a15b317d4 | -14.39524 | -47.25585 | 2026-09-23 04:27:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab19f095-5488-3b34-8de5-2057599171ca | -10.02628 | -45.2052 | 2026-09-23 04:27:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ab5c52bc-942e-3012-b722-d7a70172eb25 | -6.03946 | -53.27372 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 50011f82-cba6-3630-b7c8-ab03449d59d9 | -14.60571 | -45.63901 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 6d11f340-1ebd-3e95-b692-ba84cbd34dbf | -12.51312 | -46.96571 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 038b0bf8-e1c3-3d13-bc82-fecc185e46c8 | -7.33384 | -55.5968 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8678b24f-7d93-3826-bf07-9355a8877414 | -6.66913 | -50.9465 | 2026-09-23 04:27:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2269a47d-da95-381f-be6f-16ff63e56a4d | -6.19821 | -57.7812 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16b9f7ee-c599-3252-893a-b6982d59ec0d | -12.05885 | -50.35962 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9571e080-02ed-384e-a9cc-e75bf97c44f5 | -8.77496 | -45.62699 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6d5d495e-5136-3954-8c87-4aef2d2687e3 | -12.84496 | -50.87056 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69b9740d-abfd-3292-b113-3ce260f43818 | -9.57206 | -47.96479 | 2026-09-23 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87c4e96c-f86a-364e-8637-911d24c19ad5 | -12.67965 | -46.39968 | 2026-09-23 04:27:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a69b21f-b275-3f83-9493-333ae6feb029 | -6.74016 | -59.42499 | 2026-09-23 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81b909e0-ce54-3a10-ac29-20edce1891f4 | -9.83933 | -46.38247 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f648809d-3c4a-3b88-a77e-5fd62963922d | -11.18728 | -48.03583 | 2026-09-23 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e2f61f90-94be-3838-9a69-5f895aac9c25 | -10.91101 | -53.94007 | 2026-09-23 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 72996331-5feb-33d4-ac2c-57668ed213b8 | -9.58151 | -46.5331 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1bb827fa-eea1-3603-84ee-84a841f9d550 | -8.25207 | -50.86649 | 2026-09-23 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a7b2ba14-b16e-353a-8f16-386b552ee789 | -11.45906 | -47.38742 | 2026-09-23 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 44ecc4da-15f6-3942-9086-3f378015dac3 | -6.92896 | -46.55502 | 2026-09-23 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf3caed3-6cb6-3568-92af-d5717ce1e753 | -10.31958 | -50.50713 | 2026-09-23 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21343085-6432-3e80-92a2-50ae8b7a06a9 | -6.68084 | -55.05804 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| af614d44-f687-3271-9c67-4a65b93bc123 | -5.81974 | -57.74097 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 310f068e-5c12-39c7-a948-2292f810a811 | -14.62151 | -45.65385 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 446e74d6-6195-3904-82be-ac467051e95d | -12.4174 | -46.9691 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 01bbe304-a3e3-315e-a1ca-5c914368cad9 | -6.67624 | -55.05428 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 007e09ee-84b9-3ce2-8f12-6d9206397e21 | -14.63175 | -45.66282 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09635caa-d0af-30d7-b232-9f4becc52cb8 | -11.12998 | -51.05189 | 2026-09-23 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af7b2cde-3a41-33f9-a09b-bda056fbe1de | -6.68334 | -55.06269 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a2eb5ac-0a47-36e4-aa2e-2bf898a123eb | -12.79446 | -50.87073 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0a809f7b-49bd-337f-98bb-7f88c22d54d4 | -6.63125 | -59.93992 | 2026-09-23 04:27:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| fefa8a71-dc21-3f5d-b34a-85d15301d755 | -14.62817 | -45.63735 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7359487d-a963-3fb7-8cb4-26905745de8d | -14.61101 | -45.62732 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 126.8 |
| eb2af453-a993-3fd7-94f4-b6d7706553bf | -9.86408 | -48.31302 | 2026-09-23 04:27:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3e520c2-5b2f-33bc-b5e5-3add25bb9795 | -7.18057 | -48.23244 | 2026-09-23 04:27:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd34b313-8401-3741-b3f3-a09879611bbe | -6.68068 | -55.07767 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 807d0603-13d7-3b2d-a92f-f7352609694b | -10.54337 | -43.98079 | 2026-09-23 04:27:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ed61f6b-24a1-37f0-9a83-9790660ee44f | -12.80362 | -50.8596 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c2a63ef0-2fdc-365f-bba8-142335db8525 | -11.13011 | -42.79322 | 2026-09-23 04:27:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0f7de6ee-cbee-3141-bd34-6c355023d0c1 | -6.09497 | -57.68505 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03582d6b-8619-3e00-852c-a86667dfb1de | -11.93933 | -38.28883 | 2026-09-23 04:27:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 57e965cb-1653-388b-b3fa-7757b572b0c0 | -11.1355 | -42.7836 | 2026-09-23 04:27:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 21121848-5c41-35b2-b16b-5e8992323126 | -11.2978 | -51.35036 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7854e646-918f-3c9f-bda3-19e34b32f7b3 | -6.67371 | -55.0579 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 402d979d-3fba-3c69-b759-992c590bd31f | -6.10467 | -57.67043 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| d9bf2034-4534-3c5d-812b-49b63dad02fd | -11.45728 | -47.3332 | 2026-09-23 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2b366c3-5b6a-309a-8de4-375e9249819e | -12.71847 | -50.88734 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a84d95da-938d-3d47-aa11-53781e2e8129 | -9.99779 | -39.17216 | 2026-09-23 04:27:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 57e994fd-4786-39e3-8738-cc4300188a4c | -8.36396 | -48.54078 | 2026-09-23 04:27:00 | NOAA-21 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b548a95a-b2fd-3866-88d5-e82d69bfea15 | -12.05185 | -50.35844 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README60.md)
