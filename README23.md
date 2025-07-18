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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e883bbe9-1b9f-3acd-b358-4d7813ed6d96 | -11.99844 | -45.3102 | 2025-07-18 04:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 03359073-1319-3ef2-aa8a-cf7731e93bda | -11.56945 | -47.07527 | 2025-07-18 04:53:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b8b56d71-0bba-36b4-ba94-088a4f373cab | -8.0531 | -50.11402 | 2025-07-18 04:53:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 113aa711-f0c3-3dda-a943-aa4cd4645a95 | -11.16126 | -46.25062 | 2025-07-18 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4407f141-32ee-365c-9df1-86c85577c67f | -6.94751 | -44.55765 | 2025-07-18 04:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a1216635-544a-3941-9d48-0756c910e543 | -8.08241 | -43.15306 | 2025-07-18 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 1d3b201c-b343-3500-a83f-2f077a0e2152 | -9.01829 | -61.22185 | 2025-07-18 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e3953c3-17e2-3385-a463-07c46a145622 | -7.48577 | -63.8184 | 2025-07-18 04:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b4731b4-146d-3b37-b832-b05ba7aa906f | -7.35516 | -44.19457 | 2025-07-18 04:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 84640e6c-da32-3ff2-9a24-a669827a9e3a | -11.32439 | -55.21118 | 2025-07-18 04:53:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d57a1d6c-f42c-3042-8c5a-136403298675 | -8.53787 | -47.84578 | 2025-07-18 04:53:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f73f3f25-f4dd-3480-b731-e7728a993cb6 | -8.88422 | -44.78997 | 2025-07-18 04:53:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bb545a09-6cb3-3b27-a86d-8b7ad7394911 | -7.34439 | -44.19615 | 2025-07-18 04:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b5fff778-28e5-375c-a2c4-f250700a54fa | -10.71751 | -49.48507 | 2025-07-18 04:53:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 00ecf020-e57d-310e-848f-e367213d9c12 | -6.619 | -47.19632 | 2025-07-18 04:53:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ce137e5-f1b7-32d5-a24d-c61a837f986e | -8.87776 | -50.15308 | 2025-07-18 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 00513cf0-c421-3560-8c9e-60a4b5dd1af4 | -9.43066 | -61.9953 | 2025-07-18 04:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 626f354d-6296-3838-b4eb-dc541956f0a8 | -8.92087 | -49.8327 | 2025-07-18 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a256b3b-7880-3030-8114-2985d947f8b7 | -9.50312 | -47.56484 | 2025-07-18 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 33e1f9d9-a8e4-3334-95ec-862cf7c864ab | -8.8669 | -49.03634 | 2025-07-18 04:53:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ce44938-4ca4-397f-b1b8-11b7c71332eb | -11.74284 | -48.19215 | 2025-07-18 04:53:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d419c0d1-fe86-3e77-995d-1baf3d3b372b | -9.04913 | -49.29116 | 2025-07-18 04:53:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 721ea953-646a-3ad2-a62b-bc7a1980a6c2 | -8.03886 | -46.61996 | 2025-07-18 04:53:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 86b7be51-9bef-3154-bc30-558dfd76143e | -6.97714 | -43.73525 | 2025-07-18 04:53:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c039ff6a-2f4b-3094-aaeb-f05c947f372b | -12.70579 | -46.80753 | 2025-07-18 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 974ac741-9401-3545-a7dc-1d3d4cb51c5c | -7.22476 | -44.13973 | 2025-07-18 04:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba4042e8-d2e2-31e6-8f7a-cc7ad8a4ea50 | -12.47736 | -44.49928 | 2025-07-18 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5ba55f6-17cc-333f-ab89-2bdc77e326ff | -6.98762 | -43.92793 | 2025-07-18 04:53:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc0c2664-7af9-3e11-826a-6ada7a8ec199 | -12.48269 | -46.91673 | 2025-07-18 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b8767913-9396-3f2b-8b60-29da177a38c1 | -8.91962 | -49.84129 | 2025-07-18 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e216faa-2761-39b9-a93f-af6ac0f6f03f | -11.85284 | -46.75547 | 2025-07-18 04:53:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22940f7a-7f5b-37e1-80d5-1f53e7f92394 | -7.61421 | -45.54851 | 2025-07-18 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7fcd6af8-4ed6-3503-b6ac-af91fdeee712 | -11.16605 | -46.25087 | 2025-07-18 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d719028e-b3e8-3556-a799-26e7af29d971 | -8.88381 | -44.79288 | 2025-07-18 04:53:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| db816273-449e-3d7f-abd6-72a5f423a869 | -8.06148 | -50.08248 | 2025-07-18 04:53:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b649932-e6bd-314e-a02b-676289be0b18 | -6.49706 | -47.23289 | 2025-07-18 04:53:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0c36f0b-a4e8-370a-9171-ec45be5c2576 | -9.2753 | -49.63303 | 2025-07-18 04:53:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5c7370a-8a90-3981-95b6-b116468cc38b | -11.99332 | -45.30953 | 2025-07-18 04:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c530d02-5eb4-3641-973f-c46515cdcf11 | -7.94133 | -43.85972 | 2025-07-18 04:53:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f8ad0a18-b1d7-3fbc-9582-b89a687f858a | -9.15754 | -49.67143 | 2025-07-18 04:53:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a230e4a9-0453-32b8-8ec3-0fe425949c8e | -11.56254 | -47.09312 | 2025-07-18 04:53:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1838d046-d93e-34f0-9203-06bd0fd93105 | -8.88135 | -50.15361 | 2025-07-18 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 92a552ab-12d4-3912-aff0-77ef6e0ed881 | -7.10761 | -43.64581 | 2025-07-18 04:53:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d32d340-fa6b-305e-addc-6d32cecfb841 | -10.0641 | -46.67247 | 2025-07-18 04:53:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d7d99ca-2c39-3be2-a577-96582df17dce | -10.61706 | -48.07484 | 2025-07-18 04:53:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2159fa6b-8997-329a-b2f0-f98e4451e0d8 | -12.66439 | -47.09255 | 2025-07-18 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b5974e65-419c-3780-a362-c32e22f118b0 | -9.50735 | -47.56549 | 2025-07-18 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b40a6c0d-8fec-3110-801b-7106e9f338b7 | -11.56704 | -47.09375 | 2025-07-18 04:53:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f325fbdc-60c3-3554-9391-ac639adfffe2 | -10.08773 | -47.247 | 2025-07-18 04:53:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97740a54-86b0-38d6-b469-add736ed50cf | -9.76125 | -48.75327 | 2025-07-18 04:53:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0249da19-ba3d-36ed-8658-596d96af4362 | -7.6151 | -45.55161 | 2025-07-18 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 359a1716-d9ed-389c-98a7-d68f4770f54b | -9.38965 | -48.39806 | 2025-07-18 04:53:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1cab324f-9dc3-3fb2-bb7b-3dc669f2a5c9 | -11.32821 | -51.44014 | 2025-07-18 04:53:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b3ee175-2d81-3e1a-9f9a-c8f6a073c52a | -7.10809 | -43.64242 | 2025-07-18 04:53:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c5154af-a4ad-3a8e-b7ad-f935b5600deb | -8.10583 | -43.14876 | 2025-07-18 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3c26cf02-f050-3cc3-aa75-32aa7e6b40bd | -9.2764 | -49.63552 | 2025-07-18 04:53:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 188b3c0f-52d1-37fa-83bd-125ec7fdae94 | -8.07682 | -43.15219 | 2025-07-18 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 48cfae83-b73c-39cf-bb70-6c55032a0cfe | -8.91958 | -49.84234 | 2025-07-18 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5a28295-c3f8-3f8e-b932-02519dc6f7ae | -9.80086 | -47.73749 | 2025-07-18 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2886458e-04af-309f-b341-8148c2aac27d | -9.76517 | -48.75395 | 2025-07-18 04:53:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a2131a5b-8838-33cd-820d-f3f5280a409b | -11.56354 | -47.07715 | 2025-07-18 04:53:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ad85d72a-90a3-3ba3-909d-be8c4bd49d9f | -6.95802 | -43.75597 | 2025-07-18 04:53:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 85695b2e-45f7-366f-bc9b-d44d31d966c3 | -12.47807 | -46.91608 | 2025-07-18 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 177b9336-affd-3fe1-8677-a1a4cb67625c | -6.77382 | -45.51253 | 2025-07-18 04:53:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 1074bb89-c994-3c2e-9a0b-1ed9548426fa | -11.78141 | -45.22037 | 2025-07-18 04:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7fc302f-511a-32d8-a59e-7c832dcc5e08 | -8.64666 | -47.75214 | 2025-07-18 04:53:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f42157ff-4ac5-3c51-8175-5379f0438ec0 | -6.98739 | -43.92784 | 2025-07-18 04:53:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b480ee8-d8d9-39cf-901a-55a190712c2d | -8.88699 | -44.79059 | 2025-07-18 04:53:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 21d19622-6fd8-3f42-953d-c141bbe3de7b | -7.635 | -56.72978 | 2025-07-18 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea490b2b-ce4f-32b6-9d1f-d94ae28ac4bf | -7.60506 | -46.31737 | 2025-07-18 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6ddb130-fc0a-3298-9362-64366bc49312 | -8.88661 | -44.7935 | 2025-07-18 04:53:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| de459b12-524a-3cb8-9bfd-2044b98c0ec0 | -10.81673 | -49.28535 | 2025-07-18 04:53:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0ee103d1-1622-33fb-962e-48137982e1b9 | -10.90011 | -49.20559 | 2025-07-18 04:53:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f945ed2-3002-3375-8d0d-4acd60f6887f | -11.74339 | -48.18823 | 2025-07-18 04:53:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 912c6c37-fafb-39bb-b0fa-859e90dcc1e3 | -8.88888 | -44.79362 | 2025-07-18 04:53:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f82a9d2c-f9b9-36f4-b7e6-a7786695c18f | -11.78101 | -45.22343 | 2025-07-18 04:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6d05ab0-0323-33b7-9715-6e91d1b1e377 | -9.76909 | -48.75462 | 2025-07-18 04:53:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 24abbc3f-d439-3985-9f8a-84e81152578b | -12.03403 | -48.76154 | 2025-07-18 04:53:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46b1e212-01ba-3564-a082-5918d6a30ebc | -12.48207 | -46.92157 | 2025-07-18 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92dedb60-9ec5-323c-9f1d-a07be114a1e1 | -9.5079 | -47.56153 | 2025-07-18 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb1be492-2bca-33a7-9880-cc02c532c52f | -6.98171 | -43.93019 | 2025-07-18 04:53:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8eddfc5d-93a6-3eb5-952b-88a13a39bc3f | -9.27093 | -49.6369 | 2025-07-18 04:53:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9626ed6-6ecf-39b6-9100-15d6e938ac9b | -7.60879 | -45.55268 | 2025-07-18 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e69ccdb1-567c-349a-9ab8-2a7b5eb3392f | -10.05325 | -59.10218 | 2025-07-18 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81173edb-5b62-3701-b062-939af3e602f7 | -7.22037 | -44.13329 | 2025-07-18 04:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25b78bb7-562b-3d94-b232-c587867c2dcc | -6.99183 | -45.62029 | 2025-07-18 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42517970-f50b-3f82-8c5b-a147b09747fc | -9.43123 | -61.99224 | 2025-07-18 04:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db2c5de1-ba02-365d-bb51-875902c597bc | -7.39571 | -43.79174 | 2025-07-18 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90d77cc8-ce54-3d2b-8d39-8f1a7fae1394 | -11.56869 | -47.07314 | 2025-07-18 04:53:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ce7bb7e7-427e-32f0-b7a0-5d6c2dce65fc | -10.68065 | -56.54492 | 2025-07-18 04:53:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9981979-55aa-3a1e-bf2b-270595dcc53f | -12.0688 | -47.98142 | 2025-07-18 04:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7af497b9-b334-3ff6-9266-113d11d161d8 | -7.60952 | -45.5476 | 2025-07-18 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d67f850f-4acb-3db9-a390-4d954b0fec6f | -10.67891 | -56.54403 | 2025-07-18 04:53:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dda61a67-0383-38b2-a7b5-d3700ed8d0a1 | -11.85345 | -46.7508 | 2025-07-18 04:53:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c8eed2e-ff1f-391f-8c5b-3bea80c4a6ec | -7.6104 | -45.55072 | 2025-07-18 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04ee7a89-d4bc-35b1-9f78-76cc44c5e3aa | -7.17172 | -43.59451 | 2025-07-18 04:53:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 435615e5-dc3d-3510-b5a6-6552bf1ac76d | -7.1939 | -43.09996 | 2025-07-18 04:53:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7e4789a8-62e2-31f8-b973-3c8150e99e11 | -11.74321 | -48.19501 | 2025-07-18 04:53:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| abdfd600-86db-35e9-bc4e-6493955c1523 | -8.06386 | -50.09098 | 2025-07-18 04:53:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45f77f67-80b3-3393-aa0b-bf2f1583689b | -9.50367 | -47.56089 | 2025-07-18 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README24.md)
