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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 223e6dd5-0547-39e4-8d61-438d7c2b22f8 | -5.23279 | -50.89331 | 2024-10-23 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eba6da60-14ee-3357-94ed-2300425d82d6 | -7.98291 | -50.67623 | 2024-10-23 04:00:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15e64b9a-1833-389d-bfd0-2fab12a14c3a | -7.98218 | -50.68019 | 2024-10-23 04:00:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e75d3a68-0ad5-3ed0-902a-b9a20ed085d4 | -7.97646 | -50.67905 | 2024-10-23 04:00:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2bf3363-b0e8-38d8-90bf-18536592b200 | -4.63622 | -50.91631 | 2024-10-23 04:00:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49af317e-d020-3c22-8f60-e63b9ae2b20b | -4.6361 | -50.91331 | 2024-10-23 04:00:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93cc07ea-678e-3ded-b7b0-c9dfc8095c2b | -4.63528 | -50.91788 | 2024-10-23 04:00:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91065fbb-3ce2-391b-8f7b-a8ce49fa4564 | -4.63006 | -50.9153 | 2024-10-23 04:00:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0818afa5-1e34-3302-b8bb-f02e783e034d | -4.61002 | -50.9213 | 2024-10-23 04:00:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bdb9cdc-b1c0-3c3d-939f-e23e4e8030ee | -4.60919 | -50.92606 | 2024-10-23 04:00:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b693f812-3f40-323b-98d7-7bcb1e6c187b | -7.65368 | -38.99288 | 2024-10-23 04:00:00 | NOAA-20 | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c995c253-ea23-3a6e-b5fa-9337c3a78d92 | -6.99831 | -38.77154 | 2024-10-23 04:00:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 63003d95-a581-3a8f-8fd5-8bd06d0b78d4 | -9.37259 | -36.00204 | 2024-10-23 04:00:00 | NOAA-20 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 3df6cffd-3700-3112-a179-30d7f820d64f | -10.32216 | -36.65615 | 2024-10-23 04:00:00 | NOAA-20 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3a5f9bd1-5a87-3b50-8328-be0ba12fdee7 | -10.21454 | -36.32758 | 2024-10-23 04:00:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7d767af1-fd49-32ec-8115-7f952a25d847 | -9.45631 | -36.97909 | 2024-10-23 04:00:00 | NOAA-20 | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 43102655-036f-359d-b944-8ce28bb6a5cf | -12.61895 | -38.05212 | 2024-10-23 04:00:00 | NOAA-20 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dbca9057-dd6f-3d03-b0a8-079ff617d643 | -6.92656 | -38.13919 | 2024-10-23 04:00:00 | NOAA-20 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6acba041-3a2a-3a63-b219-cfa999ac4960 | -6.71776 | -37.51447 | 2024-10-23 04:00:00 | NOAA-20 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 07526a4e-44a2-3ecc-afaf-f797bb8315b6 | -6.71485 | -37.5101 | 2024-10-23 04:00:00 | NOAA-20 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d041c7d2-c26a-3487-b13e-c0d1dbf3dc0f | -8.74695 | -38.96824 | 2024-10-23 04:00:00 | NOAA-20 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6a892b47-e017-3dd1-a959-d9a0678f078d | -10.05248 | -39.57028 | 2024-10-23 04:00:00 | NOAA-20 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b039c3cd-ab13-34df-b2c8-0ecd3971850c | -6.44288 | -39.87642 | 2024-10-23 04:00:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 510a1535-c42f-3fae-a8e5-de35e295567c | -6.26246 | -39.59724 | 2024-10-23 04:00:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 27c97bd8-e8ff-31d2-a172-fc835663e2ff | -6.73054 | -40.48837 | 2024-10-23 04:00:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a23976bf-bf27-3f47-8b1d-3f46631e6e85 | -6.72999 | -40.49183 | 2024-10-23 04:00:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c032e988-038b-3afb-a1b1-9ba1f8b44859 | -6.72998 | -40.47052 | 2024-10-23 04:00:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c131c4db-c355-398e-9eac-bd0a184b830e | -6.72944 | -40.4953 | 2024-10-23 04:00:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 146fc6c5-6679-3a7d-b316-d7b03609e30a | -6.72832 | -40.45961 | 2024-10-23 04:00:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bb3c09e4-ff05-3763-befb-e0986ed1e7e0 | -6.72613 | -40.49478 | 2024-10-23 04:00:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 601cbf7b-a31e-39f1-b441-a84bd993fe49 | -6.72558 | -40.49825 | 2024-10-23 04:00:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1b35a495-98f4-3a08-8440-a6513c1063b0 | -6.72337 | -40.49079 | 2024-10-23 04:00:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 285e9818-9481-3904-8417-4bb54d3cc6dd | -6.71896 | -40.49721 | 2024-10-23 04:00:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ca016229-58e3-382f-860c-73da57e0a746 | -6.71565 | -40.49669 | 2024-10-23 04:00:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 94c69900-09b9-3050-a242-a55ba9846b07 | -6.71197 | -40.47503 | 2024-10-23 04:00:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c48f72dc-ac6d-35b1-977b-906d62ed3d23 | -6.6603 | -39.6172 | 2024-10-23 04:00:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 14ca4ac9-bee9-39c0-8ef0-422a678f7680 | -6.65976 | -39.62066 | 2024-10-23 04:00:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 86ab2538-c410-35a8-9186-4e7bb3f1f325 | -9.1473 | -40.65384 | 2024-10-23 04:00:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 434dca54-07d4-3f34-afab-070c5e5a949c | -9.14454 | -40.64984 | 2024-10-23 04:00:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bbb733ea-ba7e-3bff-bcb8-52cb14ad145e | -9.14399 | -40.65331 | 2024-10-23 04:00:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3cb219d4-af32-37e6-b097-dc15ca7cd563 | -9.09696 | -40.36775 | 2024-10-23 04:00:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6b880626-1d86-3056-874c-59fa0ca9c153 | -9.09366 | -40.36723 | 2024-10-23 04:00:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8912f6ed-0b5f-3617-ab25-ae7c3fcbca12 | -8.96328 | -40.59215 | 2024-10-23 04:00:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2d9cfed6-1e38-3997-bc52-f1c6bd43be74 | -8.31734 | -40.31489 | 2024-10-23 04:00:00 | NOAA-20 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e26c00b8-1897-38ec-871b-58b5ad73ecb2 | -8.11901 | -40.06354 | 2024-10-23 04:00:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cec9a16a-41e6-370b-89fc-f04feb61cc52 | -10.65758 | -40.81352 | 2024-10-23 04:00:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 68b6fe9a-6e72-36ec-bb1b-734a387e7478 | -10.65703 | -40.81701 | 2024-10-23 04:00:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e3491061-7ce6-3027-a559-b0b936276704 | -12.23889 | -40.9741 | 2024-10-23 04:00:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ba84cdd8-4e3c-3642-b480-bf14770fc24b | -11.91936 | -40.56193 | 2024-10-23 04:00:00 | NOAA-20 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bf3cbf22-20e4-39fe-90dd-47c015ab4201 | -7.33268 | -42.17726 | 2024-10-23 04:00:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fdd17eff-0d46-3fa3-8f0e-8d87edecac01 | -7.33207 | -42.181 | 2024-10-23 04:00:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e53b81e1-b4dc-316d-9a35-3799e2e752a3 | -7.10094 | -41.70075 | 2024-10-23 04:00:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7580a49f-9209-320e-bb2e-79b289699607 | -7.01977 | -40.91345 | 2024-10-23 04:00:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4abd9c42-aff3-36b5-9b75-be0ba6e5331e | -7.0086 | -41.30647 | 2024-10-23 04:00:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4023511c-829e-364e-b4d1-58da14d6cd7d | -7.00525 | -41.30592 | 2024-10-23 04:00:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 729f61f6-e174-3438-91ee-e348a87d649f | -7.00469 | -41.30949 | 2024-10-23 04:00:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| afc5c5fb-8f2c-3994-8a18-d47fc4ce49cf | -6.90058 | -40.82975 | 2024-10-23 04:00:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 154b1d9d-e0e9-3534-b851-0b67555f5b88 | -6.89781 | -40.82572 | 2024-10-23 04:00:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| be995aac-a881-3241-894f-6462b791704d | -6.89726 | -40.82921 | 2024-10-23 04:00:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4def56fd-bd46-3a63-8ff7-b7f4b0d7dc45 | -6.456 | -41.78318 | 2024-10-23 04:00:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6062419f-6ece-38ea-b9cc-fb629a767d43 | -6.4508 | -41.79378 | 2024-10-23 04:00:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2b6f90dc-0307-385e-a0ac-69891fb4e989 | -6.44832 | -41.7441 | 2024-10-23 04:00:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 66ba55aa-be06-313a-9aff-6327437e58ab | -6.44773 | -41.74778 | 2024-10-23 04:00:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1b2b334a-e5f4-35ec-a548-30e084cb8b87 | -6.44739 | -41.79323 | 2024-10-23 04:00:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dcbe7adf-eb45-37f0-b2d2-bdceffd2c20e | -8.91388 | -41.14099 | 2024-10-23 04:00:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 3740aee6-cbbd-3a06-bf9b-200cc4cfb6f7 | -11.65985 | -41.92961 | 2024-10-23 04:00:00 | NOAA-20 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 44547e79-97fd-3697-be92-23672eff1db9 | -6.32564 | -43.44431 | 2024-10-23 04:00:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b1a9164a-23d7-31d9-9867-f467bbf14320 | -5.77024 | -42.64185 | 2024-10-23 04:00:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 87209f08-d999-3e91-8259-b4803d0c4cfa | -5.70595 | -42.5011 | 2024-10-23 04:00:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d8b99806-dfca-3e46-9e6c-84f5b17fbca4 | -5.7018 | -42.5044 | 2024-10-23 04:00:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bedaa48e-e134-3af2-9dd9-a5cfabf04d61 | -5.6989 | -42.49989 | 2024-10-23 04:00:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f23050a6-2d5e-3313-9c87-7ba817879dee | -5.69826 | -42.50385 | 2024-10-23 04:00:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2f999b3b-8f60-3e0d-b8fd-a07b1c885559 | -5.69538 | -42.49931 | 2024-10-23 04:00:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2e62ba4f-b1dc-3b9b-bb6b-e45b4cdd0ae5 | -5.69473 | -42.50333 | 2024-10-23 04:00:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f74a0e16-3b0e-3881-b755-2c35f41d9ced | -5.70366 | -43.25957 | 2024-10-23 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc9e0ff5-e208-3f07-b28d-2473eff4d77e | -5.64783 | -43.23287 | 2024-10-23 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 23ff8358-4833-386f-b5e1-58598c15ab44 | -5.62904 | -43.27832 | 2024-10-23 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9a51502f-a7a9-3f44-af80-5dda26a9bb9f | -5.62323 | -43.29068 | 2024-10-23 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f2aade72-a4ba-3648-a25e-0d87a025ba16 | -5.61955 | -43.29006 | 2024-10-23 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 4aaaf1ed-c4b9-3c99-bcf3-010b87da001d | -5.58842 | -43.20675 | 2024-10-23 04:00:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5973b642-7140-391b-970f-8bd499076654 | -5.57812 | -43.20073 | 2024-10-23 04:00:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7d99b68a-3d81-30e7-b581-4076e3a2cf0f | -5.57707 | -43.25354 | 2024-10-23 04:00:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 0698ff5b-a0ec-3778-b433-c1d484f5e0ea | -5.57638 | -43.25784 | 2024-10-23 04:00:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 81ad7de7-57fc-3033-b3de-eca09232c2e4 | -5.57568 | -43.26213 | 2024-10-23 04:00:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| d7ae9d7e-1e04-300e-9e20-6bbfec7794c8 | -5.5734 | -43.25294 | 2024-10-23 04:00:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| a571a99d-6982-3055-bf21-9f805fccaaa1 | -5.5727 | -43.25724 | 2024-10-23 04:00:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 405fee75-e5d2-356c-87f9-122573cd936e | -5.572 | -43.26157 | 2024-10-23 04:00:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 2aff86c1-7477-3e6b-bd3d-60f662c7657f | -5.56973 | -43.25235 | 2024-10-23 04:00:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebecb755-ca9e-33aa-abdf-57113d94f9ae | -5.56903 | -43.25666 | 2024-10-23 04:00:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 831fed67-49ce-3694-87b4-cbe6e6786df4 | -7.60839 | -42.3407 | 2024-10-23 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 80461c88-801d-3d8c-8833-956258ee221f | -7.60495 | -42.34016 | 2024-10-23 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f23da6e0-bd1c-3fe9-bc15-704af59dbd64 | -7.57415 | -43.60086 | 2024-10-23 04:00:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36b5d6de-b9b8-35f1-a41c-bea54660eb75 | -7.49576 | -42.90699 | 2024-10-23 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dee6ac90-eb0d-3782-ab06-b3573c0189de | -7.49511 | -42.91099 | 2024-10-23 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aced1ed2-d9e8-318f-9176-ea0a3be5d398 | -7.44629 | -43.62532 | 2024-10-23 04:00:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2fc937b7-5779-32ec-bd44-8bf446022c89 | -7.44263 | -43.62471 | 2024-10-23 04:00:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 955fd0de-eaf6-3792-902e-d6d529c0a5a2 | -6.79919 | -43.43468 | 2024-10-23 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ffabd90e-b057-373e-b826-f028ce840a25 | -6.68544 | -43.53331 | 2024-10-23 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3bdd5ed2-4f19-3e6f-ba66-c3002e14a27a | -6.67964 | -43.0433 | 2024-10-23 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a022b631-e8ba-3c92-ae13-db136faa657e | -6.67897 | -43.04741 | 2024-10-23 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README25.md)
