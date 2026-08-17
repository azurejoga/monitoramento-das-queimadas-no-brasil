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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2c5313d-bf45-3d60-ae3b-9a024dc87797 | -11.28271 | -45.81556 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20f3e2c3-26bc-3a7b-8fc9-7d179f4d623d | -6.60498 | -58.96951 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b69f9182-3328-3f13-bcf2-f8bfef3ec6c3 | -6.70825 | -58.93542 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6f67a5c6-94f5-3963-97c6-9fd9de7a75a0 | -10.51127 | -50.01863 | 2026-08-17 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 070cce61-4739-3c5e-93e8-28684c23e93c | -11.08839 | -47.29928 | 2026-08-17 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7bfb7849-1254-303d-86ec-bffc7b4b3088 | -7.45559 | -60.00095 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 188c1e62-097a-3dfb-a32e-82d8d5e1a0d9 | -7.42557 | -60.0207 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83af60f0-2985-3f41-abb8-5fe2dcb72620 | -6.63403 | -58.96063 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 839f0535-75ff-3f79-8237-617781366cb4 | -6.93926 | -60.09073 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 541ff6fb-8032-361b-b32a-9885b67f00f3 | -8.5215 | -54.89694 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3ba69b9-34ec-3624-b257-238ebfdaa9dd | -6.96674 | -56.49796 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad15dc4f-1a98-3fd6-9bde-db2745b9bea1 | -6.61957 | -58.97189 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e4cb6cd-9c8b-3343-be24-9e2b178a5a51 | -11.28335 | -45.81105 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b312c85-756e-3818-9c6b-13030fbfb59f | -6.62152 | -58.97482 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78e6327b-137f-3efd-9a36-0b2c08f0b954 | -6.70552 | -58.94177 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 80f50c5b-b40a-30a4-8a1c-94adb794233d | -14.30216 | -47.18519 | 2026-08-17 04:57:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98b9a3c8-32d1-32de-b927-7624097c7383 | -15.14739 | -50.05291 | 2026-08-17 04:57:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1824eb0-89de-3054-a983-13c2db6b42f3 | -7.38719 | -59.99846 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 176cc3a5-8757-3fc3-b139-a15d12b0d7c3 | -7.88847 | -61.79786 | 2026-08-17 04:57:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0cfbecb1-d15a-3dd1-8571-9ebe1dde9426 | -8.523 | -54.91025 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2dbbf89d-f25e-3ad7-a659-445e2411357a | -7.5573 | -61.16553 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1c2053b8-9f7b-3c7a-b696-dd917382b35a | -12.048 | -46.44836 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 645ac41d-5131-3c77-9050-735fb8314e3b | -8.95786 | -60.59482 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce6376ba-1b7a-383c-8758-e843c618ba5c | -11.88727 | -51.95055 | 2026-08-17 04:57:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 973d4eac-02ff-3d4f-80e9-18202d47e63c | -13.52328 | -46.23822 | 2026-08-17 04:57:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 358e05d6-58dc-3cac-8944-fb2ec7b83cc4 | -8.5121 | -54.90844 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4679c918-17a3-3ef7-b013-786982b4b346 | -6.85212 | -58.97489 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f3d124b-219a-39fd-bd76-0ca995a50cd1 | -8.64608 | -54.6889 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2774ed83-8796-3dee-94de-cb40808199df | -12.74923 | -48.4278 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7effe457-f9fd-30b0-9101-4bab882ce90a | -10.50666 | -50.02572 | 2026-08-17 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ecee15eb-7c0c-32e9-bb72-ebb5eb8ddd21 | -7.37327 | -55.49006 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 78e37fff-b3a9-3308-81ab-bbd32f0c24b4 | -13.51211 | -46.28868 | 2026-08-17 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b420e002-3dcb-3d02-acf8-a51fdf645848 | -7.38158 | -55.51071 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2369510-d00b-3f3d-9f00-efd2834fae75 | -8.90015 | -60.58741 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e5875321-54b7-30c0-977b-78b29eb40b84 | -12.14897 | -50.18959 | 2026-08-17 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 699500f0-5e81-3a53-be87-baee3bc3016a | -11.39331 | -46.39982 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 454db0ef-0a83-3f21-a241-219819c51e70 | -9.46882 | -51.62071 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c072c188-0d90-35b9-b672-3e65c277df25 | -12.7143 | -48.48036 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f935ae60-2f12-3225-8b3f-3eddd279de17 | -14.07902 | -53.59361 | 2026-08-17 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2125f8f1-59ad-31b5-974a-d19eff918836 | -12.90561 | -52.82565 | 2026-08-17 04:57:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd1b5125-1d08-3b78-95b9-59c6befcd171 | -6.96206 | -56.5008 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8aaf5f3d-d2e6-3503-a9ef-a8119dc8856e | -15.15884 | -48.61224 | 2026-08-17 04:57:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4613050-89b9-33c8-895d-a548f01fc598 | -11.83286 | -51.77474 | 2026-08-17 04:57:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 81acf6a3-29fc-3941-bd65-cb3ac8589000 | -14.30941 | -47.18886 | 2026-08-17 04:57:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c5cc93a0-445f-3edb-824f-2a8ff6ee1caf | -11.32892 | -55.22258 | 2026-08-17 04:57:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7e88b5c-e893-352a-852a-17db52c7b16e | -8.61128 | -54.71452 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad1c98e2-c2a3-37d3-802f-14620328f311 | -14.50463 | -53.09361 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc05b966-7054-3af1-8485-2a654fda877c | -14.89458 | -46.62796 | 2026-08-17 04:57:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00667d6c-b706-3b69-a7f1-cfee95987110 | -14.30836 | -47.19696 | 2026-08-17 04:57:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 9d8a4bd3-80c7-351c-9f00-081b50de418b | -12.05126 | -46.45636 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21e09723-1e0f-3011-b3ee-8678dc0ba015 | -6.83667 | -58.97766 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6b556afb-31ec-3ed8-ad7c-9cd665bfcb78 | -11.61296 | -47.79636 | 2026-08-17 04:57:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 53479ec1-c79c-3ca1-984b-b5e163026382 | -11.23865 | -54.01424 | 2026-08-17 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ffaeac2-5e32-364b-9e82-d2c2c54e0848 | -9.33272 | -62.33739 | 2026-08-17 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e0444be4-e416-303b-9181-603396e9d083 | -6.61783 | -59.05238 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb439aec-33ef-3375-9bb4-4599f1f309b3 | -8.02584 | -55.15273 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82b38d06-ba8c-3cba-a68d-94ff6fec2b50 | -8.89832 | -60.59673 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 76470fe3-e3d7-33ec-b269-99884ff1fc6f | -7.37629 | -55.49538 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58d96611-1a44-3b8c-b500-6e48bb39e9dd | -7.59227 | -61.2254 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f622028-391d-320f-99cf-430a68fe45e2 | -14.36992 | -53.12962 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a65c520-a3c0-371a-b2b3-155498203423 | -12.73292 | -48.45941 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 97d4c771-0ff8-39d8-83a0-c83c4a9e5db0 | -8.95155 | -60.54148 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97460591-382b-33d7-80cd-94cd85bc6b5a | -14.14458 | -52.88408 | 2026-08-17 04:57:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e649782d-9093-393a-a661-4fc6a8ddc4ee | -6.6998 | -58.95557 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12d5689f-1334-3a3b-8e0c-f3b407d50a88 | -12.04742 | -46.4525 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aefa54cb-b00f-3f82-8e57-e63a2f80884a | -7.43125 | -60.01859 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ded175b8-c280-3379-b106-ce88c30d77f4 | -6.77079 | -59.76022 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b42b8f40-0bd3-3e18-8818-260547f4b776 | -13.7826 | -53.80995 | 2026-08-17 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d88867e8-5fcb-352f-8a90-b84fbc712adc | -11.48383 | -46.57951 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e6468c8d-d64c-3825-bd87-5fc83c943dd4 | -7.38059 | -59.99456 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de28ac8d-9c3f-344f-9e99-3695ed6113e3 | -14.45312 | -51.84041 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b9cc9e6-8e03-3f2a-9f55-13084c5992cd | -7.68832 | -55.15691 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bc81687-3584-3429-97c4-fe131062eecb | -14.49405 | -51.98527 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6497cd99-249b-35f6-a161-68c244682129 | -6.72455 | -58.92742 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74cb19cd-b736-3251-a55d-cd9f051780e3 | -11.13164 | -46.51867 | 2026-08-17 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| baae7b1e-daa8-352f-b02a-d783ef604cd4 | -7.37551 | -55.5001 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64a06ded-24c2-3846-a999-092bff2aca80 | -9.48322 | -51.63734 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9a2ae8f-746b-3e5a-a773-04e8f369ba77 | -6.72282 | -58.9286 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67e6be10-c298-367e-8b01-ec0a27cb3051 | -11.72473 | -54.60421 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7761ff21-2d6f-3e28-98c6-135c997825bf | -12.01411 | -46.50325 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8664b31-6a18-3b91-bb8f-81f5c1b7ce8e | -12.68295 | -48.50901 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4d791349-39a4-3c62-8e6a-7daaaea43e6c | -14.31008 | -47.19036 | 2026-08-17 04:57:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fc0d0bbb-0f86-3b44-92a3-7ff2f5512515 | -14.30889 | -47.19291 | 2026-08-17 04:57:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3f490747-9f47-3309-895a-de419b2b8900 | -6.62247 | -58.96943 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a1eb387-d5fb-3840-aae8-a063e22e62b4 | -7.59141 | -61.22299 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdec8ebd-ef56-3619-a557-418b80982c82 | -14.29908 | -53.08842 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd5b553f-d941-3d14-8f65-739a9a289819 | -11.70828 | -54.61727 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8e0fa6e-9672-3faf-8ac0-73a55c02316f | -14.5026 | -45.68162 | 2026-08-17 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a64db96e-16f5-3d4c-9bca-38e3bbbbb2b5 | -8.10187 | -51.66258 | 2026-08-17 04:57:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1f0a9115-a79a-3fa2-9156-b768d6cfd1a8 | -14.42003 | -51.83126 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 068ad857-23f2-3b80-8014-be5df77fba5f | -8.9717 | -60.51914 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36b1a93d-6e1a-330b-8056-cc4c366724ec | -7.40439 | -60.02048 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8683b81-d01d-3e5e-96ed-2e8ef2bd3c30 | -14.30419 | -47.20189 | 2026-08-17 04:57:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d46a5cd7-bc9b-398e-966d-759b3fdcda45 | -11.71215 | -54.59413 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdae6384-1b4c-3a25-8dbb-619cae1cf7c5 | -8.51068 | -54.91682 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f223d05d-6a25-3d08-b827-e3c0967305cb | -9.20158 | -60.79315 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b9d80cc-affd-36cf-a6da-d9f397b75ba6 | -14.40661 | -51.87402 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52438158-9c72-36b4-91a2-87fe7eeced87 | -6.65244 | -58.96959 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2d5d9cca-9620-3428-b887-fd092488275c | -8.72416 | -62.90108 | 2026-08-17 04:57:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84f734f4-46f1-305f-bd68-2d24b8a14a67 | -7.68716 | -55.15824 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README27.md)
