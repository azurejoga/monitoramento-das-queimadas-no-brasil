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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88c408cb-63a4-35d3-b5a4-60b3a119e991 | -10.8573 | -49.75042 | 2024-10-10 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ccd64f63-7848-38e6-b36e-3fc28c509e88 | -10.738 | -49.56168 | 2024-10-10 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1561a749-34cb-3a61-9b97-ce943d51af9a | -10.73421 | -49.56101 | 2024-10-10 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d21c93c2-0715-3aba-b22d-cc42baadb215 | -12.20366 | -50.61821 | 2024-10-10 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77a578c2-5034-3a4a-854c-03b3e130be78 | -12.19971 | -50.61749 | 2024-10-10 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5374728c-32e7-352d-8f54-dfd2e6ed3be3 | -12.19362 | -50.6058 | 2024-10-10 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8fb46123-90bf-35cc-b220-57c823e6a96c | -12.19272 | -50.61093 | 2024-10-10 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cad4ab4b-a393-33dd-8700-5734c825963b | -12.19058 | -50.59996 | 2024-10-10 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf729941-ea55-39c7-bda7-4c2a398eb8b3 | -12.18968 | -50.60509 | 2024-10-10 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a118f3d-a671-3654-85e9-ece1d8886f13 | -12.16772 | -49.68979 | 2024-10-10 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 26b95889-71e2-36f2-ba95-5db8f7545d80 | -12.16476 | -49.68453 | 2024-10-10 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2d74aa72-0b94-3e71-9e7f-5819882795f6 | -12.07631 | -50.81922 | 2024-10-10 04:19:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fbb74d25-74e3-3266-b192-a155537de396 | -12.07569 | -50.82276 | 2024-10-10 04:19:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fe54c239-ce17-3494-aad1-a80458236796 | -12.0723 | -50.81849 | 2024-10-10 04:19:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b91c2a3-8773-39c6-9b2f-472c74f6962e | -12.07168 | -50.82203 | 2024-10-10 04:19:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49ea0712-57a8-31c5-8555-68e6a3a5cbba | -11.95118 | -50.82241 | 2024-10-10 04:19:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b731b2b1-5c88-3630-bdd8-dec5c4cc97ab | -11.9444 | -50.81385 | 2024-10-10 04:19:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 614c1cda-6a90-3766-8ce7-82c2d6817df3 | -11.55636 | -49.9103 | 2024-10-10 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f35b3b21-5bec-3783-9f5a-79987c7787a9 | -11.55254 | -49.90962 | 2024-10-10 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54ee85df-edd5-3228-ae0b-8d0abac2af4a | -11.40184 | -50.03976 | 2024-10-10 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 346f2522-8069-38db-827f-602d58548d53 | -11.20713 | -49.92801 | 2024-10-10 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 581e110c-af04-3235-90a4-7c6a975f5dd5 | -11.20631 | -49.93285 | 2024-10-10 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 011cc506-557d-3b65-933f-4af9d04469d9 | -11.20439 | -49.92973 | 2024-10-10 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f41983e6-6402-3a62-b782-82bd6af799fe | -11.15386 | -49.73169 | 2024-10-10 04:19:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2573425-59b3-3d21-871f-7af52542ff9f | -11.11615 | -50.64238 | 2024-10-10 04:19:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14994110-33df-30a4-9723-33cfca2063ad | -10.86715 | -49.76197 | 2024-10-10 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f2e2f94b-f350-38e7-9b1c-f3562a25153d | -12.93698 | -51.13844 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cece39d1-984f-3c95-9d9d-a85714655510 | -12.93658 | -51.13862 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcf23128-dfda-37d5-ab76-4507331c2b46 | -12.80815 | -50.53453 | 2024-10-10 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbcc1198-1e46-323a-b05c-9332b3808594 | -13.70207 | -49.85612 | 2024-10-10 04:19:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3691d4e-1d77-364d-ac68-fcf408010677 | -2.15388 | -48.90867 | 2024-10-10 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46b1295a-4f8d-3c19-ab6f-2446aa96cb71 | -1.92846 | -48.94184 | 2024-10-10 04:19:00 | NPP-375D | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 079b29d0-cb01-3409-bd9c-88126f672b38 | -6.55854 | -49.88174 | 2024-10-10 04:19:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b61fb3d-d220-32e9-86ba-ba61eb59f10e | -6.5564 | -49.88147 | 2024-10-10 04:19:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0fcc04d8-485f-37d7-bf12-739a9075abe2 | -6.55577 | -49.88513 | 2024-10-10 04:19:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7563cf6b-5d7d-326b-9177-67c55c1ef676 | -6.1265 | -51.14495 | 2024-10-10 04:19:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59a26399-4664-31d7-a7dd-9593677eb008 | -6.12642 | -50.94696 | 2024-10-10 04:19:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3500f7df-c3b3-3f73-b413-ca2d00149203 | -6.12601 | -51.14268 | 2024-10-10 04:19:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd930ede-54cf-31fe-b6b7-f3dc6363c754 | -6.1257 | -50.95127 | 2024-10-10 04:19:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 686a3286-36d8-3ffb-8a52-c558403a389a | -6.12518 | -51.14768 | 2024-10-10 04:19:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7dad6321-fce1-3ec2-b719-1fcdfc9600cb | -6.55794 | -49.8854 | 2024-10-10 04:19:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 03ef6e9c-4f42-3c01-9f7e-032b87922154 | -6.31277 | -49.98561 | 2024-10-10 04:19:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac8ea8d6-6c17-34f2-a1cc-705d75cf2fcc | -6.31212 | -49.98956 | 2024-10-10 04:19:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a4b00f3c-5761-31f2-b96a-f8d89b9790af | -6.32161 | -49.98927 | 2024-10-10 04:19:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29f599b2-2e8b-3419-9b37-09be40f3d1be | -6.32056 | -49.9902 | 2024-10-10 04:19:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd7da2a9-3683-37b9-8bea-319e48bbffa7 | -6.3174 | -49.9889 | 2024-10-10 04:19:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf43edea-b001-3431-943f-b089bb636ca9 | -6.31699 | -49.98588 | 2024-10-10 04:19:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53d35404-6ab2-30cb-b800-fb6aabc32d88 | -6.31493 | -49.99849 | 2024-10-10 04:19:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfd5f9dd-35b4-34a9-959a-c0bdbdb98c9c | -6.31069 | -49.99829 | 2024-10-10 04:19:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 127d274d-492d-3751-a191-8d1e13e7bb58 | -6.20108 | -50.89922 | 2024-10-10 04:19:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92a0acc6-209e-374a-9ad1-6ffaebd9ff1b | -7.10342 | -51.11833 | 2024-10-10 04:19:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6266cbef-c7d2-366d-8836-32505494954a | -7.04002 | -50.31397 | 2024-10-10 04:19:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1da750d2-6a4b-3bd1-9dae-298a5ce19963 | -7.15194 | -50.64944 | 2024-10-10 04:19:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db9b6948-7312-3100-a9be-bdc16b24b478 | -7.10434 | -51.12012 | 2024-10-10 04:19:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6c7c0682-b338-3261-a337-881af5b7ddfd | -7.03935 | -50.31785 | 2024-10-10 04:19:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a4355bb-e42e-3d58-9514-6eef98426cd5 | -6.85825 | -51.08276 | 2024-10-10 04:19:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75bfb138-e1db-3c3d-b55c-09edcc2a9bc8 | -6.80062 | -49.94086 | 2024-10-10 04:19:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf4fa162-c5d4-35d8-bd8d-5f8651a802c6 | -6.8 | -49.94457 | 2024-10-10 04:19:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c70d2b12-0da0-3001-9852-f40d5fcb703b | -9.38159 | -50.75554 | 2024-10-10 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| caa5d4eb-1e9c-34d8-abde-c05e589fbaff | -9.37743 | -50.75477 | 2024-10-10 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf1b4fca-f87d-3057-ab41-c818c8ac0c20 | -9.24946 | -50.36489 | 2024-10-10 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c0338e2b-ddad-3743-91e8-b5de93ba950f | -9.18039 | -51.49856 | 2024-10-10 04:19:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 022b9761-7afc-336b-a0c3-4ef34f60f184 | -9.17743 | -51.51573 | 2024-10-10 04:19:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 27c3de7c-33c2-396c-8226-19f8dc3ea5d4 | -9.13931 | -51.50043 | 2024-10-10 04:19:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8237a045-f94e-3c97-9b97-27f9ad234b91 | -9.07927 | -51.46018 | 2024-10-10 04:19:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e011a669-e4a0-3339-8e11-edac5c267d2c | -9.03533 | -51.47858 | 2024-10-10 04:19:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99310b40-a929-3ec2-a133-acaff7f7bb2b | -9.03173 | -51.47326 | 2024-10-10 04:19:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 16d9c929-5aaa-3040-b456-f22f58b7d8a9 | -8.86393 | -50.77357 | 2024-10-10 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e3ed340-23a2-3a64-b2a5-ee5edb9aa784 | -8.77343 | -50.7227 | 2024-10-10 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c432d6de-777d-3aed-b31f-7b5e41578300 | -8.77056 | -50.71413 | 2024-10-10 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af526738-e6c1-36bb-9610-8c43861c2e39 | -8.57609 | -50.53579 | 2024-10-10 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75ae0f6f-25eb-3c52-b952-2b43868afadb | -8.56426 | -50.52978 | 2024-10-10 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b1dde23d-033f-3060-9af7-1f9ab4c6216c | -8.5601 | -50.52906 | 2024-10-10 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0604b0d-5144-336b-932b-d71f72db8eee | -8.50808 | -50.80697 | 2024-10-10 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2c402992-7779-35c7-8a3a-c13ab79df766 | -8.50413 | -50.98383 | 2024-10-10 04:19:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9063f943-3cd8-3231-8fb6-32d0d12b274a | -8.50387 | -50.80606 | 2024-10-10 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01a629fa-4669-3ecb-b8a7-48e5c5e4eb09 | -8.49964 | -50.80526 | 2024-10-10 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 314c8430-26ae-3215-957c-b8e8f4fb5e1c | -8.35357 | -50.82051 | 2024-10-10 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87ca942c-24a9-3f0d-9fa1-86e9edff995a | -8.34939 | -50.81939 | 2024-10-10 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbad9c3b-606f-30f2-bfb0-01a45365eb57 | -8.315 | -50.26071 | 2024-10-10 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c074470-269e-36b8-898e-5e9e1478fa07 | -8.22275 | -51.00164 | 2024-10-10 04:19:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ae15dbeb-47de-33a8-94a2-c9a55626be1b | -9.49816 | -50.98196 | 2024-10-10 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d33f4bf8-dab3-35fc-85fb-027c591c2d06 | -9.49802 | -50.98107 | 2024-10-10 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c1d7c6e0-32f6-3d36-ac7e-b5d15282ffaa | -9.49393 | -50.98129 | 2024-10-10 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5084afb3-2fa9-36bb-ae43-c2126fd234ab | -9.48904 | -50.98446 | 2024-10-10 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3cf69514-fd0e-333e-b6c4-81b41886077a | -10.85571 | -51.06225 | 2024-10-10 04:19:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d9ad687-a32b-3ec2-9b94-046aa93c13b5 | -10.85505 | -51.06605 | 2024-10-10 04:19:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bfd67263-0ad2-3d51-a13e-8d1e1804231c | -10.68086 | -51.09819 | 2024-10-10 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 410c9a30-3578-36ae-9b11-0f9dfb1f836a | -10.67669 | -51.09744 | 2024-10-10 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d5fa29a2-78b2-3bdd-a9ba-81cf9fe5fce6 | -10.67624 | -51.09754 | 2024-10-10 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 667fa65b-631a-3561-8624-01cda10c6b85 | -10.67252 | -51.09668 | 2024-10-10 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fb3e6c6b-ee9d-3a3a-89bf-7f14c4920d6a | -10.67207 | -51.09678 | 2024-10-10 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f3cc7a98-3039-3698-8a04-b3149daaa71b | -10.66835 | -51.09592 | 2024-10-10 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9a7d0a50-80bb-3253-b7c5-9575e6fb8fd3 | -10.6679 | -51.09602 | 2024-10-10 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| edb627c9-4cca-345f-a224-711d837577fa | -10.66766 | -51.09975 | 2024-10-10 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 14ccfa80-bcc9-3764-8d7c-42b1d40838fa | -10.66724 | -51.09985 | 2024-10-10 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 54afd5b6-b168-38b6-9d36-83a4b679569c | -10.55223 | -51.0636 | 2024-10-10 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b4f9317-a999-335f-92a3-ce43a423778b | -10.45017 | -51.88157 | 2024-10-10 04:19:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60a17230-ab60-3db6-875b-e2c6e144aefe | -10.44578 | -51.88071 | 2024-10-10 04:19:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c74814cb-4a28-3543-b00a-780e4f64c8d5 | -10.41861 | -50.72318 | 2024-10-10 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README79.md)
