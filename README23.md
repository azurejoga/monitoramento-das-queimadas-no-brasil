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
| 412c2b9e-bbcd-301b-a1c7-1efc77dfb11e | -5.72899 | -46.46872 | 2025-11-09 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 415d67c7-3cbf-3eb0-b2e2-87c1c412f179 | -3.42498 | -50.04201 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0022f17-6a10-3a34-b0ef-bd57ecd6c531 | -4.32615 | -45.69435 | 2025-11-09 04:38:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4fbb90ee-70e0-333a-8639-62058c1d0e41 | -5.37305 | -48.91973 | 2025-11-09 04:38:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b992f36f-bb0a-3123-b992-ed1d1229a573 | -3.33748 | -49.73533 | 2025-11-09 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1964004d-0450-3ab9-8fbb-013e1399d35c | -7.1774 | -44.95273 | 2025-11-09 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| eedcc74c-a2fd-33fe-a0b6-81b8b44d92cc | -4.40255 | -44.08091 | 2025-11-09 04:38:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c70c47a-ec27-36aa-b225-c5e9c07f9985 | -3.41282 | -50.26016 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3981139-eaeb-35f6-ac3a-550f65db48fa | -5.13798 | -45.71876 | 2025-11-09 04:38:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa738f42-2c61-32fb-bf0e-1b94fb49d826 | -3.14316 | -48.73 | 2025-11-09 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ec1d9ef-fbc4-34de-9094-87096b402322 | -3.52039 | -50.31014 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 960ae715-e23c-34a2-adda-dd093db0d8db | -2.50748 | -49.46155 | 2025-11-09 04:38:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ac0de9c-e220-3178-8111-20f0dbe0bb1f | -2.78911 | -49.65612 | 2025-11-09 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d6758f7-c89c-30a5-865e-bde7d783184b | -3.40886 | -50.26323 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93e6b349-6c5e-30b6-8774-542ee281016a | -3.52983 | -47.54333 | 2025-11-09 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2030d11-2931-35a5-9827-5fdc57637c50 | -5.0974 | -56.16132 | 2025-11-09 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9992d36-e122-38c8-ac38-ed833daa3c24 | -3.05752 | -50.21609 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2e8bba17-ac2b-3f98-a907-bcdde3f016f4 | -3.31384 | -50.10136 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c270090b-462f-3675-8234-d88cc5d1b3b6 | -6.6412 | -43.5504 | 2025-11-09 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f85e7dc-9fa6-38bf-9c21-40e7a9db7288 | -3.25663 | -50.11428 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9a7932f-9cc3-3a75-840d-33fd07c8ff24 | -3.0688 | -49.37146 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dffa8b29-dc64-397d-9f0e-dc9aed3bb02f | -3.34451 | -50.20135 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7317041-2040-3fde-b0f5-ca953c19578f | -3.88688 | -47.1798 | 2025-11-09 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae31a5a5-2731-37d5-8074-3627db2792a9 | -4.62764 | -48.68888 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0eba725f-c8c9-3ec6-b804-eafc8a8b517e | -3.40512 | -50.4594 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e4473dae-4df0-390f-8e88-bdec3ae94da7 | -3.32048 | -50.30833 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec2c0c1b-17f6-3e89-a28a-568577cf147b | -4.31691 | -46.80538 | 2025-11-09 04:38:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e0a0d5b-655d-3f4a-b182-38e09ab6936a | -8.20064 | -45.70078 | 2025-11-09 04:38:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d48649e-2086-3f7c-bd67-e66253b8bad1 | -3.25896 | -50.07805 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6448d318-d204-39c9-b199-7a4644ee93e2 | -5.0798 | -45.7329 | 2025-11-09 04:38:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f2479b7-0c0a-3d04-b9c2-7dc19ebdef86 | -4.55889 | -46.69037 | 2025-11-09 04:38:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3d7690f8-1b81-3c24-8233-860bc3da28b3 | -3.95606 | -49.02703 | 2025-11-09 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a341a008-37a8-3ed9-9233-1c82d81476dd | -3.09466 | -49.67952 | 2025-11-09 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44d8670e-dd51-3309-89bb-d8bd34b31312 | -3.68863 | -51.14529 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1ca042a3-0a6e-3026-90cf-c542f9bce20f | -3.5173 | -49.26483 | 2025-11-09 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9ff3787-86ab-3c12-9e93-835ee5a3d557 | -2.78563 | -50.31827 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a72ab1e-0846-3f0e-bfd8-3d98ab774b69 | -3.91063 | -49.76445 | 2025-11-09 04:38:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62553902-bf8b-3e68-86fb-8c5374d657ee | -4.58752 | -49.39519 | 2025-11-09 04:38:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f20e9201-f37c-3742-b346-747d83de4311 | -3.70854 | -49.81518 | 2025-11-09 04:38:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29ce613e-f128-3d00-8ebe-70a6e2530ef1 | -8.18874 | -46.20374 | 2025-11-09 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13c9c78f-51a7-3a09-8599-4a70963ff0a0 | -2.97996 | -48.70751 | 2025-11-09 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f0bcea0-2471-36db-a6d0-e731c050a89b | -3.09959 | -49.26274 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c0d14570-4991-3cc5-bdb0-cd00163ab255 | -4.58338 | -45.70367 | 2025-11-09 04:38:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aeb7469b-71af-3ca5-8456-0b7777ae7310 | -3.06217 | -49.37041 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80e41a9e-0119-3259-a030-aa84aaddaa4a | -4.13329 | -49.25987 | 2025-11-09 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aae58e6f-b911-3135-8f2d-63372e8a3c00 | -2.51635 | -49.44864 | 2025-11-09 04:38:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ae2cde3-f903-30c6-8697-126ec524b83d | -3.19695 | -46.43837 | 2025-11-09 04:38:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 008741bc-216e-33c6-bc9a-5850eee031f0 | -5.35923 | -44.86666 | 2025-11-09 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b142a36-4497-3315-a79d-da64a6228028 | -3.3513 | -50.18042 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2a4a54f-52c1-3db0-a95c-d7fae1a630bd | -5.37121 | -44.62218 | 2025-11-09 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c904542-e89d-3c8d-86ad-78922c15285a | -5.38713 | -44.73259 | 2025-11-09 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 470d4f31-d6ca-360c-9848-dda376ea5cc3 | -3.65329 | -50.26799 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 478ad09a-4e87-37a1-9085-4fe5c1e8ff9f | -2.83852 | -49.51678 | 2025-11-09 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56beec6e-54d6-38ec-9463-f93763c37e21 | -3.33999 | -50.208 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21b652e4-8a7f-3e82-bfcc-801e3a3bddbe | -3.8942 | -47.18469 | 2025-11-09 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 96966b02-f03f-31e1-a762-b7bdb028d2cb | -3.0609 | -50.21664 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dbf831bf-dc98-3219-b1e5-00669317c0ed | -3.09351 | -49.25824 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bc7b500-92f8-3e8e-bb87-5a728bfe6caa | -4.24432 | -44.67327 | 2025-11-09 04:38:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d6974f0-7cf5-3bdc-94f2-8b0aa97516bd | -4.32442 | -45.98005 | 2025-11-09 04:38:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a8b686c-3fac-31c4-be0c-f45e2b0b32fa | -4.89983 | -48.62234 | 2025-11-09 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb8786d5-c225-3206-8292-5238e05994ad | -5.38397 | -44.72713 | 2025-11-09 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 318c7834-5ec8-3b4f-8354-85e2b02d3efe | -3.14268 | -50.27674 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f87c5136-e7b2-3286-b21c-b7d395aa190b | -3.28845 | -50.19646 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0678ac89-2162-36cf-bfb0-226428251100 | -2.98711 | -48.70511 | 2025-11-09 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94b59985-ec83-3f13-8176-26882d66f466 | -4.57313 | -48.47527 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd8b6d38-cce1-3291-bc1b-8ec2df041899 | -6.62991 | -56.28381 | 2025-11-09 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1480aaeb-797e-34c2-8d8f-4aa8f78748aa | -3.33803 | -49.73183 | 2025-11-09 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bccf8e9f-1041-3345-8baa-7d516cda5228 | -4.14096 | -47.6595 | 2025-11-09 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32081de5-afe8-3e72-9d88-03c575405d7e | -5.57664 | -47.13142 | 2025-11-09 04:38:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c4a04a0-53d4-3bf2-91b2-9cb583761735 | -4.12181 | -47.29703 | 2025-11-09 04:38:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 32ab6a5a-6deb-3df8-8b2b-da5fea97d05e | -3.30534 | -50.17703 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af637b19-de35-3e51-acfe-f486d21ccbce | -4.37527 | -48.69548 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49d096e0-8a42-3ef1-9ab8-a06acdaa563c | -4.97015 | -49.59735 | 2025-11-09 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d17fae6b-c391-33d8-a774-182a43b9d20c | -4.98054 | -48.43266 | 2025-11-09 04:38:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9953503a-a95f-3dca-a6cf-6cbbe9608af1 | -2.97221 | -49.82949 | 2025-11-09 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13270a8f-5f97-3c92-ac60-779075e6c773 | -3.31438 | -50.11974 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8150aec6-0f7b-325d-aa83-831e988341e5 | -6.34247 | -46.76315 | 2025-11-09 04:38:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d2a1ec2-ffaf-3d6c-a37e-4c6603fc91ac | -3.75656 | -51.28987 | 2025-11-09 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d58c6ce3-4d3f-3624-be4e-5bf5dca49b87 | -3.05695 | -50.21971 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f883a0eb-8d3e-3224-acdb-de339ec707ee | -4.68238 | -45.6914 | 2025-11-09 04:38:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fedf6a77-7539-39fb-89da-b597c30064b0 | -4.5201 | -48.83429 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d28e892-4f07-376d-aa4e-b6d3b9655b72 | -4.63993 | -46.3978 | 2025-11-09 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82cd76b8-c91f-351b-947a-8c8da01da45a | -4.39621 | -49.65928 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17aa6394-feff-3872-a58e-e249df7a349f | -2.43224 | -48.04387 | 2025-11-09 04:38:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24c4bb09-5c04-3fc7-9d0b-4155ba762b8d | -3.34113 | -50.20083 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac001ea7-5691-3168-863e-75162bfa89dd | -4.68229 | -46.40768 | 2025-11-09 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02e2f959-30eb-3a7e-8b25-13c9aa9337cc | -4.20403 | -50.65839 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c10f53b2-48aa-3168-9580-238a50616fbb | -3.14377 | -50.29173 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5fc4cf6d-8648-38b7-be00-46226b04aab6 | -6.22419 | -47.01678 | 2025-11-09 04:38:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64f75eb6-30ce-3fb6-aeef-ac4f672f46f9 | -3.31662 | -50.12743 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6d0700b-9bfe-37e9-ac4d-5b952e66417f | -3.54262 | -50.38773 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae364cff-e85b-38c3-832d-ceb59f9f8742 | -6.88428 | -49.24677 | 2025-11-09 04:38:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9444078-b913-3f7c-b10d-6acfb53ab6a0 | -3.256 | -50.13985 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c798cc8a-b017-3b45-94cf-ff71e119bcdf | -3.84662 | -50.74616 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2643a316-84a3-3b9f-8e8c-94fe8deb1163 | -3.31327 | -50.10493 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 650e4619-002b-37aa-8b0d-a72808d778a0 | -4.32022 | -45.98362 | 2025-11-09 04:38:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7e80b7e-eea8-3ae0-b3e0-a0f95fcae800 | -8.12364 | -47.85508 | 2025-11-09 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04d9c683-28ab-3024-8cd8-2d8d620701f5 | -2.60285 | -49.22361 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80c3045d-5fcf-368a-8828-53311ebe4a77 | -5.18593 | -56.11001 | 2025-11-09 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 295bcaa2-a1a4-375f-85e8-6f3655730457 | -1.72509 | -54.6833 | 2025-11-09 04:38:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README24.md)
