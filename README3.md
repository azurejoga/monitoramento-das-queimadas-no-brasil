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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a52276b7-6952-3dcd-b152-e01b4c364db1 | -6.4358 | -52.743099 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0efdb482-b6ef-3f8a-bba8-c0bee6a7258a | -10.7534 | -50.327202 | 2026-08-21 00:14:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5bd4652a-6092-3e16-b812-ea993f40e91a | -6.8937 | -56.419201 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c1e4640-dfe5-3151-b5ef-9a01d2d26c1d | -18.0466 | -44.4198 | 2026-08-21 00:14:00 | METOP-B | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7e771c30-5ba3-3db4-b001-bb0d1de1457a | -12.7506 | -48.458801 | 2026-08-21 00:14:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 22103200-c8bc-3510-b5d6-b14300978be1 | -3.8403 | -59.3461 | 2026-08-21 00:14:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e49487d8-b88a-3d05-a12b-4d2928cff514 | -14.1468 | -53.034199 | 2026-08-21 00:14:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 88fe9bfb-94a3-3a56-9745-0f159dbcd825 | -6.2382 | -49.957699 | 2026-08-21 00:14:00 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d83e70b6-3546-3a6c-adfc-fd822c0432cd | -10.3558 | -48.229801 | 2026-08-21 00:14:00 | METOP-B | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c413830-5165-3525-854c-71e5556ed9d2 | -12.788 | -48.442101 | 2026-08-21 00:14:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53df22e6-b734-38c7-9908-3a20763fdd7c | -7.3491 | -55.6833 | 2026-08-21 00:14:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f2ffedc-a442-34c7-9425-457ec8c33ca9 | -4.9508 | -55.778999 | 2026-08-21 00:14:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f477e3a2-d5a9-38de-b78d-e8ab6b58c3a3 | -12.6554 | -47.780399 | 2026-08-21 00:14:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9b4b7ee2-5c4a-3233-be52-c7da8db00eb5 | -10.8215 | -50.999298 | 2026-08-21 00:14:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9fbe16d1-1222-36d6-97ba-aaa52ec49dbf | -8.5847 | -54.763302 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 229c2cee-c7dd-307f-9e66-4db69894987f | -3.9582 | -43.111301 | 2026-08-21 00:14:00 | METOP-B | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ad93b5f-fc8a-34a5-aeb4-01d8b2af8bd6 | -10.3014 | -48.217701 | 2026-08-21 00:14:00 | METOP-B | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 677a8a92-711c-3623-9767-93a7e700033a | -9.5099 | -51.624599 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e80e3bc-2053-3e6a-97f2-a34eebeef558 | -12.2262 | -43.154701 | 2026-08-21 00:14:00 | METOP-B | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3ed3e66f-6261-3c9a-8301-ba5edaf30f76 | -12.7794 | -48.4048 | 2026-08-21 00:14:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 70ce3da5-e106-3451-9855-abaafbefe0d8 | -14.0115 | -53.662201 | 2026-08-21 00:14:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 541746da-8e76-3c5b-97a6-5bdb37bb5500 | -14.3158 | -51.8951 | 2026-08-21 00:14:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 723334a2-104e-3d93-9998-c4da209c1a79 | -10.3032 | -48.225601 | 2026-08-21 00:14:00 | METOP-B | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0403092c-3547-30a8-ab47-285be8c6e59c | -9.4034 | -60.517899 | 2026-08-21 00:14:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d01b5f7-4d09-313c-aa35-edb899b02f49 | -11.6299 | -46.538502 | 2026-08-21 00:14:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 85e7b957-525f-3a54-aec9-d343a8f9f079 | -9.4464 | -51.616798 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1c81a0e-6b14-3bd8-b727-c5709f034390 | -6.4244 | -52.738201 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5c5872a-17a4-359e-a091-5b39c4720972 | -14.3469 | -51.896198 | 2026-08-21 00:14:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 98041894-41cc-3081-9ac5-cf9266c92b9d | -9.4707 | -51.633301 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| daf6e4df-2aab-35b6-8873-96d764958a61 | -9.2153 | -59.632401 | 2026-08-21 00:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0cee3a53-1229-39af-8ac0-30268fdb773a | -3.5407 | -48.177898 | 2026-08-21 00:14:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efd118dd-224e-3bce-9e8b-8ac142a1545f | -6.9411 | -58.985401 | 2026-08-21 00:14:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d9f59ff1-2ccf-3377-b844-536153d94444 | -18.029499 | -44.603901 | 2026-08-21 00:14:00 | METOP-B | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5bcf59a4-c90e-37c2-ad77-ccc58e5b3c6d | -12.519 | -54.743698 | 2026-08-21 00:14:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4ff154f8-f6ca-3b55-8fe1-d7b63f478704 | -7.636 | -45.757801 | 2026-08-21 00:14:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae05e235-4d99-3a18-8501-01755582d88e | -6.6947 | -58.926601 | 2026-08-21 00:14:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 86e21f4a-8ecb-39b3-ba08-f3631a6bd824 | -9.4593 | -51.628601 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4432746-cb63-390f-b100-4a9af10ef902 | -14.5257 | -52.987099 | 2026-08-21 00:14:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2a7cb4ee-8fad-3cd4-8481-5be00fd522d9 | -6.8675 | -43.7323 | 2026-08-21 00:14:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0716a843-0641-3c9d-be76-300e1c565f31 | -9.0543 | -50.831402 | 2026-08-21 00:14:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f076a8b-227c-316c-b49a-025b6e5d012a | -12.6536 | -47.772499 | 2026-08-21 00:14:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f632c16f-7a1b-31b0-b731-78887081164d | -14.3387 | -51.905998 | 2026-08-21 00:14:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6300767e-36bf-32c5-86aa-837c9f198110 | -7.7829 | -61.1353 | 2026-08-21 00:14:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7cd25821-df78-3d8a-9961-ef7742ef6ac0 | -4.4505 | -55.373402 | 2026-08-21 00:14:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7130ad2-e0d7-31e4-b6dc-701331592b43 | -11.1663 | -53.998699 | 2026-08-21 00:14:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 73852527-f779-3e53-8031-b198c5da0801 | -6.4295 | -52.715 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7892cdc-28f9-365b-bb42-a2477d01df50 | -11.6635 | -48.3521 | 2026-08-21 00:14:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 07c100a8-e7cc-31eb-b00a-9cb3719f3267 | -18.0271 | -44.594101 | 2026-08-21 00:14:00 | METOP-B | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0380f7eb-392e-3930-afab-07bf4926f657 | -8.1081 | -51.6618 | 2026-08-21 00:14:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78666eb9-eb28-3ccd-8981-3ca03cb7aa7e | -15.4315 | -41.382702 | 2026-08-21 00:14:00 | METOP-B | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1241dfcc-0ad8-3e32-89f6-6b05cf6b5272 | -15.0043 | -52.6814 | 2026-08-21 00:14:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 377c4626-d9a2-30e0-8a8d-9cf79e28dd62 | -2.764 | -48.558399 | 2026-08-21 00:14:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 154ffe70-001e-344f-b1c0-e30547dc00cc | -6.8618 | -43.750801 | 2026-08-21 00:14:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9c14b3e2-9f40-330a-b5ce-ea1f3c720157 | -9.0558 | -50.838299 | 2026-08-21 00:14:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ee8187f-c8f9-34f7-87cc-5c5789593559 | -10.5258 | -50.7813 | 2026-08-21 00:14:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a43efc9a-fb81-3ecf-8af5-0ff0333c6633 | -6.4238 | -54.917801 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bcd43c4-8b43-3bfc-866f-57f7f880b098 | -8.5535 | -54.760899 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1cd9bfb-0508-33b1-a869-b920182f4ffe | -9.9973 | -48.552101 | 2026-08-21 00:14:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2551716a-e79c-3c67-b954-239bbfe86ced | -12.7875 | -48.395 | 2026-08-21 00:14:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de4660a7-56f3-3be1-b85c-3588ff0ad259 | -5.8693 | -57.6418 | 2026-08-21 00:14:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b94ac9cc-82da-3d2c-9af6-e924aa90df4d | -6.1184 | -53.072899 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87bade31-1a75-3be0-8e0f-68fc02d1c761 | -6.2552 | -55.412899 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6371be4-efbc-3ec1-a8de-b5420f8aefbe | -8.9885 | -50.7225 | 2026-08-21 00:14:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 768bd280-cc55-3c5c-bda7-d0be232e79ad | -7.373 | -45.821098 | 2026-08-21 00:14:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be675c46-ab38-36fe-8317-339bb2197b53 | -12.8548 | -48.418301 | 2026-08-21 00:14:00 | METOP-B | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 442b4e34-8956-3e7e-b029-dc2ca33b4e9d | -8.5527 | -54.852699 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc7b68d8-941d-3985-b371-1c73d370aa72 | -9.5094 | -51.668598 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac7c399a-8dfb-3a68-b3c4-17d86cb4f8e2 | -7.6263 | -45.760101 | 2026-08-21 00:14:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6fdccb1d-aa6f-3912-8bc5-db9f57606ce1 | -6.9461 | -52.770599 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8dda426e-1fa6-3620-83aa-762b0c5a9434 | -4.9655 | -56.2658 | 2026-08-21 00:14:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e1d799d-2e7c-3644-aa29-a22128a1a976 | -8.5968 | -54.724201 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| babc6a82-43a4-3c09-94c2-b9b5d7874f5e | -8.5889 | -54.7351 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f5b52ec-a814-3571-af51-385ee09e5d0e | -7.2544 | -49.8941 | 2026-08-21 00:14:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fd85da7-65ec-3d62-8118-9dd9aa1da784 | -13.4102 | -54.3624 | 2026-08-21 00:14:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 42c3acb9-0de4-32db-bfe8-21964fe40ea8 | -14.4446 | -45.608398 | 2026-08-21 00:14:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 05abf585-ae1b-31b0-9e35-9fb1308ffe1e | -9.0593 | -60.411999 | 2026-08-21 00:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bc2f2d78-689c-3a71-93e7-4c2c5fc2595c | -9.4131 | -60.515999 | 2026-08-21 00:14:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 82e07bce-608b-322b-9a4b-91423ebe878e | -7.3471 | -55.673801 | 2026-08-21 00:14:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 176f27f4-cf65-30cb-b6b2-77ec5ead1479 | -8.5386 | -55.310699 | 2026-08-21 00:14:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8845b360-fc94-31bb-ac37-da780697cfb3 | -5.7895 | -51.6539 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2132977d-65ed-3a5e-9423-352193fb39aa | -6.2435 | -55.4063 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16bc517a-1f50-346f-851b-71125d123cd5 | -11.2162 | -55.060398 | 2026-08-21 00:14:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 601b7313-b077-33d6-82dd-880fcae6a4ad | -13.9492 | -53.855598 | 2026-08-21 00:14:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 96a89339-d879-39d3-b1b1-b8387e446203 | -10.7682 | -50.3018 | 2026-08-21 00:14:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 31ef4eda-1ddb-3479-94f2-beb478eda1ff | -6.3379 | -55.744499 | 2026-08-21 00:14:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b57ff5b3-0aac-3e75-80c1-0bdca085e799 | -12.5045 | -47.841499 | 2026-08-21 00:14:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e612466c-3eda-3c6d-a9df-d43beda74b5e | -8.1118 | -50.0378 | 2026-08-21 00:14:00 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06768b6d-436e-3eb0-8199-e0ca331f93c8 | -4.9223 | -56.255402 | 2026-08-21 00:14:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 193c1928-4eb6-37e6-aebf-ef9422b024c0 | -6.4327 | -52.729099 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc7b6e6a-99ee-31b4-ae81-317f29a08948 | -6.2355 | -55.604198 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4101aab1-a29e-34b7-9f06-b3c875b2afdd | -4.0788 | -42.5093 | 2026-08-21 00:14:00 | METOP-B | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1bb76976-3c61-3964-9376-c685027ae659 | -10.7698 | -50.3088 | 2026-08-21 00:14:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3cec6849-ae20-378a-b80a-0c2c95f1851a | -3.5288 | -48.170799 | 2026-08-21 00:14:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 930e18e0-0fae-3635-bfe6-f50cce7e48b7 | -12.6518 | -47.764599 | 2026-08-21 00:14:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b75634de-cf13-363d-b7d0-dfb2774c6c6d | -14.452 | -45.596401 | 2026-08-21 00:14:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3c189064-e469-3fdf-ba90-fdd668e2a0f4 | -6.2397 | -55.388699 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd6c6a14-4d67-31df-920d-213ba9b1b7e4 | -9.0616 | -57.0574 | 2026-08-21 00:14:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f228544-66cf-3c54-95de-9c6afcc83ec0 | -16.412901 | -49.6236 | 2026-08-21 00:14:00 | METOP-B | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fe3cbd62-dd92-382d-9790-adb86a418767 | -9.4691 | -51.6264 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7119fec3-48e0-3a00-8fa6-33a0b9a1d630 | -14.0096 | -53.653198 | 2026-08-21 00:14:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
