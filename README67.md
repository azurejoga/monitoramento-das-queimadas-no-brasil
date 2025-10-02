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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 939fbb7b-a944-3740-b328-be9987d5cc34 | -10.44658 | -48.08358 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9db688bc-2f24-3dab-b5e4-00d17586b972 | -10.10348 | -48.71757 | 2025-10-02 04:29:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a6f891f9-9a6a-385c-8ad6-8d52d5eeb786 | -12.12622 | -43.42984 | 2025-10-02 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4741a538-7c9b-3a11-882d-42080a3023b8 | -10.88343 | -44.27975 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2d3a0ca-c037-3a01-a4ab-9088d2b4cc3e | -7.88938 | -47.30103 | 2025-10-02 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5213435d-f9ff-33c5-9902-646540521386 | -10.22045 | -48.20793 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62dbab81-64f1-3cd9-a59c-0ca6a2940bec | -10.65161 | -48.5071 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bfb5f57d-8434-3477-9612-f289ef20f123 | -11.19626 | -47.75106 | 2025-10-02 04:29:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e0adaa9-5549-36ac-90b8-6501cb816691 | -10.83857 | -45.37482 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4e5381aa-b4e6-3730-af78-6650a500636b | -11.58602 | -47.64102 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cfa867fd-c079-3e3f-a2ed-6516347fc012 | -11.44238 | -43.89554 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b13f73d6-7f48-3f7f-8106-d978fb1b888b | -10.05579 | -48.94537 | 2025-10-02 04:29:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72d65810-0234-307b-81e5-1e4ffc5562da | -11.27053 | -47.82121 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c32a5edf-9756-3652-9cf6-d50129e6a464 | -7.56675 | -42.39481 | 2025-10-02 04:29:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cb906542-7ca4-3f1a-b155-768dd49558b3 | -11.58835 | -45.05464 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 560ebf39-2a65-330a-87c3-3f1642846f65 | -11.07978 | -47.80113 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8aaf865e-5247-39eb-8e86-bd29cb022345 | -11.08865 | -47.80981 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b17806c-3637-3d8b-b931-17860f41e29f | -6.26081 | -43.89235 | 2025-10-02 04:29:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af0f3ceb-b767-3dc1-a436-9f4d9deda712 | -9.45069 | -45.47371 | 2025-10-02 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50f90323-c838-3dc8-8382-c2067e8faf9f | -11.27333 | -47.80353 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0e96173d-e678-3cf1-aead-47ea76e9fe2b | -11.17073 | -47.27058 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 419390fc-dfa7-3538-9c31-c55e1f5fa111 | -11.83117 | -44.99618 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5431c63c-a5a7-35d7-affd-002b692d5203 | -11.8022 | -44.99707 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9317a214-b208-35fa-b934-d59d06ca06d3 | -9.4745 | -45.47734 | 2025-10-02 04:29:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8537469-0275-3a46-9fe5-916e7f0f9a49 | -11.46769 | -44.99744 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 738310c2-805f-34d0-a4e0-f0b2b1b6e8de | -7.35956 | -44.26493 | 2025-10-02 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7213b86-62f1-3628-9490-ece24d2b8d91 | -10.24347 | -50.31436 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 73d0d917-fe7d-3e23-b1f5-da98b99ab7f2 | -7.24509 | -42.99134 | 2025-10-02 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 08cbb2b6-ca75-39a0-bd9b-33d269755d29 | -10.26374 | -50.32648 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b66f248a-be40-38d4-a2ee-23c545fb8d4d | -5.83406 | -45.77204 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aade86d6-b28e-3e54-aded-5ba8db34e076 | -8.66086 | -47.70018 | 2025-10-02 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c101d7a-1a4a-301f-9fbe-17578a1bf9c0 | -11.53784 | -46.95684 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 95be1530-54e8-3fc9-a11d-77892af7546b | -11.18347 | -47.18962 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f80e63b7-89fe-3010-9b08-67b5236dad73 | -9.3981 | -47.57225 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6aaeb793-e405-33bc-8dde-ba545bfe8a50 | -9.94028 | -43.74585 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 838273bf-f17a-3495-9c0b-559d208b8482 | -11.37727 | -45.04536 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d1e8852-8dce-382c-a9c1-2cdfa0d4dcb4 | -6.7975 | -45.96985 | 2025-10-02 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e45078b-5baa-3f61-8a24-073589eaf227 | -6.2643 | -43.89295 | 2025-10-02 04:29:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 33ca3267-1a7d-3801-9986-946cd9ddc583 | -11.94704 | -43.92082 | 2025-10-02 04:29:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f7b8b1d-9a6b-3657-b871-161bb37315ed | -9.58454 | -47.08123 | 2025-10-02 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53ce0663-e1c6-3fd3-9ed4-55bd507486d9 | -12.1224 | -43.42917 | 2025-10-02 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 24484834-621a-3495-a391-bc29a6582916 | -8.66535 | -47.69365 | 2025-10-02 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b09464dc-c86e-354d-970d-47fba39487ba | -10.89725 | -44.28612 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d8eb480-2df9-3ad8-9553-c2ab15212c27 | -10.83789 | -46.60962 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a65583b9-8c35-39e5-a3ac-900dfd3facf8 | -7.00933 | -44.50377 | 2025-10-02 04:29:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f83df89-76fa-31c4-bb77-d29be6629693 | -10.70183 | -48.58215 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4ddd7b0-daea-33f3-8876-913a6eb79460 | -10.85067 | -46.59349 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ce5146b-03bb-3c44-82df-9826258c2336 | -10.21897 | -50.34908 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b6c63d96-e230-33a9-8e2c-4cf6cd4b882d | -5.88155 | -45.81217 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15d917c8-4794-382d-85b7-7a2b01e9ab62 | -10.66335 | -48.52013 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17537da9-c3cf-3e15-93b0-f51c654b68d5 | -11.38927 | -45.04215 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f9aeae7-fc33-33b2-9b8f-fff1d742cfb5 | -11.81217 | -45.00266 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 823d40d7-328e-304b-85b9-69fd448d80c1 | -10.89127 | -44.27666 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 467bb36e-34ef-32db-a480-e3b83904f48c | -10.81838 | -46.60286 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0684328e-1a91-389e-a541-51b873828076 | -9.93377 | -43.71412 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8b45fc66-3631-3e2b-b489-4f4e0d2a1fb3 | -9.77364 | -46.22454 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00a1977e-9970-3b5a-aa75-db91748089cc | -7.88549 | -47.304 | 2025-10-02 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d0b18301-f704-30f0-a7ae-0b86cb7bb30f | -11.26997 | -47.82475 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e117b8e-73a1-3672-a5a3-35c9c45f409d | -11.06477 | -47.8095 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4cc6aeae-28df-3ace-8239-1d51ec647b5f | -11.17849 | -47.26462 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6c1e508a-2f55-3bd2-a575-f74339f1fee1 | -5.99988 | -44.60191 | 2025-10-02 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 35dd74c8-afaf-3149-ab0d-b3c9b1e04ea4 | -7.3935 | -41.87406 | 2025-10-02 04:29:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0430df9a-78c2-3de1-a4fc-13e8b0a2fa34 | -9.33314 | -45.71236 | 2025-10-02 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f775c821-2125-3000-bc35-8f06c6322733 | -7.78049 | -42.52419 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| bf57727f-e346-3e14-a54c-907f3f754816 | -7.78568 | -42.51541 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a1b5db94-e4d1-3f6f-b138-bc95cd3b0ac3 | -6.4878 | -44.28838 | 2025-10-02 04:29:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33b5d9fd-799c-3c64-a12c-702fe027bac2 | -10.92238 | -44.31547 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ed60713-5870-3f1a-8b78-daa659efa704 | -9.96391 | -48.78194 | 2025-10-02 04:29:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb5121b5-d91e-3d0b-9003-4dd480ab9a99 | -8.57628 | -49.6043 | 2025-10-02 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 89dc6992-58af-3541-a161-1ab35b0a20d6 | -10.25431 | -50.31622 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1a40babe-4566-3cb2-a89f-7438eacd39b9 | -11.44028 | -44.96446 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| de54a11e-39f3-3469-913a-3f04fb4503f3 | -11.10474 | -49.81155 | 2025-10-02 04:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26ba7e96-e79c-3a5f-b506-a46e53718512 | -9.76975 | -46.22754 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d02056f-3468-3d84-94d8-44de7d7dd8b5 | -6.33332 | -43.0391 | 2025-10-02 04:29:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d14d4a5-0095-381d-b2db-4ded5e162601 | -10.1811 | -50.24079 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b3b78124-e431-30a7-ad66-7b2eacea4ee4 | -9.91944 | -43.65871 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44e33f59-42dc-3ed1-870b-744ac2e46b22 | -10.99876 | -46.60224 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9f3f4866-dae5-32f9-84d3-78b26a159dfc | -11.441 | -43.88926 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 25803e0a-ee31-36c6-9b2d-33b5655f1995 | -9.32858 | -45.67486 | 2025-10-02 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c9962977-ccfa-3847-8c7b-cbe4fd13fff5 | -10.99317 | -46.59407 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ef85ec6-d935-391c-b356-5bba0ca8223f | -10.6698 | -48.56585 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b8ea89d3-e1c3-3fc3-9c28-c9c4aea51e9e | -10.99486 | -46.60527 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e4e45d48-4748-3115-a3d4-4018d933a533 | -9.85403 | -44.60189 | 2025-10-02 04:29:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 84ec968a-98bf-3cf5-a4f7-1f047031f1e3 | -6.38229 | -44.29585 | 2025-10-02 04:29:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 097d5e77-2a8a-3519-8577-425327a08451 | -9.93441 | -43.70981 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e7a323f-2a9e-3825-8b70-9e69a1c92a9b | -9.33699 | -45.91878 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5c21093-c33f-3a73-b71a-80a589e8c4e0 | -10.6889 | -48.57632 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ed90c2e-ccbb-35dc-ac68-539a4c3c7985 | -12.75994 | -39.74098 | 2025-10-02 04:29:00 | NPP-375D | ITATIM | BAHIA | Brasil | 2916856 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 48af9e8e-2744-3d11-b154-7a7ddae1f65e | -10.8569 | -45.41648 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9c05860-e150-3ea4-aac7-62caadae3a4d | -10.99262 | -46.59763 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c3cb5f2-d589-3161-9694-3dda04f6e4b5 | -9.92754 | -43.73075 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| b9679a29-253c-3cd8-9933-a6a91fd4e62b | -11.48291 | -44.99183 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5892b564-fbc3-3c1d-9351-bd3c6b1df33c | -11.60004 | -47.2275 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9a18fea-87e1-311c-a320-f845926107d5 | -7.84431 | -42.85275 | 2025-10-02 04:29:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d6cc3e72-0c07-366e-bd21-fdf5ea31c473 | -11.09024 | -47.84268 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 328fe56a-8b40-3335-8e5c-e4707919ff7b | -11.56902 | -47.0199 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28ed25ad-abbc-3092-8270-2289559fd9ac | -11.44065 | -43.8817 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d45a1bd1-646d-3fe6-b746-e16198e40ab4 | -11.21654 | -48.21304 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 504d89b6-34f4-3c02-8641-582bf6b5ad38 | -6.00102 | -44.57205 | 2025-10-02 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8d55608d-2df0-304a-b380-628ca43a69f9 | -10.69361 | -48.71928 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README68.md)
