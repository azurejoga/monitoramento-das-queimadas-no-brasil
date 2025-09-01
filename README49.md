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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f030f06-118f-378f-bf03-c6d337786c7b | -6.79362 | -52.81477 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6865cfe9-4fca-34cd-8260-6d54d096bc25 | -8.84239 | -47.50531 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5375acbb-bce4-3feb-ac25-0d1b697d7c9b | -6.44017 | -43.96754 | 2025-09-01 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1762389-9d8b-3d7d-9d71-9dd8bfd14924 | -5.49306 | -45.60226 | 2025-09-01 04:32:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf627a3f-9428-3340-8e2c-48347bc5dc6f | -6.3072 | -44.76595 | 2025-09-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e7f694e-eb21-3448-b691-f8a05ba1bff8 | -7.69967 | -61.47542 | 2025-09-01 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 972a8f1b-a109-39fa-8ebf-5be2f9e20202 | -6.7726 | -44.62379 | 2025-09-01 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4763c682-63d0-3e28-8b89-55cd2af0b5bb | -7.88259 | -46.99983 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db02fc98-728e-3096-8d69-0af86147ed5d | -6.84038 | -43.33611 | 2025-09-01 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ff2ed8c3-f6d6-3451-8a84-bd55d7a2e46f | -6.30638 | -43.61883 | 2025-09-01 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 305d43c3-d986-3636-a2d3-beb955648973 | -10.57913 | -44.85511 | 2025-09-01 04:32:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9c40b62-6bad-39b5-abcc-531050825a8c | -7.953 | -46.45328 | 2025-09-01 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e83642bd-035b-3a31-a598-8d456c601c2b | -7.10005 | -44.55962 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dd0a8b7d-66e3-355a-b8e2-3f28c7a9bf36 | -6.2806 | -43.52641 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e9fc4b8e-19c2-3c0b-899c-763d5510afe1 | -6.30099 | -43.54882 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5bdcc77-9bee-3429-a40b-bf1affa158dc | -6.80864 | -52.82254 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b23aa0b-0364-351b-a54b-172f95eaf3fa | -6.30905 | -44.76721 | 2025-09-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 910d1633-a4ea-38cd-addc-cbb0bb388864 | -6.84057 | -43.33945 | 2025-09-01 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e1c1d5ae-b913-3ef6-a799-7e808a2c9aaf | -9.49839 | -48.84613 | 2025-09-01 04:32:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2abf3eb8-1a8f-3292-adca-f0b8d9153f3f | -6.63867 | -43.95707 | 2025-09-01 04:32:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03b6570d-6559-343e-8f55-b0ba54952617 | -7.94617 | -46.45228 | 2025-09-01 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c569e53-6091-30c5-b313-c1c944d6aa70 | -7.71268 | -50.30818 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b9d0eae-339f-35c9-b0f1-c2ff1788af67 | -4.07782 | -47.96119 | 2025-09-01 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 527e901e-459e-3fea-91df-98830880b504 | -6.83897 | -52.81195 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0928239a-dd77-32fc-b2e2-daea621ed293 | -7.10941 | -44.7685 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b358610f-2210-3c10-86cc-31d38b9547ad | -8.34638 | -52.53607 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1aaf6b91-f4e0-3fe9-86d1-07af77a7c845 | -7.70904 | -50.265 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f57a764-ea38-3ba1-9350-0f200f09f2ff | -5.58762 | -46.3258 | 2025-09-01 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f62dd99-e303-3b2a-b7e4-f824643f22fd | -9.01606 | -50.12025 | 2025-09-01 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f2ef0c0-5233-3284-9567-29304416d30b | -10.57536 | -44.85453 | 2025-09-01 04:32:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83d67236-bd70-342c-81dc-0eb96dfb6acf | -10.03625 | -48.07957 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7cc4d75a-fd98-31d7-b6c4-66bc39030f7d | -9.27761 | -47.10742 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90060d01-b299-39f6-a98b-c7d41a5ab485 | -7.11369 | -44.7648 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fed75630-be45-3862-a5e3-b7a8c9213e96 | -6.30284 | -43.64267 | 2025-09-01 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 43cf23c6-d44d-3a0f-b94b-af95e0bcbf2c | -4.73178 | -44.44568 | 2025-09-01 04:32:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 805fca02-e82a-3039-9b6a-624f24dd54ba | -7.67798 | -61.09268 | 2025-09-01 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9621a9fe-d038-3e6f-b521-88ac1c1e1c18 | -9.22534 | -47.11044 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 639a786f-e894-3048-b9fe-160cc237bf47 | -6.30255 | -43.61816 | 2025-09-01 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d5376ba4-fb57-3a32-b38b-5c637c622409 | -7.45874 | -44.83035 | 2025-09-01 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be25f8a6-0e5b-3606-99c5-5c06e13ed7c6 | -6.165 | -44.12141 | 2025-09-01 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28d355fa-f075-3b68-9d9b-a3eecf8731cb | -11.08417 | -44.62411 | 2025-09-01 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 243bc805-7032-3e9c-b8eb-aeb195fbea69 | -7.46064 | -44.81781 | 2025-09-01 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ca7ea46-7ac1-31f5-b77d-9179768e3453 | -7.23572 | -45.4182 | 2025-09-01 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da4b7321-cd9f-3177-af2e-d679ff80d721 | -6.8645 | -52.80548 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7b108b7-c526-366b-b5cd-b53269d75425 | -6.24148 | -42.41834 | 2025-09-01 04:32:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 87a34157-0b63-30c2-bef0-8f4ffd87f8a3 | -7.95006 | -46.3582 | 2025-09-01 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7f374ac-fd36-3af9-b752-92ebc040109a | -7.37023 | -43.38636 | 2025-09-01 04:32:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 343ca9a8-1730-3ad1-b7e6-b9fde5f1d999 | -6.12953 | -44.12951 | 2025-09-01 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b46aaee-6277-3f6e-acac-3b07df099a89 | -7.40853 | -47.42916 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcf5f38d-85be-343b-9fee-593a3f7d57bc | -6.29874 | -43.6174 | 2025-09-01 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 65271137-f531-3bfa-bb02-ff66ee3dab9a | -6.36969 | -43.56408 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd93a220-0ad0-396d-94b3-7ed4a7d7dd00 | -6.1973 | -45.3738 | 2025-09-01 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d72ca1d4-ec75-3cc1-90f3-7e6248bdca2b | -6.46774 | -41.74584 | 2025-09-01 04:32:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fb27f24a-1c84-3240-a4fc-dd8954825a52 | -6.33662 | -53.4368 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23d779d9-bd63-3d3d-bcdb-b630b7b51c55 | -6.45724 | -43.95634 | 2025-09-01 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c10cb5be-58a7-3ec6-8bcc-2774808da747 | -6.26482 | -43.54105 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 967564c9-ae46-3e0a-aef3-c3c292a96d2e | -6.57687 | -43.71866 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 042bf206-fdcd-3332-9631-5a02af8b29ca | -5.99515 | -43.3678 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 815fa88b-b8c7-3b79-9179-2230bd9b3128 | -5.49172 | -43.19666 | 2025-09-01 04:32:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cffbc58e-542e-3cca-95cf-da36aad316d5 | -7.07073 | -44.35337 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d64fa396-148d-3499-98a4-93ec1e1965f9 | -6.85657 | -52.80416 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 371d7bb5-4d7a-3dbf-929a-ea6308775087 | -6.81472 | -43.35085 | 2025-09-01 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8d734917-e78c-3457-85c7-a8b2f42603a6 | -6.45349 | -43.95564 | 2025-09-01 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5c1965d-ae33-32a1-99fe-74c02df6e29f | -5.62289 | -45.13815 | 2025-09-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6c59450f-81e6-3cd9-8cfe-6e156a5ba04e | -6.30809 | -43.63372 | 2025-09-01 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a23df495-48d0-37d0-9d2e-82e13fc4ea90 | -9.27759 | -47.08514 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae22b560-2216-328c-826c-152c624c2951 | -9.68726 | -48.29409 | 2025-09-01 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3649080-9f70-3c62-8529-fcf49ec53de7 | -3.81387 | -48.95197 | 2025-09-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37c5a318-53d2-3733-bacb-79d45643429b | -9.15571 | -45.22162 | 2025-09-01 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19a52089-8060-33a6-a742-712e4f329731 | -7.71652 | -50.26237 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6384772b-89a4-3c3f-af2d-59d659e05dfe | -9.6371 | -46.60938 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e05816b6-5708-3232-9751-c406c79777b8 | -7.69845 | -61.48169 | 2025-09-01 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 719673ae-5bd7-3c62-a307-0d4e293078ef | -6.95577 | -44.3466 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c2bd179-d391-3efb-bb96-98f009bebf92 | -6.78293 | -44.62961 | 2025-09-01 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a639f5c4-b941-31d9-94ab-2e8d4b639f56 | -8.47599 | -45.17215 | 2025-09-01 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68a6d185-defa-30f9-98fa-7984bed42316 | -6.15477 | -43.34351 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e33af205-eb09-31dc-a252-2c9364c17dda | -6.33923 | -58.18302 | 2025-09-01 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47768b66-62bf-335e-8265-9d9c84967707 | -4.27308 | -48.63842 | 2025-09-01 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e410fca-68d2-396c-a679-e1cf9e66159f | -7.00333 | -44.35854 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2684d710-497f-353f-b7b8-3b201f1fffeb | -6.28242 | -43.29281 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b9bf47f-07a9-3330-9f89-f5db5cb87dc4 | -11.03951 | -45.14684 | 2025-09-01 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| b136c587-9676-38ba-b244-1e8025ac2c0e | -9.64424 | -48.3513 | 2025-09-01 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffbeda23-2e7c-3a55-ba37-c82262e17935 | -6.5737 | -43.71352 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7dc71c23-1ce9-3ba3-bb87-649288c6aab0 | -7.76561 | -50.32478 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9ca454ae-559e-3a1d-9a6b-9f2d45c7e9a3 | -7.11068 | -44.76002 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fa39e7d-b312-3143-9eb1-b225edd9de9b | -6.83244 | -44.24353 | 2025-09-01 04:32:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d487fbb-b282-3837-888d-d0c0f2979edd | -6.78356 | -44.62541 | 2025-09-01 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3315b5a0-8e46-320e-a479-09037e6d0d48 | -6.81228 | -43.34022 | 2025-09-01 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b6b1ef08-03eb-3b30-968d-d88941745b0b | -7.24163 | -44.06149 | 2025-09-01 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8facd8d0-aa4e-38d2-8ad2-581a261b1d76 | -6.81049 | -45.6888 | 2025-09-01 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48b46310-8927-352d-9fa6-5e31c1cbc1a1 | -8.84627 | -47.50229 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6371d0ad-7acf-3325-bcce-4d42139869f2 | -6.16087 | -43.32938 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 102b19d0-a5f0-3acd-89f8-02a7930c2bfc | -6.85174 | -52.80872 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c9908e5-9865-36cf-b61b-4727c4d85778 | -6.26025 | -43.5452 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5dfefc7e-5c3d-3afd-ba37-c5675ada17ad | -6.35888 | -43.55732 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 604642d9-d6e9-3eaf-bd15-988c9b1a85cf | -5.31727 | -45.44955 | 2025-09-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e7983289-fcb7-34b1-b069-46ed0543dac6 | -6.61079 | -53.12915 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 513a9640-feff-36ca-a7ad-77f78aa97154 | -6.41753 | -43.96122 | 2025-09-01 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c05f2e2-5784-3ec4-8475-67087ad55808 | -6.19008 | -43.35001 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a1446e3-6ab4-3e3c-a989-3ab4edd9e007 | -7.10722 | -44.31311 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README50.md)
