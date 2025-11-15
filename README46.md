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
| 501c7dbe-3b35-3df6-b528-fec1e244229a | -11.91995 | -46.19098 | 2025-11-15 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d30a183b-619b-37f2-b000-18be27a289dc | -12.99609 | -43.81055 | 2025-11-15 04:27:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b302774-1566-3607-9296-589241222619 | -10.69925 | -44.50895 | 2025-11-15 04:27:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18006f13-f534-3b62-a41e-73bfb2f0b017 | -10.66687 | -44.48349 | 2025-11-15 04:27:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae5acd8c-ac54-3a85-bf5e-e742626c2da7 | -10.88453 | -54.14054 | 2025-11-15 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a263623-7f79-34d6-9e6c-f8462760b864 | -17.29304 | -46.82539 | 2025-11-15 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fca5d471-639d-38c0-9761-6cf6b803a06b | -10.93679 | -48.70316 | 2025-11-15 04:27:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d1c5b4a-a94d-3876-96e0-c28f15e11ed2 | -12.65904 | -46.75251 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5a3404b9-0fa9-3eca-a7b4-156d894fc69d | -10.2545 | -47.08064 | 2025-11-15 04:27:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0a641ca-1d94-3ddb-893f-fd033b4fe24b | -12.75701 | -43.6461 | 2025-11-15 04:27:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 614a04ea-3920-3998-aec1-812af8b3f2b8 | -9.66796 | -48.71368 | 2025-11-15 04:27:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a62f1c67-deb2-31b1-9a4a-d1492f82563f | -14.8553 | -52.85395 | 2025-11-15 04:27:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2b4aec5-e561-3a52-96e8-37fa10485148 | -10.62339 | -47.90464 | 2025-11-15 04:27:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e4194ea-dd9a-3d2a-a9be-412902e7f8e9 | -12.15562 | -46.6732 | 2025-11-15 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5e9f29a7-a8ef-3926-9ba0-b11a689844c6 | -11.32655 | -48.52265 | 2025-11-15 04:27:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2bc6985-6470-38bf-9d6c-df716b8b4f05 | -14.68801 | -46.61054 | 2025-11-15 04:27:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8fb9f45-ca4c-3132-85e8-1206c6b70f12 | -12.8514 | -46.43195 | 2025-11-15 04:27:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c651673d-5abe-34af-ab82-9635f426b2f2 | -11.85055 | -49.21125 | 2025-11-15 04:27:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 28ab3804-2fce-307b-8666-cb6440bad790 | -11.47174 | -41.98915 | 2025-11-15 04:27:00 | NOAA-20 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| afe6e2fb-2e94-32b9-bb44-c9fcc1181c4b | -11.16513 | -47.44622 | 2025-11-15 04:27:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0fe656c4-ba21-357d-aa79-e5f51b8499df | -12.72915 | -43.89761 | 2025-11-15 04:27:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c4bd8f1-a9f6-3397-8468-10caccbad22e | -10.35068 | -48.9193 | 2025-11-15 04:27:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6d630d78-f44d-334c-9805-595a1427730f | -14.68745 | -46.61425 | 2025-11-15 04:27:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 110e318c-e94a-39b7-bc31-78ea7ed6a68c | -13.48522 | -46.71676 | 2025-11-15 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 491a4bd1-44f4-36f8-9765-faa555dbab40 | -10.70926 | -44.5145 | 2025-11-15 04:27:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cbaf9836-319f-30f8-bd33-5aa2c6509431 | -10.53383 | -47.93315 | 2025-11-15 04:27:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e19e1958-8381-3574-9ce8-9ad8a7062d31 | -12.40865 | -48.11 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 816acd43-756b-3bd1-801d-4205aa008629 | -10.92945 | -48.70584 | 2025-11-15 04:27:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 099446ab-961f-3df9-94de-afedc76893fd | -12.8447 | -46.43082 | 2025-11-15 04:27:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8e58b10-fd20-337e-972d-3b8382504b94 | -12.15173 | -46.67624 | 2025-11-15 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2f6c3e4-3a8d-3923-bf5f-b428131dae7f | -12.84414 | -46.43447 | 2025-11-15 04:27:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 328e59bf-5b69-3f4b-a33f-98c515d237c1 | -11.84317 | -49.21381 | 2025-11-15 04:27:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 7c2f9833-6889-3c19-947c-3b99c0e705d9 | -12.67182 | -46.75824 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e46b89a1-15ac-36fe-aa23-668a49f8a018 | -10.57033 | -44.81319 | 2025-11-15 04:27:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b172aba6-fc6b-3db9-8249-065fcdd336f9 | -10.34722 | -45.10667 | 2025-11-15 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc7b7f65-cc06-3f46-83a8-25c9f012b857 | -17.24917 | -42.66519 | 2025-11-15 04:27:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a1d7e464-a00d-30a4-ada3-5f47889908df | -14.84735 | -50.09447 | 2025-11-15 04:27:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b936b02b-7b26-32ef-9c32-50a1e50b4a02 | -11.16659 | -48.14211 | 2025-11-15 04:27:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ef341b15-9757-3d65-a5be-e9857451d78e | -13.37293 | -48.52014 | 2025-11-15 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4814ccc-1e80-3ea3-95b5-188d9f01912f | -11.84656 | -49.21437 | 2025-11-15 04:27:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 712b460c-edf0-386a-8f71-3751009fce03 | -12.67515 | -46.75877 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f3dd6e8-ea3d-37de-ad7e-e0f935492bc6 | -16.97814 | -50.60579 | 2025-11-15 04:27:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95e241e0-d840-37d7-815a-9b5fb5864e24 | -16.97792 | -50.60649 | 2025-11-15 04:27:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4cc70ab9-f760-31af-856a-5723a8ca2108 | -10.70518 | -44.49334 | 2025-11-15 04:27:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 295fd8b1-8201-3386-97b2-c237c3edad67 | -12.87809 | -50.15582 | 2025-11-15 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3dafeb6a-347a-3527-ba9a-4bb81acebec3 | -10.99667 | -47.60882 | 2025-11-15 04:27:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 114a1ad7-17c9-328f-9bc7-d28a3fc60fe3 | -12.66793 | -46.76129 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16fcc63e-46a0-38b8-926d-02cacd6af9d8 | -14.92604 | -47.3682 | 2025-11-15 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f96dc16-2133-3e0c-a72f-ef76eaf0a044 | -13.35224 | -43.74982 | 2025-11-15 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 269df9dd-30e4-399c-ab30-b3ca7b26cf3d | -12.77729 | -46.95498 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db7df7e2-e3aa-3b0d-a21b-c5297fa62fe0 | -14.9521 | -47.50862 | 2025-11-15 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6a9c2d04-e534-369c-b67f-16bd571f4583 | -12.42239 | -48.13038 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5551715b-6118-31ab-9155-51b3511652fa | -12.67071 | -46.76541 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04a1dbb5-5503-3e13-9e05-a2932ed67c1e | -10.80603 | -45.17473 | 2025-11-15 04:27:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e10bf337-557b-3195-866a-e0cb6d2a31b2 | -12.6746 | -46.76236 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74b1bdca-c56b-3816-81ef-073198e3476b | -13.73919 | -43.62892 | 2025-11-15 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ff022bb8-bb17-3a66-ba77-15f3c0f6e629 | -16.44607 | -45.003 | 2025-11-15 04:27:00 | NOAA-20 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1663910f-78ef-35d7-a1d2-eacf7737d7e3 | -12.46359 | -43.75272 | 2025-11-15 04:27:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| afb86d0d-d6e9-3927-b81b-e3d416138784 | -12.15229 | -46.67267 | 2025-11-15 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f5675ef0-19fd-310a-992b-70003fc80d51 | -14.68857 | -46.60683 | 2025-11-15 04:27:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ad488d8-c53b-3e36-a7c8-e1752a7d52cb | -11.91638 | -46.20142 | 2025-11-15 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b391225-5113-3cbc-a7a0-262e81644813 | -9.71579 | -48.89551 | 2025-11-15 04:27:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a95f6290-768f-3aa0-add9-cbf5e9dc90d1 | -10.78204 | -48.14425 | 2025-11-15 04:27:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af4d8136-396c-3e24-9784-f48aa70fa6b3 | -14.67026 | -46.55956 | 2025-11-15 04:27:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61798481-49ce-3115-a7ec-d15971c6d994 | -12.40203 | -48.10889 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 161ceae5-8db7-3db3-af9b-6ec3192f8b26 | -15.45584 | -39.23742 | 2025-11-15 04:27:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c6d96815-db6a-36d9-9f9a-4fc094967df5 | -10.73395 | -47.38015 | 2025-11-15 04:27:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f22d3959-7f57-3fcd-b77d-8b515d2c48da | -15.35071 | -47.87097 | 2025-11-15 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5b12fe5-5f37-3828-88b4-982ca0cb98a2 | -12.39872 | -48.10834 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3392259f-8b65-316d-9761-0951aaffe75a | -12.40147 | -48.1124 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 573109e1-d8e6-33e0-adbb-8ebe65fe418a | -11.95569 | -44.85438 | 2025-11-15 04:27:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bec3ea01-c6c5-3013-840e-370a50785bdd | -12.97348 | -48.50853 | 2025-11-15 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5a0725e-70e0-307e-bcd0-306a374edb8d | -11.38212 | -43.14066 | 2025-11-15 04:27:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5c6b72eb-bed0-3357-90e5-349bc3430cb2 | -17.02308 | -43.38163 | 2025-11-15 04:27:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 66f63a4f-509b-36dd-82fe-fa6000ee4d86 | -12.7012 | -44.47919 | 2025-11-15 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dee2cd62-2026-3721-9948-dfb197b18139 | -12.6796 | -46.77417 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f076a14e-e116-324b-b4a3-cbf7cdf92b10 | -11.3643 | -46.17175 | 2025-11-15 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d764d1b-d75c-38ce-b76a-e8db3497cce3 | -17.58039 | -46.68086 | 2025-11-15 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 7efb43d3-2dbb-3e22-a7a6-55fde787d1e5 | -14.66068 | -46.57704 | 2025-11-15 04:27:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8963ccf3-1f4a-377c-821a-11d0687fafc4 | -10.83962 | -51.96301 | 2025-11-15 04:27:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c971d4d-1e74-399a-98b1-c9f1432b41b3 | -11.70745 | -48.39133 | 2025-11-15 04:27:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5fe57e5a-bc81-345f-a246-d8ff0cf05473 | -11.74364 | -45.3363 | 2025-11-15 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fcfe910-9941-38b5-9750-f131e2bcfdc9 | -12.23013 | -47.95084 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5561ad66-9897-3dd6-b69c-dca0a9aac34b | -11.32597 | -48.52625 | 2025-11-15 04:27:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 247d918d-070e-386a-bcd8-e8a90c04780e | -12.65141 | -43.25203 | 2025-11-15 04:27:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f726d12d-be12-3822-96eb-3d6722a5bd21 | -11.36765 | -46.17229 | 2025-11-15 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 209e2c54-1944-3d40-add4-e4d03fec3b19 | -11.85334 | -49.21552 | 2025-11-15 04:27:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 593345a2-38a4-3348-8c8d-70bc3485645e | -10.60695 | -44.96117 | 2025-11-15 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e41d2e9-f47a-3bb8-b8cd-5ca29fec4c76 | -17.16167 | -43.07874 | 2025-11-15 04:27:00 | NOAA-20 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c668415-57ee-3550-8fb8-f7148b11d065 | -10.34668 | -48.92244 | 2025-11-15 04:27:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 44a3493e-c5a9-3801-8868-24efdbf279bd | -14.94822 | -47.51168 | 2025-11-15 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90d9fb1b-3f4c-38e3-90d0-aa72e3193fda | -11.41157 | -48.50017 | 2025-11-15 04:27:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e896cf72-461d-351e-af1d-6563c5e2eaf7 | -11.96184 | -44.95818 | 2025-11-15 04:27:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0cee88b-4907-36c3-93e3-9c259ef3321c | -13.10841 | -43.69925 | 2025-11-15 04:27:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1fabc555-4edd-3ae4-849a-fd02b745d16c | -13.06761 | -53.95908 | 2025-11-15 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cdca87a6-3b3f-3c15-af36-6c0ad7b177f7 | -11.06727 | -44.97332 | 2025-11-15 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9800a1e0-13c7-3388-9722-934737bf4672 | -12.66849 | -46.7577 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf2a8d44-eae2-396c-9775-7c5076e88304 | -10.8727 | -44.67966 | 2025-11-15 04:27:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ffe96cd1-921f-3c46-b5e1-d932117d70a3 | -11.92111 | -46.20595 | 2025-11-15 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| d48d7d33-24c9-31cc-8ea6-adc7b61eeb83 | -10.42708 | -44.95042 | 2025-11-15 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README47.md)
