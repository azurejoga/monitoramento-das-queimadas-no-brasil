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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18b5fdc0-2179-3665-a1d7-18eb62d06001 | -13.42734 | -47.36636 | 2025-10-29 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b861fab8-efba-3256-8749-5ea8659c760a | -7.79834 | -46.43 | 2025-10-29 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 9c74fd57-20d0-3fdf-a902-116f235a56f9 | -9.53515 | -46.93018 | 2025-10-29 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 5f5defd6-c003-3801-bcdf-0b5b3d224666 | -9.28122 | -45.23144 | 2025-10-29 12:19:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 207e3c67-712c-3b10-8a84-b6775dc12baf | -10.65358 | -47.89339 | 2025-10-29 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4ae611b2-f147-3d38-ab98-4ea4f0c6427e | -10.48106 | -47.48565 | 2025-10-29 12:19:00 | TERRA_M-T | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ada3ba10-227b-330f-bfaf-8b57d42416c3 | -13.81788 | -41.68786 | 2025-10-29 12:19:00 | TERRA_M-T | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 36.9 |
| d1b94ea2-b04d-3a91-83aa-b68485883c5b | -8.65605 | -47.21243 | 2025-10-29 12:19:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 61f89624-501e-3892-b061-f7f169784958 | -15.66066 | -41.30216 | 2025-10-29 12:19:00 | TERRA_M-T | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 31.0 |
| c08b3680-5429-3469-b100-ce2dd94e25bd | -9.53383 | -46.93954 | 2025-10-29 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2df9c889-da20-3e3d-b140-e284c01f9c65 | -8.04937 | -45.03733 | 2025-10-29 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 35ed0058-786a-3d9f-a192-a5efbb8162e8 | -10.92618 | -47.59815 | 2025-10-29 12:19:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 0dc2b68b-a1ec-3b92-a25b-7470fd332e01 | -7.37845 | -47.63536 | 2025-10-29 12:19:00 | TERRA_M-T | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 85cbde0b-7181-37b5-aa08-075b666a89fb | -9.48688 | -47.34395 | 2025-10-29 12:19:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7254a889-f72d-3c85-99e8-dfd365793ed7 | -7.36083 | -47.63289 | 2025-10-29 12:19:00 | TERRA_M-T | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8a60897c-8938-3e89-899e-d8fb97214991 | -14.8893 | -46.76629 | 2025-10-29 12:19:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e9e034f8-6ce9-3e26-baef-c97563633a0f | -12.16703 | -46.55629 | 2025-10-29 12:19:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 11f0b3ab-37fe-305f-9331-5d8bf26d2162 | -13.64923 | -47.02151 | 2025-10-29 12:19:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 74fd7e08-332b-3c8e-a064-fae6fe27ec4a | -13.3592 | -47.38613 | 2025-10-29 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 67595c3f-fc32-3207-a4a2-0572bdf42e1a | -8.25448 | -46.92754 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 78a38463-dc97-36b5-9fed-e4c76b7bad0d | -13.72193 | -48.76181 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 033f1f59-9c5c-39fd-8bf6-df11b2a9acdf | -15.12856 | -48.52393 | 2025-10-29 12:19:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f696a275-d52d-3742-bbbf-2120836d3955 | -8.6961 | -47.1313 | 2025-10-29 12:19:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| fc651631-94ff-32fb-8519-088bf7c35301 | -13.70786 | -47.66749 | 2025-10-29 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1c9479be-56f9-3598-8ae5-aa1873387f7f | -10.22539 | -45.94647 | 2025-10-29 12:19:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 8804e64b-1a80-3963-91e3-48d22a381102 | -9.80378 | -46.98616 | 2025-10-29 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| a4cdf683-4d7e-32e5-8913-1e367753d6ec | -13.72322 | -48.75268 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 65eda89d-d449-3b33-9705-9aad63657b6b | -15.10919 | -47.9278 | 2025-10-29 12:19:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 2d1a3328-8799-3700-af65-1b30c32569db | -16.86499 | -47.59498 | 2025-10-29 12:19:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8af40f37-90bd-3d5d-8fc5-63d74eb0ed5d | -8.00294 | -46.67986 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| e29b082b-c77e-3176-b202-09044e3adb79 | -13.37352 | -47.41829 | 2025-10-29 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9793ccb6-f933-3354-b0d4-1830141378d6 | -13.56989 | -47.3279 | 2025-10-29 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c2bc3352-951a-3502-b0f8-a0f2e550eced | -10.92491 | -47.67252 | 2025-10-29 12:19:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 57f4ecdc-dcab-3f2e-b11e-ca9913568ae5 | -10.66607 | -47.99616 | 2025-10-29 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| a94067a4-161c-3c33-b10d-cabfcdf07876 | -14.27823 | -47.3247 | 2025-10-29 12:19:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 7d1f3d2f-cf35-3145-8d89-30cacab97d05 | -10.38634 | -47.56896 | 2025-10-29 12:19:00 | TERRA_M-T | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e68f2fef-d73b-3fed-8ac6-3faa7c25f726 | -11.03854 | -47.84344 | 2025-10-29 12:19:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c12a3c98-65ca-33b0-bf0e-4e36d512b0f1 | -14.60688 | -48.43097 | 2025-10-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9637d7ce-3769-32a7-9c21-beaf984b0ce8 | -7.96937 | -46.72248 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 0056b1d3-d23d-3c1c-8a6c-7639c962f843 | -15.15664 | -47.23011 | 2025-10-29 12:19:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 9491691a-c789-3c75-b01b-99d0be878b4c | -15.65718 | -41.32418 | 2025-10-29 12:19:00 | TERRA_M-T | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 29.6 |
| 591fab11-45d4-3bc4-a7d9-7a6c6680fc68 | -7.7905 | -46.48625 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 82137133-d9d3-3b5f-bb5f-3a40de10133b | -13.71642 | -43.46484 | 2025-10-29 12:19:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 20577924-3a22-312f-adb1-4381150c4439 | -10.91031 | -41.39722 | 2025-10-29 12:19:00 | TERRA_M-T | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 751fe292-fc08-32c5-ab87-cde823db2e14 | -11.28959 | -47.56442 | 2025-10-29 12:19:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 9c23802c-db55-337d-a106-a34d04c35a6d | -13.92111 | -48.45227 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1d2cdf53-8b01-3f64-8907-331961fb6fb3 | -12.705 | -46.30163 | 2025-10-29 12:19:00 | TERRA_M-T | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| f93ce3b4-f66a-3388-ae0b-d263b35c39cb | -8.06057 | -45.04466 | 2025-10-29 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 63ac5ffd-06bb-3c13-9437-d6b3d177e26a | -8.33515 | -46.15326 | 2025-10-29 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f634fc85-5597-3df0-b032-cd3ca082c0e1 | -12.8559 | -48.62053 | 2025-10-29 12:19:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| cd9514ab-173b-3b4a-ad2c-50112507860e | -12.18063 | -46.71071 | 2025-10-29 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 6fdd1476-946b-33e6-b907-ed854e6b4b57 | -7.79296 | -45.94129 | 2025-10-29 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 85697675-b5e9-3c24-b952-9d3b7510ceb6 | -8.69482 | -47.14045 | 2025-10-29 12:19:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 8be79053-4b1c-3cf1-a56d-da8b83641521 | -7.80349 | -46.45943 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 320.4 |
| 64c4a50b-ddca-36dc-8ba7-68cf6c923802 | -7.80218 | -46.46877 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 151.7 |
| bd50713c-5523-3861-a86f-03ca3b01c800 | -12.02515 | -49.83607 | 2025-10-29 12:19:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 44eeb976-88a5-3601-a807-095786dcaa23 | -10.87514 | -47.43409 | 2025-10-29 12:19:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f2fc31f0-8ca7-30e7-97fa-4c929d3f72c4 | -11.23114 | -51.69413 | 2025-10-29 12:19:00 | TERRA_M-T | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 081d489e-b4f0-38be-880d-b190d6cd7a48 | -13.32727 | -47.88957 | 2025-10-29 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 8be89aad-c8da-3036-9a7f-87bacfbc9634 | -12.54208 | -49.58125 | 2025-10-29 12:19:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| b037dc00-e626-3c74-838e-f36cf7e1b9b0 | -15.45544 | -43.64503 | 2025-10-29 12:19:00 | TERRA_M-T | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 24.4 |
| d1857bd7-59c3-3d27-b0ab-af0b9fa779a8 | -14.31479 | -48.01039 | 2025-10-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| db96df1e-ba2b-3508-9276-030d95bb5580 | -13.40746 | -48.37564 | 2025-10-29 12:19:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 7fc4f042-ca76-3b82-bb44-5eb852d4c005 | -13.72065 | -48.77091 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 30.5 |
| b6081d07-0f46-385a-bdbc-e62ce8bcad18 | -15.48752 | -43.72953 | 2025-10-29 12:19:00 | TERRA_M-T | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 36.8 |
| db853825-f9bd-3c6d-8a92-11935c463cb9 | -8.19191 | -44.44707 | 2025-10-29 12:19:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| c1b0c86b-6ff3-372e-8d6f-8d95e0e46d71 | -12.72875 | -42.01568 | 2025-10-29 12:19:00 | TERRA_M-T | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 63.4 |
| ba8566e5-d9cb-3e65-be90-77c210015bd0 | -8.05225 | -45.03211 | 2025-10-29 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 86b798d9-7180-36eb-a233-19d4bca31d40 | -8.16188 | -45.48189 | 2025-10-29 12:19:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d93c3c08-3b65-3ce0-a563-61f01c8796a3 | -14.46636 | -48.31266 | 2025-10-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 8bb7f212-f440-311e-966b-7faa2d4233cb | -7.96546 | -46.75017 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| dcedc3ac-d5f7-3750-b287-7b99ea10084f | -9.81076 | -47.00274 | 2025-10-29 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 28fab6ef-cb8b-3a15-886f-0ceb9a5f42d6 | -13.54303 | -47.12578 | 2025-10-29 12:19:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2ae53f15-f8e5-3ea5-8661-127f73c5f666 | -9.90497 | -44.92022 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 1db4f392-7ada-3aab-83af-ef8f24720c83 | -7.79312 | -46.46748 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 38ff8fb2-c8f2-303e-ab26-5646f4f7f2dd | -16.35328 | -43.09783 | 2025-10-29 12:19:00 | TERRA_M-T | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 8edd9f21-f6ed-3d23-b67d-61d2f419c7f5 | -10.21599 | -45.94432 | 2025-10-29 12:19:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| d040ee0c-223f-3f61-a545-90def332a865 | -7.49752 | -46.27678 | 2025-10-29 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| fe250a8c-c79a-3008-8181-e9d97d46f7cd | -12.71323 | -46.31342 | 2025-10-29 12:19:00 | TERRA_M-T | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 686b0057-9195-3157-9b2a-15171ad70ce6 | -8.9521 | -45.09367 | 2025-10-29 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 50b78288-ccda-3cb5-b735-b0b12e71a3f8 | -7.96807 | -46.73172 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 13dbb955-3e04-3fe1-91a0-494e06d5a6bb | -9.2797 | -47.04377 | 2025-10-29 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 55c1eee3-0b0f-39af-a62c-a4a450868fbc | -13.24423 | -46.54218 | 2025-10-29 12:19:00 | TERRA_M-T | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 45.9 |
| c92e49cf-d719-3aaa-8b4a-254c574832fd | -11.88822 | -48.09954 | 2025-10-29 12:19:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| f362df7a-7556-3918-9053-242d77ac3579 | -10.77478 | -47.87999 | 2025-10-29 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| efc6a0fe-a902-39a2-9887-5e1729cc921d | -11.40969 | -47.76218 | 2025-10-29 12:19:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 169ffdb1-69b1-318f-8f80-d94f57849f43 | -8.02956 | -47.40845 | 2025-10-29 12:19:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 49aa8928-1ea5-32f8-9019-a31390e97b2f | -13.32446 | -47.44469 | 2025-10-29 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3ee468e7-df07-34b8-98ee-f3b5424d6c16 | -9.48815 | -47.33484 | 2025-10-29 12:19:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f789010f-6624-386e-aa35-a5003e071ef4 | -14.48197 | -45.5918 | 2025-10-29 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 82c6a76d-110a-3fc4-9be9-089ce2b74519 | -9.23097 | -46.33718 | 2025-10-29 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| cebc275b-5d72-3849-bb91-07941eb92724 | -13.06627 | -43.03006 | 2025-10-29 12:19:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 168.4 |
| 92dae2fa-3c21-3b1b-8094-a6a25da1b37e | -13.0383 | -47.5821 | 2025-10-29 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c72acfc1-8e09-3196-a369-9bf9db31dd43 | -14.23522 | -48.11826 | 2025-10-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 54447a80-2dcc-3732-8ba3-868d86c943f7 | -10.11308 | -46.61946 | 2025-10-29 12:19:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 219.0 |
| 9aab8d99-b400-3611-8da5-2cff37bc8efd | -15.06645 | -48.76421 | 2025-10-29 12:19:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| ce641f17-4355-3419-ad4b-24d4837db53f | -12.1437 | -45.21469 | 2025-10-29 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 800f5712-ee87-3481-ba3b-8547b6f23aa7 | -13.6249 | -46.52002 | 2025-10-29 12:19:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| fb65ab14-d008-361f-8a0f-cf2ff016653f | -11.57265 | -49.58868 | 2025-10-29 12:19:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| cb6a3e58-4c56-3298-871b-3274e5ad8309 | -14.4992 | -47.87387 | 2025-10-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |


[Clique aqui para ver as próximas entradas](README83.md)
