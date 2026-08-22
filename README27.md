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
| 326ac752-63e6-3599-bb84-e3b843d0d58a | -12.27708 | -43.16725 | 2026-08-22 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 2ee769ff-047c-3b5f-be8c-a955637fc74c | -6.54393 | -58.52372 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c7b68412-f8cc-3880-866f-db7443cda6e4 | -7.36481 | -55.69089 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 942f6b3b-0cb5-3b90-9911-c31dcb64c0e4 | -6.80282 | -59.42905 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 2aa46be6-07d6-315f-912f-8bf4b179354c | -8.99233 | -50.73597 | 2026-08-22 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 972b58b6-e058-3088-b3dd-4582a171066f | -8.52353 | -54.83788 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3c33940d-115a-3d38-9655-2864f0a8a90a | -9.16811 | -59.44202 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c0ce90cf-08e9-3311-b8d1-bf2b0a669058 | -12.76203 | -48.47464 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 146ea9c9-6ffb-3dc2-8d3b-cdf0d663cfe7 | -7.46497 | -45.13001 | 2026-08-22 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| cc6e4c68-f1cd-3066-a1ee-cc1ab27d06d5 | -10.88745 | -50.25919 | 2026-08-22 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef1ebc1d-5a34-336b-b069-0be75bb74bfd | -5.9949 | -57.81776 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c7d3a963-5667-31a2-bbeb-baba8f27e8b2 | -7.02043 | -59.55787 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93d9545b-52f9-33d9-a500-b71c42c16995 | -11.33652 | -45.03212 | 2026-08-22 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f817fae-7168-3e95-87e1-4e36c54aac35 | -11.59968 | -46.54988 | 2026-08-22 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 7dc22bc3-6286-32d3-9e9a-07cd008f3a95 | -10.80874 | -50.97867 | 2026-08-22 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 28.2 |
| da27f66e-e871-3095-9866-0e0c98699de9 | -8.53631 | -54.83641 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 28a59f3c-2f76-374c-ade1-8f92192807ba | -12.82849 | -48.46362 | 2026-08-22 04:27:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aea26756-6055-3659-98a5-b07be65c347b | -6.77489 | -55.695 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 584646b5-58a6-3d6c-a9e9-74ddff7aea7a | -6.88778 | -56.72863 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c773ab9-e97c-3ddd-86f5-8a5947f5febc | -9.45105 | -51.64356 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e3c4bc5-7040-3961-b92a-2cfb0aa04834 | -8.09056 | -50.03223 | 2026-08-22 04:27:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2fbe78e1-e53c-3dcf-bd13-2e10ac62858d | -7.72675 | -46.14516 | 2026-08-22 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ddc3aeb-96ac-3758-a9d4-a3d1e5495886 | -6.76502 | -58.66926 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 52e29666-807b-3851-9190-05ea0b6fb411 | -6.78087 | -59.421 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| a165e042-92fb-393c-a67b-651b3f4f70b4 | -8.53925 | -54.82007 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d37341ce-7490-3d72-811c-7b4d39e7403b | -7.06002 | -59.83775 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fe72e1fb-bbbc-391e-a21b-a62b733d27bc | -6.96324 | -59.04989 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 4f88ffe7-134f-3073-b707-96b6ec1320b5 | -9.21132 | -59.76638 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e435e0cb-aee7-38d0-82d9-4ae38af64746 | -6.82005 | -59.39672 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| edb2786e-739b-3bc2-a465-44672184f6ce | -9.76232 | -48.17012 | 2026-08-22 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14cdccf7-f441-31f0-b6f2-ffe4ff8b8d9a | -7.33523 | -46.23688 | 2026-08-22 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ab53dd7-ee71-39a1-a65a-ac7796d98547 | -8.17284 | -54.98813 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 54546c8c-7941-30d9-864c-254b1f5d7c6d | -9.17243 | -59.45419 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 6cca3a91-7e53-362f-864d-4b1fc9981071 | -12.74342 | -48.46362 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 06c2580a-b494-3b99-86e3-62cebf25d2a7 | -11.4381 | -44.5572 | 2026-08-22 04:27:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 323a5215-eb86-371d-a96b-8b1ad2b445a8 | -8.5364 | -55.32654 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7862ced9-54c5-3de7-933f-87dbcbef8b8f | -9.15944 | -59.45184 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 8ad2d319-6507-38e5-8e0a-04f448c10623 | -6.37528 | -54.95634 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0ad20949-bfbc-373b-9874-da3867085a4f | -6.00107 | -57.81892 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0272a21f-6365-39c4-8ccb-34a3b5f1acc0 | -12.00196 | -53.42667 | 2026-08-22 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc070dcb-a0aa-30c5-88c5-5cf3d18f6f9f | -6.85101 | -59.43159 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d95e1a92-5d1e-3833-bc1a-c189c5adeb5b | -11.1398 | -49.03948 | 2026-08-22 04:27:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50a3669a-e98f-3068-a52b-9d30b892a3c0 | -6.75147 | -58.67448 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| fe19d74d-6ccf-336e-909b-136277400d7a | -8.03993 | -51.79755 | 2026-08-22 04:27:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7470dd2f-36e3-37ff-a117-cf8473450641 | -9.18552 | -59.45742 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bd19506f-af86-3a1d-9555-8a048f15cf43 | -6.8637 | -59.03781 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ea096ee4-8c58-3ebb-82ab-5cfeac2e511c | -9.39523 | -55.97916 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6053eafb-882f-38c0-871c-e06d68bc114f | -12.82905 | -48.46005 | 2026-08-22 04:27:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 68ed6427-fd8b-37f4-a155-05d7bb086af7 | -12.80979 | -48.40967 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ffa54fc-eb3e-3f35-a1f4-286868398f70 | -8.59169 | -54.723 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a31a8a2-ff8b-3ee3-a622-5fdc0137c295 | -6.10938 | -59.94057 | 2026-08-22 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 07c19940-7ff4-320d-ab76-f67cc3ad8e39 | -8.22339 | -55.02516 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd28bb1e-018c-3630-b91a-888e6428493a | -7.49969 | -60.07373 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d2d9ae35-34c4-3fa2-b254-23e388280d82 | -6.94225 | -59.31277 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c1f8aac9-5936-3d9a-8e3d-90332eff1b63 | -10.27925 | -50.37725 | 2026-08-22 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82a6402d-9486-3091-8ee5-765c47e82590 | -12.76785 | -48.39531 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1220f9ea-555b-37ea-9a45-ae87dc848ed8 | -14.00081 | -42.48069 | 2026-08-22 04:27:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 7ff2bc7b-3d98-3fa5-9d7f-ac91a2999b5e | -6.22831 | -55.48421 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 45ff1f41-1342-371f-b1ad-0f7713bad34c | -9.05432 | -57.07442 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ef40e6b-0dda-31ed-bc70-84d9e645ffef | -12.74398 | -48.46008 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8402d74b-936a-3777-aa2a-35764ab5d36c | -6.54487 | -58.51847 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c6c878ee-bdad-39d4-aff0-d20f0c670621 | -6.79893 | -59.43611 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e2ec0ee8-06b9-3295-9c99-993a95c4e7da | -8.10956 | -51.6636 | 2026-08-22 04:27:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1459bf99-69d6-3282-b7be-5efdfb542bad | -11.16348 | -54.02023 | 2026-08-22 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 936c05a6-0eca-38e3-a546-8c012dac1674 | -10.52362 | -50.82179 | 2026-08-22 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 13adae02-158f-317c-8b73-96c5f245679d | -6.78174 | -58.69063 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 923b95ed-c8a1-3126-b7c2-73cf69b06643 | -10.90211 | -50.23661 | 2026-08-22 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d857864e-02a5-36d5-9b5f-21414c4ee9bd | -8.34042 | -46.48421 | 2026-08-22 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 402631a3-cb42-38b4-8fb2-00efa37bbaa5 | -7.64362 | -42.72883 | 2026-08-22 04:27:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 42b8dbc1-2abc-36a5-9e40-854bb636d5c7 | -12.77002 | -48.40303 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3cef75a8-66b7-3142-b4ba-7451b1e4a195 | -11.16507 | -54.01144 | 2026-08-22 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eef60a62-be03-3b78-8934-497eed75b685 | -13.47632 | -44.04087 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| adc5392a-e603-3864-8e95-9719cead72ef | -8.53339 | -54.82462 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 0a95a424-9073-3284-8749-0977ac8f2ffd | -10.51644 | -50.82211 | 2026-08-22 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3baed558-5142-3b11-b7ab-12998f3a85c6 | -9.42677 | -51.64481 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d6ad9f9-fff2-3dd1-a2f4-c57a67707c3c | -6.75117 | -58.67238 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9aeff68d-1513-3e67-9b3b-74c9b7e25f68 | -12.71693 | -48.41582 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 727bd652-25a5-3dd5-aa2c-4581b45eb55b | -8.09246 | -51.66779 | 2026-08-22 04:27:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 630b745c-314d-33ba-b270-c18bd8a056cf | -6.78858 | -58.65367 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eaff0f5c-bdbe-3f13-b3e3-d0429e076902 | -10.81242 | -50.97929 | 2026-08-22 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 74c1a2b2-beef-329c-b21b-e2520cd56421 | -8.68093 | -49.52951 | 2026-08-22 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8146ee72-db46-361e-a156-5ddded39d9e8 | -11.05092 | -49.10834 | 2026-08-22 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1690b5ef-5a4c-3efa-bebb-4cd44d26320a | -6.43683 | -54.95253 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3276d1d0-222d-3f6b-ba1f-7451612d648f | -9.44238 | -51.64739 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4000f0d0-3a35-3f51-b3d7-75b2499d4c30 | -8.53166 | -55.31783 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b90b9f99-c7bc-37d8-b35d-44fc6202f6e3 | -5.99577 | -57.81289 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 73e30f33-8f2c-32c5-8294-d0a34ebe37ae | -6.79833 | -59.41616 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| f3c7ea0a-0afc-3da5-8c55-eb61ea3508d5 | -5.79712 | -57.5469 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c053b252-07d0-3d64-be08-7c3154d32b5b | -6.55213 | -58.51485 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a748933-43c9-3d6e-9e2e-dc3755e0283c | -7.36541 | -55.6875 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 45990011-b75c-3dbb-80b2-a947577dd6ab | -14.01576 | -46.21448 | 2026-08-22 04:27:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bd533cff-6a3c-3f93-81d5-656c5852ef4d | -6.77429 | -58.69487 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8762bfb-5d2d-3d6f-9df4-9fea3c49a045 | -12.75688 | -47.11164 | 2026-08-22 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cae611d2-cc84-3839-bd76-12fc4b42e988 | -6.0923 | -57.8725 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee817897-e972-301f-ba52-8ee86c0249af | -6.39112 | -54.95602 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b9ca0e07-31de-3166-a013-426854607726 | -8.52943 | -54.8466 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| ac265a0f-ad5e-322d-92e2-3076464de6ed | -6.81065 | -59.42448 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| f63c60e2-9e26-3b91-9609-5c5c31341cae | -13.38477 | -54.36947 | 2026-08-22 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68d0f0ff-a06c-3191-a18e-2a93d35e50a1 | -8.96235 | -49.87035 | 2026-08-22 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac0c7d65-dbed-3626-b4ab-3adbac1a1cc6 | -6.86223 | -59.44592 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README28.md)
