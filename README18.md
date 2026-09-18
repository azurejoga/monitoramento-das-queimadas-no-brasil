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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d85331b4-5815-317d-b34a-4d94c24c2aba | -7.8048 | -44.917 | 2026-09-18 01:02:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f7638eb1-7ea2-31be-8363-318fb498117a | -4.5373 | -54.926601 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5a3cee7-31a0-3a61-8c26-bf29f7e9595c | -4.4942 | -55.5037 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d90df38-6485-3bd2-b45c-7349e54ba46f | -8.4495 | -45.712601 | 2026-09-18 01:02:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e5c9752a-4e1b-35fa-9f07-178faaf8cd6b | -8.9451 | -51.460201 | 2026-09-18 01:02:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d4e0197-0bea-3c3e-b07f-010fd7f30bd3 | -9.9447 | -46.608601 | 2026-09-18 01:02:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9906e59b-d52c-3acc-a124-421d3cd89fd8 | -8.9469 | -51.467999 | 2026-09-18 01:02:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 036a2e8c-9fff-3660-83ce-a2820d9d27f4 | -12.45 | -50.681599 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9fc4ca47-d71d-384a-9082-0bdc3549f0da | -13.7681 | -48.042099 | 2026-09-18 01:02:00 | METOP-C | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7ae598ec-252e-3807-aa92-56bad21d5bf7 | -4.5587 | -42.9523 | 2026-09-18 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 251.9 |
| 03ab002e-3720-3149-a38e-5e7bdf40f4e7 | -3.4455 | -58.2134 | 2026-09-18 01:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 3da0b1ee-e267-370a-8f87-0933f829b379 | -4.5774 | -42.9512 | 2026-09-18 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 614.0 |
| 1c624186-9a51-3a10-812f-7972ea6f2035 | -2.8285 | -50.4653 | 2026-09-18 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| c3eb38b6-615e-3aab-b016-99822c4bfe5a | -12.6239 | -50.8739 | 2026-09-18 01:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 1bba39dd-d5e7-373a-b30d-5161c2447050 | -9.699 | -54.8176 | 2026-09-18 01:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| cbcdb43d-8c78-3b40-92da-121bedb5cce1 | -4.5961 | -42.95 | 2026-09-18 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 205.6 |
| c6920106-f72b-336a-9a99-24401f5d609f | -2.81 | -50.4868 | 2026-09-18 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 4c7d5429-0cfe-352d-b10f-a420b916ec81 | -5.7615 | -57.5807 | 2026-09-18 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| e2d73f09-ec4f-3530-bb3a-1231820836dd | -11.2979 | -43.3614 | 2026-09-18 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 473.9 |
| 6f1e72e3-ad68-3bd8-8918-0671f395a3fb | -9.7177 | -54.8162 | 2026-09-18 01:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 121.4 |
| ceb6e717-e07f-3ef6-9eec-986f8e9b17bb | -12.643 | -50.8716 | 2026-09-18 01:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 0005b21f-3351-375f-a854-4a44bdf079fe | -3.3823 | -50.4486 | 2026-09-18 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| a7f2f846-64e7-3476-a27e-fbdf09ee8209 | -6.3656 | -58.2966 | 2026-09-18 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 1ccc7e47-17c8-366a-b723-3acba3e884b0 | -19.1812 | -48.7717 | 2026-09-18 01:10:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 5ee40884-c844-3b1f-86b2-eaef5e4ec9f9 | -3.3638 | -50.4492 | 2026-09-18 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| ff974d23-8d8e-3d87-8c9b-22337a2fe076 | -2.8284 | -50.4863 | 2026-09-18 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 40fcef81-937a-350f-ba8f-014298509a60 | -4.5772 | -42.9746 | 2026-09-18 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 273.2 |
| a6abae59-6678-32cf-9665-e3938071cd39 | -4.5585 | -42.9758 | 2026-09-18 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 186685b4-66b9-3c48-81b9-37fbacff5c79 | -4.5776 | -42.9277 | 2026-09-18 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| ab590c1c-b3ce-30c0-8abb-4659bd83aeb6 | -11.2975 | -43.3851 | 2026-09-18 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 1a7d6727-eb3c-3393-8c11-583c71030709 | -9.7179 | -54.796 | 2026-09-18 01:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| e6a93273-4b56-3808-b2b7-bcf5b1f6c31b | -12.4359 | -50.6827 | 2026-09-18 01:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 190.0 |
| 4f61be4b-fa40-3088-b3d5-f44c6cfc55d1 | -2.8101 | -50.4658 | 2026-09-18 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 04545944-d581-3994-885a-d859ae4fd6be | -11.2787 | -43.3643 | 2026-09-18 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 580.9 |
| 2e3f1d4e-d2e4-30b8-970e-4ec08a4e42cf | -3.0465 | -51.3755 | 2026-09-18 01:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| c80e97d9-8a32-32b9-b232-6c07e1d82d13 | -19.1806 | -48.7946 | 2026-09-18 01:10:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 58b7579b-bc33-3cd0-beeb-460fe8b7c2c6 | -5.7569 | -45.084 | 2026-09-18 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 73b3b808-1265-31b4-b05e-7f5343a37dbc | -5.7567 | -45.1067 | 2026-09-18 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| dcd070e0-1620-37b9-94f1-413a40af9043 | -11.2791 | -43.3405 | 2026-09-18 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 125.2 |
| 65ad3d90-d8c1-3591-881f-e8fc128e7358 | -11.2783 | -43.388 | 2026-09-18 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 14ce8ebb-276d-3694-80fa-f16536f3bc8a | -5.7429 | -57.6009 | 2026-09-18 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 9f2ecd2f-2a9b-3b01-aeca-94f2ecdc2d71 | -12.6427 | -50.893 | 2026-09-18 01:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 147.5 |
| a749d712-477e-34eb-b1f6-5b67c49b5cc3 | -12.4551 | -50.6804 | 2026-09-18 01:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 188.5 |
| 76b0a9db-ea49-3ed9-9627-80ce03cdefb5 | -5.7431 | -57.5814 | 2026-09-18 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 3c859636-c12a-34f0-8ea8-f4806545f589 | -12.6235 | -50.8953 | 2026-09-18 01:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 189.0 |
| 7b9eb9d9-267f-3760-922f-dbc454f61a5a | -11.2983 | -43.3376 | 2026-09-18 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 7c3526f4-dbb6-386e-9c28-dbf7cb30fb43 | -4.596 | -42.9734 | 2026-09-18 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 061ae665-b13b-3494-8073-c8982f9a49e4 | -12.33 | -50.69 | 2026-09-18 01:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 60f2a01a-a1b4-328a-a2ce-c48ea180df99 | -4.58 | -42.97 | 2026-09-18 01:15:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d161125c-ea30-3da2-969d-caa11ab867cd | -11.3 | -43.36 | 2026-09-18 01:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 93217170-f71d-3f23-9efd-379ce8a89ac8 | -12.3 | -50.73 | 2026-09-18 01:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b8bac716-cf87-3033-af8b-602e2aa5bdf7 | -11.3 | -43.41 | 2026-09-18 01:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 51ae6cc9-3fb2-38ae-af1f-bf5f3e4fd4e7 | -12.33 | -50.74 | 2026-09-18 01:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9dd71cbb-5c6e-30b6-9ad3-9db9c47e1778 | -11.27 | -43.4 | 2026-09-18 01:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 23c1cbd3-ab38-3bbd-9604-241c42b913bf | -12.36 | -50.7 | 2026-09-18 01:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 40dc726f-a356-34a5-a544-039bb2e17b2c | -4.55 | -42.93 | 2026-09-18 01:15:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cb229f7e-89c8-3a58-ae21-d48662f18911 | -12.42 | -50.66 | 2026-09-18 01:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0f6e0628-0281-3bba-aba4-807cd692f20d | -4.55 | -42.97 | 2026-09-18 01:15:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c647746-7ed4-328d-8f9c-6e04be9c6085 | -11.27 | -43.35 | 2026-09-18 01:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0e0306fb-e4f5-3abd-a5ed-d918bb029ff3 | -4.58 | -42.93 | 2026-09-18 01:15:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 479a978d-c908-3579-8db7-17a1c997b2fb | -19.5539 | -47.6346 | 2026-09-18 01:20:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 010b8364-6ee9-3789-981d-4c338cea31f8 | -2.8285 | -50.4653 | 2026-09-18 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 14cfcf11-1f77-3490-90b5-727e4872471b | -4.5774 | -42.9512 | 2026-09-18 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 599.0 |
| 1665e039-f4f7-3c8d-b850-4e779f0e66c5 | -4.5587 | -42.9523 | 2026-09-18 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 223.3 |
| 643a1db8-7557-3def-9a5f-cfc3feeb8bdc | -5.7431 | -57.5814 | 2026-09-18 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| be6dcd49-6da4-3fd9-9ac7-d9388279fb8b | -3.4455 | -58.2134 | 2026-09-18 01:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 13190bfa-a024-3353-a9c7-e032f851108d | -12.3782 | -50.7111 | 2026-09-18 01:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 2e46407a-377e-3764-88ce-1cc5f0a8aedd | -3.3823 | -50.4486 | 2026-09-18 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| bd03831e-9463-3de2-9de2-5f9acfb889ed | -3.0465 | -51.3755 | 2026-09-18 01:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| edded929-3315-34b6-8bdb-0c88fcb403dd | -9.7177 | -54.8162 | 2026-09-18 01:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| a241d125-49c0-3540-abff-b419d049f0aa | -4.5585 | -42.9758 | 2026-09-18 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| d1eebc89-d406-30ac-8992-c3dcef95f841 | -12.6239 | -50.8739 | 2026-09-18 01:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 112.1 |
| d63ffcdb-2c98-3106-a71e-5001b35e8b91 | -5.7382 | -45.0853 | 2026-09-18 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 36.0 |
| ca690fdc-8043-31ec-a768-1067eee68c06 | -5.7429 | -57.6009 | 2026-09-18 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 5d4e1b67-8ece-3a2b-93b0-9377b711155f | -4.5961 | -42.95 | 2026-09-18 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 213.3 |
| 60328f32-5101-3994-87a1-4bca93dd1ee6 | -9.7179 | -54.796 | 2026-09-18 01:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| b5ef64a0-f042-3dc9-b0f7-27692130b5df | -12.3977 | -50.6873 | 2026-09-18 01:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 004a5efa-aeb0-3823-9b46-78b61aa98d65 | -5.7567 | -45.1067 | 2026-09-18 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 972dbd86-27ff-3670-a524-6a13e8786416 | -6.1358 | -59.9638 | 2026-09-18 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 1cafcb4b-35f2-3f78-be1b-992a726a8a8d | -12.3974 | -50.7088 | 2026-09-18 01:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| e65319cc-9068-354b-930f-5bcf311e3fbd | -9.699 | -54.8176 | 2026-09-18 01:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| b2d02471-322b-325f-9fb1-9889dfb4c4e1 | -6.1359 | -59.9446 | 2026-09-18 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| e2738f17-3746-3bd0-98a1-ee1c1f67ba40 | -3.3638 | -50.4492 | 2026-09-18 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| cec361c9-5974-3011-97d0-b14f7aa9b5ed | -4.5776 | -42.9277 | 2026-09-18 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| eb9fab81-f600-3b9e-ba88-a20c97f72544 | -4.596 | -42.9734 | 2026-09-18 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 2ab8f7c2-f6ae-31bd-89f2-07523ed4474d | -2.8284 | -50.4863 | 2026-09-18 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.6 |
| a7298abe-42f5-329b-9240-d1f02bd3ba73 | -2.81 | -50.4868 | 2026-09-18 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 83190316-c891-3556-87ae-9bcc5bc2c2d8 | -12.6235 | -50.8953 | 2026-09-18 01:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 86c0838c-bf3f-3362-890c-755d5ef537ff | -4.5772 | -42.9746 | 2026-09-18 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 180.4 |
| 2c92b56e-1338-3352-b331-248f54320ccd | -5.7615 | -57.5807 | 2026-09-18 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| bfdbc1f0-ba0c-3181-8364-39ecc84a4609 | -5.7569 | -45.084 | 2026-09-18 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 3d7f3a97-c269-343e-ad4b-b3d5d986c791 | -12.3786 | -50.6897 | 2026-09-18 01:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| c2fb09fd-1940-36e5-a4a9-5c41692c8497 | -19.1812 | -48.7717 | 2026-09-18 01:20:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 9acc6be8-cd4b-3fcc-8178-6cafd13e2545 | -2.8101 | -50.4658 | 2026-09-18 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 639f3c1d-e19e-3cd3-8abd-13507dbfcb43 | -4.5774 | -42.9512 | 2026-09-18 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 383.2 |
| b10747d9-b5bf-3b01-b8b1-a6ea09091576 | -11.064 | -48.2898 | 2026-09-18 01:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 44d7ef0f-fd73-30cd-9c39-27edbfae50bf | -6.1359 | -59.9446 | 2026-09-18 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 88a6ef1a-4e72-302c-846e-30d8fffc273e | -3.0465 | -51.3755 | 2026-09-18 01:30:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 00af2c7b-5c1a-3100-a605-0e26e2e83459 | -9.699 | -54.8176 | 2026-09-18 01:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 328ad723-e8f6-3d4b-95aa-73c4a5412c7f | -6.1358 | -59.9638 | 2026-09-18 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |


[Clique aqui para ver as próximas entradas](README19.md)
