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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17e4762e-be00-3072-b65d-a6b820e94009 | -12.40002 | -48.48084 | 2026-09-18 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 978afedb-5fbe-3ad8-b374-cb0d74409edd | -11.37781 | -43.93375 | 2026-09-18 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c669c22e-29a7-313a-85e3-96a6d1b4efdc | -8.29754 | -45.63301 | 2026-09-18 04:21:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2019f85-241a-3863-b7ff-352b44229408 | -9.24334 | -45.91318 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0ab13fc1-c2ee-399d-8877-591c7a6e21ee | -10.99912 | -57.06216 | 2026-09-18 04:21:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f6e229c-76ea-38eb-8148-94dd597f2c8b | -11.52209 | -46.86621 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0db21f51-3d76-30a3-910b-731a122c81a6 | -9.91297 | -46.56394 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8004dae5-e6a2-3b79-b584-604b7770badb | -13.7014 | -43.61891 | 2026-09-18 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f24ed622-42a4-3b5c-af99-fac767153cba | -13.26353 | -46.91255 | 2026-09-18 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5ff77970-86ba-3dc2-ac73-6e8ef6d9aeb3 | -14.94622 | -49.91627 | 2026-09-18 04:21:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76c9cff8-1c49-390e-a657-b3dfaf99fa0c | -8.68598 | -45.43196 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a76e48f-1223-3c8b-a1a1-836babac75b6 | -8.54396 | -44.54993 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 26dd103f-f9ef-3e14-99ec-b4f851136e24 | -9.60646 | -45.3511 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 258847f9-2ac3-3793-8c6c-eb99652eddf1 | -9.91411 | -46.55682 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e26c931-f7e1-3f08-8a98-8a777b4b7555 | -10.11867 | -45.64701 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 50f773b7-f7ed-3371-9055-1d6606067698 | -8.45548 | -45.84049 | 2026-09-18 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e7d54b8-94be-3c55-8cad-f170b32ca0e1 | -11.13269 | -49.04375 | 2026-09-18 04:21:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 3d84a655-08c1-3353-b9ec-3c8a2897a076 | -8.4877 | -44.56274 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 556b5dd7-5f90-31da-a4e9-b5855bece0fd | -10.1571 | -45.39952 | 2026-09-18 04:21:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| acbe3f35-0b13-30b9-8f63-1afb115f8a61 | -9.5611 | -45.46861 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| edfb7919-5bb8-3ce5-af68-15198b55ceae | -9.71577 | -47.09475 | 2026-09-18 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 990b16fa-bbdc-3dc4-b654-499d7f886200 | -10.79714 | -46.65358 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4adebcf-882b-3291-95e3-8a0aa22a8f98 | -9.94118 | -46.60126 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d244cb6e-6256-3e26-b7f8-64a4246d4156 | -13.27402 | -46.91064 | 2026-09-18 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d403bbf9-e0d0-3cb6-81b3-e5e99c30a0f5 | -12.40079 | -50.69652 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25a2b733-0062-3d14-b25a-f229fa15f0d4 | -11.5226 | -46.88445 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2fe664d-c241-3ce1-9200-f88d232f6bdb | -12.57537 | -47.09033 | 2026-09-18 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f82714b4-4f7a-3ca7-a875-c951f666f9ae | -12.17756 | -46.98122 | 2026-09-18 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e376fd8-1d16-324b-9172-a1d77dc228f1 | -13.25029 | -46.91037 | 2026-09-18 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 430cb33b-56ff-398f-8692-01a2003c9c56 | -12.38213 | -48.14103 | 2026-09-18 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ed1dc40c-2938-30f6-a0fd-8036732e0b6c | -9.61752 | -46.75009 | 2026-09-18 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 424407dd-414f-31fe-8517-e7183890e49e | -9.76378 | -45.0611 | 2026-09-18 04:21:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 177e8f6d-ce1a-30e3-8b1a-009f07bf9a8f | -11.8751 | -47.58937 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3775104-fbc5-36f9-a8a2-479e388d0648 | -11.8763 | -47.58205 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a04b499-f1e7-3085-aadb-3b65a4fdfc8d | -9.18537 | -46.7493 | 2026-09-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| effeb03c-80ea-3f63-a51c-c17bed2840cd | -8.68489 | -45.43891 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6c3bcb7e-7a2f-3fc4-abc1-d2bdb4eb7a19 | -8.46597 | -44.52719 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a44240f8-0ce3-331b-8ebf-f810be16bd4f | -9.19207 | -46.75039 | 2026-09-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e30b7160-04aa-3c09-9a8e-9e7feb617426 | -13.74516 | -48.7907 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2f878c11-85b3-3421-9134-e9691f42d77b | -14.80156 | -48.56451 | 2026-09-18 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8efaaca-ce58-3fe3-9c84-316dfe5639fc | -9.91354 | -46.56038 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c51b8e24-525f-31ac-b1ca-ec33c3b50b97 | -9.9462 | -45.31222 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7da5ab7e-443f-3e30-bd6f-c153460f9d40 | -11.32453 | -43.3556 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 005f70de-4200-36e4-84cf-0becf4e50a31 | -8.88302 | -45.89094 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a3b8cfb9-2bd9-3b8a-9d36-2af176623db8 | -14.94547 | -49.92073 | 2026-09-18 04:21:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c2031fc-8002-32eb-ada5-e4d50c9867c0 | -8.42968 | -45.72168 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39999740-d735-37ce-987d-6ce93dbf4b5d | -10.11701 | -45.56762 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dbcb30dd-5afa-36dd-a403-7577cf754d8f | -11.29933 | -43.38026 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf764fec-11ed-3973-9999-81d7dfd3e606 | -14.19453 | -42.16454 | 2026-09-18 04:21:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2a930d8d-c6f0-3302-a786-2b6dea3315fa | -8.47734 | -46.88381 | 2026-09-18 04:21:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3f6805b1-52b8-3836-a706-ef507ba5c6bf | -10.64365 | -50.23894 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 071c3be6-412e-36ca-ab9e-2d98222ec5ff | -12.62848 | -50.89488 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 065881e4-0583-3d66-862d-0ba32294c18d | -11.89175 | -47.61468 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9cb29fd-3228-37ec-8692-faf87eba061d | -15.86381 | -38.93595 | 2026-09-18 04:21:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 76e3fa4f-edf0-372e-9b09-c174a3060337 | -13.35414 | -48.47317 | 2026-09-18 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ff73696-9e8a-34b1-86fd-7bcbe28d564d | -10.10841 | -45.64471 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d44be67a-e157-3262-bdcb-457274b5f6ff | -10.80266 | -46.66175 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1cbf81d6-bc48-3c81-bbf7-da4b716f9fa7 | -10.78669 | -46.17933 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ae9576a-ed86-3425-905c-45ea567e2237 | -9.18595 | -46.7457 | 2026-09-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d19ec7d8-7231-3dfa-bbe5-9f36a3d67669 | -10.78723 | -46.17583 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 119696e2-061d-389b-ba8d-cf15f4a544e8 | -13.3453 | -43.78492 | 2026-09-18 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 378f0a7f-121f-3f06-8e24-13dac4f77f68 | -10.85189 | -50.88671 | 2026-09-18 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f0dd25b-51dd-3e3c-b780-b63a06045e11 | -8.80939 | -46.93708 | 2026-09-18 04:21:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d20ad642-4ecc-348c-9500-201352f268cf | -10.1166 | -46.28687 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d18aecc8-b9e0-39b0-b210-590084771d58 | -9.70583 | -54.81877 | 2026-09-18 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d525be2a-704a-3aa8-af84-6cb2cd887214 | -14.80343 | -48.55315 | 2026-09-18 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03eddef7-76b6-3037-81bc-904d81540f66 | -9.40248 | -48.94474 | 2026-09-18 04:21:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e020035e-5371-3fc0-89f0-2bd14f8c159e | -14.93329 | -49.92747 | 2026-09-18 04:21:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f607eb93-dbc3-3ebe-85d4-06d8aa3da95e | -12.36995 | -50.69106 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6bb94d86-c3d3-3d2c-8ef5-1f39581b7f45 | -9.865 | -48.62965 | 2026-09-18 04:21:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3395cffe-9ec6-398e-a45a-97e2617a4251 | -9.19091 | -46.75757 | 2026-09-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d14a7873-0013-3aa2-8cd2-79eb2eebdfb1 | -10.83297 | -44.96199 | 2026-09-18 04:21:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba647c2a-4205-3b00-adf9-37ca1b1bdcf4 | -12.36116 | -47.68455 | 2026-09-18 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 139a4a62-80a9-3696-833c-38d071127b94 | -8.46781 | -46.87846 | 2026-09-18 04:21:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 99ac5557-73cd-32b7-8b40-76a86eefdc59 | -10.308 | -46.88351 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a98d32c5-5c5c-3eb3-b6cb-7c1e17a81b34 | -11.27888 | -43.37312 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5b1f2a0d-d37c-3e47-93ad-14fbfd2e95b8 | -12.17645 | -46.98825 | 2026-09-18 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0e84fba7-5b61-3895-9a65-43fbb592d1d9 | -10.48668 | -46.31433 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6bc6ac13-2436-343c-ac0d-e950d8d82e69 | -11.77266 | -47.4303 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b738b0f-1bed-3bbc-9759-2ec40f459345 | -10.51647 | -46.27602 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a5cc35c-717a-3878-8fc8-383b18291c5f | -11.55847 | -46.89373 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 566d8ffb-2b0b-3b64-b4e7-8ad82cb1f811 | -12.39096 | -48.47132 | 2026-09-18 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5596c690-82e8-3c73-84b8-e7be2c8b4a9b | -14.94189 | -49.92013 | 2026-09-18 04:21:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| adb2a0ec-eb05-36d8-9338-87ff79371eea | -9.75948 | -46.09295 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e793356c-3cb1-391b-b412-03d5c8f1084b | -12.2906 | -47.3599 | 2026-09-18 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a873cc4-d45b-3d65-bc6c-913212cd8292 | -12.30968 | -47.95996 | 2026-09-18 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fc15111b-d056-34d7-82de-27fd8a240664 | -12.29394 | -47.36046 | 2026-09-18 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d650ac9a-b349-3bdd-8a1f-c39f9f6aaeaf | -9.59541 | -45.33511 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 070e9fef-c20c-3761-b0b8-39aa3e8b4f4b | -9.59487 | -45.33859 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ceb2d920-d4e4-3b3d-b589-edfff9eae9d0 | -9.93301 | -46.52359 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7664be63-7a43-37f6-aa5d-b7d09dbfeac1 | -8.46651 | -44.52368 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13594c2e-4a78-3972-a430-2c7f2ff55157 | -9.95601 | -45.46733 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 186bf4f3-3a52-367f-ba55-826c39f4e8e9 | -11.05939 | -48.30094 | 2026-09-18 04:21:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67f9a7dc-be0b-360c-8afb-6c0dc7fba84d | -13.43044 | -51.89961 | 2026-09-18 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fde28a0c-13a1-31c8-b254-2d34853b3373 | -12.99935 | -46.9273 | 2026-09-18 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c55dc0e4-7f7d-3330-869b-b82d9fc99592 | -13.55528 | -43.50692 | 2026-09-18 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6bffa3c-887c-331d-b8a0-41491f4ef53c | -13.5977 | -48.29301 | 2026-09-18 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9d107eb9-d925-379e-9dad-19c6824ae63e | -14.13849 | -48.72652 | 2026-09-18 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1e601e0-f2bf-32d4-947a-3bf22513afc6 | -11.22058 | -43.42892 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 327cb39e-6697-3189-8079-b08186287ce2 | -9.70462 | -54.82539 | 2026-09-18 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |


[Clique aqui para ver as próximas entradas](README47.md)
