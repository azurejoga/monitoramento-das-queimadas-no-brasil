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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cae9b9d8-ae7a-3c3c-a76d-fc9502cc9425 | -10.99293 | -46.83242 | 2025-09-03 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 67ca72ac-738c-38d0-84c0-dc2aae4b0acb | -11.12134 | -45.11405 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8fc0e948-6b77-3db2-9b44-87f07531cae6 | -10.1416 | -46.29718 | 2025-09-03 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8bafb07e-8878-3a02-b52a-b178a7446491 | -13.30132 | -46.92863 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9ecab0f8-bbf7-3ec4-992f-4c488ec31dcd | -11.84908 | -51.52878 | 2025-09-03 03:55:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6a12393-b718-3129-8647-9e74515981a8 | -10.49361 | -50.33948 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63b776b6-f916-3b22-84d5-998f38af3c11 | -15.09829 | -48.12856 | 2025-09-03 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ee761233-e999-3fdf-a932-ca574ebd2ff1 | -11.60154 | -52.10554 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5d028080-bb4c-3e07-9f70-0179fb351c31 | -13.35968 | -46.33027 | 2025-09-03 03:55:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b4cbd957-02b5-30b7-91b5-3733c1bf0654 | -11.63093 | -52.06 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9dd2d21-851d-3ba6-94c1-c544aec759c1 | -10.4824 | -50.34994 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6351bc76-ecbc-3096-bd71-45bd9e8a71d6 | -14.99186 | -45.30635 | 2025-09-03 03:55:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56615b8d-9e08-3701-88b3-aac6afb7d509 | -15.57918 | -48.32507 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53c89167-68ff-3a5b-9da8-655495300c6e | -12.84232 | -48.0559 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4fec5b8-118e-384a-8152-94eb67cd431a | -12.84278 | -48.02633 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ddf123a2-ce04-3c14-bb8d-55bc24da82ff | -14.80305 | -48.22763 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 735c5241-212d-3fa1-a225-307768dd7fa8 | -11.06321 | -52.07763 | 2025-09-03 03:55:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e14cb3bb-fcd9-33c7-a3bc-19bd59c43300 | -11.60707 | -52.07825 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1d352699-263f-3747-9a5d-b27709eaba3e | -12.08889 | -43.33168 | 2025-09-03 03:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f772b1c-7903-3606-97eb-38166e5d87ee | -10.75029 | -45.27485 | 2025-09-03 03:55:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 991cde0d-a09f-381f-a527-b798944a3a06 | -9.63437 | -47.86684 | 2025-09-03 03:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8ed7cf76-3301-34bd-8fec-b2b512611a60 | -10.91818 | -50.86823 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3d82611-35a6-37f5-9e4c-3aa99275f6b1 | -9.13323 | -49.64887 | 2025-09-03 03:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 146c1ac7-024f-3a5f-a478-6ac1e05dbba3 | -10.14306 | -46.26212 | 2025-09-03 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a376eeb-64db-3dab-8f48-6e2318d9e5fd | -15.116 | -48.16483 | 2025-09-03 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 092263e5-6904-385e-9644-4deb106cef30 | -15.59468 | -52.68102 | 2025-09-03 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d46dc589-95d4-3989-9f69-17c23ce81c79 | -11.60041 | -52.11108 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2e4cb783-3668-39d7-a65c-311c5d7a0df0 | -10.10084 | -46.26052 | 2025-09-03 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40245b44-b049-3d78-8d7d-55dd82db8b80 | -10.89519 | -45.79148 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a07e9d74-c0d1-3135-9b6b-acfd75554d0b | -10.90325 | -45.79682 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f700ca6-04e3-3824-806a-977fedd611a1 | -14.79727 | -48.20238 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79a818e7-2ee3-3e25-a80b-9a462c2f12d2 | -15.54649 | -48.31529 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9ddb98a7-e45a-374a-bcf8-ce3bbd8eb913 | -12.98091 | -48.0857 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b77f8013-170a-329e-9da3-d8018d72859c | -10.91171 | -50.83758 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0826f51c-305c-387c-8180-c42967d909bf | -10.44873 | -53.62435 | 2025-09-03 03:55:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6083a1f6-3c13-3f77-901e-0a5c6fc31b14 | -13.32468 | -46.82516 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 98dc3faa-a8e8-37d8-9c07-555e98447b70 | -10.05394 | -48.09085 | 2025-09-03 03:55:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e39e103-2d92-3f46-83fa-24b4e0cbd6e1 | -14.77442 | -47.5192 | 2025-09-03 03:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1a6d2aa-8e14-3c66-919a-104d9cefb271 | -15.01958 | -50.07768 | 2025-09-03 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6366eb33-bfcc-31ea-9d43-799a2af2e7ca | -10.73636 | -44.80356 | 2025-09-03 03:55:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2dffe9df-5963-3652-8634-a56f063ad5b2 | -11.62449 | -52.05864 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb714973-52ce-326b-9e35-bf792f9b5dc3 | -13.58658 | -46.921 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 474ba8f2-9acc-30df-8d4d-6241f942e48f | -12.88659 | -48.04599 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2306df7d-83e3-3b0b-a4be-6ad77ee01af6 | -9.6492 | -47.85517 | 2025-09-03 03:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad0bb073-bff0-325b-a472-d89c754e822a | -11.54906 | -44.83747 | 2025-09-03 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a2bdc90-fcb0-3c5e-a771-a000a3044a32 | -14.83335 | -46.69284 | 2025-09-03 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 65e5f341-7d6c-3048-bcba-91b3c0ce9dae | -15.02613 | -50.04522 | 2025-09-03 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 397963de-c0fa-3fc5-acb2-ec0e9f4ef506 | -11.39054 | -43.62696 | 2025-09-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55578115-8e30-327f-b4da-c7e00f61b0ea | -15.01034 | -50.06788 | 2025-09-03 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 673c0e39-f866-3ec4-84b5-ec708198b6b3 | -14.78232 | -48.15351 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 43d97026-0695-34da-be99-e95c2d59d77f | -13.48615 | -46.82547 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 652298de-1445-3224-9695-3cd7f47eb495 | -12.88394 | -48.03336 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 35159fc4-3953-38b5-9dbb-4f63a11fd8ee | -13.01059 | -48.09777 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8d53d47b-baff-3bdb-bc79-cc2c45de81d2 | -13.30803 | -46.84911 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3bc16d43-1fec-3901-a8ea-dfa646f42465 | -13.00346 | -48.10839 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1a2684e0-c0c6-30fd-be93-5d5916872c74 | -13.70647 | -46.93508 | 2025-09-03 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2b0cf66-5e05-3c33-870e-4ebc215f561c | -11.00464 | -46.93532 | 2025-09-03 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 862a186b-300a-3c7f-a19b-a19b0484f6f2 | -9.13665 | -49.66261 | 2025-09-03 03:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4740f28a-ceac-3005-b66f-e8cfb8db5ecc | -13.50118 | -46.81934 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8629ff42-5a5d-3520-b838-9e87b18e994f | -14.80583 | -48.21286 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3861d22-4746-3e4e-bc5f-f81b8fe9729b | -11.38685 | -43.62882 | 2025-09-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8aee28cc-332f-311c-8a25-d422c5e8c495 | -11.64598 | -52.05194 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 621ce070-022b-3ede-a13f-38302ec5cdcd | -13.49794 | -47.01959 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d4f9b22e-d155-3742-ad2c-2a558604bac4 | -10.91659 | -50.87584 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ae8700c-14ca-3614-96f2-0175491eb891 | -14.33827 | -52.79753 | 2025-09-03 03:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b4a6d1c-4eee-3d30-8a10-c085f1f93594 | -13.4527 | -46.93052 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0a75f8f-a612-3f26-8852-725c082a9ed4 | -11.90899 | -46.67127 | 2025-09-03 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bff78ec2-609a-3bdc-9210-60bab0d710d7 | -11.60967 | -52.13045 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 6d3bba41-38b4-39d9-b592-7212c6ac5e7d | -11.851 | -51.53238 | 2025-09-03 03:55:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1573c61a-a49c-3f8a-890f-55364ca76612 | -10.49007 | -50.34233 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 34c3fde1-ad4e-3280-8d1d-b911ea82b1e4 | -16.29343 | -45.68784 | 2025-09-03 03:55:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 16d5e8f6-f3a7-30a3-8943-3620736e389f | -12.75577 | -47.67299 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d867aa4-cdb8-3033-b29e-b8f1752f9bf5 | -11.58641 | -52.11364 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 7d2d5b19-91a2-3e0e-9a57-9fc91367c689 | -10.90661 | -50.82969 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ba42363-3bb7-3603-98c9-6b530b56f32c | -15.11502 | -48.17004 | 2025-09-03 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bcf4ffbd-92e5-3356-b7bb-184c6a233bf6 | -14.57541 | -48.04709 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bc1f20bb-f05c-3091-9bbf-3f73edea7b76 | -15.54968 | -48.34941 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9199f752-1b1e-3657-a986-573e774cb410 | -11.12055 | -44.65891 | 2025-09-03 03:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e174b51a-ac75-3381-a6d1-08ca06d90e50 | -12.91912 | -48.0891 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| afee3e65-ab80-3ae7-b2f5-10e3d62cbceb | -10.486 | -50.34711 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 64823531-78bf-3c8d-b269-ffbc04975e32 | -14.26705 | -51.22993 | 2025-09-03 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8694de53-a685-35ec-8fc0-3efa0b1a6058 | -10.4892 | -50.34675 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c61910d4-fecd-3a76-848b-f483a78db301 | -11.44382 | -47.30453 | 2025-09-03 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cf931f04-9c7f-38b5-98c0-eb5bf4105bab | -12.90189 | -48.09924 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c84683b1-84ba-3108-8d6c-d9ddb6fbc055 | -10.13931 | -46.25664 | 2025-09-03 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68836799-7769-3494-9a65-92b78dfd86ce | -12.8406 | -48.03791 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3244f399-757d-388c-a2a4-227fc12451d0 | -11.84808 | -51.53362 | 2025-09-03 03:55:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| daeeb7d5-1bd1-30c9-bb4d-8e735841d3aa | -10.92007 | -50.85883 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| af340cd1-0988-36bd-91e7-b6f31ff58dd1 | -10.52964 | -50.42419 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1954dd9-85a8-364e-9d5f-67efbaff2856 | -11.89334 | -40.98068 | 2025-09-03 03:55:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0ca5ec40-1cec-37ff-96ca-baf8a7c533ed | -14.9739 | -50.21939 | 2025-09-03 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2647244b-272b-3732-9e09-41017237c6a7 | -11.61044 | -52.06168 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4fb92e15-d9cb-36e5-83c1-7cb8a8a984ba | -11.63226 | -52.05454 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d433927c-0791-3c43-aa26-b9e359fe1d21 | -13.70103 | -46.93942 | 2025-09-03 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81867d31-c3d3-3d94-9623-59c5e1e17190 | -13.73247 | -46.93019 | 2025-09-03 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb68e8d3-26d9-3c78-a7a1-d227f6c447fd | -9.13744 | -49.65843 | 2025-09-03 03:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 17282b40-1eac-37b4-9fee-f74a5a403bfe | -15.14417 | -52.36337 | 2025-09-03 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da2a9bf2-024c-3b35-b86f-24fdf8f45bf6 | -13.8984 | -48.10215 | 2025-09-03 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5930f4f0-09d9-3153-9f35-e51de8acfb3e | -13.73139 | -46.93589 | 2025-09-03 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 004a3f7d-9b4d-30d2-b630-a922bfa060d0 | -13.46279 | -46.92646 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README40.md)
