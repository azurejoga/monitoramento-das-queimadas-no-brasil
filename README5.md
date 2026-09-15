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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1dcc2a7-3595-32af-bdfc-ea84618ea975 | -6.1719 | -52.7202 | 2026-09-15 00:02:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bef50c34-fc15-3bd0-bc99-23cc284be857 | -11.8032 | -46.582802 | 2026-09-15 00:02:00 | METOP-B | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb01d7a4-c4ae-37a2-9ee0-452afe67c3ac | -12.0289 | -47.7924 | 2026-09-15 00:02:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ff4f4fd3-5d98-3262-aac0-2e5a8092afa9 | -6.6037 | -44.1828 | 2026-09-15 00:02:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f94be10d-60eb-3ac6-a5c6-ee8e1560b5a9 | -2.8844 | -50.391102 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 560c4794-dca4-324a-9c13-cdb138daf923 | -17.4557 | -43.624802 | 2026-09-15 00:02:00 | METOP-B | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5311dac4-c935-3392-8984-906bac87f939 | -9.5957 | -46.706402 | 2026-09-15 00:02:00 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a40fbfc-caab-369f-8631-453be4f85c57 | -11.0187 | -47.547001 | 2026-09-15 00:02:00 | METOP-B | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c088b5ea-0101-3f92-88a5-f15bcbe0397d | -18.8183 | -44.504299 | 2026-09-15 00:02:00 | METOP-B | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 89f8962e-680d-3542-9c2b-652c64d916ba | -14.1718 | -47.060398 | 2026-09-15 00:02:00 | METOP-B | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ed65b546-0438-3899-bdc8-79572a713568 | -14.1596 | -47.383301 | 2026-09-15 00:02:00 | METOP-B | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 64dd8a4d-edf0-3f95-a7e3-cde7a51b90b3 | -7.4506 | -49.740501 | 2026-09-15 00:02:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 486baa28-7340-3abc-9f16-049176ef3b75 | -6.4222 | -43.056198 | 2026-09-15 00:02:00 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c3842d2b-cb1f-3792-8775-3a7f1715bfd2 | -18.958401 | -47.283199 | 2026-09-15 00:02:00 | METOP-B | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 57ab7bb4-0a38-3721-a9ce-a37d8fc138f9 | -4.2893 | -49.0816 | 2026-09-15 00:02:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3cb74c9-2461-3db3-8805-1bf8781cfac4 | -14.6861 | -48.0214 | 2026-09-15 00:02:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ac76a591-651c-3d01-aede-5a5399c53ced | -8.7885 | -45.874001 | 2026-09-15 00:02:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b51d56cb-8cd5-3ac4-b7b5-10cfdf5e87d3 | -2.8247 | -49.210201 | 2026-09-15 00:02:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06717afc-4461-338b-a192-252a05e1cf20 | -8.1994 | -43.772598 | 2026-09-15 00:02:00 | METOP-B | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 38869a9c-711d-3069-9cd2-ff58edae53e2 | -11.1718 | -42.808998 | 2026-09-15 00:02:00 | METOP-B | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b008f73b-f21e-31ef-8755-fee170c6de2c | -5.3536 | -50.160099 | 2026-09-15 00:02:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c97b5c8-8510-39ed-b1aa-324ccef71562 | -13.2611 | -51.2598 | 2026-09-15 00:02:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 62cf8aec-a805-3689-a606-c29ba2078a51 | -8.8359 | -45.855598 | 2026-09-15 00:02:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a33fc909-f131-34bf-a21c-e325926ccdcb | -5.5895 | -48.084702 | 2026-09-15 00:02:00 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| b311f7ed-2fea-3c3f-96fb-45be6aae3e44 | -5.9656 | -49.257401 | 2026-09-15 00:02:00 | METOP-B | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e8f6b18-c081-3584-8851-04a4e3215e96 | -6.672 | -46.177399 | 2026-09-15 00:02:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b69ccaee-5181-3f23-b0a2-687ec695b1a2 | -13.5476 | -43.512299 | 2026-09-15 00:02:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f70e80c5-9f63-301c-ae61-acdc479c1785 | -9.4239 | -50.079601 | 2026-09-15 00:02:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5f59930f-0682-3d61-b8e5-1f97c5f19182 | -6.4162 | -51.205898 | 2026-09-15 00:02:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61a01fd9-e7d4-3a76-9741-c8fe042cb488 | -10.6695 | -54.091 | 2026-09-15 00:02:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 03496492-7016-30cc-aced-b69897b0c57b | -3.8599 | -51.951599 | 2026-09-15 00:02:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79796366-9455-36ee-b6ac-6e7d08856211 | -1.1109 | -49.194801 | 2026-09-15 00:02:00 | METOP-B | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9adf9603-b653-3de8-bd71-2de25751e542 | -5.9541 | -49.252399 | 2026-09-15 00:02:00 | METOP-B | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99131316-e732-3668-b331-7b777d22572c | -14.7534 | -42.926601 | 2026-09-15 00:02:00 | METOP-B | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 12287b54-6b5e-3cc4-ab4b-4aa4b7ef5747 | -5.6097 | -45.233002 | 2026-09-15 00:02:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b98ab1d3-d1fa-3e1b-b865-d7481da886ea | -5.4095 | -48.521198 | 2026-09-15 00:02:00 | METOP-B | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 5a77e2da-6d21-36ef-84c4-f478e4ea6bce | -6.148 | -55.656399 | 2026-09-15 00:02:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed7fbd28-ebf4-3c27-a8df-cb95f2e9ed41 | -2.886 | -50.398499 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb25750e-17d0-3804-9bba-27d0aa4de59d | -2.922 | -50.375198 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93c7bee5-93d7-3839-82f1-77f3fe9e2cfe | -13.6121 | -42.4263 | 2026-09-15 00:02:00 | METOP-B | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5b8569f4-f25c-3a01-8114-99efb87304cb | -7.0136 | -44.6152 | 2026-09-15 00:02:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d279d52-430c-30d1-a1fe-3f226c98d642 | -5.5997 | -43.547798 | 2026-09-15 00:02:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e5bc5e83-3864-3cc0-9b99-0d9922ca8d36 | -2.8631 | -49.6092 | 2026-09-15 00:02:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0306248f-0859-36f2-8c2e-9d6bcef0e411 | -8.5644 | -50.137798 | 2026-09-15 00:02:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f94eb4d3-e8c0-3b07-bfe2-2df28410e68f | -5.1292 | -55.886902 | 2026-09-15 00:02:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c3b1d81-1f8a-34b5-a677-233c8669b7a3 | -17.316 | -49.214901 | 2026-09-15 00:02:00 | METOP-B | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f45a2f2c-d772-3250-9bf0-7c57de5be4a3 | -7.074 | -42.109798 | 2026-09-15 00:02:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f7151e8a-7e53-3046-a8b5-4e3e9f9bac2f | -2.9138 | -50.384602 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8810029-2385-33e7-9b73-6802a1fa10d2 | -6.1578 | -55.654301 | 2026-09-15 00:02:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1001b1e3-0318-3dbb-9cd4-d68142470969 | -14.9579 | -47.514599 | 2026-09-15 00:02:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e2b6a3b2-90a9-3ffc-b392-15b602ea1b40 | -6.6057 | -44.191399 | 2026-09-15 00:02:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26d02e41-7fad-30de-b6fe-0798f045dbe1 | -15.2749 | -42.771 | 2026-09-15 00:02:00 | METOP-B | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c5c79b82-6df6-35f6-8723-1f8ae5d2ac90 | -13.3025 | -51.262501 | 2026-09-15 00:02:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ce28e3bd-07cb-3dfd-bde2-2938ac44895d | -6.3585 | -55.786301 | 2026-09-15 00:02:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d501e6c-b98a-3b41-a7ca-dab4d1c1c448 | -6.0166 | -52.146801 | 2026-09-15 00:02:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de321536-285e-3484-8ae3-ba1495dc4cb2 | -3.8619 | -51.9604 | 2026-09-15 00:02:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 083ba913-7cde-39db-8517-51518901381f | -3.4926 | -50.3498 | 2026-09-15 00:02:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a908a6f-15ad-32dd-86d2-7d7cb16db751 | -7.0878 | -45.0247 | 2026-09-15 00:02:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c995aef9-a4ba-3e9d-8f2f-9ad3622a3d80 | -10.7064 | -47.4841 | 2026-09-15 00:02:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf4a024c-20a0-342a-8730-6ba427be3b32 | -3.2334 | -50.570499 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b2abc18-eb6a-3872-88c7-29640fda7361 | -6.7157 | -48.100201 | 2026-09-15 00:02:00 | METOP-B | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 606129b1-a34f-3ae6-8941-72fbaec0b0d1 | -2.909 | -50.408798 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12e9adbb-d513-3269-82b4-6e6cb0b1825e | -8.7982 | -50.459202 | 2026-09-15 00:02:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99533042-3e1d-3483-a93b-2397af46aa64 | -10.0851 | -36.2616 | 2026-09-15 00:02:00 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1ef54c22-2972-3573-8141-ce9d45fa2fd9 | -4.1316 | -40.813599 | 2026-09-15 00:02:00 | METOP-B | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 73c33137-8d00-33da-8257-0d44ff845ba6 | -3.3949 | -50.740601 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4298e991-7445-346f-a322-c300991c858c | -7.7425 | -49.479 | 2026-09-15 00:02:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da3dce33-cb63-3d5f-8906-44e049a1586e | -8.6591 | -49.113701 | 2026-09-15 00:02:00 | METOP-B | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d7a866d-f60a-378e-8d4d-6333cd53529e | -13.43 | -43.805801 | 2026-09-15 00:02:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e214bed2-9919-3a5f-afa8-283c056a26ad | -5.4116 | -48.4846 | 2026-09-15 00:02:00 | METOP-B | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 2e5e360c-36e0-37ac-9099-ea2d95d25aa8 | -15.2613 | -42.756901 | 2026-09-15 00:02:00 | METOP-B | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6b253b97-9618-382d-bd3a-27eb16d0c2d1 | -17.3141 | -49.205502 | 2026-09-15 00:02:00 | METOP-B | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 73ee7c10-f127-326b-a30e-25628bf7b7c6 | -12.4072 | -48.114899 | 2026-09-15 00:02:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 664be978-d5ce-33a0-bab1-ff74c50686ec | -4.5401 | -55.5648 | 2026-09-15 00:02:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79851810-e257-3b07-b7e6-28903b314ba7 | -3.4828 | -50.352001 | 2026-09-15 00:02:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5297610d-0942-3f56-8c9e-9aa108984523 | -7.9557 | -43.966 | 2026-09-15 00:02:00 | METOP-B | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c5057fb3-8a30-38e0-9ab8-7ecaa3a3bb6d | -2.78 | -51.348701 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1c20840-2ca1-3c33-a390-367a4720c5de | -10.043 | -44.868 | 2026-09-15 00:02:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e39bc174-37e7-3757-a59e-40ad9981492c | -13.2152 | -51.637501 | 2026-09-15 00:02:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1084cbaf-fc02-3d04-9be8-bc9e87edcfc6 | -4.2654 | -46.518398 | 2026-09-15 00:02:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ae2f99ac-8565-3c93-9516-085088561b79 | -6.7188 | -48.113998 | 2026-09-15 00:02:00 | METOP-B | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 00d72e7a-1a2c-3824-942d-c2441b655f55 | -3.4845 | -50.359299 | 2026-09-15 00:02:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9661fea9-dc53-3bc4-85a4-60fc907edfb3 | -5.7097 | -51.8218 | 2026-09-15 00:02:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3022e2cc-a511-3443-81db-91b0fa2a407a | -5.123 | -55.9053 | 2026-09-15 00:02:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d75d1a0-1c3d-357a-8af6-da4ca8c76f0e | -15.5121 | -41.766602 | 2026-09-15 00:02:00 | METOP-B | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eb87067f-1e6a-379f-924a-956f5d942a91 | -8.8375 | -45.862701 | 2026-09-15 00:02:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 03dba8a7-d5e7-3c57-9e72-a83e3fae9186 | -0.9571 | -47.560001 | 2026-09-15 00:02:00 | METOP-B | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 471211ac-60c8-32eb-be9d-adf241a39494 | -11.1654 | -42.781898 | 2026-09-15 00:02:00 | METOP-B | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 92cf0700-8784-3ef1-90d6-580061ec711b | -14.8481 | -49.2351 | 2026-09-15 00:02:00 | METOP-B | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 13b79be6-8056-3c9e-9893-6bc11c4652f2 | -5.8055 | -53.77 | 2026-09-15 00:02:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8d4a684-d540-3417-8be6-21d80bc5562e | -7.5558 | -44.9081 | 2026-09-15 00:02:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b1b07f87-04aa-3d96-854b-057ec2a19d8b | -8.5087 | -48.478199 | 2026-09-15 00:02:00 | METOP-B | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b5826c09-f4e5-3f12-945d-30b4b3d57e10 | -8.3708 | -54.669701 | 2026-09-15 00:02:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4426c2a5-ae54-36f5-901b-ec041c27cb7c | -13.3034 | -43.7047 | 2026-09-15 00:02:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 45b89819-eb79-3740-8336-d7f018b5dcf5 | -2.8647 | -49.616199 | 2026-09-15 00:02:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 160d80aa-1a40-3caa-aa8a-acb572af183e | -12.468 | -45.871601 | 2026-09-15 00:02:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2eabbcee-61b9-35cb-bbda-39b438292c02 | -11.4988 | -45.778 | 2026-09-15 00:02:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2aed5cc2-1dac-3d2b-a9d9-e00bc9249a09 | -15.5451 | -48.796299 | 2026-09-15 00:02:00 | METOP-B | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ef1247a9-b098-35d2-9889-3a8f8561af9e | -8.8098 | -50.4655 | 2026-09-15 00:02:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c005513-dafe-30f5-8755-ca26c7b6a943 | -8.8034 | -46.893501 | 2026-09-15 00:02:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
