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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c86fab40-771f-37af-b938-8eea8217fada | -12.7832 | -52.9477 | 2025-09-07 13:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 180.0 |
| e723f048-cb18-37b2-8429-51f310ebe401 | -8.1421 | -44.8769 | 2025-09-07 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 52a534ab-eb47-38a4-b02b-d1ec4fc8e861 | -7.725 | -50.3386 | 2025-09-07 13:10:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 68164ef3-15bb-333c-8d11-89e94a422143 | -5.9713 | -44.1312 | 2025-09-07 13:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 8cd1b34c-170d-3702-aeb2-7140f0197cb9 | -7.7439 | -50.316 | 2025-09-07 13:10:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 5e2497c7-6364-37b5-8e6e-0910718e9c49 | -11.4093 | -43.5573 | 2025-09-07 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| c5516dca-1f94-3bad-a83a-83c0172d9715 | -8.4607 | -45.0266 | 2025-09-07 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 171.9 |
| 5c154dbb-d63b-31ca-8df5-daf4afb43e8c | -12.9289 | -54.7744 | 2025-09-07 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 734a881b-60c9-3089-b7ca-8de634ba233a | -18.0424 | -47.1044 | 2025-09-07 13:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 100.0 |
| c497a435-3679-3bdd-9aed-7cb2f3b5c39d | -12.7835 | -52.9268 | 2025-09-07 13:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 899aef38-3c83-3005-97b1-9c756b8bead7 | -8.161 | -44.875 | 2025-09-07 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 298.1 |
| a76d6bab-1dde-3fd9-a4fc-ce2d00430549 | -7.7252 | -50.3174 | 2025-09-07 13:10:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 3cfb16e7-a90d-3242-bfb2-b1aa4253091d | -8.6832 | -45.3221 | 2025-09-07 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| c6db0f2a-c3fd-3be5-9f57-c6f68786e5f5 | -11.1575 | -48.3883 | 2025-09-07 13:10:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| b1fa0d83-2437-36a2-8e9e-435c48e901cf | -8.4604 | -45.0495 | 2025-09-07 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 86188a8a-ad12-3419-b8ce-a6dfef85b617 | -15.1044 | -48.0659 | 2025-09-07 13:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 95a195c3-ba73-3aa3-ac0f-999ed4e57e1b | -12.8059 | -47.9959 | 2025-09-07 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| ff82ab06-8f1b-3b9f-96c4-9fc585a652e4 | -19.4898 | -47.7646 | 2025-09-07 13:10:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 142.4 |
| e2b2dd44-a060-3464-8012-b5232fba29f7 | -14.4882 | -48.7671 | 2025-09-07 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 75fa708b-3648-3217-8e36-380250dabe01 | -10.4632 | -53.6132 | 2025-09-07 13:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 7685f239-d543-3b2c-9943-b65069745ac0 | -12.948 | -54.7724 | 2025-09-07 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 151.9 |
| a2083854-0447-3b66-9a35-ae129af5cb20 | -7.7437 | -50.3372 | 2025-09-07 13:10:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 5ed4eafb-bc4d-3471-80f2-a580da6ca530 | -11.0245 | -45.9502 | 2025-09-07 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| a26177f0-5a94-3df2-9357-c287138e2344 | -11.4089 | -43.581 | 2025-09-07 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 417b0f11-e53e-374d-a6c7-a3c1376cf574 | -7.6176 | -44.6543 | 2025-09-07 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 841bc350-edeb-3fe5-8771-011e641dccb7 | -15.1845 | -47.9627 | 2025-09-07 13:10:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 9d23480a-edfd-3d9c-9924-81ff7b59af9d | -5.73 | -43.8958 | 2025-09-07 13:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 290e0dc5-22e9-3671-a0e8-015ccd65fb42 | -19.4695 | -47.7691 | 2025-09-07 13:10:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 368ef243-a0cf-34c0-a43b-e9aa1ca1e300 | -14.1946 | -53.3483 | 2025-09-07 13:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 657fe150-2ebe-3a27-84db-67c8d12f9d15 | -15.124 | -48.0627 | 2025-09-07 13:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 170.6 |
| 64065495-a7b4-3f64-89e4-cafd85dff62a | -12.7641 | -52.9498 | 2025-09-07 13:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 262.8 |
| 26bcc060-4978-3d50-ba11-8faf98853c5b | -7.0129 | -44.9613 | 2025-09-07 13:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| d27f8355-090a-3422-a334-2bfad2158361 | -6.192 | -42.6442 | 2025-09-07 13:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 99.6 |
| 607aa6be-7b72-363c-8d6a-f754038592ae | -11.4089 | -43.581 | 2025-09-07 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 371.0 |
| 350df865-3fda-3778-ae1a-3d6098009bc3 | -11.2636 | -46.4843 | 2025-09-07 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 234.1 |
| 4cc7e19b-c7ec-36fb-990c-21527c64be04 | -7.7437 | -50.3372 | 2025-09-07 13:20:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 7e4073f7-5ac0-3c21-b8be-d09ec9ab91dd | -5.9899 | -44.1528 | 2025-09-07 13:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 224.4 |
| bfb00cd6-626e-3fd2-9666-4ff30884691e | -10.4444 | -53.6148 | 2025-09-07 13:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| c9661149-10f8-31b0-8236-1aaaa68c7c9f | -15.103 | -48.1334 | 2025-09-07 13:20:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 73b665ac-6fca-3009-85da-423651c75e6c | -5.9901 | -44.1297 | 2025-09-07 13:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 83e31dc9-77af-3dfe-9a21-4c8f0998d36b | -8.1421 | -44.8769 | 2025-09-07 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 223.5 |
| 0ed65387-2125-32bb-b330-dd252fadd1fb | -12.8248 | -48.0155 | 2025-09-07 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 276b34ac-d407-3113-8e3a-7d0777c0fb31 | -8.9028 | -45.8426 | 2025-09-07 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| b47ee233-abba-3413-8027-2c7937b73a13 | -11.3897 | -43.5839 | 2025-09-07 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 279.2 |
| 9c0abed8-f327-389f-9fcb-558193272de0 | -12.948 | -54.7724 | 2025-09-07 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 166.6 |
| f70c7db7-0ffd-3904-8eaf-0aa7649b3a4c | -8.6912 | -54.6682 | 2025-09-07 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 8b0b5660-8124-3b84-ad93-086464643848 | -8.9031 | -45.82 | 2025-09-07 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 58866150-1c10-3585-9865-fc89a63495e6 | -5.8401 | -44.1412 | 2025-09-07 13:20:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 54ff8173-5f42-3aea-a4fe-af9de80915a8 | -8.4607 | -45.0266 | 2025-09-07 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.2 |
| db73789b-079f-30b7-acc5-93c0912ca60f | -8.161 | -44.875 | 2025-09-07 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 505.7 |
| 17b4e4bc-ba2d-3c59-ae87-2c9d039ae4b6 | -12.8252 | -47.9932 | 2025-09-07 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 5c23a673-b26e-34a7-b898-9eb604760609 | -8.1814 | -49.6003 | 2025-09-07 13:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 7a43faf9-1b7a-37bb-a104-7d3f6d48bae5 | -7.725 | -50.3386 | 2025-09-07 13:20:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| c989867b-036f-3373-b956-4c5ce88bdb48 | -6.4788 | -43.9979 | 2025-09-07 13:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 2cd970ba-dd6e-39d6-89a3-f32a0bb62e09 | -11.586 | -47.7613 | 2025-09-07 13:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 040bc29d-2171-33a9-8bcb-e94572c75b25 | -12.844 | -48.0127 | 2025-09-07 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 9844633b-4dba-3a4e-ba99-6dc439409475 | -6.1388 | -44.2561 | 2025-09-07 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| efa79f67-1a44-3885-b358-63711d03cd4d | -6.1923 | -42.6205 | 2025-09-07 13:20:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 88.1 |
| 9e09028f-f965-3dd4-82cf-e00af9ee1f81 | -5.73 | -43.8958 | 2025-09-07 13:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| f7aabb2d-06f4-3865-82e7-79d0b38fc8bd | -15.1225 | -48.1302 | 2025-09-07 13:20:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 141.7 |
| c634cdb8-ac2e-37c7-81c5-9b0ed713b685 | -12.9289 | -54.7744 | 2025-09-07 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 6c588d02-44b1-32df-b147-29567ebb9ed9 | -19.4891 | -47.7879 | 2025-09-07 13:20:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 324.0 |
| 1f3ee774-c480-3bf6-85b1-2a25b004ca47 | -14.4882 | -48.7671 | 2025-09-07 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 98685b8c-c5aa-349e-8d6c-e9677a7d2251 | -12.8444 | -47.9905 | 2025-09-07 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| a95ced97-df8a-3c90-833f-5da183c221d1 | -5.9711 | -44.1542 | 2025-09-07 13:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 740caf95-0022-3421-b7cf-7a9fa11bc4fb | -5.8403 | -44.1181 | 2025-09-07 13:20:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 128.9 |
| d9024f31-19e2-3362-af14-dd3082b84b86 | -8.4509 | -47.3394 | 2025-09-07 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 53f948f6-b4f9-3979-afe6-660dcdb58533 | -11.5856 | -47.7836 | 2025-09-07 13:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 1a626651-36b0-3fdb-bd74-d34032c7a9eb | -18.0424 | -47.1044 | 2025-09-07 13:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 180.9 |
| dc719bea-b929-3171-9a69-9f3c34e72514 | -8.4135 | -47.3209 | 2025-09-07 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 1cdaa27b-72bf-3dfa-bc38-f38360987496 | -11.3901 | -43.5602 | 2025-09-07 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 229.5 |
| 07f45e3b-8b6b-31ac-966a-f96e6b08902d | -10.4632 | -53.6132 | 2025-09-07 13:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 453.8 |
| 8c89ee53-e2de-3ab1-b7ff-7f22068f08ae | -18.043 | -47.0812 | 2025-09-07 13:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 122.9 |
| c12b3600-10c9-3692-9eeb-cf5b228efe1c | -12.3016 | -47.2416 | 2025-09-07 13:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 5cb9e9a4-b0f6-3692-87c5-890f8bcb73f7 | -11.1575 | -48.3883 | 2025-09-07 13:20:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 559dd486-6283-352c-99a1-039ab16657e9 | -11.4093 | -43.5573 | 2025-09-07 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 282.5 |
| 0d6b08b0-1b6c-3898-884f-8cc5ae4ff242 | -7.7252 | -50.3174 | 2025-09-07 13:20:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 3c60efda-4df2-30b2-8d1e-5ba11b681b22 | -8.4697 | -47.3376 | 2025-09-07 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 65f13f95-b58a-3c7f-8d42-447dc25da467 | -11.0245 | -45.9502 | 2025-09-07 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 0fb414ce-bff4-3788-bcae-840d23e40d8c | -8.4511 | -47.3173 | 2025-09-07 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| f4125aa4-d8fd-3965-ba32-f7675ec24e5a | -19.4898 | -47.7646 | 2025-09-07 13:20:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 82edb7bc-d39d-3af2-bc82-19af16fc1c80 | -6.192 | -42.6442 | 2025-09-07 13:20:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 112.8 |
| 86bec0be-923b-3de8-833d-338ff7fe4f22 | -8.922 | -45.8179 | 2025-09-07 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 109.5 |
| e12fab96-1f93-3f60-a58a-650e61412374 | -12.7641 | -52.9498 | 2025-09-07 13:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 136.1 |
| f0405974-6e49-3821-b630-d6ddc983dd2c | -11.264 | -46.4617 | 2025-09-07 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 1ff7c1da-ab8f-3b96-b9aa-2d8f7bd2aed3 | -6.2108 | -42.6426 | 2025-09-07 13:20:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 97.0 |
| 06c084c1-d111-3fea-97e3-ca948cd8c363 | -8.1612 | -44.8521 | 2025-09-07 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 120.7 |
| b86aed95-64f6-3a7e-959e-2e1f18147b53 | -6.4976 | -43.9963 | 2025-09-07 13:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 18302926-46ef-3be5-bd06-8ff75f5d072d | -5.8216 | -44.1196 | 2025-09-07 13:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 70983ef5-5fdb-35ec-bd87-1133c99f3e2f | -14.5076 | -48.7641 | 2025-09-07 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 256.0 |
| e52971e3-2e2d-33d0-a5b1-dad55ce2da11 | -12.7832 | -52.9477 | 2025-09-07 13:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 2506e92c-81bf-3150-8a85-815e1d8805b5 | -12.9477 | -54.793 | 2025-09-07 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 43bdd539-a028-3267-8107-5fa6a6d743e9 | -11.5669 | -47.7638 | 2025-09-07 13:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| a970202c-875f-394e-9bf4-47036a39c61a | -10.4821 | -53.6115 | 2025-09-07 13:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| cc1d0bad-7f77-347b-8f77-a778fe2be093 | -6.0086 | -44.1513 | 2025-09-07 13:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 7c39f726-9adf-389e-a2fa-cf7e71baa86d | -15.103 | -48.1334 | 2025-09-07 13:30:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 3db4b8c1-3bad-3a2b-924f-5a865ee42199 | -10.4444 | -53.6148 | 2025-09-07 13:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 580952d4-48f9-35df-b667-0d3309521d0b | -11.2636 | -46.4843 | 2025-09-07 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 285.9 |
| c4c315fb-c07e-374a-b627-f9dc91835e22 | -6.3494 | -43.8005 | 2025-09-07 13:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 7c034e44-85ff-30bd-9e7b-552fc0457c20 | -8.161 | -44.875 | 2025-09-07 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 191.4 |


[Clique aqui para ver as próximas entradas](README88.md)
