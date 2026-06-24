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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3d7819b-4c88-392c-ae70-8e8529cc6ea7 | -12.77711 | -44.4392 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6f9f2328-501e-3dfb-9c7b-1134d5437a99 | -12.84112 | -44.36126 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 2b86398a-3446-3d71-982a-091962deacbe | -15.72399 | -41.35574 | 2026-06-24 03:47:00 | NOAA-20 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8ec42574-05f8-3631-bd03-8a53902acb8d | -13.66943 | -41.80808 | 2026-06-24 03:47:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2fdb536b-4964-3d56-9267-49c2864cf598 | -12.77808 | -44.43394 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fccb3201-9ed2-3426-ba51-a1e8b5b2dca6 | -14.87494 | -48.37235 | 2026-06-24 03:47:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8222175e-f694-34fb-961f-0986b44901a8 | -14.87595 | -48.36752 | 2026-06-24 03:47:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c17344da-8364-3db3-96ae-c325a1ba5f7f | -12.78053 | -44.4469 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8881b846-21ba-3c38-9f7b-185eb03cec15 | -8.60833 | -46.00343 | 2026-06-24 03:47:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| c2b57447-1e23-38f4-bb47-8fe1e472a811 | -12.77614 | -44.44446 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 171161a8-17f7-3155-ae62-cfc57d37b05d | -4.66328 | -43.12356 | 2026-06-24 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 794655de-383c-368e-ae04-7dee1197f4a5 | -12.51673 | -48.27541 | 2026-06-24 03:47:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db01bae8-08e0-3f26-8824-b803d02e2bb4 | -4.65826 | -43.1227 | 2026-06-24 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac92d484-6133-3b4d-bc8e-aa4e8e862ed4 | -7.36507 | -47.0314 | 2026-06-24 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6827fa2c-f7e2-3074-8f7c-edc8c89498a4 | -8.68625 | -47.8509 | 2026-06-24 03:47:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| aed7d739-99d8-3a87-b485-6717336f36d7 | -12.51159 | -48.26942 | 2026-06-24 03:47:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 700ac69a-bc7a-3574-b322-9b733c3eeff4 | -14.83757 | -40.96109 | 2026-06-24 03:47:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7cc1ef39-5c62-3dfc-8865-57b199438ddc | -9.0338 | -42.70417 | 2026-06-24 03:47:00 | NOAA-20 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 43b72084-9df5-39e6-93d2-90d0fc902625 | -8.9791 | -40.26255 | 2026-06-24 03:47:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cf422920-8f03-3627-8068-0524f3358028 | -12.84013 | -44.36649 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| b2dcd4a2-58a4-31dc-a257-6c6ff567a15c | -13.84866 | -47.04049 | 2026-06-24 03:47:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9628d0e7-c55e-3978-9044-54ce355e66d9 | -12.19187 | -47.97208 | 2026-06-24 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f01525ab-d43f-39d9-837a-ec0ed3481144 | -3.8728 | -42.96466 | 2026-06-24 03:47:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7f5bd7d-ab5a-33b0-9519-e447b387271c | -12.84683 | -44.35699 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 50d14d4b-55aa-3720-8b67-830f06f45426 | -4.31506 | -38.4914 | 2026-06-24 03:47:00 | NOAA-20 | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9c3e81c4-b9bb-3c8b-9845-2dc73047d6ff | -4.66686 | -43.21946 | 2026-06-24 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13ef890d-880c-308a-87fb-418d55236c91 | -4.66724 | -43.22382 | 2026-06-24 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9ce6ff9-7960-3660-8ff9-4db7398e1dff | -6.99587 | -42.89582 | 2026-06-24 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 2b6f7e98-0159-3596-9457-453989a0abb9 | -8.6047 | -46.00166 | 2026-06-24 03:47:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 6e40a1fe-342e-3a78-a786-1f4397cf810f | -12.51769 | -48.27071 | 2026-06-24 03:47:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01b2591b-8f3f-3271-a08e-5a2839a91276 | -8.85315 | -46.94865 | 2026-06-24 03:47:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33c8d254-549a-329d-8a18-95dd55b7bab8 | -8.85408 | -46.94366 | 2026-06-24 03:47:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c52e054b-bf75-3e6b-8be1-2cda066eaca7 | -6.36128 | -43.59398 | 2026-06-24 03:47:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9e8324ff-7e4f-31f6-a9af-25526b694760 | -12.77516 | -44.44975 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 731cee1c-2374-3e69-a29a-708994d53625 | -6.50687 | -42.22403 | 2026-06-24 03:47:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b95557cf-877f-34c7-86e1-ecebfd020b8a | -7.91843 | -48.28968 | 2026-06-24 03:47:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 431e393c-4f67-3744-9f8f-69779e015355 | -4.66773 | -43.22089 | 2026-06-24 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ccd023ff-f6f7-3378-91d5-edbb1f30ff7d | -3.95992 | -43.11663 | 2026-06-24 03:47:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc509b78-baac-3a11-b6dd-4c790d5fc963 | -13.54801 | -42.49071 | 2026-06-24 03:47:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d73ad00f-1d5b-36f2-91d1-2b04d7689aae | -4.66121 | -43.22883 | 2026-06-24 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2021eecb-7dfd-34e6-92dd-dc95f0c1150e | -8.61199 | -45.99414 | 2026-06-24 03:47:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| e0377c9a-e0c5-398f-98a5-cfa4f9fb3faa | -12.8354 | -44.36558 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 8e009af6-967e-37f0-bc74-6cb87041166b | -3.86678 | -42.9696 | 2026-06-24 03:47:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 58107567-a6da-3a89-974c-a7e235269006 | -9.21743 | -45.33988 | 2026-06-24 03:47:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5b6f46ed-3d72-3ca6-8421-a57a856060fd | -13.85412 | -47.04194 | 2026-06-24 03:47:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8062f877-e7cf-32dc-a175-f39c73884b15 | -13.18471 | -43.39829 | 2026-06-24 03:47:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 97d6561d-552a-317b-ac36-749f67b65884 | -7.60016 | -46.47985 | 2026-06-24 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e9613b9-d00f-37bf-a6ef-de8c2411d0d4 | -15.72854 | -41.35172 | 2026-06-24 03:47:00 | NOAA-20 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 7272886c-c635-336f-a43c-134766cb7417 | -7.29578 | -46.24723 | 2026-06-24 03:47:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c122507-c898-3512-a5cb-8d42affff811 | -4.6613 | -43.2215 | 2026-06-24 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53495ed4-96a6-323e-a0f5-006a548c3a60 | -6.36076 | -43.5969 | 2026-06-24 03:47:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 93d43455-a725-37ed-872c-8c6a7e44100c | -5.10842 | -38.06489 | 2026-06-24 03:47:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 05943bba-d7f3-3a9a-b18f-d6cce234d220 | -6.99657 | -42.88899 | 2026-06-24 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 56858a9a-f601-34b8-b10b-d109d341e957 | -8.12257 | -47.88638 | 2026-06-24 03:47:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 303e378f-4db0-3ae8-85d5-fe361c6df398 | -12.83441 | -44.3708 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| e2926c73-b75e-3455-9c03-e68f9f2e0b04 | -4.65275 | -43.12474 | 2026-06-24 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebf7ec9a-9fed-3e57-b3cd-f1d6cc582848 | -8.60969 | -46.00633 | 2026-06-24 03:47:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6079a1d4-5f35-3384-909f-b79291cadb60 | -12.78527 | -44.4479 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 45a46862-11a4-314f-a659-24bac9146351 | -15.36389 | -47.36422 | 2026-06-24 03:47:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 44856629-cacf-3b9a-b903-f09ce60c5924 | -14.83838 | -40.95656 | 2026-06-24 03:47:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 319c3dbd-9076-36bd-97d3-2a1e9aa55808 | -7.37237 | -42.79789 | 2026-06-24 03:47:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 78b72613-d789-35e5-b2a0-9b2b4bfbc017 | -15.30522 | -42.01781 | 2026-06-24 03:47:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 336302a1-3ce1-3a24-8188-21943f439bbe | -8.85592 | -46.94358 | 2026-06-24 03:47:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba6e6e8c-7632-3fe1-a1f2-2e554ff2a374 | -12.83067 | -44.36468 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| cd288ddf-3726-3b6f-bccc-ec4e2efb1a10 | -4.66079 | -43.22444 | 2026-06-24 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| acc4b7b9-2f5d-373e-bfcb-e246bbf9667e | -6.84129 | -47.86395 | 2026-06-24 03:47:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b088cd6-038d-3059-b3a8-fef6ba3098b0 | -13.39729 | -44.12253 | 2026-06-24 03:47:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08e07cc7-b05b-384e-81ff-1cbd3557b76a | -9.21807 | -45.33644 | 2026-06-24 03:47:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e481780e-463d-371b-9792-a60c686701da | -12.78254 | -44.43645 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 83ac2784-7119-36a8-87cc-3946d788b3f3 | -3.86777 | -42.96381 | 2026-06-24 03:47:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cc80d0fb-e06f-3bbd-ad83-e28f12805c3b | -9.21478 | -47.92983 | 2026-06-24 03:47:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb277c81-c238-3cce-867e-6fb7f9bcb9b1 | -6.50771 | -42.21917 | 2026-06-24 03:47:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 7a0d6fa5-d413-3ca3-8e6f-1e3ba22a17c8 | -12.78628 | -44.44267 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 085165cd-ad65-31c7-a484-de3122833845 | -12.83738 | -44.35514 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| bc13e78c-2689-3b67-9d21-a8f91f24f8c4 | -13.54595 | -42.47836 | 2026-06-24 03:47:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e32c94ca-8d67-3eb7-8c29-9c2eec0e931c | -6.50233 | -42.22304 | 2026-06-24 03:47:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f595a6d5-b6a2-3a91-9b03-1b12ff40966a | -4.66219 | -43.22293 | 2026-06-24 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a24b1f6-ccba-3fb1-8730-d84dbc71e9ab | -14.84292 | -40.82856 | 2026-06-24 03:47:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 91c71089-eb60-3d4f-a985-60967b925afb | -15.72772 | -41.35646 | 2026-06-24 03:47:00 | NOAA-20 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 78909500-56dc-3219-9168-445eea58cf62 | -13.5487 | -42.48685 | 2026-06-24 03:47:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ad05cf10-c225-3705-95bd-12d1d413611b | -8.68334 | -47.85711 | 2026-06-24 03:47:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9d1179f2-850e-3595-a54f-a602cc55e8f7 | -14.51179 | -40.35618 | 2026-06-24 03:47:00 | NOAA-20 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 302c2860-a90d-38fc-a243-444302d4a663 | -12.77895 | -44.45597 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 522ba697-a644-325d-af66-53208c0f943b | -8.67892 | -47.85469 | 2026-06-24 03:47:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| bd8c6029-996b-3505-b681-4ed9fb230ac4 | -12.81446 | -43.89993 | 2026-06-24 03:47:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3000dff4-dd9e-3852-ba60-7d39f5acd5e2 | -7.28989 | -46.24615 | 2026-06-24 03:47:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35799ed1-b04a-3c06-bbcb-c04b7d19b419 | -15.01503 | -42.36762 | 2026-06-24 03:47:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 19c1f934-9ebb-309d-8c06-8443c78bc40b | -9.22227 | -40.53342 | 2026-06-24 03:47:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7a343e4d-78fa-3142-a2c0-1b4b0f5e2414 | -15.36465 | -47.36049 | 2026-06-24 03:47:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ff428f1-0d34-303a-a5cb-1365df99c038 | -11.6169 | -48.49072 | 2026-06-24 03:47:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60dc547e-e948-3805-9e6e-c577fe93e6c2 | -7.37151 | -42.80278 | 2026-06-24 03:47:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0c56a4af-308c-3d3f-a1c4-08fcce1d54aa | -13.53081 | -42.49133 | 2026-06-24 03:47:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| acd53d0f-a03c-306e-a14d-d19cb18eeafd | -6.99482 | -42.89927 | 2026-06-24 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| c3e0f194-61d0-3f00-9fed-10bf91bd07fe | -15.75635 | -43.22909 | 2026-06-24 03:47:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 4aacde1a-78a9-39f2-9216-da8d98dccfa6 | -8.61124 | -45.99813 | 2026-06-24 03:47:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ddd49fab-f08e-3627-98c0-95bea4b80619 | -12.19286 | -47.96727 | 2026-06-24 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17648db8-19e4-31f5-b40f-8d6ad5404958 | -7.9118 | -48.28851 | 2026-06-24 03:47:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 558099d0-412e-3920-ae51-74bce81dc174 | -8.60982 | -45.99519 | 2026-06-24 03:47:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 77d73870-ccdb-3dcb-9f52-a8ee8fc990fc | -9.21142 | -45.34227 | 2026-06-24 03:47:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46f4d89d-816f-3b51-b3c4-d120658ccc7e | -9.22217 | -45.34437 | 2026-06-24 03:47:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README9.md)
