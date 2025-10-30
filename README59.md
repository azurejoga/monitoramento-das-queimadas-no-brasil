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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29c6d0b3-d92e-38e8-8a60-57a39cc79744 | -12.71205 | -46.30114 | 2025-10-30 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b52a67e5-f02d-3e24-b3a6-37b8c9f7a225 | -13.92921 | -48.4893 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 33584457-e37e-3662-a1ef-b8dfb696c3cd | -15.11286 | -43.26966 | 2025-10-30 04:27:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 48f7ef98-c93f-3250-b0fa-2696549b49d7 | -13.27618 | -47.74639 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9434ef9a-7746-3e96-96f7-c9ff5442c12e | -13.41416 | -43.74655 | 2025-10-30 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ba232954-1a33-30a2-b8e1-47668f6a7fa0 | -13.19895 | -44.48333 | 2025-10-30 04:27:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c57aaaa4-0b7f-3221-828d-bce8b723775d | -16.82407 | -43.10984 | 2025-10-30 04:27:00 | NOAA-20 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f7aa8bd5-0375-303f-8d66-25dd8ffe1bb2 | -13.64688 | -48.42814 | 2025-10-30 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb82aa86-3a28-31bd-afe3-5b09cecefecd | -12.88204 | -48.64128 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 839206b0-48d0-39f3-a6ff-107d239dc9c5 | -13.5979 | -42.51152 | 2025-10-30 04:27:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d30de3db-1448-3af7-84ed-8fd4884f1692 | -13.22779 | -48.55953 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7745420c-d5cf-37ea-b325-be0c2d58b7e8 | -12.23198 | -46.47401 | 2025-10-30 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6b34b20-c01f-3167-abb6-081d80481c49 | -13.93946 | -48.42538 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed6e6b00-d558-371e-ad4a-257e2788b238 | -12.30983 | -48.05415 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d06abc4-25d3-34e1-8f36-3beada1d7493 | -12.14268 | -48.01593 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d064d3e3-573d-302d-9c5e-d4e278273402 | -11.95338 | -49.94239 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b95c0e6b-7b85-3464-8477-9f2fafbf0c0a | -13.22145 | -47.72632 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da41713a-b65b-314b-b223-bd9b2be3564a | -13.47165 | -47.45244 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aae8789c-9bee-348d-b048-37f8791a1e4f | -18.04679 | -43.14832 | 2025-10-30 04:27:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 78a43a27-d99e-3920-82f0-aa8efed54206 | -15.02033 | -46.3076 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0642cf61-a234-3549-8f08-9a989e3151ca | -12.16187 | -51.48136 | 2025-10-30 04:27:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| adf734f0-14a2-3fe8-8ae8-1f854fadcf56 | -13.47641 | -48.3667 | 2025-10-30 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e093e10-8375-3aef-8755-60a0864adc7f | -13.32641 | -47.68589 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a26ef04-3154-36a2-9e74-c1f47d82f42a | -14.7797 | -44.98582 | 2025-10-30 04:27:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7579e03-97f2-3123-b0b8-c55bf13c4f42 | -18.23208 | -42.37044 | 2025-10-30 04:27:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 138da01e-fcd0-3736-9e3c-64dcf1f4f8af | -12.06368 | -47.82904 | 2025-10-30 04:27:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2df4468-2af6-3df3-a103-611b71a76463 | -12.29164 | -50.32603 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bed75f29-75ef-30e4-a085-5371712943cc | -14.28553 | -47.30711 | 2025-10-30 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6dce2476-53f7-38c4-8863-3127b7103fb2 | -12.1916 | -46.71251 | 2025-10-30 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 24ecf50f-cbb8-3127-9a40-18933c5985b9 | -13.77781 | -48.39525 | 2025-10-30 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c58014fa-3bd8-3466-b2f4-157513b619af | -13.32549 | -47.4758 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f51f3524-e654-338c-ad14-85ff359281b0 | -12.29774 | -50.26879 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 13fc32bb-211c-3f4d-bcaa-915a5f16d816 | -14.57157 | -40.72258 | 2025-10-30 04:27:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b14a0459-ff2f-39a8-b98f-184f814b6a6a | -12.12099 | -47.14317 | 2025-10-30 04:27:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 946b9555-ed9b-35c7-ac3e-be66ed4aceb4 | -13.27785 | -47.7358 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3cc7bba-1189-3be7-8b24-59de7db2d860 | -14.67992 | -46.8406 | 2025-10-30 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 805ab478-0093-3060-acd0-c4614afb4af1 | -19.33383 | -43.05595 | 2025-10-30 04:27:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 397c8082-8c5a-3bbf-bdce-7593ff49c547 | -13.9598 | -48.44706 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cb188853-6afa-3f19-8cd5-50e2937e077b | -12.57384 | -48.88351 | 2025-10-30 04:27:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1f2ab83-e007-3612-b767-b11207335c54 | -13.03571 | -48.46513 | 2025-10-30 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47e5543c-a1ee-3493-9b39-1976e86278eb | -14.28833 | -42.33569 | 2025-10-30 04:27:00 | NOAA-20 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 8c1573b2-3f9b-34fd-93bd-9d1d82312063 | -15.61416 | -43.98804 | 2025-10-30 04:27:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55274572-cf08-37a4-9c93-51a32b0cc5ac | -14.75621 | -44.95747 | 2025-10-30 04:27:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a714d38-ae07-3fee-88fe-93ff7dd8de96 | -14.53483 | -43.78798 | 2025-10-30 04:27:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0697df6b-142a-309f-99c8-a8010f7ecf06 | -12.32882 | -50.17089 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4c2065c2-3b75-33e6-b7e6-38d54e41317d | -13.67428 | -47.1754 | 2025-10-30 04:27:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e2926e9-ff03-397a-937f-881f0de325ea | -13.30712 | -47.70078 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b7ee335a-a252-3de1-9132-845faf07bd68 | -12.32949 | -50.16689 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ec90445a-8884-3b6d-b5e5-e070cc452b04 | -13.3005 | -47.6997 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ef50f96-f974-3d4d-9efe-636d09e98088 | -13.32255 | -47.71056 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 26ac8203-32ad-3f1d-b853-cf13b1a6cc9e | -16.03811 | -43.72625 | 2025-10-30 04:27:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 805982ec-9271-3822-a664-d8de65b0c6ad | -14.78689 | -44.98687 | 2025-10-30 04:27:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 670bbbad-97e3-35e4-b75d-46c9c9cfc7e7 | -18.3548 | -42.24901 | 2025-10-30 04:27:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3f5b6e9a-7cfe-3c85-b3d6-1e0e95e90c78 | -13.28763 | -48.56944 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1142241-5889-313a-a3a9-d5d9dbbefa7b | -15.09537 | -41.9866 | 2025-10-30 04:27:00 | NOAA-20 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 055e9609-a6a0-3966-bc8b-bf91a0e700b7 | -13.21815 | -47.72578 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47302ae0-c7e9-39f5-a358-cb8e96f45655 | -12.32196 | -48.06339 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b889a824-4222-30ed-8133-b3ae83ec6877 | -13.08191 | -49.49073 | 2025-10-30 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d508ff9-172a-3fa6-9939-1dbd59b9ba52 | -13.49491 | -47.99558 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93f43e8c-8f57-30a3-a84d-0989162f89e1 | -12.18827 | -46.71198 | 2025-10-30 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5bf9c827-b3f2-3154-aae3-8e60d54639cf | -13.29731 | -47.06763 | 2025-10-30 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d634c51-d7a6-3f45-a7b4-08bc39da8a55 | -12.85771 | -48.62238 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc9cd3a4-ea65-3741-a268-bc89ef01bec3 | -13.62623 | -47.59333 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66e2f941-efa2-3b33-8628-383c5e3df8ce | -12.25056 | -47.93579 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3f6f43b-d477-3e7b-b0f2-bb53df2ab09e | -13.52844 | -44.34293 | 2025-10-30 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 281a9318-167a-3fb9-a135-ccd705443482 | -13.93889 | -48.42892 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3694170f-53d7-3208-9ab8-0a91f9870c8e | -13.2205 | -48.56593 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22857540-7aaf-3710-9d7c-b211935eb20e | -13.40029 | -48.37603 | 2025-10-30 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f52a5e2b-326e-31fa-92ad-b53a32c94ab3 | -12.52147 | -44.87956 | 2025-10-30 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8feef271-a357-371c-863f-b475a0676215 | -12.31558 | -50.31351 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83ff588c-a409-3f5a-8d68-d523f2d0d696 | -14.97748 | -43.38692 | 2025-10-30 04:27:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9682c70c-9fa7-3ea5-a346-189828e71f28 | -15.02487 | -46.32397 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eb19f3fb-521b-3df6-aa0d-d005eb323d97 | -13.28171 | -47.73282 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3be3b2e8-2276-30bc-80cf-7f6adf0da5ac | -13.1796 | -48.43816 | 2025-10-30 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67818f21-f510-3ce3-9006-e7f90f1cc8fc | -12.3159 | -48.05873 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d6fd7fbe-60be-3b79-aa12-af69753d0399 | -12.88146 | -48.64496 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aae8906c-91b4-3760-97cf-3808ed52b1a2 | -12.22475 | -46.47654 | 2025-10-30 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ff88ad3-287a-370d-aaa8-eac52dd576aa | -13.56016 | -47.36475 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6ccc46e-a782-3d69-a313-001c68a9b551 | -14.24622 | -47.3192 | 2025-10-30 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3ec21093-9b40-372c-92a8-0dd2dc553e73 | -19.9126 | -42.32608 | 2025-10-30 04:27:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a8f6b242-627c-354f-9b72-3347136f951a | -12.47795 | -50.59666 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94304a6d-b92e-3812-81f6-a61bd1dbe9f5 | -14.97355 | -43.38634 | 2025-10-30 04:27:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 507d0e3f-b04b-311c-abea-b75ad60c9b09 | -12.49359 | -50.56953 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5ace48c-bd93-3857-9902-93dd7a83d0e0 | -12.31314 | -48.05468 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e3351f1-4d7a-300e-9cb3-810d22a9dba5 | -13.12576 | -46.9266 | 2025-10-30 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2f7bec5-b9b9-3838-9a81-182d9d0fc655 | -13.03136 | -47.03267 | 2025-10-30 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08ae0f65-92b1-350e-9d3e-4dd448b30d04 | -13.78288 | -44.36327 | 2025-10-30 04:27:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e6bd789-f03d-323d-ba2c-6e00ee2db7f7 | -13.47726 | -47.99989 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 76547fb7-2bfd-32d7-b301-3a9c47a8e689 | -12.98216 | -47.9074 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16e0bb42-4ae7-3e1c-b113-bd32b3106065 | -18.54881 | -41.57536 | 2025-10-30 04:27:00 | NOAA-20 | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c8e3b4d3-1cd6-389e-8de8-75f8ea2bb707 | -12.04108 | -47.82171 | 2025-10-30 04:27:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85b9f299-7f0a-3438-8ced-19c3d3ecf058 | -13.67041 | -47.17836 | 2025-10-30 04:27:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61a4f3bd-784d-3c62-83e9-eb3ac94ad5cc | -13.19777 | -44.48475 | 2025-10-30 04:27:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2be5822-d9ba-36a6-979d-2be56cf99d44 | -12.30547 | -50.26599 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 368401a0-9ccc-34ac-82d8-50253549b482 | -13.58059 | -47.34256 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddc166bb-c9b8-3b4c-8958-4d478d89daba | -14.28493 | -47.33275 | 2025-10-30 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d9b529dd-80cf-332d-9c8e-51d13dd83ef1 | -13.41928 | -47.37494 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe735644-5996-3e85-827c-ed7f68dc5705 | -13.54962 | -47.12681 | 2025-10-30 04:27:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21db346c-02f1-369e-b244-b3e403b3a2ab | -13.62018 | -47.58873 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d572cf6a-bdea-3dc9-ad56-d18ce6c52e32 | -14.25786 | -47.31001 | 2025-10-30 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README60.md)
