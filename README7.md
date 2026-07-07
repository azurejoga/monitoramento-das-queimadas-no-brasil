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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc4ee326-b5b0-3231-a8df-84ad68ba9050 | -4.35076 | -47.76719 | 2026-07-07 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1eb793cb-8f72-3eaa-8932-be26ed38edc6 | -6.29794 | -43.64 | 2026-07-07 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0c90076f-2dc6-3ee7-ab20-a253face3c6a | -5.30865 | -43.69099 | 2026-07-07 03:47:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65d5ec70-92d9-31bf-9afc-9c92c8c6350b | -6.67147 | -38.84765 | 2026-07-07 03:47:00 | NOAA-21 | BAIXIO | CEARÁ | Brasil | 2301802 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 975e2eb3-141e-36cb-a4f9-c4f62542a6c0 | -5.80089 | -43.79782 | 2026-07-07 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a24f6099-ea48-3b6f-8f89-3b84c6793f0a | -6.20646 | -42.51609 | 2026-07-07 03:47:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 48a13e4c-72c8-3f71-8bc8-5a77c02d0b74 | -6.90416 | -43.70566 | 2026-07-07 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 79e73a5c-45f7-36d3-af0a-3efc306d68ca | -6.90338 | -43.71035 | 2026-07-07 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 075522ec-a92b-3854-a38e-30940a0131aa | -10.31964 | -49.91934 | 2026-07-07 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec5e76ec-7af1-33e5-ad41-2685f95794ac | -6.92314 | -43.70805 | 2026-07-07 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 03389591-e1f8-3d7f-862f-15243450223c | -10.55947 | -36.58081 | 2026-07-07 03:49:00 | NOAA-21 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1ecc51f4-ad85-3ee0-9190-70f5a6c9c8e2 | -11.68521 | -44.56596 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2324547a-2399-3604-8a51-b9bd5b3f202c | -9.44193 | -40.32237 | 2026-07-07 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 27019f88-16ab-3874-b786-8e966384224d | -9.30228 | -40.2462 | 2026-07-07 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 93657e36-bd7b-30c0-8cb8-7892b5da7524 | -9.20743 | -45.31902 | 2026-07-07 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0eca6464-d27d-36af-b317-8b4936b89230 | -7.37695 | -44.00536 | 2026-07-07 03:49:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25bc2845-8350-320c-93f4-e1b906524710 | -12.68246 | -47.67918 | 2026-07-07 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3cdbff55-220d-3c95-aa5e-28d28d74ae81 | -10.93789 | -43.06474 | 2026-07-07 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d125aeb1-4341-3cb7-9055-05aa19ed4cdc | -12.50571 | -48.25598 | 2026-07-07 03:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b73f8141-b22a-3aa2-8b01-0009757df81e | -12.79404 | -44.50256 | 2026-07-07 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 05757970-4b54-33c3-aeab-ddbe8d41aa73 | -11.68076 | -44.56516 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b4e23978-12da-3e03-8fcf-5eabe29f3a27 | -11.92221 | -43.37728 | 2026-07-07 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c6c67d2d-750a-31ea-ae00-82242ff12237 | -9.18159 | -37.50574 | 2026-07-07 03:49:00 | NOAA-21 | CANAPI | ALAGOAS | Brasil | 2701605 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7312b56b-f6ef-342a-b24e-6447db6db910 | -11.63363 | -46.36713 | 2026-07-07 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef7b7b90-b2be-3452-96eb-feed3910b3f2 | -11.6844 | -44.57045 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10ad5877-0225-3f24-bece-bdc02c46c096 | -13.52206 | -43.99226 | 2026-07-07 03:49:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a03b782-2547-3bea-9b8b-d44adf20c2bd | -11.67712 | -44.55987 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 2cbd96f9-9a58-3cef-ac5b-27787f530c31 | -12.68606 | -48.21234 | 2026-07-07 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6f9a850-beed-3d10-8c3b-5d0729f30483 | -12.78459 | -44.50521 | 2026-07-07 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7167f290-9121-360c-85ed-bfdb64569e73 | -6.90868 | -43.71038 | 2026-07-07 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| da0d4b51-2d8f-34aa-a4d7-40a39ade5d28 | -6.91404 | -43.70648 | 2026-07-07 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 44d49970-a5ea-3cbb-b6f3-71c9c841ed23 | -9.50385 | -36.54692 | 2026-07-07 03:49:00 | NOAA-21 | PALMEIRA DOS ÍNDIOS | ALAGOAS | Brasil | 2706307 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 24338cf4-a9a6-3a52-9002-0a4d70048c98 | -11.65771 | -44.56562 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a87fdf9d-2550-39a3-976a-162c3b6752c0 | -9.50439 | -36.5434 | 2026-07-07 03:49:00 | NOAA-21 | PALMEIRA DOS ÍNDIOS | ALAGOAS | Brasil | 2706307 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 832a59dd-5651-3bbe-9106-a64f524a98f1 | -9.40777 | -48.02104 | 2026-07-07 03:49:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60e4114d-595b-3581-8325-676878e60487 | -9.37857 | -44.72672 | 2026-07-07 03:49:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72e45086-4829-3d6d-bde7-55df044584cd | -8.07553 | -45.58317 | 2026-07-07 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10c8e506-20e1-32b6-bea8-caf4deacad1c | -6.91324 | -43.71113 | 2026-07-07 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 9b73b283-833d-3884-ad89-e621c86e3b83 | -11.66297 | -44.56194 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4962cec5-3909-3bd9-83cf-6238d5d139f5 | -13.44185 | -43.85531 | 2026-07-07 03:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9a67824-a725-370f-b716-22b6b8c02abb | -7.00958 | -42.77812 | 2026-07-07 03:49:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1c45e52e-39ca-31e7-9dc1-17072229e1cd | -6.93304 | -43.70497 | 2026-07-07 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a026c633-d3c0-39f1-b5ff-975333c00778 | -6.92234 | -43.71267 | 2026-07-07 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ed8efc75-ecda-355f-bfe3-99263aa6d590 | -8.04146 | -45.04077 | 2026-07-07 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c6a4f6b-b73d-3f2e-8e1d-0ab9f5512f9f | -13.08273 | -48.16588 | 2026-07-07 03:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8cb96184-8da4-34d9-af5d-18cc47faf722 | -12.50978 | -48.26481 | 2026-07-07 03:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2f533a1e-9ac4-3ce3-8132-1b11de893867 | -8.11778 | -47.11053 | 2026-07-07 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d287bf89-6a7a-3d19-b8ab-41e1897182a4 | -11.62956 | -46.36449 | 2026-07-07 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d462772-ffb8-3fbc-b6fa-3ea721789d57 | -13.52383 | -42.55105 | 2026-07-07 03:49:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 61681ddd-ab02-360b-b441-f318beaba410 | -12.79482 | -44.49828 | 2026-07-07 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f2f7e640-e6b0-32de-8ea6-be487752a4e6 | -11.65408 | -44.56033 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 24228db2-eca9-3331-9169-503e42c661fe | -6.89956 | -43.70893 | 2026-07-07 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4a652af-af82-3d80-a186-2f655613f82d | -11.4657 | -46.65052 | 2026-07-07 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b299a5f3-612e-304e-bdc2-fa7a74bfc791 | -11.04971 | -49.60048 | 2026-07-07 03:49:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 918a54d3-1c68-3853-87f9-b257199f9b8c | -9.20256 | -45.3181 | 2026-07-07 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c236a31-1f00-3d4d-b327-f17514de1d5a | -11.99179 | -45.14308 | 2026-07-07 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4272e54b-c7b9-3fb0-9a25-391571162385 | -13.08819 | -48.16718 | 2026-07-07 03:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d81db90-0bdc-339e-9dcf-6235897bde01 | -12.78537 | -44.50091 | 2026-07-07 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 658eb1a6-c7ba-351e-b001-a2c45ced2b11 | -8.03657 | -45.03992 | 2026-07-07 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae778951-dc38-3389-bbee-2d9e607237d8 | -9.36327 | -40.42788 | 2026-07-07 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 065d95ec-006a-37df-955a-e15cfa8a44a7 | -6.92689 | -43.71345 | 2026-07-07 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 3d06532b-3aa6-3bf2-bc94-c448c05a3472 | -10.93724 | -43.06842 | 2026-07-07 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 8ce8717d-9a2c-3b8c-92d2-3af18aea64bb | -11.63009 | -46.36159 | 2026-07-07 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a975d5a3-a542-329f-a9ff-a32f1eed6ff8 | -12.79837 | -44.50341 | 2026-07-07 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a4f1974-463a-3967-b270-636051808e75 | -6.90949 | -43.70572 | 2026-07-07 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| abfda3f0-8283-3bb2-8f1b-662518a32217 | -8.12172 | -47.11038 | 2026-07-07 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 223d6244-ae8c-31e2-9ee3-74defbbae86a | -11.63399 | -46.36864 | 2026-07-07 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8b8cc15-32f2-3d41-bf67-a4452355888d | -10.69826 | -41.86989 | 2026-07-07 03:49:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ada5dae7-65c5-36b4-b050-6526bd6e0145 | -11.65689 | -44.57011 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1de24a07-6427-3664-ba9b-758d0aa64926 | -11.66379 | -44.55745 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9d7b4d51-9477-3d97-9f26-815ba7ff1b95 | -11.68238 | -44.55619 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dcad5d14-6781-3a5c-b2aa-ee6a0ae3c19f | -10.93317 | -43.0677 | 2026-07-07 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 77e7d645-9d38-31a4-83cd-0ce8f2237607 | -9.36395 | -40.42373 | 2026-07-07 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4a5c56e2-88bb-3154-bb54-a2f61f699b6f | -9.28312 | -49.58328 | 2026-07-07 03:49:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c7403e5-0cb8-3234-8974-5209414cfff4 | -12.35923 | -47.42283 | 2026-07-07 03:49:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 34157715-2bb2-3c3a-b071-e4681bff6f52 | -11.66461 | -44.55296 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6f0289aa-0f11-302c-bfea-f17fa30912a2 | -11.69896 | -44.13074 | 2026-07-07 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cb343d54-ce3b-3e92-8bb2-43665eff56dc | -11.66861 | -44.58152 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 26d08a66-498a-307e-9efd-d095337c7c83 | -9.30294 | -40.24214 | 2026-07-07 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 123573d9-bde6-3bea-bbd6-874fbac39bd0 | -11.62341 | -46.36975 | 2026-07-07 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e772b77-5d13-3ff9-8181-5ef57024dee6 | -12.7976 | -44.50769 | 2026-07-07 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd9b01e2-0cf3-33a2-9ea0-55a13a68f3af | -13.44253 | -43.85152 | 2026-07-07 03:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d82362df-7d76-35d7-91ce-a419d8a7abb0 | -6.91485 | -43.70185 | 2026-07-07 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 30a5e906-8ff5-33bf-a2a8-f5ad1f150e16 | -7.90623 | -48.25119 | 2026-07-07 03:49:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2dc42bc9-dddb-35ce-a9b1-d20239a09d55 | -9.37477 | -44.72095 | 2026-07-07 03:49:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eeebc4a2-dbbc-33da-b03a-c504f1cef61d | -8.07451 | -46.68741 | 2026-07-07 03:49:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1bd9c4f9-0e68-3e41-868d-df14c6d69484 | -8.1234 | -47.11144 | 2026-07-07 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f69509d4-0afd-3a44-af54-047fca219863 | -6.90786 | -43.71506 | 2026-07-07 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b1b9598a-2e10-3e51-a61e-79e3c56af6f8 | -12.75703 | -44.55787 | 2026-07-07 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9527986e-63cd-3e5b-99ff-a39dfb908646 | -12.51205 | -48.25323 | 2026-07-07 03:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73f3430f-299f-3920-a537-9b75f54b20e9 | -10.32072 | -49.91394 | 2026-07-07 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae5fd98d-30e8-3593-8d5d-bf158df67d93 | -11.66943 | -44.57701 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d51baf0e-e770-36a9-867a-974b4f587f2a | -9.2046 | -45.32061 | 2026-07-07 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 50090c1c-5b80-3d66-ae94-d0f034d9ff1f | -8.1171 | -47.11433 | 2026-07-07 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ba33e271-f5f0-3c5c-a987-c7954d781b74 | -10.93659 | -43.07211 | 2026-07-07 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 6046385c-6d19-3545-b87d-f2135ace1fd9 | -12.36388 | -47.42729 | 2026-07-07 03:49:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51b7adff-cdc4-37df-b2cd-d9db67a04c71 | -12.76296 | -44.55008 | 2026-07-07 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61ea7612-7226-37aa-8c69-96bf4138c86c | -12.68314 | -47.6757 | 2026-07-07 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50bef2f1-1c94-38e5-9551-523931e95026 | -6.91242 | -43.7158 | 2026-07-07 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| c8ab4203-966b-3508-80b0-4e830136416e | -6.93224 | -43.70961 | 2026-07-07 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |


[Clique aqui para ver as próximas entradas](README8.md)
