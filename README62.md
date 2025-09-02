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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cc57f4d-b354-3ecb-ae6e-350d5d2a196a | -11.66046 | -52.2027 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| d9180d4a-cd2e-3ae8-8fcb-71d3d6a2ef1a | -12.61525 | -48.17928 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 38fe1fff-5ad4-3fe7-abcc-9628332f0720 | -10.75122 | -49.58079 | 2025-09-02 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2a936fc0-eca9-3a8f-a53e-89b51f4cb541 | -10.26706 | -47.52353 | 2025-09-02 05:06:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 756689ca-48a3-3255-8137-47e333de151d | -14.79745 | -48.19603 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 150b7abe-6980-3f16-bc6a-f506c0501f3f | -12.77035 | -48.094 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83dddec2-5062-3692-9aa2-fcdb936bf2c4 | -11.66601 | -52.22128 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| adfe1b66-e57e-3a69-b996-7eb1e30b64e9 | -11.66989 | -52.19346 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0057dc21-2db6-345f-9e3d-ce4f6e899ea2 | -13.53658 | -46.98947 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54c4e97e-9c26-3954-a466-49ea4fb0943d | -13.53057 | -46.99382 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 139d0205-fe08-3050-964f-60dc94160e7d | -11.976 | -45.87354 | 2025-09-02 05:06:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9dc6bf21-829d-3e29-9238-4470e15cc353 | -11.6694 | -52.19696 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fd1b3a91-7c82-307f-91b2-87e8f8563148 | -11.79198 | -46.40232 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 86b62d67-bf8f-33dc-a246-c525b9efa24b | -8.66422 | -62.92494 | 2025-09-02 05:06:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d64a29e-abef-3e84-86ee-022c4ba93d1c | -11.43752 | -46.81549 | 2025-09-02 05:06:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 692def3a-0059-30c8-a9d3-1f42029efad4 | -10.834 | -47.45572 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f07459d9-4de9-3cb6-9bd3-fd6268078c36 | -14.59447 | -48.0516 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85536267-c685-3b14-a135-e56c2948da35 | -10.39679 | -47.12884 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7ff76060-fab9-368d-a673-203e6d5db538 | -14.62321 | -48.93951 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd1526c0-e27b-3224-8584-7a700b9ff7d5 | -11.81148 | -46.40318 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 23ed1f11-2d8f-3c78-8924-e195b1e6f7b4 | -12.98849 | -48.10061 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8c0f4f12-1cb8-38db-8066-40dd0b5d33f1 | -11.54152 | -44.84705 | 2025-09-02 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdcdff02-45fa-3f9d-b736-4bc9eb5f7257 | -14.58175 | -54.54382 | 2025-09-02 05:06:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 834744db-0d02-36bd-bcab-3f1107634a15 | -12.64508 | -48.24287 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e59e46e4-30bd-3ae7-918e-bbaeb426800e | -11.66348 | -52.21025 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8a6e5e6d-f94e-3abd-b861-f692c78e6538 | -14.9965 | -48.32119 | 2025-09-02 05:06:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8cfc98e6-65a6-3615-ad7f-1a5eb232584e | -9.26919 | -59.75298 | 2025-09-02 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19b7334f-8f72-3098-a5f7-9e2db7c960be | -14.60232 | -48.03577 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8daa2ed9-04c9-3b85-84af-21894ec0a474 | -15.12596 | -48.11191 | 2025-09-02 05:06:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 106e9984-2dc4-3d4f-8736-d6d13642d995 | -10.33773 | -48.14061 | 2025-09-02 05:06:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e5f4ccf-9954-3019-ae90-2a71dc8e46d0 | -9.46544 | -48.30124 | 2025-09-02 05:06:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33954487-3d6e-343b-9888-7f663b5d3998 | -7.66382 | -61.09257 | 2025-09-02 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec38ac23-2d51-36da-9e50-b2d8d77b88e9 | -11.67739 | -52.19807 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 7251ab83-989c-3748-b886-9dbdd2636b81 | -14.58879 | -48.05757 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8eb1de8d-aa75-3c3e-bb0b-e887151a81e0 | -12.64449 | -48.24226 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d63daf7f-2842-315b-b24f-09851e93b837 | -12.99236 | -48.09667 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c91efbdf-db73-3fa5-a7fc-ae1c7864ffe2 | -7.54669 | -61.33944 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 6de04759-c97c-3145-bca3-dc546a0694d2 | -9.16637 | -58.89542 | 2025-09-02 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b45e744b-cf86-3450-a7b9-7e7054e2a646 | -13.48522 | -46.92311 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56ac6dbf-52b0-3374-9ad5-5b5863d67c4d | -11.03047 | -46.85336 | 2025-09-02 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9bebbabb-c526-3d0b-912c-42c1b987632a | -11.848 | -51.46677 | 2025-09-02 05:06:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 34b8c4da-12a9-343c-bf3e-59de92118800 | -7.56213 | -63.07354 | 2025-09-02 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7a74b731-735a-3e1c-97f6-6797a1bcef44 | -11.42176 | -55.18799 | 2025-09-02 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2ee0225-8908-38bd-af5f-7018cd61b602 | -12.8761 | -48.05889 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70c3b72f-ec57-380c-89a0-09f7d52192fe | -14.59498 | -48.04722 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| df43c33d-a548-38e3-b2b0-e90c00ad2ee1 | -11.01063 | -46.82646 | 2025-09-02 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c46cebc5-72f3-3e7c-9746-054d9291f783 | -12.92879 | -48.09922 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 55e3f9d0-cdfa-3db8-ac41-47109885a9e4 | -12.98663 | -48.0992 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2ff5ef51-440e-3ba8-936c-ad2f235312ed | -14.61246 | -48.04489 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cc079b1f-9f30-3efe-89ca-ca2ae0a22a21 | -11.92005 | -50.62528 | 2025-09-02 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a425d1d2-e21c-30a5-8ff3-4678de4091e4 | -13.50515 | -47.00687 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cad5a870-cc35-3554-9c1c-066c70e87737 | -11.1042 | -44.62906 | 2025-09-02 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f39961f3-91a3-331f-a6ab-b6ca71d938da | -9.06732 | -65.42372 | 2025-09-02 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da1958f0-81c1-39f8-ae69-d545dd9c0aa1 | -12.93013 | -56.95684 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2da5891-1d14-3f15-b5d7-1c9ad979e5d6 | -11.64028 | -52.05183 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 84c26c19-dca1-3ea3-b662-49f7c6cb21d5 | -10.06405 | -48.09833 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9fd4939c-b5c4-322b-aecc-54de2725186a | -9.8413 | -48.31947 | 2025-09-02 05:06:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d879661-808a-3c6a-98f8-06f30a199a45 | -8.6819 | -62.39566 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c80b3cab-1fc0-375e-ac71-88c935f18751 | -12.98698 | -48.09618 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 34ac9947-970e-3fb7-bf3d-48ee1eb0f83d | -9.27347 | -59.74946 | 2025-09-02 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1e64e26-8c35-3881-a063-b84ddc082942 | -7.70225 | -61.10689 | 2025-09-02 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df0ccd78-ae13-34eb-b136-46ecdd1c1f95 | -7.47589 | -63.83073 | 2025-09-02 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 260aec10-766f-3a98-b3ca-0659921faf58 | -11.64995 | -52.19038 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 6884fe1f-7ee8-3254-b38c-0dec98d67833 | -11.67389 | -52.19401 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 585bcf99-c775-3059-a57c-60d416691499 | -11.86295 | -46.70671 | 2025-09-02 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c92f5647-2840-3b8f-905b-62a1ddb3daa7 | -11.6703 | -52.1612 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6239804f-5242-3325-bece-50438dcc2f07 | -9.73483 | -48.96582 | 2025-09-02 05:06:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9dea6f98-b898-380e-8526-8b53ee14eff9 | -8.85882 | -64.23417 | 2025-09-02 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 40cd04ae-55e2-3894-bbe5-00d59a898716 | -13.53729 | -46.98622 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e8f6e4d-30b2-3d4f-a2c8-ff21805c1e38 | -11.89069 | -46.67234 | 2025-09-02 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33959585-5540-3d8c-8b0a-8960e9191e3d | -9.3444 | -65.4232 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4f886db6-12d7-3142-aeed-af7aa05f8953 | -12.62825 | -56.99508 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b563620-7354-38bc-a20b-090a8d095d24 | -10.05521 | -48.12604 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b06fb10c-3551-3cda-ab4c-4f09cc87d465 | -13.51095 | -47.0075 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00204295-1cfc-3c2f-84c5-8dc9589660e9 | -12.93681 | -57.00134 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acb2fa0c-d9ea-36c5-91be-4637b2718495 | -7.47775 | -63.8203 | 2025-09-02 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 47f0da68-2ea5-33b0-b588-f07f9a894264 | -8.64583 | -63.27158 | 2025-09-02 05:06:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8dff9e56-a988-35b6-8b34-49ce280dc176 | -9.54554 | -65.94539 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| be847adc-d393-36b1-a5d1-6b1649b6207b | -9.54491 | -65.94882 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 219859df-360e-3618-a4fb-74b8e3939f62 | -14.58259 | -48.06331 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d0227e2-1bd2-381e-ab25-aa80d2f3be14 | -10.88178 | -55.75144 | 2025-09-02 05:06:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a4e5dfcc-7a96-3fd7-a830-b98f8f0cb346 | -11.92241 | -46.45241 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2bd609ec-0790-334d-8ebe-5686ffa5748b | -11.84219 | -51.54162 | 2025-09-02 05:06:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80731798-b1a4-36f2-8b77-9e1bfd186980 | -11.91724 | -46.45551 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cd28fafa-e061-3e96-895e-579c108a942f | -11.8629 | -52.41713 | 2025-09-02 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68f78565-0aa3-3c13-a9eb-b1163d8080a4 | -11.91392 | -46.67878 | 2025-09-02 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f2997e5c-0c6b-3ab1-8044-cfb16937a5c6 | -11.67234 | -52.17589 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 00fe6c50-327e-3c04-bdf2-32dbcf9b1233 | -14.76171 | -48.15889 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66c78ba8-fea9-34f6-aa04-4e2e8768401f | -11.86684 | -52.41771 | 2025-09-02 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09b12545-c4f4-397a-b479-269ffef40d2c | -11.67536 | -52.18346 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 9b52b32a-b45f-313f-86f2-a67a4865f5bf | -10.35919 | -59.18163 | 2025-09-02 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ba7b7da-ced6-376d-889b-0443a7cf219f | -12.99592 | -48.11277 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e79588bc-52c9-3538-931a-955365329cd4 | -12.91746 | -56.9729 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fbce9018-42aa-3739-aa76-45c2e62c4cb1 | -13.54356 | -46.98273 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 654dd4fa-0aa0-3efc-9169-9d0cc63ba913 | -7.36063 | -61.65152 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 951731ad-f2dd-351c-ad69-c1c2066c1e62 | -10.05309 | -48.14238 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 47c70bab-0158-3374-9d18-a7ae1a14fe45 | -10.44726 | -54.76946 | 2025-09-02 05:06:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 963784d5-25d5-3340-bd21-039670326dd6 | -9.75779 | -54.76326 | 2025-09-02 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fad22a1-7339-3d58-ac27-dc9b5141f5c2 | -11.66048 | -57.3569 | 2025-09-02 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ed6bbc6-5466-3948-9e23-4572582d91c6 | -12.63101 | -56.99913 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README63.md)
