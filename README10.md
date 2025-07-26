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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e106df1d-4ee6-36ca-9300-2239f8e1e646 | -4.61633 | -43.32458 | 2025-07-26 04:02:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d9e26ce0-1ab2-31c4-be97-8fc18f8f4a1a | -6.22489 | -44.52321 | 2025-07-26 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a9dda647-ad1e-39db-9b04-f608d8a34cd5 | -6.41907 | -45.08249 | 2025-07-26 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2edcb580-5cce-32b2-9cbb-7808fb8a013d | -13.70145 | -45.69165 | 2025-07-26 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e45a7efb-0c97-3b19-8455-ad5d2124c901 | -9.73179 | -48.01692 | 2025-07-26 04:04:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| adc2d09a-4edb-35bb-afe9-7daf2b9a7c9c | -9.02481 | -45.35145 | 2025-07-26 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfa40c86-902f-3974-8cb8-c102baf7b3d8 | -13.64891 | -46.82082 | 2025-07-26 04:04:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8855f231-1bdc-3ab7-8e3b-fdd3712c9567 | -12.70405 | -47.00618 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| daf0e023-da08-3e93-a1d7-61886b17e7a2 | -12.29914 | -40.09031 | 2025-07-26 04:04:00 | NPP-375D | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7d8d6e7c-4c0f-3daa-be3b-efa09e5a617b | -9.81136 | -46.71499 | 2025-07-26 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| bdcc0042-cc28-3039-ba0e-5195a1a9e196 | -13.11718 | -47.33966 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4c2b0f1e-f16c-3aa7-8275-fd3b15e91d79 | -7.56503 | -44.48724 | 2025-07-26 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd194170-6ad9-3113-b05e-2105b6cfa232 | -8.17397 | -43.21525 | 2025-07-26 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| a21013c7-7e9c-3c26-96c5-9ed889664b71 | -10.67903 | -51.89314 | 2025-07-26 04:04:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 93107f04-9336-361f-91a7-76bf825222fe | -13.24376 | -51.15836 | 2025-07-26 04:04:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 922f1458-9cde-37da-8569-44ddedba4c00 | -11.94721 | -43.82844 | 2025-07-26 04:04:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2c7b4179-1945-381d-bfb9-22c8430500bd | -10.96295 | -42.18262 | 2025-07-26 04:04:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a7b08cb8-db5a-353c-8bf7-0ad145912201 | -9.00804 | -45.36751 | 2025-07-26 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 661d6403-4f4d-3cc1-bade-123f464be4fc | -7.46035 | -49.39798 | 2025-07-26 04:04:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5bc670aa-4d49-3b1a-ac3f-6f0a2a0c2af9 | -12.6888 | -46.99491 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ae6898bc-bf57-398b-af3f-7d639bcab113 | -13.11384 | -47.35018 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18ff5d56-0710-306a-bb5b-315a9f21e024 | -13.23833 | -51.15722 | 2025-07-26 04:04:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93cabfff-34b5-35d1-a6d2-eb6734879e30 | -9.58099 | -43.85667 | 2025-07-26 04:04:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2e8b9d49-f789-3b02-acef-b74b5aa5e863 | -12.71703 | -46.27173 | 2025-07-26 04:04:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7180a275-adee-3aaa-8dea-287de4b05d97 | -11.95074 | -43.82906 | 2025-07-26 04:04:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89bf4318-b43e-3a6b-89d4-43574ca592b9 | -12.68388 | -46.99826 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07f6f691-5476-340d-aa52-ab529798ee93 | -13.11074 | -47.35132 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b14109e2-bac9-35cf-9487-6d2104ca0c43 | -12.71091 | -47.79472 | 2025-07-26 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7585a839-a1b9-30d3-8432-e2fe577932d3 | -13.24445 | -51.15479 | 2025-07-26 04:04:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f7083ed-6bc3-3e70-abeb-31ceb0e8c612 | -11.46041 | -45.19395 | 2025-07-26 04:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bddf95ec-4f49-3b1d-a048-2e1e0637d435 | -7.3622 | -46.218 | 2025-07-26 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 236045ab-e61b-3dfb-b5fc-f73340337084 | -8.56701 | -47.24204 | 2025-07-26 04:04:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e715275-f25c-3f1b-88ea-cb2d33ca558b | -7.53699 | -42.42489 | 2025-07-26 04:04:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0a2de12b-82d0-33cc-b29a-cef11f4d3071 | -13.1265 | -47.32907 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e4d80f3c-3cb8-381b-9b0f-33ed7a3322d3 | -13.2391 | -40.59632 | 2025-07-26 04:04:00 | NPP-375D | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 43489855-d78c-30f8-af10-449e08e77317 | -13.10207 | -47.36633 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70a2e063-ec49-3662-bd85-5c5ce845d5bc | -13.69633 | -45.67606 | 2025-07-26 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14f72b8e-bbe2-3130-ac16-f50b195da1e8 | -14.13021 | -45.27801 | 2025-07-26 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2a8bd97-495f-3f40-bcd4-935753dbb011 | -13.09223 | -47.35678 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e96670f9-2fdb-3bf1-8a82-e8ea08f79dd2 | -13.70309 | -45.68217 | 2025-07-26 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bebf91d-e760-36ef-9b93-3c124354d0bf | -13.23903 | -51.15364 | 2025-07-26 04:04:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 581cab8b-6e66-34f4-9c33-c207cfa7f6eb | -12.70479 | -47.002 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 158ee0f2-10a0-31b1-aa52-475a88a61fa6 | -9.13496 | -45.87207 | 2025-07-26 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 018ae625-645b-3a22-8f6f-879af54002ea | -12.71117 | -47.79674 | 2025-07-26 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f4017b20-e972-3152-883c-1b4140b4de5e | -9.47277 | -40.37024 | 2025-07-26 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| bb93cb3b-f852-348a-8461-1a7780b137b9 | -13.08937 | -47.34827 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8644bfe1-8c71-387c-9b56-4fd14068ad1b | -14.21918 | -43.96083 | 2025-07-26 04:04:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85fd0b96-c6f6-3399-bafa-25082d48c00e | -7.36554 | -43.43339 | 2025-07-26 04:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14b08d66-a74c-3301-a9fa-36679b07d506 | -8.87183 | -45.58445 | 2025-07-26 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d9312d7-f3b1-33e9-a280-ea33ac35db12 | -13.2352 | -40.59938 | 2025-07-26 04:04:00 | NPP-375D | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 2965cbdb-7a54-30e6-8cf8-3ec51e24af26 | -13.67657 | -44.2239 | 2025-07-26 04:04:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b3f5e87-59e3-34cd-9b0a-a7918983ab03 | -13.11225 | -47.35878 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63825509-837f-3698-b0cc-e917b9de4d27 | -9.73649 | -48.01782 | 2025-07-26 04:04:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33be4b1b-a225-3e19-93c6-e1835993cae8 | -13.72123 | -45.69039 | 2025-07-26 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2cb1a9b-7481-3c04-bf88-e2bd67e70c3e | -13.1161 | -47.33795 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e676de83-18bc-3296-acf8-b312049f763b | -14.21984 | -43.95692 | 2025-07-26 04:04:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2688b390-a8ad-397b-acd8-ea0d6ab4c27c | -7.63949 | -44.27934 | 2025-07-26 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3edfaac3-ed52-3084-a1f1-61a739ead892 | -13.11501 | -47.35194 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05db070f-8c9d-3711-ba4a-aca5ee731ae2 | -13.7242 | -45.69587 | 2025-07-26 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 37aa1a45-6ff5-38dc-9ec5-6dfe3c0395b6 | -14.13255 | -45.27623 | 2025-07-26 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d120dc61-c4f3-3149-a9d7-8897ffc1748c | -9.36307 | -40.31331 | 2025-07-26 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 5b657c87-f81f-32f2-9934-04ad1dc589aa | -13.09989 | -47.36306 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3bce0886-6ae1-389c-b930-62e609fba853 | -8.17196 | -43.2276 | 2025-07-26 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7dcedfff-b481-3405-b137-ac5166b48a95 | -12.04446 | -45.4402 | 2025-07-26 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70353de8-0fcd-33ab-818e-0beb7129b4d3 | -13.18298 | -42.32314 | 2025-07-26 04:04:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ca9e6655-7781-37a6-a0eb-957f1ff71d20 | -13.6993 | -45.68148 | 2025-07-26 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ecef1f1-c014-38c9-b3ed-61b70b3058c7 | -12.04593 | -45.44313 | 2025-07-26 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d488c8fa-045c-3385-a933-e9fc2d6db0de | -13.10288 | -47.36199 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72d8ff14-54bf-38bb-a5b7-27ec6fed4e1e | -14.22049 | -43.953 | 2025-07-26 04:04:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 85282d46-838c-3d81-afd5-5f2bfd2f5ca3 | -12.04674 | -45.43832 | 2025-07-26 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0da18585-afea-368f-878e-55207de328be | -9.47 | -40.36621 | 2025-07-26 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 31abb466-a295-33f9-ab36-80d9a33e818b | -14.29413 | -47.42029 | 2025-07-26 04:04:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| aeb7ad2f-f302-384c-8156-0dfd1843752e | -9.13432 | -45.87583 | 2025-07-26 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e76cdd99-a379-32bb-8c57-727c949738bb | -8.87209 | -45.58007 | 2025-07-26 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab855dee-b659-3c43-9b9b-c8dd117623ca | -14.21702 | -43.95238 | 2025-07-26 04:04:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e586d534-0815-32d5-85de-e9a4fe893dee | -13.12715 | -47.3255 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| abb8da36-08b4-31f1-b42a-46d488010c15 | -11.11068 | -45.1185 | 2025-07-26 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2666eb4c-09f7-30f8-81a2-cfa33cb90fa6 | -11.73889 | -48.18695 | 2025-07-26 04:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f0605809-7cc4-3d08-a342-10b16d959423 | -6.98974 | -47.07945 | 2025-07-26 04:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4ac072a-761f-372a-979b-a544fc37b93e | -9.14797 | -45.87033 | 2025-07-26 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46dd543c-957b-35ce-a1f8-9bb49cceadd3 | -9.46945 | -40.36971 | 2025-07-26 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 2dea2171-9887-3da0-b304-c2f4cf7d5f51 | -13.70063 | -45.69638 | 2025-07-26 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4768f02-b4a3-3bcb-920c-78e561753b1f | -7.24217 | -44.54806 | 2025-07-26 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 655fba98-03e2-3d61-80e4-ba69fc3430c3 | -13.23855 | -40.59991 | 2025-07-26 04:04:00 | NPP-375D | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 3d961a44-fdaa-3092-a8d5-6bfac9c44ec0 | -13.69715 | -45.67133 | 2025-07-26 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a253ff79-c76b-3092-96e3-9cea5699f636 | -13.11497 | -47.32744 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3fef07b3-25d3-36ed-afb3-c9c66bfc4638 | -7.78448 | -44.53983 | 2025-07-26 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac95755c-b8ba-357b-a8bb-8fe86161752c | -13.72501 | -45.69117 | 2025-07-26 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 79e47430-56a7-3a11-ba95-0265501bfbac | -14.3062 | -43.79144 | 2025-07-26 04:04:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 897d4d0a-9bc6-3781-a7a5-e4a14cd413b5 | -10.6207 | -44.76567 | 2025-07-26 04:04:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d39f3ed8-61e7-3422-abf0-d7cde37c75f5 | -9.14386 | -45.86957 | 2025-07-26 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b077f976-7367-38e9-a707-edaf2f229952 | -7.97179 | -49.69256 | 2025-07-26 04:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05c9375f-1de3-358a-b45f-1a74b4c5cdc1 | -9.01865 | -45.35322 | 2025-07-26 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c461642-51e7-35bc-8d39-0c8b4e4a9b8a | -10.62147 | -44.76106 | 2025-07-26 04:04:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cbd6dc45-9c44-325c-858c-d0eac2d2670a | -8.33316 | -38.08795 | 2025-07-26 04:04:00 | NPP-375D | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 40955cfc-c1ec-3e17-b0b7-835e23c9a811 | -13.1052 | -47.3331 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fe406b7-d8c4-3c6e-93bd-9f81d746bc3d | -7.45802 | -49.39748 | 2025-07-26 04:04:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 23ded934-cdbb-3ae9-a57c-0730581c9811 | -9.47886 | -40.37479 | 2025-07-26 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 75b2fba3-e278-3a66-9bee-f45e2b8f0e50 | -9.60121 | -40.56232 | 2025-07-26 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| aca946d8-50bc-33d5-a56c-881a43e621b3 | -13.11012 | -47.33011 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README11.md)
