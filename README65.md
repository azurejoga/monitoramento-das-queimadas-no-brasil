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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54bf2ee9-be64-3e4e-8c4f-0485c8499e55 | -7.6873 | -46.17285 | 2026-08-22 05:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f16ff1ca-381b-3ed2-ba12-0daa37612ae7 | -6.8585 | -57.68439 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ba9e2ec-b657-374c-a735-a5041931ee8a | -6.43036 | -54.9606 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 955d2789-6b6d-3243-8cc7-d2d9e9570e8a | -6.88721 | -56.43192 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c17c93a2-a9bd-3977-a2be-a2dfa868f985 | -8.62139 | -54.68501 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8e4f516-eef9-3292-93d3-e82e4c8c475a | -6.69582 | -58.94516 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0946567f-8e1c-36f5-b152-54c9a100fb18 | -8.59281 | -54.71301 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91f0b83c-35c0-3308-b226-ca34b4ccacb5 | -8.62089 | -54.68853 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c185de53-77bf-3a39-a91d-7ab0021f9cd8 | -6.64863 | -59.09375 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2215d4ad-edac-3768-bac4-c2621a63f94a | -2.89255 | -48.79989 | 2026-08-22 05:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d8e259e-4d60-37b7-b45d-2a7cd7eeb3a9 | -6.88082 | -59.40742 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d7f8cf9-ac10-3bff-b17a-92f7782fc43f | -7.60152 | -60.96037 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4173154f-af55-3c36-a859-8f6aed36aa60 | -6.88038 | -59.43224 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be6c75c7-c9f8-3058-a93c-4f5c2ffdc3c6 | -6.95084 | -59.30865 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f3e2104-b7bb-3359-a52d-f70e83b6a611 | -6.81092 | -59.65549 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ad33e65-9fb0-35a1-97d0-a0a2ae2b7d8a | -6.08655 | -59.95777 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3a23e61-2997-35cc-a582-8ca31d505ffc | -6.60675 | -58.38965 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54ba367a-32f8-3ef7-bb4a-009a93ee2195 | -5.74862 | -53.5903 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68f2051d-4848-3cbf-afa3-3bc21b41366c | -13.95329 | -53.85392 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3cf7fd4-b621-38f4-946a-feea82ae7a7d | -6.86649 | -59.41224 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 76aa1681-87b6-3071-9eae-68f1bccc79a4 | -6.8031 | -59.427 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 237cb3a0-328a-3655-a26a-a7d88f07d8c1 | -14.9725 | -52.65741 | 2026-08-22 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fec63b3f-a442-3b1b-8b48-97ed55732241 | -6.69494 | -59.10106 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e9f09d2-49b2-3512-a49c-032143b672ec | -6.13767 | -59.89406 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7abb3f05-47a3-3a5a-81bc-41fadb119dec | -6.37609 | -54.95732 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b032557a-aea7-39f8-9f90-6bef8afeb2e1 | -14.01379 | -53.70667 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 993af764-3365-3fcd-8f11-411797465000 | -6.79373 | -59.42197 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| bf1b92da-0335-3c3d-bc9a-600619beca87 | -6.82142 | -59.67494 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 30eaad58-f777-3bdf-b49a-4906a729168b | -6.76497 | -58.67876 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 326b2b16-d557-3206-97d9-cf15e4f46a81 | -6.80199 | -59.41263 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0e36f296-bf37-36e3-9a42-39a49af0235e | -6.81744 | -59.42218 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76c14b6e-6433-3fd8-aea9-f1d73aece119 | -6.38131 | -54.94844 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7656b8f4-1263-31de-a645-208710226358 | -13.99929 | -53.70961 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7d46e23a-f6af-36d3-880a-0353f542c31a | -6.8516 | -58.97011 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07c1eca7-839c-345c-9583-41feddb01326 | -6.36559 | -62.89748 | 2026-08-22 05:23:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c205d1ce-cb5a-3e85-bc41-cb5d906943cd | -6.73938 | -58.58195 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c624f866-9428-3182-a8dc-6ebab7dc0827 | -8.61833 | -54.7345 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48ba8f03-ad6f-34cf-8f65-fe281749b833 | -13.98499 | -53.67297 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0023246f-b8b6-3b0e-b555-0872de1c1b22 | -6.75277 | -59.46472 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72fdfedd-5248-323d-81cf-b7303d0f428c | -6.76661 | -58.66831 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c6997d3c-3667-35ed-8b7b-9d3c45e1fb88 | -7.13615 | -59.63953 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d305885-bfd4-3cc1-866d-66b596009da1 | -6.43383 | -52.71241 | 2026-08-22 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d57c1ecf-7517-3429-a6d9-a8a079214e44 | -12.55202 | -54.76781 | 2026-08-22 05:23:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b9b297a-8c59-3baa-ad45-7cd2241f2756 | -6.96374 | -59.05531 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a5edd24c-4ec6-3094-99eb-bcff18643310 | -7.36926 | -55.69204 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a4e2dc79-5a66-35df-9ea3-086449aa6220 | -6.13822 | -59.89056 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a54f7e9f-546a-3ba1-9b41-e38d221f8587 | -6.8108 | -59.39985 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1de71970-b0fd-345b-9f1c-1579ab65cbb4 | -7.44511 | -60.00326 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7d6258e-1e09-381d-912c-44218d4a2649 | -6.27282 | -62.52941 | 2026-08-22 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3ec9aaf-b4a8-3f18-a97f-ed3280065ca2 | -8.08805 | -51.66658 | 2026-08-22 05:23:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c699eb4f-19ea-383f-9714-63f1590db066 | -8.55371 | -54.85328 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1fe21293-8666-31c7-a166-ad86b74c9063 | -4.53342 | -56.12196 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c940bc09-6019-33f2-9843-73d709ef92d7 | -11.20304 | -55.06648 | 2026-08-22 05:23:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa05ddcb-880a-3a1f-8fb2-65093ea97152 | -6.81729 | -59.8918 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13c73316-414f-3c64-95d4-677732b2f3a3 | -8.54236 | -55.31042 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 030e3ccc-459d-36eb-92d0-ab708e5a073f | -7.50201 | -60.07329 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 54ff5ee0-7695-3868-a42a-89174a8c3b6b | -7.55031 | -55.56145 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d5075fb-b611-3dd3-b4b9-04e19d51179b | -7.04793 | -56.60981 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9bdb874-d0ed-3d17-9fbb-e3289ef63807 | -6.92332 | -59.35393 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2abd1f7-e3ba-33a1-b6e7-9102cd7fad45 | -8.15912 | -46.72287 | 2026-08-22 05:23:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a5cd4f09-544e-316d-a349-d99dd6d758a1 | -4.47 | -55.39705 | 2026-08-22 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdf3c3d8-acba-3890-bd1a-0c34b4288ff3 | -6.77434 | -58.6624 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fb7d3f6-505f-3243-b7da-2d531ec464ea | -6.8688 | -59.03318 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83b16ffd-bc32-33f9-80ed-5dbbdb974b7a | -6.67506 | -58.75365 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d696ec8f-eda3-3059-b28c-b6241f7cf718 | -14.31969 | -53.00863 | 2026-08-22 05:23:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99131162-ffc8-37ff-9a98-7d8dbc1ea871 | -6.3776 | -54.95491 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a98c94bc-3982-3206-9c93-885d6e4b651f | -6.81413 | -59.42165 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b2e31bd-ff69-3950-b24b-7fe2a7ee42ea | -6.86872 | -59.44098 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4e21ea2-1638-377d-bca1-7d97932f2dd8 | -7.01684 | -59.55722 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 893d5e76-a73d-34a7-a9a8-42837cb4b6bf | -11.17346 | -54.00879 | 2026-08-22 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa69f255-3280-3c1a-8b43-feb88452d2c9 | -6.65933 | -56.33727 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f704110-6f7c-3551-9df2-7ad4991894ba | -6.24862 | -55.42252 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 682df317-83ac-3ec8-8e5d-b99a359e448a | -6.76609 | -58.6932 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5149dcc-fc98-334d-aea5-7ddc50154f11 | -6.44162 | -60.07595 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8deaf8c-f7ac-39e2-aaa2-556abaf8ef7a | -13.45661 | -51.76442 | 2026-08-22 05:23:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f728f496-70ac-3aa7-8e5e-64709fb680a4 | -6.13544 | -59.90805 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52d039fa-9fb2-3293-8829-3b47c7bb169e | -8.64383 | -54.72778 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5e03420-2204-3cd4-926f-634e7a0b8a15 | -7.59651 | -60.94839 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c95b36c7-ea69-30ce-9f5d-aab76fac048c | -6.86432 | -59.44738 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da8812a6-c69a-3fa4-9f31-17f13bff0b1d | -6.85659 | -59.43195 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d426e142-cd09-3c18-a370-ff568cd11918 | -6.37365 | -54.94733 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 46f06469-eedf-3d14-bac3-f3d7f617eb07 | -7.55146 | -61.18503 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a0477c19-2dcf-33b4-bd30-9d5f1849d103 | -7.35107 | -55.67286 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46103514-18ba-33bd-a5b0-0e10a4c18e30 | -6.84887 | -59.43782 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54546d55-8f73-3f59-ace4-b70fd2ed4748 | -8.52586 | -54.8223 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e3dc0daa-fe43-337f-9878-e09c8b65e2ef | -6.77215 | -58.67632 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5669adad-2f8e-3620-8bc8-21869958667c | -6.12157 | -59.90943 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6bfd1a53-dd4c-3127-9b30-d5d866560042 | -8.15236 | -46.72212 | 2026-08-22 05:23:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6c59834d-c0a8-3f2a-858f-cc546ef1e7bd | -8.53252 | -55.32381 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21ddf058-d391-31e7-ac02-9e1598abe67f | -6.89593 | -55.71537 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d53aefb9-f2de-34db-8024-3036edf14805 | -6.37296 | -54.95203 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2e95781e-9d96-37d0-b305-d7e1ea4a8026 | -6.76181 | -59.15064 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 645fb8e7-0810-3b91-bc3b-9a58db5c9d4b | -7.01849 | -59.54683 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b52e9415-5ad3-3756-8a4a-082e399b9a71 | -6.53878 | -58.51868 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bc64565-f151-3b44-95db-a5ee1afd110f | -6.2721 | -62.5337 | 2026-08-22 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b103120-9970-320c-897e-14a75caa4e19 | -6.1421 | -59.90911 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e1ae526-456a-3a43-bd6e-089aa09239e7 | -6.78901 | -58.63258 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca97808e-9709-3be0-963d-56fb7072fd55 | -6.20465 | -55.63898 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0dad7833-24f4-342e-a80d-8e432bd987d6 | -6.88811 | -59.44766 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd5cd271-66dc-32d2-8774-4a89974a9a27 | -8.52417 | -54.80614 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |


[Clique aqui para ver as próximas entradas](README66.md)
