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
| 13dc7732-29b7-3821-90c5-3144ff56a70b | -15.60849 | -45.92157 | 2025-10-24 03:49:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5dbba1cc-4566-355b-a00e-f3da02c9d3b8 | -9.86026 | -44.89984 | 2025-10-24 03:49:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 057c0b2d-fe8e-3579-af70-06e7f2d5f1bb | -3.12604 | -49.10737 | 2025-10-24 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3cbd3c90-a221-3b56-9342-2aae232adcf6 | -13.90402 | -48.38889 | 2025-10-24 03:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e182d660-7599-3e2f-bbe8-45e192eed78d | -15.83728 | -49.08588 | 2025-10-24 03:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f00e787e-cce8-3803-9158-727c0a16c28a | -5.38616 | -41.55584 | 2025-10-24 03:49:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 98e3bcc3-c201-3e77-a535-35243a01b341 | -14.27445 | -48.13205 | 2025-10-24 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7f2c085-1d6b-3269-94be-cef91d1bafce | -12.81059 | -48.62838 | 2025-10-24 03:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f69057f-db22-3141-bd31-c5b51d7bb661 | -14.75728 | -46.60536 | 2025-10-24 03:49:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e7fb3780-0e61-3149-bc7d-8a906a14470d | -4.31537 | -48.23416 | 2025-10-24 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 821682d2-ba50-3d43-821c-38f3a393a2ba | -5.55439 | -41.34824 | 2025-10-24 03:49:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4885e83f-4195-382f-a52c-19bb53dfe4ff | -4.98998 | -39.87741 | 2025-10-24 03:49:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7dd93b6b-54cf-3c14-a61f-de3ddbea13a5 | -16.31278 | -46.57493 | 2025-10-24 03:49:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7c0c222-4bca-3161-beeb-9195097ff56a | -5.82282 | -40.80537 | 2025-10-24 03:49:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| fc924825-2452-38a1-bfc9-b590c1b0be45 | -10.65715 | -44.72325 | 2025-10-24 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 05e64015-a663-39ee-a580-c91fd8cfb093 | -4.15802 | -46.79059 | 2025-10-24 03:49:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33ed7fdb-2b48-3eb1-87fe-ba08637c5527 | -9.60076 | -46.91993 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| d49e7b17-5056-3138-b353-15677da88608 | -5.43451 | -40.87889 | 2025-10-24 03:49:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e003484e-968f-3d34-b0a8-de42d7535192 | -11.97853 | -49.18238 | 2025-10-24 03:49:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 86931d91-a8bf-3aab-b96b-afa1f27de7b6 | -10.88854 | -46.06877 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 214f5641-99e0-3c06-a9a3-fdcdb63bad4d | -12.82648 | -48.66719 | 2025-10-24 03:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 46a6da09-8f9b-3b24-bcfe-17fd8992c731 | -12.22692 | -43.3069 | 2025-10-24 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02a2a396-87c5-3150-92a8-cc3b04bba87d | -15.61202 | -45.92766 | 2025-10-24 03:49:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a0bf7bd-e9bd-37dc-aa1a-4373f3eff180 | -13.2881 | -47.48228 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e8057153-129f-3558-b5aa-49b41cb83da4 | -12.17856 | -43.60712 | 2025-10-24 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b1917e7-4112-3bad-a152-e1668919929a | -15.57533 | -47.71724 | 2025-10-24 03:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6a12301-43a9-3747-9b2b-32b6de20ae3d | -9.60525 | -46.8657 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0d5132d4-73ab-3854-9a18-643d78007c26 | -10.59091 | -49.64733 | 2025-10-24 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5c1aa7f9-1437-3f60-aaad-89072f1dfbe1 | -10.89433 | -43.82618 | 2025-10-24 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0048a00e-7847-3afc-ad13-c6af468476db | -4.06022 | -38.23352 | 2025-10-24 03:49:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f4403e25-254e-33f9-876d-bf4018e37742 | -12.1563 | -47.01844 | 2025-10-24 03:49:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 76019f3c-4575-367b-8391-e9f6b6022693 | -2.82125 | -49.14363 | 2025-10-24 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb8411f5-5ce5-3d48-9be2-174f31af5055 | -13.08348 | -47.55891 | 2025-10-24 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd3c9e5b-d32f-383f-bb04-3eff752ae329 | -5.5424 | -41.37123 | 2025-10-24 03:49:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 033c0b0f-825c-35af-9eeb-f018c4ea1c3c | -10.88039 | -45.0799 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd4ca8b6-2877-3a3b-9ca6-191cd1263040 | -15.5782 | -47.71655 | 2025-10-24 03:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d885cfbc-a7fa-38f9-9c72-54e07a0de22b | -4.78538 | -37.75478 | 2025-10-24 03:49:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 24996b01-3b9b-3149-942b-90a2acebb25c | -9.60884 | -46.90639 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8cb083ac-9cc1-3c00-8680-fbd2816e5f30 | -3.70294 | -40.42588 | 2025-10-24 03:49:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 39934458-fa44-3d2e-ae0f-8e7e0b289c7b | -12.83237 | -48.63766 | 2025-10-24 03:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7517e4f0-faf7-3269-81b3-7dfef9190eb2 | -11.05402 | -45.3974 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b8074e69-5c1e-3810-9440-8380be067716 | -13.3538 | -47.96996 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 33431625-3e18-3cad-9472-4ef0905a844d | -13.35081 | -47.97603 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9e24cc9d-0b9a-3270-ba85-59016594eb68 | -4.8508 | -42.95621 | 2025-10-24 03:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b0073a6b-94f3-3d80-a941-3d7ffc0b9477 | -3.92876 | -47.69574 | 2025-10-24 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b2ab090-a82c-306f-a9f6-0ed06dda7130 | -10.96091 | -45.07637 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23e50c0c-58e2-3953-bb5a-37a668c19dd5 | -9.26862 | -46.46079 | 2025-10-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbca64bc-8a3f-3b0b-8ec1-8b86a947496e | -15.44404 | -48.57788 | 2025-10-24 03:49:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c959fe1b-28fa-3623-ac94-e72e42881755 | -11.46057 | -43.70456 | 2025-10-24 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85d60e7c-6842-3d24-b635-e64c877376c2 | -5.58383 | -37.28785 | 2025-10-24 03:49:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a717087a-73a6-3551-87e7-07ea8eedc671 | -5.54695 | -41.36844 | 2025-10-24 03:49:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fb5ca30e-eb08-35f1-8a46-bcf38a7059c6 | -12.27956 | -43.82361 | 2025-10-24 03:49:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21b094ac-c8a0-3889-b269-52b36a50bce7 | -15.35729 | -48.09464 | 2025-10-24 03:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 986a72e9-66e6-3bc5-a65b-01dd4828f3de | -14.51212 | -48.34947 | 2025-10-24 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5319a297-6c8c-3f37-87e6-a26f5b12c6ce | -11.34538 | -45.89857 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22bcfc50-be11-3213-9390-df3de5300b52 | -13.90888 | -48.39413 | 2025-10-24 03:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddac9363-3d2e-3256-a577-f1def65ec180 | -9.87057 | -44.89635 | 2025-10-24 03:49:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4188bcb-d9d9-363a-8e9b-e31d67d39bea | -13.33021 | -47.96658 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f45445c1-5c58-3527-bb7a-21c25db85588 | -12.01696 | -43.88158 | 2025-10-24 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2bb93a9-4745-34a0-9f8f-6b9330864c74 | -3.7037 | -40.42111 | 2025-10-24 03:49:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a247f78e-7b3f-36e6-8848-26c57e01d5e5 | -15.95563 | -49.60287 | 2025-10-24 03:49:00 | NOAA-21 | ITAGUARI | GOIÁS | Brasil | 5210562 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4bf1e911-bc0d-335b-9103-30a650816864 | -11.36126 | -45.94853 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c2302cee-c4c5-3f38-9344-9491575d980f | -12.07133 | -46.62992 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c4e7bdd-6b26-332d-83e2-ea0ec8af6dff | -4.45906 | -43.23761 | 2025-10-24 03:49:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| e3ded77e-d61e-3bba-8874-a6d60392a9e0 | -10.27378 | -47.88223 | 2025-10-24 03:49:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce64b950-d800-39c0-92a3-1d3667b61f7f | -5.04155 | -41.94556 | 2025-10-24 03:49:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b17fcc4f-e09f-37eb-8d69-35b0426a7432 | -12.80934 | -48.66404 | 2025-10-24 03:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 769d2b86-976b-3abb-82aa-b7c45447c8c4 | -9.30751 | -45.20676 | 2025-10-24 03:49:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cf0e70fa-db4e-339a-8e61-c4674347d4f9 | -3.76631 | -40.78483 | 2025-10-24 03:49:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4b3c7ebf-b86a-3b64-8ff4-d164016e9655 | -14.77473 | -44.97104 | 2025-10-24 03:49:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5082b2a5-469e-3eaf-97be-3da31c6bbcf1 | -12.17645 | -46.56339 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d670775a-c67b-33cc-95ca-0d5e6bfdd92c | -9.64549 | -46.88872 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dff47712-2353-3c07-b776-2707c8860a26 | -3.12642 | -49.10019 | 2025-10-24 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 03895189-2c63-3fa2-b2c8-5ece7c5d5ce4 | -15.5194 | -50.01084 | 2025-10-24 03:49:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2dd4e7fc-76d9-3a77-ad0a-f03ea311df23 | -4.15907 | -46.7897 | 2025-10-24 03:49:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0036c3df-4610-3418-8b73-d43fc9978b95 | -11.78269 | -44.23581 | 2025-10-24 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f59b57e-0981-366c-9845-5135de6cc6a6 | -10.63125 | -48.07956 | 2025-10-24 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bc989f72-ff2b-386e-b7dd-90f3173e3f51 | -5.42595 | -40.8827 | 2025-10-24 03:49:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 477e9ebe-c1ee-3618-8dc1-a4d8a4ec1886 | -13.2515 | -47.88308 | 2025-10-24 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c2ff1cb-addb-38ef-be84-14932a117a62 | -13.19585 | -47.75655 | 2025-10-24 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e4eea08-a9f4-3ab4-a81d-957f16d925bb | -3.11916 | -49.10638 | 2025-10-24 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b95dd66-99b9-35a2-9988-de4ce952bd7e | -10.65631 | -44.72797 | 2025-10-24 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8b02378f-d872-3933-89f6-11de34d79274 | -12.73513 | -46.34495 | 2025-10-24 03:49:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1391b170-5909-3a26-976a-9f308b5d8e66 | -13.35294 | -47.965 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b4e09739-6c12-34f6-8285-9dad0d35c81a | -12.08009 | -46.41608 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8bfb72b3-c4f1-3432-b47b-4e5ebc30b9f0 | -9.5987 | -46.90096 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2ef31f80-3da3-3f2b-bc34-28a34bd409b4 | -15.83915 | -49.10448 | 2025-10-24 03:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 70258105-195a-31ef-966c-7927a21e96e1 | -14.47871 | -47.91804 | 2025-10-24 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 899f1839-e5a2-3f47-8bf2-ebb21b5a8940 | -16.37254 | -47.41528 | 2025-10-24 03:49:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4f81d210-b9ae-30e9-a352-9776dc289e1d | -10.01131 | -47.10014 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8cede4ab-c46f-3ab5-bd3a-f474657087cd | -15.82905 | -45.65363 | 2025-10-24 03:49:00 | NOAA-21 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fa0a2be-e938-3a21-800b-8fa7c139453f | -12.26435 | -47.45022 | 2025-10-24 03:49:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2fc3343-b75e-3c5d-b91b-76f702b34591 | -11.98924 | -43.3243 | 2025-10-24 03:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 01141d3d-e911-3e83-81e0-8a257376e9e2 | -9.64204 | -46.89019 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e5b11cd-d584-34ab-801f-bc9c3cd887a6 | -3.03081 | -49.49421 | 2025-10-24 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7cc9929-2de1-3483-81c7-37fc2fed0947 | -2.47355 | -49.22295 | 2025-10-24 03:49:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a70c6fb4-6074-3b14-bb88-d4feba803ce2 | -10.888 | -46.07165 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10bf9a0c-c66f-378f-9485-8d0125ef3f10 | -13.34842 | -47.96881 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2f8adafc-1134-3af9-83be-839214410ed9 | -13.90864 | -48.39421 | 2025-10-24 03:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 901fdf7b-60e0-3bf7-9010-e3437c4ccec7 | -9.8711 | -47.72492 | 2025-10-24 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README8.md)
