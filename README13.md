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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0abeafb-5b68-3652-9a3e-ad3609dc8c7f | -11.25 | -50.55 | 2026-09-01 01:15:00 | MSG-03 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8e92b606-0b81-3671-bcb9-b37a8283b700 | -17.3713 | -42.3794 | 2026-09-01 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 00795121-b264-317a-990a-d22163c39705 | -6.6035 | -58.6166 | 2026-09-01 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 12bc2cc4-0508-3ff9-997c-7be3b16eafd0 | -19.194 | -57.3926 | 2026-09-01 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.8 |
| 8124a49e-2d41-3d77-9e52-22924f4143fe | -3.879 | -44.0576 | 2026-09-01 01:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| ebc04316-51b1-3421-ad95-3a2ff237a789 | -6.9551 | -55.655 | 2026-09-01 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 9d220f82-981e-3188-a6d9-8afdc4b2c328 | -7.571 | -60.4643 | 2026-09-01 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 6ec51ec1-559e-30bd-82e5-1e6741ac9b0e | -17.3921 | -42.3495 | 2026-09-01 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 298.8 |
| 0e1c1849-e5b1-3571-8cf5-f71343a6a3ae | -10.0364 | -44.6825 | 2026-09-01 01:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 129.9 |
| e2a3baf4-7ce7-32c1-9634-04ba669bdb2d | -7.5895 | -60.4636 | 2026-09-01 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.8 |
| c958678b-7ece-3fc1-9056-8f3e825234e2 | -10.0173 | -44.6849 | 2026-09-01 01:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| cbc7c150-9557-355a-bfb4-7f4d981e7805 | -11.2767 | -50.6029 | 2026-09-01 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 219.2 |
| 40ea6329-7273-344a-935a-9e11b7f02514 | -3.8605 | -44.0355 | 2026-09-01 01:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 57c18a01-ac5c-32b1-8272-433c33104351 | -7.3487 | -60.5883 | 2026-09-01 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 584194b3-6aef-3ce2-8419-aa34d9d1d073 | -11.258 | -50.5836 | 2026-09-01 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| aa94665c-c42c-3eae-a97c-86f50fd4ac69 | -7.182 | -60.6904 | 2026-09-01 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 6a516803-9540-377c-b75b-1c02947a9e56 | -11.277 | -50.5815 | 2026-09-01 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| a5772d4a-9908-3c4f-800b-2bfe2589221c | -17.3914 | -42.3744 | 2026-09-01 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 0b86fc56-57d1-3049-bc55-b3d7a663eea7 | -7.9048 | -44.2577 | 2026-09-01 01:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| d53d7e1a-b315-3da9-8d5d-82e96978e5c5 | -3.8604 | -44.0585 | 2026-09-01 01:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| fc5fa365-38da-3f8b-b72d-30264f689d42 | -14.4587 | -52.5151 | 2026-09-01 01:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 927aece2-270c-3032-b111-31ab64f38ad4 | -6.9552 | -55.635 | 2026-09-01 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 7df3830c-0ae7-3708-992b-47ab6523c848 | -6.5851 | -58.598 | 2026-09-01 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 80633aff-e30b-3010-afa5-2955ff7b18c4 | -10.036 | -44.7056 | 2026-09-01 01:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 43b51d97-ec0b-3f8e-88e2-b2d52a4481cd | -10.3574 | -50.0171 | 2026-09-01 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| e7e5795c-309d-3ef6-9094-17bd1b131297 | -16.0547 | -54.3908 | 2026-09-01 01:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 76a0b0f5-ba12-3d19-b7b7-1542002c6b45 | -17.372 | -42.3544 | 2026-09-01 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 60e9eb09-d41d-3aa4-badf-e1b8266c76fc | -3.8603 | -44.0815 | 2026-09-01 01:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| e3596828-ac30-3f5c-87f1-605a0ecee640 | -6.6036 | -58.5972 | 2026-09-01 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 725db03c-be53-3b2e-96ef-150f53fd63b4 | -6.7162 | -55.4082 | 2026-09-01 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 537013ca-80c2-3713-a678-775fa80c8c5f | -6.7358 | -50.4721 | 2026-09-01 01:20:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 59e21b31-0248-3a8f-a303-9447a8ab9a96 | -7.5709 | -60.4835 | 2026-09-01 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 2c917831-a402-3b36-8290-b820d8cbafcf | -7.905 | -44.2346 | 2026-09-01 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 81.2 |
| dd7cac7e-7627-3812-b249-7264720e9155 | -6.6976 | -55.4091 | 2026-09-01 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 8a6f77dd-2ed3-3bec-84c2-56a484119ad0 | -19.1347 | -57.3589 | 2026-09-01 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 238cdfa3-aae8-3154-ba41-9bdb4f8d215a | -19.2147 | -57.3483 | 2026-09-01 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.1 |
| 29687969-8aba-391d-9d6e-7fafa047a9fa | -7.2005 | -60.6897 | 2026-09-01 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 88142295-320c-3d78-a56a-2a6c05c926ea | -3.8605 | -44.0355 | 2026-09-01 01:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 58491bc1-cad6-3ce9-884e-2c2c0e048cff | -14.4587 | -52.5151 | 2026-09-01 01:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 41.3 |
| ec6eb752-3fbc-3b07-a86d-36c61f1d6e2d | -6.6035 | -58.6166 | 2026-09-01 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 42a656c8-444f-3ab2-afdf-704337ea59c5 | -11.2767 | -50.6029 | 2026-09-01 01:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 277.0 |
| 330b394e-2c1d-3806-bcc5-002793f664be | -17.3914 | -42.3744 | 2026-09-01 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 315922b0-2848-36ce-9498-bdbdab677921 | -3.879 | -44.0576 | 2026-09-01 01:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 151840b8-68a7-32b6-9e11-c94e2d940af9 | -11.258 | -50.5836 | 2026-09-01 01:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| de237ecf-545d-31de-9294-3fd895a15d6e | -7.571 | -60.4643 | 2026-09-01 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| c6cd14a9-8adc-344a-9a61-77fd2aca6f29 | -3.8603 | -44.0815 | 2026-09-01 01:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| beb4fc9e-eb32-3890-94a6-07d7852c4012 | -11.296 | -50.5794 | 2026-09-01 01:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| e12fc6d0-edd6-3fd6-ae21-1e5768258f98 | -17.372 | -42.3544 | 2026-09-01 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 4f801492-56b1-3fc1-9022-5638086da0c1 | -7.3487 | -60.5883 | 2026-09-01 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 7bb201a1-51b0-3a5b-9929-907df61c6eb5 | -3.8604 | -44.0585 | 2026-09-01 01:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 04c78156-2813-3b75-8528-b9f5e538ea87 | -16.4773 | -47.9381 | 2026-09-01 01:30:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 46.5 |
| de9de34f-6230-305d-8605-98532eaa905e | -16.0547 | -54.3908 | 2026-09-01 01:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 89eb61e1-996d-386e-ad52-999aeb1b38fc | -10.0364 | -44.6825 | 2026-09-01 01:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 161412ba-7d23-3996-8da9-9aa568aadeea | -11.2957 | -50.6008 | 2026-09-01 01:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 218.7 |
| dd381b00-7bf7-3cea-a1b7-670a72d5bd8f | -7.5709 | -60.4835 | 2026-09-01 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.8 |
| b09a0761-a2f5-389b-bfb4-a3a7b3231a9a | -17.4122 | -42.3445 | 2026-09-01 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 74.9 |
| fdfce268-ff03-3144-8d43-5e443c24977d | -3.6215 | -60.566 | 2026-09-01 01:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| ce98ea6b-2dd8-3e96-9709-e6e4fe337eaf | -19.2155 | -57.3066 | 2026-09-01 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.5 |
| 2597e795-e516-3296-951c-8b41a09cdcd0 | -7.5895 | -60.4636 | 2026-09-01 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 858eef10-7589-30b2-ba59-75fe362ca1d7 | -19.2151 | -57.3275 | 2026-09-01 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 243.3 |
| b54a954a-072f-3657-a666-53331e8e9593 | -16.3258 | -49.4662 | 2026-09-01 01:30:00 | GOES-19 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 88b2dc40-706d-3536-99e6-5ea10d4a119c | -16.4768 | -47.9608 | 2026-09-01 01:30:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 828d9d3c-3d38-39de-8519-9c5ff67b18bb | -7.5894 | -60.4827 | 2026-09-01 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 6a319265-c1ab-3ee7-b86a-6f810e2a3296 | -6.585 | -58.6174 | 2026-09-01 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 9298d1a5-ebf6-3a7f-97c6-9349919776df | -6.9552 | -55.635 | 2026-09-01 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 2c53aadf-1bf3-3ed8-bb9e-94b312d16d3f | -10.036 | -44.7056 | 2026-09-01 01:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 4da7dc03-8564-3f2d-b7ca-bdf35aa2596b | -6.5851 | -58.598 | 2026-09-01 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| a036e63a-2c53-3634-92da-517c75a1dca8 | -19.194 | -57.3926 | 2026-09-01 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 4766ff6c-64bb-3891-9b1f-48e93c317d0d | -11.2577 | -50.605 | 2026-09-01 01:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 299c6379-2553-3f93-ae1d-d0a1fc23a318 | -19.1951 | -57.3301 | 2026-09-01 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 217.5 |
| 14010682-c8bc-39d1-9786-9de80bb85e14 | -19.1947 | -57.3509 | 2026-09-01 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.2 |
| d7ec6e68-629e-3afd-8e84-8f93cfd7bbc1 | -19.2351 | -57.3248 | 2026-09-01 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.8 |
| 8bb25024-3417-317e-8c2d-1e16fb3e3d81 | -6.6976 | -55.4091 | 2026-09-01 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 0ca61929-89a7-3e59-b91f-20d663acf0d5 | -16.3262 | -49.4439 | 2026-09-01 01:30:00 | GOES-19 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 5a55d439-5def-358f-8ba4-cc63ba91e46d | -11.277 | -50.5815 | 2026-09-01 01:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 164.3 |
| f9def32d-ec70-31e7-9e9a-1426bb6fa968 | -7.3488 | -60.5691 | 2026-09-01 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 9ffb4fe0-96ea-3d50-bb6e-e09792384c9a | -17.3921 | -42.3495 | 2026-09-01 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 207.6 |
| 3c5ed110-787c-3efd-acbf-7b0d1aba22e7 | -6.6036 | -58.5972 | 2026-09-01 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 0701f0e7-b6ff-33aa-9f36-e5d697b8b694 | -14.4587 | -52.5151 | 2026-09-01 01:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 57.6 |
| de7e48f1-0bf0-34ce-986c-13c7dbae21be | -11.2957 | -50.6008 | 2026-09-01 01:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| a1809548-1904-3b27-af71-5f039054435f | -16.0742 | -54.3882 | 2026-09-01 01:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| e475795a-80dd-3854-8c24-02a1f75716c0 | -3.879 | -44.0576 | 2026-09-01 01:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 844c0729-e64f-3b30-be9b-576ee12a8235 | -7.3487 | -60.5883 | 2026-09-01 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 9a3a6d5c-da3c-3286-ac64-afbed02e8c9b | -16.4768 | -47.9608 | 2026-09-01 01:40:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| f344f127-ce19-3a94-81b6-4e72aacf951e | -7.3488 | -60.5691 | 2026-09-01 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 1ffa48d1-9f3f-3ecf-9846-d94e3d91c33d | -6.5851 | -58.598 | 2026-09-01 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 0ad203a6-62ad-347e-9309-90f8ba590a1a | -7.182 | -60.6904 | 2026-09-01 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 29dcfcc3-754e-3434-ac23-e98a9797edd8 | -7.5894 | -60.4827 | 2026-09-01 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 2aa259f4-845a-3167-b450-6004559574c9 | -7.3672 | -60.5875 | 2026-09-01 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.1 |
| f419b010-cfc6-3bb5-ac1d-a659d10c1cca | -17.3921 | -42.3495 | 2026-09-01 01:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 232.7 |
| 7b7018c6-9727-31ae-8724-37188f94b91c | -17.4122 | -42.3445 | 2026-09-01 01:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 54.7 |
| d1a312b6-bc8a-379e-bf0d-2e3184d614f8 | -16.0547 | -54.3908 | 2026-09-01 01:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 110.9 |
| a6bc7f9d-fb30-3378-9197-4658593ccc6a | -7.571 | -60.4643 | 2026-09-01 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 251.2 |
| 91fd4939-10e6-3cb3-b34a-ca44011d5f5e | -16.4773 | -47.9381 | 2026-09-01 01:40:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 3f4d43e9-5e6a-3b90-ba18-e58e09d66bcf | -6.1844 | -57.7395 | 2026-09-01 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| cddb7a5f-ec49-3800-9c9c-d1187069041e | -11.2767 | -50.6029 | 2026-09-01 01:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 9afa12ad-b016-39ce-ab27-1478184b1231 | -6.6036 | -58.5972 | 2026-09-01 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 162282b9-2fad-398b-865a-76805862c16c | -7.5895 | -60.4636 | 2026-09-01 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 169.2 |
| a847db33-3b42-38b9-88dc-db448f18362e | -19.1347 | -57.3589 | 2026-09-01 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.2 |
| fe246ad5-de80-3ba6-b5fd-857f82c37ae2 | -3.8604 | -44.0585 | 2026-09-01 01:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |


[Clique aqui para ver as próximas entradas](README14.md)
