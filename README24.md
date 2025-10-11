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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c777942b-429f-337d-9ddf-9873047c18ba | -14.99297 | -45.56441 | 2025-10-11 04:34:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2adac70b-3bdd-3719-bad6-d383c11af9c8 | -11.60536 | -48.56702 | 2025-10-11 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80e178e7-e075-3f6c-83f0-b7590a7a85df | -12.74931 | -48.64563 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21c0e358-a69d-373d-9d65-bd8809ef8634 | -9.16273 | -43.16908 | 2025-10-11 04:34:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| eeb869ac-a4f1-370b-b0db-30199dee4af7 | -13.20687 | -42.34185 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 65b8152e-5ca0-3518-8322-1b51bcac4f4c | -10.5126 | -47.3568 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 38829bf3-f41a-327c-a622-517bf1f4919f | -13.33615 | -48.47638 | 2025-10-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7fa9311a-4651-3e1e-9d56-7e546ee78da1 | -15.39348 | -47.28601 | 2025-10-11 04:34:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50b27090-880d-36de-af6a-2c416e0f6a63 | -10.57207 | -44.51029 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c28c629-0c45-3037-8bea-07f01067ece7 | -14.2348 | -49.09119 | 2025-10-11 04:34:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c32b5e65-bd63-3186-be23-672daf5a508c | -10.61404 | -47.45063 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0ff32156-75df-3c76-8640-bb022ff8d379 | -10.57272 | -44.50563 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 807d504f-4ed2-3362-9a70-f96b60087dd1 | -13.31705 | -47.11879 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e380448-dec5-38ee-a06f-c07b565f417a | -12.22214 | -43.7907 | 2025-10-11 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4af8cc7f-9cea-3ccd-9bcf-a69ec60cd7e0 | -13.31621 | -47.97915 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f2ee7fc6-97bf-3daf-9911-b4ac0131e2e4 | -14.01238 | -47.0587 | 2025-10-11 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca866fd7-4c02-3526-808e-9343e292b966 | -12.74768 | -48.65619 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ca141e30-ae25-3f9b-b792-f17bf6830b48 | -11.06504 | -49.55988 | 2025-10-11 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f10d6d18-d9ac-34b8-a3a9-ce92fec054df | -13.33893 | -48.48054 | 2025-10-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2fbe8b8-0268-3236-91d0-cc51a785ff89 | -13.31888 | -47.13045 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a273825-9260-3997-b2ca-1f5c9d1354be | -9.51123 | -47.8792 | 2025-10-11 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4aeef6f8-f1ef-3422-a056-9169ac642b5b | -13.29214 | -47.12773 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 36cc37db-d486-3e91-8c2b-1afed183cb4d | -15.70661 | -46.63416 | 2025-10-11 04:34:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ee6945d-8c0c-306b-82f4-794e7d1c1fb6 | -10.52716 | -47.35158 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 64dec828-dbe0-329e-bc8c-2e0367be44a4 | -12.89945 | -47.05376 | 2025-10-11 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dc1352ad-1666-3bf9-998a-3ee091f7dc2c | -13.34226 | -48.48104 | 2025-10-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae6dde2e-2d1b-3890-9f20-3742d3ed0d59 | -13.30838 | -47.98552 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a22bc55-6cf5-349f-98ea-5f3a6e502470 | -10.17682 | -44.545 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9d13a9e1-b690-3655-857c-6c19d3d905e7 | -13.53621 | -48.12174 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76442cf5-4dd2-346d-94d4-e40b6c6b05dc | -9.12108 | -45.06541 | 2025-10-11 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4532d9bf-df7b-3c89-a8c0-dfddef60ec84 | -13.48692 | -48.10672 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8a43d4c-a6bf-3c6a-a37b-c498ee88426e | -13.33839 | -48.48406 | 2025-10-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06e55ff2-feb8-343b-900d-d07b6b11b309 | -13.21665 | -42.3383 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 103.3 |
| ae290cb7-2c99-3556-aced-68848f14be3c | -11.76444 | -45.04525 | 2025-10-11 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97c66402-fd81-3ea2-9d4e-6808837c96b7 | -13.38359 | -47.7369 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a0c58c2e-f9ea-3170-b0c9-1574036b9028 | -14.4422 | -50.35061 | 2025-10-11 04:34:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 102e18cf-b2df-3a47-8861-b88a170a1706 | -16.29247 | -45.24402 | 2025-10-11 04:34:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40d8cf4c-cdc5-3684-9ec1-3f91439268ff | -12.22161 | -43.7946 | 2025-10-11 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8370db3-7887-3365-8836-33d815496afb | -12.76782 | -48.65925 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 359f751f-a343-32df-b1d6-e3841c20a8af | -13.28699 | -47.13857 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b1351fb7-a3c5-3eb0-9398-3463aab6950f | -12.89025 | -47.04408 | 2025-10-11 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 150773db-9729-330a-9fef-e45dab4b88e0 | -9.40298 | -45.77597 | 2025-10-11 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 747b4d61-d4d4-37e2-9a86-6e1902d4fca2 | -11.77185 | -46.37204 | 2025-10-11 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9581e2f4-14e1-3d02-bdd0-a9399f734dd2 | -10.15255 | -44.55172 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 85e56aea-c63b-36fd-a53c-36905fd8edaa | -14.7414 | -46.11578 | 2025-10-11 04:34:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11d5c279-8d1a-3ee6-ad32-3a30f46f8339 | -12.75951 | -48.64703 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f0a2353-c0b1-3bda-b02f-71f4262289e1 | -12.77113 | -48.65978 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3929afa4-ebcc-3783-8a67-e0a3f323d411 | -12.76011 | -48.66523 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92941fc9-e7a3-37da-a0f5-8ccd92621a01 | -14.99481 | -45.57934 | 2025-10-11 04:34:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a501064-95de-3ecf-b4d6-350eda57762b | -12.76674 | -48.6663 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a48ac0c-ccc0-356f-9a7b-0dcc132db1d6 | -9.2932 | -47.7046 | 2025-10-11 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8dc856fb-c329-36c9-8100-f94ed62c33fb | -14.70616 | -47.43909 | 2025-10-11 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70883ca7-1341-37ba-8bfe-1a1ea2bebbf3 | -12.92456 | -45.04672 | 2025-10-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e9d61f32-081e-32d3-a404-6a0688ba482b | -14.95421 | -46.7456 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 731405df-3faf-377d-9a14-8607d8791ba7 | -9.10735 | -45.03196 | 2025-10-11 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 874133d7-337e-3f00-839d-557bf52660c9 | -11.45373 | -43.48111 | 2025-10-11 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba260251-5ccf-32d7-af0c-30690948e7e8 | -10.18063 | -44.54552 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bdbe076-82a7-3e7c-8271-92dcb9b55507 | -11.78475 | -46.38205 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da2941de-0800-3682-afd4-ae869cc2b24d | -15.32224 | -49.55697 | 2025-10-11 04:34:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47d67500-a045-33b6-a46c-f120f24f8b2b | -12.92839 | -45.04725 | 2025-10-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc8d7a20-d10f-33ae-ac35-749dc9e26943 | -13.28057 | -47.99645 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 94235129-90c0-375a-9d59-8fcb19c5830b | -15.06449 | -46.60413 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec3091f6-93ca-336e-9a59-5c4582940858 | -14.01528 | -47.06337 | 2025-10-11 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 937a4ba0-f92a-3cf5-b872-0a042de4a3c1 | -11.77479 | -46.37645 | 2025-10-11 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 20d012c6-21f3-3b87-ad03-a8a2c32f90f9 | -10.75978 | -47.9639 | 2025-10-11 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6166e658-e65d-33f8-9b2d-3c08a2140049 | -12.22561 | -43.79594 | 2025-10-11 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 800f0836-61a8-30ad-b0c2-5cbb023dbf94 | -14.99231 | -45.56923 | 2025-10-11 04:34:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1421ab1-6d18-326f-b922-9843d56d8285 | -10.17751 | -44.54022 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f463167c-dd39-36d0-b518-3a75ff4b29e9 | -12.76891 | -48.65219 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 074ada57-423e-3fca-9aaa-7b2f146cec83 | -13.30777 | -48.48614 | 2025-10-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ec289bd-5cb8-3378-918e-19d1a67d6f37 | -13.2996 | -47.12514 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8578f78b-9054-3bea-aa76-8b068435d5cf | -8.93665 | -46.58157 | 2025-10-11 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eaea4a82-08db-3363-9b67-65760341cc5b | -10.38632 | -57.64409 | 2025-10-11 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4b3a09f-c53a-37f2-ba2e-cd8b0ffb37d3 | -11.71656 | -44.29065 | 2025-10-11 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e5e8829-71d9-3329-b8d3-782f387d3a72 | -10.19455 | -44.60979 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 61bc3c6f-b6e1-3489-8d18-08390beaddfd | -13.51162 | -48.12524 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9aecedc6-7349-37c6-9fbd-d215fb8fcdc0 | -12.89423 | -47.0411 | 2025-10-11 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8970d7de-52bf-31ee-89c7-5dcf6a4650a1 | -15.40984 | -47.29675 | 2025-10-11 04:34:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e548f52-926c-3109-a048-3e1dbba2a871 | -14.32396 | -44.68107 | 2025-10-11 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0e95839-f9eb-32ef-a449-38e0c81c3275 | -13.21037 | -42.34978 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 20.6 |
| e53d3928-83c7-3f3b-b26c-c87adfa7e8f2 | -13.22064 | -42.34378 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 41.4 |
| bf103001-9f33-3624-bd5c-8809dffd1aa1 | -13.46188 | -47.7072 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bc05ac5a-bdea-3bb9-b450-c46605ceb619 | -13.30225 | -48.49992 | 2025-10-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11a94d56-8cee-3ff0-af91-3512e8bc55c7 | -13.39549 | -47.75002 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78175c97-bbc3-3f98-93d4-ca59d3b8b818 | -16.29957 | -47.16791 | 2025-10-11 04:34:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| df335fda-2b40-3666-9a26-4ec4ee3c051f | -13.84434 | -45.7976 | 2025-10-11 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a397ca8e-3afa-33c2-a1f4-5664799c8ed9 | -12.90347 | -47.05047 | 2025-10-11 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 93c61808-68b6-34f3-a8b9-d15c23444f3e | -15.70632 | -48.3987 | 2025-10-11 04:34:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5926ba7e-c0bf-3381-a5e5-3d7401279a58 | -14.65601 | -56.21174 | 2025-10-11 04:34:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91c5cf51-ccfd-3732-a732-fca1209f21e3 | -10.19788 | -44.61216 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 505975b8-6c5d-3ef4-aa01-75daad26a993 | -11.76063 | -43.31232 | 2025-10-11 04:34:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c18cedc-5b59-3e8a-abc5-ade80b36e307 | -15.0651 | -46.59983 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d985f63-3118-3665-82eb-bfe5b19f28bb | -11.76539 | -45.04236 | 2025-10-11 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 558b50eb-55e5-3aa1-988a-609af22535a8 | -11.62336 | -55.01433 | 2025-10-11 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b36a3408-12d8-353d-a7ff-204c4306773e | -12.74105 | -48.65512 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9f27569-334f-3b5a-98d4-8d6634ec74b0 | -15.54394 | -47.91295 | 2025-10-11 04:34:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6475c8b1-f180-3e3b-948e-79e1a26bacf2 | -15.60739 | -42.67526 | 2025-10-11 04:34:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1afc7ee3-1065-3c36-b074-d777e9030bcf | -12.71505 | -44.94217 | 2025-10-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8b9e8891-c3ab-36a0-935c-66c43a805c89 | -11.91237 | -44.17435 | 2025-10-11 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 77f65450-90d5-3ca1-a858-1654b30593cf | -12.90457 | -47.04296 | 2025-10-11 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README25.md)
