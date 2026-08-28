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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fd5b027-c8e6-34f6-93c9-5ea160db8fc3 | -10.76233 | -54.04906 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0df13788-9825-36a7-95d6-bdae126d90b2 | -15.84181 | -56.45666 | 2026-08-28 05:12:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bdd8365-010d-3245-9331-d603dd9fcbc4 | -10.98467 | -51.09349 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d061bbbf-9246-399b-a8ff-e986fcf5360f | -12.29456 | -50.59813 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c84c8fca-6812-367a-92a7-4c1d83668d6c | -10.79709 | -54.01228 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 433e1121-dc32-375e-bb29-5d3b0f551150 | -13.46063 | -57.04783 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 458f24a5-a364-3740-9128-9eb7cb3a3d52 | -12.76167 | -44.26264 | 2026-08-28 05:12:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ae7ca6d6-e81e-328a-8d31-f558a7ff2fc5 | -14.99246 | -52.60785 | 2026-08-28 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5663f33-78f2-38de-b11f-f756ddf442a4 | -11.2797 | -54.01466 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abbaf97c-668a-34c9-ba9d-9cdbe85b06c9 | -9.87724 | -60.25909 | 2026-08-28 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf170887-922e-37a5-9f66-023c7b378913 | -11.76763 | -47.63558 | 2026-08-28 05:12:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be4a9628-ddaa-37dc-bf56-917fc9c543aa | -14.11971 | -44.38751 | 2026-08-28 05:12:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| abe704ff-f71a-3ede-a43b-dccc2faeb40e | -8.59311 | -70.21975 | 2026-08-28 05:12:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9b5fc0c6-3ff6-3820-8f30-ae455a86a673 | -12.27775 | -50.58647 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4de7df0a-a993-3403-8faf-ea66d1618c55 | -11.73902 | -54.52227 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fe7d2dc-28c5-3ff8-a083-8ec592d87d58 | -11.83624 | -47.21607 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc77431f-98b6-3cf6-9961-28beb46daf8e | -10.35161 | -64.46549 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| efffc177-e5dc-3550-b4e6-f69cefc22b5a | -11.72725 | -54.52872 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95388ca6-5533-3cf0-9683-7d7b1e099244 | -10.76209 | -53.97735 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 711caaca-d415-31e0-bb37-a095bdfd468e | -11.83059 | -47.21555 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 004f85d8-075c-3189-bf07-330d96c62316 | -13.60176 | -45.77971 | 2026-08-28 05:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24a3f01d-c57b-3db9-95d5-cfdb11ea6d7e | -12.42802 | -43.41294 | 2026-08-28 05:12:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 1d532ca7-f4a4-3158-af11-e118b1d620b2 | -10.76713 | -54.0414 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 534376e3-588b-35db-9b58-f87309ea8d99 | -10.57926 | -57.48576 | 2026-08-28 05:12:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3c3160d-716b-3f65-a20b-9e7387bec64c | -12.26033 | -50.57938 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| f0d98b9b-ec59-3ccf-b759-d466738de403 | -11.22161 | -53.9988 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 089b06bf-c7a3-3cae-bb0e-4a6cd2920af2 | -11.19798 | -51.23174 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 263e9e11-f743-3912-b2a6-12962523e919 | -13.41261 | -51.41135 | 2026-08-28 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| e8b36ad0-4f2e-388b-8007-61f55b6dd802 | -11.47811 | -46.94748 | 2026-08-28 05:12:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92b28358-d84d-38fd-9fc2-3dee3fa74461 | -14.86032 | -52.60843 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 04dba69c-7f5b-3785-ad33-91b5a1c8ec78 | -14.88618 | -52.59673 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4918371b-77c4-3fcd-80e7-47cb2437f11d | -16.15667 | -58.59834 | 2026-08-28 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.1 |
| b1f6d82a-b556-3848-852b-381b8c4942af | -23.82161 | -48.7085 | 2026-08-28 05:14:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 797b1668-11a7-388c-9c02-32c08dc35f3d | -23.53661 | -47.32063 | 2026-08-28 05:14:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fd9c2269-d87e-34cd-aae4-51723284229c | -16.15896 | -58.584 | 2026-08-28 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.0 |
| 9c637479-0c12-3aff-8fa1-ca6df21f9042 | -20.34064 | -47.59546 | 2026-08-28 05:14:00 | NOAA-20 | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c32d80a-ee67-3158-a6fa-9b4197cc5b4d | -16.16228 | -58.58456 | 2026-08-28 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.0 |
| 3cc60f31-9e4d-3dfa-8975-3fb01a4d37ea | -16.15336 | -58.59777 | 2026-08-28 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.3 |
| 184f1f2f-7315-36a4-9771-a44d1f1525e2 | -16.15508 | -58.58701 | 2026-08-28 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 8677fa06-f453-3b71-a1ac-007c31c8e98a | -16.16616 | -58.58154 | 2026-08-28 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.6 |
| ebcd611b-ca70-348d-b0de-4db24838e6e3 | -16.15622 | -58.57984 | 2026-08-28 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0615e614-c48a-32c4-8fa2-3a9ee311fef0 | -16.16011 | -58.57682 | 2026-08-28 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2ed43d41-8f03-3d94-914d-413348be460c | -21.54168 | -55.83688 | 2026-08-28 05:14:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99d5cbab-953e-3485-86c8-c861e1306e79 | -23.02522 | -52.66421 | 2026-08-28 05:14:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 137ad2d5-ddf2-3b51-b2de-8be9860333ce | -16.15061 | -58.59362 | 2026-08-28 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.3 |
| fde80d3d-2a39-3e1e-b87e-c89a84a9ec1e | -22.30399 | -51.51102 | 2026-08-28 05:14:00 | NOAA-20 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d2fe2702-515a-3de4-911e-5143eb8cab85 | -21.54231 | -55.83222 | 2026-08-28 05:14:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cd56951-e5c5-3ff9-8958-199b28688183 | -20.81736 | -57.32034 | 2026-08-28 05:14:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98525b99-97ee-3401-8b32-c7c1c0234cdc | -17.40599 | -50.81603 | 2026-08-28 05:14:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5cc843cd-5bb6-3900-89cb-6f8c67c37e5a | -16.16502 | -58.58871 | 2026-08-28 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 83501365-22db-30cb-83d1-9012b6a4fa17 | -16.15278 | -58.60136 | 2026-08-28 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 19a094c0-0866-314e-98c9-a97ebaa6b094 | -23.02571 | -52.6647 | 2026-08-28 05:14:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 7192978f-28c9-397d-b290-1be047df0035 | -17.25545 | -53.30905 | 2026-08-28 05:14:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a101a1d1-a6f6-3787-a711-da72018303f7 | -22.3011 | -51.50966 | 2026-08-28 05:14:00 | NOAA-20 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 24ee5da3-7578-3a90-8d43-5ced487ac298 | -17.57834 | -52.5573 | 2026-08-28 05:14:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cbb71195-6aa7-39bf-acd2-d23450c20181 | -17.59081 | -52.50038 | 2026-08-28 05:14:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b6a8a6e-7ed4-341e-8387-3a5be39518ae | -20.34023 | -47.60021 | 2026-08-28 05:14:00 | NOAA-20 | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6186f42-db19-39f0-af96-4f5ea869c0eb | -23.13868 | -48.67894 | 2026-08-28 05:14:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c660f37-6f68-38b2-8b42-b59571d0e019 | -20.82574 | -54.95358 | 2026-08-28 05:14:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8b0e311-c6ea-3385-8241-adc9698e3d40 | -16.15004 | -58.5972 | 2026-08-28 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.3 |
| ca91860f-e41d-3d8f-a6af-84657ae47c8e | -17.7753 | -51.72534 | 2026-08-28 05:14:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97cb99e6-d114-3606-861f-47cb4756bb8a | -16.15782 | -58.59116 | 2026-08-28 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 27.9 |
| 4fecb481-5cd9-30a0-b340-569c9972ad68 | -17.25594 | -53.30537 | 2026-08-28 05:14:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fd79077-d77e-3596-8f1a-a1d374287cdc | -16.15954 | -58.58041 | 2026-08-28 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.0 |
| aabe40ba-8256-30eb-9c0a-e9e9c67d6c44 | -21.53798 | -55.83638 | 2026-08-28 05:14:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0d82401-d48a-3418-8980-30568b2348b1 | -16.16056 | -58.59532 | 2026-08-28 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.1 |
| 99052104-63a2-327c-9729-ecde6c3b4ae3 | -16.16285 | -58.58097 | 2026-08-28 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.0 |
| 61db4d18-4777-33ee-a721-350409486dae | -16.16559 | -58.58514 | 2026-08-28 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.6 |
| 77eb4734-bd75-3ee8-be82-966e0de0efa4 | -16.15839 | -58.58758 | 2026-08-28 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 27.9 |
| def4923d-c5e4-3bde-9063-736b1031ae90 | -23.20613 | -51.73672 | 2026-08-28 05:14:00 | NOAA-20 | ASTORGA | PARANÁ | Brasil | 4102109 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3f640745-377d-3ad2-81fa-dec676e91468 | -23.54162 | -47.31797 | 2026-08-28 05:14:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6d511b8e-00d3-31d5-a645-dedc6fbce67b | -23.53703 | -47.31489 | 2026-08-28 05:14:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e691a057-1227-3b31-a545-1e4433446305 | -20.8244 | -54.95007 | 2026-08-28 05:14:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbd8b58a-c4b5-318f-b122-092f26a371f7 | -20.34593 | -47.59676 | 2026-08-28 05:14:00 | NOAA-20 | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a602171d-804d-3460-82ee-46886515da83 | -16.15565 | -58.58343 | 2026-08-28 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6b26af38-c6f5-3f6b-843b-90a8730f4564 | -16.16113 | -58.59174 | 2026-08-28 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 27.9 |
| 494a49b4-1ac0-307b-b34e-cd3e5d16a49b | -17.57888 | -52.55827 | 2026-08-28 05:14:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77be4b1b-8364-3400-8b55-6a55a3d7feee | -23.58112 | -51.63589 | 2026-08-28 05:14:00 | NOAA-20 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 8298e254-bce3-30de-9393-d071cb08c12c | -16.1473 | -58.59304 | 2026-08-28 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a378a6ba-202e-3743-8264-6fe2e6922772 | -20.33984 | -47.59617 | 2026-08-28 05:14:00 | NOAA-20 | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 502ca539-8009-3367-8597-736d84819306 | -23.82121 | -48.71309 | 2026-08-28 05:14:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f79239c9-c263-33de-8834-820aa36bc08b | -23.57623 | -51.63528 | 2026-08-28 05:14:00 | NOAA-20 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 7408889f-2584-32f4-8649-df7b18b6b687 | -17.59409 | -52.50005 | 2026-08-28 05:14:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ca2ed2c-0926-3202-98fe-5d1112ee68fc | -23.02978 | -52.66473 | 2026-08-28 05:14:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 9b8a1345-0913-336d-a316-7a2e351095fb | -16.15724 | -58.59475 | 2026-08-28 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.1 |
| 49d77fe9-698f-3fd0-9076-cfb237e465f3 | -16.14787 | -58.58946 | 2026-08-28 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 32998754-29b6-3b14-b3c9-84d4fbf3b0d1 | -23.57828 | -51.63651 | 2026-08-28 05:14:00 | NOAA-20 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 7e7caabf-9d4e-3c1b-9eb1-eec4bed78755 | -16.16171 | -58.58815 | 2026-08-28 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 27.9 |
| 34e7873e-6576-3c6f-a178-5baa98e90ece | -23.13278 | -48.67865 | 2026-08-28 05:14:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5b04195-e008-33ae-9a41-9eb8e5371675 | -20.41394 | -54.97268 | 2026-08-28 05:14:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 418bacd8-83bc-3fa5-ab9b-e7db46f52074 | -23.57891 | -51.63024 | 2026-08-28 05:14:00 | NOAA-20 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 68b60283-2d44-360c-b2df-d94749865954 | -16.14947 | -58.60079 | 2026-08-28 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| e6805fac-8e18-3783-8321-fbfa58ea2a5a | -20.8208 | -57.32089 | 2026-08-28 05:14:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 52e40086-522e-3f9f-b092-f20f54e073bd | -16.15119 | -58.59003 | 2026-08-28 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| ce40dfcd-6419-30de-8a2c-ba04bacc0dc6 | -22.30457 | -51.50541 | 2026-08-28 05:14:00 | NOAA-20 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3a536df3-f9fb-3275-82f7-8a89c024711b | -28.66574 | -49.91267 | 2026-08-28 05:16:00 | NOAA-20 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ef38dab9-9718-3589-864a-2594cf1db5e8 | -28.66677 | -49.89885 | 2026-08-28 05:16:00 | NOAA-20 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 9bba824c-5013-3b23-b00c-05131e6a163b | -28.66644 | -49.90337 | 2026-08-28 05:16:00 | NOAA-20 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| dc38adfe-65f8-3015-bdd9-e46feb4977db | -28.6661 | -49.90799 | 2026-08-28 05:16:00 | NOAA-20 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 01c3cd62-0a46-3d2a-a9ec-6c367361c76a | -28.67186 | -49.90862 | 2026-08-28 05:16:00 | NOAA-20 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README63.md)
