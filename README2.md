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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b3460c8-a512-399b-8aff-06fa8df297ac | -3.24834 | -43.26436 | 2025-08-08 00:09:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7fbae534-b4be-3c3b-8b0f-fadab991802d | -10.46477 | -44.39717 | 2025-08-08 00:09:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4f6a9eed-66f3-3c61-9a72-dfc435aed864 | -3.82357 | -41.56596 | 2025-08-08 00:09:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| b713b94c-44a9-39ec-b3d5-9903dfd64637 | -10.63428 | -44.75871 | 2025-08-08 00:09:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 33.2 |
| f12a6c7b-a15d-3263-94a3-6606fe00c1b4 | -6.95964 | -42.86058 | 2025-08-08 00:09:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 6c1d4006-5fd2-3966-98f6-7bb744d3be30 | -9.07273 | -45.06855 | 2025-08-08 00:09:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 47.9 |
| cd188d59-0e04-3f20-b891-5bd5fd8ba4be | -7.90453 | -45.34094 | 2025-08-08 00:09:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 5b69526f-c4fd-325f-9118-e4584d778660 | -5.98278 | -44.14678 | 2025-08-08 00:09:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 235.0 |
| 64a15d40-58cd-394c-882f-c69265f4510c | -8.21539 | -45.06573 | 2025-08-08 00:09:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c754f0b8-fc4f-3b75-a8fb-96f8d9d4a6d8 | -7.24127 | -44.65104 | 2025-08-08 00:09:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4a91b71b-867e-3ca9-b654-5ef1ce4eab69 | -5.98411 | -44.15678 | 2025-08-08 00:09:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 218.4 |
| 12920583-42c6-3286-babc-eeb076b7331d | -11.02899 | -45.05702 | 2025-08-08 00:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f4caa872-4297-39ab-a6ce-8d8b24090eeb | -7.89266 | -45.33017 | 2025-08-08 00:09:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 6ad180f1-4086-38be-a8ab-8b78578ef03a | -8.16128 | -42.4218 | 2025-08-08 00:09:00 | TERRA_M-M | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| a0dce931-8c77-37a9-bc8b-10c01eb13fbd | -4.9193 | -46.73576 | 2025-08-08 00:09:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 8f48e965-8efb-36b8-a369-12505f6160a4 | -10.42881 | -44.35458 | 2025-08-08 00:09:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 3adeb639-a5aa-36bf-9ed8-6263296b1366 | -5.57064 | -46.53041 | 2025-08-08 00:09:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 43f99988-7ac0-37cb-a77f-401f643142a8 | -8.93072 | -46.74835 | 2025-08-08 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 921874bb-d131-35c5-8a3a-8348b2629eea | -8.06705 | -49.72691 | 2025-08-08 00:09:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| a0a30f4d-40f1-3bda-aad9-e37adce5c05c | -7.10631 | -44.22814 | 2025-08-08 00:09:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5bf0de0f-9abd-3199-bdc8-ba75e5c9fc73 | -6.42932 | -41.75192 | 2025-08-08 00:09:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 452f1bcd-27bc-3213-9156-05460771da28 | -7.2459 | -44.66667 | 2025-08-08 00:09:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 3426a7a9-b5c6-3181-9b39-48ea2f594c08 | -3.82231 | -41.55691 | 2025-08-08 00:09:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 1a555afb-1faf-3b1b-adab-1b67cf1d0b6f | -9.65021 | -43.85801 | 2025-08-08 00:09:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| d8cd76ea-03ed-3b08-9fa9-efe6e4966580 | -7.90948 | -45.54492 | 2025-08-08 00:09:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 560f6973-f092-3dc5-bdae-c6a06964fb18 | -6.68409 | -43.33605 | 2025-08-08 00:09:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 9ce26293-583f-3735-b2d5-00bf573ae124 | -10.63589 | -44.77108 | 2025-08-08 00:09:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f6b81937-1503-3e9c-8055-d373c90f4cbd | -3.66596 | -41.75666 | 2025-08-08 00:09:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 24.7 |
| 21e2c2fd-91c3-3bb1-b145-7703f181ae73 | -8.53141 | -43.31533 | 2025-08-08 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3896e141-3a35-39dc-87ba-7a723dcd402e | -3.65705 | -41.75794 | 2025-08-08 00:09:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 8849d7a0-0e84-3222-8636-c27968f76d5a | -5.28042 | -41.77815 | 2025-08-08 00:09:00 | TERRA_M-M | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 98bffa75-39f1-30cd-9329-b07fd1e4ebb9 | -6.28859 | -44.22849 | 2025-08-08 00:09:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 7c0cf3ca-7d08-3604-a5e7-85a5a4eb64e3 | -6.12619 | -42.95853 | 2025-08-08 00:09:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 25.7 |
| ed1e72b3-8238-38f5-80aa-9f797789dc7f | -11.03065 | -45.07002 | 2025-08-08 00:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 406caefc-a199-3e1f-b11b-88a0af3d81df | -5.9885 | -40.38381 | 2025-08-08 00:09:00 | TERRA_M-M | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| fbedbed4-32bb-3c1e-a1bc-f0b9d32a36b6 | -6.96859 | -42.85933 | 2025-08-08 00:09:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 52b7afea-d055-3ba8-a2de-e814f39320ef | -5.83178 | -44.10957 | 2025-08-08 00:09:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f3119633-eee6-3d6a-9227-82b17f538cc3 | -11.02005 | -45.07139 | 2025-08-08 00:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 66018383-e38e-3389-b661-07a2562619fa | -9.6598 | -43.85681 | 2025-08-08 00:09:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 34c89059-732b-31a4-806c-deea6a76de23 | -5.97583 | -44.14396 | 2025-08-08 00:09:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 21147c9d-7f3f-3b00-9790-7003be9d2a0f | -4.78055 | -45.32927 | 2025-08-08 00:09:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9ee58253-0858-3613-b204-79bc4dc031fc | -6.69976 | -43.3186 | 2025-08-08 00:09:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 113eefed-2ba5-3582-8964-afc700cd6e56 | -10.62399 | -44.76006 | 2025-08-08 00:09:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 34c19e7d-5971-3986-87c2-0db5b95b8f3a | -3.82484 | -41.57499 | 2025-08-08 00:09:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| c9ce0aa1-d447-3576-a398-29637d1830fa | -6.12743 | -42.9676 | 2025-08-08 00:09:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 0550a47f-f532-34c4-8f56-d52a60488e66 | -6.85138 | -44.31261 | 2025-08-08 00:09:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 330aa857-3134-3e9f-92ec-d6cc73b18554 | -8.5209 | -43.30696 | 2025-08-08 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 0258c639-23ec-300e-bac2-3d05da71744b | -8.86861 | -47.2803 | 2025-08-08 00:09:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 40711bed-8c57-3083-b687-1a7ca5019d54 | -7.1158 | -44.22685 | 2025-08-08 00:09:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4f1e294a-7904-3694-a3ef-62c8668f6f25 | -7.24448 | -44.65577 | 2025-08-08 00:09:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 507ed689-dac5-37bf-a686-3b5ca6251be6 | -9.60663 | -40.5623 | 2025-08-08 00:09:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| bb72911b-0d9a-3b32-9c8d-9e437c684bff | -4.80466 | -42.85498 | 2025-08-08 00:09:00 | TERRA_M-M | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 116f0315-dc7e-395c-a623-07870d62fdc4 | -6.63804 | -41.86345 | 2025-08-08 00:09:00 | TERRA_M-M | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 2620b017-e65a-3de5-a540-3ef923bc9708 | -10.82757 | -49.38618 | 2025-08-08 00:09:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 0857d008-9f6b-3a73-93a3-9e4218d13669 | -7.25997 | -44.3275 | 2025-08-08 00:09:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2d5715e4-410d-382b-a10b-d88fc9c11076 | -7.3856 | -44.65215 | 2025-08-08 00:09:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 8e4bbf81-a318-3cc5-a2e6-341236742686 | -7.58323 | -44.90893 | 2025-08-08 00:09:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1628fb35-5db7-3269-bf31-1cd461f9545b | -6.54111 | -43.91235 | 2025-08-08 00:09:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 880126fd-e98d-3253-8961-642ad7617082 | -6.46583 | -44.57541 | 2025-08-08 00:09:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7fc2bc29-ef7e-336f-ac6b-33a0ebce7039 | -5.9813 | -44.18375 | 2025-08-08 00:09:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1f2c8b73-51a5-3244-8c58-00d22ac52e31 | -10.75519 | -44.43542 | 2025-08-08 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7c7de6ee-7788-3ad5-b776-650912c125e7 | -10.82695 | -49.37975 | 2025-08-08 00:09:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 8f431743-2f5f-34e8-a226-c31263e04416 | -6.28724 | -44.21841 | 2025-08-08 00:09:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e169aaf6-c6d8-3b93-bcbe-7cc7b6d3c7a0 | -6.58926 | -43.3839 | 2025-08-08 00:09:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 11.9 |
| e37a9db0-25f2-396e-b189-d9427796d981 | -6.70101 | -43.32791 | 2025-08-08 00:09:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 03a8dff1-5e6f-3b44-ad20-f84523a1c49c | -10.61369 | -44.76144 | 2025-08-08 00:09:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| d73fec48-0209-3d0b-8c59-6bdbc8a01951 | -9.65839 | -43.8461 | 2025-08-08 00:09:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 70de2017-399f-32f7-8981-5e061b3c4cf0 | -9.06403 | -45.08234 | 2025-08-08 00:09:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 7d55118d-f694-38fc-ab67-755baa5c261f | -7.82585 | -46.88351 | 2025-08-08 00:09:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3d4a72fe-8488-3595-8d09-7ee89f429e4e | -8.9213 | -60.7489 | 2025-08-08 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 183.9 |
| 6695ae3d-f025-3117-ad85-aac680067f95 | -7.8918 | -45.3348 | 2025-08-08 00:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 9529e767-0e11-3f95-b60c-c4d7fda9c88e | -13.054 | -56.8545 | 2025-08-08 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 3af1ec4e-fdcf-3b4f-ac96-f75c2caf5e0f | -5.9713 | -44.1312 | 2025-08-08 00:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| bef8b4b7-8b1f-39ba-8f8a-f24f5e536b83 | -8.9215 | -60.7297 | 2025-08-08 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 116.3 |
| dad60018-6c9a-3592-9011-955b531d329a | -8.9042 | -60.5385 | 2025-08-08 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| fadfd158-8490-3098-8b36-e9e790b548c9 | -10.625 | -44.7439 | 2025-08-08 00:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 4fd12ded-ffe2-3094-89f7-de903a42c44c | -5.9711 | -44.1542 | 2025-08-08 00:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 210.3 |
| 9412408d-a3b1-3d77-a97f-f6c5c62dd69d | -10.6247 | -44.767 | 2025-08-08 00:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| b632a201-1f5b-3fe5-abc8-b3a52c4b957e | -8.5211 | -43.3063 | 2025-08-08 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 3628af8a-38ab-391f-b14a-ea28f87160e2 | -5.9899 | -44.1528 | 2025-08-08 00:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 80520bab-0971-358d-b35c-5a87d8b0abfb | -8.9399 | -60.7481 | 2025-08-08 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| bff2107e-81a1-322b-ad2c-12453eeac9c3 | -8.9212 | -60.7681 | 2025-08-08 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| d2d98911-d5dd-3cf0-8e9e-1e19143ebefc | -8.5211 | -43.3063 | 2025-08-08 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 01913e44-3b92-3f68-b9e7-3e39c6a208df | -8.9213 | -60.7489 | 2025-08-08 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 175.6 |
| 82062c45-5480-32db-bcf4-6f5540ca12da | -8.9215 | -60.7297 | 2025-08-08 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 5a7b57ee-678d-3814-9586-24cd2bf38440 | -5.9711 | -44.1542 | 2025-08-08 00:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 0b4b45c1-8f6a-3ed3-a826-89a557aa4309 | -8.9399 | -60.7481 | 2025-08-08 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| ad3ccc63-7e24-3b35-a69a-6bc09fd37fbe | -10.6247 | -44.767 | 2025-08-08 00:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 76a86696-ac24-376f-af94-4eff5c87e188 | -13.054 | -56.8545 | 2025-08-08 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 2542ec7d-7aa4-3c21-91fd-27b93e6b0531 | -8.9041 | -60.5577 | 2025-08-08 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| bb433d40-2885-3a51-b7f7-a4b0ec91f80a | -5.9899 | -44.1528 | 2025-08-08 00:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 8f06b2e3-8ac0-30e3-9518-ad8e2424d22f | -10.625 | -44.7439 | 2025-08-08 00:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 66.7 |
| f04904c2-79e6-3d7f-ad62-d7da590a1508 | -8.5208 | -43.3298 | 2025-08-08 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.3 |
| cbb70136-dd26-36ed-bfdd-7b7888a77029 | -7.392 | -44.6528 | 2025-08-08 00:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 5171dd59-07fb-3579-b014-b0246ff628d6 | -8.9042 | -60.5385 | 2025-08-08 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 4833b6a7-8af7-3783-95e8-145e1f08ad3d | -13.054 | -56.8545 | 2025-08-08 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| bab02053-786a-33a2-9003-30c4b5e17abd | -9.0642 | -45.0749 | 2025-08-08 00:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 45bc4cc7-66cf-33b7-aef2-95ff1ab42099 | -8.9041 | -60.5577 | 2025-08-08 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| dccafcc8-6755-38b9-857e-b2bd17690076 | -8.9042 | -60.5385 | 2025-08-08 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 40320b04-ce10-342d-94d4-d79abe016757 | -8.9215 | -60.7297 | 2025-08-08 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |


[Clique aqui para ver as próximas entradas](README3.md)
