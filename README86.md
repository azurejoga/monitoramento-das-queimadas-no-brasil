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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 423c74d1-371d-35f1-911c-72580b96adac | -13.75032 | -43.50279 | 2026-08-28 15:46:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 7aba0f2e-c41b-3ee4-8fb7-8985ccb1cb9e | -9.79609 | -43.55729 | 2026-08-28 15:46:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 451c83f8-ac66-3746-9d9e-0901a1307243 | -14.18758 | -41.24535 | 2026-08-28 15:46:00 | NPP-375 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 69c265ef-5377-3980-93ec-12ea6de07754 | -13.44586 | -40.6991 | 2026-08-28 15:46:00 | NPP-375 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| ffb10e18-ef70-3fe0-a69b-e047e542234c | -6.91705 | -38.48544 | 2026-08-28 15:46:00 | NPP-375 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 6da59bda-32eb-3a06-91b2-ccadb63d82b1 | -11.41468 | -42.303 | 2026-08-28 15:46:00 | NPP-375 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| dac37355-3963-39f9-acc0-c85167f45077 | -8.28539 | -39.97149 | 2026-08-28 15:46:00 | NPP-375 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 5.5 |
| b95cb8ee-b927-31f2-aab5-cd5f92021c02 | -7.6235 | -44.82274 | 2026-08-28 15:46:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 21255f3e-0e19-3fc9-9fd9-01c071562031 | -7.20405 | -42.74076 | 2026-08-28 15:46:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 34dc292f-6e6b-36e5-8b1c-e677b9b46889 | -12.66138 | -38.78391 | 2026-08-28 15:46:00 | NPP-375 | SANTO AMARO | BAHIA | Brasil | 2928604 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| de40feab-4ff2-3107-83c7-c770e9c388d4 | -7.26965 | -45.35542 | 2026-08-28 15:46:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7d5c1b9b-c323-3f65-8c6e-ad40a9028e1e | -13.43997 | -40.69985 | 2026-08-28 15:46:00 | NPP-375 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| fccdccc3-00f2-365c-9794-112ae7991c00 | -7.05956 | -43.58714 | 2026-08-28 15:46:00 | NPP-375 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8c17dae2-9760-3ff8-b790-3d6839d7db5d | -11.41527 | -42.30821 | 2026-08-28 15:46:00 | NPP-375 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 797226d6-aee9-3c1e-bd83-541277d80960 | -11.14409 | -38.16106 | 2026-08-28 15:46:00 | NPP-375 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| e232bac2-987d-30d8-a4b9-e6ba255ecf10 | -6.92344 | -41.62783 | 2026-08-28 15:46:00 | NPP-375 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| bbf07ef8-66da-3dc1-8846-060b1d54936b | -13.28208 | -40.34111 | 2026-08-28 15:46:00 | NPP-375 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| d6960c07-9442-3c14-ac9f-01755a86deed | -7.20467 | -42.74536 | 2026-08-28 15:46:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| fb98de95-7055-38d3-97e3-445446671b9e | -9.99998 | -36.38522 | 2026-08-28 15:46:00 | NPP-375 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 0cf180cc-ac32-3551-9d16-5ff99c401310 | -13.11087 | -40.88274 | 2026-08-28 15:46:00 | NPP-375 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| fd55c8ac-eb10-32b1-ac4e-9afb7fdb78bf | -7.09565 | -43.71054 | 2026-08-28 15:46:00 | NPP-375 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eb6f229a-c80e-36ad-b6c1-df63106192d2 | -6.9283 | -42.6824 | 2026-08-28 15:46:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| a2aeff8f-03a6-3aa1-b447-5683019c6030 | -12.86835 | -44.34484 | 2026-08-28 15:46:00 | NPP-375 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c7061a5c-7849-32ae-9faa-cb48721df05f | -12.03632 | -42.97952 | 2026-08-28 15:46:00 | NPP-375 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| adb5332b-739b-3d81-ac1d-d90c5ee7714c | -7.58317 | -44.0129 | 2026-08-28 15:46:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 61d738d8-fa36-3b96-bbfe-862d73c3e0c1 | -9.99525 | -36.38191 | 2026-08-28 15:46:00 | NPP-375 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| f0ef03bb-7b5d-3b6a-a3c3-bdaa50fd7ac9 | -11.40719 | -42.30649 | 2026-08-28 15:46:00 | NPP-375 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 736f89dd-e69b-32f9-a20f-51441c16cfee | -14.24042 | -42.62288 | 2026-08-28 15:46:00 | NPP-375 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8fb0565f-ebf1-34e7-b42e-421482baca5b | -12.86813 | -44.34543 | 2026-08-28 15:46:00 | NPP-375 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8e370b4a-ef88-3ced-914d-d2904a11a69e | -13.28182 | -40.34136 | 2026-08-28 15:46:00 | NPP-375 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| e12ff8c1-eec4-38e4-85ad-0b1730af2cd1 | -12.86891 | -44.35279 | 2026-08-28 15:46:00 | NPP-375 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6b7bfd43-61b6-34e0-9b0f-0aefed8f28e4 | -8.47954 | -44.80048 | 2026-08-28 15:46:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 85184cc7-c365-384c-934f-b4cb39bf0eb1 | -12.09454 | -39.70765 | 2026-08-28 15:46:00 | NPP-375 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| a89299ae-301b-3430-a23c-da1e4d3a404a | -12.62123 | -40.30985 | 2026-08-28 15:46:00 | NPP-375 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 55bda3f6-9797-358f-9e24-484bcb669b7d | -7.27109 | -45.35017 | 2026-08-28 15:46:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| b8e3324c-9252-36af-9e5f-a173733107c8 | -7.58394 | -44.01881 | 2026-08-28 15:46:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8e33d575-cb62-31d2-adb5-947a185fefec | -7.71387 | -43.9253 | 2026-08-28 15:46:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a3795322-adb3-30d9-a172-7a37304d9e59 | -8.47858 | -44.79263 | 2026-08-28 15:46:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| cbb6d8ef-3be3-3069-817d-2007fbf6f43c | -9.05727 | -37.01957 | 2026-08-28 15:46:00 | NPP-375 | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 11.1 |
| f561b26e-463c-30b4-b233-14ccb6686b66 | -11.4089 | -42.30889 | 2026-08-28 15:46:00 | NPP-375 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| c7875c69-7ceb-3f8b-a298-2dfca26b391f | -6.93382 | -42.67682 | 2026-08-28 15:46:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 37b5b173-c175-39ac-8f5a-243ee78e9846 | -12.8616 | -44.35343 | 2026-08-28 15:46:00 | NPP-375 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 3b5adb1c-3ab9-3a4e-a324-b528890299ea | -13.44538 | -40.69479 | 2026-08-28 15:46:00 | NPP-375 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d73da0e4-e16d-379a-99ae-ea5f36f93525 | -10.86481 | -44.80119 | 2026-08-28 15:46:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| fd9f38d6-d490-30df-829f-7026360c4053 | -12.27071 | -43.14288 | 2026-08-28 15:46:00 | NPP-375 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 9d67a3c6-eacb-351f-bb2e-f940208845ac | -13.51934 | -42.57368 | 2026-08-28 15:46:00 | NPP-375 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6a3f84ec-19ff-3744-a69c-6009f222c055 | -7.62651 | -44.82729 | 2026-08-28 15:46:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8a7a2a4a-4461-3f12-9e7a-2cfa0a4975ed | -9.99116 | -36.38227 | 2026-08-28 15:46:00 | NPP-375 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 7fb8dd99-46c0-3312-8180-e06b248a3a9a | -7.0776 | -42.20852 | 2026-08-28 15:46:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 5565345f-bdc3-3442-8f60-0974344f7fb7 | -14.09003 | -41.20544 | 2026-08-28 15:46:00 | NPP-375 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 01507255-e32e-303d-af41-1833f90b8e90 | -12.65986 | -38.78256 | 2026-08-28 15:46:00 | NPP-375 | SANTO AMARO | BAHIA | Brasil | 2928604 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| e155c876-0ae2-3165-a4a9-a5efd6d14955 | -8.31122 | -39.01994 | 2026-08-28 15:46:00 | NPP-375 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 11.0 |
| b1012655-b6e0-3364-9ccb-8d4dbd70e831 | -7.08646 | -42.79742 | 2026-08-28 15:46:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 93933731-398f-3380-b3c3-639858cbb6d5 | -6.92236 | -38.48954 | 2026-08-28 15:46:00 | NPP-375 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 07480010-bc8c-36a7-b5e1-0dfe75e0889f | -11.19666 | -40.83794 | 2026-08-28 15:46:00 | NPP-375 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5a675229-0921-3889-b2fa-67f63aa9ef7e | -12.86254 | -44.36039 | 2026-08-28 15:46:00 | NPP-375 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| aa94fb25-caf0-3b14-9131-e057ded00161 | -11.94656 | -41.32485 | 2026-08-28 15:46:00 | NPP-375 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 3e8105d7-bf11-3588-aeb3-933289db0233 | -7.08155 | -42.80802 | 2026-08-28 15:46:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 887877d1-ed35-3ff6-8102-603825b1c33b | -5.57816 | -42.69294 | 2026-08-28 15:48:00 | NPP-375 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 0a8e2900-a090-3c06-a3ca-a02aa6588abd | -3.43508 | -40.64436 | 2026-08-28 15:48:00 | NPP-375 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| fb13bc36-e764-3a2b-9d56-812a0ec5c070 | -3.70639 | -45.25686 | 2026-08-28 15:48:00 | NPP-375 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 2abebe0a-d4bc-3d6d-a5d0-7b3b155b4a73 | -3.41911 | -43.38366 | 2026-08-28 15:48:00 | NPP-375 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b845f1a3-7130-3afe-9d88-adb1a54b05bc | -6.95661 | -45.23407 | 2026-08-28 15:48:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 52b1b37d-2428-3bc2-a4dd-2f3e7b4b5d0a | -5.34066 | -45.15931 | 2026-08-28 15:48:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1c3aaebc-720d-30a4-96d9-42c9fcf413b6 | -3.96057 | -43.11853 | 2026-08-28 15:48:00 | NPP-375 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 429a9078-7f5f-3de6-bd7e-af245c3e53bd | -5.95528 | -44.78907 | 2026-08-28 15:48:00 | NPP-375 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 54446701-d1e5-3c93-955a-fe028f522d29 | -3.73106 | -43.08415 | 2026-08-28 15:48:00 | NPP-375 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39cd1937-40f2-3132-9634-1faad08d4907 | -6.90595 | -45.65681 | 2026-08-28 15:48:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 38.5 |
| bdd8b319-9cb8-3e66-aadc-8989d9733cfa | -5.16592 | -38.14143 | 2026-08-28 15:48:00 | NPP-375 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 0e383728-ecc9-3e4e-971e-9f21b9b85839 | -6.90167 | -43.64655 | 2026-08-28 15:48:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| e13eab2c-5d59-3a52-9c28-8c6296fbf85e | -6.56427 | -45.32617 | 2026-08-28 15:48:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| d6f7a6b5-9aa5-3cc4-bbc7-8fefcbdd3407 | -6.24873 | -39.1984 | 2026-08-28 15:48:00 | NPP-375 | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 90a5f1de-0435-3e6f-b98b-89414e2c5e55 | -3.42001 | -39.27501 | 2026-08-28 15:48:00 | NPP-375 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| e505d9e0-1622-379c-8412-283ca6adba49 | -5.48123 | -45.12087 | 2026-08-28 15:48:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 6b51c2cc-8b3e-3f06-b81f-94a14b31bbf4 | -3.41871 | -43.38267 | 2026-08-28 15:48:00 | NPP-375 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f41f5da6-acb1-3e28-b16f-24432cb4c7fe | -4.84678 | -45.40371 | 2026-08-28 15:48:00 | NPP-375 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c31e2c26-157c-3747-bc8d-0635091d52cf | -4.0833 | -40.12428 | 2026-08-28 15:48:00 | NPP-375 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6a110cbd-b3bb-39d3-862f-a44e274dda03 | -6.9033 | -43.64936 | 2026-08-28 15:48:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| faa41f08-0c76-36c2-b81f-dff51cf25a08 | -5.33977 | -45.15295 | 2026-08-28 15:48:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a6576fa2-7f13-38c1-8075-dec714421054 | -1.78756 | -45.77578 | 2026-08-28 15:48:00 | NPP-375 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 78492712-db59-375a-87f8-6198ab255b1c | -3.93101 | -44.90734 | 2026-08-28 15:48:00 | NPP-375 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3b9b9020-b6d2-3c57-a4d5-4619fc35fcc3 | -3.70728 | -45.26315 | 2026-08-28 15:48:00 | NPP-375 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 413341c3-6148-3071-844c-41960e340ef8 | -4.8503 | -45.40603 | 2026-08-28 15:48:00 | NPP-375 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 785f9fac-30eb-32ad-8400-f1b3b4845725 | -1.60811 | -45.46548 | 2026-08-28 15:48:00 | NPP-375 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 22.6 |
| dcc28dda-9f58-3c1a-8e58-db86584dfb09 | -1.60547 | -45.46201 | 2026-08-28 15:48:00 | NPP-375 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| f853027f-04a5-386b-98f8-66d70e6b6d7e | -3.42523 | -43.38283 | 2026-08-28 15:48:00 | NPP-375 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 89cfe4cb-50b8-34b3-bfe3-472d3c336cfa | -1.60641 | -45.46799 | 2026-08-28 15:48:00 | NPP-375 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| bf72df14-1c49-3a2e-99fe-63e1f019dca9 | -6.05822 | -44.88391 | 2026-08-28 15:48:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4b0bf7f3-14fb-3173-9546-77ea960f90cf | -4.91625 | -43.47122 | 2026-08-28 15:48:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| dfc77ed3-c757-3ba7-b52a-3f5630964a6d | -4.84934 | -45.39926 | 2026-08-28 15:48:00 | NPP-375 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b49ba08f-4e81-3ca4-a27c-6e8669fa6417 | -5.01869 | -37.63951 | 2026-08-28 15:48:00 | NPP-375 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 76397c6d-1e7c-3dde-b5b6-30e40b686794 | -5.09293 | -43.86837 | 2026-08-28 15:48:00 | NPP-375 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c7810653-45c5-3acb-9e77-caa5a4ccf7cc | -3.84942 | -38.80154 | 2026-08-28 15:48:00 | NPP-375 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a4466f5d-6321-392d-9b14-588258a7a578 | -6.56334 | -45.3191 | 2026-08-28 15:48:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| b8860f7f-655b-30a3-9b81-83f2ba65b7e4 | -5.95694 | -44.80151 | 2026-08-28 15:48:00 | NPP-375 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 05cb2544-7451-3c5e-8e46-d901b3dbbbc7 | -6.90233 | -43.65181 | 2026-08-28 15:48:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2b3cede3-1035-3b10-9071-b45ae1b69afc | -5.95609 | -44.79516 | 2026-08-28 15:48:00 | NPP-375 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 83c9a580-2316-32b5-a126-cb8999d36659 | -4.91946 | -43.46774 | 2026-08-28 15:48:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 01d8927c-9d64-3261-bce8-0dd6ba6a7b34 | -4.08362 | -40.12719 | 2026-08-28 15:48:00 | NPP-375 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 995c66ac-937b-3902-9cbd-5abafe8ab797 | -4.36867 | -44.35719 | 2026-08-28 15:48:00 | NPP-375 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README87.md)
