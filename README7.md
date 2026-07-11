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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38f77e5d-f35d-3f5e-959b-cbe2cf3d7f7e | -14.74295 | -48.19544 | 2026-07-11 05:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c024eca-e194-3e08-9ce7-c77a0f2f070f | -13.76345 | -46.26406 | 2026-07-11 05:10:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de47ae56-83dc-3262-9352-c79d2ba57f31 | -15.6892 | -47.51425 | 2026-07-11 05:10:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6bfbb52-42aa-3823-9bf2-7b0a10168c63 | -13.25282 | -45.10093 | 2026-07-11 05:10:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e95761d5-513c-31af-a46a-545be67a9fd1 | -10.38877 | -49.58028 | 2026-07-11 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06401563-929b-3691-b697-2242f22a7bd3 | -12.6876 | -46.51274 | 2026-07-11 05:10:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74205a79-1867-3025-accc-e1223f881b57 | -13.3835 | -54.3544 | 2026-07-11 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 989cd659-78b0-391d-955e-383263ff0eff | -12.45668 | -49.5798 | 2026-07-11 05:10:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ff0f8809-168c-36e0-a35f-b5d96f75b25a | -8.73633 | -48.32801 | 2026-07-11 05:10:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 940d0aec-d94e-3d59-b33d-dbc414653d52 | -10.82613 | -49.37969 | 2026-07-11 05:10:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5c61c04-6bc7-35b4-9baf-45eb0e9c84b4 | -12.84828 | -44.36698 | 2026-07-11 05:10:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7fad9051-45d0-32e3-ad66-f3d20e6f52db | -13.25868 | -45.10749 | 2026-07-11 05:10:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97b04095-49ef-3340-86d4-4503b7225aa6 | -8.50188 | -48.0641 | 2026-07-11 05:10:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 430f8932-736b-3fd0-b8fa-afb677fd6f27 | -12.45601 | -49.58519 | 2026-07-11 05:10:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4cf2913e-dd62-3e94-a57a-e8e176c8d1cd | -13.39616 | -54.34339 | 2026-07-11 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c18b3b1-abf4-35ab-af4f-973ff43197a8 | -8.50691 | -48.0649 | 2026-07-11 05:10:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 208b596a-d620-3d37-ab0a-c763bc66db97 | -15.58876 | -46.81121 | 2026-07-11 05:10:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fdbd77e-4277-3f8c-aa72-3866f840054f | -12.85044 | -44.36742 | 2026-07-11 05:10:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e8d0d5ff-2ad6-387a-96e7-1c0058c4525f | -13.38288 | -54.35861 | 2026-07-11 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8510e8d6-f7d3-3d0a-b1dd-ac2be81cd1e2 | -10.0964 | -47.98301 | 2026-07-11 05:10:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9e550dd5-1f08-3187-bce6-ec22794a8b9f | -15.58926 | -46.80643 | 2026-07-11 05:10:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79a5cdf8-2d1b-3c57-991f-22003773671d | -10.12218 | -50.17248 | 2026-07-11 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aeb943f5-58ee-3456-a6fc-411d1352531d | -8.50148 | -48.06702 | 2026-07-11 05:10:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 195bb70f-58ac-35fb-a35c-f505bbaf972b | -8.89999 | -48.3288 | 2026-07-11 05:10:00 | NOAA-20 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 60560f0e-3d9f-3f22-9f83-ceb60513b2d7 | -12.82396 | -44.33918 | 2026-07-11 05:10:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 63f5db3e-ef45-3e7b-a3b0-5968c026415e | -13.2516 | -45.11203 | 2026-07-11 05:10:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4cb56062-7315-3711-b6cd-21ffff2f1e9d | -8.50651 | -48.06786 | 2026-07-11 05:10:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad06c6a4-a6b1-308f-ad7f-374ebc524015 | -12.45186 | -49.5792 | 2026-07-11 05:10:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f734a4c3-ea1e-39b6-919e-d1cb3829bdf5 | -13.76396 | -46.25952 | 2026-07-11 05:10:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0cd1e70-2e00-39eb-8939-0caec301092a | -10.7364 | -47.26909 | 2026-07-11 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1489f098-a54a-3d5e-837b-0e7184af267e | -9.57085 | -49.10232 | 2026-07-11 05:10:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58440eb9-6d0b-3f36-8706-b536ed0b75b7 | -10.09572 | -47.97907 | 2026-07-11 05:10:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0693eb52-506b-35f9-bda9-b116848b5af0 | -8.71973 | -47.84079 | 2026-07-11 05:10:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69f65617-91db-3000-b8f0-c9bebd605891 | -12.84432 | -44.3605 | 2026-07-11 05:10:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a3c0007c-2929-3e47-886c-442fa15816c0 | -13.96793 | -53.92528 | 2026-07-11 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 312e0e57-1f8d-3a3a-9ec1-bdd614a68b45 | -13.75771 | -46.26022 | 2026-07-11 05:10:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe741ca6-c5e4-3379-a994-e01fe5d1fadf | -13.32289 | -54.34097 | 2026-07-11 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7229a711-5f63-3f24-be6f-b74a62d06058 | -9.16298 | -50.89209 | 2026-07-11 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb0b9a8f-620f-3577-a016-a5be73e9c1de | -13.43721 | -43.84525 | 2026-07-11 05:10:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0ace171c-99f5-3ad3-9aa0-de46e2dfae50 | -13.25808 | -45.11293 | 2026-07-11 05:10:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a80c4c09-3f46-35e1-a0ca-9d9e1dd34a00 | -12.85108 | -44.36132 | 2026-07-11 05:10:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1ecd1ff9-6671-3ba3-9d41-37c1483b2771 | -8.72251 | -47.83976 | 2026-07-11 05:10:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c5ae694-9fbf-3aeb-a072-168f0a236636 | -12.45119 | -49.58455 | 2026-07-11 05:10:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9b636a1e-b676-3e7e-9b7c-5f433afc9a14 | -9.41584 | -48.214 | 2026-07-11 05:10:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27ab360f-55dd-3f59-bf6e-92aece75b648 | -10.73686 | -47.26545 | 2026-07-11 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71e5e20e-607f-342f-b17e-97a990312f54 | -12.68217 | -46.50787 | 2026-07-11 05:10:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7996afc-12d8-30db-90a1-2680b734e76c | -13.97534 | -53.92644 | 2026-07-11 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cc1ae6f-22c1-3161-9393-352a48709c5e | -10.40722 | -49.44541 | 2026-07-11 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 701c226f-300f-353c-a2e2-c2d7c7b8e2d4 | -10.11882 | -50.17475 | 2026-07-11 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bf8f7c80-7529-3325-9ec1-9887f35b3231 | -14.74191 | -48.20421 | 2026-07-11 05:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c67a9b29-4f38-38bb-b310-029cee386cee | -11.71108 | -47.80431 | 2026-07-11 05:10:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2cd39d0b-9d9e-3a8c-a6e0-9e6a9d82e880 | -12.68709 | -46.51704 | 2026-07-11 05:10:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b818d735-a213-3374-9a72-0cc27e70ff92 | -10.11771 | -50.17186 | 2026-07-11 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d47f2ae-7260-3bf6-a7f0-8d3342ed46af | -12.82463 | -44.33303 | 2026-07-11 05:10:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0af6eb85-1d80-3949-abd1-b8da1c463331 | -8.72208 | -47.84288 | 2026-07-11 05:10:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37f02025-6a8f-31b8-8e23-e99f6e60961e | -10.40249 | -49.44482 | 2026-07-11 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38eeb168-74cf-369b-bc7e-38205cdd9269 | -10.10047 | -47.98305 | 2026-07-11 05:10:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 561f75fc-190a-35f5-a1f8-31437beb8021 | -11.88252 | -47.65725 | 2026-07-11 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ab7e2e3-b5f7-3941-a5be-550400c22c6a | -9.22272 | -48.58011 | 2026-07-11 05:10:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a4d0cc9b-bff2-3166-8512-f678cf2e365d | -10.09683 | -47.97968 | 2026-07-11 05:10:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21b07293-0fd4-3ced-8a55-864f30d5cbc9 | -12.46163 | -49.58431 | 2026-07-11 05:10:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 39fdb74a-4e8b-3bb1-8c93-844c9c303e87 | -15.22768 | -52.68212 | 2026-07-11 05:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b239e72-424c-329f-944e-7d1ac20259b5 | -11.8771 | -47.65647 | 2026-07-11 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2726fec9-9c24-311b-8298-a1f1ac5498d6 | -12.68167 | -46.51214 | 2026-07-11 05:10:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 082becc6-2360-3cc0-9006-0685adf4bbd0 | -13.2522 | -45.10657 | 2026-07-11 05:10:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10218fa8-ca69-3ee7-904e-3d05cdc34c93 | -8.50731 | -48.06194 | 2026-07-11 05:10:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5271300-d4a3-3248-a53c-66e78716b854 | -10.37944 | -49.5789 | 2026-07-11 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 74cf6eac-bbb9-339d-b7a9-8f4b300201dd | -10.09724 | -47.97641 | 2026-07-11 05:10:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e93f8159-86b3-3c38-b217-e3c6de7129f1 | -10.41383 | -46.20026 | 2026-07-11 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ba3cefc-324b-3c7b-96b2-21a20c939bcc | -15.68417 | -47.5142 | 2026-07-11 05:10:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7fff2fcd-5978-39a5-9fd3-a4d4989a5f96 | -11.71064 | -47.80779 | 2026-07-11 05:10:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16c8843c-2940-3b5b-959c-e2dc5e86fb29 | -21.42524 | -47.0668 | 2026-07-11 05:12:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1bdaff98-590f-394c-b7cb-d4a2e9424ec7 | -21.12697 | -54.37521 | 2026-07-11 05:12:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11479f68-fca2-384e-99a3-d2df12b9eace | -20.15447 | -54.40374 | 2026-07-11 05:12:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dad61fd6-79d1-30ca-8e51-ade2c5ca7b07 | -18.02655 | -54.36758 | 2026-07-11 05:12:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98e2633c-0721-33f4-a6f8-16a845b4e1dd | -19.30179 | -47.44397 | 2026-07-11 05:12:00 | NOAA-20 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c7802e7-20be-36c6-9854-4c14b8acd118 | -22.91575 | -49.20642 | 2026-07-11 05:14:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab9684c9-35c2-3ecb-958a-49f136a3b1a5 | -21.97676 | -55.94174 | 2026-07-11 05:14:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b929b60e-acf8-3c55-b6ff-0e1ea6a3758a | -21.10075 | -57.46642 | 2026-07-11 05:14:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b28519a-9504-37d3-af3e-818424ce75c5 | -22.91886 | -49.20528 | 2026-07-11 05:14:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18134aa6-de6c-3442-af14-b030df6c347d | -22.38162 | -49.78889 | 2026-07-11 05:14:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5456baab-b73a-3518-92f9-19793999ae90 | -22.92175 | -49.20318 | 2026-07-11 05:14:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c283c429-3cff-34b2-94c1-1de3aa196158 | -22.91921 | -49.20123 | 2026-07-11 05:14:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 335af0b2-9b16-33cc-8011-f63481d73cc6 | -22.38129 | -49.79239 | 2026-07-11 05:14:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 808abcd6-52e6-3288-88ef-d37af7753105 | -21.09734 | -57.46584 | 2026-07-11 05:14:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5b300d9-24e4-3210-9fbb-e6099b10b4de | -22.37589 | -49.79177 | 2026-07-11 05:14:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0e3ab405-f373-3d4a-bae2-c649f44646d0 | -6.49272 | -42.20044 | 2026-07-11 05:38:00 | AQUA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 40.0 |
| 28770258-5e77-35e1-8596-da635de84a35 | -1.87737 | -54.68446 | 2026-07-11 05:55:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f46232b-7241-30b6-a394-402a1bcdceec | -4.19945 | -56.03725 | 2026-07-11 07:14:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 0fe572ec-3c3a-385f-94fe-6953ee41c2cc | -6.68583 | -63.80264 | 2026-07-11 07:16:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| a767a3dd-4493-3ca9-8037-93e907ddb343 | -6.99909 | -42.9002 | 2026-07-11 11:45:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 2e47b0ee-bc3c-3442-bd8e-e8574a2393b5 | -7.75333 | -44.83537 | 2026-07-11 11:45:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 5ea2378d-a797-3896-a255-704a4d07250f | -6.4878 | -42.22041 | 2026-07-11 11:45:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 2ad009a8-8e91-3da0-b9f2-688dc500ced1 | -7.91495 | -48.24529 | 2026-07-11 11:45:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9960d415-82a8-3d2c-be7a-c87ded18d9b4 | -6.49799 | -42.22765 | 2026-07-11 11:45:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| da924bca-a5fc-31c4-b6a4-64a97b22aac9 | -8.11526 | -47.57583 | 2026-07-11 11:45:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3dd649ef-f9ef-3868-af90-e1ee8fac48cf | -4.97716 | -37.93455 | 2026-07-11 11:45:00 | TERRA_M-M | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 4528d95c-0d4d-3b4e-9b08-696b31ec70ea | -6.49932 | -42.21044 | 2026-07-11 11:45:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 4d158ab4-f8b5-3ada-a2c2-3950e275d466 | -7.7546 | -44.82636 | 2026-07-11 11:45:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| dd7e5635-f7c1-3f2d-adeb-4219bdc4325f | -10.3663 | -46.17841 | 2026-07-11 11:45:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |


[Clique aqui para ver as próximas entradas](README8.md)
