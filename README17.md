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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f36ddb37-d65e-337a-95b6-2950335599cb | -13.04095 | -48.82904 | 2025-06-25 05:25:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 461b02b6-2133-3af0-aa1a-cdd394ddd20a | -10.06243 | -51.11443 | 2025-06-25 05:25:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e62c7b5-cb3a-3e89-9ccd-27809cd6078e | -14.71564 | -48.40971 | 2025-06-25 05:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9dc49eea-f44f-3277-965a-e9624e6cf995 | -11.18784 | -48.61939 | 2025-06-25 05:25:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cba56b66-e8d7-3a75-b109-8dda861548b7 | -8.67548 | -51.46886 | 2025-06-25 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2421bf5-3bd5-3dae-bfca-2bd23b320151 | -9.50805 | -56.10656 | 2025-06-25 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ed72c48-5bb1-3b4b-8935-ca23e034ab53 | -9.57467 | -49.11388 | 2025-06-25 05:25:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| df580ce8-9b87-3f8c-8556-71a1bae5b6d3 | -11.94189 | -48.42927 | 2025-06-25 05:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7af1dc9-1737-3f1c-936c-bd5f99a14319 | -9.92435 | -52.4314 | 2025-06-25 05:25:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1c565bb-e974-3fa1-86a3-2256ae30f389 | -8.4814 | -50.27969 | 2025-06-25 05:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 64b3981d-d7b7-37cf-90c6-616db18b3202 | -8.67116 | -51.4664 | 2025-06-25 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0182ebf-f162-33dd-94b8-9306f8000960 | -8.9828 | -49.86727 | 2025-06-25 05:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ac2e753-111d-3d5a-b027-5f751343f3b2 | -2.90907 | -54.48496 | 2025-06-25 05:25:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04f3896f-920a-356e-9bbc-fb30b7c31dd8 | -9.92479 | -52.42813 | 2025-06-25 05:25:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 015f919e-d44a-3c2a-b5d0-0da8fedd2a69 | -12.80099 | -48.73546 | 2025-06-25 05:25:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b38816ba-aea0-39cd-9a63-c20515506f12 | -10.23755 | -56.76587 | 2025-06-25 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfa6441d-f626-3b57-baa3-586a8899e8e2 | -9.51213 | -56.10718 | 2025-06-25 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9454e78d-b39a-3994-a801-b827ebe29bd3 | -14.80694 | -48.29358 | 2025-06-25 05:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 63cdfd48-7f49-3253-8ffb-8653d11551d0 | -9.38117 | -57.55757 | 2025-06-25 05:25:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a94fa93c-db3b-3d9a-b28e-eaac42beecc4 | -9.17355 | -61.40598 | 2025-06-25 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44ee6311-5840-314c-bd38-0b5176f28804 | -10.29987 | -57.13778 | 2025-06-25 05:25:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69ff4ecb-ebf3-3019-b962-059c2ace2ffe | -11.57461 | -47.42845 | 2025-06-25 05:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0719dbd6-73c8-3bdc-a61e-5d9b2b9e0681 | -12.80035 | -48.73359 | 2025-06-25 05:25:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2fdc8991-c47d-391f-9675-054a7a8480d0 | -13.04029 | -48.83533 | 2025-06-25 05:25:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 26200d2a-f802-3c73-90e1-eea207844e84 | -9.50857 | -56.10295 | 2025-06-25 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e06245a5-bd61-379e-9d96-0b6fa39eb3ee | -13.64419 | -53.9379 | 2025-06-25 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4286b69f-64bd-3cf6-b166-9117fe20d3f3 | -10.36314 | -57.25761 | 2025-06-25 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d93cc49e-58b1-315d-b49f-0b0155093d38 | -9.85269 | -55.16131 | 2025-06-25 05:25:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ee414ff4-2dc6-36fc-9701-509d6093c8a1 | -7.89264 | -61.4738 | 2025-06-25 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e9bf59a-a553-32e2-af89-83eda416856b | -8.48083 | -50.28397 | 2025-06-25 05:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 440df452-6d8c-3c42-8118-bbd2b8a74d8d | -13.2933 | -57.07966 | 2025-06-25 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3195c0aa-d56c-3fb5-b652-f450c097d28f | -10.86956 | -54.31926 | 2025-06-25 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f93e3003-97f7-303e-aa23-39f8aefead4b | -3.61899 | -47.53693 | 2025-06-25 05:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8d8c907-3fd2-31bc-8e47-654e478eb03e | -12.2816 | -57.27081 | 2025-06-25 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee1bc67a-63b5-3df6-b52e-6648dd8e34c0 | -10.44026 | -47.96183 | 2025-06-25 05:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 1f91546e-6996-37f0-9dd4-954bfb68f831 | -12.58309 | -56.98949 | 2025-06-25 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c44f2be9-adb8-32d9-bbe2-0379a78360f7 | -10.87249 | -54.32358 | 2025-06-25 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 186304bc-0009-3b66-90ca-f4b327d463f7 | -8.47488 | -50.28315 | 2025-06-25 05:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3770a02f-c1aa-3796-af0d-da8aefea62bb | -9.91864 | -52.43395 | 2025-06-25 05:25:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88f8a4f1-9d56-3ca3-b648-a881de8301c0 | -12.58358 | -56.98592 | 2025-06-25 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f9c560c-bf15-3ee2-8048-3521e8cef568 | -10.8695 | -53.76581 | 2025-06-25 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64e8b150-98e5-38c5-bdb5-d30265f76e41 | -11.18102 | -48.61852 | 2025-06-25 05:25:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03e368bb-cf2c-3502-aa9e-77ccf7a2318f | -14.80853 | -48.29892 | 2025-06-25 05:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8bdb55b5-7409-3b94-9d1b-24ce26d716f3 | -10.82831 | -54.00512 | 2025-06-25 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 343940d8-0aef-3430-9cac-9816d554c730 | -13.04782 | -48.83006 | 2025-06-25 05:25:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7558609b-2852-3af9-9948-c63dca8e9721 | -10.8689 | -54.3243 | 2025-06-25 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 508f46e1-2fce-35bb-bbae-573226aea2a7 | -10.82356 | -54.04131 | 2025-06-25 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 838309dc-3478-3b4d-8d5f-0b41cdf7ea41 | -9.50449 | -56.10234 | 2025-06-25 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2fa36101-a2f5-3b58-ac77-68465211b2d6 | -10.81807 | -54.04601 | 2025-06-25 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2730d36-e3e9-3644-8bb6-ef882d169d88 | -3.61978 | -47.53135 | 2025-06-25 05:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75488a23-a40c-3a8d-b5a7-c443d9031307 | -10.3593 | -57.25704 | 2025-06-25 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91847f5f-2eed-32fc-b2e5-479c6dc38671 | -9.50552 | -56.09514 | 2025-06-25 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0ad40e92-b7be-355c-a8b7-f8cabede2e69 | -10.83246 | -54.04777 | 2025-06-25 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 88074eea-6487-33ca-8ea7-a807ff41e359 | -11.13938 | -53.92113 | 2025-06-25 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3230a55-3b83-3618-aad9-8b25d57fc570 | -9.50908 | -56.09938 | 2025-06-25 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 54d4b6e1-e14a-3ec6-9a2b-e1ec8ac29603 | -9.5096 | -56.0958 | 2025-06-25 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 82f3e921-9f9a-3e94-945b-50389dd93a56 | -11.57337 | -47.43525 | 2025-06-25 05:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eb052229-4605-3d4e-928a-010406bfe654 | -13.0415 | -48.82975 | 2025-06-25 05:25:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6c171dd-f70f-3bb4-b783-3794b123ceeb | -7.86552 | -50.66741 | 2025-06-25 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01fdae17-2f20-34b2-87de-ba9c7e0b6ad6 | -9.56818 | -49.11298 | 2025-06-25 05:25:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| cb555784-644e-3251-8753-5dee9b43b98c | -11.94262 | -48.42266 | 2025-06-25 05:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c93950e8-8acd-3abb-8894-5460e559f098 | -12.79411 | -48.73444 | 2025-06-25 05:25:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 842c3948-26eb-331c-96b6-d0e535794a50 | -8.67669 | -51.46714 | 2025-06-25 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8553ae52-2107-3936-8cc6-82c9bd67b71b | -11.83902 | -57.85808 | 2025-06-25 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 263a98dd-83a2-3012-8444-adf8dbb64744 | -9.92391 | -52.43467 | 2025-06-25 05:25:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20088ac0-adb4-3212-bbde-c2bcb1efe362 | -2.90851 | -54.48871 | 2025-06-25 05:25:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b239b59d-c139-3ce7-aade-0c39cd9dc19e | -9.17411 | -61.40248 | 2025-06-25 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5c29243e-ddec-36f7-a037-d77019ca3402 | -10.82835 | -54.04193 | 2025-06-25 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15fadc07-e055-3d1e-b8ce-83a2b55c118b | -9.505 | -56.09874 | 2025-06-25 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f7bc83f2-057c-3048-b38c-5f1d4427213e | -9.56884 | -49.10757 | 2025-06-25 05:25:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 64b31383-54e0-3924-be12-13f94b5e615f | -12.80724 | -48.73457 | 2025-06-25 05:25:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa97f8c7-f674-30e7-bcbe-1fb7ef0005ee | -9.85706 | -55.16193 | 2025-06-25 05:25:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6ca3d176-8dcd-3586-9398-35723c71eded | -13.04079 | -48.83603 | 2025-06-25 05:25:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 025cc899-7df2-388f-a627-188818756636 | -10.36246 | -57.26237 | 2025-06-25 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13363be0-0b04-3d0e-b359-a2bcdc11b1d5 | -9.50144 | -56.09451 | 2025-06-25 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 147acdb7-f339-3564-bb11-f94282cdda93 | -13.04731 | -57.09581 | 2025-06-25 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7740473d-f455-3cc6-87f3-93ea2f9888d9 | -9.56751 | -49.11835 | 2025-06-25 05:25:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 276530e4-d41f-3eb8-9da6-392148912474 | -12.58712 | -56.99008 | 2025-06-25 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f97b60f7-d3b1-3883-9e89-47136f18611f | -10.83726 | -54.04833 | 2025-06-25 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 989bbcba-96d1-3a79-8f17-a6fda7d19e65 | -9.92348 | -52.43795 | 2025-06-25 05:25:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80918dd9-a841-3548-a627-472c17c473b1 | -3.62135 | -47.5361 | 2025-06-25 05:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4681e3e3-c1e3-3f38-861e-6e84ccf2e39b | -10.82766 | -54.04721 | 2025-06-25 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8bb537a-28c4-370f-9b32-20f654368730 | -9.51265 | -56.10357 | 2025-06-25 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eff2c47d-c690-324e-8b32-52dbaec34c47 | -7.94611 | -63.01002 | 2025-06-25 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c2e2a8c-5707-3581-a742-fc75801a638d | -13.29282 | -57.08325 | 2025-06-25 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c9bc5bf-df2a-3ab6-8c60-e2e8b2da13e7 | -10.06299 | -55.55442 | 2025-06-25 05:25:00 | NPP-375D | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e3baf38-b38b-3b5e-bcd1-07f0e4df5fbf | -2.53302 | -53.95713 | 2025-06-25 05:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a42a9b39-8696-38c6-b652-a84403ca2ac2 | -8.67594 | -51.46528 | 2025-06-25 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6487298-6f17-3e18-acab-4447fe036ae1 | -11.57378 | -47.43639 | 2025-06-25 05:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 60648c36-87a9-3e98-8ddf-4b4ceaae4cc6 | -7.91813 | -61.54978 | 2025-06-25 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3218ca6-a5ac-301f-8c54-b99cf459c2b9 | -8.71555 | -47.85745 | 2025-06-25 05:25:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8f6cba0-a0f0-316d-84d1-115a0aed5e0a | -7.90204 | -61.52201 | 2025-06-25 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ec3ff4b-dabd-3662-b913-d8e4307e0b4f | -10.86531 | -53.75979 | 2025-06-25 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42d03da9-2f49-33cd-b1b7-b19feeaeb92f | -10.86848 | -54.31789 | 2025-06-25 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7435f5da-3045-3b76-90f3-90712f2c3efc | -11.14008 | -53.9157 | 2025-06-25 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7398184b-20b1-37dc-a49a-ef3d4296fb01 | -10.30374 | -57.13832 | 2025-06-25 05:25:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78a8184d-c8d2-3803-9d7a-1c5e787f1bc9 | -21.81544 | -56.29502 | 2025-06-25 05:27:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db01f7fd-7129-3fe2-9fb2-a4daedf715c1 | -21.68012 | -57.34482 | 2025-06-25 05:27:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d155714-9937-3208-9d29-27408f95cc95 | -20.9242 | -49.09481 | 2025-06-25 05:27:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 434b0891-6abb-3c1b-8ca8-97bfcf7d2d05 | -21.81518 | -56.29629 | 2025-06-25 05:27:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README18.md)
