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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 573959f6-da0f-3f3c-aa8f-f5487fd4084f | -11.6378 | -47.76626 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e8b2708-d5c3-3f4d-9c54-5189ff8a360c | -9.46152 | -45.42989 | 2026-09-20 04:40:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 28b9ff6a-b891-3439-ad1c-0e6e97ded75e | -7.59045 | -55.68696 | 2026-09-20 04:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 542b6093-dee6-344d-add2-24ff8b8503e6 | -11.07508 | -49.49394 | 2026-09-20 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dbe80639-4284-3e37-b845-e3e23b2a0e10 | -9.05111 | -48.72166 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9bce8018-27cd-3cc5-bc73-6a3b5ab4f193 | -8.13744 | -46.8083 | 2026-09-20 04:40:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e057772b-8eba-393f-88e2-12ab3467b45e | -6.7785 | -48.65689 | 2026-09-20 04:40:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22cf3fd4-01da-395d-a151-18ee9cc95300 | -10.85695 | -56.18335 | 2026-09-20 04:40:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a60c383-a0d0-3e42-9c89-2a48641044c8 | -10.41257 | -48.33414 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5ca6177-e8c3-3b36-8c5f-c9e2fd9823ab | -9.34652 | -48.18292 | 2026-09-20 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4ec170b-48c6-3160-8cdc-18acb9134817 | -9.79716 | -48.31908 | 2026-09-20 04:40:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 421138b0-2aad-3add-94ad-e8f6b4505c5b | -12.87694 | -51.00875 | 2026-09-20 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50d4153f-fb79-3f31-80d7-81840873a874 | -11.32573 | -47.29066 | 2026-09-20 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40737043-56eb-3b02-b01a-efb4d1a15c91 | -7.88552 | -44.85123 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc81bfd5-877f-3368-82e5-4836eabdc89f | -7.75869 | -44.87935 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 39650842-6402-37f0-b71d-4121eb0e8d60 | -13.03163 | -46.91917 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 50c033eb-0269-3b7d-90c5-7de4f3e61574 | -7.27872 | -45.55694 | 2026-09-20 04:40:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ac4805c-ff80-3263-8f5e-03daca616bfc | -5.85357 | -53.55104 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7d3d34a-ec4d-34a2-80fa-7fb108e92159 | -12.12652 | -47.03347 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6bdbba83-d6af-30c6-a325-522ccccc981f | -10.30547 | -50.23931 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 3735f455-1a9c-3831-815f-90d661e91665 | -9.26375 | -46.19427 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64ff0eaa-6dba-32c1-8e5d-3deb27e08701 | -7.13621 | -47.44711 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a1ed726-b340-3ad3-a13c-10505c1692d9 | -13.23624 | -46.95175 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32995243-303c-397e-864c-d1e4a80119c0 | -11.84321 | -46.87296 | 2026-09-20 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 479de3c2-9c6d-352c-8ef9-b3f5a7fbd190 | -6.65229 | -47.73801 | 2026-09-20 04:40:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ef62cac-3872-3d8a-93be-56f2dbdf8895 | -7.75673 | -46.7091 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f701ec8d-6f83-3ba3-b3ff-9822589d1e63 | -10.37213 | -50.45475 | 2026-09-20 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb13c8ef-6b75-3cf9-b953-abbff782e8ca | -10.55296 | -46.75525 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ac8f775-596b-3939-8852-66ab191d292a | -10.90133 | -53.98281 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ae51d3f-b283-3d32-a259-18d04c540cd7 | -7.62451 | -45.42113 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a66804d-dc13-3808-a264-f60ff121b1b5 | -7.84034 | -49.22182 | 2026-09-20 04:40:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53f28e14-2f19-33f8-97e1-764a5d5fcf70 | -9.05055 | -48.72514 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f27c32f9-7022-325d-9acb-832d871735da | -11.41464 | -51.44858 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0aff76fa-239f-3226-8fb3-14916a2bacd7 | -9.39825 | -40.30639 | 2026-09-20 04:40:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ced2aa33-3d6e-3c62-89ed-3291f4a752de | -12.15838 | -47.03441 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d4537786-5947-39de-9d59-db07e6579fcd | -11.71688 | -54.55255 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d772518-906f-3b85-802b-18a531360bb4 | -11.8111 | -48.83567 | 2026-09-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd8e93e1-6a99-3a52-899e-0d15851e8af7 | -9.672 | -54.32013 | 2026-09-20 04:40:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 90ea7477-02d0-31f8-8f62-9e935b4c148f | -8.67216 | -45.33507 | 2026-09-20 04:40:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5402d66-0612-3263-bdb5-45cf45b16e02 | -9.73205 | -48.15049 | 2026-09-20 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 308addd9-7b5a-35ef-94e5-9bafed8d0876 | -9.27551 | -48.247 | 2026-09-20 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8e40252-7bbd-381d-a970-74046481da0a | -9.7239 | -47.21429 | 2026-09-20 04:40:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0deb4961-d891-363c-9ce6-c09c4797d0eb | -11.83626 | -46.84774 | 2026-09-20 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7aa302d5-3591-3889-9021-a743bf42aeba | -10.4599 | -51.28017 | 2026-09-20 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7d27828-8951-3512-b796-0a0139f3fe4b | -10.88343 | -54.06147 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53c57015-af54-3786-8e3b-9f32a908932d | -9.02242 | -48.73133 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba233d09-9960-3a47-ad0f-6c0b0a554b74 | -7.53712 | -44.93584 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0fdd62c0-4409-34f1-8d04-241653ee3a07 | -8.63031 | -47.61965 | 2026-09-20 04:40:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e45438c9-cf3f-3852-9c61-c45111071838 | -8.76899 | -48.72301 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c84e0576-5183-3ecc-8e31-abc3124b471d | -11.38212 | -51.3964 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02f6de37-0665-3dee-96eb-48407ce45f64 | -11.08885 | -48.28574 | 2026-09-20 04:40:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ed01860-61de-332f-8625-2f48a861b3a3 | -11.50088 | -47.74896 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef2c14b5-a829-3594-9142-4403ed8bcc57 | -8.46738 | -57.62738 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e90f133b-1622-3fae-97bc-665bd7e97fe1 | -9.7326 | -48.14697 | 2026-09-20 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ce9d90b-8258-38b3-9d1f-da344840a396 | -9.55212 | -46.57713 | 2026-09-20 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c565bc56-2467-31d6-8afc-cd9fa6aadbdf | -11.79006 | -49.82469 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07bf0010-2678-345d-8ecf-ef806cb15db6 | -11.47729 | -47.79019 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fed270ce-5ecc-3cbf-a158-456eebcf8aae | -12.29276 | -47.12218 | 2026-09-20 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d545a82-51ba-3650-8152-f769aa920649 | -7.1703 | -47.44494 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4eb65fdc-1df8-388c-b9a4-29a1bc2bc165 | -13.58212 | -51.46199 | 2026-09-20 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d71c9bdb-bfa5-3d0e-b4ee-b6c4aa71a136 | -10.19727 | -44.14594 | 2026-09-20 04:40:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f3c38f9-d167-388b-a666-ad2c12d9bf12 | -7.7701 | -44.0524 | 2026-09-20 04:40:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c9c1fb0b-3eb9-3bc8-8e2c-ec5ba5200c0d | -11.33829 | -47.34637 | 2026-09-20 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56a3baaf-da86-3b90-bb09-2915542bd7a4 | -11.03347 | -48.29525 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa39b1d4-cfbc-3012-a024-77bcb6672f20 | -12.13 | -47.03401 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 010ab036-d578-36ec-b80a-c29147e6b70a | -7.75488 | -49.20085 | 2026-09-20 04:40:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d61dfa20-40cc-3b8a-b135-cdde6485ab81 | -5.86932 | -52.03783 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c907d55c-1c85-371b-b786-75f6fb1a8a45 | -13.63213 | -46.95919 | 2026-09-20 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28368be8-72f5-3d35-bdaa-8c31dcf13bdc | -9.83007 | -46.44422 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9c5eddf8-e157-33ed-873e-c342789f787d | -11.02515 | -48.30481 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef5d1d43-8a74-34b7-8628-cb25b012d715 | -11.69258 | -47.73342 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 3bad6ecc-49e2-3e70-a0e2-72b136f14688 | -10.30134 | -50.2646 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90cf50fc-6ba9-3d27-af12-762944e66984 | -5.85197 | -53.53517 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b7c0e709-b090-369e-8f3d-f14dddc223a4 | -11.47162 | -47.7594 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4752a2b-fae1-3248-b12b-d6c314e6ac7c | -10.40733 | -48.92998 | 2026-09-20 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6cf6cfc9-98a9-354b-b5c8-cffd3bbda2ff | -12.52971 | -50.08491 | 2026-09-20 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfd8eee1-e6c0-3b57-aa24-85da885bec0d | -8.85645 | -45.9251 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4be142f1-a6ec-34dd-b16f-2db51c1e7d06 | -10.09143 | -48.4347 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 729f6358-cdbb-3914-8edb-3f9085c6c32d | -10.84055 | -50.93324 | 2026-09-20 04:40:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6cd2a5b4-ab84-3990-bbef-2a727aaefe01 | -9.10614 | -51.58749 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bb7bb381-dc31-30d5-aaac-c741a7951526 | -13.59645 | -46.93353 | 2026-09-20 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c43cf065-7dbf-34bd-8a57-8651edc42825 | -8.42454 | -54.7327 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f0fe7cb-85c0-34bc-8e38-566f4550da65 | -7.41162 | -49.84074 | 2026-09-20 04:40:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 20cd4be9-8132-3e45-9f9e-d0867a9c6ebb | -6.65897 | -50.93589 | 2026-09-20 04:40:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13097e10-f3d6-3c6b-803f-16b853674dc3 | -5.85838 | -53.54805 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b6f7248-eb46-3535-8ed6-a78f666d05a6 | -12.76239 | -46.13068 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d982ea48-d222-3d18-9760-940c2a8b63d1 | -11.78531 | -47.46706 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea7eed0c-9c74-34d1-8b43-727f6d2c665a | -7.49038 | -46.71318 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13f779d3-57e1-3e73-b74f-705e51498543 | -10.2716 | -49.99071 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0b91570-ad36-3aa3-8717-85d872e98ded | -11.4246 | -45.40401 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bee1d25d-b5f3-38ba-a8bc-1871db87b06e | -9.61951 | -45.87277 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16604a0a-3522-317b-b371-3474921604e9 | -8.70812 | -45.44644 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45ad2bd4-a332-3104-80b1-d07aa88edb94 | -10.41671 | -48.91357 | 2026-09-20 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9f327c7c-b503-3c27-a9f0-6280e07f714c | -11.24046 | -48.38271 | 2026-09-20 04:40:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3c45f33b-1905-3859-9f67-8ba0718efe5a | -8.6162 | -54.59698 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc3c85ae-a793-36d5-9faa-bd567547ba5d | -8.79105 | -48.7123 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7428fc8e-0c65-3025-b7d6-8fe6517eb204 | -7.74826 | -46.74146 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0109aec8-30cb-303c-90a0-f4cfce63bb70 | -12.64941 | -50.92136 | 2026-09-20 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3660925-c73e-3228-9233-c3a764b647e1 | -10.82334 | -50.93157 | 2026-09-20 04:40:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06fa108c-3c36-3981-8767-fe03b5d3d1b3 | -10.39126 | -48.90203 | 2026-09-20 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README58.md)
