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
| 6d4beaf7-1711-32fb-aeae-8719f1e242a1 | -13.27054 | -47.30555 | 2025-11-16 03:49:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d200a27a-cd6c-3734-bedc-e09c10194326 | -14.67735 | -46.54368 | 2025-11-16 03:49:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0a4c7eed-21e2-3596-864b-89a508eba3b5 | -16.51664 | -43.54317 | 2025-11-16 03:49:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6926261-9902-38ca-b776-0cf1a1903b37 | -13.87223 | -46.84368 | 2025-11-16 03:49:00 | NPP-375D | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 975561e7-093d-3712-b3f1-832ccf58d8c5 | -15.47257 | -43.18745 | 2025-11-16 03:49:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d261d6ad-5315-3a59-9a98-b42483892ae3 | -14.66158 | -46.59455 | 2025-11-16 03:49:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 094b1484-1223-3b62-86e6-2fdffaf63ae9 | -12.8544 | -46.42076 | 2025-11-16 03:49:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c03c593-287b-3008-8233-07833bf5d322 | -11.03858 | -45.21356 | 2025-11-16 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cf4c60b-c5f3-390d-9804-97526dbedc9b | -13.97692 | -47.0501 | 2025-11-16 03:49:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8a6b69c-364d-3b41-afd8-d6777a78a97d | -14.64811 | -46.57855 | 2025-11-16 03:49:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7ee1842-91e9-3c48-98f2-5323274d881c | -12.06243 | -46.97219 | 2025-11-16 03:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 885e618b-5c84-3763-9635-c83aca3a3f8e | -11.85206 | -44.7182 | 2025-11-16 03:49:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 730c3bf1-ba58-374a-a25f-875da091bc95 | -11.97256 | -44.95441 | 2025-11-16 03:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c744bf1a-0363-335f-b2cb-577006b6c716 | -13.00252 | -43.21525 | 2025-11-16 03:49:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7cc7f1f8-e4ba-3de9-9738-b5fb0926679f | -11.84404 | -47.60342 | 2025-11-16 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c26cbff-6c3a-3be0-82a8-2c5c5dabdf50 | -13.55394 | -44.27683 | 2025-11-16 03:49:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| aa82e0a1-dfdf-3809-b6ec-04202f1bcf06 | -11.84493 | -47.59886 | 2025-11-16 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 955ab803-f914-3392-84a9-f162ce1c565b | -14.07287 | -41.26508 | 2025-11-16 03:49:00 | NPP-375D | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 27df92be-864c-34d8-bcee-8a678c71a98a | -14.15553 | -43.40385 | 2025-11-16 03:49:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7096624-abe2-30f8-b2f7-8e4c9ee041c4 | -11.91175 | -46.22189 | 2025-11-16 03:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77f3700d-9df4-3091-b6b3-d8ac471371dc | -13.82429 | -43.19268 | 2025-11-16 03:49:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d1650016-07d9-3405-8583-cbf488eb34a2 | -13.40249 | -44.14621 | 2025-11-16 03:49:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6de7431f-494f-3ae9-8c9e-44cd4c61c343 | -12.68948 | -46.79781 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6fd0fb82-f414-310f-b00f-78cda5e6dfab | -12.67577 | -47.16777 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fae17cde-d13d-3502-a72d-9c1748d5ad39 | -12.00986 | -49.27951 | 2025-11-16 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| b25856cc-1d4c-35f3-af7d-6b24e5597fbe | -10.71021 | -44.52708 | 2025-11-16 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71c28625-df93-30cd-a10c-8667e416c2a5 | -11.96346 | -44.94716 | 2025-11-16 03:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 196b35ac-d18d-3b02-8012-3915d3019881 | -12.65774 | -47.16829 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 009f4184-1433-33f4-b065-e6e86b5e1af4 | -14.6728 | -46.53875 | 2025-11-16 03:49:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6931dcac-ad81-3f32-9468-375e69ecee1b | -12.06315 | -48.21431 | 2025-11-16 03:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0ddb7b5d-788d-3130-bde9-e47e4faeae42 | -11.80635 | -45.54806 | 2025-11-16 03:49:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec688832-46b0-35b5-80a2-ce2690e0416b | -12.80925 | -46.45059 | 2025-11-16 03:49:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22d5cc34-c594-39b8-82f5-000fb88fc331 | -12.41334 | -47.54888 | 2025-11-16 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2c5aad1-846c-3c7a-b259-16d5ecdc6b18 | -11.15817 | -49.44963 | 2025-11-16 03:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6eb4a5a5-3414-35cd-9c4a-c69ccc099719 | -13.81514 | -42.55076 | 2025-11-16 03:49:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 15c5345c-f6b3-35fe-9dd0-c04c84c9dfc7 | -13.26973 | -47.30944 | 2025-11-16 03:49:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 51c181db-60a8-3413-b1e3-65b3a78198c1 | -12.79797 | -46.45 | 2025-11-16 03:49:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40617d76-b87c-35da-897f-3a080a786e5b | -11.97143 | -44.96038 | 2025-11-16 03:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ec5f090e-7aaf-3aad-bf6b-08adde92d11f | -11.99863 | -49.28302 | 2025-11-16 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| d8df9fc5-238b-35b2-a7ad-7d32843ffd25 | -12.66289 | -47.1713 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 925a6be7-8f6d-35d7-9932-6156048f431d | -12.66683 | -47.1829 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8ba01738-dbb4-3378-8a81-9eec0f4e3b95 | -11.42522 | -43.13652 | 2025-11-16 03:49:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cb2990c9-e924-3ce8-9446-b19c3063638f | -11.40931 | -43.32699 | 2025-11-16 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e2e2760-fc23-327a-a0e2-698aba258625 | -12.40564 | -47.55655 | 2025-11-16 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f5128b4-bb58-372c-82a2-ab067ba5d73b | -12.6815 | -47.16902 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2ab7caaf-9e11-3246-bf07-af2d536bed8d | -11.05929 | -45.16121 | 2025-11-16 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9d6bb724-0da2-3d72-8ff2-37aea6fc6886 | -11.8242 | -45.53497 | 2025-11-16 03:49:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d62f1b9-1862-3362-9d8b-a222d91af159 | -12.65313 | -46.74621 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0dbeb9e2-cfca-36aa-8fb8-9d970e4b53ab | -12.00646 | -49.27839 | 2025-11-16 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| ba6b22cf-5ead-319a-816b-c992c7c7d997 | -10.80372 | -47.9921 | 2025-11-16 03:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df58fe2d-3894-3683-abe0-7cef37527e91 | -12.05694 | -48.21313 | 2025-11-16 03:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9f701351-bdc6-3d0d-bb98-f637b91e1805 | -13.35586 | -43.63897 | 2025-11-16 03:49:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d2d4191-af7f-3600-a455-f3013fcb992d | -16.52971 | -43.56702 | 2025-11-16 03:49:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a36b983d-eb6c-35e3-b121-ba066c1a6966 | -13.98211 | -48.78299 | 2025-11-16 03:49:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2e5aeb9-a95d-3146-946f-c3a234924677 | -13.55577 | -44.2751 | 2025-11-16 03:49:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d6f03806-a980-3a7b-bf73-e2776277478e | -12.40388 | -47.56526 | 2025-11-16 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 318e56b7-e9b8-3532-8b5a-02e357a0f431 | -14.64199 | -46.5813 | 2025-11-16 03:49:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77090b5e-7835-343d-8301-709e5479bff9 | -11.82483 | -45.5317 | 2025-11-16 03:49:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2aa69aa5-55be-3694-861f-ac947f0e439b | -12.87298 | -46.44181 | 2025-11-16 03:49:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 017a2c75-57a0-3886-b88b-f6242debbd66 | -12.66697 | -47.18064 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 774fb72e-49e0-360a-bbad-4abe85d4eaf8 | -12.6801 | -47.17494 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bba16eb1-323a-3a1e-881b-5dcf0861fe43 | -11.1106 | -44.80477 | 2025-11-16 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1db6bb89-40b5-3f24-aaeb-608f6e47f720 | -11.10554 | -44.80376 | 2025-11-16 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 13dba5c5-9df4-3173-b160-16099a8b50b7 | -12.67927 | -47.17905 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 10168a7c-a3cb-3224-aa4f-04f0ce7e17ee | -9.70967 | -48.89985 | 2025-11-16 03:49:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56b0ee71-dcb3-3789-9d74-7a3b93e1561d | -12.87622 | -46.45428 | 2025-11-16 03:49:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ecc94d8-a9e8-3e45-841a-3eebcf9add1e | -10.70104 | -44.52554 | 2025-11-16 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6043583-465d-3fd2-b3ec-7c85fbcf3448 | -12.67991 | -47.17718 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ac15e12f-9d5c-3028-91a8-db3fa2024c19 | -12.80891 | -46.4492 | 2025-11-16 03:49:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f64e87f0-f728-3b85-89ba-3a60e7e98fb7 | -15.38272 | -39.3086 | 2025-11-16 03:49:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 87d8d500-5f93-32f3-ac61-537a75eff726 | -11.71093 | -48.39513 | 2025-11-16 03:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3355f526-53b0-3db5-9bcd-23540e21df35 | -12.7734 | -43.71165 | 2025-11-16 03:49:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 81ecf099-17ff-363c-9918-b22ba1ba711a | -12.01184 | -49.28572 | 2025-11-16 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4e75f52-08c3-3bcc-85da-d6ad27c42440 | -13.97586 | -48.78194 | 2025-11-16 03:49:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87e7c642-6904-3f34-8b1d-3ed0a0c44774 | -12.68093 | -47.17085 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 401bbe29-eae5-3790-92a8-e49de268a8f1 | -13.97542 | -47.05736 | 2025-11-16 03:49:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d411443-1a59-3768-a1f4-6d9726daf567 | -11.1601 | -47.45711 | 2025-11-16 03:49:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6059adbd-feb9-31b6-99a0-9cbcbb682115 | -11.99668 | -49.27673 | 2025-11-16 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| bddd84fd-4782-3420-b150-0eb6b9c3b3fa | -12.676 | -47.16565 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb5c618c-c962-36cb-802a-97fc3e8c83b8 | -12.86372 | -46.45997 | 2025-11-16 03:49:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59cf81cb-f5fd-3ef4-b8f6-f7175065273d | -12.04835 | -43.51212 | 2025-11-16 03:49:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 33170110-bd02-3292-a806-452fa405a75d | -11.71353 | -48.87286 | 2025-11-16 03:49:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e9613166-a894-34ad-ba40-ba83a507921b | -14.66633 | -46.54332 | 2025-11-16 03:49:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e67aa5ad-a711-3716-bdde-bc33e188a321 | -11.706 | -48.87665 | 2025-11-16 03:49:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e0450c56-1ab1-398e-a3be-73a36a6b6cba | -12.80471 | -46.4446 | 2025-11-16 03:49:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8b92d22-fc88-3e0d-9e00-de6e3f7f7cf8 | -10.54368 | -47.92677 | 2025-11-16 03:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 02b79de7-a452-3790-8d47-cfa0a8ceae06 | -10.53244 | -44.83895 | 2025-11-16 03:49:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f391a50a-c786-3432-8cb7-076e34927933 | -12.21503 | -49.55302 | 2025-11-16 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3beed29c-1a3a-39b7-a8c2-a0803de0fd1c | -11.11004 | -44.80774 | 2025-11-16 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87cbf2d6-ed13-3797-9e33-4586cbf01d45 | -10.5313 | -44.83862 | 2025-11-16 03:49:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f742c96-5907-3cbd-9fcf-fdb9518a8cce | -12.77253 | -43.71643 | 2025-11-16 03:49:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 63572d19-f702-3921-a654-89f5af4dc90f | -12.65712 | -47.17023 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a47e1f9c-fd09-3221-bb96-fce3dcd3ee79 | -10.7053 | -44.02977 | 2025-11-16 03:49:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d6f3827-3081-3e75-82c7-cc2e40be9dab | -10.84609 | -44.09852 | 2025-11-16 03:49:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7578bfdf-e5b7-3c20-94b3-76ac661478af | -14.20689 | -41.842 | 2025-11-16 03:49:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 280edd37-bf72-3387-808a-31b7888679ef | -12.80996 | -46.44694 | 2025-11-16 03:49:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd88e248-c320-388e-a2bf-3b4ad98addc7 | -12.38411 | -48.09832 | 2025-11-16 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b59b8e21-8558-3265-b5b7-adf9897b9e18 | -10.62149 | -44.58998 | 2025-11-16 03:49:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba21fc21-d5ed-3a60-b6e5-e535ab2d9b81 | -10.53304 | -44.83578 | 2025-11-16 03:49:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b522e373-3c63-3be7-b4b7-e47c2847407c | -12.39745 | -48.09539 | 2025-11-16 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README24.md)
