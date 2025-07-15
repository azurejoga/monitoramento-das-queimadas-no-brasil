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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9318e3a-54a4-33fa-a2d9-bbb3a52a59e1 | -11.43591 | -45.13089 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f00ef425-a08e-34ea-87df-adb4df645e6e | -13.11763 | -47.26777 | 2025-07-15 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00f6d9b0-5544-3444-8e9c-f295d9d91b2a | -13.65988 | -45.72928 | 2025-07-15 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c976040-bd8c-357c-8656-d3542cef5015 | -13.10548 | -47.27817 | 2025-07-15 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77af6fc9-720d-37ba-a1f3-d212687ede01 | -10.8801 | -54.05286 | 2025-07-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb59162a-07bc-3450-92fe-79ea69826a47 | -16.89921 | -52.67524 | 2025-07-15 04:34:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb59d2e9-6743-3674-97a1-b6cdfa3d6a38 | -13.09746 | -47.28461 | 2025-07-15 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e42fded-eb02-36e7-aaea-dbfd5c41bee8 | -10.87089 | -54.05846 | 2025-07-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e3d2bf4-438c-3ba6-bf21-193170bd2032 | -10.86689 | -54.05774 | 2025-07-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0531a795-4532-3a23-9bc4-c493ec1b6402 | -11.45578 | -45.10056 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 41de54d9-b60c-356a-9d7c-8a7cdcc56960 | -16.83746 | -52.15985 | 2025-07-15 04:34:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ff890e3-1cb7-3627-9c09-70362e80e3b4 | -11.7329 | -47.05527 | 2025-07-15 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c1ad9b9-659e-354e-a586-4eb01dd9e97c | -10.86288 | -54.05701 | 2025-07-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d0a2e5b-bd56-3c66-abcd-6624b0a324f1 | -11.46689 | -47.31394 | 2025-07-15 04:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4296470c-069f-36ee-ba60-4facd1316d6d | -10.05938 | -59.11019 | 2025-07-15 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d3dfdec-1d53-323c-b3de-2d358a0cac4b | -13.11705 | -47.27168 | 2025-07-15 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 63f05e51-dad6-386b-a365-7154b73af159 | -11.45606 | -45.0981 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 29.9 |
| bb7a6a94-c9d5-3975-a673-c20f3b489a6f | -13.65613 | -45.72869 | 2025-07-15 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 65aa8116-10ef-3bfb-bd33-9323e0dd2659 | -11.46907 | -48.52428 | 2025-07-15 04:34:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ed5bc0b-53ef-3fae-b87b-80996317d888 | -10.69574 | -48.30103 | 2025-07-15 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 11cac188-caf8-394b-97e3-bc8bdea49fee | -10.8847 | -54.05009 | 2025-07-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d32266fd-dd54-3185-af08-000ce0700f86 | -10.56461 | -49.13748 | 2025-07-15 04:34:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 60268faf-9b32-3619-add7-2c54b09b88b3 | -11.04183 | -48.19212 | 2025-07-15 04:34:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e825e35e-d9e2-3110-bd33-d0d2ff0a6513 | -12.4048 | -45.37758 | 2025-07-15 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c126910-90ff-3d0b-bef4-d893a1190d67 | -12.92274 | -56.67946 | 2025-07-15 04:34:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5673b184-1f53-3f90-9fea-024e184c9eab | -10.54877 | -54.25236 | 2025-07-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12261c4e-ebf0-33a8-850f-53980ca054e5 | -12.40857 | -45.37811 | 2025-07-15 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ace20981-bb36-3183-a5dc-31c943a261a7 | -11.45957 | -45.10109 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 52b6bacc-b437-393a-ab17-296e8971832a | -12.43672 | -63.70271 | 2025-07-15 04:34:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b81c563a-de01-309d-9ce0-e6720e09ff09 | -11.45672 | -45.09339 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 1d7fcc62-5291-3ddd-a3c3-244073fd7dbd | -10.56075 | -49.14043 | 2025-07-15 04:34:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 0cb99576-2482-3967-99ef-d228cfdf6ae3 | -11.44393 | -45.12962 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 31.9 |
| cc518769-25c6-384f-98a8-e6abf7879e25 | -10.78708 | -49.25566 | 2025-07-15 04:34:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 886bf922-b633-389d-b4e8-b897c32e50c8 | -10.56847 | -49.13452 | 2025-07-15 04:34:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c4c41c07-b484-3547-a878-75142dce6edf | -12.06874 | -47.98179 | 2025-07-15 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be3e12af-b548-3790-babf-1b7d9ecbb725 | -10.4954 | -53.5715 | 2025-07-15 04:34:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f18f61cc-c4b6-3139-960e-8edb5b2b6725 | -10.3283 | -49.91474 | 2025-07-15 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| faca922e-bb48-39ec-90a1-b73827c8fbd7 | -10.56406 | -49.14097 | 2025-07-15 04:34:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 9881b869-026e-3687-b418-60544ce6a10d | -10.67409 | -56.55317 | 2025-07-15 04:34:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 308f67e3-de60-317f-9555-7a628912883f | -13.22643 | -49.83459 | 2025-07-15 04:34:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 50710ea8-87b9-3e50-9e3c-773ea35fbbe0 | -11.44891 | -45.09479 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 4b4b6ff6-c471-3409-80a8-273b5a45ca57 | -12.40923 | -45.37347 | 2025-07-15 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0099ac32-e638-3b08-8314-bf4b184cdfb3 | -12.6783 | -47.86952 | 2025-07-15 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bcdd667f-c620-3138-a7ee-24d11215a004 | -12.40792 | -45.38276 | 2025-07-15 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f602cd2-bfc0-33ae-ad4b-4b821535c402 | -11.4477 | -45.13017 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 379fe75b-d749-3247-a6cd-01177105365e | -12.0721 | -47.98232 | 2025-07-15 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 074f0094-5483-3e08-ac2f-29624f624a8d | -11.45227 | -45.09755 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| eeb99545-4cda-3876-94c7-76aa3d603e9a | -12.07802 | -43.47819 | 2025-07-15 04:34:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 738f10aa-a01c-33d1-ac36-2ada787c86b4 | -10.16893 | -52.62086 | 2025-07-15 04:34:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1285f599-6432-367a-be6c-346a44bc9f46 | -11.73347 | -47.05145 | 2025-07-15 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 847287e0-83ea-37d2-86d2-22a3c2b0d0e8 | -11.94012 | -45.76366 | 2025-07-15 04:34:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0d47c80f-0057-3661-810a-9d4e04ba9215 | -10.57122 | -49.13854 | 2025-07-15 04:34:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 4b43b40a-d324-320e-9d66-d73025b27882 | -11.44723 | -45.13255 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 56bc5899-73da-3cec-831d-36a86b5d9b59 | -14.58597 | -48.11675 | 2025-07-15 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfbdcc61-3f89-3655-9c4e-eeb733bd3aeb | -12.40545 | -45.37293 | 2025-07-15 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9306ad7-7f19-3f0b-8998-0facd74f16c0 | -11.91054 | -46.75561 | 2025-07-15 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b98558d2-6f29-341e-bbf1-68cbe99ed328 | -10.96105 | -49.25177 | 2025-07-15 04:34:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 767f9827-eaf4-3759-841c-f006e35732cf | -11.44822 | -45.09946 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1366082f-b524-362e-a1aa-56890f9eac8e | -11.44036 | -45.12682 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 390a976b-2ab9-3868-8acd-65b62172718e | -11.44345 | -45.13201 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 598d7cde-feee-3a7c-8867-3fd2131fd36b | -10.38233 | -49.89803 | 2025-07-15 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 31040186-2c76-3b0f-85d5-fe09d967299f | -15.74598 | -49.64384 | 2025-07-15 04:34:00 | NOAA-20 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 986e69f5-9998-3a88-8547-2214ce4ba2f6 | -11.8563 | -46.7525 | 2025-07-15 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 97f32990-33d1-30a9-8413-30114a80be68 | -10.08958 | -52.7399 | 2025-07-15 04:34:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7edbaac-900b-3b82-b4a2-af11589948cb | -12.28962 | -48.79309 | 2025-07-15 04:34:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5968bea-7bf1-3d2a-bb79-ae0342ced266 | -12.47534 | -44.49794 | 2025-07-15 04:34:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 371c3f20-cdf5-39b6-8a55-b1720edf32ae | -11.44512 | -45.09424 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1d9c0e25-deba-31d8-810f-031bfb6e8049 | -11.4605 | -45.09392 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| fd929b55-b0da-3ccc-a9fe-b5ec757d9428 | -12.07383 | -43.47739 | 2025-07-15 04:34:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 695398bd-7020-306d-b836-61aa1722077e | -10.55285 | -54.25304 | 2025-07-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c84f13d0-4c26-3186-bf87-68e115abbaff | -10.09332 | -52.74057 | 2025-07-15 04:34:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e158394-6c55-3576-a720-622a7d3094c4 | -11.44849 | -45.097 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 1f4edb87-4640-36e8-8db7-ad44688deadd | -13.65678 | -45.72409 | 2025-07-15 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c3575730-402f-3322-8726-133fc568c3d1 | -10.57453 | -49.13908 | 2025-07-15 04:34:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45a97173-0184-316a-8d02-58f4fc3e0d28 | -10.3322 | -49.91172 | 2025-07-15 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| beafc710-1cea-302d-8952-177e9c021cc4 | -10.67289 | -56.55653 | 2025-07-15 04:34:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 11512aee-4edb-3b04-b5d9-cd6a4afb5bb0 | -11.44278 | -45.13665 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4c60ab16-52d9-3c5e-b725-f56361c026ad | -13.04689 | -47.81272 | 2025-07-15 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2c6ffd7-9a7d-3e21-bc72-0dc229200551 | -15.74654 | -49.64026 | 2025-07-15 04:34:00 | NOAA-20 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90a21297-fd4f-3322-b46e-ff1dd57e96df | -11.45162 | -45.10223 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| e6d48755-512f-37e9-a042-d1398c9cffeb | -14.58314 | -48.11251 | 2025-07-15 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7b59ebe4-39ae-304b-8158-76bbbcf07298 | -11.45738 | -45.08865 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 1251c89d-18bc-3609-83c0-492103b090fe | -11.80769 | -44.26308 | 2025-07-15 04:34:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0cfe7b5-8980-3138-8999-f648c06e465f | -13.65924 | -45.73388 | 2025-07-15 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdb2caaa-fce9-38c8-b5a7-225fa0f3dcc5 | -10.12962 | -57.7776 | 2025-07-15 04:34:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5df4c6d-031c-327e-b2a5-868d2f08ae3a | -15.22669 | -46.96387 | 2025-07-15 04:34:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03e084cd-8a80-3f94-8d4d-30b9fae1262d | -10.89305 | -49.20819 | 2025-07-15 04:34:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 384678bc-7e93-3d97-b06e-35370d313241 | -13.1285 | -47.26608 | 2025-07-15 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd8a25c0-7c11-398b-9209-3534ca796110 | -12.40104 | -45.37704 | 2025-07-15 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63d0782d-8cf9-3b35-a09f-3837fdef3536 | -14.57582 | -48.11493 | 2025-07-15 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c85eb91b-ee7e-30fc-95db-161b26f02e0d | -10.64395 | -46.62079 | 2025-07-15 04:34:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f78074ed-afb8-34f3-854c-43046d43bcb5 | -12.40415 | -45.38222 | 2025-07-15 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec943eb4-4502-34b2-b6c5-3e91a1daf18e | -11.46575 | -48.52375 | 2025-07-15 04:34:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bdb4ae4-8a03-3dc2-b426-50400a0a3ab8 | -11.47086 | -47.31072 | 2025-07-15 04:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fd828e5-9a1a-3088-b727-6f5dc7816d1c | -10.49844 | -53.57722 | 2025-07-15 04:34:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4e412d7-e0d6-369f-a91f-1452ce97a278 | -11.90355 | -46.75455 | 2025-07-15 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7956e960-bdfa-36cf-a2c8-2a99c0db3e21 | -11.46363 | -45.09915 | 2025-07-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db0c2a3c-caa8-30bf-bb39-ad4ca79db1a7 | -12.40038 | -45.38168 | 2025-07-15 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 819f5cd7-762d-3ee8-8ced-0fd9d577d8e2 | -13.04407 | -47.80835 | 2025-07-15 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83ba1f2a-359f-3072-b3c8-c9e533355c64 | -10.56791 | -49.13801 | 2025-07-15 04:34:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |


[Clique aqui para ver as próximas entradas](README21.md)
