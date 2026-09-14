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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d4fbd3e-07c6-361b-a5a5-028c2b42f7b4 | -2.9368 | -50.44218 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3db21f70-646f-3c1b-a415-f78687c601f4 | -2.95525 | -50.3979 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fa8451bb-2c67-3efc-b984-d6333cdeb1bd | -2.92942 | -50.40481 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 12502f0f-dafa-371f-bd67-120c383a0f74 | -2.87869 | -50.42062 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 15e1ec62-c5a7-32b2-92f9-e24879c679fa | -3.46541 | -47.46401 | 2026-09-14 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0f850a7b-f657-3f83-84d1-492d2b6464ee | -2.93112 | -50.43517 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 9f417a58-d600-3bb2-9301-4fd659d2a40c | -2.89694 | -50.41324 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 95b15a48-36f1-38cc-8db5-5e98b48eb02c | -2.90176 | -50.38403 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b959c8ff-c5ac-38cc-92e7-d7a5b7e049f6 | -2.93011 | -50.4411 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 46f63bbc-864f-375b-8e77-1c0a901497e4 | -2.89026 | -50.41219 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 66a04224-9a8d-37bb-9e84-f1a8db4500de | -2.93481 | -50.45388 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 388a5e89-2135-3921-9a0b-fbd890b5fb7a | -2.88817 | -50.5254 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e2210367-e606-392b-8d19-34b2f6be8898 | -3.46483 | -47.46755 | 2026-09-14 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 48370079-77cf-38e7-8674-4705759d82c4 | -2.9171 | -50.39671 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| f6382687-7b62-39da-948c-fe684f8fa490 | -3.79909 | -44.11552 | 2026-09-14 03:53:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f29cbb0b-04a9-3292-a5ba-a4d6cc9e2d47 | -2.94746 | -50.41973 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5ca5b7bc-6e05-3198-9164-e60a4a9fbaa1 | -2.88929 | -50.41804 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| efb785e8-49bb-3b6f-bd14-9a053f2b325d | -2.88941 | -50.3983 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7232c56b-edd8-366b-a7ab-9edf0475a52f | -2.93211 | -50.42933 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 07cd2aba-f844-3524-be8c-4050f05d8b27 | -2.89366 | -50.45333 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 4ab12e2e-c092-33b8-832a-9f01b1504ca7 | -2.9522 | -50.41529 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 504b8018-1383-305b-bbb2-f02fa6384730 | -2.90842 | -50.40736 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| eee5e113-117c-34a9-901c-abf903dadf0e | -2.92713 | -50.45865 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 7658e04f-f89c-3599-88b0-7bc4aaec68c4 | -3.22581 | -43.0327 | 2026-09-14 03:53:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad0e44db-bb08-3f04-a3af-0ed8abbe4639 | -2.90763 | -50.49234 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| e7526c7e-5914-3938-8539-6371e462555b | -2.89671 | -50.43557 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 190.5 |
| 31e13731-915d-3623-937c-fd718cf4b605 | -2.88033 | -50.51374 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09d6354c-6981-35de-9a15-678ffb206cb6 | -2.88451 | -50.50654 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b2d15b07-ddae-3bef-840f-75db5c4c1500 | -3.23204 | -50.58778 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbb1aed0-e64a-3656-a4b3-b8c15a8bcf19 | -2.88839 | -50.40424 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3b1f5269-3ba9-3cc6-811b-9c35cf51896d | -2.94176 | -50.41288 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f0c73cb1-f6a3-356e-af1f-af1b282901ae | -2.94844 | -50.41389 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0a1f7273-4ff5-39b6-b0cf-10bf23709bdf | -2.87971 | -50.41473 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 866bc39a-7246-37b9-a755-19f99a0a18d4 | -3.22989 | -43.03334 | 2026-09-14 03:53:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 339878d7-a54d-3960-a4f3-32486ffa3f3d | -2.89932 | -50.46044 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1140f13a-5cbd-345f-9740-966ea5b6b4c1 | -2.88536 | -50.42173 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| b2003edc-0686-3ab6-8f4c-9f4d347b9476 | -2.90855 | -50.48694 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| e1f44ebb-509c-3360-ba4e-08dcd2c78702 | -2.88815 | -50.46642 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bb9f47d3-efd1-3dab-aa52-36fbe77cfd67 | -2.9358 | -50.44807 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 24bb2bac-84c3-30bf-8a8e-2f5dbe0cd712 | -2.88597 | -50.45802 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 727bfed0-22c1-3387-9359-f2e04a4da5af | -2.88164 | -50.42277 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0e489a01-3328-3354-a094-e938d25cc64b | -7.08493 | -43.55428 | 2026-09-14 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 554aa5c3-9c5f-34a2-af60-807bcc8d7859 | -7.07698 | -43.55286 | 2026-09-14 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06976b89-9255-3f6f-ade4-1c7c6a4446ff | -7.07243 | -43.55563 | 2026-09-14 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d896996-ff1b-3a64-888a-e18f1f2336aa | -9.47105 | -47.32613 | 2026-09-14 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb8308c6-037e-3b9d-9053-ac307009babe | -9.45305 | -47.85608 | 2026-09-14 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9248c256-c755-3a10-996e-4365407c9296 | -6.73968 | -50.92727 | 2026-09-14 03:55:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 301bb2f9-a77c-3b23-a759-20a23f94f043 | -6.42284 | -41.55339 | 2026-09-14 03:55:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bad4d5b0-92c0-3f55-bd3b-517c7aebfc1c | -9.4084 | -50.17005 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a212dc98-8402-39d5-aed4-81d6fad3a5b2 | -7.77513 | -46.67203 | 2026-09-14 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ed0a182-5cf1-3e7d-be7a-fe6e62ec9a09 | -4.85903 | -48.35994 | 2026-09-14 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| ee2083b2-bf84-3712-aaf0-ac96d31434e4 | -9.44916 | -47.87784 | 2026-09-14 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e26d030-89fe-3911-8853-04a068572974 | -5.61683 | -45.24669 | 2026-09-14 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ededb883-a03a-383d-8111-b0bba71ebdf3 | -10.46759 | -51.25151 | 2026-09-14 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8dd2a616-5187-3bba-b8aa-fc15ae813963 | -7.08763 | -41.82116 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b12c5cd0-16f2-3d8c-96b0-a0fd6455d4fa | -3.78642 | -48.92748 | 2026-09-14 03:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40bb4754-03d5-39b1-a26f-c8f710b25c0d | -9.44348 | -47.88013 | 2026-09-14 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 542de78d-b79e-3f34-9c5a-45e87eacab3b | -4.34723 | -48.96771 | 2026-09-14 03:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 95c47a1c-8bd3-3703-8e7b-57b30efccb55 | -10.10921 | -48.86092 | 2026-09-14 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 3341f8c9-bc57-33b0-bd43-c3dfc464b3b7 | -7.09324 | -41.80931 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2b2a9c5c-144d-398c-b384-c96aa2c0a343 | -7.47185 | -42.11247 | 2026-09-14 03:55:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ca3dc3b8-5510-3ee9-9598-306216001a14 | -8.61638 | -44.44007 | 2026-09-14 03:55:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed781254-13ee-381b-b446-9bec0fe7cecb | -6.33934 | -43.36387 | 2026-09-14 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 992e8437-243f-37db-8a6f-e6b09a8827e3 | -6.87224 | -52.11108 | 2026-09-14 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| eae5facc-beca-3fa9-a84a-c1f635a9e83d | -7.15576 | -42.11736 | 2026-09-14 03:55:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5e2d587c-7605-3315-9efc-c7e69276148b | -11.22127 | -46.42251 | 2026-09-14 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7fe6a3db-39c7-30cb-beb0-61c6479c2a5d | -8.50436 | -40.19967 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7f2180f3-7304-3238-8ff9-1d3f19ee962e | -9.45081 | -50.12863 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b18544eb-40e1-334a-9eae-07b150234d83 | -6.77366 | -42.74452 | 2026-09-14 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7e487505-ff44-3fb6-957e-5a1f42014eec | -7.42187 | -41.93251 | 2026-09-14 03:55:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 380082c7-a564-3d5c-bc0c-bb93ec2b0c97 | -7.11456 | -41.79154 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| faa9b7e7-244a-393c-a4c4-b7ddc221265c | -7.56057 | -41.83868 | 2026-09-14 03:55:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 25f99175-6730-3688-a636-9e2536ad8989 | -8.42733 | -46.04265 | 2026-09-14 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1d961c68-b19f-3768-8295-fd12da85bd2d | -9.40674 | -50.17878 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6490a30b-a973-3fe4-b4a5-3594efdc5221 | -4.59551 | -47.17236 | 2026-09-14 03:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bb513e9-2047-3101-bfa4-4b53eb43796e | -3.78374 | -51.345 | 2026-09-14 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4b25fdac-3395-3d11-9ee5-0c26fa9bbe9c | -5.81587 | -42.73415 | 2026-09-14 03:55:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 728ad4bc-3b9f-3a85-9e61-adbb5cb6dcce | -9.45359 | -40.39304 | 2026-09-14 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 93b832e9-4e3f-3723-aa92-daa0dc98fcf4 | -11.23019 | -46.42449 | 2026-09-14 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef38b370-8edc-3707-855d-07c80dc4abc3 | -9.33061 | -44.3719 | 2026-09-14 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8c0bf0b4-5fb2-3daf-bb7a-6a9871341deb | -9.41349 | -50.17556 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9cd6868e-6300-383b-ab59-d096a189a281 | -11.22732 | -43.43474 | 2026-09-14 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 612bbab4-52aa-334b-828d-99600dc15df9 | -9.33528 | -44.36903 | 2026-09-14 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2ffe0596-20ec-3200-889f-f8cce416cbc5 | -10.6394 | -46.09717 | 2026-09-14 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2e031d86-5858-32d7-81cb-292e5e38dd19 | -9.98307 | -50.27515 | 2026-09-14 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9d53ff7-1ba9-3a20-850c-c30b12cde82e | -10.54763 | -51.30478 | 2026-09-14 03:55:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 61497fa2-92f8-3084-ba86-f6b8ab0df184 | -6.17735 | -43.34987 | 2026-09-14 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| faa3174a-da7b-3c09-9815-613521adaa2f | -5.84889 | -52.09557 | 2026-09-14 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ca1aabab-924e-3802-9bfa-634a94f94532 | -8.6062 | -44.45021 | 2026-09-14 03:55:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67a91125-3e4a-3793-85d8-ba18cc229dc2 | -9.41752 | -50.12193 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4f7ed2e1-0be6-3378-bd4a-516d324295f4 | -7.01767 | -44.64206 | 2026-09-14 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5af1c61a-8a1e-3237-8daa-fdaf1949d963 | -9.02615 | -49.81327 | 2026-09-14 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 92fe744e-4b12-3fd5-a3dc-657a8eb56038 | -3.39512 | -50.75918 | 2026-09-14 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c7cd03da-f244-3ed4-8d9e-f38b9b8e5f59 | -11.22421 | -43.45284 | 2026-09-14 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 023d9347-0c5f-33cc-a36f-584d547bfdf5 | -9.41432 | -50.17118 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0b8715e9-08f4-36cd-a44f-ee2356aa5332 | -10.17905 | -48.06369 | 2026-09-14 03:55:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50dbb9e4-0f18-3e3a-a336-d1de2b90dc95 | -3.38646 | -50.38743 | 2026-09-14 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a5c52bba-bd75-3f2a-8f5a-84024e33941a | -11.21596 | -46.42631 | 2026-09-14 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fa15b567-11f4-3caa-b26a-ea957e27b2f7 | -10.23725 | -50.90787 | 2026-09-14 03:55:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2de2c210-0a9f-3452-8416-f22cd57013a7 | -10.77313 | -48.97571 | 2026-09-14 03:55:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README11.md)
