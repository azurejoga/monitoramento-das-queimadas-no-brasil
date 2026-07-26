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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5ad77ff-d425-3a21-87ae-fca73b9a825d | -11.1635 | -44.4838 | 2026-07-26 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 03630fb3-0d10-3a2e-9abc-5ab521ca4386 | -9.65445 | -40.5886 | 2026-07-26 03:28:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 941b6f36-8622-305c-88c7-e05c8bf27b85 | -9.65361 | -40.59296 | 2026-07-26 03:28:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 580b230d-d321-39d1-b44f-95ffd03a7db3 | -9.24029 | -40.50874 | 2026-07-26 03:28:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b4d7876c-559b-35e9-ad08-1b6167ec9539 | -7.85214 | -39.90456 | 2026-07-26 03:28:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b543de6a-964b-3bbc-a0ab-0fc108e1a07c | -7.85292 | -39.90037 | 2026-07-26 03:28:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d6475bcd-80a3-388c-a4e2-3ba653a4da86 | -9.6595 | -40.59412 | 2026-07-26 03:28:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 20.2 |
| 926a25ee-f722-3e80-929b-1df6451a5c19 | -9.23947 | -40.51302 | 2026-07-26 03:28:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.5 |
| aa1260e7-e025-31c0-a40b-53245e9dbe13 | -9.66035 | -40.58976 | 2026-07-26 03:28:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| b808b32e-3930-30a1-9bf0-1588162e7ebe | -9.2462 | -40.50989 | 2026-07-26 03:28:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ff13a47a-1133-3621-b47d-a22645205d7e | -11.1443 | -44.4865 | 2026-07-26 03:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| ec299710-9333-3d05-abdd-83ed5c1689a9 | -11.1635 | -44.4838 | 2026-07-26 03:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| e430a9bd-78f5-30fc-af8a-68b36510caf5 | -13.74579 | -42.57379 | 2026-07-26 03:30:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| afd7ff11-7fa1-360c-8e25-e7ba8a1f304d | -19.36443 | -42.53784 | 2026-07-26 03:32:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ef258205-966e-3d95-8627-56d04e2a42fe | -18.69299 | -44.55225 | 2026-07-26 03:32:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6b1b61f6-2d60-369d-9e9e-bab01e5bab5d | -19.36988 | -42.53963 | 2026-07-26 03:32:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dcb5c688-2e2e-3d3f-aa42-aa4e1fb3abd3 | -20.29895 | -43.90117 | 2026-07-26 03:32:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0cf59466-ff99-3d58-bd1e-221fe395a17f | -18.69228 | -44.55114 | 2026-07-26 03:32:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 083f76a1-cbb2-35ea-bf9c-8f6bb6a3edb0 | -18.69863 | -44.5526 | 2026-07-26 03:32:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 34bffa8a-1884-3ea1-9935-2c190a62615e | -11.1443 | -44.4865 | 2026-07-26 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 0a523cd2-db4b-382e-9c0d-f196f8f4e545 | -11.1635 | -44.4838 | 2026-07-26 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| a76b8e7d-157a-38d6-b411-4b118efaee77 | -3.99941 | -43.29889 | 2026-07-26 03:47:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 24061402-8547-31df-80b3-351a049ae38e | -11.47822 | -47.52175 | 2026-07-26 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 13829ee6-8c3e-3536-82d1-cc6650108d83 | -7.0097 | -38.37599 | 2026-07-26 03:47:00 | NOAA-20 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 11e98506-da7d-3897-b69f-06cd138b1321 | -11.47229 | -47.52063 | 2026-07-26 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 273597f3-3efc-39fb-9222-ffec9884bb64 | -11.1465 | -44.48431 | 2026-07-26 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1cd46f5b-e31f-3e1e-a3b1-852ef4755d68 | -8.82976 | -47.08305 | 2026-07-26 03:47:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 384d1ce5-86b3-3d77-9075-6bbee93e99ee | -5.48637 | -45.11768 | 2026-07-26 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c7e40b3-518c-3b04-8c23-c75b246711bc | -12.95201 | -41.18031 | 2026-07-26 03:47:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8467be21-7e8f-3265-ace3-9cca477375a8 | -8.82371 | -47.08207 | 2026-07-26 03:47:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3d3eedc-b44f-381b-857e-3adf0a1288df | -11.47163 | -47.52393 | 2026-07-26 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8334f92-6aa9-34c2-9932-be5d3572e8a1 | -8.83157 | -47.08224 | 2026-07-26 03:47:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 398010f4-7027-39a8-be26-3a9c3510fbb6 | -9.92533 | -47.90509 | 2026-07-26 03:47:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfccbf53-037d-3006-92ad-5466f74eac48 | -11.47755 | -47.52509 | 2026-07-26 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7be93302-2de6-3576-bba8-c9ebd68fa1e6 | -4.00092 | -43.28984 | 2026-07-26 03:47:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 34dd1ef2-e778-3b28-866f-eb5717061775 | -5.93679 | -43.65425 | 2026-07-26 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 63d5885f-dcfb-38bf-b86c-6f8165be64c5 | -3.24148 | -47.91993 | 2026-07-26 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf5fd591-1fa9-3b72-9136-10d0cddbdea7 | -11.76865 | -46.57174 | 2026-07-26 03:47:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d15e3d0c-a0e3-3c02-becf-a390758afc8a | -3.95809 | -43.11094 | 2026-07-26 03:47:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4d17f8b-5145-3616-af9c-400553277389 | -9.53362 | -47.11518 | 2026-07-26 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6f81eed5-1b55-314b-8a1a-696751f37904 | -5.93626 | -43.65726 | 2026-07-26 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5faa3229-7d68-3477-917b-5f189cc120c8 | -7.01036 | -38.37192 | 2026-07-26 03:47:00 | NOAA-20 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 27593d67-a705-34e4-b2c3-02d74ff8dd4c | -4.91483 | -43.47099 | 2026-07-26 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4a6fa47d-605f-345c-aaa5-210f9da0cd18 | -12.95406 | -41.17801 | 2026-07-26 03:47:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 020dbe0f-14c4-3cdb-a723-97318e0fc0e2 | -3.96313 | -43.1118 | 2026-07-26 03:47:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 177d42d8-e839-36c5-bb7b-2112d6bbc1c3 | -11.14825 | -44.48585 | 2026-07-26 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 77e26540-20ab-3e33-b665-4a495fcc5d4d | -3.2404 | -47.92634 | 2026-07-26 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb7214c9-1644-3867-ab82-b6f388d7a090 | -11.76316 | -46.57041 | 2026-07-26 03:47:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 208e455f-1e8d-3163-88c7-bacdcd65a002 | -11.1514 | -44.48519 | 2026-07-26 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 641134a1-1e16-3c25-a7c2-ef4f1d50d9b0 | -8.82552 | -47.08123 | 2026-07-26 03:47:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d093cce6-f156-3a65-b8b5-70b1f1ab4ad8 | -9.36939 | -40.38134 | 2026-07-26 03:47:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7dc66c06-ac72-35b4-b0fb-09a233028d9d | -11.15421 | -44.48116 | 2026-07-26 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 61464ceb-984d-31a8-bb94-e629ff4a4e24 | -11.14751 | -44.47876 | 2026-07-26 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 329b3a9d-dc1f-33e7-8907-5b248737edf9 | -5.93121 | -43.65634 | 2026-07-26 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ed0e6a4c-cb87-3644-96a3-d284fbd99ec4 | -12.95584 | -41.18099 | 2026-07-26 03:47:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7a4e60d1-dcf8-3dbc-abad-638b3e51f524 | -7.00894 | -38.37462 | 2026-07-26 03:47:00 | NOAA-20 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 417b586b-a50c-3812-8bd2-5c27d4818036 | -3.99992 | -43.29584 | 2026-07-26 03:47:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 379674eb-b135-3483-987e-0829d37627e7 | -11.15315 | -44.48672 | 2026-07-26 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 86e3eb1a-ec1b-3767-80fe-a66787a3563b | -4.00042 | -43.29283 | 2026-07-26 03:47:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c1f80d84-609b-3a5a-a050-bae0594324a2 | -5.48567 | -45.12163 | 2026-07-26 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e1fc927-8e0c-3b84-b654-5e6ecf31a66e | -11.14931 | -44.48031 | 2026-07-26 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 9e833a3e-230e-3f12-8d36-2ef6774b0705 | -9.65565 | -40.59371 | 2026-07-26 03:47:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4ee7fb94-ebad-3a84-b8f2-d44479ae22a6 | -11.15241 | -44.47961 | 2026-07-26 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| c50a17e0-a22e-3e74-8bd6-2674046cfb7b | -6.85578 | -39.20739 | 2026-07-26 03:47:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 31bd98d8-a66b-34cc-ac3a-ae64bbd132d3 | -11.15038 | -44.49078 | 2026-07-26 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| bf876c46-14b7-39fc-831d-5f883b0b5d07 | -9.53279 | -47.11953 | 2026-07-26 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f5f3d3c-030b-371c-90ec-9f54181ec16a | -9.53872 | -47.12084 | 2026-07-26 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a8233f4-99b8-33e3-aa7f-4b052cfd098b | -9.93156 | -47.90623 | 2026-07-26 03:47:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59bea18b-07d7-3782-8c42-5db616486d0a | -7.34931 | -41.13432 | 2026-07-26 03:49:00 | NOAA-20 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 61a2116c-44a9-37ea-a823-becebec36088 | -17.28372 | -46.50304 | 2026-07-26 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 998e91dd-ed67-3334-84e3-10b8f4b07ed3 | -13.57793 | -41.3799 | 2026-07-26 03:49:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b67cbdf5-ab7d-3866-839d-129e64075d44 | -13.40663 | -48.16686 | 2026-07-26 03:49:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0517981-1d06-3131-8cf4-40fc85c2773e | -19.104 | -45.05977 | 2026-07-26 03:49:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7dac546c-c884-3960-9bf8-e943f18e8e86 | -14.89913 | -39.52927 | 2026-07-26 03:49:00 | NOAA-20 | IBICARAÍ | BAHIA | Brasil | 2912103 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 33e8c09b-cf9b-309a-9da7-33039eefda97 | -6.95674 | -39.8905 | 2026-07-26 03:49:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 683cded3-029a-3f90-a526-640f83634876 | -9.24342 | -40.50812 | 2026-07-26 03:49:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.5 |
| c5415806-f226-38f4-a540-7ec129a62347 | -12.66595 | -48.21197 | 2026-07-26 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f704b975-4815-3ff7-a89a-637270faae92 | -16.89334 | -41.16629 | 2026-07-26 03:49:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f3e25d97-bec4-3762-ab3d-991ece80b175 | -15.6358 | -47.86536 | 2026-07-26 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0557b4c-9167-3a5b-81b8-0de684d254c7 | -7.85408 | -39.89975 | 2026-07-26 03:49:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 6e009b99-1a62-3e55-b2a9-bd96fc48d0f9 | -15.69955 | -39.90451 | 2026-07-26 03:49:00 | NOAA-20 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e6432060-eb23-32d1-8acf-cb584bc2093f | -19.10512 | -45.05762 | 2026-07-26 03:49:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f698428c-fcbc-3157-9e51-9e8882cc809e | -19.10426 | -45.0621 | 2026-07-26 03:49:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1ae3aef-5536-3c8d-8f1d-91f637eec695 | -14.66237 | -46.95762 | 2026-07-26 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e72e66e0-0c6f-3281-8dc6-91a43fbc53e1 | -15.7734 | -43.06358 | 2026-07-26 03:49:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4b110a5f-ecef-3ba0-95d2-58f2ab15c567 | -7.85127 | -39.902 | 2026-07-26 03:49:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0fc2ccce-6e05-3455-842e-bdb6df0207ce | -8.01799 | -36.49664 | 2026-07-26 03:49:00 | NOAA-20 | JATAÚBA | PERNAMBUCO | Brasil | 2608008 | 26 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 781ca9d2-32a0-35b9-b0d7-61e7d41c322b | -15.635 | -47.86917 | 2026-07-26 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11d9e9b7-1496-34d8-9d8a-3efc337a059e | -15.77408 | -43.05985 | 2026-07-26 03:49:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4cdd5384-e4cf-3304-b216-87d99c4e87c1 | -19.3648 | -42.53939 | 2026-07-26 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3c91c8c9-7587-3590-bb15-db083f57b6f8 | -17.28319 | -46.50367 | 2026-07-26 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 224c8837-919e-31e5-b9ec-141b621aff3e | -17.28313 | -46.50603 | 2026-07-26 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87b6618d-fffe-33f3-84a9-237f4d496586 | -18.69538 | -44.54621 | 2026-07-26 03:49:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b1621b9e-caa6-35a3-93fc-63ce255d537c | -13.2007 | -48.3304 | 2026-07-26 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06162684-2f99-322f-8f90-9943eb73c9de | -13.38315 | -41.33922 | 2026-07-26 03:49:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| af5cd139-e3d6-3898-8d7c-4b92f60e94f5 | -20.29596 | -43.90179 | 2026-07-26 03:49:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d8699cdc-4e1f-3e03-9a5b-ec52efe58c59 | -13.19468 | -48.32911 | 2026-07-26 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7878d001-23e5-3864-8d53-e80f5e4423c6 | -19.36509 | -42.5381 | 2026-07-26 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7abc6424-d724-3398-a9ed-6cdc4f623b40 | -9.2387 | -40.51237 | 2026-07-26 03:49:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3e0ef427-ca56-39ed-b023-b83cdc56567c | -16.24851 | -46.29382 | 2026-07-26 03:49:00 | NOAA-20 | URUANA DE MINAS | MINAS GERAIS | Brasil | 3170479 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README3.md)
