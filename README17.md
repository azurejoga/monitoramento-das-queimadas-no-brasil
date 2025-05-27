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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b16c746-e5c2-3b57-8210-096b7505f3f9 | -14.02905 | -55.13602 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 620f947e-b99d-3487-bda2-c824658d82b5 | -12.03227 | -51.59696 | 2025-05-27 04:51:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cec1800c-c8a3-300f-9d40-5cea90fafd8f | -11.5662 | -47.44797 | 2025-05-27 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c9ba1088-6e40-33a0-afe1-f4964d554992 | -12.0282 | -57.10561 | 2025-05-27 04:51:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59aa2911-3ea2-3622-8564-c2e0797307f5 | -17.53191 | -52.11542 | 2025-05-27 04:51:00 | NOAA-20 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50ac1e61-540a-39fe-a268-89f7b33ad623 | -10.71781 | -49.62348 | 2025-05-27 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ae25c7a-b441-3f7c-b64c-65fcd39909b1 | -12.64452 | -54.08067 | 2025-05-27 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee7c5b23-d4fa-36d5-b382-eaf84d34917e | -14.14941 | -45.47661 | 2025-05-27 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6c73c9f-ff28-3991-9ed8-aad41685f3de | -10.83269 | -54.02703 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 537dc5e1-4af5-347f-8ad4-4dd066e66ab5 | -12.06714 | -47.35241 | 2025-05-27 04:51:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b35a089-117f-32cd-aad2-08ff2a9a36db | -10.72173 | -49.54367 | 2025-05-27 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee899f41-8d6f-3ab4-83ae-a4e2dfb46673 | -10.84411 | -54.01803 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5742b7d-8533-3fdc-8017-7efc6fdd28c3 | -15.88881 | -43.46132 | 2025-05-27 04:51:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1e522b01-4fb1-31ac-a763-1246fe59620d | -12.15742 | -43.20715 | 2025-05-27 04:51:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb5f5f43-faf6-3af5-a145-16aef7e3ae92 | -14.14383 | -45.47917 | 2025-05-27 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba3265fa-dd48-3394-bd3f-a6934f8bbc32 | -10.73611 | -53.88575 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3f9a9b5-ed4d-31b8-9434-19c49243373e | -11.80081 | -44.26978 | 2025-05-27 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f9d8bcd-1b01-3b29-905e-031b1bb9db7f | -16.28706 | -52.93586 | 2025-05-27 04:51:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53a1ab87-1aae-32c3-ba31-872cbee1c7fb | -11.40165 | -52.95506 | 2025-05-27 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc3506ca-ac48-3265-91d0-959a2434b782 | -14.59123 | -48.35814 | 2025-05-27 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 248718b0-94ca-30c8-b583-7c9a7d65f065 | -10.82937 | -54.0265 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 467472aa-6902-359e-9b5f-cca90655f230 | -12.12684 | -54.66665 | 2025-05-27 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e57a211f-2809-3d0a-a6eb-91c687ee5612 | -10.94976 | -48.15666 | 2025-05-27 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62452b36-a7b6-3f75-88d6-ecb8c3eaa055 | -14.01414 | -54.48293 | 2025-05-27 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb55201c-eba9-328d-b186-26401c24f40a | -11.80125 | -44.26621 | 2025-05-27 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58543070-f25f-3c9f-85d3-141a645abdd1 | -12.82425 | -47.3829 | 2025-05-27 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 112034a4-6715-3967-89d6-e4948e87e950 | -15.88326 | -43.45597 | 2025-05-27 04:51:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 59ddd73b-fd38-367a-9dc7-4f51e29f8cc4 | -10.84799 | -54.01505 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d502b2bc-6d23-3f89-8873-0a8e611bbe03 | -10.82609 | -56.96083 | 2025-05-27 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3fe7ba0-cca5-3d8a-933f-b4ab57881fe6 | -14.03294 | -55.12946 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8af8b8ef-e554-31f7-b59d-965e610b974d | -10.59747 | -52.84266 | 2025-05-27 04:51:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 289ba44f-93c1-3869-b89f-937526a66c7b | -11.81619 | -55.07534 | 2025-05-27 04:51:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29e44d0c-4b5b-3027-9f7a-d62a06ee7eea | -10.94615 | -48.15232 | 2025-05-27 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df74632b-8638-3f09-8827-5c3240eeea2b | -15.16915 | -52.29332 | 2025-05-27 04:51:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5511827a-d1ab-314d-a67f-a5e1bc1e9264 | -12.65512 | -52.43214 | 2025-05-27 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef8d4683-2aa2-3de7-a3a1-1d95d32a9364 | -12.82814 | -47.38801 | 2025-05-27 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 469f1bc5-d2fc-3576-98a5-82c87d893be6 | -15.78399 | -54.51962 | 2025-05-27 04:51:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 54709d23-4f96-31f4-81cd-e2e4324a6ba1 | -10.93532 | -55.31387 | 2025-05-27 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 958a24f6-32e1-3624-8fe0-f15b8be5f979 | -16.33215 | -58.11939 | 2025-05-27 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 230f5d04-ebb1-3e4b-8490-7a4edc6409ba | -15.88474 | -43.44215 | 2025-05-27 04:51:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e7c0fc2-dd0b-3bdf-adcc-f20901eec31c | -12.03632 | -51.59363 | 2025-05-27 04:51:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64ab8d4c-e5e2-3e37-a16c-4ef483fa403b | -10.30444 | -57.14421 | 2025-05-27 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e36c276-bc32-36f4-ab32-6c9a21c03f8b | -12.02458 | -57.105 | 2025-05-27 04:51:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f1b57f1-0cc2-3683-9ef2-a3a8ccb0c9a6 | -12.42264 | -49.98353 | 2025-05-27 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb79293b-1f79-3486-8dc1-d7d172015f43 | -12.12294 | -54.66966 | 2025-05-27 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5b6b4007-ecad-3e16-b967-312f9806ec5f | -10.80213 | -49.26029 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0018e8c7-104e-371a-845a-4eadc89cec6a | -10.12708 | -58.22174 | 2025-05-27 04:51:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba7126fd-5537-3782-8178-3ed87a0c4996 | -14.02572 | -55.13547 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba20efdc-5887-35a3-aa2d-cf8a0e4ddfcf | -11.8156 | -55.07896 | 2025-05-27 04:51:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e9009a9-ba96-3c2a-aea6-4544c1e5af15 | -11.39887 | -52.95098 | 2025-05-27 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5ae96c8-89ba-30ba-a78e-9be666a4673d | -12.83262 | -47.38859 | 2025-05-27 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa30b4dd-3484-318c-969d-293af70a235f | -14.0147 | -54.47938 | 2025-05-27 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfb9c9a5-02a5-36ee-a82e-ae412a614ab6 | -10.82661 | -54.02244 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eaff58a0-bc62-33f0-98cf-49fd746892ad | -14.03959 | -55.13059 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c8ee4ae3-99c8-3df9-bdd6-59856a7ea4a0 | -10.95138 | -48.14528 | 2025-05-27 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e1871dd-8219-3ca0-9fe3-adb6ad6084fe | -14.0312 | -55.14021 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0207a6f2-5b88-3c99-9ad9-496aec181eff | -12.12351 | -54.6661 | 2025-05-27 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f98ef444-b31a-3356-ab8d-9462e7760c19 | -10.84024 | -54.021 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c72bf4ea-069d-35a4-9f68-f5f2ec66ebae | -12.75737 | -48.34016 | 2025-05-27 04:51:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7903e88c-ea1a-32f4-b5cf-04b41c9f08b6 | -10.82993 | -54.02298 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27ba8774-494c-385b-9dc5-b3a8fd0cbc79 | -14.59179 | -48.3538 | 2025-05-27 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e36ff730-ed50-370c-b4df-b2f4635aa2e3 | -10.83213 | -54.03055 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2597da14-3697-373b-9bbf-d83180e5f8e1 | -17.52954 | -52.11624 | 2025-05-27 04:51:00 | NOAA-20 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c1171fa-5b1b-3cc6-8be6-599ffdf41976 | -14.0302 | -55.12886 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30ef5d44-891a-330c-9e89-43f6820548b2 | -10.81664 | -54.04245 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72d93f8f-8a0f-3c9c-ad4d-dd7e6d74fcd9 | -14.02962 | -55.13244 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2a1ad46-b2ed-3a0c-9c17-05a9494d45e3 | -11.14011 | -53.92962 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bec30d66-e9e9-38dc-95d7-fa023d34b41c | -11.05759 | -48.85277 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d26be2f2-df65-3184-9dea-8408ef7f1e92 | -14.01964 | -55.13077 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2efb7c20-ec75-3cb1-adf8-5c5dfb980d50 | -14.14422 | -45.47596 | 2025-05-27 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8354a5c7-f9ca-3a3a-889c-dd1abb4a89a3 | -12.83322 | -47.38405 | 2025-05-27 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0cc72542-3128-354e-8746-80a35ae5a563 | -14.01413 | -55.12248 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16978fb5-76c4-3040-b9fc-eec4082b0e21 | -12.65794 | -52.43639 | 2025-05-27 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8faf96cf-ce6b-395a-aae8-919cdb08bfca | -12.36856 | -49.98499 | 2025-05-27 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb083546-d6e4-35bb-89a0-dc98b0220981 | -11.62465 | -54.93602 | 2025-05-27 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| bf458bfb-8e95-3b87-ab0b-7cb78514c7dc | -10.13103 | -58.22242 | 2025-05-27 04:51:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f0705da-5c43-31d5-bfb7-b46d69ef7681 | -12.34694 | -49.92007 | 2025-05-27 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 637fa3cb-65bf-3b59-8058-53f98492e18a | -10.71403 | -49.62298 | 2025-05-27 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 251f5311-f941-337c-8294-8024471a3238 | -15.89079 | -43.44292 | 2025-05-27 04:51:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97699fb2-0564-332f-b8dd-52c5b74a31f9 | -11.2861 | -47.50054 | 2025-05-27 04:51:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ff91a74-388a-3b74-a7cd-cf8f7a99fd88 | -12.41887 | -49.98298 | 2025-05-27 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9f0f6c8-79ca-386d-9df3-1703d2bec995 | -18.85172 | -53.60508 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30cc6abf-0eed-338b-9a65-b3f799aa32a1 | -18.84549 | -53.62374 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c9a94a9-70eb-3de3-bd3e-bfca511107bb | -23.60545 | -54.76249 | 2025-05-27 04:53:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 19cae3e7-2148-3547-8c1b-d03e714733e5 | -18.83638 | -53.61433 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8dfb2117-243d-3f27-8f7d-0a8a911d79b3 | -18.85115 | -53.60893 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 444f2644-5d3f-3132-8127-0a4a36043e29 | -19.43825 | -54.78135 | 2025-05-27 04:53:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f79cc14-40cd-398e-ac30-8e6e8ffb3095 | -18.84208 | -53.62317 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 975a7dcf-c475-36e5-a358-0d94fb53ba75 | -18.84774 | -53.60835 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5f0c7793-8d03-3433-954f-2d3899356d52 | -18.83353 | -53.60992 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6739867a-4fac-3209-b0e3-45bc6029def8 | -18.8489 | -53.6243 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60150e46-ebfa-3f79-9804-43f3b59e5b45 | -18.85229 | -53.6012 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dba511bd-7380-34c9-99e5-6104f98799c9 | -22.15579 | -55.28011 | 2025-05-27 04:53:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3b830ea-6d4c-3262-99ae-23d2e6dc904b | -18.84377 | -53.61163 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 19.4 |
| da5e55c3-1718-3c4a-a064-c2a4505c802f | -18.86368 | -53.61888 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f91555ee-622d-3a24-8dbd-a05c22f73334 | -18.85629 | -53.62159 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 82.9 |
| c868a30a-2924-34c7-8b48-9440ec162fe7 | -18.85914 | -53.626 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8899ae0f-3a09-3fc1-aa7b-e4f1750042e8 | -18.85855 | -53.60621 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5a244c8-90f9-32a1-956d-9212b6c3c4fa | -18.85573 | -53.62542 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18e662a8-d895-39ed-b83e-69e5b34cb4cf | -18.83751 | -53.60663 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README18.md)
