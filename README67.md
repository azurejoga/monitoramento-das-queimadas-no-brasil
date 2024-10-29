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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 535ed704-0ddf-3588-91b9-ccfe0a546602 | -13.69617 | -46.1165 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a7df629c-dddc-3d9a-851a-f8cc9dc9a72e | -13.69569 | -46.12004 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 25067f98-f02a-38ab-ae3e-fb92fc375195 | -13.69522 | -46.12357 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 3836a1b2-16b0-394a-84f0-0944b921ad72 | -13.6939 | -46.1333 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4b06caa7-e5b0-383c-856c-45c8b5c1adee | -13.69219 | -46.11589 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f4738a84-dcfb-317e-a4dc-e3e57f36e427 | -13.69171 | -46.11943 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 248415b4-6903-3ba7-98c9-5212f89b808c | -13.69124 | -46.12298 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| ee2ad175-5353-381e-9eb5-e520555dda6b | -13.69064 | -46.12743 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d0bf42ea-95a0-3f50-8d12-d0d2020ef71e | -13.68992 | -46.13277 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f52c4990-bd90-3eaa-9239-333d9b607487 | -13.6892 | -46.13811 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| acc08bbe-6449-3eb8-9e31-09424efa110b | -13.68773 | -46.11885 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 58bb7aa0-5285-3c72-8a98-5bea1e6c56df | -13.68521 | -46.1376 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed2e8342-3470-30b0-bd60-96a8a7a04134 | -13.68374 | -46.11832 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cada8142-ecc4-35f8-af61-8ee2b37b5caf | -13.62789 | -45.57927 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65c86dcf-0102-3601-ad80-3002b403f172 | -13.62221 | -45.59001 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac5b8feb-687e-3057-b369-c41e908a657f | -13.62079 | -45.59222 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f13b258b-a28f-3e78-9210-f63ef3bacb25 | -13.61554 | -45.57745 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bfcbe393-9861-372a-aefd-875f40549210 | -13.60986 | -45.58822 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0cc9f25d-6150-349f-a34c-f9aa0f5c6e04 | -13.60934 | -45.59201 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cf9959f2-a628-31ce-a7bc-8f309202c603 | -13.60679 | -45.58004 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| cf215e54-9111-30a4-846c-decaf1c738b8 | -13.60627 | -45.58384 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6f02d9de-e355-33f5-a10b-75381c2d2ca8 | -13.60575 | -45.58764 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8c2e0c44-3876-377e-afbb-54b19bff433b | -13.60523 | -45.59143 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9207a9b3-feba-39ed-a0ca-319a3dfafbfa | -13.60471 | -45.59522 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8aebf769-f723-3033-a3dd-c80443efbf00 | -13.60215 | -45.58324 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6bc817a4-beae-37ec-85a8-f48fb9f43616 | -13.60112 | -45.59083 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2f174da0-bbf2-391f-9b0b-0dacf4e60f1e | -13.6006 | -45.59461 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c07b78ea-42bd-3d11-b656-d2007c0d37ef | -13.3723 | -45.11483 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba8ab38e-ad54-39e6-8ffa-71ae37c5fab5 | -13.36911 | -45.10617 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 626a7f63-c931-3240-9cac-92b6184c0787 | -13.36906 | -45.10789 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27208943-5075-36bd-89d1-c2184a92574a | -13.36859 | -45.1102 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1c3e63e-6be5-3dfa-af1b-b3bc3cf9ce2c | -13.36851 | -45.11191 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05f83416-065f-3b82-bca0-4515536ca39d | -13.36807 | -45.11422 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 444485d1-0670-3392-a6bc-a811c054e49f | -13.36796 | -45.11592 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ac4a0b2-2db4-3e32-8adb-3d21cc2d4026 | -13.36593 | -45.09924 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70cf4e52-c459-37ed-8f57-4e9c9b7331a9 | -13.3654 | -45.10153 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 479c56d6-9a46-3fb4-a75f-71f197413419 | -13.36538 | -45.10328 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f4342a7-1967-3d4c-aab6-012e8f097514 | -13.36488 | -45.10556 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b1fcd23-e0c4-373d-8c36-4ece50f5acf4 | -13.36483 | -45.10728 | 2024-10-29 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9861e90-29e1-36cf-ba6c-8a08cc290ed4 | -15.089 | -46.64401 | 2024-10-29 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fc9fafb-038d-389d-922b-cd59134694e6 | -15.0858 | -46.6382 | 2024-10-29 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aee0bfe8-9fdd-32b1-8b1e-b6f6b39814bd | -14.16308 | -46.15861 | 2024-10-29 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de4a4cf5-97fe-3e06-a234-d513cbb7dcf7 | -13.63915 | -47.09702 | 2024-10-29 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7aabd0af-54cb-3a8b-ada7-7c310e2c6adf | -13.63786 | -47.09893 | 2024-10-29 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 414c84ac-d491-3fd0-9c4e-31a9da68db37 | -13.22064 | -47.76817 | 2024-10-29 04:42:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad4392d7-2d5d-3a63-9e96-b92429cdc25c | -13.22003 | -47.77242 | 2024-10-29 04:42:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f23da64-62f8-3b96-be0d-a2fba727d594 | -13.21874 | -47.80756 | 2024-10-29 04:42:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c491ec66-674a-3537-a39d-4981070e8549 | -12.80207 | -47.89365 | 2024-10-29 04:42:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b1420e3-d189-30d6-8596-7e01f310f8bf | -12.64628 | -47.54729 | 2024-10-29 04:42:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc4b7067-0cdc-34b8-80af-d958ce6f3809 | -12.64266 | -47.54675 | 2024-10-29 04:42:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ef10003-22fc-3c79-a092-76bb7e967680 | -12.63904 | -47.54621 | 2024-10-29 04:42:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb480cc1-3925-3692-8d70-ff62e6c5afc2 | -12.63842 | -47.55047 | 2024-10-29 04:42:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba1ec50a-3d93-3af5-be97-22db5cf51acf | -12.6348 | -47.54993 | 2024-10-29 04:42:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ccab7bf-0dd8-3674-a387-fe0da0eef153 | -12.63118 | -47.5494 | 2024-10-29 04:42:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee643830-0637-3973-b50f-a411533a6c4a | -12.62756 | -47.54886 | 2024-10-29 04:42:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 685c093e-fb2b-35f7-a172-4d63d269aa3e | -12.62695 | -47.55313 | 2024-10-29 04:42:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 600e5746-f116-30ac-a0e9-6fa6576d799b | -13.51864 | -48.21276 | 2024-10-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 179ead9c-d8b3-36a3-9d40-a5d17e965904 | -13.30494 | -48.97704 | 2024-10-29 04:42:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d8a172ea-c147-300f-ad3e-7e902ae400b8 | -13.23777 | -48.27728 | 2024-10-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c965def-53bd-3802-8789-d25b1278915f | -13.2254 | -48.31229 | 2024-10-29 04:42:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88bf862d-b778-3c3d-9f23-a112a0686896 | -13.08363 | -48.12139 | 2024-10-29 04:42:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e507036-1e43-37e8-b08f-d97c49c14486 | -12.69776 | -48.8433 | 2024-10-29 04:42:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa442b53-f011-32ae-8326-9c09cb61a815 | -12.61841 | -48.52971 | 2024-10-29 04:42:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac56c228-a805-3eaf-be2e-50281850bf66 | -12.56661 | -49.27741 | 2024-10-29 04:42:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 149f24c1-4a64-31a9-be9d-e9683cb0d03c | -12.38872 | -49.40417 | 2024-10-29 04:42:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f8b7610-06a3-36fd-b638-bdd56f088b52 | -13.87245 | -48.83495 | 2024-10-29 04:42:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e424d71e-5478-3aed-98f9-83f750c8e5af | -13.22753 | -49.83198 | 2024-10-29 04:42:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 922cd690-e35f-3e29-9a11-ffe6430ad0d7 | -12.5957 | -49.89437 | 2024-10-29 04:42:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d1480b8-57d4-366d-84fb-12ce62b70d50 | -12.45555 | -49.90118 | 2024-10-29 04:42:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed9ed63c-c904-3e04-91f2-18d58504177b | -12.34974 | -49.92447 | 2024-10-29 04:42:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c915ef76-8914-3f91-9e0c-88151bdacdd9 | -12.34919 | -49.92804 | 2024-10-29 04:42:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 72ae5fc0-0d42-359b-a8ed-77c2d9b34b76 | -12.34865 | -49.93159 | 2024-10-29 04:42:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b2a1787b-2a9a-39e9-a615-fabbb8f6dff9 | -12.3481 | -49.93516 | 2024-10-29 04:42:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a005d89a-0e1e-3685-b593-788f37aab203 | -12.34756 | -49.93873 | 2024-10-29 04:42:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a71f9cb6-d19d-3e1c-bd86-33dcd16c0a8c | -12.34707 | -49.92074 | 2024-10-29 04:42:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 8b951a17-304a-33d8-9403-de0b1e97802e | -12.34652 | -49.92431 | 2024-10-29 04:42:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| cbd0e056-ee77-37bd-abe4-38d8c4c89129 | -12.34597 | -49.92787 | 2024-10-29 04:42:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 4554a190-3331-3f5c-8737-8c1706336e82 | -12.34542 | -49.93143 | 2024-10-29 04:42:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| e6f6ea2f-03a6-3c61-9d3d-aa9ccd05ebc6 | -12.34487 | -49.93499 | 2024-10-29 04:42:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 5694e55f-b16f-3a0c-b10b-b8f248e6d5ff | -12.34375 | -49.92021 | 2024-10-29 04:42:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e79b000f-ac56-3e38-9e31-58e9a8754a5a | -12.3432 | -49.92378 | 2024-10-29 04:42:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| bbdc4c1a-47ee-3dd8-aacb-89310c4d2f9d | -12.34265 | -49.92734 | 2024-10-29 04:42:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 52bba4ac-595d-3560-8808-138aa0641089 | -12.34209 | -49.9309 | 2024-10-29 04:42:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 79353f6c-f043-37ef-b8ab-95f78dce3937 | -12.34154 | -49.93446 | 2024-10-29 04:42:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d0990b8f-e6e3-36c7-b7bb-a35d404d09c7 | -12.34042 | -49.91968 | 2024-10-29 04:42:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4965862f-c77c-30e0-95f9-1fff8da28e01 | -12.33987 | -49.92324 | 2024-10-29 04:42:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c6545cbe-b9b1-369d-b4e3-2efab07e6860 | -12.33932 | -49.9268 | 2024-10-29 04:42:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| de1887da-3656-3276-bb35-1c01a64018e2 | -12.33877 | -49.93036 | 2024-10-29 04:42:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2a1dc879-7c30-34cb-b546-99252dbe4e7d | -12.33767 | -49.93749 | 2024-10-29 04:42:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5000f6f6-25dd-3b04-9b46-9c9ceb0cfb44 | -12.09678 | -52.48156 | 2024-10-29 04:42:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8f4f1f7d-df50-370a-9696-758cd09f1d49 | -12.09617 | -52.48528 | 2024-10-29 04:42:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 28fc2ab3-acd8-3e84-8245-9b13513204bb | -12.09556 | -52.489 | 2024-10-29 04:42:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ec2ef15-d82e-3c4c-a77d-c5a91e318825 | -12.09338 | -52.481 | 2024-10-29 04:42:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eed121cc-e56a-3cb2-b059-b696277c6fbf | -12.09277 | -52.48471 | 2024-10-29 04:42:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ec9d2bbf-95de-3082-b98d-524bf2db2085 | -12.09216 | -52.48843 | 2024-10-29 04:42:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a391e64c-8b83-3fca-ae50-2ce288ed4139 | -13.25518 | -53.9261 | 2024-10-29 04:42:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9cce0c3d-2aea-3a03-97e8-596e9e8298fe | -13.25163 | -53.9255 | 2024-10-29 04:42:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3cae2d6d-9d8c-304a-ba82-2977db009823 | -11.89792 | -54.79776 | 2024-10-29 04:42:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6792df57-81f1-31de-8058-c776bf7293cd | -11.89709 | -54.80251 | 2024-10-29 04:42:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a05d584-6eb7-3386-91ec-1efa5a0bb4d1 | -11.76204 | -55.46075 | 2024-10-29 04:42:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README68.md)
