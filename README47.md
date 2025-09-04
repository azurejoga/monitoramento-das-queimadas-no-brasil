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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6d42b11-a541-3cca-b139-86d175c4fb5c | -7.97096 | -46.34116 | 2025-09-04 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eec8409f-6e63-36fc-b879-1ce871bf9e69 | -9.4949 | -57.8169 | 2025-09-04 04:27:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5eb4b606-3ec3-30d7-bd3e-0493594e1b0e | -14.77454 | -48.14174 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6bda4eeb-ec19-30d5-a117-9c5e5e1264ab | -10.47551 | -53.62946 | 2025-09-04 04:27:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28e63c32-941e-3667-96b0-802ab4895dc9 | -10.48979 | -46.76407 | 2025-09-04 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06279a3d-d549-3cfe-870d-c5130ce646b7 | -8.40833 | -49.18919 | 2025-09-04 04:27:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 311e4949-db7a-389a-9f9e-7fcc22b97ba8 | -9.48662 | -47.61179 | 2025-09-04 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f05e1c63-1b45-307a-9ba8-064908a71cb1 | -7.69225 | -48.73298 | 2025-09-04 04:27:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 10cfd34b-f948-3d24-93e3-c5c4b3cfca52 | -12.47766 | -48.08356 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28d52a4a-9026-30bc-b7e7-ce4eb33fe883 | -11.88623 | -51.55194 | 2025-09-04 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f338964-c15f-36ae-b07f-f8e30968e8eb | -11.13293 | -44.64099 | 2025-09-04 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0e32ebc-ec6e-380f-8b87-1c749c887fa2 | -11.24207 | -44.95975 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1addd892-3ce6-3e83-b968-3776a8326e0d | -10.47383 | -53.63058 | 2025-09-04 04:27:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1828019-4fee-3973-a69d-679a8e6139ee | -9.91494 | -45.87746 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a1aa5fd2-da01-31c1-9164-c1e5ac05dba6 | -11.62523 | -46.6541 | 2025-09-04 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8ef13b7-2a67-31e2-9039-b2cf84f6c6b5 | -9.32818 | -55.22626 | 2025-09-04 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb13acd6-4a5a-3e6e-814d-5555abe33504 | -11.87739 | -51.53629 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 20e08bc4-c214-305c-8c75-26ee7ef215c0 | -9.61915 | -47.02991 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1bd9b80-6fe1-3c15-987d-3c581aea7fb3 | -14.20761 | -48.09212 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 674e22a9-e69e-3811-9fad-50602c135a0a | -8.87651 | -45.84962 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11b38458-d061-31bf-b877-d2729ed1a44f | -11.05021 | -45.15203 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 2602e49f-f8d2-36c9-bed9-61d9b81fb8fb | -10.43317 | -50.38436 | 2025-09-04 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 657cf088-6c77-3522-b092-a7c7fb94fbed | -12.47491 | -48.0795 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25d0669b-c02e-399e-a276-d167dd52234a | -7.76199 | -50.72993 | 2025-09-04 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55d662f0-e174-3b32-bb30-9b7770adb186 | -10.06003 | -46.22319 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0afd0ae8-0bc0-3593-a5ad-e4574bf9ca1a | -14.80295 | -48.2009 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0076841-9c78-37db-ab35-9bdc7538533b | -10.09827 | -54.76812 | 2025-09-04 04:27:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 397bca49-fd40-36aa-bb7b-fec9eaff0812 | -14.63145 | -48.10027 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af8e8e75-d578-3066-950e-a1f6de27eb1b | -14.6017 | -48.00823 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 132e9761-e2c1-3cba-b7f6-9a3306a916c8 | -14.5431 | -48.05624 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| adb0c0c3-6d98-34ba-a537-1a42ef51f6ff | -10.61382 | -55.40218 | 2025-09-04 04:27:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e688e079-663d-382a-a767-864a60318757 | -15.0282 | -50.08723 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 18d4346c-d37c-3966-9945-ee6ed93f0b48 | -11.86001 | -51.45892 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83b49404-f4af-3e0e-ba0e-8744430537f4 | -9.8108 | -45.96119 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb787c40-9547-30fc-b646-5a5f966ebebb | -9.69596 | -51.04481 | 2025-09-04 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18c98b52-6406-36bc-90c0-934e7e5bb939 | -15.04158 | -48.10912 | 2025-09-04 04:27:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fd63b2f7-cd12-3e46-9f7d-3ae445d8146a | -14.53979 | -48.05569 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ab64617e-db0d-3c60-9b69-389c5ed301d1 | -14.38785 | -53.07339 | 2025-09-04 04:27:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ca006f5-7858-3998-a9bd-a027bd13b134 | -14.56512 | -48.04536 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6dc148ba-f024-397e-996b-433684a5d2d0 | -10.14215 | -46.7484 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4cb97e15-33bf-3910-87aa-d20e8e8841de | -11.85379 | -51.49507 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64867154-a9e3-3321-8488-9e6e6a3d6c70 | -6.75396 | -58.7326 | 2025-09-04 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| fec16f39-5413-3183-8c14-abac58519a15 | -12.22948 | -45.05542 | 2025-09-04 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 983cd9be-12e1-3533-9214-ae468674c551 | -8.89359 | -45.78289 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c54e46dd-beab-34be-aa32-243b25d38152 | -8.12224 | -45.02378 | 2025-09-04 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bdac158-8c8e-3043-83a2-ba31020df587 | -10.97085 | -49.74675 | 2025-09-04 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42d1e229-e91e-33a3-b9df-c7bf7fe898a5 | -8.44234 | -45.68761 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5d2f82d-b174-3151-9e3f-cc0f428dd0e2 | -15.03442 | -48.11161 | 2025-09-04 04:27:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1250a347-65e4-378d-89b1-cd0db46c8612 | -10.14122 | -46.2467 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20df375b-c7b5-32a8-ad1c-1ec56ad2ade9 | -8.03873 | -45.36924 | 2025-09-04 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 77b56825-c6cb-3c8b-8fb4-102fc28f49da | -10.49057 | -53.64521 | 2025-09-04 04:27:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c9422ff-db48-3d9f-9ca5-bf3a4a769336 | -12.11568 | -45.21513 | 2025-09-04 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1cfb58cc-b231-3b12-a8ca-b99d1b2df138 | -10.65118 | -44.84233 | 2025-09-04 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 011959dc-2bf4-3938-89a0-b04571893be9 | -14.5497 | -48.07913 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4697a5bb-215e-324c-a8ff-e63bc7f944eb | -9.44311 | -46.78413 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98a20aea-b12a-3af2-8f55-9060a1f0f376 | -14.54034 | -48.07397 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e57e6d17-21e0-3765-bd67-7f9b49da5fe9 | -12.96637 | -54.77362 | 2025-09-04 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33514494-1c66-382c-be4c-60b3b9c53895 | -12.91623 | -56.99977 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5848658-3428-3db6-860e-34c3c85a4342 | -7.69301 | -50.26141 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0ec33ebb-6d82-36ca-a9c5-3ca0abe57a5d | -14.20211 | -48.08395 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8296df3-f164-35d7-9382-6f2d4c66eb3d | -7.68352 | -50.27305 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 193bea5b-b77a-3b1d-b48b-17726937ea99 | -7.72109 | -50.31961 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a1b4ad31-c0d0-396b-8808-8499bae89cd9 | -12.64318 | -57.00644 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41324748-94ed-3e08-9613-9b5d2f4fe02f | -15.04671 | -50.05938 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 628a7857-8675-3dce-b97b-8b2c5a1bebea | -11.63139 | -52.19547 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fbd12c8c-e527-3930-8bf4-0396a52aaf7e | -11.65424 | -54.53012 | 2025-09-04 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| afb1c85c-139a-35a4-a254-8fd01cc85859 | -14.5442 | -48.04914 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0123a28d-f800-3a49-b6a1-ec8afae3a77c | -15.04947 | -50.06371 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 24dc65e8-1110-35a8-84f1-4a4fcb871d21 | -9.9183 | -45.87799 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 406ae1cc-dd62-32e3-bfba-5c2c104e07fb | -6.73916 | -58.73621 | 2025-09-04 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 940c9514-4881-300f-bd85-d63e1c8521bd | -8.00924 | -50.09607 | 2025-09-04 04:27:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4b8a9336-6eed-3989-90c1-501379ca7331 | -14.8166 | -48.33046 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 33289a7c-4a65-3daf-81db-11d83e405f43 | -9.96182 | -51.64334 | 2025-09-04 04:27:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5ff728ab-250c-3f41-8916-2a0c5db6c556 | -11.58154 | -52.10691 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 40765097-8753-3e90-b34b-faab3948b604 | -8.52982 | -51.32116 | 2025-09-04 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| b3b96052-b215-3b6c-9662-3f79d5fef459 | -12.97816 | -54.78532 | 2025-09-04 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70ab7423-4014-34be-b544-b9a6a8c23968 | -15.13732 | -48.1719 | 2025-09-04 04:27:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 905d3d5a-4c91-332d-9da2-ef6b840ce97e | -12.95387 | -48.06428 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6baaa48-ff1a-37c8-93c9-f3eeeb9e9e68 | -13.57307 | -48.12569 | 2025-09-04 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2001c0c7-d980-30cf-bb22-534e9a0f12e8 | -13.50711 | -46.92395 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af0e2749-16cd-380e-8c15-58097b1813a7 | -13.53518 | -47.02755 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65405f0b-6d6c-3843-8f15-5d6564c97a10 | -11.67677 | -57.34712 | 2025-09-04 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| fe2f5c13-6201-3174-92ea-ed4fd08c600a | -11.86778 | -51.5252 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d56098bc-3cbc-36ff-b66a-d22116167076 | -13.73275 | -46.91492 | 2025-09-04 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1098c9dc-4ff6-35b9-82b6-1be1ce76597a | -14.20486 | -48.08803 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00250e63-e503-35af-9d42-fe491e9fba69 | -10.43811 | -50.3767 | 2025-09-04 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 043beb3e-be05-3077-ac94-900af4e694ba | -6.74839 | -58.72194 | 2025-09-04 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 764f8df8-ff78-3a68-923d-5ccfb2ca3e2b | -15.03016 | -50.03329 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e61b0fff-35b4-3261-b7d7-26155df5271b | -9.47945 | -47.61423 | 2025-09-04 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 683baa31-5963-31a9-9300-d5e8e33eb630 | -10.96613 | -49.75388 | 2025-09-04 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 942696f9-d868-3924-92ef-4640e6282769 | -14.7859 | -48.1362 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cdf3fb86-9972-3097-95f3-188459cbc258 | -8.35858 | -48.32697 | 2025-09-04 04:27:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9401e3d6-5b36-3499-bfd1-16290a2b7de8 | -9.68859 | -49.01082 | 2025-09-04 04:27:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18fa6938-cbff-3a62-b6ab-c9a1d51e55de | -10.96959 | -49.75446 | 2025-09-04 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63230292-59a1-3448-b2e7-e32a791cfcc2 | -13.46089 | -46.93547 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9ba786a-5e71-37ad-837f-a76d9c62c839 | -14.81614 | -48.22491 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3dfb3110-6e33-3de9-86a5-501a2570be97 | -10.58302 | -55.41752 | 2025-09-04 04:27:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 6e472685-2c87-3caa-987a-da89f0b35452 | -7.70037 | -50.26249 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 11bbfc85-4a5d-393b-8c2e-579ef16cb809 | -8.89863 | -45.79469 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 30e4a2aa-a061-385e-9dfe-71477a3603ca | -14.55081 | -48.05024 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README48.md)
