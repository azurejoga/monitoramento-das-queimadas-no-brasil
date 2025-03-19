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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc17beab-d68d-39ba-b3be-7313a9f2ccb9 | -15.34266 | -46.96128 | 2025-03-19 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc5cccbf-8c44-3c23-95a9-eb9a7a048bb4 | -13.47683 | -42.4958 | 2025-03-19 04:21:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 71d8fad0-155b-3bc8-be8f-c9be38ebdb94 | -15.80123 | -42.03378 | 2025-03-19 04:21:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 919a0058-0fd7-33b0-9acc-685846a09f46 | -11.57207 | -47.63028 | 2025-03-19 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d6a3fda-837b-30d1-a5ce-79f520c68260 | -17.78152 | -42.80828 | 2025-03-19 04:21:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da90aca1-1ac3-3b9f-b545-bc94df7418b3 | -11.25314 | -41.90279 | 2025-03-19 04:21:00 | NPP-375D | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5d2e426c-7dfb-3f4b-a5ae-8f35388c387c | -16.08632 | -40.88498 | 2025-03-19 04:21:00 | NPP-375D | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 74026611-8205-3e51-b9c5-8b98156ed838 | -16.68256 | -43.88419 | 2025-03-19 04:21:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 937150a5-9f7b-3d75-942f-2d044822e995 | -15.34323 | -46.9577 | 2025-03-19 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e2662b9-5761-38ea-83cf-99141c47de8b | -12.42157 | -46.7258 | 2025-03-19 04:21:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bb0da54-d091-34df-ab17-fe104652cb8c | -16.08324 | -46.61897 | 2025-03-19 04:21:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4d7fd33b-8672-3500-8c42-6e3f1c6c9216 | -12.14774 | -40.29449 | 2025-03-19 04:21:00 | NPP-375D | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5933f8b4-166d-3370-a1da-7b8cd37c9f63 | -10.65328 | -44.39576 | 2025-03-19 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2444a51e-aaeb-3cb8-be1d-63bdd446d2e3 | -11.57952 | -47.6277 | 2025-03-19 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19ce6ed8-1c00-3408-b4a6-2d308c14c035 | -12.27249 | -43.53025 | 2025-03-19 04:21:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cba65c71-17d4-3f3e-b93f-bb78eee8e92f | -11.56707 | -47.6179 | 2025-03-19 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 452c53d3-661b-3983-8eb0-f08f7cd4492a | -13.54119 | -45.44129 | 2025-03-19 04:21:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34cf85a0-ed35-384d-90e2-41be6e729d48 | -13.71261 | -48.43039 | 2025-03-19 04:21:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 02574a0d-bc40-3152-9af0-869e0ec90f3e | -14.12698 | -47.84748 | 2025-03-19 04:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 929c2f24-d10a-3153-85ff-10e4f9ad536f | -13.54342 | -45.44901 | 2025-03-19 04:21:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f99d72d4-96c6-3dfb-a3ab-ea3b5d35cac8 | -11.57269 | -47.62654 | 2025-03-19 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9540d2ce-02e9-3dc5-942c-151ecf235bdc | -11.85528 | -37.5998 | 2025-03-19 04:21:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 11d1f144-fb84-3073-863f-82b44a681fe6 | -11.56987 | -47.62222 | 2025-03-19 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c9c5c36-e672-3967-8c5e-63bd8dbd1914 | -10.64992 | -44.39524 | 2025-03-19 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7918a818-a89c-3b38-8a20-342d9ff9b3e0 | -16.08657 | -46.61953 | 2025-03-19 04:21:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9c085585-dc20-3637-b1fc-7dd4494471fa | -12.45767 | -43.56865 | 2025-03-19 04:21:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e563c8e2-f75f-3221-b074-9b74296997a9 | -12.08565 | -45.62687 | 2025-03-19 04:21:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2ec4b1b-db04-30d8-95c5-e665aa218857 | -11.87339 | -44.37855 | 2025-03-19 04:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 39e99077-ed55-390b-80bd-01c6e6ae932b | -11.87677 | -44.37908 | 2025-03-19 04:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 89b6fbbf-eb2c-3229-8e4c-de3d871a2c01 | -15.35101 | -46.95167 | 2025-03-19 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1e8d793-73c3-368b-8de0-6e42bfc752f1 | -16.29247 | -45.0981 | 2025-03-19 04:21:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6764c0c5-2de9-3b03-866a-52709ae90139 | -15.6531 | -40.66634 | 2025-03-19 04:21:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3608fbf9-f1ed-33d5-94dd-258978c4f788 | -11.67348 | -39.99511 | 2025-03-19 04:21:00 | NPP-375D | VÁRZEA DA ROÇA | BAHIA | Brasil | 2933059 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0027343c-00a9-31ef-b34b-d645030a4374 | -15.35262 | -46.96297 | 2025-03-19 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62eca285-7e5c-353f-9be2-6857411ce946 | -15.34379 | -46.95412 | 2025-03-19 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab1bc76b-4b18-3e5c-94ef-a16622afc8c9 | -11.96367 | -48.08928 | 2025-03-19 04:21:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a99dd548-6d85-34a0-918e-902ef443c7ff | -16.0858 | -40.88909 | 2025-03-19 04:21:00 | NPP-375D | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d8c701d9-973e-3ce8-8d58-6d1f457a5de1 | -16.08205 | -40.88448 | 2025-03-19 04:21:00 | NPP-375D | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 89a9ebbe-55b2-38e9-ad26-a6f61e2b6730 | -13.05108 | -53.33087 | 2025-03-19 04:21:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c7e6f76-2eba-338b-ac2e-c4d5b642ff59 | -15.34873 | -46.96599 | 2025-03-19 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9c5c69b1-52d6-31c2-9295-1dc6c0d5ce2d | -11.96713 | -48.08989 | 2025-03-19 04:21:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9892bf4-580a-3fba-ba07-b73716fdb7d1 | -12.08731 | -45.63799 | 2025-03-19 04:21:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 723e772e-59ba-31e0-80fa-076e31500334 | -12.08953 | -45.62388 | 2025-03-19 04:21:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5084ee2-2517-337b-880d-6ac3aa3bd905 | -15.42804 | -40.58582 | 2025-03-19 04:21:00 | NPP-375D | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| e671db50-86f4-3403-848e-2680af8ff527 | -13.54397 | -45.44542 | 2025-03-19 04:21:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2de8be68-ea96-3fb4-93fd-aa26d17605a4 | -15.08065 | -48.94514 | 2025-03-19 04:21:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 226c9064-e3ac-30bd-b06d-636bc2ef72c4 | -14.85799 | -45.19632 | 2025-03-19 04:21:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d467c444-0cdb-37cd-ae1f-f5ac8e2687d6 | -13.54063 | -45.44489 | 2025-03-19 04:21:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5759e90b-2dc9-3645-86e7-998aa959989a | -15.35708 | -46.95638 | 2025-03-19 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| efe0dd1d-662e-316e-bf36-bec7ee4da933 | -12.08288 | -45.62281 | 2025-03-19 04:21:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab5d0465-6b61-344e-8f82-13511e17a1be | -15.65739 | -40.66699 | 2025-03-19 04:21:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fb581f1d-ba77-32b2-a92e-98d005223a3a | -12.08455 | -45.63393 | 2025-03-19 04:21:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36babc9f-0572-309e-9cfa-def6a00f249a | -16.08268 | -46.62256 | 2025-03-19 04:21:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f231cab-8a57-3ba2-8e99-2ba2e2d4570c | -15.34768 | -46.95111 | 2025-03-19 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88ff75a5-40fd-311a-9b37-83d32701b7cd | -15.80064 | -42.03434 | 2025-03-19 04:21:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ad65b5aa-d846-36f4-bfe5-6ba70514e7ed | -15.35376 | -46.95581 | 2025-03-19 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ebb9440c-e384-394f-96d4-33a8b50d1977 | -15.35044 | -46.95525 | 2025-03-19 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f03e5f40-70d4-348b-87b0-08f1f7af8f53 | -12.27949 | -43.53132 | 2025-03-19 04:21:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 12a4c9d3-2665-3588-9903-53d863357ce6 | -10.64936 | -44.39884 | 2025-03-19 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bfad36d0-1800-34ee-8a05-1825e89d5f7d | -12.08842 | -45.63093 | 2025-03-19 04:21:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae291ed1-d9df-39a1-b792-8caa93be0ab7 | -16.086 | -46.62312 | 2025-03-19 04:21:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fcb2c15-cb5e-380b-81bf-17d0ae1a5fdf | -13.88793 | -41.65296 | 2025-03-19 04:21:00 | NPP-375D | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b1d1e70b-9e22-357d-8b31-f6818b64f00e | -15.34209 | -46.96487 | 2025-03-19 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75e9e674-c9fd-3b12-88e0-6255adc32be8 | -15.42438 | -40.58036 | 2025-03-19 04:21:00 | NPP-375D | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5b97a0c6-6ea4-30fa-b8f2-1b2bd3dfc0ff | -15.65526 | -40.66421 | 2025-03-19 04:21:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ac654161-1e15-3759-91f0-2391e467c179 | -12.08178 | -45.62986 | 2025-03-19 04:21:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc8983b7-c87c-33ef-bc73-dc40cd48fef1 | -10.65609 | -44.3999 | 2025-03-19 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca5a0390-8160-3bdd-9c39-750cce2fd0ce | -15.34436 | -46.95055 | 2025-03-19 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 764c5bab-3149-3bc8-8fad-7b2f17ed78e6 | -15.33933 | -46.96072 | 2025-03-19 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68e5f8e9-2158-3547-928b-8284cd7b28b1 | -13.2779 | -54.38113 | 2025-03-19 04:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 538eff88-2b4e-31b2-855f-7e6e0ec30e40 | -13.27069 | -54.3387 | 2025-03-19 04:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15f77e16-67f0-3aa6-9e0d-3ca283b071fb | -12.08233 | -45.62633 | 2025-03-19 04:21:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1040f26e-fbcf-3882-aba1-1f2022214fea | -12.09119 | -45.635 | 2025-03-19 04:21:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6fe2915-3edd-3133-8202-48898a3902f6 | -13.64244 | -48.44605 | 2025-03-19 04:21:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edd22c98-fb2e-39a6-9f6e-430d13b95bda | -12.46117 | -43.56919 | 2025-03-19 04:21:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 301c5dce-8fb2-395f-ac03-fb8fab338789 | -15.34655 | -46.95826 | 2025-03-19 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 072169db-d69c-3ab8-8125-4fa318b5acde | -15.35651 | -46.95995 | 2025-03-19 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a88f4af-0743-3fb2-8494-5dbcacede2aa | -16.29646 | -45.09484 | 2025-03-19 04:21:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9646cef0-8972-345b-84ac-33776fea1085 | -15.25563 | -43.67329 | 2025-03-19 04:21:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cb36f793-788d-328e-a0a7-b49de4912127 | -13.71198 | -48.43419 | 2025-03-19 04:21:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ca51281-db0d-3f89-9bea-05502fa6a20b | -16.29589 | -45.09865 | 2025-03-19 04:21:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e2b8e8d8-37d9-3c66-a636-348b5968138b | -12.0862 | -45.62334 | 2025-03-19 04:21:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 572f1ef7-105d-39eb-84d9-8f95d1b28f75 | -15.35319 | -46.95939 | 2025-03-19 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 927a8169-5f73-3c3d-ba9e-3ba5777ebcb4 | -14.12761 | -47.84366 | 2025-03-19 04:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25c90b92-ca2b-3444-b0af-e4212bed1b61 | -15.3493 | -46.96241 | 2025-03-19 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f3c25aa2-c4a6-316b-949b-9a0ff574b618 | -11.85178 | -37.58748 | 2025-03-19 04:21:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 463ecdff-3f92-3813-ae4a-50eddd12fa7a | -23.40384 | -46.55599 | 2025-03-19 04:23:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 086d7eed-c3d4-3a4f-b515-163271bb04a4 | -22.92143 | -42.41531 | 2025-03-19 04:23:00 | NPP-375D | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| c110f768-1916-375b-812c-56fa0dd0f919 | -22.92192 | -42.41111 | 2025-03-19 04:23:00 | NPP-375D | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0dd7e58c-5ecf-353c-9b5c-a9a1d03b6568 | -23.02071 | -48.03019 | 2025-03-19 04:23:00 | NPP-375D | CONCHAS | SÃO PAULO | Brasil | 3512308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e0433894-cd95-3339-aea4-ab4881ea56ba | -22.92287 | -42.41346 | 2025-03-19 04:23:00 | NPP-375D | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3eb45371-f64a-3814-abbd-cddf9946410a | -23.5941 | -47.44016 | 2025-03-19 04:23:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cefaca12-5fa4-3ca7-a473-00d0441ad669 | -22.91863 | -42.41289 | 2025-03-19 04:23:00 | NPP-375D | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 793c7f4f-61c2-3ed1-9cb2-29a17db35ef7 | -30.74612 | -52.66575 | 2025-03-19 04:25:00 | NPP-375D | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| f5f5a166-9b16-33d6-9cb3-c2429c915356 | -30.74271 | -52.66494 | 2025-03-19 04:25:00 | NPP-375D | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 05260da1-93cd-35d7-9196-42b605853ebd | -30.14892 | -52.02387 | 2025-03-19 04:25:00 | NPP-375D | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 40cac3ac-470d-3b0f-b329-ce5b5d2009a7 | -30.35726 | -54.29125 | 2025-03-19 04:25:00 | NPP-375D | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 3.9 |
| 4e58a552-197c-3b58-a335-9546fe2046f0 | -29.87308 | -51.15586 | 2025-03-19 04:25:00 | NPP-375D | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| ceb691cd-8c36-34d4-a4fb-b9995dd784ea | -26.96826 | -53.64035 | 2025-03-19 04:25:00 | NPP-375D | TUNÁPOLIS | SANTA CATARINA | Brasil | 4218756 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 959397fd-a967-380e-ac54-4e64f7395f27 | -27.33773 | -50.57626 | 2025-03-19 04:25:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README5.md)
