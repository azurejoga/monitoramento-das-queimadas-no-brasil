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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb1d2e20-3321-3b42-a6fe-a4ab423cb20e | -10.85251 | -46.1855 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 134cd2ac-3ab6-3048-b4fe-7adf317c2277 | -9.13463 | -65.84505 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aefa7a3b-765e-335f-9f18-edf2385ec32d | -10.83983 | -46.20034 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1c210acc-a018-3514-8b31-66afbf9e4fcf | -10.09761 | -45.6133 | 2026-09-16 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 38bd22ec-e02d-3ed4-959a-a81b7cccd842 | -14.66606 | -48.01773 | 2026-09-16 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0479b4d1-c96c-3342-a7df-3e66443f803f | -7.65634 | -67.16698 | 2026-09-16 04:59:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ff8469e7-35e5-3dab-8c35-ce92b2cdaa8a | -9.80547 | -46.50233 | 2026-09-16 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 17543139-2c58-39cc-8594-e26346146a0d | -12.05898 | -63.37879 | 2026-09-16 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b9d3f4e-b223-36b6-a846-f677d4b99068 | -10.78056 | -46.20979 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca1144a6-3e8f-3e27-9fa0-46e975ad03a3 | -10.67304 | -54.13989 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d9f8ddc-a99a-325a-ab6f-8c5d1a9723bf | -11.16959 | -42.78983 | 2026-09-16 04:59:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 043912a7-1b05-3d23-8497-45a3673b9e71 | -10.46606 | -44.94841 | 2026-09-16 04:59:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4884fd9c-4495-3881-9631-54d494d63aa7 | -10.78141 | -46.20311 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 371afa69-4a57-3165-9ba6-48318e1f2f07 | -9.93835 | -53.98968 | 2026-09-16 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37bbdc4a-b3d0-3fe2-b8a2-baffea782613 | -7.64115 | -67.17584 | 2026-09-16 04:59:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b33f321c-b33a-3259-be63-f56fb70eaa41 | -8.37505 | -54.73273 | 2026-09-16 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db3f230e-d1ba-34f6-a865-ca212cf7290e | -10.76827 | -46.22149 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9cbc5e5c-4b89-36cc-974b-3e03dd56886e | -9.83667 | -57.70329 | 2026-09-16 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 604053ae-afd6-39cf-b95d-df5db518b35e | -13.39549 | -57.02337 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b89c149-6f71-319d-8100-218a89db20df | -8.54821 | -54.71441 | 2026-09-16 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39da3cf9-f18e-3568-97a6-be67b34a7397 | -10.95035 | -57.18609 | 2026-09-16 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5542dca0-695b-38ea-a259-b8543567aa99 | -7.64876 | -67.17135 | 2026-09-16 04:59:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6b5058aa-7cc4-30bc-ba83-72fe6fd9bf27 | -10.41767 | -48.65241 | 2026-09-16 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 90e75452-7e50-3579-8982-07e5f8cdf289 | -11.19513 | -55.03123 | 2026-09-16 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 889f98e6-faf3-334b-bdd2-77f0acbf0045 | -9.10508 | -65.92686 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dbe389e6-7f9f-37fb-bd30-59a7bd081dac | -10.89488 | -51.49554 | 2026-09-16 04:59:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97e124f7-9422-3107-9f18-4eb10063db08 | -11.89621 | -43.829 | 2026-09-16 04:59:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 25dd3a43-88c8-386b-9069-ec2eff98b52e | -10.70123 | -54.17396 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c319a517-1580-3f3b-b560-1ba468db05ea | -9.80116 | -46.49541 | 2026-09-16 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 1f8a045c-2710-3570-88df-d07a21e18d7e | -9.36071 | -56.93618 | 2026-09-16 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f1edc203-9da5-3460-adc5-3546f17a93e7 | -9.15959 | -49.99423 | 2026-09-16 04:59:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c4797e85-59d2-3ff2-bb03-2f37e46134fd | -11.19938 | -42.82325 | 2026-09-16 04:59:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| cc02068c-4161-342d-bba3-80a53676733d | -9.17295 | -65.60332 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99bfe4a7-708b-315c-aa5e-5e9ac6d9a484 | -9.13255 | -65.84734 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 477b4373-61ad-3817-87ad-5f56279db777 | -13.55935 | -43.53188 | 2026-09-16 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 82c81700-6e2f-3d91-9677-ef77b6372e74 | -8.58354 | -54.57416 | 2026-09-16 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9edaeda-2082-36b8-8d29-da95a2968ac6 | -12.11625 | -57.19147 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 437439d3-8bc7-3ea7-922f-f454c8383b17 | -8.65353 | -66.59052 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c188a7e-875e-3bb4-a2a7-38cce6895863 | -11.79116 | -46.58862 | 2026-09-16 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e995be14-51c9-39ba-b955-6f890b20b732 | -9.70606 | -52.02277 | 2026-09-16 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| eb13c1c7-f7f2-3544-968c-a7abd6410850 | -10.1026 | -45.61779 | 2026-09-16 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| c55459a0-3c05-384a-808b-bf4cc4e72035 | -9.17371 | -65.59914 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 535c8193-84d6-3c38-be86-85b3e4ffc9da | -11.19923 | -55.02874 | 2026-09-16 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d85502ec-8cd0-3eef-9b89-0ed0e3447076 | -7.64221 | -67.1702 | 2026-09-16 04:59:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 28c9821f-3c56-365c-a021-e5947ca44863 | -9.10255 | -65.94003 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 286e01d2-7299-3b80-8b46-5fa41a045bf2 | -13.75898 | -48.79776 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5419a931-06a7-34d6-9dd3-5edb2c454094 | -10.81152 | -46.17931 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4897f841-f69e-3d4c-b129-74d824267e99 | -9.78658 | -46.48699 | 2026-09-16 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31b3d0a8-87c6-3b64-9c13-5ce37ed0f9ff | -11.41454 | -51.42845 | 2026-09-16 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be339b42-30dd-37d9-930b-6384a3490894 | -9.57407 | -46.5902 | 2026-09-16 04:59:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 78742263-1f2b-3516-888a-3efd042ee4c9 | -10.87835 | -54.01656 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63b8edfc-e3ee-3df4-8c7d-d68e9fe31620 | -11.89325 | -50.05302 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| addf0850-6b5c-354e-80af-95a76a42571d | -8.53607 | -54.70539 | 2026-09-16 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67939946-53ba-3574-9885-346042a26bc9 | -8.83093 | -62.47914 | 2026-09-16 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1cc9a915-2b72-328d-91e2-1fd2481ecbb7 | -10.87016 | -50.81713 | 2026-09-16 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cf0df7ee-66fb-3ffe-aac7-70b63eb783c2 | -8.87899 | -62.51637 | 2026-09-16 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5fcc32ba-29b5-3459-a88c-4d7609ef88aa | -11.89678 | -43.82397 | 2026-09-16 04:59:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c1ef3190-ca63-36c2-86dd-306b93fe54fb | -11.23982 | -43.43478 | 2026-09-16 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 867b8142-0562-33f6-98c8-6c7bfbb37a90 | -9.70666 | -52.01862 | 2026-09-16 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1b54bc28-f766-36d0-bb0a-40139457263d | -14.66645 | -48.02384 | 2026-09-16 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2b7e8c04-7907-38a8-bfda-3c7c76bc0f72 | -14.86175 | -48.12595 | 2026-09-16 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb103582-9483-3984-89a0-52dc2eb74ec5 | -10.89962 | -54.01247 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f20aed09-a691-3b19-8d61-04b10fa37636 | -10.47415 | -57.91034 | 2026-09-16 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e19962b-d7d2-32c9-be2a-d60ff113e3c6 | -12.80755 | -60.49077 | 2026-09-16 04:59:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa37e130-59c2-33cf-bf3b-3cc871fdfdf1 | -15.25101 | -49.10881 | 2026-09-16 04:59:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 899c4c71-7b99-312e-8c91-f37d2f7a04f0 | -11.41833 | -51.42903 | 2026-09-16 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f3e079d-fbb4-3888-8d62-f5303e261b92 | -10.88226 | -54.01347 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df7e6591-a494-37c0-8cdc-0e77f826030d | -12.15498 | -48.94912 | 2026-09-16 04:59:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ced79306-717c-3d99-853a-458ebf5bda1c | -7.56116 | -62.32965 | 2026-09-16 04:59:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d777be8-d50f-3a20-b783-671eefd9d2cf | -11.26814 | -54.13179 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67889f16-3dea-3a40-a106-12806c664ac7 | -9.92399 | -60.46561 | 2026-09-16 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9af3660c-6d4f-3366-bb1d-fd2516ff6e16 | -12.77454 | -51.23127 | 2026-09-16 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| ca23ce11-1573-3391-af2f-0b0e834a11f1 | -11.19835 | -54.12503 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f437ce3-b8e5-3de7-a043-61c80838713a | -12.11566 | -57.19514 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a7bc6202-2153-3cf9-bb1a-3f7e89354abb | -11.41126 | -51.42512 | 2026-09-16 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2b058d30-f3c5-3ab8-9754-b5498b5d4243 | -13.38592 | -57.04023 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 491855c7-fcff-3b73-beda-32eecad28137 | -13.38926 | -57.04079 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d901116-13aa-3334-a6e3-5d2c70bf01a8 | -13.7596 | -48.79288 | 2026-09-16 04:59:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 26435b3e-9b12-3018-bce4-58af8f8929b8 | -13.38984 | -57.03719 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbcea31a-2269-3558-891c-ac5380192e3d | -8.36898 | -54.72823 | 2026-09-16 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ee9a96c-d370-3d15-8a30-0986e2b80b4b | -12.15402 | -47.99122 | 2026-09-16 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0453a45d-7da0-3e4d-9a63-def035f4152e | -8.64636 | -66.59434 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d0c90fa-f81d-3645-bd84-6ace2f9e462e | -9.79172 | -46.4877 | 2026-09-16 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59519cb2-a8b1-3cfe-af1e-8e28a61e566f | -9.80075 | -46.49855 | 2026-09-16 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 33.3 |
| b066effb-190f-394d-a5d8-e1d7436533a0 | -11.54332 | -46.85835 | 2026-09-16 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02c06f57-e59a-317d-a55e-1852c4a2f03c | -10.59838 | -47.75769 | 2026-09-16 04:59:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cf7473e3-0f66-3430-b552-a983139f2e7d | -11.1989 | -54.12141 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 65f90d0a-c7fe-3a5a-9c00-74a96eff7024 | -7.61314 | -67.25252 | 2026-09-16 04:59:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 693806b5-c8a5-3d04-af0b-36206c645977 | -12.11962 | -57.19203 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 460022fc-0bde-3961-8d1e-4ed529744fa1 | -11.98384 | -52.47181 | 2026-09-16 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7010d075-1cef-3d64-97f5-4039213ccfba | -12.77523 | -51.22624 | 2026-09-16 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| b3363058-5b5d-39a3-b6a6-29a6141c4c22 | -9.04088 | -65.92192 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e606a9b5-fe6f-3e3e-8625-4ec195a29100 | -12.62997 | -50.7677 | 2026-09-16 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 329b8df3-5b12-30bc-816a-ebfc8ec756b1 | -11.55274 | -46.86651 | 2026-09-16 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4b1e02e3-1572-3bb2-8920-fd78daf54c30 | -11.44927 | -49.76814 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02e03ece-63cf-38b0-b52a-7919f1a7f512 | -13.55933 | -43.53029 | 2026-09-16 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 12568832-a16f-3a9a-b2e7-3738d28be6cc | -9.04236 | -60.45874 | 2026-09-16 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1fe76a48-3f90-3c4c-9458-1f7aa563b876 | -10.41712 | -48.65656 | 2026-09-16 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bef29a36-e9c8-3799-9943-97802eef58ea | -11.34207 | -47.31892 | 2026-09-16 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b4929510-f8b7-3291-8a5d-48941370480c | -10.41262 | -48.65612 | 2026-09-16 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README47.md)
