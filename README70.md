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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72c97e22-ca66-37e7-89c7-3abf540c962c | -3.04663 | -53.01431 | 2025-10-27 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4beb8c21-77cf-390c-9ae9-fb859ee6fd83 | -5.77804 | -51.56442 | 2025-10-27 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d131e03f-c4cf-323f-96ca-f2446615be4f | -3.57482 | -49.02067 | 2025-10-27 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6c14cfb-d7b0-38c2-b802-4eca59f43208 | -3.09732 | -54.61776 | 2025-10-27 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75685246-8322-3e5e-aacd-ce2b92e19373 | -5.77426 | -51.56125 | 2025-10-27 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb0f96f6-80c3-3917-a0dd-63877da9f5de | -10.41638 | -47.65205 | 2025-10-27 05:23:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d5a2a138-1627-38a4-bdb9-014c830de2af | -3.97829 | -55.74456 | 2025-10-27 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f355e336-53dd-312b-9da3-5c6c79022025 | -14.24973 | -48.13493 | 2025-10-27 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4cb7b77d-5ef3-3b75-85b4-64137941e369 | -13.31628 | -54.37243 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 84f36566-fb62-3385-a5cf-fa95234c1ff1 | -13.32033 | -54.3797 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2ff028c4-d458-3b32-a07e-92586261fb76 | -3.10177 | -49.44512 | 2025-10-27 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 811d22c4-25d3-3cd2-9cc9-91546084e63c | -13.30326 | -54.36033 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| db2fc66e-8da4-31b8-803b-ba56315ce725 | -5.77472 | -51.85754 | 2025-10-27 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d9f0f2d6-d084-39ba-a39e-7e6ccd50af3e | -4.32538 | -48.09506 | 2025-10-27 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c98e0639-5d80-34e2-a86e-60ff2167d48c | -6.8968 | -52.19513 | 2025-10-27 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea52a4f0-653b-3174-875a-397dd391a4fa | -12.89045 | -54.73257 | 2025-10-27 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12947071-5c96-3c22-bbcb-eeb038a2023b | -3.25108 | -50.04272 | 2025-10-27 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d853da21-8a01-350e-b452-db08be5b3c28 | -3.8116 | -51.7826 | 2025-10-27 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 034e1817-5390-33ef-aef0-514e6b4592e6 | -3.24593 | -50.65717 | 2025-10-27 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0338e03-ea45-361d-94af-62966cdff3b8 | -7.24383 | -46.9585 | 2025-10-27 05:23:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 29528bd4-a166-3478-ac78-54632a1f9003 | -8.88907 | -47.99945 | 2025-10-27 05:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13f1c066-d0a4-3d64-b769-42d1adda4bbb | -9.4456 | -56.64885 | 2025-10-27 05:23:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 845a894a-adc5-3407-b621-5fc2200b6874 | -4.26467 | -50.508 | 2025-10-27 05:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09bee76e-3c84-34d9-a8b7-060dac9fe002 | -13.27326 | -54.36696 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f8e899c4-a36c-3927-99d4-d13fc4eb700d | -7.23078 | -46.94759 | 2025-10-27 05:23:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 96e86f90-077f-35cb-a81e-019dc5d1765d | -3.04974 | -53.02413 | 2025-10-27 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ba430098-1dbc-3cff-b928-53eb18e55d31 | -3.42465 | -52.43172 | 2025-10-27 05:23:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0645805e-6356-35d3-a30a-a6665f4bc2ba | -8.06653 | -46.95918 | 2025-10-27 05:23:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| defa99c4-0c31-39a1-9b72-833cea6aedbd | -13.25351 | -54.36951 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| b7a33b9c-3678-365f-8c20-005b390f5193 | -2.06358 | -56.88437 | 2025-10-27 05:23:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e16e375-0391-3b02-b5c5-c9624106469e | -13.30603 | -54.37653 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbc92035-a61e-3c00-9d0d-aaaa0601d784 | -5.71048 | -49.30693 | 2025-10-27 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0cc74587-6cff-37d5-83a9-1a516da94b3f | -13.29314 | -54.40116 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 981587b9-b68c-31ee-b200-42901bf243dd | -3.39072 | -50.39817 | 2025-10-27 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0b1a5ef-d764-367e-ab1c-0f72b4a5f1d5 | -3.98399 | -49.29015 | 2025-10-27 05:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f09196f1-c4cf-3cbc-8e86-516e04402fbd | -8.10133 | -47.05542 | 2025-10-27 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9772fb4a-4d9e-3075-a483-219b36165a4e | -13.32097 | -54.37446 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bf3b891b-6125-316a-9e44-134cd8d1680c | -3.24062 | -50.65634 | 2025-10-27 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff38f9ea-0853-3511-b3a8-4e27a0550833 | -10.8383 | -56.96259 | 2025-10-27 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 871709f1-7a57-30c8-88f6-0990967ad1be | -10.63062 | -52.18592 | 2025-10-27 05:25:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75102efb-2c8f-3370-94d5-21c0e938fda0 | -9.40631 | -64.42498 | 2025-10-27 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5fa90970-33d4-3eac-b166-b2b780571d08 | -10.34333 | -54.19965 | 2025-10-27 05:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 70887a27-2905-37fb-8844-92670411cdbb | -12.86137 | -48.64224 | 2025-10-27 05:25:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b869f731-ab2c-3024-b65c-86ad7b45546f | -9.63145 | -57.015 | 2025-10-27 05:25:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3525e3f1-c856-342f-bcde-06b33143b738 | -11.10486 | -55.55828 | 2025-10-27 05:25:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65764136-058c-32db-8241-df0e6db338dc | -8.97861 | -65.94133 | 2025-10-27 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a62dd2b2-fa4c-3906-bea4-101f59c36f7d | -10.90659 | -50.23131 | 2025-10-27 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34ab2ba2-9d04-337d-a90f-191b5fb55671 | -10.21642 | -52.65868 | 2025-10-27 05:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a33ee371-2a6e-35b1-aebc-9abdf1f6cd49 | -10.83899 | -56.95766 | 2025-10-27 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1a8ba4e1-bc15-33ea-a000-92323b409926 | -11.62733 | -54.57941 | 2025-10-27 05:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b04cbad-6c95-3fef-a3fe-8b8134d2f161 | -10.21599 | -52.66183 | 2025-10-27 05:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62dda705-3c6a-3b26-9d95-54f7acec76a1 | -10.83441 | -56.96203 | 2025-10-27 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 4b49cbc4-160e-3c96-80c3-149d258cd2c9 | -9.78151 | -64.17458 | 2025-10-27 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7917a742-8be5-362d-9673-ab2e35f6daf4 | -9.85324 | -64.17751 | 2025-10-27 05:25:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6952a5ed-c984-38a1-8055-e7fe54dad5c5 | -10.38401 | -57.49569 | 2025-10-27 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fe723fa-8c41-3cb6-bf4b-7b4b76564f24 | -11.63193 | -54.58001 | 2025-10-27 05:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0199c428-714c-3025-9278-e555b9b6d7a7 | -8.96384 | -65.93158 | 2025-10-27 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee1998d3-9d3f-3212-8f30-c05b41fca799 | -9.88696 | -58.02981 | 2025-10-27 05:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f417d43-ab4f-3a5d-a580-eb57f7ec5606 | -8.9719 | -65.90803 | 2025-10-27 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42e6524a-2db0-34d9-aab8-43658667214c | -10.10129 | -65.11801 | 2025-10-27 05:25:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87e3032b-24fd-38cd-9d05-0140c3814bae | -10.21558 | -52.66493 | 2025-10-27 05:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6bdf2aa4-68d2-3ea8-b662-4ec088b3f320 | -11.6313 | -54.58483 | 2025-10-27 05:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d34c6489-279f-3451-b7d0-5573bb25f2fd | -10.83376 | -56.95992 | 2025-10-27 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 06024947-126e-39f0-8f44-4529348eac5b | -8.97262 | -65.90371 | 2025-10-27 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| debf8128-e8ce-3c7f-b677-eba10ee3e79d | -10.63553 | -52.19 | 2025-10-27 05:25:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85261d2b-4794-3f79-88ef-56abd8448306 | -11.09149 | -55.56055 | 2025-10-27 05:25:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe3acc81-2a42-3f0f-9ff7-66510e0ba23f | -10.90603 | -50.23595 | 2025-10-27 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f0c1278-fff8-3b52-a062-778193565ba3 | -9.56165 | -66.76096 | 2025-10-27 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fcaa2625-e63c-32ae-8388-f2d9469468c8 | -10.83448 | -56.955 | 2025-10-27 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 2c22f742-d183-3bef-a8d4-cd8616a02117 | -9.63058 | -57.01673 | 2025-10-27 05:25:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f361ad2b-ba48-3b5f-baa6-beedc9f8ef7d | -9.61744 | -66.4613 | 2025-10-27 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9460e770-5113-3930-835f-24c3ec5c5b47 | -10.08323 | -59.41704 | 2025-10-27 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5af08c9-576e-3df9-9d50-6e4fd3b89a79 | -10.03243 | -59.59117 | 2025-10-27 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fbd57e9e-1187-37fa-b6f9-7f087d188370 | -8.96792 | -65.90733 | 2025-10-27 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b05499b-a223-3c67-a3b4-96549d86a58e | -10.95526 | -47.58197 | 2025-10-27 05:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ebca80d1-aae9-3c61-affb-6761452383e3 | -10.963 | -58.97373 | 2025-10-27 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b676c1a7-b9ae-35b3-8270-e47afd0883b3 | -10.8351 | -56.9571 | 2025-10-27 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 02acc045-ffc7-3348-ac0d-e187c531ece1 | -10.91155 | -50.24137 | 2025-10-27 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe90fbf7-12ca-3e60-9f34-aeefaecffbb7 | -10.83764 | -56.96048 | 2025-10-27 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 15d8ce1f-06f2-361a-90ea-4167e84bdbce | -10.83579 | -56.95215 | 2025-10-27 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 82c2a383-ee96-3d14-9283-3dfd506994c3 | -11.09576 | -55.56113 | 2025-10-27 05:25:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88550168-d66b-3ed1-ba8f-a7d2e1d4b59c | -9.00158 | -65.93808 | 2025-10-27 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a651b7c-17b4-3900-a5b3-b70a95c5ed18 | -10.9546 | -47.58792 | 2025-10-27 05:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9f15da7-cc6a-3bbc-a5d2-f082734181f4 | -12.85446 | -48.64185 | 2025-10-27 05:25:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02ffedb3-d05c-3d4e-881b-082b34849a35 | -9.85393 | -64.1734 | 2025-10-27 05:25:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9be59134-957e-32ec-a98c-3d862da2264d | -10.38774 | -57.49625 | 2025-10-27 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a4cfa09-1b5b-3c15-8468-4154dc2326fe | -10.63019 | -52.18929 | 2025-10-27 05:25:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90517db0-3f30-38f1-b72c-68d84b7c2914 | -10.96241 | -58.97766 | 2025-10-27 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3bf46a6-6d1d-3fc1-804e-ba0f88aed700 | -10.10286 | -65.11652 | 2025-10-27 05:25:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0ca3e6f-c91d-3e00-8e0f-b3e71c6579bd | -12.04204 | -54.23901 | 2025-10-27 05:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b04cc94-e951-3548-98f5-3c1b2b7a613d | -10.83836 | -56.95556 | 2025-10-27 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 8d9f29dc-5fcd-3019-9f30-8f765513a7b0 | -10.21086 | -52.66114 | 2025-10-27 05:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce1658b9-c8f0-31c3-91e4-f9b3fc3213dd | -10.34188 | -54.20134 | 2025-10-27 05:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2cdbde4d-339a-34c6-8dd7-e6dc8a4d2dba | -10.63595 | -52.18664 | 2025-10-27 05:25:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93647c66-5c66-3380-b991-1d25f31c767b | -10.21044 | -52.66427 | 2025-10-27 05:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1038e3fc-ac4c-381e-a17c-c596353ad065 | -8.96734 | -65.91077 | 2025-10-27 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27003792-ede4-3281-aa51-f0d1c14f622c | -10.87715 | -54.04895 | 2025-10-27 05:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 56840386-aa79-3fb6-bc19-4d90f3793ade | -8.98046 | -65.94156 | 2025-10-27 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 832dc9eb-088e-38f8-ab65-cbc1acc0a057 | -9.85462 | -64.1693 | 2025-10-27 05:25:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18a95bf3-d65a-3399-9866-820c95a5b9ff | -10.83122 | -56.95654 | 2025-10-27 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |


[Clique aqui para ver as próximas entradas](README71.md)
