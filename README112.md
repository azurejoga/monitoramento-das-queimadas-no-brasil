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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 179f0158-c932-35f9-972d-5b8db97b5c93 | -12.2208 | -45.51603 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3b2313b6-2d45-3480-b8d9-e321e7ac5d08 | -12.2206 | -45.52962 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| d461544b-8c94-347a-85f6-d2838914d802 | -12.22036 | -45.51985 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8d906f52-aade-3ac8-95ee-0bc96e74e472 | -12.22014 | -45.53342 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e46586fb-9846-3b2b-a9cf-e0700eb781f4 | -12.21992 | -45.52369 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 125ec08c-3c4d-37f7-a207-f3c324567bb7 | -12.21947 | -45.52756 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| b2ed7bf4-701d-3bbf-94d0-a5d58ffbfa28 | -12.21903 | -45.53139 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 63b04ae7-153b-3b86-98d6-1a88f5a934b9 | -12.12024 | -45.04766 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 76003746-022a-3515-8212-67fcc622f963 | -12.11976 | -45.05173 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e3b10ec1-4a97-36e6-ab43-1e27ede5406d | -11.86591 | -45.53568 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0bda548-3e46-38d5-89cc-f9a3ece581be | -11.86543 | -45.53965 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57793543-a0d1-37e3-832d-e9167a1d1671 | -11.45636 | -45.72306 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 55a01549-a6fd-3b78-a319-85293d989cf5 | -11.45593 | -45.72667 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a979ee5c-8fb7-35a3-a127-05fb558806cc | -11.25537 | -46.11156 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6b2d6c2-8bab-3136-a625-1a88a2259def | -11.25499 | -46.11458 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5995906a-2cc8-3bf6-be45-31a7825cb9c4 | -11.25011 | -46.11051 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74c5a4cb-242d-3453-8ad5-2920e233bb35 | -11.24973 | -46.11359 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc455893-84f1-38a2-9b09-cd062ad09320 | -11.24523 | -46.10646 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6be8d9a8-bb1e-3f2c-81d1-b533212961e7 | -11.23996 | -46.10549 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27f12033-5190-37fb-8973-467a1a8b2f65 | -11.23006 | -45.50235 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20a8eb49-9d50-3451-b048-43dfb1d7aefd | -11.22962 | -45.50589 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79c02745-dc08-33b3-8207-0dbc3ed500be | -11.22637 | -45.48687 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9acb3ba1-b75d-3e16-98af-13b98ff34910 | -11.21579 | -45.52707 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d116a679-b07f-3953-a119-9f3b2ba4e3cf | -11.20796 | -45.54525 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 919c91b6-43d6-3261-a651-9cd1286bc094 | -13.33537 | -46.29958 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55ac0fd6-082c-3ad0-96d7-dd6d73d3d8e1 | -13.32995 | -46.29923 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a427e34a-ecc9-388d-9048-b6ed69de8449 | -13.32958 | -46.30234 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7696c964-53b9-38d4-ab94-0fcc929a0875 | -13.3252 | -46.33988 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 61b6ced1-a985-3e94-b21f-f81601c97ef4 | -13.3248 | -46.34336 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 226c0259-ae52-37eb-bbd0-4ca2112c7dd2 | -13.32374 | -46.30559 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 450cbae8-74f9-38d9-b3df-b05cdba78fd6 | -13.32103 | -46.30393 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c32794de-404b-3c05-b65f-afcaeb3d47c6 | -13.32064 | -46.30717 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db2120a2-6f3a-3dd9-818f-5426452805b4 | -13.31822 | -46.30611 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 881ca2d4-6452-3fff-a0f0-2fd57b2ac4c0 | -13.31695 | -46.33698 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82e5cf83-26ed-3a54-9b96-831d9b9b3774 | -13.31634 | -46.32236 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1308645d-b7c7-3600-8ab8-332fc908a267 | -13.31484 | -46.33526 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d398e90c-8a84-3861-a2bb-2bdac91de20b | -13.31445 | -46.3386 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5bee6ab8-9208-378f-a9d6-24865e7b185e | -13.31349 | -46.32082 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b1ec591b-8f00-3338-a721-4d7a194442c8 | -13.31312 | -46.32384 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d086cff1-635b-320c-871a-0a012d408627 | -13.31158 | -46.33633 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 010b8e0d-7650-3fe9-ae50-6979b0ba06fb | -13.31121 | -46.31956 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| afe0737d-1518-3aa7-aa2f-f0c6a13046d0 | -13.31087 | -46.3225 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4110bd93-f3b0-35ff-95c7-318700f33ba5 | -13.30984 | -46.33127 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7973190-9f6b-3e6b-ba54-cefafbd2c466 | -13.30768 | -46.3237 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dadb8d80-0cd3-3b25-bdeb-92b169262a7b | -13.30701 | -46.32911 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| fcd53084-209e-3ec6-b63b-65473366b110 | -13.30663 | -46.33217 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3c6b6202-d5ee-3fe9-b9d2-39be0b138959 | -13.30623 | -46.33543 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| bbb8f4d2-d36c-3196-9c38-737ee7c10e43 | -13.30449 | -46.33038 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 5a230be7-c020-39d9-8b1e-647eac0ee782 | -13.30412 | -46.33358 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d0a6c555-f692-356f-a33e-9cb3d26bda49 | -13.30374 | -46.33691 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2bbfb4ef-fa5f-3bf0-b223-8b8c4c96a225 | -13.30009 | -46.32136 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3cb7be77-e618-39a7-9acf-11ed8511a25a | -13.28772 | -46.30824 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47e003b8-f594-3e3f-921d-c08d3f38b8f8 | -13.28739 | -46.31096 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 181e482c-37c8-3737-8e20-fcced48d3903 | -13.28591 | -46.41245 | 2024-09-26 04:59:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad642e5f-2b55-3e25-840d-df24e51ee481 | -13.20356 | -45.64798 | 2024-09-26 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9f3d9597-bdf7-3888-98ba-34d575f36fe0 | -13.20312 | -45.65185 | 2024-09-26 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c26c64d7-c0b5-3d4c-b991-2fabb2ad94ff | -13.20267 | -45.65572 | 2024-09-26 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ec269b84-a869-34b1-9792-06ec1feb0447 | -13.20222 | -45.65958 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3974a907-63ff-3a88-b96c-f55259455599 | -13.20178 | -45.66347 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 57690f9d-1c2f-3c2d-8074-f8b605b077b6 | -13.19929 | -45.6356 | 2024-09-26 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0348e1c5-efcb-31a3-9886-e83b11dd0f11 | -13.1984 | -45.64335 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 49db7a94-a216-3ef3-8261-01f74679ebf4 | -13.19795 | -45.64724 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c301a28a-15ab-35c6-9b9d-52c8645640da | -13.19456 | -45.62708 | 2024-09-26 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 069e57ca-b60b-32dc-bac2-1d753ed3596d | -13.19367 | -45.63484 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f82480a3-97ba-361b-a4a3-9b21faa2d33f | -13.19031 | -45.62902 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ee1e159-408f-3c52-b5d1-7203b9360325 | -12.9594 | -45.29735 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0aafe2eb-ec39-3ff0-8deb-4b22ba22088a | -12.95893 | -45.30139 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 513cc32d-3d56-3b7c-b819-58aff2a63b81 | -12.95846 | -45.30543 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e3329c68-b07b-3a8e-aec2-345f1ea93732 | -12.95798 | -45.30945 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6903b0e0-65a2-3781-9a69-f9721ba58baa | -12.95462 | -45.28852 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c19870b0-6e81-3770-91d4-5f81d7eae440 | -12.95415 | -45.29257 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1057bdd3-3b4a-3fc3-a62d-fc7e78ec7d2d | -12.95368 | -45.2966 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4dfe7259-b17e-3222-a408-9be15a24e3eb | -12.95274 | -45.30468 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 208e45e7-302f-3f60-b2a8-71d68280feb6 | -12.95227 | -45.30872 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12359947-cef9-3ac6-b5f0-a3abc530581a | -12.9518 | -45.31274 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d401857-18ec-391e-a339-5be099ca4335 | -12.94937 | -45.28373 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 34454ed6-8f21-3ad5-bff5-ccde83bd861a | -12.93052 | -45.3462 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 7315557f-a200-3c6e-9498-75693e71f375 | -12.93006 | -45.35016 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 29dd0dc3-49e3-3ab2-9d21-e0a3c4887447 | -12.9296 | -45.35416 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 9bc738cc-5b36-35e9-a1e0-c79b414cc1ed | -12.91913 | -45.34459 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54031e88-adca-3284-aed6-8251208c1bd8 | -12.71998 | -45.57004 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82e648f2-5fdf-3445-87de-9ec50124e007 | -12.71952 | -45.57386 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ef4e20e-22d0-3b35-bfa4-a4b4a102c476 | -12.71907 | -45.57767 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9363d8af-be33-3fa8-8f16-d66818290fb8 | -12.71484 | -45.56544 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c0796b2-d5da-33f9-8990-ea60e43b07c7 | -12.71438 | -45.56927 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e968407-ee6a-312c-8c8e-8743b9aec173 | -12.67991 | -45.85751 | 2024-09-26 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab7e0578-8dba-3020-805a-5135e04b5282 | -14.81701 | -46.72578 | 2024-09-26 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f523c939-2a2f-3a49-97e3-ef802dbec724 | -14.81654 | -46.72982 | 2024-09-26 04:59:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7a1dd33-81c1-3152-bbea-aabdd36a3c67 | -14.69335 | -45.47536 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3bf4a6b5-5636-3ddb-a8aa-45902e1b8c35 | -14.69292 | -45.47935 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16ebf913-c3d8-31a3-a512-8b300669af2a | -14.69263 | -45.47467 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c44d3fd-2d5b-3e9c-872a-714390e9d3eb | -14.69217 | -45.47866 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72da97c8-211b-3d4a-89df-a6281a9cc9e0 | -14.68756 | -45.47469 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60a72332-1aee-395f-9d65-3e1351245cc1 | -14.68713 | -45.47868 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b59a2a6-8b0d-3963-9d3b-887170b090e7 | -14.68683 | -45.47401 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ea15980-67f6-3902-8d9d-fc09fc55272b | -14.68638 | -45.47801 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 280ac36a-cf71-3459-afd6-a92464a8092a | -14.68134 | -45.4781 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 434be73d-f1f4-3bce-943c-47a4f6dbd065 | -14.56928 | -45.67221 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a5c459f-e509-3cf4-a961-1532fd54c25b | -14.56891 | -45.69609 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 88ac870e-a6b5-3f79-813a-d9278435d4db | -14.56881 | -45.67622 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README113.md)
