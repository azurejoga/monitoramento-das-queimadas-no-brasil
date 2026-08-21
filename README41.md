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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e553c1d-091b-3d68-8680-a6d16d055126 | -7.74738 | -61.08494 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96c88ed4-e673-3f86-89c3-db9b2cd2195e | -8.38068 | -62.70547 | 2026-08-21 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.1 |
| f4596d0a-bf65-3c4e-aabf-f6e4dd78bdcb | -9.40524 | -60.439 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c6eb33d0-a2e8-3d82-b422-1ee0158ddc4e | -9.46904 | -51.63905 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 997e5b5a-503c-392a-91e4-9301a0a55222 | -8.46574 | -45.58094 | 2026-08-21 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e26b7275-f224-39ef-bdaa-b626952746cb | -9.1152 | -60.33437 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70606a89-b1ef-3319-937e-dea8288eac09 | -6.21715 | -43.74141 | 2026-08-21 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0e89f7b2-5237-37e6-951d-767a0fb78cc8 | -10.10723 | -54.28222 | 2026-08-21 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a91bcb6f-23e3-3cb6-abc7-66554eb94671 | -6.82739 | -59.40086 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 9579e071-01c8-3b17-bd4b-9f71c8e9f869 | -5.66285 | -51.64284 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6c3161af-e7c6-3015-8372-c68b4a9c7a2c | -6.58263 | -58.96706 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16a7e8bd-f8a6-3b37-a4bc-52811975335e | -7.63617 | -45.76956 | 2026-08-21 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0971fa25-a7d5-33c9-afd0-d27d531f587d | -8.49326 | -54.8835 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0492e70-3b06-3dd0-b083-ec1dbd49eb4e | -5.60398 | -44.00646 | 2026-08-21 04:46:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 8091d64d-5557-3e1b-a03d-f79bb0ef3b99 | -9.42104 | -60.41042 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 693ecf87-84ec-37b6-ac88-db1e63d15843 | -7.34085 | -55.68301 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3af2feca-1982-3e35-8606-8efef4d820b2 | -6.61549 | -56.34782 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57c4ddb0-7c2d-3688-8f10-d06a2c3139c8 | -6.16396 | -55.44642 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7cba8b60-09c1-316f-b218-fe32ce0ab2e4 | -10.76512 | -50.30667 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7557ae8c-1caa-3c2f-852d-0fa42f6479c4 | -6.20475 | -55.48773 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79fbbe63-7037-346d-a29b-bd2298b6322f | -9.20947 | -59.66058 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49e63bb6-61a5-31b8-b0df-b108faee6aae | -7.36675 | -45.80654 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 283bbb41-c9ff-3bac-ad43-5d65f2e4a377 | -7.02324 | -48.04329 | 2026-08-21 04:46:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4827259f-c563-354a-acca-0f6fc803254a | -6.94421 | -52.78951 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 466c2b2d-6304-36d1-a377-290ed5921939 | -5.60328 | -44.01124 | 2026-08-21 04:46:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| ad7e88b7-6106-31a9-9981-4d65b7a02d0c | -7.60059 | -60.95576 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93642299-0916-33e8-924f-533bfc2798f0 | -8.5473 | -55.30345 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c1670866-92ff-3e2b-ad1a-5c5c2e140eb7 | -4.39181 | -55.47258 | 2026-08-21 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f43943a0-9378-355d-a41b-e0502b2e1c34 | -8.45159 | -46.94717 | 2026-08-21 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a2c0e7f-43bf-3dd6-85fd-cbe103e89a4c | -6.42783 | -52.7229 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bae27be9-aadb-3da9-bdaa-9c35610aaa74 | -8.54286 | -55.30724 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b2838a6-d078-3319-9159-e03bab378341 | -6.71845 | -59.09812 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5c5b97b7-0c79-3f38-8699-cd1e859fc643 | -10.75729 | -50.33595 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97b89e43-b743-3dbf-8a7f-b1424517d85f | -7.77794 | -46.04088 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 41463a9f-4518-39e4-8fa4-ff21c73bef0d | -8.44624 | -46.95664 | 2026-08-21 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a609c85-fa6a-3fab-a2af-c71e76007f41 | -10.80084 | -50.27781 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a6bf6b9e-66ae-3165-b44c-4c592c4f14c7 | -7.34694 | -55.694 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18ce9b7d-8f7f-3117-a88b-111283d091ee | -6.6065 | -58.38901 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c9056571-001b-349d-8408-84c75f054a8d | -10.76116 | -50.30987 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed53fe79-157c-3a44-b73f-9983dbf4ff49 | -8.16142 | -46.73361 | 2026-08-21 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d4c0a241-ba45-357b-9aac-6cfd5ae90e85 | -7.22436 | -51.68372 | 2026-08-21 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72498226-0c18-3d99-a5b7-1daa1aa72937 | -9.40077 | -60.41789 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| afb28802-e031-3857-a921-8e9da31337e7 | -6.86702 | -59.4384 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35758175-4013-39e0-840e-493afddb428d | -6.71936 | -59.09272 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 27771248-c35c-3795-83c5-2578d91074d4 | -6.82839 | -59.39509 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ba377f46-3f60-31f8-a3b6-bd8326fad8b7 | -6.82241 | -59.4001 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 3d2bd999-ef4c-38f6-9f74-17e0f3bc1f6e | -10.2625 | -50.29252 | 2026-08-21 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a36cbcb7-e622-32ab-8d01-d1f0db5088ce | -8.09494 | -51.66243 | 2026-08-21 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48d60de0-48ca-334f-9a53-6e8b234b30e5 | -9.05443 | -50.88867 | 2026-08-21 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1eda2bf0-c981-3dc0-a214-754926116cb0 | -9.41736 | -60.54537 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f858804-0e82-3ef2-956a-0d3973700370 | -9.45419 | -51.60108 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 910a4c19-38a3-30eb-a39c-9788f4d84837 | -4.9161 | -56.26289 | 2026-08-21 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fa09cb24-61cf-318c-9fac-7a541c5ea873 | -6.57501 | -58.98241 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ae60474-9744-301e-9e0e-6bf8d49e2d56 | -6.90238 | -58.99604 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2aeab6d1-e1e6-340b-8c7c-a795174f1ded | -9.38945 | -60.55296 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c860df7f-6acc-3c92-bba1-2ea2fa0fb863 | -10.7606 | -50.3136 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 44200172-c528-35bf-ba96-1a7c671e675b | -6.64168 | -56.41637 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d749edb6-087e-3c20-9369-fd141e72e715 | -10.63603 | -51.60915 | 2026-08-21 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2ff8602-d0d4-3ded-9904-4cd4e22fcae2 | -8.65468 | -54.6271 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec66666b-becf-3545-8b69-cc92c82112a6 | -6.12902 | -59.90956 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0820c177-cbf6-3190-afe4-9315da9e2075 | -11.48834 | -45.11409 | 2026-08-21 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 22804711-f129-3a9b-a4d6-fdd29ca0ab80 | -6.22495 | -55.61409 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 06dbcd44-8de0-37a6-9853-14dfaa32bc67 | -8.10263 | -51.65654 | 2026-08-21 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0814c6b-2119-33ea-898d-28142d350615 | -8.05685 | -50.10834 | 2026-08-21 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aac4ccea-6d4e-307b-8701-898be35b81a0 | -7.55186 | -55.55748 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba4ad82b-4777-3239-8db8-62858d249d1c | -6.16998 | -52.4859 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e23cf296-0502-3be8-a77d-a554fccb7775 | -10.83409 | -51.00538 | 2026-08-21 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a0ff1ca-9033-35c6-b3e1-3764b39d9bdf | -5.13913 | -56.27928 | 2026-08-21 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41079912-1719-3791-a287-df64c6b1cbc4 | -9.99798 | -48.56203 | 2026-08-21 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e1d2a0d-27e8-3745-a161-905038109902 | -8.57819 | -54.78016 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6441ab72-2614-3459-b833-34fbbd2a8122 | -10.76798 | -50.31092 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8f655cf0-2138-388c-bc70-e581842f6883 | -9.20851 | -59.65661 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ff41136-f903-344b-a531-97057d507d6d | -8.38837 | -62.69755 | 2026-08-21 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 758c24d6-cea3-3d65-866e-8dd7594e39ca | -6.91928 | -59.34846 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10135713-acc8-3049-a6f5-b46ce4f5c617 | -9.40539 | -60.55281 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff7fbacf-df5b-372e-bc3b-8c07111dbd83 | -9.41086 | -60.40865 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 22.5 |
| daad156d-4220-37db-b1b4-a1f051e2eb71 | -9.39343 | -60.56014 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 537ee078-04e2-336e-bf62-2b1777c4950a | -10.72799 | -44.78295 | 2026-08-21 04:46:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3bae3564-05e7-30d4-a5ac-f3a6d159266f | -8.98818 | -50.72293 | 2026-08-21 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e038b3d6-790d-39d5-90af-bcf278fbc709 | -6.88579 | -56.43129 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7e0238c-d782-384c-b582-f6ec71a77d11 | -9.30592 | -56.81055 | 2026-08-21 04:46:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7700d86c-0046-34bf-9875-f70e51c9b4b1 | -8.33156 | -46.49903 | 2026-08-21 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9be8194e-e24f-3227-832b-c6c1754da282 | -9.55022 | -56.79907 | 2026-08-21 04:46:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4fd1a6fe-07a7-34da-b7a1-b1cca96e460d | -8.65582 | -54.63485 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1968215e-f483-3bd1-af82-c70c03a62403 | -6.36112 | -58.33249 | 2026-08-21 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cc45c1a4-30d4-304a-9736-d70c90e085d3 | -6.16862 | -55.44216 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 345548fd-48f7-39fa-b195-d99610c038c3 | -9.43361 | -48.25132 | 2026-08-21 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c3473ed5-4351-3a4b-8f72-59b0c2fefbb8 | -7.27614 | -47.45494 | 2026-08-21 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 024fa495-3788-38e8-a886-cb8dc0e51cff | -3.84749 | -49.04069 | 2026-08-21 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58596fd4-f9b9-3efc-9050-7bea0d1d0988 | -4.658 | -50.87072 | 2026-08-21 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6a69c17-d446-381b-905e-afb24ebe932f | -8.59696 | -54.71083 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e10b1fc-cc23-3c0a-8b12-f9d7dffbf049 | -9.43114 | -48.24864 | 2026-08-21 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 495b67a3-11d5-36db-a3bc-e110b53053be | -5.99704 | -57.8401 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2eb9fb3-8a34-386c-be2b-875819d981fe | -6.42091 | -56.18488 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5470d49-4324-370b-a5f0-a20c13a32262 | -6.25117 | -48.65799 | 2026-08-21 04:46:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc9b65e9-ce3e-3827-8a20-7a3d7162d7d8 | -7.77286 | -61.16555 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0538f1ba-3b74-30d6-9b1f-58ffd17c6fcf | -6.93975 | -52.77402 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5ac11a7-1da9-3a19-a1fa-a70c7871762e | -7.36039 | -45.82118 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b2e2a354-c440-3df4-b491-0bb85248641f | -6.34388 | -44.07705 | 2026-08-21 04:46:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b126060d-97b8-392d-a119-5fdc92885916 | -8.66687 | -54.59051 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README42.md)
