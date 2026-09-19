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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1085be8-ecef-39e1-9ea1-a651a741229a | -9.75706 | -45.05029 | 2026-09-19 04:40:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77b363c7-5c6b-3e90-b720-22ec6cf4a060 | -11.02067 | -54.13074 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5789a9b1-746e-3458-8be2-9633263ad7a1 | -9.03706 | -48.75702 | 2026-09-19 04:40:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 714a2aef-81df-3209-9f09-4522c01f989e | -12.83884 | -44.3903 | 2026-09-19 04:40:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42cfff09-820c-3ee6-b5e1-979296bedeb5 | -12.13699 | -47.00828 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2c737a73-f5b4-3a6e-b19f-60198cc2ba1e | -10.45496 | -48.68008 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3d32800c-f3e4-3718-a75b-56bb827409d1 | -9.38736 | -45.36894 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f73d435-283f-3225-a954-0f4e470a5c72 | -14.68127 | -46.67694 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5dbb2c0-6452-36e7-80c0-f0fba73d4ae5 | -11.22694 | -42.82957 | 2026-09-19 04:40:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 813e4670-7215-3442-b2f9-1d4b3d86ce92 | -11.30772 | -46.75599 | 2026-09-19 04:40:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b50b3a25-9f2a-3130-aa0f-ad2cf05aad31 | -11.41182 | -47.28315 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ed690e0-cbee-3c93-a751-46daa79ea37b | -9.91184 | -46.5808 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 017b5774-29de-30a7-8abd-17ef55f425fc | -11.94017 | -55.91624 | 2026-09-19 04:40:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5261a572-8aa5-307b-92bd-fe8391477cc8 | -7.57895 | -57.69318 | 2026-09-19 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3340dbc6-f351-3bd9-a4f3-11ba9ee12e2d | -11.83285 | -46.83562 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2d1113f-cdf0-34d8-97a1-8669b33493a7 | -8.49882 | -57.6271 | 2026-09-19 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 10e152cf-525a-3e75-949e-5cdb739c9c90 | -10.85645 | -56.20141 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ed1710f-10b2-3483-9eb7-d7e515dae0bc | -10.35324 | -49.00159 | 2026-09-19 04:40:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 617f9ded-ef97-3e27-a425-712a13709786 | -10.92891 | -53.96529 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62121f0b-871d-3aed-b6a2-f5bd1e9a160a | -8.78168 | -48.67735 | 2026-09-19 04:40:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c7f4b131-ad32-3a88-b7db-0e6f1687f17f | -14.68183 | -46.67321 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9f488b0-2744-355f-91cf-4e47f224e44e | -11.33799 | -47.36143 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6bb1033-95fb-3c9c-a46d-7c9d82c92b3a | -12.69086 | -45.97083 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| f16727d6-b3db-3325-9231-b6cfbecfc1a9 | -12.12475 | -46.99895 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 207a7928-0e87-3398-842c-8401e15a77c7 | -9.15549 | -49.99566 | 2026-09-19 04:40:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93e42bcd-7a66-365d-b9d3-7b47d298b909 | -12.6909 | -45.9477 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 72c9b3ed-78ed-31a9-bc9d-ed8bbae9b585 | -14.65973 | -46.65819 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 46c804af-2965-34e9-8567-f832d8943b08 | -13.62796 | -48.32127 | 2026-09-19 04:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a18adcd-4f30-316a-90df-77d2e0628608 | -14.7971 | -48.57842 | 2026-09-19 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 474444cb-769a-3dd4-894d-50a443fe1e1e | -12.98329 | -46.97539 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| acb04921-b02f-3c90-8a4c-b7fcd5f2df3d | -10.93585 | -53.95273 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d5c733c5-21b1-3497-87cf-3a37e7d924e5 | -12.34992 | -50.70073 | 2026-09-19 04:40:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d8fac0e2-e6fd-3642-b1b4-fd332a8c161e | -12.28213 | -49.17044 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 21f05c17-7340-3b8f-acf6-6bbbb38da68c | -9.55296 | -46.58862 | 2026-09-19 04:40:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 198ee83c-6671-34fa-8adb-7e1ac19b0fba | -7.56551 | -57.66943 | 2026-09-19 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e2f160a-5ee2-333b-9854-0f571efe2abd | -11.24574 | -54.0998 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 187fffea-caa5-3b25-8fc5-101bdf686042 | -12.39785 | -45.05637 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 242a3859-3002-34d5-95a3-b8106993ccef | -14.16943 | -47.8449 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c10a65c-bb4e-39bb-afd3-3f4b0e03e359 | -11.47261 | -47.40895 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 216ead07-3039-3dbd-bc01-da5ec7971c09 | -11.30287 | -54.88143 | 2026-09-19 04:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98398da4-59e0-3aee-90bb-a8458494610e | -10.46411 | -51.25914 | 2026-09-19 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b1ee36af-8fe7-3b5c-9bc8-f55eec3924c6 | -11.31754 | -47.27508 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c64a64fd-eec4-34d9-8f99-00799bbfda19 | -9.23733 | -46.20336 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 742f78fd-bd7c-36fa-b60f-58359c5fccab | -13.0095 | -46.93906 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 599a84eb-a717-3471-997b-c9d99ab48e3b | -9.56693 | -45.44835 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 158be255-679f-3ac0-bfe8-e3529fff4031 | -10.52894 | -44.84953 | 2026-09-19 04:40:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0844dbc5-1d35-3029-804b-753fe2e0abac | -14.69486 | -46.65618 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fa478530-68ce-376f-a54e-56ceca5f03b1 | -13.01679 | -46.98062 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94374750-1593-37bf-a7e4-52890a352c80 | -12.74506 | -47.01794 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d616a8f7-ac1f-3885-afc2-dc220834a6e7 | -8.84496 | -50.4499 | 2026-09-19 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42338364-5955-358e-aeba-49f61b8a762e | -11.12713 | -45.29721 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43b82787-759c-35f7-8aa8-d35efa526f35 | -10.44877 | -48.67535 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f328c438-8611-3f8c-b412-a1fc5627a0ee | -11.49352 | -47.72309 | 2026-09-19 04:40:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd58ba65-ad59-3e3c-8a29-c5dd6b440e54 | -10.99823 | -48.32318 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| d4e107fc-ad58-35eb-ad32-cd6352148813 | -9.80192 | -46.09559 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb9928a4-f54a-37ef-8a0b-4e84f764c9c2 | -13.88073 | -48.59797 | 2026-09-19 04:40:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9db05117-2e15-3e97-9852-f562469860ae | -10.92535 | -48.4109 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7de7a59c-9bb6-39f7-a336-82b1f896b998 | -11.12828 | -45.28962 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b87a373e-bb07-34fd-a183-b2cba0753f05 | -11.94549 | -50.13835 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 849a7944-cbe1-3bc5-8575-0373d5724a76 | -9.98233 | -50.27679 | 2026-09-19 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08deb7a2-fea0-381a-a658-4b330d877056 | -13.01397 | -46.93233 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b470e094-dd4c-35c5-8070-91b2464db527 | -13.59548 | -46.93558 | 2026-09-19 04:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3674d25-a386-3d7b-b5d4-7658fc3c51f4 | -11.12517 | -47.72448 | 2026-09-19 04:40:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffc1c70f-5c16-35aa-b13d-59f0f252c45d | -11.43783 | -51.46903 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f635abfc-6856-3807-a6ae-54254db62a1f | -10.84595 | -50.18761 | 2026-09-19 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a2d3f70-8e39-303a-ad61-ee140cf8f1ca | -10.47639 | -46.30761 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b7b9d3e-e9c4-3a91-a51a-c1e06f4219be | -10.62772 | -46.05188 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8b29ce93-4dbb-3a73-a296-5c81f536ad44 | -11.55718 | -46.8942 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5af5b89a-05e2-35c7-a149-e09f1f23850b | -9.5746 | -46.55969 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30cef795-e281-32b1-a4bf-0a628aa8893c | -9.74647 | -46.08721 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89db2e4d-1d35-33cf-ac91-0f94bb1b2b0a | -10.93799 | -47.85329 | 2026-09-19 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf3b6131-c788-384d-a0f8-88d942de1db3 | -10.86657 | -54.09705 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d566cf41-50eb-31c1-a52d-50eb796eff31 | -11.43864 | -51.46434 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f64b552d-5786-3fa0-94ba-bff96941a177 | -10.20688 | -46.58117 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f413e26-c776-3561-92dd-09969e582716 | -9.66318 | -54.31411 | 2026-09-19 04:40:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cbdad90-cadf-30c1-8a4a-f704a52c2015 | -8.77948 | -48.66924 | 2026-09-19 04:40:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2ca6f18a-58c1-39b9-afbb-c8fdfff3f139 | -10.75843 | -48.97976 | 2026-09-19 04:40:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e6cef1a-a5a4-3acf-b25f-2027f675a3e8 | -8.77263 | -48.66801 | 2026-09-19 04:40:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c56ede65-ab71-328c-9f6a-2c836936ca21 | -10.13424 | -45.56969 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4df9fdf-dbcd-34e4-ae66-2f38ea976bcd | -10.07043 | -45.64532 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d3ec674-a970-3cc2-8d6c-d1351bb27aab | -12.14533 | -46.97675 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 060ec6eb-5bf3-3d35-b191-adc4c9d26dc6 | -11.00086 | -48.3496 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba38d276-ef29-313e-b705-7a2f791e4348 | -9.92741 | -46.5905 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a1b099f-3047-3352-b6d4-595309253e55 | -9.89432 | -46.54572 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6deba14c-c4ba-3ff8-b84b-848e4dc897d8 | -10.83005 | -50.16087 | 2026-09-19 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9bf6ea4f-88f9-3e9d-ad55-ce5abdec596f | -11.9082 | -50.12403 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1c244774-d47b-3d54-991e-2257cca5d4a4 | -12.13032 | -47.00715 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 474bce19-e711-3dc4-aedc-ab86a0e3fd30 | -12.41497 | -45.03872 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21fc6ed9-2f24-39c6-b6b7-8b860b7687fe | -9.92686 | -46.59401 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c843c1d5-b0f6-3dd4-844e-a163b53af750 | -12.14922 | -46.97375 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2b7c6a46-afdc-3b29-8f15-821079565cc4 | -9.88377 | -46.54761 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7d4dd40-2051-3e43-8e58-439c3280bb09 | -10.88666 | -54.06314 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6967db61-ec98-3a28-ae35-9b665b344c74 | -11.06019 | -49.77409 | 2026-09-19 04:40:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f099c1c6-ad60-3763-8b7e-b3130a2cfe94 | -11.67248 | -54.44727 | 2026-09-19 04:40:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00f88aca-9d68-3eaa-8a69-c43d0f4f1014 | -10.85877 | -56.19109 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61a7541b-81a5-394d-aa2a-d1fee1bfed24 | -12.74172 | -47.0174 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1cca8c10-777d-3da5-a71e-efcb53d36097 | -12.86437 | -46.33906 | 2026-09-19 04:40:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 38956131-fc5b-3c04-8fa7-d3276505ba83 | -10.39769 | -48.32434 | 2026-09-19 04:40:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e10786cc-ec3f-3243-9e27-591090b19ba5 | -9.36952 | -48.54145 | 2026-09-19 04:40:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a79378ac-bd7d-366b-9b4e-12d732b9d017 | -11.14 | -54.01901 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |


[Clique aqui para ver as próximas entradas](README67.md)
