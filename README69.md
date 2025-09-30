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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a670e44-a657-3b0d-85d2-0adafaf6f605 | -12.84506 | -47.01084 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4fb8fe50-fb7e-3eb7-9dc0-e5e7408d9c14 | -10.8876 | -53.7557 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2413f810-58ff-336f-be12-c2f02d148aa4 | -8.53458 | -44.66954 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd91b823-e0c5-3f7b-a177-047210cb4764 | -13.363 | -47.91817 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0940ea6c-47b2-3623-a1ad-120483037df1 | -10.79146 | -45.20385 | 2025-09-30 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc34966a-0184-355c-a6b6-552b7b67b538 | -10.89076 | -53.74815 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2befd99-2bbd-39cf-bcca-21a88430b3e5 | -13.8144 | -47.47725 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91f3a565-70be-3fd9-9843-fdcb551151da | -9.32701 | -49.83494 | 2025-09-30 04:40:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a347676a-b4f0-3337-b428-92e54e162a3d | -12.87191 | -46.9017 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 9eb24867-2aff-3921-a44c-75540ef778fc | -13.52638 | -49.4788 | 2025-09-30 04:40:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aff8d8d4-3791-371a-8462-508a68b40a2e | -7.77552 | -45.7229 | 2025-09-30 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a79c3f9a-cd7a-3761-aca4-09e6f9b1a8c3 | -10.83519 | -46.6723 | 2025-09-30 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eead673b-e601-3811-9cbe-beba5bc91823 | -12.96954 | -48.41467 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a7388e80-903c-3cec-ab7a-80ae441f677c | -13.34494 | -47.81172 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22ca264b-d83b-3229-bf98-af03b53aee2a | -11.22186 | -47.20612 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| cf13b58e-2325-3378-b095-a45aa25872d2 | -10.42983 | -46.14704 | 2025-09-30 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 18c28414-0a13-31c9-be26-8e33af7df695 | -13.23992 | -48.44206 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5fa9fcc3-0647-3c45-a6c9-c7fea12eae98 | -9.05865 | -47.62213 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff5c78f7-7087-3f72-bd64-86b1d3be4199 | -12.83839 | -46.97618 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6667e056-2491-3e65-8a5a-ef0299e7ca75 | -10.18883 | -44.90232 | 2025-09-30 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 76d0cc71-04ec-3a6c-b811-f790cd6fe4e2 | -7.78539 | -54.92478 | 2025-09-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 584bd5ce-37ea-39c2-9ed8-c027c7ce2b35 | -11.84043 | -46.62078 | 2025-09-30 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90f1fc39-5665-3404-9c45-c106cd647eb2 | -10.63869 | -53.68634 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c89fedb1-0081-36d2-b3a0-915f9ea2a9c8 | -11.37562 | -45.06276 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da3e7ae8-0659-367d-ae85-a6bd09e674be | -13.8323 | -47.50336 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 96f57e8c-a310-3747-8fd4-f9a5e2285508 | -9.32516 | -50.63194 | 2025-09-30 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba047bf4-35bf-3e2a-a9d0-ce4639f665a6 | -11.88922 | -48.05658 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bda38160-cc82-3017-9889-4a2229740709 | -7.76479 | -45.71685 | 2025-09-30 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6eaebaba-ec92-3bcd-aaf8-7e2973786b7f | -12.85325 | -47.0071 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| a4eedd15-2b79-355c-9d2c-f32b377b7e12 | -13.23142 | -50.93605 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 04117781-8019-3c39-a95b-04420b1e5af5 | -11.14843 | -54.12289 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ad64307e-0000-332a-98b9-8b0c6875db47 | -11.89048 | -48.05143 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 78d92fdc-d373-3eb2-9aa3-78f78c78cb4e | -11.7556 | -44.73969 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 34.9 |
| ba94b081-3c3c-37f1-9a75-165e62fa37c9 | -7.82726 | -46.99252 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e55e2163-a546-34b0-bfd7-d8ef9d87ebee | -11.88571 | -48.05603 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 553fa1b3-6309-3793-888f-eb3f51d6086b | -8.8695 | -46.59137 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33fe83a4-c20b-3995-be4e-dcecba9960ef | -13.02042 | -49.44666 | 2025-09-30 04:40:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d85f8085-c1b3-35e8-82ad-87d31222da04 | -10.64158 | -53.6912 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9493928d-ac5e-3ddf-9504-dcb234333587 | -13.36579 | -47.29255 | 2025-09-30 04:40:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e8e76ca-c223-3409-973a-a0fcc302eed1 | -10.40026 | -48.14282 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18785431-289c-3f56-8bde-6b095c851ecb | -12.84379 | -47.01988 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 92c3da60-0923-364d-a70f-75b730bc06ed | -8.38429 | -51.06688 | 2025-09-30 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7aa5e759-5c07-30f7-b3ef-c7142cdfaf24 | -10.3848 | -48.15164 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05b8a90c-a8d4-3290-8d2d-592ece21999d | -9.40309 | -54.70305 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29081b22-9f67-35bb-b0c6-fd01131f6e3c | -13.56972 | -48.0905 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29650827-a725-3b2b-8ec9-c1288e44b98f | -8.27023 | -45.50995 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9fdbf3b3-324b-30a9-9311-7ce404d4d3a3 | -12.87341 | -46.78006 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cf01b5f0-7c80-35f1-ad40-9dab37a41855 | -10.79891 | -45.36151 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f686d67-97d2-3e34-b5d7-73da61e144f1 | -13.81263 | -47.96019 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86d44b76-cb21-3684-ba6e-4b046bceac7b | -7.91162 | -44.6333 | 2025-09-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 65a8972c-6ae9-3249-ab4d-06d05da842fb | -8.89976 | -50.58845 | 2025-09-30 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e914d46-c09f-39e3-a0c7-7e305bfe81c4 | -13.57802 | -48.05828 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35dac715-c706-3c9d-bd8b-b86ae3584870 | -7.04615 | -45.17857 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce78c90e-cb73-3260-8ac1-aba3675291cf | -14.04007 | -42.15461 | 2025-09-30 04:40:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0977ae42-994b-320f-b8bd-925ddf2b1fa2 | -10.65318 | -48.58629 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f27bda17-e9d7-34b8-818c-258c2e93bdcd | -11.43235 | -43.50053 | 2025-09-30 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7d2bbffb-efc1-35c4-98f0-351185de8943 | -9.93731 | -47.45467 | 2025-09-30 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e804e9f-8cd9-30fc-90b6-74b393ed8566 | -7.76616 | -45.75974 | 2025-09-30 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56f9c053-b2db-3f53-b9cf-9a845e996d80 | -8.15531 | -46.38597 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2b576d8f-415d-33ca-b3ed-fb8b03cfb8f9 | -5.98877 | -51.90321 | 2025-09-30 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba2f184e-f1bc-31b4-a5cd-ab00728a0612 | -10.81814 | -45.3715 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3d0dde7-e8c8-39de-bf98-e18b14d35f90 | -11.46133 | -44.99593 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2e653601-efef-3750-aade-084a03df5ac8 | -11.25599 | -47.23201 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a6f2efe2-2f6e-31ff-94da-2ee28ab1248e | -11.45261 | -45.05806 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 37bd8f3f-78bb-377d-b544-aa2b6bf52f18 | -11.99482 | -46.59631 | 2025-09-30 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb33b576-b740-38d6-aef2-460acceca8df | -11.87986 | -48.04694 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 70e98141-0b66-3ec3-b003-1da9bff98a10 | -13.58277 | -48.05071 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b32c723e-e84b-3250-ad95-d96733771ee6 | -8.25486 | -49.84193 | 2025-09-30 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 025c2ce7-48fe-313a-875d-1d47ca55d5ef | -13.78663 | -47.96173 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 98c3bd63-c9f8-3643-98cf-73b502c471d6 | -10.25689 | -48.05122 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2401806f-8e2e-34f7-b381-20d678f6a72a | -9.04006 | -46.70304 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8e88cde7-7ab2-3a8c-b586-7633a7237b12 | -9.1319 | -47.63332 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 30f8465f-70f6-3b7b-9aee-dfe3a5804cbb | -12.87249 | -47.11414 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b19ccb74-9299-39f0-9436-9822973fd07d | -9.4247 | -54.72494 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 626d5358-43de-3f8e-89fb-0b544d681b2f | -13.39524 | -48.07518 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 84dc07ff-b0ce-3af6-ab2b-b10c27b70a00 | -13.01141 | -49.43756 | 2025-09-30 04:40:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d969544f-aa32-3b84-89ac-e5853b933ada | -11.46382 | -44.98703 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9af71686-f905-37f9-a8d4-d607f6e2f96e | -13.08863 | -47.03683 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35ece30b-6aab-3b9f-916e-76d63274d0d8 | -5.98751 | -51.91096 | 2025-09-30 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a167e951-c462-3ec7-b270-eccb6bb27026 | -13.21858 | -47.32727 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8fdf2d3e-2d2f-3985-834e-1ab114877635 | -10.12254 | -45.67488 | 2025-09-30 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cb71ddb5-6299-3247-992f-4d6b08159efa | -10.39453 | -48.13377 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d835318c-0b15-3227-8803-1efef46b9274 | -9.32095 | -49.83043 | 2025-09-30 04:40:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6cc43915-27af-3841-be4e-b443b186017e | -9.62661 | -50.89899 | 2025-09-30 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d57c068-2207-3b1c-aff4-b31546269fe2 | -13.09305 | -47.03274 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e5fad70-7847-38ad-ad67-cf2c05bb78b2 | -13.7713 | -48.3227 | 2025-09-30 04:40:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2b8d950-3a51-366e-9ed4-19a5c6175509 | -8.04789 | -49.70258 | 2025-09-30 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ccdb183-dce2-35c4-b7db-ae10cab8fea5 | -11.22549 | -47.20672 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d11a3441-a08c-3542-9ae8-6d03b95364a0 | -11.8869 | -48.04803 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c3e98cda-719b-3e09-8473-453429a46799 | -14.44409 | -46.35761 | 2025-09-30 04:40:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee8973ec-03b2-3160-8993-f454f17a4a1e | -14.57406 | -43.72738 | 2025-09-30 04:40:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a51f66d-5a0c-3c0c-82b4-c68efe542c26 | -13.73814 | -48.67194 | 2025-09-30 04:40:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c229abd-a5fe-3d02-ad51-b1bc27d61f39 | -7.44707 | -46.99268 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 650046ed-80d9-3ed6-9c34-388b2d50d87e | -11.45651 | -45.01 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71928b18-6d0c-3d0d-9d9c-dedf0d49015d | -10.08312 | -46.06176 | 2025-09-30 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da329325-f5ed-3113-b069-cb4a520b7bbb | -7.37415 | -47.04669 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 925f7ee8-3092-3223-a3d4-299bb8ce86d4 | -11.25505 | -47.23331 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 79e774e6-e9be-360a-9e40-8ccf4d5db354 | -7.50112 | -45.44983 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1657942f-abd9-39fc-80e4-3b7545cd0bdb | -13.79456 | -48.00929 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7abcb26-ddad-37e8-a789-1a6b024b1634 | -12.75987 | -46.87306 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |


[Clique aqui para ver as próximas entradas](README70.md)
