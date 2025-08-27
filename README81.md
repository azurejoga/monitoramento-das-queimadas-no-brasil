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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0684b32b-33fc-3033-95d6-682b891f2556 | -10.0977 | -62.9085 | 2025-08-27 06:00:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 7e4e064a-3b46-313a-9e20-f22e62d89b60 | -5.60684 | -60.22529 | 2025-08-27 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4eb6007-1fe9-321b-b1b3-f0c38311ab08 | -6.81133 | -58.96097 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c7407759-3bb7-3f10-b546-bb3f58cbe7e8 | -6.83833 | -58.96482 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 65ed135c-72a7-3727-a1cd-669beece1de3 | -5.91918 | -61.30387 | 2025-08-27 06:05:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5c07fae-38da-3ba8-86b5-4d5181649b0c | -7.35052 | -59.66682 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdaf4644-8125-3b09-bcc3-8aeb4459a341 | -6.81644 | -58.97401 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ed9bac86-1a6d-347c-a62e-e9681666944e | -6.84425 | -58.97177 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 9cfc29c4-d087-33a3-924f-c08d11fd9104 | -6.81726 | -58.96799 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b9d78243-48b0-3fcb-923c-7384d3cf14b5 | -6.24218 | -60.01879 | 2025-08-27 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5c75d555-9afa-3777-b4f1-3ab2abd9d43e | -7.35705 | -59.66765 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f782a751-3f6f-3a45-982e-b50d9de51286 | -6.79147 | -59.64045 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d14c68e5-5b65-3165-95fc-8e25c7ae53d8 | -6.71041 | -58.56147 | 2025-08-27 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a64a7300-bbc1-338d-b70b-bf3be52fdfe9 | -6.78571 | -59.63414 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dec8c49d-54bc-3540-bb37-381b09cdc868 | -6.24031 | -60.01008 | 2025-08-27 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0453f9e2-6465-3703-8e19-fb517b6db7fe | -6.941 | -59.56391 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 46d2989e-dfa6-3603-a6f1-6fe2f55c39dc | -6.25476 | -60.02052 | 2025-08-27 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f092ede6-14f6-37c3-9998-41a87707ba2b | -6.79221 | -59.63497 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 37cc557d-b9b9-31e6-9617-662037fbf01d | -6.24985 | -60.00978 | 2025-08-27 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e8640311-00c2-3f78-a6b2-a833217a9905 | -6.8232 | -58.97484 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fa559f79-3f99-3082-8c96-5098a02ba5d0 | -7.35631 | -59.66885 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01971d27-5204-34b3-90b0-ab0761d0c1e9 | -6.25293 | -60.0116 | 2025-08-27 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2c5fa144-ca4c-3517-a948-1d38cd021722 | -6.84047 | -58.9656 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 32c9026a-3b90-3511-8b09-f7a8d6ab9621 | -6.23402 | -60.00921 | 2025-08-27 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 674f6888-5c71-3620-800f-a7d4fb81c44e | -5.4531 | -60.15965 | 2025-08-27 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 342993c0-5917-3643-8174-50787d2f2ad4 | -6.8262 | -58.96959 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b07fe7f0-9d8e-39b5-912d-185f5282c546 | -6.76691 | -59.67612 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c704b103-9ea3-31ec-b814-2553e7eb124b | -6.81867 | -58.97469 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2721426e-fcfe-3152-8e77-a6491fc9234b | -6.76764 | -59.67066 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af4e7aa6-bb83-3c2f-8a75-beb9d39e9024 | -7.41453 | -60.62345 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ae2d1e5-50a3-33d0-a1b3-93bdc1cbba7c | -7.1685 | -59.74112 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 078b5189-2018-306a-a690-1d281e3f9695 | -6.78497 | -59.63966 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 84f002d0-6ad7-35c4-87a1-904e23d85d03 | -5.45376 | -60.1549 | 2025-08-27 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0dbf42c-044d-3e2c-9d01-4864727c6f42 | -6.81808 | -58.96194 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4250ad4b-f371-3eaa-bc80-ab203dc88956 | -6.23901 | -60.01991 | 2025-08-27 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b42a9da-fb5b-3fe1-a25e-c24186a83c68 | -6.82401 | -58.96889 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 31b10158-d558-30e3-8ac5-ff5d19fa8f57 | -5.91862 | -61.30792 | 2025-08-27 06:05:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d212e3b2-6f6b-3054-9881-b8fd93faf70e | -6.83373 | -58.96458 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 33725d6d-b21b-3e22-b834-388756112ea0 | -6.83751 | -58.97075 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 74791a43-d226-3b7c-91a3-14da206a9220 | -6.90813 | -59.36004 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d71ed28-9d62-33ef-9091-361504ec4392 | -6.24149 | -60.02375 | 2025-08-27 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 306f8cfc-6b2b-3db1-9880-c0f5f4dbc72c | -6.79074 | -59.6459 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31cf9fe2-8385-3e82-849f-31076c5e94b6 | -6.82543 | -58.97555 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f8333c2c-1289-3d52-b031-7b19dfeff1cf | -6.2516 | -60.02157 | 2025-08-27 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9727a60e-21ad-3da0-a60e-06735f66adee | -6.23724 | -60.00825 | 2025-08-27 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af17837f-e07d-33fe-a5fc-e9b2eb0cc991 | -6.82023 | -58.96263 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 00f7470c-d20c-38d3-adef-3e7b4409b53a | -6.91474 | -59.36095 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd03de8e-d73c-33b4-b634-6ef990ac9770 | -7.43316 | -60.62066 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfd4eaa8-9017-3874-9490-a8af669abe95 | -6.81348 | -58.96168 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5055e9a5-431e-3df6-ab9a-d070188e26ef | -7.34399 | -59.66606 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bde53ff4-835a-3a0c-9e1b-1b2da33d8fa6 | -7.427 | -60.61984 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e143beb-7320-327f-9810-66a22c4644d5 | -7.43362 | -60.62124 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9dcd61f3-f6cc-3e05-9042-d536f6a4498b | -6.70959 | -58.56768 | 2025-08-27 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7517a9e6-91fe-33ee-beb1-b408579b24cb | -7.34978 | -59.66798 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 373458ad-8b1b-3fdd-8572-27db8bd335b7 | -6.76838 | -59.66508 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f65050fc-93e0-3bb8-b8ff-115f1cbd89e7 | -6.24466 | -60.02563 | 2025-08-27 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5537ac5d-7b63-319a-bfdc-be7991827395 | -6.81052 | -58.967 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f60c701-452d-3479-bc73-3a616c63c22d | -6.24532 | -60.02061 | 2025-08-27 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a36646e-844b-3df0-8d7a-8338bdfb0267 | -7.34325 | -59.6672 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 365abd2f-693d-3bcf-bd1b-2d452c360400 | -6.94016 | -59.56487 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 950b371e-5e42-3946-a492-25935d54c7e1 | -6.83077 | -58.96976 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bae16df8-d988-305d-8e12-e675df94f7a5 | -6.94086 | -59.55949 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d61f513-5738-3f89-b533-76fff7332c34 | -6.24779 | -60.02457 | 2025-08-27 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af482828-16fc-3506-9096-92a74d2fc439 | -7.42746 | -60.62044 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91a2865a-037b-3095-88c9-e2f13717ddf9 | -6.8179 | -58.98063 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ec2fdcf-0683-363e-ba24-f55ca57db9fc | -6.25546 | -60.01553 | 2025-08-27 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 99d08fea-3d66-3f73-b392-c71dc23a1832 | -6.82239 | -58.98076 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d7a2b4fd-e84b-30f6-a17d-993e4edd72d3 | -6.84722 | -58.96659 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ec50630-6038-3d1f-a1da-24f6c4b1bbba | -6.23655 | -60.01318 | 2025-08-27 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4350d34-5098-3932-a8e2-87b89c095862 | -6.91398 | -59.36665 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 520d5a60-4d56-3bb7-b0e7-8e277909258e | -7.42131 | -60.61962 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c05dd9b-ccca-3b1e-acba-33bdbb458f1a | -6.24096 | -60.00517 | 2025-08-27 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2de8c32-b961-3404-9a3e-49296eb0e04a | -6.84507 | -58.96579 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d3ff496e-c5bd-3fb4-8f29-624706312692 | -1.42369 | -60.39979 | 2025-08-27 06:05:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5225a840-aed7-35cd-8c4f-55eea527799a | -6.25227 | -60.01656 | 2025-08-27 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d0658d0-b7f6-3739-9ecf-af22cd683058 | -6.23966 | -60.015 | 2025-08-27 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 14cef86a-2f92-3c16-98c3-4ecf2e1fbcf8 | -6.8127 | -58.96774 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ff8a61a5-422c-359f-88a2-d4ceab06ad77 | -6.81944 | -58.96871 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5a569f22-e5f7-3162-98f7-7ed6bee35eed | -7.34394 | -59.66179 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4571719-0ce9-32d2-adf9-49836d11baf8 | -7.34471 | -59.66066 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c985f3ae-6b0a-38d1-b4ed-eeff2921d673 | -6.81192 | -58.97379 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 400a82c8-c246-3a22-a37b-bcb53861b59d | -6.70352 | -58.56038 | 2025-08-27 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1826aa30-ca42-3bd5-a937-eb49f5ac3722 | -6.83969 | -58.97156 | 2025-08-27 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 7a9502d7-bb8e-3da0-a0f8-9915dc42e044 | -8.95852 | -65.96149 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a9d562b2-8d33-32fb-8651-99eda3bbabce | -8.95974 | -65.95297 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| db551f45-a0cb-34a5-a1a5-5eb0d5790a85 | -9.41385 | -60.53926 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7e30f4e2-fa0a-321d-a2a2-192752e59d86 | -9.78844 | -64.24378 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0677f4d7-e9b6-3761-ad94-855189e158cb | -9.40066 | -62.49075 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ed016ef-010d-3811-a931-189462eae653 | -9.79095 | -64.26315 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d3d863a-8ca9-3404-9f6f-7345f0fdf6df | -9.16637 | -60.77354 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c35d305-aab3-3925-906d-f0a5ced66cae | -10.5084 | -69.35263 | 2025-08-27 06:08:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 848e3fee-9024-3134-9d01-40e11dfb6a02 | -9.22851 | -60.92319 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f58a759-387f-3d9a-8010-e15826c63dc1 | -9.15897 | -59.54555 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48a00c43-8bde-329b-81a6-5808a66e99d6 | -8.96043 | -65.97933 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| adebbd89-6d6f-32f1-b7e9-7b96551934ad | -8.94534 | -65.95963 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.5 |
| ba3d0b4d-06b5-31fb-b25d-b75811afeecc | -9.22911 | -60.91829 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 249c57bb-d1fb-3216-8c4f-092697350525 | -8.88629 | -62.47879 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a5f0473-0b72-339c-96f5-682e264f2216 | -8.34773 | -62.93745 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea367b82-8bab-3c73-9a77-a9e41a5990a5 | -8.72127 | -64.02438 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 89d70624-cbb9-3fce-a96e-073568ed693b | -9.16904 | -59.46117 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README82.md)
