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
| dbc8154a-ec11-3f25-aa66-840fdf66278c | -14.53378 | -48.62379 | 2025-11-20 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 712f9a82-d0d7-3579-b5bc-aca59d8be4c6 | -17.53533 | -53.71225 | 2025-11-20 04:14:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 922c0674-350f-33e0-b86f-0d3c25782a85 | -17.6242 | -54.18963 | 2025-11-20 04:14:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eee9b848-e5a5-35e7-964d-465cb0095570 | -12.43171 | -47.88133 | 2025-11-20 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 254ed3ab-ba61-35c6-ac03-9b029ac8132b | -12.50528 | -49.87182 | 2025-11-20 04:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6dc39c2-3b0c-3b3b-9015-4ddf0811d2fc | -14.52972 | -48.62304 | 2025-11-20 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b6074618-697f-3e2d-a0bf-8b6aa264d27a | -19.76878 | -48.01195 | 2025-11-20 04:14:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 916d6a92-9942-3124-b549-2fff8cfdfd39 | -13.94255 | -47.45961 | 2025-11-20 04:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 149a9f42-f5da-3ee3-a40b-6d1bf9936eb1 | -15.64964 | -46.23282 | 2025-11-20 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc8d7ce1-da18-3e99-a4d4-3676c86ddec9 | -19.47535 | -48.92163 | 2025-11-20 04:14:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bb35389-954c-3c15-899f-ea61a1f72b6f | -15.47089 | -43.17558 | 2025-11-20 04:14:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a8d72c60-035e-3b37-8eaa-9b4bb0184513 | -15.54555 | -50.66195 | 2025-11-20 04:14:00 | NPP-375D | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 866b7a99-e787-3714-91e6-59515564a2b2 | -12.94685 | -47.70968 | 2025-11-20 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9190edaa-4c26-3b87-9dc4-b39ffe332a78 | -12.91138 | -45.10612 | 2025-11-20 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e8d11f67-ae22-3433-8e20-48900bd5ce4d | -17.62339 | -54.19349 | 2025-11-20 04:14:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b96b408-feb7-3c75-8bd3-00a7d4ca7105 | -12.61424 | -48.87415 | 2025-11-20 04:14:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b59d67a-a0f1-3ae6-a76b-977051d9e6a6 | -13.93956 | -47.45423 | 2025-11-20 04:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8dd65059-7cb3-36bc-8e32-e188b7e6f1fe | -17.53147 | -53.70403 | 2025-11-20 04:14:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 548586ff-ba7c-3b37-8849-4c00e0e35aee | -14.88859 | -49.57342 | 2025-11-20 04:14:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c9272a8-7c47-36e6-ac7e-26c8bb26226e | -17.47031 | -45.74739 | 2025-11-20 04:14:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a80a99f0-a11a-38b0-b963-982ff31236a5 | -17.61951 | -54.1847 | 2025-11-20 04:14:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6bd08d6b-ddae-3ac8-8cc4-4b3e961a46d1 | -19.87838 | -44.05282 | 2025-11-20 04:14:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1e9ec527-bd7c-3b40-afb3-e8e42bfdde40 | -10.83739 | -56.95412 | 2025-11-20 04:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d523f3f9-c045-39f0-a653-0856bbf7e805 | -14.53444 | -48.62016 | 2025-11-20 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4cc0506-8aad-34c0-b01a-60c2a0630391 | -10.84463 | -56.9557 | 2025-11-20 04:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| eb8e21a7-c132-36be-bf9e-783244ea9cc1 | -12.88491 | -50.15881 | 2025-11-20 04:14:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8a93f058-7f22-3ffe-b3bf-ed286f957d73 | -10.83584 | -56.96164 | 2025-11-20 04:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 1ba5461d-0025-3a1d-b801-cc2351fdc035 | -13.48837 | -46.70974 | 2025-11-20 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 09610f83-7630-38dd-be0d-0e63b142b8e4 | -15.55864 | -43.54645 | 2025-11-20 04:14:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a54cfa76-8100-3c1a-a04e-e5b0bcb8ceed | -14.62873 | -46.54068 | 2025-11-20 04:14:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5be08a41-d659-3c01-9978-69ce7b802396 | -15.5403 | -50.66347 | 2025-11-20 04:14:00 | NPP-375D | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 26.7 |
| a05bc2b4-ed0b-3d57-ba25-41c83933c4c8 | -18.12195 | -54.52384 | 2025-11-20 04:14:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 977dec88-094d-3889-a8da-71f054032f37 | -16.3243 | -50.0515 | 2025-11-20 04:14:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 562feb9c-61e5-324f-be52-6d1cfd21b029 | -13.16976 | -48.29945 | 2025-11-20 04:14:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d368faad-57af-3140-a351-5f11ecf8f1cb | -12.6192 | -48.87096 | 2025-11-20 04:14:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| faf739b4-697d-31f1-a37e-a63430f25109 | -12.67905 | -46.77658 | 2025-11-20 04:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe6d6620-05e9-3466-889b-3327ca9bbc07 | -15.54462 | -50.66671 | 2025-11-20 04:14:00 | NPP-375D | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| b8986a9a-5d2d-3db0-a30a-02138d292176 | -19.47155 | -48.92085 | 2025-11-20 04:14:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5dfb0b8-df02-3dc9-9207-844b59e920bd | -12.68199 | -46.77964 | 2025-11-20 04:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a550eb4-56ef-3c29-971b-477f459a62c1 | -17.50457 | -44.92245 | 2025-11-20 04:14:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0769a71-3e74-317b-91e2-445baad9407a | -14.54595 | -48.62598 | 2025-11-20 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44681f09-d6fd-3293-8ed7-12c2dc72cdc4 | -13.3579 | -47.66003 | 2025-11-20 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c9faf1d-2547-3324-af94-3ebf44db9c10 | -20.34677 | -44.71568 | 2025-11-20 04:14:00 | NPP-375D | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 533f644c-a584-3ebe-93e7-346007b1b142 | -10.83764 | -56.95761 | 2025-11-20 04:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| e1ba3664-3068-3b77-b269-554d1dbddad6 | -13.09595 | -46.40527 | 2025-11-20 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 670ee61d-5783-3b71-95d4-b96e041e0f2c | -13.9324 | -47.47274 | 2025-11-20 04:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aacced96-5f33-35b2-8f38-2c5a42461ed3 | -19.97902 | -44.85547 | 2025-11-20 04:14:00 | NPP-375D | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eba67655-a341-3395-b19b-da1b608c126f | -19.76957 | -48.00753 | 2025-11-20 04:14:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f7b9de2-815c-3197-bafd-5b3bc0474476 | -17.61395 | -54.1839 | 2025-11-20 04:14:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76b76798-ed27-32f8-81c9-457cc3a945b0 | -14.51407 | -47.36097 | 2025-11-20 04:14:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1726e9d1-c95d-368d-b3fb-21d0003c2a64 | -13.93875 | -47.45887 | 2025-11-20 04:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7b9249f-06d6-3822-aa86-5d373ae9e5cd | -16.19946 | -52.58698 | 2025-11-20 04:14:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46927ef8-fdb8-3f46-8132-87a9bb9362ab | -17.96329 | -42.70279 | 2025-11-20 04:14:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| df4240e8-da67-33ae-910d-e23e0a39a263 | -14.5385 | -48.62091 | 2025-11-20 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b4f37095-9cff-3b71-87e5-53845c982cd0 | -18.12282 | -54.51983 | 2025-11-20 04:14:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2890d40a-2c3d-3a44-88a9-4c6deb13fc28 | -13.0756 | -49.51536 | 2025-11-20 04:14:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e864c0b-a57d-34aa-a0f9-36575129ba44 | -15.54394 | -50.6692 | 2025-11-20 04:14:00 | NPP-375D | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 547aa6d8-00c3-3de9-9e63-43622dbddfa4 | -12.88031 | -50.15789 | 2025-11-20 04:14:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f5e65ea7-df56-35c1-85af-2b4ca43e4951 | -12.42833 | -47.87706 | 2025-11-20 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e302f02-f92f-3968-99d6-1aa5444ba3cb | -17.90387 | -46.71473 | 2025-11-20 04:14:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7529916e-b646-339f-8935-449c1ffa7145 | -21.04598 | -48.55392 | 2025-11-20 04:16:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e992d01e-6c95-355c-bc73-5056c493b009 | -20.73686 | -55.70113 | 2025-11-20 04:16:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c2811a74-851a-3a03-a144-532a9d76fdb0 | -21.29081 | -41.02653 | 2025-11-20 04:16:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 51db437a-078d-3066-9266-0285a0572f38 | -20.29869 | -50.97013 | 2025-11-20 04:16:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.1 |
| 7814cc3b-7284-34de-ba68-14bd7fcc5cbd | -22.42512 | -47.63191 | 2025-11-20 04:16:00 | NPP-375D | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b4205512-d34e-3468-8548-936caf94a15d | -20.6797 | -50.12375 | 2025-11-20 04:16:00 | NPP-375D | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ea521170-74bf-36ff-95c0-7e233d30484c | -21.03955 | -48.55505 | 2025-11-20 04:16:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 37c7b04c-5c93-3312-b6d9-000a5fef97d8 | -21.04036 | -48.55049 | 2025-11-20 04:16:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| f59cfba3-2063-3e95-9d67-ba8ea0b1b1ee | -21.1454 | -48.52711 | 2025-11-20 04:16:00 | NPP-375D | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 50b9d98e-5eaa-37a3-bfb0-c963469f97ef | -20.28937 | -50.97257 | 2025-11-20 04:16:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 4378ca2f-0f1f-39a0-8a79-5592db003feb | -21.62133 | -43.59304 | 2025-11-20 04:16:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 54619042-2d6c-3dcd-a1d0-17be924ea758 | -20.30034 | -50.96175 | 2025-11-20 04:16:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| c06c7055-432e-3ebb-9d76-ab7937724234 | -20.99002 | -42.89472 | 2025-11-20 04:16:00 | NPP-375D | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5c1f3a55-12f2-3673-8974-9cc2baa71a34 | -20.29952 | -50.96592 | 2025-11-20 04:16:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.1 |
| e46cb16f-c041-312e-bfc8-1ef18f55b91e | -21.89498 | -42.0652 | 2025-11-20 04:16:00 | NPP-375D | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| bde6f43d-8a7e-3ca1-89cc-3e7de98aea7e | -20.88851 | -52.34649 | 2025-11-20 04:16:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a09f86cc-e790-3172-b1fc-6267ef30a27f | -19.47397 | -53.9538 | 2025-11-20 04:16:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e80d8893-b79c-3331-9ac8-32d8e7794ddd | -21.33374 | -48.69014 | 2025-11-20 04:16:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4122c082-5053-3929-96ee-848cf5f60c87 | -24.38015 | -50.42221 | 2025-11-20 04:16:00 | NPP-375D | TELÊMACO BORBA | PARANÁ | Brasil | 4127106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| d2245998-7b34-365b-9ee0-b5755b00ece4 | -21.4244 | -41.17113 | 2025-11-20 04:16:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 81d8aa86-5f42-3d24-9821-c5db3fc3b27f | -22.94682 | -47.47649 | 2025-11-20 04:16:00 | NPP-375D | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| becf00c2-8586-3a9f-93d8-e0d9698d53cf | -20.23878 | -50.67464 | 2025-11-20 04:16:00 | NPP-375D | SANTA SALETE | SÃO PAULO | Brasil | 3547650 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 737ac06f-ad3d-3740-a7c1-0c42af908e83 | -20.88291 | -52.35044 | 2025-11-20 04:16:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee3cc412-c71f-383c-b0d2-938738b76859 | -21.78313 | -43.43935 | 2025-11-20 04:16:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6c56c677-3560-384f-b55a-87e3f9c18b85 | -19.47549 | -53.94667 | 2025-11-20 04:16:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 253e89b5-1f8b-3090-afc2-3d483473fc08 | -20.28854 | -50.97683 | 2025-11-20 04:16:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 71296104-cd33-37d5-b5ec-2319a71609fb | -23.02725 | -45.86759 | 2025-11-20 04:16:00 | NPP-375D | MONTEIRO LOBATO | SÃO PAULO | Brasil | 3531704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a0b0240a-6c94-3379-bd75-2f9498414296 | -20.88397 | -52.34531 | 2025-11-20 04:16:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00f45438-5a55-3e9d-95f9-1e6ffc4b1ac8 | -22.51401 | -44.69722 | 2025-11-20 04:16:00 | NPP-375D | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f63dbdff-c613-3950-99b4-4cdf9e953d8f | -20.29528 | -50.96502 | 2025-11-20 04:16:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.1 |
| 23644d50-b9d6-343e-a8df-b59392f6a023 | -23.49199 | -46.77539 | 2025-11-20 04:16:00 | NPP-375D | OSASCO | SÃO PAULO | Brasil | 3534401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| fac11932-a7cd-3458-a015-ff364bbd988e | -21.14905 | -48.52782 | 2025-11-20 04:16:00 | NPP-375D | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 08c67dae-dce3-37e1-8805-8a5e13f290b5 | -19.47473 | -53.95025 | 2025-11-20 04:16:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 64727c4a-242e-377d-84ed-103a33150017 | -20.56338 | -49.56925 | 2025-11-20 04:16:00 | NPP-375D | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24a2ea09-64d0-3c53-9058-692ba3e7ca2a | -20.29278 | -50.97775 | 2025-11-20 04:16:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.3 |
| be6fce6f-96e0-3299-ade9-4354dfe69b94 | -24.37532 | -50.42667 | 2025-11-20 04:16:00 | NPP-375D | TELÊMACO BORBA | PARANÁ | Brasil | 4127106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 6fcff563-af0f-3db6-89e7-45e1671434b3 | -21.33008 | -48.68939 | 2025-11-20 04:16:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7e9cd09a-762b-35dc-a026-4e4057a2dae0 | -26.43229 | -48.72056 | 2025-11-20 04:16:00 | NPP-375D | ARAQUARI | SANTA CATARINA | Brasil | 4201307 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d6d8b01b-bac2-38ee-84db-b171a16b79da | -20.29362 | -50.97347 | 2025-11-20 04:16:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.3 |
| 5b72f9d8-8924-38fc-95bf-80dc5ecbe548 | -22.83476 | -46.32193 | 2025-11-20 04:16:00 | NPP-375D | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README9.md)
