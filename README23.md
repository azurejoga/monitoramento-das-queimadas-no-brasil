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
| f9d5fc03-b1ae-3493-8f22-a49ef5ff2988 | -12.05525 | -48.33858 | 2024-10-24 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48695c66-3fc4-375d-8af1-8be05dd79e39 | -12.05422 | -48.34361 | 2024-10-24 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61571e19-a8d1-36b8-9688-ef53a08a362f | -12.05263 | -46.71216 | 2024-10-24 03:42:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d8d69d2-fe2d-3b11-877f-b9ad45c236e1 | -12.05184 | -46.71614 | 2024-10-24 03:42:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14f4c9af-aa4f-37d7-884d-e98437ca6a00 | -12.05051 | -48.34126 | 2024-10-24 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f167028-8d76-3f7d-af1c-4a34e09bb1cc | -12.0496 | -46.7115 | 2024-10-24 03:42:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f31366e-6e50-3d32-b991-306a11ae8d03 | -12.0491 | -48.33706 | 2024-10-24 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc355d07-ae0d-355e-b9ee-8bc84026d5c9 | -12.04884 | -46.71549 | 2024-10-24 03:42:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a09d8cd-2d8a-3eaf-a4d2-64a410782442 | -12.00681 | -48.26921 | 2024-10-24 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 73475622-e3f4-38ec-9634-9c9d1aa2b72d | -12.00584 | -48.27402 | 2024-10-24 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 20e20a70-d2c7-37ad-94ca-295b655da1a5 | -11.99965 | -48.27277 | 2024-10-24 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 78eae9d9-d674-359b-8fea-a1301b301141 | -11.94149 | -46.59087 | 2024-10-24 03:42:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f917b23-317a-39b8-beca-2883049ef5a9 | -11.93998 | -46.58732 | 2024-10-24 03:42:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18e543ea-26ab-3f8e-939a-7afc0437a594 | -11.93918 | -46.59134 | 2024-10-24 03:42:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94ffd280-4021-3045-84e6-8ee1a222eead | -11.93593 | -46.58957 | 2024-10-24 03:42:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8fc2f32-7877-3133-8b5e-ae6910b8baca | -11.82365 | -47.07828 | 2024-10-24 03:42:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bb6a325a-dd87-32f8-a1ef-2a29122b9309 | -11.82284 | -47.08243 | 2024-10-24 03:42:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ca3421c2-3522-3f20-b1e7-5dd907a0c16d | -11.8179 | -47.07701 | 2024-10-24 03:42:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 091f181b-1a73-3e81-a4ae-47aa220f1b9b | -11.81708 | -47.08118 | 2024-10-24 03:42:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 10960d53-8513-323d-8826-a0c475d7edef | -11.7912 | -47.89078 | 2024-10-24 03:42:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c532f9f9-15cb-3b45-8905-63540afa138c | -11.79035 | -47.89208 | 2024-10-24 03:42:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8e379b52-7753-3135-a6bb-1d8d1aa7078d | -11.78915 | -47.07063 | 2024-10-24 03:42:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eda26f7e-1d86-3971-92c7-81fe5ec88784 | -11.78833 | -47.0748 | 2024-10-24 03:42:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d274ec2e-e626-32c2-9295-2675d3aceb1e | -11.78751 | -47.07898 | 2024-10-24 03:42:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 270b21f7-69d9-3a1f-8ac5-3d74885f3b95 | -11.78339 | -47.06945 | 2024-10-24 03:42:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5aaa0274-f8cb-34c1-bc96-cf3f6b100cdd | -11.78257 | -47.07357 | 2024-10-24 03:42:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6b10b782-958c-38c5-a191-a640f8d64b30 | -11.72416 | -48.3582 | 2024-10-24 03:42:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8da644d-a5d9-3ad7-b692-57885a1b9849 | -11.72314 | -48.36338 | 2024-10-24 03:42:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 557871f4-1f2b-39e3-8bc8-1434485056c1 | -11.6561 | -48.80675 | 2024-10-24 03:42:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 52b379ba-192e-3f18-971d-6d53eaa80e6b | -11.62019 | -48.3892 | 2024-10-24 03:42:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6739ba2-b202-318a-8433-f2741fc80db9 | -11.61393 | -48.38787 | 2024-10-24 03:42:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8b4644d-1ddf-363f-856c-77c62ecb4306 | -11.60285 | -48.46178 | 2024-10-24 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6a33b4f-6460-331d-b734-e57f75ec6ae2 | -11.60128 | -48.5468 | 2024-10-24 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c291f69b-8ddd-3be7-a840-7d527f95d6d3 | -11.60022 | -48.55205 | 2024-10-24 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0b8892b5-e0c1-30fa-9985-51655dd40ad8 | -11.59915 | -48.55731 | 2024-10-24 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bbd1bc5f-f2a9-368f-b66c-04e5683b9e79 | -11.59807 | -48.56263 | 2024-10-24 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 54139a30-5c3b-3bb7-9a2c-be1d048cfd55 | -11.5979 | -48.59602 | 2024-10-24 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65bb113a-1f38-3272-8862-2b02e2569919 | -11.59681 | -48.60139 | 2024-10-24 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efb4902e-a71a-34ef-9f53-2cdc82e858eb | -11.59608 | -48.50763 | 2024-10-24 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 925bc468-74c0-38d4-abfb-bee1c8622f99 | -11.59283 | -48.55591 | 2024-10-24 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3e7e53f0-9a7c-35a2-804d-fb310b4f2459 | -11.59174 | -48.56126 | 2024-10-24 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 74f84013-407f-3310-8ab3-892a6a9dfc36 | -11.59045 | -48.60009 | 2024-10-24 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9df2df4-66b3-3d31-844e-58297a4bb1f3 | -11.57274 | -48.54776 | 2024-10-24 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c668957c-c67a-3e15-a101-e7f172181af5 | -11.56856 | -48.5455 | 2024-10-24 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b03c8590-3ce1-3cfe-ba36-80c75191892e | -11.47162 | -47.06738 | 2024-10-24 03:42:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2de82015-e1cc-311e-a469-d709f05e4a01 | -11.47082 | -47.07148 | 2024-10-24 03:42:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aab55d16-bbc8-3b25-bf3f-3feec747ade5 | -11.28051 | -47.58507 | 2024-10-24 03:42:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b49fb2c9-dafe-3e36-98eb-16591c775e08 | -11.24989 | -48.72063 | 2024-10-24 03:42:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03a9814a-a6ec-3c5f-a9c2-17a6574e152c | -11.24876 | -48.72622 | 2024-10-24 03:42:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd27e2b6-def3-3460-b206-cdb70c87ab8a | -11.12731 | -48.6291 | 2024-10-24 03:42:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fee09542-70ad-32da-8c3c-5780e148131a | -11.12588 | -48.63342 | 2024-10-24 03:42:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3edae913-5503-32c1-b395-50dce8f1fef8 | -11.1209 | -48.6278 | 2024-10-24 03:42:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dbd20c59-2427-30e8-b7e3-0563df084739 | -11.12053 | -48.62669 | 2024-10-24 03:42:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c18c148-437a-3f36-8f31-f96dc3bafbf3 | -11.11946 | -48.6321 | 2024-10-24 03:42:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 329ef501-3163-3667-9643-760210cd5f02 | -11.11447 | -48.62656 | 2024-10-24 03:42:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a5cc9a9e-0d25-3b59-866a-2270186c58eb | -11.1141 | -48.62543 | 2024-10-24 03:42:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b82ad2da-9253-3dd0-80e7-e1271781bf55 | -11.02855 | -48.28083 | 2024-10-24 03:42:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c83d120-00bc-354c-be37-4d9df63f247a | -11.02224 | -48.27961 | 2024-10-24 03:42:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3f9b2fdd-2cd9-3173-9d18-5cee9e8b8d79 | -11.02127 | -48.2845 | 2024-10-24 03:42:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b900a44d-15e6-321c-a9b5-2dca84d6a102 | -10.97443 | -49.30633 | 2024-10-24 03:42:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f15b1ff-0236-38cf-b230-e3bc5cf9372b | -10.97316 | -49.31245 | 2024-10-24 03:42:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5bfe42c-fb53-35fc-8895-82ef5b610cde | -10.97186 | -49.3055 | 2024-10-24 03:42:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21cb3534-78b1-3a51-b0d3-f9dfa3a42f53 | -10.97064 | -49.3116 | 2024-10-24 03:42:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 68fa329b-37b6-313b-8f9a-802a320e093a | -10.8867 | -47.91039 | 2024-10-24 03:42:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 68917572-25cc-316b-8c51-f1dec5c27693 | -10.8755 | -49.14661 | 2024-10-24 03:42:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d05b5497-d7d1-3309-84ea-d23ec0813d62 | -10.86797 | -49.54111 | 2024-10-24 03:42:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dff81fe3-2346-3515-91cf-aed810a00aa8 | -10.69201 | -49.11333 | 2024-10-24 03:42:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c8b176e-dd70-3689-84f9-a1b89c1a4b25 | -10.68895 | -49.11013 | 2024-10-24 03:42:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6906cd5b-35a3-3e06-8614-78891a13487f | -10.68775 | -49.11616 | 2024-10-24 03:42:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 819a38c4-3f00-3adc-835c-09efd30b459e | -10.68535 | -49.11203 | 2024-10-24 03:42:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6cef2a0e-2bbe-386b-82d8-21905de34ffa | -10.68411 | -49.11805 | 2024-10-24 03:42:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ff4099f-325a-3875-9903-1900dabe1088 | -10.6811 | -49.11481 | 2024-10-24 03:42:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31c079b4-1ba2-32b2-bdd1-bda3a29d618c | -10.58869 | -48.0335 | 2024-10-24 03:42:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8a16de4-da84-3311-b7cc-ce2fe064f7ef | -10.58508 | -48.03383 | 2024-10-24 03:42:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 432d286a-ef8a-3f23-b97d-42e6f53ef106 | -10.5825 | -48.032 | 2024-10-24 03:42:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ecc21e7-6522-3ebe-b778-d0703b82ea62 | -10.4764 | -48.28715 | 2024-10-24 03:42:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1c28f788-e0af-3c20-9472-be3ae811f453 | -10.47011 | -48.28554 | 2024-10-24 03:42:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b347be4d-6bae-3eaf-bc1c-ba7b846fbe5d | -10.45644 | -48.59022 | 2024-10-24 03:42:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff2142c9-b3ac-3e15-9633-2ef026c30696 | -10.4564 | -48.58852 | 2024-10-24 03:42:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd4ea583-f961-3d7d-85f0-2c2525f09bec | -10.45544 | -48.59529 | 2024-10-24 03:42:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a43af3b-1308-3e3c-9b90-e1822c42bdf5 | -10.45537 | -48.59357 | 2024-10-24 03:42:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f58c748-27b1-3da0-9e80-e831506cc690 | -10.07575 | -47.72046 | 2024-10-24 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf6c1744-f5be-3ed4-b1c6-2a552c7d82d1 | -10.07481 | -47.72533 | 2024-10-24 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 39e67708-c051-31c7-9785-8d05120f33f2 | -14.48092 | -45.53139 | 2024-10-24 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93e0f32f-4f12-3ff1-9dfd-ad267fe6826f | -14.48035 | -45.53434 | 2024-10-24 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d74b5ac6-e172-380c-8ca3-c74665b363d5 | -14.47595 | -45.53036 | 2024-10-24 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d217df55-50f5-3357-8a56-75604a0cb692 | -21.28679 | -41.74591 | 2024-10-24 03:45:00 | NOAA-20 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 29ded827-e15c-3c60-b008-184cc9ce58ff | -19.83893 | -40.08292 | 2024-10-24 03:45:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3bc0b51f-c454-320e-b742-9ec220c27fe7 | -19.72157 | -44.20684 | 2024-10-24 03:45:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36b2ab5e-7bff-3a45-9a07-76faaa7452a5 | -19.71626 | -40.35362 | 2024-10-24 03:45:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 432c21f1-30c9-3f67-bf64-285c27c3714e | -19.37791 | -43.03238 | 2024-10-24 03:45:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2cf6a06b-ce9f-3035-8392-4a46b979d7a3 | -19.37755 | -43.03387 | 2024-10-24 03:45:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5b4422a3-f6d0-3276-beeb-b794ce941b53 | -19.24507 | -44.1624 | 2024-10-24 03:45:00 | NOAA-20 | ARAÇAÍ | MINAS GERAIS | Brasil | 3103207 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae504283-4738-3f75-a666-f256ce7b94c7 | -19.21829 | -40.13944 | 2024-10-24 03:45:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f6d0a121-987c-3e87-bf34-2de0c9654371 | -18.79178 | -42.49982 | 2024-10-24 03:45:00 | NOAA-20 | GONZAGA | MINAS GERAIS | Brasil | 3127503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d1942f18-c199-33fb-9db1-cb266b84d09a | -18.61988 | -42.80396 | 2024-10-24 03:45:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e562913d-3a7c-344d-8bc0-bd3b5a41b33b | -18.37819 | -47.39708 | 2024-10-24 03:45:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eab1053d-52fd-3c09-8f9f-bb982f6a5144 | -18.18378 | -42.87184 | 2024-10-24 03:45:00 | NOAA-20 | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ed2442d7-9c4b-3a4a-8c3a-c9824826ce86 | -18.03866 | -39.92551 | 2024-10-24 03:45:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f94b4be6-48c4-3465-91ed-c214c757dbc3 | -18.01485 | -41.83603 | 2024-10-24 03:45:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README24.md)
