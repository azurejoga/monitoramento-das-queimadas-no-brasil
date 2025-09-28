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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| caebee5e-7f1e-39d8-8313-52f7daaca153 | -8.20022 | -44.40171 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cde9fcdd-b633-3fcc-b630-da62a295e690 | -5.90699 | -42.9353 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 36c208b6-8066-3d3c-a92e-6608d7e889dc | -8.918 | -46.09718 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 679bbd30-82ed-37ba-ae67-d55aa9fa47ac | -7.1716 | -45.49614 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 71aadea1-e35b-31fd-b619-15ccd735eab9 | -12.01518 | -47.90863 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e59fac3-5a03-352f-a737-7462f66ae162 | -11.96801 | -46.58873 | 2025-09-28 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 777348a1-8339-3c79-9c86-a1dbecd8a21f | -6.09661 | -42.64857 | 2025-09-28 04:25:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6b765657-58ff-3073-a524-73fce061d02b | -6.49536 | -44.24551 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 583096b6-05e4-397c-8d9d-29d858d39ee0 | -9.27987 | -48.96199 | 2025-09-28 04:25:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbcf3a9d-d57d-3e46-a85e-e896c2f7242b | -7.03118 | -44.76678 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 76ed20cf-dca0-39ff-a059-1c4e24bb6517 | -7.59739 | -43.0538 | 2025-09-28 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8a336cc2-bde5-3ccb-a4c3-bca6f2323d1b | -8.63913 | -44.00356 | 2025-09-28 04:25:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc9331d5-dad4-3b6b-8b1c-a3ba364b3570 | -6.08753 | -42.63397 | 2025-09-28 04:25:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6bffe19a-da55-3b95-9f1c-d24c10f66864 | -7.77922 | -47.0109 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e9a771a6-2ff3-39b5-ad16-c70652ab43a5 | -10.91197 | -45.73803 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8f77b191-6c2c-35bf-ba59-270edbc93481 | -5.74144 | -43.37514 | 2025-09-28 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 807b1563-0162-3226-b4d9-fd0da322007d | -8.16617 | -46.43157 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ff88641e-ecec-30ee-a78f-6c4664ab08dc | -6.78571 | -44.08852 | 2025-09-28 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| a91257ef-c9de-3e31-81f2-52213475e1a1 | -8.68353 | -47.06995 | 2025-09-28 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dbf4c586-5a6e-3efe-8aab-e57823f6f033 | -11.98116 | -47.06982 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e30de04-1a84-3f14-922a-6566f094b0d0 | -11.4315 | -44.92176 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2d27545-7968-3c14-a1ee-166b4ba14b3a | -11.70192 | -44.41317 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e1a73d7-ef61-3632-8441-bbdc041a36bb | -6.29297 | -39.8268 | 2025-09-28 04:25:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 408dcf8c-866a-3d3e-8e17-b19755259a00 | -6.09386 | -49.39821 | 2025-09-28 04:25:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 98ffe122-166e-32be-bc55-307d57219c5e | -8.82229 | -46.01354 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 240a3402-2a83-3e83-8640-e706fb02775d | -6.5146 | -54.8729 | 2025-09-28 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d40cb71f-5a5f-3d80-8e1b-8251a2a9ea89 | -12.53661 | -48.30358 | 2025-09-28 04:25:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68ced418-fd81-3208-a2b3-3593ef8b2d58 | -8.50041 | -44.73196 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44ab3dad-1869-3e4d-8692-5e479300d759 | -9.65319 | -45.25011 | 2025-09-28 04:25:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1441ca1-b5b2-37a5-9fef-336668005260 | -7.75049 | -46.97775 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 62a6de29-873d-3e9e-aa51-d4508f52ae33 | -11.39494 | -46.93259 | 2025-09-28 04:25:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6ba36e4-6988-3819-a702-87e722518a23 | -5.63819 | -44.92295 | 2025-09-28 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1f5ac12b-c4f1-3760-be2f-16f45a035924 | -6.04478 | -43.92108 | 2025-09-28 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26840d06-3047-3f04-ba35-1f554497ce74 | -7.74717 | -47.02008 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be9ab82c-4dc2-3424-814a-856e75c6af5f | -12.26355 | -44.09348 | 2025-09-28 04:25:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 645a43f7-e47d-38d0-9247-4d82587996e1 | -8.64442 | -43.99243 | 2025-09-28 04:25:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41340dfa-b312-38b3-8e2e-7e53d71cb5cd | -9.10717 | -45.88508 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 893239fc-52ea-3922-9ff3-66d79bc0c2cb | -7.74441 | -47.01606 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f5111b58-b21d-3206-b02a-cfd782122429 | -12.01704 | -47.07941 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9c2d799-6032-3753-bb9f-89f8651222ce | -6.60823 | -45.88674 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24d47ed7-f253-3d79-bce2-fd012d91d415 | -12.0053 | -47.88531 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4032fad9-fb31-32d7-8c4f-33c3c04e0780 | -8.4997 | -47.00808 | 2025-09-28 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04ed72de-c6dc-3499-9f4b-e650cfa40821 | -9.04723 | -46.72514 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ecb7cc92-f3c6-3f74-bc66-b14e5b9830ad | -12.05766 | -48.76926 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f988d68-983a-37c2-8edf-6fd4cefeb145 | -5.51081 | -44.9108 | 2025-09-28 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3233afd8-2fdb-37c5-b324-c55f69d23130 | -6.50998 | -54.86905 | 2025-09-28 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5e22ba8c-627e-34e4-a7f3-cba8bde135d6 | -6.09166 | -49.39194 | 2025-09-28 04:25:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1276dee9-50b3-325c-921f-0a1cfe16997e | -9.11884 | -46.67954 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2179809c-85ee-34a4-8067-1646aabe8e1a | -7.382 | -47.02965 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| c4641be4-366c-3a4c-b2c5-478ecbd5069e | -9.29437 | -45.6883 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c48a455d-a6b2-3513-9dcf-01b78e08cf20 | -12.78341 | -47.75601 | 2025-09-28 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 804747d0-35d4-3225-8592-99c12c809710 | -9.11223 | -46.67848 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 075b03e8-94f2-3629-9669-c807cd6e570a | -12.01899 | -47.9274 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9804439d-e5e4-3e35-ad80-174044c34d66 | -11.95683 | -47.89202 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35acac16-9a87-3fcf-8d7b-d83d48352d29 | -5.63095 | -44.92543 | 2025-09-28 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f978b29b-7dd7-3cfd-bb91-e501a15eba06 | -10.17412 | -52.57262 | 2025-09-28 04:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fff118f2-3841-3d9f-9679-a14c9fb9449a | -7.60301 | -46.87898 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c40d9dc-849b-3547-9834-a87527264b41 | -6.09459 | -49.39675 | 2025-09-28 04:25:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 62f17de9-1aaa-3a8b-8265-63eaabb8cff7 | -11.9795 | -47.08039 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 49bc91d0-724c-3619-b969-f38c7d99b8fc | -6.48338 | -44.25505 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be834a07-a1e8-3b23-9c39-d365b730bce0 | -7.3803 | -44.29597 | 2025-09-28 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 867839cf-4aa2-37f3-9362-a38913e85bca | -11.3542 | -44.99911 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf07144c-2a39-3f4c-9703-75befee5bb9c | -11.978 | -46.59037 | 2025-09-28 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d389b437-4649-305a-9f03-5faf04bac82c | -7.42467 | -40.07513 | 2025-09-28 04:25:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 455c5fde-9006-3c75-b9c5-b8b8c0a3b50f | -6.49982 | -44.12359 | 2025-09-28 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00d39bc0-3dfe-3f42-a54e-b42a818c9647 | -5.90636 | -42.93942 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c3ad0e50-c563-379a-960f-a82152b91a3b | -7.25592 | -42.98999 | 2025-09-28 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3a3b2766-a705-3e52-8ecc-ebba4ae14ce0 | -10.91253 | -45.7344 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6abc1ca8-ef21-345b-a454-5a0fca054fce | -5.64153 | -44.92347 | 2025-09-28 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d85d8af4-eaaa-34e9-adef-672e7ad891cf | -9.10493 | -45.87749 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6b91902-f9ee-3548-9213-0c2c83fc9ad7 | -5.89432 | -42.50217 | 2025-09-28 04:25:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c2c37d67-f440-35eb-b77f-eefd997b08fa | -11.01997 | -47.99192 | 2025-09-28 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3261bb4-4669-3526-82d0-56f71cdc0c51 | -7.37038 | -47.03852 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfe0d182-bf58-3c02-93d5-dcfa0635b00d | -7.03006 | -44.77395 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 648c0a12-0253-3ecd-b10c-209140c22274 | -11.65523 | -45.34038 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cce3c438-f7f3-3e08-9222-8f840d611471 | -9.8006 | -52.24614 | 2025-09-28 04:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d920d0b5-0695-31bc-b181-51777b4aef0a | -11.99109 | -47.04974 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 065f0353-2fca-37d1-b933-c2faf86c0245 | -11.99 | -47.07847 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f06d168-76d1-37ad-83a5-8ceb80861003 | -8.00251 | -44.4846 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56e8f10c-bf39-3018-866e-2d173ddca09a | -7.79784 | -47.021 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 057e8b7e-2991-3271-a6ba-eabe9790173c | -5.35779 | -45.97637 | 2025-09-28 04:25:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d2935491-6ba8-388e-8216-7922ec3080b3 | -12.42016 | -44.11954 | 2025-09-28 04:25:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| baa5880c-4ac8-3d06-8cb1-46102c2a60f6 | -9.29493 | -45.68473 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f41bc41-e23b-36b9-b659-c5149416be91 | -7.03005 | -44.7517 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0969f26e-2551-3fbc-a4a8-96ca3ab529f6 | -8.50301 | -47.00861 | 2025-09-28 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03883a59-1c09-3ff2-9823-dd511428bf9f | -10.4104 | -48.15135 | 2025-09-28 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4dc6b81c-35c3-3346-8a6e-34bd25b144c3 | -12.86918 | -46.79333 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 742d3965-df3b-3abc-83c5-aaf7ebe6ce28 | -8.27886 | -45.44693 | 2025-09-28 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66849ec4-727e-386f-bdac-0fe30892ea42 | -10.95613 | -54.09986 | 2025-09-28 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f0304c72-8ee6-39ec-a35e-9883c93b97d1 | -11.98005 | -47.07687 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9e3a4be2-3721-31ba-88a3-16e264ce9288 | -11.69466 | -44.46268 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bdc8f240-43f1-37a8-9c6d-9694c68c345a | -4.85821 | -49.46643 | 2025-09-28 04:25:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5181274-cd22-3c9a-8267-9309d6461396 | -7.53837 | -46.10483 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 31b40bb8-62c4-3366-a0cd-2cb2af4a6581 | -6.10534 | -43.14249 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| e5bd1ba9-d0a2-32a3-9731-8de384fd2581 | -5.63655 | -44.93352 | 2025-09-28 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6f70de65-8383-3b95-acff-fe55d1810e53 | -5.90573 | -42.94349 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b59a7daa-a79d-3867-a865-cd0e83f9ba14 | -9.87615 | -45.93964 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdeec672-88b9-323c-af6c-5ab0fa9a3ce5 | -12.38572 | -42.53185 | 2025-09-28 04:25:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8dff22db-f380-359b-8c1a-51c49e80db54 | -8.17002 | -46.42863 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| beb8e901-64e8-3193-9870-7c9a063098f7 | -11.35201 | -45.00188 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README61.md)
