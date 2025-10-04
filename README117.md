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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60d3eb07-ae6b-3e1f-84bd-d3f0c253cd2d | -11.9241 | -46.36683 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0bda3084-5f61-307e-a3fb-1fb1d3fabf0b | -13.28939 | -47.84152 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3a38b673-3c47-3d4f-9682-f26b9b94de80 | -11.10701 | -47.74654 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f8ce47a6-b9dd-38c9-ab26-12893ccb4d50 | -13.33227 | -47.61856 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e4d337c7-3ccb-3de6-81e7-97a2ea56884c | -13.58603 | -48.17633 | 2025-10-04 05:06:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 07a53de9-4f5e-3aa9-abfa-3ae9656d95bf | -13.78083 | -47.81438 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a9dee796-b94b-3bb2-a2e0-98c5e8eddfe7 | -11.49988 | -46.75772 | 2025-10-04 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f12ae0e-7088-336f-a71a-c5a3a4732d88 | -11.54436 | -47.67057 | 2025-10-04 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d94041f9-77a7-3863-b119-a8e9ba1fb99a | -10.94144 | -47.43177 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2e10c23-2f12-3c48-b7c2-d35f6047414f | -15.60585 | -52.4699 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2297931c-fa4c-3607-b2ce-454cfd7aa752 | -14.9844 | -49.97285 | 2025-10-04 05:06:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 9a213f53-d3c0-39a9-a265-c41922fa6cb3 | -11.92425 | -55.90889 | 2025-10-04 05:06:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 650b41e6-3024-3193-9b11-10440f70ca32 | -15.58082 | -52.46924 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 79ee4a8c-305c-33ec-baef-4b6448dbde5e | -11.78306 | -46.81862 | 2025-10-04 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fee1baf6-4dbd-37e1-9b7c-9e45f040c5b2 | -11.50556 | -46.75857 | 2025-10-04 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 574fe7eb-005b-3c98-87a2-e31c81a2cda9 | -15.24614 | -56.76873 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e91b216a-f425-3e1f-aa59-1e61934af5b7 | -11.72277 | -44.44275 | 2025-10-04 05:06:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8883c21a-62db-3470-a467-106f8af9ad7b | -16.04629 | -50.93377 | 2025-10-04 05:06:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7ba889cd-f8e1-3657-9bfa-529fb793b758 | -15.18682 | -52.78022 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe2d4f4b-1201-3395-83f0-5a54894020ac | -13.1843 | -50.92732 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 451a247c-9a3d-3041-9a2f-7f367a86eb9c | -15.3835 | -47.96149 | 2025-10-04 05:06:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1d8e6016-064e-3277-877f-9b068cc13de5 | -15.98475 | -50.86602 | 2025-10-04 05:06:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a050fa73-1531-3255-8d11-988c9b1bdda9 | -14.88835 | -48.29255 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a4938047-7b82-31fa-b7e1-25350e13c922 | -10.41781 | -50.67188 | 2025-10-04 05:06:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4258b6c6-9a29-3ac1-9946-f7a0fc053160 | -14.20027 | -46.07322 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9d665bb2-3be8-3467-8a4c-795a94233818 | -13.39433 | -47.28385 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9a175248-9bd2-36a2-b372-1e78322ac0c1 | -12.79283 | -56.95967 | 2025-10-04 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cce997f-eba1-3b78-accd-8ae2bfa8a28c | -11.49999 | -43.49824 | 2025-10-04 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5ed085e1-d153-380a-9662-83af17c339f1 | -12.08148 | -45.18814 | 2025-10-04 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55352e3a-a581-3b48-b792-e86183a40e5f | -12.81765 | -46.85839 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| da3107a8-8562-363f-b906-a15b61f83511 | -15.20903 | -56.83329 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2ceeff0-41e1-3bab-baed-44616df75d1e | -13.33156 | -47.6246 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ccf0663c-da9c-3e34-885e-722834cfd2c0 | -14.46115 | -48.39781 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91373d65-eed2-372d-847a-13b8f5880ca1 | -12.87396 | -44.62982 | 2025-10-04 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b8bdf140-b42a-3b99-9677-f8694f5da9ad | -10.73645 | -56.59646 | 2025-10-04 05:06:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c049a140-e331-36ae-be98-2f035724e712 | -11.71412 | -51.46624 | 2025-10-04 05:06:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 30e1eb3a-c09c-37b3-a968-4dda657e459f | -14.20601 | -46.07789 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da29ddce-c5a2-347b-8937-882a383ffe38 | -11.44853 | -45.14032 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce2c4a69-d024-331b-8420-83c05699b5ee | -12.28008 | -55.13618 | 2025-10-04 05:06:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd702da1-723b-3332-9605-b46128029700 | -15.79894 | -46.25068 | 2025-10-04 05:06:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c480e56-77ff-39e6-aa9e-c594e40dc5a0 | -11.11611 | -47.88498 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4862f6c-9029-3d66-9653-3e3842ec5cc3 | -11.12133 | -47.88601 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61fff0e6-d4bf-3b51-aefe-b7f12f670c28 | -11.54573 | -47.65977 | 2025-10-04 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1916d1d5-5a78-3e84-90d8-329635b44c65 | -9.90706 | -63.50622 | 2025-10-04 05:06:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4943744a-b953-3985-be05-ce4f2a354fd0 | -16.09126 | -51.06559 | 2025-10-04 05:06:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ff57bca-6e61-351e-84da-f6d4936802fa | -13.30706 | -48.13528 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66e8bbcb-89b5-30e8-b93d-ab79421d96f5 | -12.90839 | -54.74429 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b12c14c-fd81-35fb-ab22-038a72643306 | -13.191 | -50.87708 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6eb901c4-b709-355e-9b0f-835885b1a7e0 | -14.6586 | -48.31425 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 933d0808-8744-3790-851c-78c4eaa1606c | -11.92457 | -46.37094 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 85952a9b-871a-3bed-9b5b-f50aa16b1295 | -14.93081 | -46.85796 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 33c11bd0-8886-30e7-973b-fbbc3d3df3ef | -9.45863 | -56.65479 | 2025-10-04 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 263ed14a-1e96-33b5-a203-2941f3c68929 | -13.11685 | -47.93501 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0b7318ff-dc14-3b48-b4b4-b8edea57d04a | -14.83806 | -48.37168 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d07178f-3051-347d-b26d-6bc8868bcfb0 | -11.56637 | -47.66915 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6c461a1a-bbdd-33f5-9d90-23eb9e3c1aa1 | -14.94684 | -46.8582 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b86b4958-80c3-3002-a2b0-1e771fb71aad | -11.91926 | -46.35689 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b135405-e7bf-3e0f-b8c6-3e3fe1324441 | -14.19452 | -46.06863 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f12f39a4-50ca-3e64-a182-1181cf21fa6f | -13.69401 | -47.35271 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a5cbcc5-26da-3b52-8ecb-331950730d6f | -11.56941 | -47.67136 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c13b0a76-85ca-3ad6-8cb0-fa252a4be694 | -13.3217 | -48.11788 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7d89eeb5-a251-32d5-a8a6-f303f6b5de71 | -12.65057 | -46.97647 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 65214251-cf65-3488-a64c-795b0c0bfc88 | -13.10867 | -47.84419 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 135a2be4-bc67-3d2f-bf1d-b4ee3b169b3d | -10.04857 | -54.33089 | 2025-10-04 05:06:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f57c7e7a-39a2-3359-b709-f28ce00d54ac | -16.37054 | -49.40343 | 2025-10-04 05:06:00 | NOAA-21 | BRAZABRANTES | GOIÁS | Brasil | 5203609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37164961-edac-3d39-8b25-7617bbe7bdf1 | -13.3325 | -48.07434 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| dec7b6b0-166e-30da-8084-568a7020205b | -10.56544 | -48.70242 | 2025-10-04 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 86a84edb-5809-30c1-96f3-8b7e0678de11 | -16.02622 | -50.94562 | 2025-10-04 05:06:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f6960b2b-7588-3b7b-baa3-bbdf8dd6fca8 | -13.65466 | -47.29596 | 2025-10-04 05:06:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e13fdab-1b5d-3c36-98ee-6438de247520 | -15.32706 | -46.3061 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 99d8ce2d-487e-38a1-bf4d-c57769a2b814 | -15.53409 | -46.82731 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0ed9fc08-7833-35c6-9bf3-084ccaefea0e | -11.56506 | -47.67935 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f719d189-a535-308f-a3cd-7eb8dcdc08ec | -15.34872 | -47.82312 | 2025-10-04 05:06:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ac2b436-1c20-37ce-9538-f7959fad3a2e | -12.8723 | -47.28968 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e417a846-9fb6-3a20-b213-013365489bab | -13.12144 | -47.94267 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 298ccf92-5ef4-3b9d-9194-f6704540a252 | -13.66078 | -47.29262 | 2025-10-04 05:06:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bea3969-b668-3a1e-ab46-b81054e4d0b5 | -14.21364 | -46.06468 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c559868f-db9a-3343-a6b2-d2eee0faff17 | -11.11235 | -47.74699 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 964305e0-c4ac-30b9-942e-3b2b901ddf81 | -13.26657 | -47.21981 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2b983f81-ddd6-36cf-8308-e79865ae2b04 | -13.17935 | -50.93108 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 162567ea-3b6e-355b-aad3-a124e75d417f | -11.92087 | -46.35226 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ee57a7e-4e38-3cea-8dba-2f2245137077 | -13.31681 | -48.11354 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1194a236-6536-3947-a1f6-7d00f179a4da | -15.73377 | -46.27565 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 34f36947-c22a-3962-805e-0ddf68a36c65 | -14.46643 | -48.39895 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7a6aca5-0f1a-3d6f-94a7-104cfec5c495 | -14.29728 | -53.26158 | 2025-10-04 05:06:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ef78712c-92a3-364f-9867-9f37fab6694a | -11.55967 | -47.67886 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 01c05918-a087-3d24-9e70-34962295b1b5 | -13.22089 | -47.84361 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7f03ba1f-2188-3396-94cb-fea11b8875f8 | -11.91418 | -46.2585 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de730ac7-c4be-301d-b138-2567a92fb3a6 | -13.69997 | -47.35061 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b1949e2b-2828-3f98-9f19-130ed4f90047 | -13.6282 | -48.6736 | 2025-10-04 05:06:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bafdc58a-4630-3992-a130-79c5b8b088df | -10.53055 | -54.47995 | 2025-10-04 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb9a454e-6611-3f71-8a59-25c97cf9f9e3 | -13.13485 | -47.82563 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4c92e23b-e6a2-34cf-ad6d-a5feacfd6077 | -15.58782 | -46.94344 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1c750662-1f1a-3dd6-a7d0-6237dc5904f3 | -10.58246 | -48.71168 | 2025-10-04 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3846dca1-ca3e-37ad-9942-6d315cd94124 | -13.171 | -50.89224 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b29e8e0-f622-365c-a928-3d27ac5450b1 | -14.60297 | -46.7255 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7dee996-1a78-316f-90a6-6c3e59da07fa | -14.75193 | -48.14623 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1771ec78-0118-389d-acba-e812e1614975 | -13.29755 | -47.81905 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 246ebe18-8157-35e6-966b-e56ac2afd88c | -14.22451 | -46.07973 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 67dc7d7b-e3c9-31ad-b53f-39329ca98663 | -12.20266 | -47.77757 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README118.md)
