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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83f41aed-afe5-37fc-a3fe-3e77a496ab53 | -10.7268 | -50.6618 | 2026-08-31 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 29139a0e-73f0-3c15-b298-73823dc470ec | -11.3806 | -45.1928 | 2026-08-31 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| cf256c3c-b890-32eb-a746-71134cfb8a6a | -12.9032 | -45.8382 | 2026-08-31 15:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 78082d5b-8af7-3ab1-a6eb-39312096cac7 | -10.8987 | -50.5372 | 2026-08-31 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 81ba1ad4-dfb3-3bca-a44f-500c0d146dd2 | -9.0615 | -65.4169 | 2026-08-31 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 80ef0386-7e9b-35c0-90ad-1dafec6055e5 | -3.6398 | -60.5656 | 2026-08-31 15:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| b72eccf5-d8e1-3e0a-bda2-e43fb747fbbb | -11.2294 | -45.099 | 2026-08-31 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.2 |
| af1842bf-e1cb-32d8-acdd-43d280cc1fb3 | -10.5607 | -50.3595 | 2026-08-31 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 1f4476fb-2362-3275-9523-6d7964485fa7 | -3.1997 | -61.1799 | 2026-08-31 15:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 202d07ca-64fe-30f4-a4e8-b47e3cc2f140 | -6.2469 | -53.6826 | 2026-08-31 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 2d314da9-5cf2-3e81-900b-1de61f4398ed | -10.844 | -45.3356 | 2026-08-31 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 731d1e6b-170f-347a-8324-1387aa1c89fe | -7.566 | -61.343 | 2026-08-31 15:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 7f29648a-5b43-3000-b207-5fc560e7b0b1 | -7.9425 | -44.2538 | 2026-08-31 15:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 158.4 |
| 0d46d852-14b6-35f6-bdb9-d3ab35cd13ac | -3.6215 | -60.566 | 2026-08-31 15:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 201.9 |
| 08c35d8a-1f49-38a2-9685-4d06b8f69f62 | -3.1998 | -61.161 | 2026-08-31 15:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 54b0e003-cdc9-3877-92bd-a7b1401cb242 | -6.7514 | -55.6654 | 2026-08-31 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| ed41fc5b-673c-382f-954b-cccdbe69ba07 | -11.0434 | -49.6851 | 2026-08-31 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| e1515609-9941-301a-9f8c-e8e36198d01f | -18.2695 | -52.7284 | 2026-08-31 15:00:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 55f1ea30-b29f-357f-942f-46cdae86737f | -13.967 | -54.395 | 2026-08-31 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 226.8 |
| f13a36cb-10a7-3a48-bf20-b734bb321ce9 | -6.7691 | -58.6873 | 2026-08-31 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 2761b8d6-ddcb-36c6-b99f-e90e5d1824f3 | -11.2314 | -54.0164 | 2026-08-31 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 92777a62-15fc-340f-80bf-d32da2335ae4 | -11.0244 | -49.6872 | 2026-08-31 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| defba2d8-9521-362c-bc44-eeced8f2e5f0 | -15.2275 | -56.3716 | 2026-08-31 15:00:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 8087dafd-d193-34a6-9a2f-5d075767b75c | -10.8218 | -50.6306 | 2026-08-31 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 739bc40b-eb9e-3c39-90d7-839ad5df0651 | -10.8022 | -50.6752 | 2026-08-31 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 7c7e53cc-d5a4-39b8-bef0-e36ea16039cc | -13.8371 | -54.0989 | 2026-08-31 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 764adbb7-cf4d-37b4-bdf1-441bb06b8ac7 | -5.8783 | -59.9726 | 2026-08-31 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 08d382f7-0889-33b3-834f-c7cfe2994943 | -13.8563 | -54.0967 | 2026-08-31 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 181.9 |
| 8ef6fdf4-4aa6-3326-a77a-5ceeb8f1f016 | -9.5964 | -47.6204 | 2026-08-31 15:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 306.3 |
| cfed6583-3546-3426-9aa9-3e7f22fcf1dd | -13.9667 | -54.4157 | 2026-08-31 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 223.8 |
| a211bd03-61fd-378a-88dd-3f5ad5155d1c | -13.471 | -57.0373 | 2026-08-31 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 6c644996-511e-3b75-a193-7686e77e2c79 | -11.0376 | -51.4559 | 2026-08-31 15:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 54.8 |
| a565957e-1a85-341e-80d5-cc846c97c1ac | -7.9608 | -44.2981 | 2026-08-31 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| dfbc77f8-30d0-3afb-81c1-cfa4aab6ab4f | -9.6939 | -65.1145 | 2026-08-31 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.1 |
| d417ab45-6917-30e2-a388-ca1c2cc0fb09 | -15.6336 | -56.3876 | 2026-08-31 15:00:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 266.7 |
| 335ea53e-7305-3277-bde8-1a2cea8cd7e2 | -6.7832 | -59.4401 | 2026-08-31 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 1faf665c-5a50-3201-9720-3cacb629980a | -10.7428 | -50.8727 | 2026-08-31 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| d8992182-c138-35af-9cc6-9ae95e56fc32 | -13.9474 | -54.4179 | 2026-08-31 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 146.3 |
| b4280042-24ad-3f5b-8ff9-2f05ee0d3b12 | -10.8215 | -50.6519 | 2026-08-31 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 8c9a7ad5-3b5b-3337-9f1e-1050db2a2ae1 | -10.7596 | -54.0384 | 2026-08-31 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.9 |
| f50bed9f-6bc0-3049-a780-2e6fd7e0097f | -6.1295 | -57.6637 | 2026-08-31 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| c75bed6a-fede-3a81-b7e3-c5b4edcb3398 | -14.4835 | -52.1938 | 2026-08-31 15:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 692e0273-8a09-362b-88f2-4a9008ff42f2 | -14.5871 | -54.0944 | 2026-08-31 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 01c9a77a-6771-35f9-bc16-a4a17809b89d | -11.0752 | -51.4731 | 2026-08-31 15:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 546f7c05-6d45-31bc-875f-f7197c5b7060 | -11.0744 | -51.5365 | 2026-08-31 15:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 153fa33b-ad82-33fa-b775-309ea209f75c | -10.3391 | -49.9762 | 2026-08-31 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| b5cdfe47-ee35-3324-b234-738727d7b1b2 | -10.3205 | -49.9567 | 2026-08-31 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 738f9616-7d12-37b7-8fbf-5d0d640cc849 | -10.8025 | -50.6539 | 2026-08-31 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 82b5ee48-8825-3295-ae8b-9ff16705f58a | -17.2944 | -46.0056 | 2026-08-31 15:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 110.7 |
| e15b13b8-12a8-343b-8dac-598580dbaa9b | -15.2272 | -56.3921 | 2026-08-31 15:00:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 4982a137-802e-3231-812e-c85e16ac7ef5 | -11.1821 | -50.592 | 2026-08-31 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 86d39481-b7f6-315a-beca-3dfb17c035b1 | -5.9636 | -57.6704 | 2026-08-31 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 44bbd618-99c7-3d8a-8d16-da4b5dd60b07 | -11.1824 | -50.5706 | 2026-08-31 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| a86c6812-c82f-3e15-9915-75c79b760217 | -5.4876 | -57.1416 | 2026-08-31 15:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 32b9a624-82a7-3df0-8c59-18fab7cc4c63 | -14.2599 | -52.8782 | 2026-08-31 15:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| f94130bc-a9f1-3477-8b0d-44f88938490b | -10.7856 | -50.5066 | 2026-08-31 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 5749e45b-963d-3623-8550-5cc1f111ad71 | -6.9367 | -55.636 | 2026-08-31 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 01b54184-8218-3199-9aa8-3ab201e30e8c | -7.2934 | -60.5713 | 2026-08-31 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 99cb21bf-4be6-3de7-93a3-5ae35a0b93d7 | -5.8782 | -59.9917 | 2026-08-31 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 60f095e4-4a75-3973-bd1f-d2f59092aff4 | -14.1459 | -52.7871 | 2026-08-31 15:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 233159c9-3139-394e-a96a-bffd19b938e9 | -18.27 | -52.7068 | 2026-08-31 15:00:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 3f6fd947-f229-357b-a09d-0e14fe4008eb | -10.7405 | -54.0606 | 2026-08-31 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 4d2879b7-07c1-3572-8624-2a57146fb910 | -9.5967 | -47.5983 | 2026-08-31 15:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 4740c5f2-2133-3e28-9835-58810ba733fb | -12.9054 | -59.8857 | 2026-08-31 15:00:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| b7444761-4374-3ad7-ada9-118cf995cc53 | -14.8319 | -55.7194 | 2026-08-31 15:00:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 7e566163-9b95-3e31-9565-7adb10b0ab2a | -7.9797 | -44.2962 | 2026-08-31 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 245.4 |
| e8a5e5a4-4319-32f9-82da-02f54435faac | -10.918 | -50.5138 | 2026-08-31 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 0bfad84e-e285-3d8a-ba40-1146cb85036d | 0.1914 | -60.5067 | 2026-08-31 15:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 58a792fd-96d2-39cb-a380-e2fb53af2d90 | -7.9605 | -44.3212 | 2026-08-31 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 5c72873f-e758-36e0-97ec-69c101ec0102 | -10.3394 | -49.9547 | 2026-08-31 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| bdf1fcf7-7f8a-3083-b48a-5f88922096c6 | -18.2704 | -52.6851 | 2026-08-31 15:00:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 171.7 |
| bb4f9c00-3a60-39d7-ac8d-f9461b5f1d9b | -14.2792 | -52.8758 | 2026-08-31 15:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 31464d26-61a5-392e-83a4-24156560949a | -8.7579 | -45.3823 | 2026-08-31 15:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 2e32934d-0946-387b-b193-99a34489dd8d | -11.0747 | -51.5153 | 2026-08-31 15:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 124.6 |
| dc1cf5b5-093b-357f-a98c-c7f1c8a7f07c | -14.5868 | -54.1153 | 2026-08-31 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 110.9 |
| f64643d2-4332-36de-950d-eb896dbae7ab | -11.0054 | -49.6893 | 2026-08-31 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| e22ac4dd-bd1f-39c4-bb2d-1e79bbaab21a | -19.4907 | -57.5609 | 2026-08-31 15:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.0 |
| 4ff4ceef-d071-38ac-8c9f-3ebba7a40f47 | -11.3427 | -45.1751 | 2026-08-31 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.6 |
| e06bae08-4143-3cd2-9e08-afe5a6023211 | -14.5678 | -54.0968 | 2026-08-31 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 638f8077-848c-3509-8ad3-88bdd8d45e82 | -10.1321 | -45.8825 | 2026-08-31 15:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 1659690e-1b73-33b4-af44-3b0e0e6f20fb | -15.2478 | -53.8666 | 2026-08-31 15:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 93c8e084-c50f-3126-9f6b-2685e7241537 | -11.6786 | -54.5484 | 2026-08-31 15:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 4c2877f8-e9d3-395b-8569-0b304a1c9217 | -10.1084 | -50.299 | 2026-08-31 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 01c37a29-b603-3ce2-b275-571a9697766b | -10.7618 | -50.8707 | 2026-08-31 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| a183130f-48b0-39c4-b4ee-80fd64d50c7d | -3.6216 | -60.547 | 2026-08-31 15:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 616cac95-d1e8-35c5-b035-dfc133b2f088 | -5.2362 | -55.9112 | 2026-08-31 15:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 9208eba2-73d6-32e7-be58-3bff82832b0a | -3.6076 | -59.0769 | 2026-08-31 15:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| bf5cd4a0-7246-3efc-a52f-1f167d94406a | -8.7213 | -67.1014 | 2026-08-31 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 3862592d-010d-3dfe-9ca7-92c0653d277d | -10.5601 | -50.4022 | 2026-08-31 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 7ea46c37-0f86-3496-9625-2778ac4e54a3 | -18.2904 | -52.6818 | 2026-08-31 15:00:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 121.1 |
| baf861d4-84b2-3414-8e4a-7cc76fa5a1b6 | -11.0566 | -51.4539 | 2026-08-31 15:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 152ed97d-dd51-3e10-b1a0-a9868cb656b3 | -12.3814 | -48.1655 | 2026-08-31 15:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 17e05ad4-9804-3aa2-a6d3-45663e2fe1fb | -10.1087 | -50.2776 | 2026-08-31 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| ebe742c8-4bde-3480-b522-cc58a4d6d692 | -14.4007 | -52.5226 | 2026-08-31 15:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 8b922349-959d-39a1-aa38-e7bf9793250a | -10.7407 | -54.0401 | 2026-08-31 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 214.8 |
| 40b8f149-cd0f-3212-b54b-3e008afe04ea | -5.2548 | -55.8907 | 2026-08-31 15:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 157.2 |
| 1e224ab3-38df-3f6d-bb45-a0e3454d0321 | -11.3423 | -45.1982 | 2026-08-31 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 2b5b093a-8a6d-3f8d-901d-1e1e371990a3 | -19.4706 | -57.5636 | 2026-08-31 15:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 195.8 |
| e7f02762-e696-32b8-a0ba-0f8996ec4500 | -11.2295 | -51.2667 | 2026-08-31 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 5ef179f8-f460-3b36-a289-ca143ce49122 | -9.1906 | -51.546 | 2026-08-31 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |


[Clique aqui para ver as próximas entradas](README98.md)
