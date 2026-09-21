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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df5f5504-287a-3bca-b060-39b55e073cad | -13.33553 | -51.29706 | 2026-09-21 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d4047cf5-25e3-37b2-bb64-44a6d60e0eb4 | -11.65158 | -47.78522 | 2026-09-21 04:21:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1934763-af0f-36a9-8ebc-605522c02cfc | -15.46038 | -48.47728 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 787a389f-2eaf-34ff-97c8-51d8352ff8c5 | -9.98546 | -50.26592 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 512c3446-8fa1-3b8a-a2bd-d4808d79e3ae | -16.03197 | -52.52253 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e7cd0f9-d03c-3fc1-a920-e67c7a2bd7cc | -10.52629 | -57.45529 | 2026-09-21 04:21:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2687746-d109-3316-aebf-2e61f2821b38 | -14.60836 | -52.07183 | 2026-09-21 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| be16e3d9-1e33-377d-8478-c6311d6652ca | -15.45823 | -48.43542 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 56f5b193-207c-3c43-9668-aba0b273187f | -14.22653 | -44.62856 | 2026-09-21 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b84686de-d85c-322c-9424-6504c12392fe | -14.66733 | -54.47818 | 2026-09-21 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 993b8afb-aac9-3fb1-8c24-db3f8f087f1d | -10.58008 | -57.48481 | 2026-09-21 04:21:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0266cac-8108-3651-98ab-4ef17cc418c8 | -12.11831 | -47.03407 | 2026-09-21 04:21:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aacce9bd-5ce9-3454-b27d-b613d0c5c8c9 | -11.25204 | -54.14258 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e635753-5fa3-3127-aa2c-38e3ada047fb | -9.97253 | -50.26355 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1f47df2b-d5f0-3af8-bff3-8f17f21e8949 | -12.30009 | -50.73641 | 2026-09-21 04:21:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d305b869-e454-3bf9-adab-afd295a242b5 | -10.79543 | -50.749 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 036aa040-f8da-322b-bf53-17f5da918dc0 | -10.09017 | -46.10631 | 2026-09-21 04:21:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7cf62f7e-c9d4-34e7-919e-6c519671ed1a | -11.94067 | -46.50316 | 2026-09-21 04:21:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f303b43-bb1d-323f-b190-14e86b6526bb | -11.67533 | -43.42284 | 2026-09-21 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cc38181-1ead-3a4e-87be-3ec598cbe8f6 | -12.48415 | -44.7178 | 2026-09-21 04:21:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95561904-a041-33d0-aecf-4c4b34dc8bc1 | -11.85455 | -46.89436 | 2026-09-21 04:21:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2577ca39-d4d2-350d-bda6-01a8dbfbedf1 | -11.14122 | -42.79716 | 2026-09-21 04:21:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f3fa740e-4520-3a90-a976-f0999a474561 | -10.37473 | -50.22158 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5944c598-114c-3be4-a66f-19016aa431ee | -12.12246 | -47.03073 | 2026-09-21 04:21:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d2ae812-1d40-3c83-b40b-03cdee24bd4f | -10.89069 | -53.9823 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9827ab5d-f111-3dd5-9892-b1fc1f0e0968 | -10.46099 | -51.33031 | 2026-09-21 04:21:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82d82b1c-6a2b-3bc4-96d1-330b57e37a77 | -11.34048 | -43.37032 | 2026-09-21 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfc0edf6-9a5c-323d-912a-cf48e3851cf2 | -10.80062 | -50.84349 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4339535b-d23d-316b-83ec-967c92a7efde | -12.51316 | -49.80164 | 2026-09-21 04:21:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3797c41-bdc7-3d9e-93cf-551d5c0f29b6 | -11.80397 | -49.81145 | 2026-09-21 04:21:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| cd2a252b-e87f-389b-af84-9e7afdb92e00 | -10.47764 | -46.28962 | 2026-09-21 04:21:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6807d8e-4385-345a-9cee-3735504d5889 | -9.77057 | -46.06641 | 2026-09-21 04:21:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1a74b1d-11ee-32ed-9e3a-b8d34b0be354 | -10.8128 | -50.77924 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 96a8b471-6962-30a9-b57f-7b605607bf8e | -13.58986 | -51.46507 | 2026-09-21 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8237f73-02f4-373e-9301-c110d1b695ff | -10.82864 | -50.78989 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| db45e6c7-4b0b-33ee-861e-53f1fc9f0888 | -10.83093 | -50.15148 | 2026-09-21 04:21:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed3f15e6-1993-3ebd-9fb2-5bfb71e23c2e | -11.08018 | -54.02771 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6142d192-c19d-3216-98f5-a663b8cf2344 | -17.0236 | -47.13921 | 2026-09-21 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 09ad5623-d324-3fb7-8729-3462e18e02c7 | -14.75609 | -48.41973 | 2026-09-21 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16196624-f4e9-3208-a6bc-1c185cc2cc28 | -10.46796 | -50.29359 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b091fa3-cf99-39be-b7e2-1ec308a18ae5 | -15.44894 | -48.4468 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 81ae812e-226b-3e1c-ab3c-6d804e9bccdf | -12.54086 | -50.044 | 2026-09-21 04:21:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d97049f-34f2-3034-a162-8484aeace4df | -15.63302 | -52.6996 | 2026-09-21 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97fe3a38-a5c3-3c4b-8d28-304455cf1280 | -10.45369 | -50.27403 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 127e1d48-d7ec-37b0-9540-a231f7bde52e | -14.98079 | -43.08852 | 2026-09-21 04:21:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ce70aeb6-fc3b-30b5-90d1-eb3a508b720b | -10.10478 | -46.94799 | 2026-09-21 04:21:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a2a84203-2266-3f46-ae18-738f1ae857cb | -10.45154 | -50.28632 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4df2c6c1-9eb6-34f4-8f1e-7cfaf9c11b9b | -9.72611 | -48.15518 | 2026-09-21 04:21:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c74458c8-f2c7-3fe3-b362-84f3bacb3ee0 | -11.02183 | -48.32409 | 2026-09-21 04:21:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d326441d-a184-3620-8321-b4b19df15c7e | -10.47558 | -50.28997 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 88b7624d-d8ed-3cb4-897e-3a3172aee1ba | -10.87469 | -54.0944 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a1019df-1a57-3294-b8c5-804899986d6d | -8.1861 | -54.74314 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a44df39f-7e5d-3215-b36a-4266c0a23832 | -12.11765 | -47.03799 | 2026-09-21 04:21:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8cfa28f8-16d9-3f78-8a87-d3b5c0a6b3b5 | -10.57709 | -48.69552 | 2026-09-21 04:21:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90dc0223-1bae-3547-9fda-bd7ae168136b | -16.04003 | -52.52916 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d75262bd-6e1a-3785-b2e2-db0de04052e3 | -15.44822 | -48.47267 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50bc7466-bbde-3d54-b1db-ace648f2e17f | -10.4259 | -50.25623 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2e5ed518-823b-30d4-84e0-fd9716efeac9 | -14.76109 | -48.43372 | 2026-09-21 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 213f330d-35d8-3889-8d1d-defbe39c2b26 | -11.67589 | -43.41924 | 2026-09-21 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9cb683a2-ce5c-3a06-a968-4525c6581d67 | -11.11111 | -54.01965 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca1569e8-2314-31fc-81db-817da3456fb5 | -10.90905 | -53.97472 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57856c44-d280-3062-acd1-81cee46e366f | -11.43617 | -47.31246 | 2026-09-21 04:21:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5db37ea-6e39-3cf9-81a7-1fe78fff619b | -11.62624 | -47.7807 | 2026-09-21 04:21:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 26eca0cd-1282-3708-ab1b-5dcb4f88442a | -13.93683 | -47.84151 | 2026-09-21 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a93c7028-1b98-3e6a-a219-9ce51152a98b | -8.1786 | -54.78313 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b98db073-240d-33ec-aa12-a01efcc08b1b | -15.87936 | -49.92558 | 2026-09-21 04:21:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed9c62c6-b87e-3d7c-84e0-a75242b3ab29 | -13.5413 | -44.03823 | 2026-09-21 04:21:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 30c3a0f4-1ee6-3416-ba1d-475a419cdead | -11.74951 | -54.57029 | 2026-09-21 04:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c68794e-801e-377b-aa9f-e2540d25f7c0 | -11.33827 | -43.38464 | 2026-09-21 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b2979b4-4cc0-3a2b-b68a-8e8aee0be0f7 | -11.33105 | -51.3442 | 2026-09-21 04:21:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30afdcbd-b081-31af-a0a1-1768155a142b | -8.18099 | -54.73743 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87f03356-7d4e-32b7-87ff-d83b2c15ca7f | -13.58714 | -43.7192 | 2026-09-21 04:21:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a772330-ac2f-30ca-990a-d166e883d286 | -10.48497 | -50.98899 | 2026-09-21 04:21:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0e02237-f8ab-3622-b4e8-28e1bd52b9f8 | -11.87525 | -49.01115 | 2026-09-21 04:21:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9639ba7f-64ff-3530-95ba-b55e722adb7c | -14.19628 | -41.84651 | 2026-09-21 04:21:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 62c36d3e-5402-3a6a-9afb-1588fabac38b | -10.70045 | -50.77175 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cc8f6d2d-80ef-3a4f-8428-90d9e5d676b5 | -14.03425 | -52.07751 | 2026-09-21 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c12f3a7f-1d2a-33e1-881b-e8bf927e5ffc | -15.4618 | -48.43606 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 84eeea05-216e-380d-9438-2c83d10dbb94 | -15.61314 | -47.84339 | 2026-09-21 04:21:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6dddcc74-e215-31af-b2d0-ff99f9d6c90f | -12.18057 | -47.00427 | 2026-09-21 04:21:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d53f2b3-d9ac-38e6-9332-874b86beb759 | -15.46174 | -48.47993 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 621df09d-b912-36ba-82b1-0e12c28c93e4 | -12.10935 | -47.04466 | 2026-09-21 04:21:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a1288c8-f98b-34f5-b366-240e85c91048 | -9.74939 | -46.0667 | 2026-09-21 04:21:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7fc1cb7-e236-322b-b6ef-357c7edcf5f2 | -11.79337 | -46.84448 | 2026-09-21 04:21:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8699d0b1-b955-3bb1-b498-63dfbcbb34ae | -15.97544 | -50.10755 | 2026-09-21 04:21:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bb322f1-f2c1-3473-b49d-7f8a29c53865 | -13.17269 | -43.56853 | 2026-09-21 04:21:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 60a5cfab-5fb7-33b9-bb94-003029f15d44 | -16.105 | -49.81797 | 2026-09-21 04:21:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29cc286a-e8f2-3c90-a57d-9dbdcd33f2bb | -10.41813 | -51.86964 | 2026-09-21 04:21:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62e4333a-d314-3dbb-9c3f-1e2f6cd6827b | -13.8737 | -48.59509 | 2026-09-21 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a1e8947-b53b-3538-9ad5-95be8210f84e | -11.93787 | -46.49882 | 2026-09-21 04:21:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acadd467-9e28-3e86-bb65-56d351436cc6 | -9.94579 | -45.6833 | 2026-09-21 04:21:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbc5bc46-9614-3006-95af-c8e69d9c2a52 | -16.18613 | -51.12783 | 2026-09-21 04:21:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4e7b2b1-2d1f-356e-8ad6-225ded3fec68 | -15.97066 | -50.11184 | 2026-09-21 04:21:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74c744b5-a46e-3ac0-bd9d-42aff2824728 | -10.39961 | -50.23035 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 8a7dff63-3013-3343-b3fa-18927b06aca1 | -10.79916 | -50.83096 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3271fc8-fb5f-3860-aea1-0f6de3a1b8fb | -10.87073 | -57.16671 | 2026-09-21 04:21:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f417c8e3-d484-353a-a03f-57ab8d8f826b | -14.6628 | -54.47364 | 2026-09-21 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 663f81f3-7db2-30aa-990d-8f517e085b65 | -11.82403 | -46.82116 | 2026-09-21 04:21:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fbb73deb-ccab-3bab-a2fd-4dd834684b60 | -11.93446 | -46.49822 | 2026-09-21 04:21:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff523361-29be-3938-82fc-241a3184f484 | -15.86148 | -49.90436 | 2026-09-21 04:21:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README43.md)
