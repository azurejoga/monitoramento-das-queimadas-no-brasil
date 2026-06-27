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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c563abf7-0921-3b79-8cda-7d5580ef61f4 | -5.30565 | -47.24555 | 2026-06-27 04:29:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8cb6324a-95e4-3f7c-b4e3-107e8194e766 | -6.50176 | -42.2321 | 2026-06-27 04:29:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a98c5265-f240-3b4f-8088-cdb9cf724cd8 | -6.97521 | -42.88003 | 2026-06-27 04:29:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2afebb2b-38b7-31b3-a35b-c706e75f8384 | -6.86977 | -45.52008 | 2026-06-27 04:29:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43923e08-783a-38d9-bb5b-54d9a7af03ca | -4.14714 | -43.65265 | 2026-06-27 04:29:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17ac6afb-0807-324d-a47c-02613110d707 | -7.74972 | -44.61679 | 2026-06-27 04:29:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e3934f7-066e-3989-8a91-26944556a422 | -8.31302 | -47.11755 | 2026-06-27 04:29:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fee0527-fe7a-301b-91b8-323ea1b4f9bc | -7.00179 | -42.76947 | 2026-06-27 04:29:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6f1a146c-5945-3902-a604-aaf3276bdc7f | -3.86556 | -42.96428 | 2026-06-27 04:29:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92f979e0-d58f-34e0-8d02-c5d5590da6c5 | -4.28111 | -48.3611 | 2026-06-27 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| dc5840a1-74c5-341b-b38a-ac0e4883e402 | -4.28396 | -48.36559 | 2026-06-27 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 600a86f7-07b6-3352-bcf7-c5fc37024dc8 | -4.94513 | -48.24735 | 2026-06-27 04:29:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a24be3be-cf0b-3735-bbfd-06a22a52b648 | -5.98416 | -43.36996 | 2026-06-27 04:29:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7c95e828-4b96-3f44-9c29-37060aa8ab10 | -8.49094 | -44.73863 | 2026-06-27 04:29:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d616459-6928-3df7-8dd5-3cb628850ee7 | -6.97544 | -42.8966 | 2026-06-27 04:29:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 147bb181-0997-335f-a773-c190fc37bcb1 | -5.89825 | -46.89436 | 2026-06-27 04:29:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 99b6a9c4-db67-3247-8611-4d6385bd1ff8 | -6.97175 | -42.89601 | 2026-06-27 04:29:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 53a87e8b-48e9-30e0-aa6c-cf030e60040e | -4.28047 | -48.36501 | 2026-06-27 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 438e2298-7523-336f-86e8-9d96548ddccd | -3.51056 | -48.03426 | 2026-06-27 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 892bf4ca-6a91-3790-9620-43a2e8356f58 | -6.97453 | -42.88443 | 2026-06-27 04:29:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7dfa7ffc-739b-364c-a190-18d2c219459b | -4.14656 | -43.65644 | 2026-06-27 04:29:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7a9daa0-36a4-3aa2-8d12-eb858bee6d3d | -6.01004 | -47.10876 | 2026-06-27 04:29:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 99b847cb-9991-3ac1-8025-71b604394ea6 | -3.31295 | -42.49456 | 2026-06-27 04:29:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7753232-810f-3fee-b5fe-d14e901b6598 | -8.21411 | -47.11911 | 2026-06-27 04:29:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d14bd4fc-6e26-30f0-a03d-448681897d2a | -7.3013 | -49.62178 | 2026-06-27 04:29:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c53e6fc-2e26-3050-9181-eedad405d902 | -4.1431 | -43.65591 | 2026-06-27 04:29:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 371cead6-976e-3569-9fa1-28d8a2945ff0 | -6.75002 | -45.00682 | 2026-06-27 04:29:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d780acd0-13c2-3c91-9c5b-7cc724f29be8 | -6.97913 | -42.89717 | 2026-06-27 04:29:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| fcf8bf21-4aac-3576-b29c-7f60e19de2cc | -5.86456 | -46.25101 | 2026-06-27 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eeedd19b-6af4-305d-8ba9-57584b236f35 | -7.75315 | -44.61732 | 2026-06-27 04:29:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 114dfac1-2e9b-359f-98ee-bf134aa5a87c | -7.74422 | -44.17862 | 2026-06-27 04:29:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 04657d8a-0428-3205-b2f5-1decf8d71da0 | -7.00114 | -42.7739 | 2026-06-27 04:29:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c126c37d-3b81-3d81-9578-ce360d803435 | -6.97318 | -42.89322 | 2026-06-27 04:29:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1f09697c-5a32-3193-929e-0bfd6d04e915 | -7.50079 | -43.3802 | 2026-06-27 04:29:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d0441ca-29a5-3527-b3b4-1695ad623692 | -3.3136 | -42.4904 | 2026-06-27 04:29:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd7bf732-ac99-356e-8064-add133dc9dcc | -7.75257 | -44.62111 | 2026-06-27 04:29:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bbf541c6-68c7-3666-b09a-8a2131f4934d | -6.93585 | -43.67385 | 2026-06-27 04:29:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3421538c-47a6-33b7-9782-36bb8c29034d | -6.99873 | -42.76447 | 2026-06-27 04:29:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 93fe97b1-50ab-3f5c-b952-d197527e60f3 | -8.10736 | -45.52741 | 2026-06-27 04:29:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 073aef60-159e-3ce4-b92f-e9d0c5b5d39f | -6.97978 | -42.89278 | 2026-06-27 04:29:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| c434b679-a038-384b-9b67-56f3930cd87a | -7.1385 | -47.74581 | 2026-06-27 04:29:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9eb168f2-01ad-303a-b3b3-08b4d7d3384f | -8.30474 | -47.12692 | 2026-06-27 04:29:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b0851961-eb74-34a7-ad7e-e669b3bb2afe | -7.71866 | -44.15879 | 2026-06-27 04:29:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bc2557e-0067-3d8e-a4f6-fd3d42c87e24 | -6.90443 | -43.68961 | 2026-06-27 04:29:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d73a5fb6-2462-3c50-acd7-ba298c831f1e | -6.98347 | -42.89332 | 2026-06-27 04:29:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 044d9cfb-49d5-365a-8e26-10c33649d60b | -7.25415 | -47.25795 | 2026-06-27 04:29:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9c67c61f-d513-33f4-bf93-c53600e50d7e | -6.9725 | -42.89761 | 2026-06-27 04:29:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c690f36b-69a7-3c66-835f-4c98ed7f189b | -5.77897 | -45.06495 | 2026-06-27 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e23e2a8-eee6-31b7-8fba-ca7d5eeac3ad | -6.50245 | -42.22751 | 2026-06-27 04:29:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6273f275-9dfe-3b0b-9cd4-e8637e9abb90 | -6.00947 | -47.11226 | 2026-06-27 04:29:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 032cadb9-c1dd-3335-856f-6270591f0ef6 | -5.13242 | -42.8795 | 2026-06-27 04:29:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4acbe731-0014-3ba9-8dd5-120f678a9e5f | -7.44567 | -46.77914 | 2026-06-27 04:29:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 92e285f6-f968-3aa1-85d6-a38f56388960 | -7.74834 | -44.17508 | 2026-06-27 04:29:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 626c8749-0873-3ac6-a42c-c061169efc50 | -7.49654 | -43.38384 | 2026-06-27 04:29:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 867b493a-af05-33ff-bef2-7b09ce089617 | -7.74012 | -44.18201 | 2026-06-27 04:29:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d370d2d7-e30c-3468-9109-28d957f56808 | -3.86849 | -42.96884 | 2026-06-27 04:29:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| fd7dfb59-62b5-3b95-a31d-e2b1c3e72145 | -6.50628 | -42.22796 | 2026-06-27 04:29:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dd17328b-489b-365e-bea8-cd0f1de9ead5 | -5.77508 | -45.06795 | 2026-06-27 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a3689667-19c1-32d8-9ac7-baf9d527fd13 | -6.0128 | -47.11279 | 2026-06-27 04:29:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 156b1cd5-074e-3f1b-babe-2c0fef5aa499 | -7.31662 | -49.69526 | 2026-06-27 04:29:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3e1628e0-883f-36f8-a491-4a46119ec34c | -5.1288 | -42.87897 | 2026-06-27 04:29:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff1a72f0-6658-3c7e-94c3-d37af294e6af | -6.9724 | -42.89161 | 2026-06-27 04:29:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| daf7b34e-1b2d-35e6-b63a-7de1bc6f9052 | -8.31247 | -47.12103 | 2026-06-27 04:29:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f30b7a7-78f9-3afa-a29d-33f99f261586 | -7.17036 | -46.45838 | 2026-06-27 04:29:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 84176f7c-58e7-3360-a4e2-bb180939caa2 | -7.50015 | -43.38438 | 2026-06-27 04:29:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7cad12c-38f6-352e-b9e7-9b3b94bfafc1 | -8.31633 | -47.11808 | 2026-06-27 04:29:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3073cc3-f07c-354e-9b64-10f5da837912 | -7.6305 | -50.22026 | 2026-06-27 04:29:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e936026-fc00-3f46-807a-48a2b7454b6f | -4.28459 | -48.36168 | 2026-06-27 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9c9d8a95-ca3d-35a0-b5d8-c5825b33f971 | -4.66158 | -43.22086 | 2026-06-27 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 072d4eea-69c0-3774-8787-89b0e3f74b28 | -3.30935 | -42.494 | 2026-06-27 04:29:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6fbb47e9-0f35-307a-8d17-f49021748f5c | -6.75339 | -45.00735 | 2026-06-27 04:29:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 565d31fa-418f-3ebd-b6cd-2ac18dc95c41 | -4.31246 | -47.75797 | 2026-06-27 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9740ac93-ca6e-37d7-ab9c-4ccc0cdb8c68 | -7.74772 | -44.1791 | 2026-06-27 04:29:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 59f24e09-bda7-3321-b7f8-22191cbca3ab | -8.3122 | -45.39424 | 2026-06-27 04:29:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c640d39d-0206-3164-a990-e63a83fc616f | -5.79609 | -43.63124 | 2026-06-27 04:29:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e55f89fb-13f9-3462-a82c-164f4f5bb8ad | -7.17091 | -46.45492 | 2026-06-27 04:29:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb694d35-bfc3-321e-9364-5b422ee97d14 | -12.4651 | -58.5009 | 2026-06-27 04:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 172a27e6-45b6-32fc-8291-8b28fcdaea36 | -12.6046 | -57.8942 | 2026-06-27 04:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 40145eb8-7c60-3c66-873b-a9de1a5c6635 | -12.4654 | -58.481 | 2026-06-27 04:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 9dda7857-1a80-308e-be6f-99ea98248142 | -12.6236 | -57.8926 | 2026-06-27 04:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 9bf4f85d-d9fb-3b1a-be7a-2c832e9f9cf1 | -12.46278 | -58.49457 | 2026-06-27 04:32:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 26.9 |
| c912f0bb-9931-3e77-b5c4-4fced925e3b7 | -10.4808 | -47.11696 | 2026-06-27 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f4108778-e019-3215-ae16-55d228219c36 | -9.42493 | -50.68027 | 2026-06-27 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 027efa02-c244-3271-a7eb-9dbb1f94c222 | -13.64398 | -55.29467 | 2026-06-27 04:32:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d012c8d5-8614-3e86-ac57-f7d046c8a66d | -14.87882 | -54.5398 | 2026-06-27 04:32:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56a1a40f-4f35-3127-b5cb-83a13a67d19b | -12.60384 | -57.88042 | 2026-06-27 04:32:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f2c1e3f0-47ed-3d63-9288-3a1a2b67cfa1 | -12.44592 | -44.75304 | 2026-06-27 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 441de8d6-971e-39a8-9dd8-460523c8397d | -13.253 | -54.40637 | 2026-06-27 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7bf0e52d-1b25-35e7-ba8c-31ae1c70d3ec | -13.6699 | -53.94291 | 2026-06-27 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 010518f0-17ab-3660-b8fb-316bb117f19c | -10.4797 | -47.12393 | 2026-06-27 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 85d3871b-0a51-3278-8e62-7b03fa8c6472 | -12.5524 | -54.58878 | 2026-06-27 04:32:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d8a9b45-0eaa-3383-9f1b-6cf2949c7444 | -12.61747 | -57.89917 | 2026-06-27 04:32:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 621a1068-d482-3437-90d4-6bf9748d0aef | -10.9365 | -56.85365 | 2026-06-27 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1239131b-7128-3670-9348-375ecfbee46d | -10.93478 | -56.84857 | 2026-06-27 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f5622ffc-f619-3e36-8509-17860e9e538f | -10.78024 | -54.10449 | 2026-06-27 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1fad6f57-60ad-364c-be53-c7f5bd0b67eb | -11.32211 | -54.4673 | 2026-06-27 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44d5288e-9dc4-3390-8ab2-e07e4fcae94e | -14.87182 | -54.52971 | 2026-06-27 04:32:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| cfb80128-f080-3827-87f0-70d6172b1e1e | -8.59008 | -46.91314 | 2026-06-27 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11143ac8-11bb-3233-94bb-ad373e2387bd | -13.43713 | -47.86333 | 2026-06-27 04:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4166030-cc1a-3705-a24a-09d2b54b93f0 | -12.93205 | -56.62844 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README13.md)
