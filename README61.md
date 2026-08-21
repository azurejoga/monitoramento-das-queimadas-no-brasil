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
| 54ab5e81-bd66-3eab-a004-bfd4791c0fd8 | -12.94436 | -56.6267 | 2026-08-21 05:23:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e7def4d-656b-356b-9e4d-c694dd94207c | -6.91735 | -59.34563 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66717ad3-cf76-3d77-a40e-54b0e5b985c0 | -7.43534 | -59.79068 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9f46b37-a12d-352b-873e-cfe19050ca65 | -6.65484 | -56.34277 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb3a416c-5cc5-3153-a1de-a5a0001fd64f | -6.22471 | -55.4026 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2954f5b1-058a-3ff0-aa6e-44be03efa17f | -14.02381 | -58.86542 | 2026-08-21 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66136ad8-258a-3865-9c89-c707ec755e9f | -9.05289 | -60.43245 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75eab2ac-b07f-3c8d-bc25-c079ccf2ca0e | -7.60152 | -60.95679 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4b0ae53-4464-38d0-a1ed-fed10b57fac3 | -16.30294 | -53.16674 | 2026-08-21 05:23:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1cc0ae0d-5431-3aaf-a8e5-f2ac4d6ebe8e | -14.24086 | -52.14162 | 2026-08-21 05:23:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b503550-dc5a-3ae0-bf2b-805126807c41 | -6.13802 | -59.90516 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57fe0218-3880-3c69-b6b5-c58596eefe41 | -9.21168 | -59.76605 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dd3acfa3-7ad7-3c8e-bd99-02234436072b | -5.87284 | -57.66153 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc92d338-c99c-3dd2-9244-9f84b055dbad | -8.593 | -54.73751 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a95cce32-daab-3b25-a986-b550e81b85d8 | -6.43262 | -52.71704 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23e34461-dddc-38fe-af85-3028f4d397b0 | -10.53028 | -50.8216 | 2026-08-21 05:23:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e5af61f-6ee1-3f9e-9a2e-69a6d4385a1f | -8.57144 | -54.78181 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 563690f2-e7ed-353b-89ff-0b8ef746da57 | -16.71506 | -49.38062 | 2026-08-21 05:23:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c88edf99-c62d-355b-acb1-8cb514e26fa8 | -6.87969 | -56.42165 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a43f0a0f-49f2-359b-bd3f-d75938c4441f | -6.72268 | -59.10053 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 725f2569-4bad-3325-8386-46420fedf53c | -13.39019 | -54.38527 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| d89a40f0-d3f3-3dd8-960a-7c75eba4d5d0 | -7.34404 | -55.67611 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54779f98-7cf2-3299-8566-08ac4116bdbf | -6.16895 | -55.44377 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1543fc5f-5174-33bd-9afd-a89676795858 | -4.50685 | -55.45002 | 2026-08-21 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6076b9ef-34de-3ee0-bf46-303386b50c9d | -6.95865 | -52.81298 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 572b6b55-b6ed-3e62-b18b-5b3f08c83be3 | -16.72079 | -49.38151 | 2026-08-21 05:23:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb069c4b-ad9b-3722-8dde-ae2934eb6f7d | -8.58315 | -54.75345 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57b9fe6e-1802-3322-92eb-528de62e1724 | -7.34461 | -55.69535 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7bbd293-443a-3e26-a332-f2ace4a4002d | -4.10818 | -56.36477 | 2026-08-21 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b29970b3-6b15-36fe-94d3-90675bdd5660 | -6.86889 | -59.42869 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea4b7f63-4755-398f-84f8-27da8c1a908e | -3.26655 | -49.52744 | 2026-08-21 05:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 466add5f-b6e1-36bc-a2e4-5fb61a9d352a | -6.16974 | -52.48594 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ac373d9-a394-396a-bae9-2ea79fa68373 | -8.54696 | -55.32139 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 836feeb8-e58e-3420-a415-3073d5883936 | -3.53888 | -48.18691 | 2026-08-21 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 9de0c426-f98e-3fbf-aa9c-f191c9b5c152 | -6.1291 | -59.91572 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02b5b783-b220-3ca4-8670-a409ca9289af | -6.58005 | -58.9701 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef6c9034-7a59-3877-816a-b5303cc96a95 | -6.43668 | -52.74388 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7696042d-749e-3186-a635-f0ab39e4ebe7 | -6.42795 | -52.74784 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1561be92-a0fd-3275-801b-09ae8e227393 | -6.87752 | -59.41872 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d8553fc-cf17-3377-a32b-bca47a675a1e | -6.82401 | -59.40242 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4b3fe9c9-f49b-3ceb-8b4c-b9356cbc738c | -6.60486 | -56.36836 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e98a8847-08f7-3f44-af0a-c04095b86955 | -6.55053 | -56.26487 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0bb012cb-523a-3324-a26c-67bf588008ce | -6.80445 | -59.44117 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dc97715-8ad8-32fc-9e8e-e4f3c3e0783e | -15.00323 | -52.67516 | 2026-08-21 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 602aa524-53bc-3a8a-82d1-e8999f634f63 | -6.43235 | -52.76171 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 229b804e-230e-33c8-998c-dcba818fbbdc | -6.24652 | -55.42124 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67701df4-4864-3548-a3eb-850e436e1c79 | -8.5866 | -54.77984 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37b63fb7-7938-3076-b1d5-0e675973ba62 | -7.0601 | -56.65308 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 420576a8-25e3-3ba5-bbd9-8e92d1f8ebea | -8.58442 | -54.74502 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ec2085b-8ac7-3316-ab83-30cdff53d8bb | -6.89908 | -59.43745 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bce53e79-9a4e-3a24-b709-f9a07669551e | -5.9372 | -52.21286 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9541283c-84fb-34f9-9e66-4e9b94c53534 | -6.86024 | -59.4387 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d2ef14cc-b2d9-3f23-942b-a51b2f679376 | -6.81375 | -59.40076 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7b719826-5bcc-3d4b-946e-982f9c761056 | -14.44858 | -45.61792 | 2026-08-21 05:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4c328bbd-df3d-3801-aa80-a99178b39078 | -6.76037 | -59.15113 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54a52c5b-3b81-303f-8027-73a335b8a997 | -2.85593 | -60.86164 | 2026-08-21 05:23:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7aa8f887-3b62-329c-a540-020107319898 | -7.60584 | -60.95317 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f83bfcb-e9a1-3840-9f21-09dbb021ae6e | -6.12687 | -59.90734 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0f45b86-b5fe-3ad2-9548-6176db301916 | -6.83488 | -59.40035 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| f1bc2aa0-a7b7-3ebf-bf01-f66afd860501 | -7.05669 | -59.84778 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08e34d75-8702-322b-a305-6e01e5508427 | -6.44105 | -52.75771 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4280bbf-bbb4-3685-927a-13a15e62f15f | -8.49857 | -54.86607 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f23e761-e894-33f9-927a-b5c4d5a2dd4b | -8.58742 | -54.74979 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf01324b-ff07-3e4e-a00d-ddef106e5636 | -9.80439 | -46.64887 | 2026-08-21 05:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 68293249-59ca-30cb-88e4-a20d0fff7dfc | -6.38462 | -54.95429 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba68ffb1-6214-3d59-8479-bea48e3fa425 | -6.84997 | -59.43703 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e216f7d7-08e9-3604-8222-9d4074cb5d0c | -6.00008 | -57.83805 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d2ea2c2-6aa0-3b3a-8480-30b99a6d9429 | -6.89134 | -55.71544 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 226a8105-8980-356a-ae04-5e90e1399c55 | -8.49496 | -54.86551 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1efde351-0be2-30d3-9d26-11cd3af7ec98 | -6.67475 | -59.07418 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bee6e16-482b-3680-8a92-2699ce3c97ef | -8.55091 | -54.86908 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49d95988-0ca9-3ae3-8b4c-fbf21d8aa4b3 | -6.38582 | -54.94645 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0a77f8e-62e8-33f5-8f94-671346cd4bd4 | -6.05596 | -57.70108 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e1d53ce-5989-3bd2-8993-a439fbb74d08 | -6.96079 | -59.05336 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f14eac1d-afb0-326b-a7c6-c859bc537d39 | -8.52093 | -55.33096 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e2ea21dc-7269-3c28-8b2a-cf9496633c8d | -9.22366 | -59.75673 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 650a3be0-5a2a-37aa-bb99-9d36a8c6f83c | -7.4434 | -60.0028 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 837dc63d-2111-3958-9d59-8dbbe3f3a47a | -14.33012 | -51.91158 | 2026-08-21 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f686f5d2-f118-35e0-aed0-b1db153596b3 | -6.85998 | -59.02956 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 08b33ced-a86e-3cfd-ab10-197e875ebacd | -8.10422 | -51.67147 | 2026-08-21 05:23:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c380ae89-4919-3fe4-afb8-65ffdd168921 | -10.66091 | -49.02604 | 2026-08-21 05:23:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a8a9752-1fc8-34d7-81f9-3741c0b11665 | -14.03046 | -58.8665 | 2026-08-21 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fc002e8-c118-3cbc-94c5-9025e0046adb | -6.87513 | -59.43353 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 169fe824-430f-3637-97c9-fdca24459699 | -7.34767 | -45.81078 | 2026-08-21 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a92d68f-20ae-3a2c-b03f-a51bfe46a672 | -6.80281 | -59.42948 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae50b5a5-528e-329b-9518-543decfcd957 | -14.99814 | -52.67896 | 2026-08-21 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aef88b30-df30-3a9e-a0b6-b4127288d9e8 | -6.82964 | -59.41094 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3262fa6f-450f-37b3-9cbe-7042bfe84a76 | -14.43403 | -51.81636 | 2026-08-21 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37ae31c6-3790-353c-9a10-5c2baf0b921e | -6.85177 | -58.97265 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8dd72b9-04cc-3827-98fc-07aff4f28854 | -7.35478 | -45.80637 | 2026-08-21 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 61869d6f-1989-317e-9a1d-f2ed7a8fba2f | -4.46609 | -55.39895 | 2026-08-21 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27b22755-322d-3a77-a0d2-3e5ece9e6b2e | -4.47006 | -55.39583 | 2026-08-21 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 674c86d5-1003-36cd-8110-5a655f25f30e | -12.51712 | -54.7572 | 2026-08-21 05:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a13e991-0b02-3f71-8e0e-9e7b7af90a6e | -14.08763 | -58.86457 | 2026-08-21 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdedc67b-2ed4-3f52-8aa8-c40cd91b01ac | -6.88923 | -56.42678 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff797554-1e8e-3fe4-9a03-60fc252efdaa | -9.0835 | -59.4834 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f282b6d8-2972-3932-b6a4-9f7da0350c11 | -9.05702 | -50.88852 | 2026-08-21 05:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47e0bbf3-0c32-33fd-b429-6ee73e6664a1 | -6.80645 | -59.01717 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 474f085c-bff5-3610-8b73-4701a0a8fe91 | -8.7144 | -49.61595 | 2026-08-21 05:23:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 230d175f-6d8c-31c4-94be-0ea9fef5a776 | -6.88659 | -59.42779 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README62.md)
