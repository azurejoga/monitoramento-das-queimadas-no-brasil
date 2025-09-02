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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e94f55e8-aa2c-37ec-8a42-ffc974c1e826 | -14.99122 | -50.19357 | 2025-09-02 03:53:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f98c4ebb-2ce2-3b95-8d81-5a38b8473868 | -15.56001 | -48.32751 | 2025-09-02 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 45b9cfd2-3fdf-39cc-93e5-c6ad1509a432 | -17.70754 | -46.88587 | 2025-09-02 03:53:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9c75272d-80fd-36ae-bebd-ab23774d6c87 | -16.07929 | -43.61945 | 2025-09-02 03:53:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 474ea5e0-fedc-3b42-90ab-3eaac9b8952b | -17.89465 | -47.16275 | 2025-09-02 03:53:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2c635d6-4d1a-35b2-a9d5-3b54fa8bce92 | -18.08928 | -50.47392 | 2025-09-02 03:53:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15ea042a-0d2c-3906-979f-9ac70f50e5ea | -15.57749 | -48.3877 | 2025-09-02 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5fdcaaea-cee8-3406-8a54-ffe9563bcccc | -14.96121 | -50.06604 | 2025-09-02 03:53:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3ccc0cb-9227-39ed-afde-7a1e190a8a6f | -15.73064 | -49.02307 | 2025-09-02 03:53:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c2ef526-8fb9-3412-83e5-fec50861dfc2 | -17.88878 | -47.1673 | 2025-09-02 03:53:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 492baa3d-16e3-3acd-9d76-3d1a0f27baa6 | -14.78734 | -48.18488 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40c55773-d10c-3902-8104-b24d69b154f6 | -15.68282 | -48.94688 | 2025-09-02 03:53:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19521931-2e16-39c9-9255-d72bd6255d73 | -15.71787 | -49.02868 | 2025-09-02 03:53:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e34129ae-b009-3840-8305-eed25b72d0a0 | -15.69382 | -48.922 | 2025-09-02 03:53:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17921756-e105-3f02-8a8c-ec2caf476e70 | -20.70399 | -46.29709 | 2025-09-02 03:53:00 | NPP-375D | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a51d3e7-a9bd-353d-a0f9-5fbfde6a4902 | -14.75324 | -48.15164 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a02bc1d-cda1-3aee-842f-a28f407dbd79 | -20.74975 | -47.13696 | 2025-09-02 03:53:00 | NPP-375D | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 035460a6-444a-3972-981d-d7f18fdf7c32 | -15.56634 | -48.37907 | 2025-09-02 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55886686-49c6-3f48-b327-d3d414caebf7 | -17.70652 | -46.89112 | 2025-09-02 03:53:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 56.4 |
| f7068368-1026-33d7-ad75-2df58174a812 | -15.08949 | -48.11646 | 2025-09-02 03:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f15b016b-ed3e-3788-a71c-39c5c7220fd1 | -18.09488 | -45.00799 | 2025-09-02 03:53:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba2afa4b-9702-3256-a623-3511772427de | -17.89292 | -47.17183 | 2025-09-02 03:53:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 50b4d50c-3190-3f68-8126-ab0f4cb762f7 | -15.33587 | -46.11265 | 2025-09-02 03:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7660d91-a3fa-3cff-95d6-7cbccec64ff2 | -20.69708 | -46.30966 | 2025-09-02 03:53:00 | NPP-375D | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4077ac8b-4190-326a-869b-dca626cccf46 | -14.76436 | -48.15176 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b1bbfe7d-26e2-3e79-8a89-0080cef79666 | -18.37093 | -46.02352 | 2025-09-02 03:53:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| be86d4e4-e690-3a56-9376-1ee901b976d6 | -15.56381 | -48.33627 | 2025-09-02 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| af81b8bb-fc7c-3b48-a231-3d35680de6db | -20.12106 | -47.79559 | 2025-09-02 03:53:00 | NPP-375D | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbfd7b7b-6d6c-38f4-80ff-3e2317522744 | -16.86344 | -49.57508 | 2025-09-02 03:53:00 | NPP-375D | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 043f8580-da78-363d-befe-7a4a2641c2c1 | -15.72345 | -49.02978 | 2025-09-02 03:53:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a36c23ce-0a1b-369a-80dc-5318b8497638 | -18.07245 | -45.95301 | 2025-09-02 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76a031f8-5ea3-3dad-b092-7c6a3f9a406d | -16.85831 | -49.58005 | 2025-09-02 03:53:00 | NPP-375D | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a957fc8b-b76f-368f-9679-a05cf3f78af0 | -15.13222 | -48.11251 | 2025-09-02 03:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d83acb21-0645-3f15-8e7d-687549ae1013 | -14.20264 | -51.6621 | 2025-09-02 03:53:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ff87063b-7ff5-3ed2-bdac-9c2fe9f746bd | -15.73006 | -48.94193 | 2025-09-02 03:53:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9db03a88-c9e2-3601-b4c3-6d4529914b48 | -14.75821 | -48.1547 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d88568a0-3aa5-360b-b702-872841452156 | -18.07162 | -45.95731 | 2025-09-02 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a009c9d-a77d-3138-a939-5d6fbbfe79b2 | -15.55695 | -48.34268 | 2025-09-02 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 094a16ee-ab30-3b7d-9d86-1b58243fee64 | -16.85787 | -49.57354 | 2025-09-02 03:53:00 | NPP-375D | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 732acdba-22f2-3261-af06-aeaf358b52ae | -15.57544 | -48.38935 | 2025-09-02 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b5b86c10-7713-38f7-8d8d-ea5bb8619bfb | -14.99298 | -48.31971 | 2025-09-02 03:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3c4d53d-06f4-3290-8bdd-9ef6183d8421 | -16.68611 | -43.84858 | 2025-09-02 03:53:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 391b9c84-f9c7-32af-96a8-30f52d493f46 | -15.11763 | -48.18438 | 2025-09-02 03:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3fb2f70b-cc74-36e9-9e75-b5f7dcbe67a7 | -14.74846 | -48.14764 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 377c80f1-31ad-3eb0-b873-b170fefefcee | -20.69619 | -46.31417 | 2025-09-02 03:53:00 | NPP-375D | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 24ba243a-e9ac-3560-afcc-64f49374a98a | -18.12187 | -44.98845 | 2025-09-02 03:53:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51071be7-3a90-3469-95ad-370bbfa48534 | -14.19713 | -51.65527 | 2025-09-02 03:53:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1c6eec12-3519-398a-91cd-55689e8dcb87 | -15.80048 | -43.56487 | 2025-09-02 03:53:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0f31e56-8107-366f-be88-967cf0bc2e2a | -15.7187 | -49.02467 | 2025-09-02 03:53:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c168f07b-faa1-36b2-8af8-697d430510d6 | -16.04273 | -46.30363 | 2025-09-02 03:53:00 | NPP-375D | URUANA DE MINAS | MINAS GERAIS | Brasil | 3170479 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8681509-f60f-315d-b913-f9ceaea3ce53 | -17.61293 | -46.64343 | 2025-09-02 03:53:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 52a807df-9178-366a-8f41-348c38cca136 | -16.86 | -49.57216 | 2025-09-02 03:53:00 | NPP-375D | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9c036c22-7cf4-3ef4-a5c0-7c409ef04e55 | -15.69521 | -48.92335 | 2025-09-02 03:53:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81db5e24-5be9-36c9-b511-437cb74b4316 | -15.68441 | -48.93931 | 2025-09-02 03:53:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43264b57-14fd-3d1a-9a48-7159ac17d179 | -16.59386 | -48.97556 | 2025-09-02 03:53:00 | NPP-375D | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 332d2bff-b47a-39a5-9a2a-2f3a809731c3 | -14.75262 | -48.15476 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97fa4633-24de-3389-90d7-60a08f53d20c | -14.76377 | -48.15476 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 475f5bbb-ab05-35aa-979c-3ee0cf9bfbee | -15.55385 | -48.33048 | 2025-09-02 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cc79a265-2eeb-398b-a5df-a7abb913ceae | -14.78205 | -48.18344 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e42a59f-3ba6-372f-9995-267162999417 | -16.85705 | -49.57751 | 2025-09-02 03:53:00 | NPP-375D | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 160ce510-cacb-3923-8bdf-31927411e471 | -14.77074 | -48.15676 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1b554b2-6c34-36c4-8684-9babe2882033 | -18.15909 | -47.91572 | 2025-09-02 03:53:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dabbd8bb-d6e1-3199-9b4b-6981aebfe0ac | -14.61918 | -48.93972 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efa52d52-b533-31cf-8f6a-f67a559ed49f | -15.8044 | -43.56562 | 2025-09-02 03:53:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a15a578-efe8-3e2d-b198-82782b39bba4 | -17.17386 | -46.08711 | 2025-09-02 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ee92848-242f-33d8-b137-b8eb95eaf87f | -17.19654 | -46.06596 | 2025-09-02 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 746ecaef-4c70-34e6-b8d6-c3cea77d3312 | -18.59361 | -44.51592 | 2025-09-02 03:53:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d93cd37-0e3a-3fd1-82ec-54997918af26 | -15.68947 | -48.92326 | 2025-09-02 03:53:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f669add6-0605-3b3a-9602-46eb1380298d | -15.54848 | -48.32954 | 2025-09-02 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a0439444-bf04-3d87-bb15-de67b9dbaec1 | -18.37008 | -46.02789 | 2025-09-02 03:53:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| cdf45fa6-d416-3afe-83c5-d7c082586186 | -19.75596 | -47.89162 | 2025-09-02 03:53:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2a940de7-f6d5-33a2-b8d9-542a07e40305 | -19.81984 | -45.00506 | 2025-09-02 03:53:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 37c27e85-8cfb-36ec-885f-d36753afd130 | -14.76082 | -48.15071 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57f11b1a-dc96-3ac4-a0ca-b8d8478f24d3 | -14.2311 | -51.66953 | 2025-09-02 03:53:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 61d41461-a120-3486-aad2-a92a2fa0aa1e | -17.20188 | -46.06237 | 2025-09-02 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cd23d2d-7218-35c8-9ad9-5f400a9b7dc3 | -14.99622 | -50.19976 | 2025-09-02 03:53:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba4ec599-166a-38b6-aa2e-87d3ba32db08 | -16.59308 | -48.97935 | 2025-09-02 03:53:00 | NPP-375D | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc4f066e-ae81-3cae-9c5d-3cac75aff834 | -15.72979 | -49.02716 | 2025-09-02 03:53:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1a66739-7f18-3d68-a0cc-912adbadfd96 | -16.59227 | -48.98321 | 2025-09-02 03:53:00 | NPP-375D | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c2d6edd-f6e0-38a6-9b31-9160b57ed7e2 | -15.09408 | -48.12123 | 2025-09-02 03:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2145202-a4f9-3eaa-a04d-2c2af7d965bd | -14.99034 | -50.19751 | 2025-09-02 03:53:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 58925c4d-ab56-3f16-ae78-48bd5cc02a46 | -18.04452 | -47.74192 | 2025-09-02 03:53:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a9d4abf3-f9f7-32ae-b5cf-4e05f9d7dca6 | -14.99639 | -50.19883 | 2025-09-02 03:53:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 064f89fb-6b99-37f4-ba02-ed1b4fb67cc4 | -15.56562 | -48.38266 | 2025-09-02 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4dc8e501-ca12-3aae-bb3f-34857b6c2083 | -17.28666 | -49.20465 | 2025-09-02 03:53:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fff6cea0-d8d9-308e-bcb8-3d34a395ab7f | -14.9773 | -48.17737 | 2025-09-02 03:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f336f6f-3e00-39af-a529-8a6f919bea6d | -20.69465 | -46.29948 | 2025-09-02 03:53:00 | NPP-375D | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d16f7a76-4af8-3853-8919-07395865cd4b | -14.61996 | -48.9358 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85525571-6f5b-3575-89e3-353e57ce335d | -18.08828 | -50.47844 | 2025-09-02 03:53:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c2ef7e3b-febc-3f6f-bc66-6466d8584c05 | -19.81926 | -45.00332 | 2025-09-02 03:53:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c2aeb748-1b88-3c5f-baac-911ea88dc2a2 | -16.40818 | -45.65132 | 2025-09-02 03:53:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b607807c-3fe6-3c5f-b7dc-18e1095d0e2a | -14.77426 | -48.15812 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 762d7afa-6b8c-3694-8672-a01a46337b4a | -20.25482 | -46.94004 | 2025-09-02 03:53:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e89cbc8-0142-32b6-a8a6-73244e39b6bf | -17.28745 | -49.20095 | 2025-09-02 03:53:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0576b8eb-8a83-3d57-ab8b-b2f2d77e8da6 | -15.57616 | -48.38577 | 2025-09-02 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a29390b-3a68-398a-b854-523b14bd4e82 | -18.58964 | -44.51517 | 2025-09-02 03:53:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ddbe93d-1a53-3b62-a497-682f54b86c3e | -20.7453 | -47.1358 | 2025-09-02 03:53:00 | NPP-375D | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2389f229-a571-3e8a-9b82-b635534cc12f | -15.56488 | -48.38633 | 2025-09-02 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff665238-035e-3eba-9883-66c728eb93ba | -14.20393 | -51.65616 | 2025-09-02 03:53:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| df232b7c-5d44-3669-bb93-bf1859086a5b | -14.76554 | -48.15488 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README28.md)
