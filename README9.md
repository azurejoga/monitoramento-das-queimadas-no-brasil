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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9be3b890-d786-3a0f-a39c-7ae2b04c286a | -3.79421 | -46.85279 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00ae4002-adeb-376b-a0b3-370d14ddd71f | -2.63066 | -46.11439 | 2024-12-23 04:31:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c782623-e980-3a95-acff-1e7f26e9b33a | -2.53323 | -54.15022 | 2024-12-23 04:31:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4928ce82-9fd7-3f3b-9891-a7b3a0bd4c7d | -2.6731 | -54.60062 | 2024-12-23 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 158d7dd7-bf31-3361-97bd-3c3c45e9bcba | -2.72784 | -49.07243 | 2024-12-23 04:31:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b847ce9-dde2-31a6-9139-8d178a392449 | -2.081 | -52.04465 | 2024-12-23 04:31:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90a4a747-a609-3b3e-b798-8470abb974cd | -4.02251 | -46.90298 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 881273e9-5a3f-39a1-a925-1fcc5c350c64 | -5.82317 | -35.48561 | 2024-12-23 04:31:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3d29b500-717d-3619-a5b8-f5a55347d1ff | -3.79809 | -46.84985 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd71eacf-3a3d-3005-a172-6894db7e8fc6 | -3.80032 | -46.85731 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0343ab4a-e6c3-36fc-a47e-58597fde04b0 | -5.80649 | -39.07761 | 2024-12-23 04:31:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ee255a2b-f774-39ad-ac76-2b3f9e5bc652 | -1.638 | -45.84903 | 2024-12-23 04:31:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 805c2645-91e3-3321-8857-92ecc17b8a9a | -2.50013 | -48.06483 | 2024-12-23 04:31:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b33ec09f-10d1-3acb-9414-de061fe265fd | -3.96771 | -46.66911 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| def1b770-80c9-33e6-9cf3-3a08c8f4182f | -4.02367 | -46.91736 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3dec8ebe-c2e1-38fc-a4eb-4bc0b1fabc22 | -2.46454 | -45.81292 | 2024-12-23 04:31:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8f0cd49-d48b-3ef8-92db-eed4c19248e5 | -4.09558 | -45.30529 | 2024-12-23 04:31:00 | NPP-375D | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06cadddb-7a94-326b-a7bd-a319ad8ffcf3 | -1.27199 | -53.03605 | 2024-12-23 04:31:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b93d4284-7675-3f55-be36-779a437652bb | -1.45356 | -52.65594 | 2024-12-23 04:31:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce386b90-98a5-3d10-b3fb-90f696477338 | -3.91914 | -46.93605 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bea20970-959b-3e9d-815e-f78e744de0dd | -3.75411 | -43.48089 | 2024-12-23 04:31:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d268da2-57e2-3d1f-b8d1-8c4458abc8ee | -2.53053 | -54.15305 | 2024-12-23 04:31:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a02ea642-68b6-3b4a-9985-24ebf538617b | -3.97384 | -46.67365 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 936df5a6-1dfb-3b00-b223-3a1c486aa99b | -2.68915 | -51.90806 | 2024-12-23 04:31:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b77a7167-5286-35e8-96d5-364f4956e2fa | -4.04676 | -47.03113 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c75397f-2163-3ab2-b570-a38124ef57cd | -4.01471 | -47.06163 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ffed70a0-dc48-3c0f-bc7e-7b7f66d696af | -2.67411 | -54.59953 | 2024-12-23 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b711355-a29b-3711-b2a9-7cbec1364d9e | -2.58139 | -49.05363 | 2024-12-23 04:31:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06a944f4-ea00-33a1-a885-9c854ca5fb04 | -3.90665 | -47.0158 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ab0640d-48b4-3dcb-8a46-1875c3e224f0 | -4.04548 | -46.79969 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 147fc611-26ff-31d8-8b69-9cc85f845f51 | -4.17865 | -43.65266 | 2024-12-23 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| daa0df32-1894-3c00-be3c-6b90e44e641d | -5.25599 | -46.32754 | 2024-12-23 04:31:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae110400-f288-38e3-830b-0deee5e9a304 | -2.1124 | -45.49494 | 2024-12-23 04:31:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1b5a56d-f411-3630-956c-cc4e80935721 | -4.01247 | -47.05419 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 494a5599-53b9-3a4d-9d15-df7c9f4e9304 | -3.18134 | -45.97745 | 2024-12-23 04:31:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22178be8-963c-35d5-86bf-153661168d5a | -3.85366 | -46.58361 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3b470a3d-3fdc-388b-ae43-e2811ce7f3d9 | -3.81274 | -46.71325 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9557e2d-2d54-3912-88d2-074109a65b75 | -3.48645 | -49.69591 | 2024-12-23 04:31:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 848c76bd-9ba6-37f1-8d92-12e9f7f18e47 | -1.63239 | -45.84093 | 2024-12-23 04:31:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf231886-5ab7-3788-8f46-6848d9db2831 | -4.03956 | -47.03357 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c178d9e-36f2-327f-a5d2-9aec0af346b6 | -3.13519 | -46.34702 | 2024-12-23 04:31:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ea944ae-3d25-38c1-aa79-c589f8feb951 | -2.62638 | -48.63574 | 2024-12-23 04:31:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb2642f1-a6ba-37cb-9d74-ab90a4c74c4a | -3.91715 | -46.36658 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2e30581-058f-306f-94f9-41965a20bfce | -3.7569 | -47.1981 | 2024-12-23 04:31:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 953493d2-90c8-3f78-bf83-b375bde4aad4 | -4.0086 | -46.56071 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fa34fc5-34ab-3550-bc30-40e580ee1fe6 | -3.92675 | -46.88747 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db039b64-05bf-33e2-8743-de1d6106e148 | -2.0631 | -45.38392 | 2024-12-23 04:31:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9bf10bb1-2b18-32df-8ce9-c80dae7a887b | -4.05747 | -47.09312 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dda8df28-2ef7-3ecc-9d31-8932d46e0d5a | -4.01612 | -46.90495 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 769b0ed1-6d4d-3530-97e9-89823f1230b4 | -4.02469 | -47.06317 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d53ad0a-1b5f-334c-a7df-8e742aacb859 | -0.20525 | -51.59979 | 2024-12-23 04:31:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ca95d04-b384-368b-aa55-0dab3635083f | -2.70837 | -46.14448 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a984b33-c7d2-320b-9dae-9bce0750d16c | -5.30151 | -46.46265 | 2024-12-23 04:31:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7467b12-0b42-3f47-95a1-7897e8949495 | -3.9279 | -46.90189 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b4c2008-7095-3881-8ff4-8f9872311bc5 | -3.91825 | -46.35954 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bac8dae-3dfe-3720-85c6-fb671deb08fa | -3.9216 | -46.36008 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a92518a2-41e9-341e-bb58-10941b337a7e | -3.91513 | -46.89635 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9da68d6-0398-3c5b-bc27-cfbcbcedec8c | -4.27798 | -55.74274 | 2024-12-23 04:31:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4ff2493-054f-31ed-b17f-7fe559c2a80e | -4.32955 | -44.19411 | 2024-12-23 04:31:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a3cb70b2-dd03-37c2-be57-c5df29ce5e68 | -4.10281 | -46.62965 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0330f305-c957-3319-9d2d-e4d77b130a0a | -2.71283 | -46.13797 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5692d264-5758-398e-92fe-ef6c0be0ad59 | -4.01749 | -47.06561 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a865aab0-e21e-36fa-9bed-f62f81e435f3 | -2.72574 | -46.18676 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a99dde52-b59c-32c7-90d2-3b0028abc4e8 | -2.5618 | -45.50016 | 2024-12-23 04:31:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6da26e4-bd35-37bf-a3a2-a8fa404b5f90 | -4.04398 | -47.02715 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae15bf25-2cfd-33bd-9299-a178b962459b | -3.88214 | -47.02635 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57cee514-5bc6-3a58-a0c5-72de3bfd7133 | -5.44886 | -44.81549 | 2024-12-23 04:31:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4e0a912-02e6-3f75-8915-1bdc62596abd | -4.00225 | -46.90635 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 10daa9e0-7462-3e1e-b670-2e151d3ad057 | -4.02082 | -47.06612 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a08cd11-7ca6-3fee-9693-229a047f0e14 | -0.95634 | -47.5365 | 2024-12-23 04:31:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c46433e-d3ad-3926-8ee5-3ad030a23646 | -4.17629 | -43.64302 | 2024-12-23 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f41a2c0d-f3ab-34c2-bd9f-d6e69d2c9a62 | -3.18413 | -50.54916 | 2024-12-23 04:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e7391a6b-72b2-3222-831f-173edc88c201 | -3.03936 | -52.71518 | 2024-12-23 04:31:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1916174c-4078-361b-8799-aa2a1a9b6053 | -1.94026 | -45.68169 | 2024-12-23 04:31:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 150299fa-398e-3130-8c61-0a7c6f3a98db | -1.36749 | -46.06236 | 2024-12-23 04:31:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b98955c-e1c4-30e2-936c-576cb3c00d3e | -3.3307 | -53.1041 | 2024-12-23 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5e3c570-d767-3d41-a117-cb86d6fc7ac1 | -4.02595 | -46.84243 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 170ab984-451b-321a-8976-9e39a9a290b9 | -0.78357 | -48.76835 | 2024-12-23 04:31:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98afc460-8e5b-319e-a232-92a0e9889373 | -3.982 | -46.34767 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 85b0b9bc-8500-39c5-9369-f407e4a13e16 | -5.43657 | -47.61417 | 2024-12-23 04:31:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68f3731c-9fcf-350b-abaf-b6c8321f57be | -2.81506 | -48.08504 | 2024-12-23 04:31:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7bd7c11e-2ae3-3f44-a892-7fdc50430366 | -3.58465 | -54.30519 | 2024-12-23 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3899bb04-de06-3ab2-9af8-3eb4e42f7313 | -4.02696 | -46.79264 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d68b3583-9ad3-3b17-8c3d-423416d86f6b | -1.95145 | -45.6542 | 2024-12-23 04:31:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c28bf8aa-ba26-319c-97df-7fad11c53965 | -4.08604 | -46.8024 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a386d87e-5ecb-3461-878b-076f971c3cec | -3.98002 | -46.8958 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b585a53a-fbf2-3947-b913-a8468fc45ab1 | -4.04215 | -46.79916 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 292cff6e-12be-347a-8b24-396d0c3de203 | -4.10442 | -46.8159 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 205fb1fc-ff13-37d1-b6a5-80548b8d9df1 | -0.96347 | -46.84574 | 2024-12-23 04:31:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b568a265-e70c-30e5-928e-3e3452b0baa6 | -4.15679 | -43.64468 | 2024-12-23 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 82d56aee-4eaa-378c-ad20-81405202e3ba | -2.65909 | -46.08632 | 2024-12-23 04:31:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17275f51-1050-3d4b-97f5-c57b9f56c894 | -4.04785 | -47.0242 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7dbc178f-2227-3d03-8080-e763e58e88f2 | -4.08216 | -46.80536 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99416e51-2a81-34b0-a302-4d08a4e6f076 | -2.2649 | -46.39787 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e31ac966-8640-374f-860f-2f096e9bec14 | 0.64651 | -59.73993 | 2024-12-23 04:31:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf86f9e5-960f-3599-b373-460e5bd5bf65 | -6.93654 | -43.53479 | 2024-12-23 04:31:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| ee2e98f0-3cb9-3986-9b09-70e0a6e161da | -2.72734 | -46.18673 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e35a1ab0-972f-3c8b-8ac2-ec4a86d75b58 | -2.62355 | -48.6316 | 2024-12-23 04:31:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9a2995c-6388-308f-9873-e9cb8936ccfc | -3.99405 | -46.74114 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9547aa4f-b4ac-3210-b435-7de969941ddf | -3.13143 | -49.16846 | 2024-12-23 04:31:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README10.md)
