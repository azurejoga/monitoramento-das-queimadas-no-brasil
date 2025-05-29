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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9f9e803-ad95-3022-9ab5-e1a5374b0d68 | -10.53083 | -47.58411 | 2025-05-29 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd544b1f-35a4-3039-b629-4bdbd640299a | -10.64367 | -48.8036 | 2025-05-29 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b30bc479-9994-34e0-ba00-cf91cfcc458c | -12.36096 | -53.28681 | 2025-05-29 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34fb37d1-180b-3ea9-b659-921362ce02a9 | -17.32589 | -43.61263 | 2025-05-29 04:14:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82788aac-3f53-3e2f-acbe-0def64d8ba9c | -11.78465 | -54.7769 | 2025-05-29 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7469e76c-32cf-3d79-8814-fea6bb2fd416 | -10.73588 | -49.28967 | 2025-05-29 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 52856a0c-41e6-3c67-9d20-69be67e56e48 | -14.21345 | -47.71567 | 2025-05-29 04:14:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 092f53eb-d3a1-3212-acee-49a226dba389 | -15.07822 | -43.3733 | 2025-05-29 04:14:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f042e8fb-9a6f-3e56-b9be-c43c9c6042a0 | -11.7994 | -44.26683 | 2025-05-29 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d576ea1-e194-3465-acbc-9e34114b1f86 | -11.9707 | -52.45767 | 2025-05-29 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9f229af6-4990-33fb-a925-3af67084b903 | -10.65274 | -44.49432 | 2025-05-29 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fba40f6c-2a12-38ad-bc74-034ce7846030 | -15.80435 | -43.57015 | 2025-05-29 04:14:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10823d83-1cc9-3507-bfbb-915d795a2212 | -14.67653 | -45.39996 | 2025-05-29 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7cfe1028-0749-3f86-9c37-9ab6a3bea29e | -10.66612 | -44.41021 | 2025-05-29 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c3731f0-df94-3eb0-a30f-f024fafd0498 | -12.36126 | -53.24651 | 2025-05-29 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df38a740-a960-3060-a5bd-9a2219aa3a5f | -10.9591 | -48.15654 | 2025-05-29 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 32db7877-53cc-33e0-9ce3-2554df84f1cc | -10.64455 | -48.79844 | 2025-05-29 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7ee1e3aa-5262-3a3b-9ef3-576d8a33e259 | -8.75182 | -49.77129 | 2025-05-29 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5781399a-1f30-3104-8656-970323a13c8a | -12.30479 | -47.26818 | 2025-05-29 04:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4e917360-fbad-3589-ab16-cdd4880d7124 | -14.68093 | -45.09394 | 2025-05-29 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ce74955-4fab-3efc-b479-b5b8784794ff | -9.20044 | -49.47258 | 2025-05-29 04:14:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 596f5e06-6ac3-36f3-916f-63dab57beaa0 | -11.81651 | -44.26601 | 2025-05-29 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 80db5ebd-7fb7-35cc-812b-f90a4b3988e3 | -10.47013 | -47.94749 | 2025-05-29 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc77f06e-5bde-3849-9f8a-c7c706ec0f0a | -11.97458 | -52.4642 | 2025-05-29 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5f27e291-6690-37ab-a354-ebd76df26367 | -14.67818 | -45.08983 | 2025-05-29 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d1a267c-9a3b-33cb-b2cd-571de2010de4 | -11.1337 | -53.91169 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3f4e674-a363-3c60-8368-3814093cd98d | -11.92056 | -44.55335 | 2025-05-29 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f4582596-f369-33e5-9d3a-69faf1432111 | -11.13896 | -53.94287 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 048a3a69-dd5f-3b00-aea4-df6daddb18dd | -10.83419 | -54.04763 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9efe7805-4f94-3025-b1d3-ab7372af5875 | -13.08252 | -45.27724 | 2025-05-29 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc61f158-5232-33f8-95c3-9d87ecda6028 | -11.90575 | -54.41557 | 2025-05-29 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b2e4954-9e3e-3a95-947b-bd7cbbe27bc6 | -14.20922 | -47.7192 | 2025-05-29 04:14:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ceb0714b-a592-3f68-a62b-5cc07aa76867 | -12.38528 | -49.9675 | 2025-05-29 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e688297-c968-38bf-b1b2-3f5e306d1db3 | -15.25589 | -46.61124 | 2025-05-29 04:14:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e3429af9-abf4-34f0-8228-67c75ea3eece | -12.32548 | -49.99194 | 2025-05-29 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c44cc8f-9533-359c-baab-4ab25b51c946 | -14.61723 | -47.9403 | 2025-05-29 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4201804-1ad6-37a3-8623-c2291d937655 | -16.83162 | -47.65336 | 2025-05-29 04:14:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10810730-7f8b-3f6c-94ff-19d61f366907 | -11.91222 | -54.42063 | 2025-05-29 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4376bf73-b822-36aa-b722-d608d8cdcc06 | -14.6771 | -45.3964 | 2025-05-29 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4eec461a-e52c-3a28-be36-48d1084852c9 | -14.20853 | -47.72334 | 2025-05-29 04:14:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83b601fe-c23f-3097-9d1e-4189b0d1c6b6 | -11.90949 | -54.40469 | 2025-05-29 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63f3db88-4072-317c-9d05-6ca7949e26aa | -11.20739 | -47.83911 | 2025-05-29 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f88a62d-f284-39b9-b82e-8295c0343c03 | -11.89314 | -47.4475 | 2025-05-29 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b7e087c-bf46-3c3a-8ac4-74facc154ab5 | -10.81833 | -54.04037 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30ffd800-620e-33fd-9e46-8946dbc0804b | -15.47735 | -41.89692 | 2025-05-29 04:14:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0a8e6a45-cc67-3766-930d-74cbbf229e0a | -10.81498 | -54.02803 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1f391e0-973a-314c-be6b-ae085bbcd57a | -11.28732 | -46.43684 | 2025-05-29 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 91291a5f-ebc5-3eea-917d-1644822377ff | -12.27803 | -49.53379 | 2025-05-29 04:14:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d70d6f22-7db7-3abb-be73-fd1a591d0a36 | -10.4626 | -48.12881 | 2025-05-29 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bdfe48bb-3922-3534-8363-dc5c71dc237e | -10.83083 | -54.03521 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| baa39fac-b1e6-3d00-b32d-855226e5849c | -14.21138 | -47.72806 | 2025-05-29 04:14:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5bffd3c9-4161-37e5-8ccd-4cbbf71d4542 | -10.8253 | -54.03405 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffb88017-541c-370d-abf1-414a5717909d | -11.91293 | -54.41691 | 2025-05-29 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0594e166-1005-389b-9fe2-72ec2be422bb | -10.67661 | -44.40833 | 2025-05-29 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 41ce4f92-bd80-3727-9786-6fd6474d042b | -10.73524 | -49.29337 | 2025-05-29 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| abae0f43-1099-3551-801f-a3d25fd7769e | -11.56965 | -47.62678 | 2025-05-29 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7b5faa0-3f24-323d-be0e-d044aab003f0 | -10.81764 | -54.04398 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdd72b33-c64e-3dab-9f04-6b35a4fd76e7 | -10.82387 | -54.0415 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| adb7927f-85dc-3baa-9235-bc68184f4467 | -11.13918 | -53.91269 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5dcee49-0674-36cf-9995-73696dfaaec5 | -10.42138 | -46.82161 | 2025-05-29 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf4f854f-a244-34e2-afd3-c01f5fe5a486 | -11.90088 | -54.79614 | 2025-05-29 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d605f51f-c7b9-3d15-80d6-e3c916b6f961 | -9.75385 | -48.23652 | 2025-05-29 04:14:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a5bd9a46-6d0f-30ef-ab49-94b5f726adc3 | -13.08139 | -45.28435 | 2025-05-29 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 529b6d57-a343-3b45-bb84-dbdebc6d1c08 | -11.5746 | -47.44385 | 2025-05-29 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c7a2cf84-84c9-3f57-97bd-207b69056988 | -9.29631 | -50.43338 | 2025-05-29 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30918967-902c-39b2-9c9b-91125e583ec3 | -12.94514 | -46.53802 | 2025-05-29 04:14:00 | NOAA-20 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 98c241e9-e273-37f1-a467-3317536710c0 | -14.66551 | -45.08406 | 2025-05-29 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c995e2f5-5084-3f31-9863-6bceb56606bb | -11.28163 | -46.43732 | 2025-05-29 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 64886304-fc84-35f2-a432-63f740b3d89d | -10.72129 | -49.54291 | 2025-05-29 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0a75d570-c4cd-3988-a9aa-0c4dfde36b6d | -11.88955 | -47.44688 | 2025-05-29 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 692e316d-670a-394b-9ed1-20b30f68e6ad | -11.13778 | -53.91984 | 2025-05-29 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0db83484-d9a1-307a-9b40-b65f7645b6a1 | -11.9756 | -52.45857 | 2025-05-29 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ef375567-6e42-3fff-92df-1f8ed556196c | -12.10221 | -51.04892 | 2025-05-29 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e3fa1ac-23fc-30af-97a1-dc3a5ffcb403 | -11.90878 | -54.40839 | 2025-05-29 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5828243-ef57-3ad7-bcdc-35628480bf01 | -12.10666 | -51.04978 | 2025-05-29 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c6e37735-625d-3cf8-baaa-423b388d4079 | -11.66576 | -48.73897 | 2025-05-29 04:14:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7e80a01-0d1d-368f-b625-48d8c6d0d53c | -11.90648 | -54.41189 | 2025-05-29 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9550ab3b-fa28-3e97-8ba5-47ae0f40598c | -12.42229 | -53.32853 | 2025-05-29 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f82a885-61f6-3d62-b619-51710cd30829 | -13.08082 | -45.28791 | 2025-05-29 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b313f0b-3b6a-37c3-b532-10cf7df71aea | -14.11994 | -44.79742 | 2025-05-29 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0739f0d8-a226-31bc-9d31-288981ea5cef | -13.65629 | -45.4268 | 2025-05-29 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb3a84fc-f911-3fc0-ac76-6c5664787b48 | -14.21561 | -47.72458 | 2025-05-29 04:14:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d85fdbb7-d1af-3ce4-9991-f9fc2ad42817 | -17.09465 | -43.80429 | 2025-05-29 04:14:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a39d23e-d236-3f60-b317-86eed7f14a02 | -11.91616 | -51.09503 | 2025-05-29 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2ef3c70-43d3-3de0-849c-173de9002699 | -13.68587 | -47.6846 | 2025-05-29 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbe234fe-caf3-380d-ac2e-d9eeeaf1eda9 | -13.08195 | -45.28079 | 2025-05-29 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3188794d-9aa5-3401-8686-ccffcc104341 | -11.90321 | -54.40732 | 2025-05-29 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3292c5bc-98f1-3249-ad8a-f724360dd648 | -14.66881 | -45.08462 | 2025-05-29 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b6118ad-f817-3e2f-ba4a-53c7aa162c8d | -20.3102 | -45.58388 | 2025-05-29 04:17:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb955945-bd9a-3ec2-97ec-74622dc76511 | -18.18055 | -42.63409 | 2025-05-29 04:17:00 | NOAA-20 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 946fed2a-0f98-3f24-a466-c19d6866e1c3 | -18.23973 | -45.62981 | 2025-05-29 04:17:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb8fda46-6c1d-308b-9039-6b4ede1beb5d | -19.43802 | -44.34082 | 2025-05-29 04:17:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b52f8e18-5729-349b-b203-221db0431efe | -21.18097 | -43.98074 | 2025-05-29 04:17:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| aeaacb71-6419-3d89-bc64-7c355e98c445 | -19.49306 | -44.27469 | 2025-05-29 04:17:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6cb3ccdb-9703-3bc4-972b-a51da6badc59 | -18.38011 | -44.51611 | 2025-05-29 04:17:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b993361-7d62-3a49-b24e-e0865a702937 | -18.23698 | -45.62563 | 2025-05-29 04:17:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96136221-b19a-35d5-9fa1-03eba5b96f4b | -28.58349 | -49.44139 | 2025-05-29 04:17:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| eadc7abf-5f11-3ae8-a4c9-d51ad022ec5b | -18.17995 | -42.63842 | 2025-05-29 04:17:00 | NOAA-20 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8643d85b-179c-3859-9884-731e7f5dbc8b | -21.59365 | -44.29446 | 2025-05-29 04:17:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d3ba3c11-c546-3ebf-8df2-8060b0655f58 | -20.90854 | -44.22263 | 2025-05-29 04:17:00 | NOAA-20 | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |


[Clique aqui para ver as próximas entradas](README13.md)
