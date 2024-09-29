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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbcad460-cf96-3570-a34d-4e05c5a8189b | -10.51427 | -51.12595 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89ee53e5-9b31-3eee-82db-e3fce360887c | -10.49811 | -51.13911 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13da0a4e-6fd3-36ae-898b-e1b06ae3693c | -10.49695 | -51.14686 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03d9e0e2-27e9-3b92-b1b4-45db0915eac9 | -10.49407 | -51.14243 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffba62ac-8273-3b8c-b4a3-b0dadda9439b | -10.49061 | -51.14188 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3951cdba-190a-31cb-88fa-3455274c0ce9 | -10.49003 | -51.14577 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ac3b35d-ab95-37f5-875b-6bdb9058071f | -10.48944 | -51.14969 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9ddbafd-0274-3fd5-9f5c-af19dedbbcf1 | -10.48656 | -51.14523 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f67539f-ea5c-3b98-aeec-468f5c206edf | -10.48598 | -51.14913 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d671e0a5-ebcf-3953-9650-132b52cefa7f | -10.48303 | -51.21633 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 176a55fa-ce7d-3a27-ad13-a6148c00c12d | -10.48247 | -51.22011 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae8928f5-a85e-37c6-b56a-f0bedfd622d9 | -10.48015 | -51.21199 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c9fd81c-2646-35c3-8161-f4ae49a7914f | -10.4783 | -50.8328 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecf085dd-0ed8-3a38-bddc-8c53c16c46d5 | -10.4767 | -51.21138 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0ed391a-4893-3e8a-b414-861d16cfe487 | -10.47479 | -50.83225 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a25acee5-a27a-32fc-9d4b-c91578adbff0 | -10.46926 | -51.19009 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cd80a70-fdd9-344e-b101-02e84e974b86 | -10.46867 | -51.1941 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11e05fb2-45c4-315d-b9cf-ac82bc1dafde | -10.46809 | -51.19799 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| deae90d6-3f48-3ad2-9f63-d7c9cbb49110 | -10.46582 | -51.18943 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05538478-893f-3066-a3c7-f78c15d4f90c | -10.46524 | -51.19339 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 414b8c4d-24ee-3231-a8d1-ae428b995b5b | -10.45144 | -50.79622 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a8a0b6b2-489f-3a8b-9d37-ebd4f10f09f2 | -10.44852 | -50.79171 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4301ae98-3ac2-399b-bfc3-36ac22f3370e | -10.44793 | -50.79567 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e00dc745-1ecc-3710-b69e-0c3ee9f4e125 | -10.44675 | -50.80361 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e920dc2b-0f0b-38b4-97d5-140c5a11a5ca | -10.44382 | -50.79911 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e096d9a-52ad-357e-a22b-39ad7930f29c | -9.74438 | -50.66725 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb394552-bc9f-3184-9310-4ab9f498c9f0 | -9.74028 | -50.67067 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5caa37b5-48cf-3bfe-957d-bd63dde1cd7e | -9.52434 | -51.37804 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5dde0246-a1cf-38a8-bcb4-b142e8c894f7 | 0.75201 | -50.78114 | 2024-09-29 04:49:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 82556fa5-0065-3a1c-87e2-3c1bd09a01eb | 0.36594 | -51.3723 | 2024-09-29 04:49:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 060faf10-261b-365f-9102-da3d053feddf | -4.15395 | -51.05655 | 2024-09-29 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81cf584c-2463-370d-835a-bcafc59a21a5 | -4.15061 | -51.05605 | 2024-09-29 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e40f8bad-40e0-3312-b4dc-8120d9e71dea | -4.10809 | -51.13176 | 2024-09-29 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 167b6bfe-744f-3570-ac8a-aa6b93a545a7 | -4.10477 | -51.1312 | 2024-09-29 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90e463dd-a56f-386e-adbd-6e75519b007b | -4.09867 | -51.12666 | 2024-09-29 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ca266a9-1898-3179-ae77-f20111ef38d7 | -4.04692 | -51.09012 | 2024-09-29 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42348b9a-0ea6-3e2c-b2a4-7a31bab5ea6f | -3.93748 | -51.33311 | 2024-09-29 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0700dea7-f38e-3f47-b3c5-813f57b9082a | -3.90408 | -51.91412 | 2024-09-29 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd6ebc44-beb4-3ded-bc77-9b4e1c131f9c | -3.90077 | -51.91361 | 2024-09-29 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a10efa6-8ae3-3665-a8bf-c3efbe432afc | -3.89801 | -51.90966 | 2024-09-29 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2fbbbd74-aae0-3840-bac6-f66ef607c33e | -3.86431 | -52.25341 | 2024-09-29 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e98dc91-e059-36a9-b55c-1d83cc3382be | -3.83616 | -52.23843 | 2024-09-29 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0edc0f1d-06b3-307c-9a24-b8d92b8f4813 | -3.81734 | -52.20726 | 2024-09-29 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44bc10a6-58c8-32bc-97b3-7f7f4a86a6d0 | -3.81013 | -52.18849 | 2024-09-29 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 312fcb4a-ccec-3f9e-93d0-22f1bbc76f81 | -6.14352 | -51.25134 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b928e3fa-8cf1-3210-b32f-14cfe49cd15a | -6.14297 | -51.25489 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3980b7b4-2803-3170-825c-c698b5110400 | -6.13962 | -51.25435 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0568a443-7d57-32c7-9d2b-4cbe01fa0550 | -6.13907 | -51.25792 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 294cb29d-0ee7-3d16-a87c-1b21141766e9 | -5.91468 | -51.43619 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 13974729-def4-3964-a27a-87acf5c9a210 | -5.65128 | -51.68836 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 603b7596-0389-3811-a24f-06afc8016a24 | -5.64796 | -51.68785 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5174cac1-9770-371c-91b1-9bd05e203ff7 | -5.41149 | -51.15636 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c46eefd-61c6-33ed-bbd7-0f6bb0fe7c2e | -5.25026 | -52.01565 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ceef36a-4f4f-30fc-b04f-3e8bcb96ec46 | -7.78119 | -52.72609 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3da24e65-93cf-32d8-84a9-d0e4022a56d6 | -7.78065 | -52.72955 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d78be65d-d769-311a-bd68-2d8738d92ad6 | -7.77843 | -52.7221 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77ed035d-517c-33fc-beb6-59f27977c141 | -7.77127 | -52.72452 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6fd1b30-18e3-3af6-9792-fa9fb057070d | -7.77073 | -52.72799 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e973dd3-476b-3c44-8bc8-433ecc09dd54 | -7.2801 | -51.71532 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4241821f-e4c4-31ab-975b-cefc6d97e577 | -7.20732 | -51.68306 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4819419b-a160-3277-b6a6-463b5df9d8b2 | -7.20168 | -51.84732 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4fec5dbd-f671-33ab-b9e2-180f1e7a94f1 | -7.20114 | -51.8508 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ab0ef6f-b052-3bdb-9726-8feb8cc65e93 | -7.07788 | -51.68441 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36933c62-1d52-33e6-a8c9-9b9b0cf947da | -7.07733 | -51.68793 | 2024-09-29 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a78164f6-a710-3d5b-8f86-8a1c87f70f8f | -6.78756 | -51.38948 | 2024-09-29 04:49:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9537cda8-48da-3f41-8d95-c70d3e7ba3dd | -8.33154 | -51.73998 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3472d70d-cf04-31f0-bc5f-2d70cfaaa41d | -8.32873 | -51.73591 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8a51516-d462-344e-9e58-f1d9fc2cd75b | -8.32539 | -51.73537 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| addc3ee0-3954-37e8-9c7d-1dcf374fc6ec | -8.32484 | -51.73893 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47815923-a40d-30e8-9e18-a4f313adf580 | -8.31089 | -51.74046 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aae28d0f-f718-3c4f-9fe7-611b57a20e02 | -10.89494 | -52.4178 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42788cdc-688f-3804-92f6-e160b544cd83 | -10.89159 | -52.41727 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50230f26-7236-3c81-ab0a-a03e1f1551b1 | -9.76836 | -53.54541 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c7a39003-1314-3b40-8633-422548ba1ae2 | -9.74928 | -53.17074 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53ad2514-acb6-3ade-9462-b5c4b64916cb | -9.74542 | -53.17369 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e21fe24-f31e-310d-bb83-8ee9c9de0242 | -9.6856 | -53.48922 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc392c14-14a6-3080-a52d-23c653560dc2 | -9.68505 | -53.4927 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb8e3216-6f48-32dc-9034-05c02c327b7b | -9.6845 | -53.49619 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39040415-40a0-3032-9771-8b3724051a0e | -9.68229 | -53.51013 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19fbd72e-1344-3b51-baf0-f86a0445f39e | -9.67899 | -53.50961 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b86344c2-7ae0-393f-8dcd-0fd648a3ed5a | -9.67568 | -53.50907 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a03cfec9-d6e7-3888-9339-ea409f57f61b | -9.67182 | -53.51203 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1122ad2-5c05-3cc5-b6db-264cf2b933b9 | -10.68908 | -53.04507 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dcc71479-667b-3b47-b025-48ea5b3ffde0 | -10.49628 | -52.99627 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d4d467e-cc03-3eca-94f8-86632deb8b83 | -10.49359 | -52.99232 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9959e2e-5525-32ce-b85e-328b5f883569 | -10.48474 | -52.98373 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6419259-8a6f-3d21-bf26-cb4734cd5378 | -10.48198 | -52.9797 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 608977c9-1c3d-370c-b7f0-4baa59e57c74 | -10.47921 | -52.97567 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8771918e-861e-3710-b9fd-6b5d0362f0d9 | -10.47368 | -52.96761 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0e4e9de-0805-39f9-b96f-4c768aaa2f82 | -10.47313 | -52.97111 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54c3ecbc-8381-36e8-ad52-51f5eae984fb | -10.47091 | -52.96357 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ef04547-076b-3f74-b66e-f00fe8f4755a | -10.47036 | -52.96708 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01b7866f-4890-374b-903c-5480bd02be25 | -10.4676 | -52.96305 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d96b8d9-8367-3c57-8c97-0c5c3443b909 | -10.23356 | -52.74293 | 2024-09-29 04:49:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 445a2ff8-c8fa-3e2b-8e53-445cf1753f56 | -10.23302 | -52.74644 | 2024-09-29 04:49:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6978bc39-991d-3640-9e67-7df696c165dc | -10.23188 | -52.73186 | 2024-09-29 04:49:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7f0c26f6-f18d-3464-b753-e9ead023f408 | -10.23133 | -52.73538 | 2024-09-29 04:49:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 29376677-c33d-39de-ac6d-a1f3f6fc6d7b | -10.23079 | -52.73889 | 2024-09-29 04:49:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5c28a04-2359-3658-89a0-f56a0a018c43 | -10.23024 | -52.7424 | 2024-09-29 04:49:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50f93ab8-32c5-3fb7-80a4-d8c8f94ab6b3 | -10.2297 | -52.74593 | 2024-09-29 04:49:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README49.md)
