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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fed7074d-bd79-39c6-960a-aaeffdd21b0b | -4.0031 | -43.27569 | 2025-10-14 03:34:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1aebb88-5ca6-31ee-bf27-aa686673abe0 | -4.45693 | -40.77697 | 2025-10-14 03:34:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cde6123c-5d68-316f-a3c3-e728fcb1c337 | -4.43006 | -38.9603 | 2025-10-14 03:34:00 | NOAA-21 | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6c3f017c-4587-3a00-a7e8-620430a946bf | -3.86234 | -42.71281 | 2025-10-14 03:34:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 056113cd-283a-3369-b068-915f1408aa5e | -3.86209 | -42.71272 | 2025-10-14 03:34:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 332218a7-a2b6-3059-8068-43fbac730f6c | -3.05452 | -40.8135 | 2025-10-14 03:34:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a07bc72c-a532-3d8a-9dba-d446af1e22b2 | -3.15893 | -42.88765 | 2025-10-14 03:34:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0eac56a8-addf-387a-b72a-2d100614edba | -3.04175 | -40.11451 | 2025-10-14 03:34:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 3b82c4a7-af7e-3963-af97-dfec5e9791b9 | -5.13669 | -38.07 | 2025-10-14 03:34:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f0e63c98-6916-3fd6-b567-91222e05ef39 | -3.04257 | -40.10954 | 2025-10-14 03:34:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 654e1877-71ba-31f1-9c23-6d88ba860716 | -3.04644 | -40.11523 | 2025-10-14 03:34:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 896af93f-2df0-3fe3-9aaa-af87c6e9965f | -3.15263 | -42.89061 | 2025-10-14 03:34:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7245bbb8-490d-3de4-b722-baa75d23455b | -3.29431 | -43.50158 | 2025-10-14 03:34:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 88424627-d646-3a0c-8520-69006e997c2c | -2.84593 | -45.45728 | 2025-10-14 03:34:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6eee08c6-103d-3396-b318-9a922bd7413e | -3.70329 | -43.2098 | 2025-10-14 03:34:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a40bbdb4-8165-3c83-bfb0-53692e807cb6 | -3.7026 | -43.21381 | 2025-10-14 03:34:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 30da1b37-00f2-36e6-b2c9-259435143400 | -4.66704 | -43.12003 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| cff94b21-c348-3af0-8718-c604d8a50a8f | -5.80389 | -35.53432 | 2025-10-14 03:36:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7e17ae7f-6ffd-3e62-8a4a-d4416b676407 | -5.10575 | -43.19822 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b11132fa-b877-31dc-86b1-ff33dfae99e7 | -4.74301 | -45.65532 | 2025-10-14 03:36:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0707f46b-fc73-3bcd-95c5-b754aaeff15d | -5.8843 | -42.90977 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 72a9d8b4-bf33-3951-994a-068703fff564 | -5.4085 | -46.01643 | 2025-10-14 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0cfaf7bd-36eb-3e55-acbf-b2b099db1ecc | -6.988 | -38.44499 | 2025-10-14 03:36:00 | NOAA-21 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8847c0db-c3b3-3c13-9002-8ed283528f03 | -4.91672 | -41.53214 | 2025-10-14 03:36:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 72941e62-2dce-38a4-8e7a-0065f75d794c | -7.94496 | -44.11468 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7106b18d-5af0-3f4a-9912-1f2c83a27ef0 | -7.91054 | -45.00683 | 2025-10-14 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c459a7a6-dbbc-3e42-934e-cb7c1fa4ae1e | -6.29195 | -42.98573 | 2025-10-14 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da4874cb-5155-309f-9697-d01918580268 | -4.66384 | -43.13906 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4eac7a4a-d062-3b04-aaee-a2fadfd16fe6 | -5.88131 | -42.88233 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| bee6bb45-f08e-3eb4-85a4-098e5d8d54fd | -5.26484 | -41.00518 | 2025-10-14 03:36:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0110d255-7508-3fdf-9a86-86c59ecdac1a | -5.21668 | -41.64545 | 2025-10-14 03:36:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0d66b187-8c28-3b99-a9a1-549e41747dac | -9.49331 | -43.06044 | 2025-10-14 03:36:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fd447e01-c0da-3c33-bacc-fd69b2129151 | -5.99419 | -42.86846 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e69619fb-15e5-3524-abc6-2006b7235cd1 | -8.39706 | -45.05634 | 2025-10-14 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a94fb8d-020c-33a8-ba20-1543b4ccf817 | -7.90058 | -36.4344 | 2025-10-14 03:36:00 | NOAA-21 | SANTA CRUZ DO CAPIBARIBE | PERNAMBUCO | Brasil | 2612505 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fc9098d9-91c0-31a0-8da8-9f79843fb71c | -6.44173 | -41.8331 | 2025-10-14 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 442a6fd0-4edd-35bb-a021-0708902bcc21 | -4.62203 | -45.7813 | 2025-10-14 03:36:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4ffab4d7-f374-3a33-8ccd-058e849328e8 | -6.99203 | -42.79737 | 2025-10-14 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8a5339da-85e3-3bab-8ef0-f7c385461185 | -4.83983 | -42.76518 | 2025-10-14 03:36:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| abf233a9-9ba8-3d54-a410-97e5d77f61c9 | -6.53986 | -43.5638 | 2025-10-14 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6b75370d-1dcf-3a83-a3c5-8b85bc10ea19 | -6.54056 | -43.55995 | 2025-10-14 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b21512cf-6475-38f2-bcaa-1f0132b59c5e | -5.88733 | -42.9122 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 762a4bee-f7ae-372a-8efb-ce63a264f48a | -7.16755 | -42.19482 | 2025-10-14 03:36:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4898d223-a46a-39ea-a5b8-68dfc066eccd | -7.62854 | -47.83712 | 2025-10-14 03:36:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0c86a96b-b6fe-3f43-8883-86af2c8a3f10 | -7.91197 | -47.21146 | 2025-10-14 03:36:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5ac57df4-5182-36e2-a18f-550d92466616 | -7.40293 | -39.78949 | 2025-10-14 03:36:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 8ad734c4-7441-33a4-8da4-33d403f3650c | -6.53596 | -41.6241 | 2025-10-14 03:36:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 31db2977-631d-3011-aa81-dc3417caa8cf | -10.17106 | -36.39227 | 2025-10-14 03:36:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| cfb6759e-29c5-31ed-830a-2101b175e3df | -4.82694 | -43.20832 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92853c92-d595-3819-bcbb-ac10bdd62717 | -4.74469 | -45.6513 | 2025-10-14 03:36:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| adbf6335-90ff-38c3-b50a-ceea6ddb99ce | -10.16887 | -36.38424 | 2025-10-14 03:36:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 14ecdc03-f546-3bb2-a561-c0226ddaa8df | -4.83379 | -42.76774 | 2025-10-14 03:36:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 9a9014a1-e790-3fa8-b46f-c654e73bd100 | -5.91782 | -42.81519 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b3727729-1cac-32ad-b85e-180b783c0871 | -5.99354 | -42.87205 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 964d5e67-95fe-323d-80a7-052c1b7aebd6 | -9.00676 | -47.35215 | 2025-10-14 03:36:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ac86550a-71c8-318a-9057-d0e660046336 | -7.92088 | -44.1184 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 938e865a-32b8-3dcd-aa82-79fc8da75f39 | -5.87051 | -42.88037 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5c0a791a-bd12-3b37-ae5c-8e4fdcaea49e | -6.14477 | -41.76152 | 2025-10-14 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 76a3f649-faaf-3e4e-8fbe-d1f92a585d95 | -5.11949 | -45.49602 | 2025-10-14 03:36:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0d919e10-e75a-3c09-82d4-697cf25c2756 | -5.9119 | -42.81738 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 47e04759-231a-304a-b3d9-4b2e54df1465 | -4.62108 | -45.78675 | 2025-10-14 03:36:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 893ce913-39ad-3ae2-87e4-53cbe5f1d82d | -7.74794 | -42.43912 | 2025-10-14 03:36:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a5b111d1-dc49-3b66-8786-874070077668 | -6.22035 | -41.55767 | 2025-10-14 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f9084cf5-875c-3f23-9bae-cc83714e6549 | -5.86418 | -43.85291 | 2025-10-14 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd3f6f62-1a58-3d31-9b3e-379c859a9e05 | -6.53427 | -43.56285 | 2025-10-14 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d641fb97-ff32-35dd-a724-c30f8059696d | -7.39934 | -39.78469 | 2025-10-14 03:36:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 24.2 |
| 9c302b6b-e5f4-3e85-ac43-1de40a7441bc | -4.66528 | -43.11949 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1d494cff-febb-3577-b662-e026f47c8fbb | -4.67088 | -43.12043 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 68f48f50-59e4-3da7-8bef-4c3f4d8093c1 | -7.29114 | -41.95973 | 2025-10-14 03:36:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3701b893-1c97-3181-9d73-9f6331ee2073 | -7.91417 | -47.20574 | 2025-10-14 03:36:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b423604b-64fe-3134-afbc-b500609fd392 | -8.21648 | -43.3227 | 2025-10-14 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5167df71-21c7-3c53-ace1-6e314392d13d | -7.9187 | -44.13004 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0a03fa40-40db-3466-b262-19568e0e5eb8 | -6.43597 | -36.89094 | 2025-10-14 03:36:00 | NOAA-21 | SÃO JOSÉ DO SERIDÓ | RIO GRANDE DO NORTE | Brasil | 2412401 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8740df95-26fe-342b-af20-e959bc91391a | -5.89035 | -42.90712 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 98ccbd2b-da7d-3cb4-ad94-ba0f8e28a2a1 | -5.48419 | -45.40859 | 2025-10-14 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 821681a6-e296-3e44-8f5a-8455eff01c15 | -10.1757 | -36.38538 | 2025-10-14 03:36:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8fa6522a-0902-3999-b21f-6e391156a0f6 | -6.99186 | -38.44607 | 2025-10-14 03:36:00 | NOAA-21 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8e4c6c62-c82f-3796-ac50-401085331366 | -7.91292 | -47.21217 | 2025-10-14 03:36:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 08ae9cfa-ced8-32c7-81bf-6fbb88d33e60 | -7.89938 | -45.00035 | 2025-10-14 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2822f0c4-1a5d-3344-941e-b88ec89e3f28 | -7.93787 | -44.12136 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bdc778c-e6de-32b4-9298-57caa13d03c4 | -5.38976 | -43.22738 | 2025-10-14 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf5e424b-6fec-3d48-8049-e3cc123cda9d | -7.92924 | -44.12219 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe5f5d57-cbb8-3d9d-b940-dc51158dfe15 | -6.16212 | -43.7534 | 2025-10-14 03:36:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ff4dac17-eebf-3b6f-9c2f-47545430b3a8 | -5.99722 | -42.86856 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| dcd43f0c-a252-3eba-bdfa-4cc8fd02ef45 | -4.61951 | -45.78273 | 2025-10-14 03:36:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ab3687bc-3198-3108-8c66-36d11c976ea3 | -10.17508 | -36.38912 | 2025-10-14 03:36:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c2e70817-406c-3056-b2c5-63cef2692740 | -5.4084 | -40.88622 | 2025-10-14 03:36:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c0f3664b-ac5e-3b4b-87f9-bb246b323ef4 | -4.67382 | -43.13657 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 77e0d514-37b0-3fd4-abdb-3279768c15d0 | -5.25117 | -45.24154 | 2025-10-14 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c085999-15bc-39c1-a003-be5e71793093 | -5.56592 | -41.31961 | 2025-10-14 03:36:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2af0c076-5092-309e-9764-77c8faef344f | -4.68633 | -43.13095 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73174094-c6ad-3d5b-9402-083f3501e2c1 | -5.33411 | -45.1946 | 2025-10-14 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 26d5a97f-6275-30ff-a467-6521fbc3a984 | -6.44275 | -41.82726 | 2025-10-14 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 81b1bda9-0dcf-3f37-980d-f5439d470163 | -4.6688 | -43.14388 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 167c52af-8750-3121-90b4-3137c4514b9c | -6.44224 | -41.8302 | 2025-10-14 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6a22d4e3-bc40-3a43-8b18-c8359b27cc69 | -4.84045 | -42.76865 | 2025-10-14 03:36:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 93c94078-879f-3120-8603-993d844ba08e | -7.92436 | -44.13102 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 19deb57a-c591-3c42-8fe5-f081f6d5d95f | -7.94845 | -44.12735 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6e329c4c-dfc6-388a-ac68-1754a631251c | -4.84116 | -45.21119 | 2025-10-14 03:36:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81557676-1938-3a65-881e-32f0c01242d4 | -6.57673 | -39.24617 | 2025-10-14 03:36:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 12.6 |


[Clique aqui para ver as próximas entradas](README7.md)
