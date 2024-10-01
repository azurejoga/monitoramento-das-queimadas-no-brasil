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

## Dados Diários - Página 164

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31f4643d-0dc9-367d-9734-24f7df2092c6 | -16.898 | -57.7153 | 2024-10-01 12:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.6 |
| 3762ec23-31f3-392b-ab4c-128c7dcb85ba | -16.8787 | -57.6971 | 2024-10-01 12:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 142.5 |
| ad507fd8-342b-381e-a0dd-80ecf9ee2f8a | -16.8983 | -57.6949 | 2024-10-01 12:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.8 |
| 454b9878-ffe4-344c-8128-793fb02dc059 | -16.76 | -57.792 | 2024-10-01 12:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.8 |
| 8b2233d2-ddf9-33b2-b51b-d8626f15bb23 | -17.0895 | -56.7503 | 2024-10-01 12:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.3 |
| ad0fa55d-759b-3486-b178-5577bd146bea | -17.0695 | -56.7733 | 2024-10-01 12:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.7 |
| 2cbe10b0-ad36-3fd2-bada-769e1f293407 | -17.0699 | -56.7527 | 2024-10-01 12:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.0 |
| e8d49536-1ece-3d09-bde8-e83c7c8c5891 | -17.0898 | -56.7297 | 2024-10-01 12:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.6 |
| 7d36f440-d3ba-3d44-bf96-c3907fba058a | -17.7248 | -53.2016 | 2024-10-01 12:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 33fe772d-dcbc-304d-a43c-8ea82c08d6c4 | -17.705 | -53.2046 | 2024-10-01 12:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 8cecb71d-244d-311d-95cb-ac9340316e4c | -18.1127 | -49.0983 | 2024-10-01 12:36:47 | GOES-16 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 6ad921fd-426e-3b3e-91f0-875feb37e22e | -18.6977 | -57.3123 | 2024-10-01 12:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.4 |
| 57962232-3818-32b6-83cd-21e257f33831 | -18.6973 | -57.333 | 2024-10-01 12:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.5 |
| b813d55a-fde4-3cbb-bd8f-cda66b37e1e0 | -18.7176 | -57.3097 | 2024-10-01 12:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.9 |
| ccca515a-473d-39fc-ae50-603b6043ac85 | -18.9096 | -49.1902 | 2024-10-01 12:36:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 289.4 |
| 97199dbc-2083-3d84-9411-cc4462c6983d | -18.7172 | -57.3305 | 2024-10-01 12:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.9 |
| 8fe7f406-c625-3b12-b1d0-2e8b10649fb2 | -18.9091 | -49.2129 | 2024-10-01 12:36:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 132.0 |
| 1afee47a-1e1b-3e31-857f-d7e598e4c5c1 | -20.9147 | -49.13 | 2024-10-01 12:37:02 | GOES-16 | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 128.0 |
| b15fb60a-3f35-3551-afb6-49001069dcb8 | -20.9153 | -49.1069 | 2024-10-01 12:37:02 | GOES-16 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 126.0 |
| d19b2b4c-a7a6-32b3-bf62-f3f487b2272a | -20.9359 | -49.1023 | 2024-10-01 12:37:02 | GOES-16 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 552.1 |
| de599c50-2710-3628-af13-0d6583c85713 | -20.9353 | -49.1254 | 2024-10-01 12:37:02 | GOES-16 | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 592.3 |
| 9b8fbe7b-9abb-38fd-a9ea-ac2dddbe1f2c | -21.3834 | -48.4915 | 2024-10-01 12:37:04 | GOES-16 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 134.0 |
| ff2b5085-db40-3edb-ab0e-005984a94db0 | -21.3841 | -48.4681 | 2024-10-01 12:37:04 | GOES-16 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 119.5 |
| be753b76-3508-3a6f-954f-ae5935e45d46 | -22.3707 | -49.3244 | 2024-10-01 12:37:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 327.6 |
| c49b8a11-2048-3b85-8e24-3920b82be3f5 | -22.3916 | -49.3194 | 2024-10-01 12:37:09 | GOES-16 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 109.3 |
| 5bb4f03f-653e-3a48-8cef-a1ab0bbdf006 | -22.37 | -49.3477 | 2024-10-01 12:37:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 113.1 |
| b10c9427-8af1-3260-9149-8d5dfb5f40f6 | -22.3713 | -49.3011 | 2024-10-01 12:37:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 231.0 |
| c305b50b-52f4-3e99-b368-00d56fc5d245 | -10.6978 | -46.1514 | 2024-10-01 12:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 4464c578-e3e4-3fd5-8665-c88eb68d3e77 | -10.5746 | -48.0178 | 2024-10-01 12:46:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 06066918-eb2e-33ee-b14c-451d8e0af398 | -10.5743 | -48.0399 | 2024-10-01 12:46:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 958cb392-4af7-3b10-9f60-ebfeade0b04e | -10.996 | -46.5418 | 2024-10-01 12:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| dfde2a6b-194a-36ed-abee-3d7dd85dc2a0 | -11.258 | -45.6682 | 2024-10-01 12:46:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| acb0f662-b0af-376b-9c08-10574c7b16dc | -11.158 | -49.6289 | 2024-10-01 12:46:09 | GOES-16 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| c0ce32f8-ca71-3a28-82f2-efc539b7a7e3 | -12.1593 | -50.0717 | 2024-10-01 12:46:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| ba8e12fd-2faa-3471-9a9e-037f62308c4c | -12.1402 | -50.074 | 2024-10-01 12:46:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| c5373759-8420-3e9b-bace-3cfd760b56fe | -12.1406 | -50.0524 | 2024-10-01 12:46:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| dbdd664a-a1dd-3708-89f4-bef38b0151a2 | -12.3934 | -50.9658 | 2024-10-01 12:46:16 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| ce5b0209-bdb1-336b-a0e3-31cf4acb5501 | -12.4125 | -50.9635 | 2024-10-01 12:46:16 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| db6c0a58-18b5-3f72-be0a-e640d0f4ae76 | -12.94 | -51.4327 | 2024-10-01 12:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 2522f7f9-b8d8-352b-b95d-a32fad745087 | -12.9437 | -51.1979 | 2024-10-01 12:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 84a602ec-eef1-3f7b-8ce5-0691c63e2be4 | -12.9995 | -51.2976 | 2024-10-01 12:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| b4a62d41-2753-31b4-b9b9-cf55f1d879c2 | -12.8397 | -62.8607 | 2024-10-01 12:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 90.1 |
| db606bf9-d35c-358e-be87-9a9512350641 | -12.9396 | -51.454 | 2024-10-01 12:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 2985a9f8-bdcd-3e9a-8d90-6b5bbea3e663 | -12.9998 | -51.2763 | 2024-10-01 12:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| a611ab03-e936-3d09-ae17-7c3440f6439a | -12.9803 | -51.3 | 2024-10-01 12:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 02b98b78-abd1-31a8-9f13-a58cff2d0fea | -12.9205 | -51.4563 | 2024-10-01 12:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 3cec85b2-59b3-3b32-9f1a-9f370397d2a0 | -12.9433 | -51.2192 | 2024-10-01 12:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| eb05a642-5348-33d1-8308-628615b2c9a7 | -12.9807 | -51.2786 | 2024-10-01 12:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 52e48f14-7ad0-33c3-90f1-f3580eb0ffa3 | -12.9169 | -62.6829 | 2024-10-01 12:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 109.6 |
| b83e80ff-7cd0-31a5-b958-68ac1dc0723e | -13.2112 | -51.2287 | 2024-10-01 12:46:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| b67be4cb-d34d-3f1a-816f-9a657284a63c | -13.2116 | -51.2073 | 2024-10-01 12:46:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 929fe0a0-1ceb-3570-8ba1-7d995f06974e | -13.5765 | -51.1821 | 2024-10-01 12:46:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 7789884b-76d1-3738-a0b8-3c03776bd9ab | -13.6164 | -51.0913 | 2024-10-01 12:46:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| cb042bd6-ae55-3a7b-801b-73187b2a3716 | -16.0906 | -50.4081 | 2024-10-01 12:46:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 84.8 |
| e8a97790-fd39-33d5-a0a9-1e485295bf2a | -16.4536 | -57.4188 | 2024-10-01 12:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 184.3 |
| e4fe5558-8471-3370-a16f-4499048dc286 | -16.4743 | -57.3349 | 2024-10-01 12:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.5 |
| 713e92cd-1ac5-3ce8-8900-8de5ebf00299 | -16.5131 | -57.3509 | 2024-10-01 12:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.4 |
| 038eef7c-66b8-35de-ae9c-21432dced906 | -16.4539 | -57.3984 | 2024-10-01 12:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.7 |
| 26a5cb31-1481-39cf-8bae-d7bef50ecdc5 | -16.4939 | -57.3327 | 2024-10-01 12:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.6 |
| 37c3b403-0c7e-3cca-9805-684c38bd6594 | -16.474 | -57.3553 | 2024-10-01 12:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.8 |
| 318be447-8ae3-3265-8e31-e141363ae196 | -16.6525 | -55.958 | 2024-10-01 12:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 85.6 |
| 00f2f7c4-551f-32d6-92a3-dab73fdaa558 | -16.7532 | -55.7797 | 2024-10-01 12:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.8 |
| c18251e1-24d4-3cc9-8326-5d47e4a1892d | -16.6263 | -55.1934 | 2024-10-01 12:46:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 77.3 |
| 84f06331-c653-394b-8400-d5393380e0bd | -16.6259 | -55.2142 | 2024-10-01 12:46:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 69.3 |
| 5e4eb5e8-60cd-3484-b481-c8594634605f | -16.7728 | -55.7773 | 2024-10-01 12:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 122.0 |
| deda84d6-3679-320f-9308-a640c9cb2b98 | -16.7528 | -55.8005 | 2024-10-01 12:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 65.6 |
| 7b568b7b-4da9-3d06-99ea-70a4e359cf3d | -16.7724 | -55.798 | 2024-10-01 12:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 80.9 |
| f265a3a6-dc4e-3b4c-9f46-271ba529b5be | -16.8591 | -57.6993 | 2024-10-01 12:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.1 |
| 7fe50b5a-4a69-3a61-b606-87989fef4ac4 | -16.8787 | -57.6971 | 2024-10-01 12:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 139.2 |
| 40a29893-431c-3825-b0c2-6220de2e6c10 | -16.8784 | -57.7175 | 2024-10-01 12:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.2 |
| d90473dd-f1a7-3549-9f5c-236210130b7a | -16.7796 | -57.7898 | 2024-10-01 12:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| a700430d-3962-3c43-9133-3f930337c209 | -16.76 | -57.792 | 2024-10-01 12:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.0 |
| 4f7595ba-f8aa-3cfa-bec8-43175abca507 | -17.1377 | -56.2076 | 2024-10-01 12:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 91.2 |
| 7b7f53cd-97ff-3afb-bd4a-6fbe35a014a8 | -17.0705 | -56.7114 | 2024-10-01 12:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.6 |
| b279aeeb-aab8-3600-8c65-6db2a8defa6d | -17.0895 | -56.7503 | 2024-10-01 12:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 180.3 |
| 319bf543-9efd-3fba-954e-ebab4edd6ee4 | -17.0892 | -56.7709 | 2024-10-01 12:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.9 |
| 06f37aac-76c5-38e5-ad88-f0e80f0a9a27 | -17.1381 | -56.1869 | 2024-10-01 12:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 91.2 |
| d2bd678f-7f5e-3c74-8d3f-b30af5b2daa2 | -17.0502 | -56.7551 | 2024-10-01 12:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.7 |
| d7328b54-9e55-3864-9d13-5ccb9e27665c | -17.0699 | -56.7527 | 2024-10-01 12:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 94760043-2a31-3648-93ef-27c8c36da0ca | -17.0898 | -56.7297 | 2024-10-01 12:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.7 |
| ec0e3933-3807-351e-92d6-2dd18bb6ba40 | -17.1964 | -56.2209 | 2024-10-01 12:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 121.4 |
| bc34ba5c-b069-3f51-be3c-c777629e6c4d | -17.2167 | -57.3718 | 2024-10-01 12:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.6 |
| 6f9c2d8e-6cbb-372b-bc7b-18de42267406 | -17.1774 | -56.1819 | 2024-10-01 12:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 67.1 |
| 654cc075-2c1d-3dbc-b9d2-4e40eb932c16 | -17.157 | -56.2259 | 2024-10-01 12:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.5 |
| 097830b0-33a8-369c-8eba-f9e268c774b2 | -17.1581 | -56.1637 | 2024-10-01 12:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 107.5 |
| 50754f5a-e3a4-3cee-b690-d9a5a5982609 | -17.1767 | -56.2234 | 2024-10-01 12:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 191.6 |
| a6956a39-8a48-33d2-acb4-73677d3fe8e9 | -17.1778 | -56.1612 | 2024-10-01 12:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.1 |
| 3cf3252e-827a-3bc5-aaa9-9220b274ddc4 | -17.705 | -53.2046 | 2024-10-01 12:46:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 9ce177cd-f732-355e-9cb8-64363c013b16 | -18.5236 | -49.4241 | 2024-10-01 12:46:49 | GOES-16 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 364.1 |
| 7b5892b5-e17b-3542-bef1-3e4808aa4ba0 | -18.6977 | -57.3123 | 2024-10-01 12:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.1 |
| 6600af65-2cf4-347a-912e-4bf4554fab12 | -18.6973 | -57.333 | 2024-10-01 12:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.8 |
| 09b1bb4b-187a-32a3-97ea-49c663dd2c49 | -18.9091 | -49.2129 | 2024-10-01 12:46:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 86.1 |
| 300b3ada-c9a4-3571-9c51-6f130fcd393b | -20.9153 | -49.1069 | 2024-10-01 12:47:02 | GOES-16 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 136.9 |
| 59b4666c-047b-38f6-98ae-c422daf17ea5 | -20.9353 | -49.1254 | 2024-10-01 12:47:02 | GOES-16 | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 990.4 |
| 484372d9-fe26-373c-b49a-c5d66ad7e52c | -20.9359 | -49.1023 | 2024-10-01 12:47:02 | GOES-16 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1006.4 |
| 6ecf2ef3-6443-3737-8b47-58302c106a3f | -21.3834 | -48.4915 | 2024-10-01 12:47:04 | GOES-16 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 110.1 |
| b613a98c-5745-32fb-987b-9a88cd928641 | -21.3841 | -48.4681 | 2024-10-01 12:47:04 | GOES-16 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 127.4 |
| fe352b1b-5393-343d-a6b1-7fc025488eac | -21.63 | -47.8016 | 2024-10-01 12:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 250.8 |
| 8a641f6c-ec86-3a6c-9388-510f36f35aaf | -21.5892 | -47.7882 | 2024-10-01 12:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 505.3 |
| 1fda8000-73a0-3d43-b928-fcce6f088fb3 | -21.6099 | -47.7831 | 2024-10-01 12:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 583.0 |


[Clique aqui para ver as próximas entradas](README165.md)
