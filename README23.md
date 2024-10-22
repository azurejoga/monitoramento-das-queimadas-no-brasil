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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a29a52a-6f69-38e9-808d-5644d14cfd7d | -2.47548 | -49.10598 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 140e17a2-1fd2-3477-a139-d782fd263b87 | -2.47428 | -49.11334 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb9b3541-7a29-3c36-a551-4509bd1f1a08 | -2.46847 | -49.09735 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80f77815-efc0-37c5-aff2-36f48a2f0407 | -2.46437 | -49.09669 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cbb1677-8362-379c-a6da-c4e76e5a8951 | -2.4312 | -48.5368 | 2024-10-22 04:19:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49c68b6f-99f0-3560-b940-2ca7d2b17204 | -2.41645 | -47.82158 | 2024-10-22 04:19:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 268cf436-6cb9-352f-b494-ac8964494784 | -2.41583 | -46.17628 | 2024-10-22 04:19:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8427d145-cbc2-3276-95d1-e1a0b734d366 | -2.39603 | -50.80481 | 2024-10-22 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2d71030-df13-31fb-a5b9-8bb062536020 | -2.39212 | -46.10198 | 2024-10-22 04:19:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 97033368-d6f4-36c5-ba2d-feaee265cb9b | -2.3895 | -47.72338 | 2024-10-22 04:19:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 921371cc-251c-3027-a6cb-aaa451581d87 | -2.36451 | -46.47549 | 2024-10-22 04:19:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdd9d23c-56c0-37d0-bea0-2724b3686a8d | -2.34181 | -46.5043 | 2024-10-22 04:19:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e04e0d6-d15e-32bc-8ec9-04fa080c24f1 | -2.33637 | -46.51559 | 2024-10-22 04:19:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c80608d0-e681-33aa-b677-dc63ecb752e5 | -2.31172 | -50.4776 | 2024-10-22 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c86b762b-3ced-3881-a198-33e550dc5d8c | -2.30721 | -50.47686 | 2024-10-22 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5dbbe24-298f-3b39-ab5e-7779f57a72e6 | -2.28629 | -53.73488 | 2024-10-22 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6c38b21-512e-3a40-9a22-fa764f43c69f | -2.28566 | -53.73864 | 2024-10-22 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f24c57ca-7912-301b-93f6-c93e56a7f07d | -2.27801 | -47.91176 | 2024-10-22 04:19:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c872025-d8cf-311c-9223-d33c846959e9 | -2.27136 | -46.74493 | 2024-10-22 04:19:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90daf06f-4817-3fae-9382-2207684d46b2 | -2.27033 | -46.7281 | 2024-10-22 04:19:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5afff07-e89d-3d2e-a373-a518dfd4bff4 | -2.2697 | -46.73217 | 2024-10-22 04:19:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 771b29c7-6b54-3a06-8fa5-d9edaf171a54 | -2.26962 | -46.06415 | 2024-10-22 04:19:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97642929-a6fa-3144-9ff6-17770640d1ff | -2.26842 | -46.74028 | 2024-10-22 04:19:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d93dcb9e-4ea7-37b0-8fff-56c7c9caa6e3 | -2.26615 | -46.0636 | 2024-10-22 04:19:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebf652b4-6cfb-363c-baca-b053eb3255d2 | -2.26485 | -46.73972 | 2024-10-22 04:19:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3322a7cc-727c-306e-ae1b-c91039f14222 | -2.26329 | -46.77293 | 2024-10-22 04:19:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a14d479-618a-322b-9dcd-8e1ab3ceb5cb | -2.26127 | -46.73915 | 2024-10-22 04:19:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20d90340-20f6-3608-a6ea-bd09f6afc775 | -2.24345 | -46.78236 | 2024-10-22 04:19:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a38528d-cc1b-379d-ab6e-03331d656d40 | -2.22219 | -50.45827 | 2024-10-22 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2404d73-034d-347e-aec9-57077aabfaa9 | -2.22041 | -50.46023 | 2024-10-22 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac6c4fbe-ec85-3984-acb7-35106bd58c3d | -2.21588 | -50.45954 | 2024-10-22 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0993f7bc-1cba-32db-a443-7735bfc64fd7 | -2.20666 | -46.48864 | 2024-10-22 04:19:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f33fa8d6-c58c-36ea-bca5-6079f82067b1 | -2.20064 | -46.43487 | 2024-10-22 04:19:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29b086a4-2678-372b-b191-3edb122c24fa | -2.19889 | -46.71683 | 2024-10-22 04:19:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6084f5f8-4f7d-3228-82ca-c2c62140f17e | -2.19531 | -46.71626 | 2024-10-22 04:19:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54d0543f-84d4-3852-a034-03b4a90ac270 | -2.18751 | -46.7192 | 2024-10-22 04:19:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d13e68f-2002-3ad4-a041-6fc105e88b65 | -2.1862 | -46.72734 | 2024-10-22 04:19:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e704b1d2-ef99-3eb7-b02c-5e35b2b0e475 | -2.18328 | -46.7227 | 2024-10-22 04:19:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36bcc1f4-dfdc-37bd-ac1d-e3127d5db06b | -2.18263 | -46.72677 | 2024-10-22 04:19:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 815407a1-d537-3f6d-89ce-f1457beaf28c | -2.18197 | -46.73085 | 2024-10-22 04:19:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ffb7228-fb4c-3858-8f1d-09ee9bed9505 | -2.08584 | -53.23257 | 2024-10-22 04:19:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9737ce6a-1c0b-390b-95ec-b2f335971f3e | -2.08526 | -53.23616 | 2024-10-22 04:19:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 174334a5-8f67-3e9e-90d1-86fdc18437ba | -2.02153 | -47.05155 | 2024-10-22 04:19:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aac11fb5-8aa0-34cc-932d-59941e005d64 | -2.02095 | -47.05264 | 2024-10-22 04:19:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cc8e7bdf-39da-3e0e-b406-9f0f67c324ba | -12.21744 | -47.27231 | 2024-10-22 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 71efbcf4-975c-3e9c-b276-e0a128fe1a89 | -12.21685 | -47.27593 | 2024-10-22 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 706b5d41-d473-39ec-bc67-5a9ab3cea583 | -12.0718 | -47.98869 | 2024-10-22 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f25e1bc-0b7b-3c67-81e2-946a4005bdcf | -11.63843 | -58.61559 | 2024-10-22 04:19:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1713369d-d9d2-3fb8-8b77-c45dc6827bf9 | -11.63367 | -58.61217 | 2024-10-22 04:19:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a122cc6-a566-3a42-ad5e-2642a43a02d5 | -11.63252 | -58.61789 | 2024-10-22 04:19:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37907e00-1dd7-3859-84d8-fdeba798102b | -11.63188 | -58.61429 | 2024-10-22 04:19:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34a1c17c-5c8b-3357-ac8d-8944afe07cca | -10.51936 | -57.59636 | 2024-10-22 04:19:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e60a8630-97b4-3d20-81aa-fc431d38e31a | -10.51835 | -57.60149 | 2024-10-22 04:19:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cc75a0a-059a-30dd-baeb-0eae42143e08 | -1.97684 | -48.68548 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 465d5415-bfe2-3c09-bc8c-791604cfbef4 | -1.97627 | -48.68897 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bcee0cf-8163-3f43-889a-21f60308b984 | -1.97562 | -48.68494 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 026430f2-17e5-3730-9858-e4ce9a5e996e | -1.97507 | -48.68843 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b66a58a1-ca36-3103-9629-ca91ff246ea9 | -1.82887 | -48.58992 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e00992e5-e374-3bb0-b292-94b36d570bb0 | -1.2359 | -53.38275 | 2024-10-22 04:19:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fef47ba-77e8-39e6-a082-5989d49401ad | -1.17648 | -53.66206 | 2024-10-22 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d124a578-1d35-3183-b146-ad3ee655578a | -1.17586 | -53.666 | 2024-10-22 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 93349137-a40e-34cb-8a9b-13fdc048f231 | -1.17523 | -53.66996 | 2024-10-22 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b157f938-9241-3604-95e0-9babcec0f974 | -1.17258 | -53.66153 | 2024-10-22 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 714a151c-f5b6-31e9-85dd-73a91de8f338 | -1.17193 | -53.66547 | 2024-10-22 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 695aaedf-ac89-3e6b-9d9c-d2184d8dd5f8 | -1.17128 | -53.66941 | 2024-10-22 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cada5db6-726b-356c-92d1-c109789541f2 | -1.17072 | -53.66146 | 2024-10-22 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 03ecc543-a529-3ec7-bfa7-a828739aac3e | -1.1701 | -53.66534 | 2024-10-22 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c18fca05-4763-3b79-84cd-193b3e4da6fb | -1.16949 | -53.66922 | 2024-10-22 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 076c9e92-05c0-3720-82f6-fa9a541a4ac7 | -1.16692 | -53.66032 | 2024-10-22 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76157620-2651-350d-86d5-0452c80c5a43 | -3.84596 | -46.48288 | 2024-10-22 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c217d44-e705-393a-8945-fd132ce63b2f | -4.62411 | -39.67262 | 2024-10-22 04:19:00 | NOAA-20 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0f5ebd1a-c2e1-3c82-8f6c-9db6f165fef1 | -4.46443 | -42.90077 | 2024-10-22 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec5a70a7-cacd-333c-ba9b-79b457e2a2dc | -9.92738 | -44.5857 | 2024-10-22 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1f6a8f9-3dc5-3b12-92b6-382c91e6bec3 | -8.89607 | -44.22933 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a596a60e-3843-32c6-b3df-bbda73d86c0c | -8.89328 | -44.22527 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e18cb980-346e-3cc2-ab58-fa7ee01191ee | -5.24171 | -35.55443 | 2024-10-22 04:19:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 6d97b6db-adfb-38e3-be0e-36f97f7d418d | -5.24124 | -35.55767 | 2024-10-22 04:19:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 655ba015-f92d-3303-8a4d-d03d483cc4fc | -5.23646 | -35.55365 | 2024-10-22 04:19:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 881778a7-e2e4-3bfd-83e0-5e7f99fe2211 | -5.23599 | -35.55691 | 2024-10-22 04:19:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f7c3bbe3-c55b-3889-8b18-b1ec6fc66ef1 | -23.40627 | -46.55685 | 2024-10-22 04:21:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a6e3ef00-462a-3be0-b6e3-eda97331cdf5 | -23.33749 | -46.76904 | 2024-10-22 04:21:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e24ce62a-0a6b-348b-9630-e80aac0724f2 | -23.3369 | -46.77304 | 2024-10-22 04:21:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ee45dda8-2cd1-3ee3-9ad9-e1bcdbfea83b | -22.90271 | -43.75454 | 2024-10-22 04:21:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ee53a4da-24cc-379e-a77a-6f4f733370d9 | -22.90267 | -43.75253 | 2024-10-22 04:21:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 088d1538-cfdf-3e30-8c6f-b49073e8aca4 | -22.54097 | -48.81236 | 2024-10-22 04:21:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f674d3f-cf42-3925-b610-f2ade4272326 | -22.30424 | -41.88134 | 2024-10-22 04:21:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 61d0d933-250a-3e00-8ac7-134cec135524 | -22.18387 | -53.27686 | 2024-10-22 04:21:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 86a3e64e-0774-3b16-b8da-5e72609be3bb | -20.51519 | -54.64524 | 2024-10-22 04:21:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd8959c8-6132-33d5-960d-5dc9fd913d78 | -19.54765 | -56.65984 | 2024-10-22 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b4577502-35e2-3cfc-bddd-52a6352ba013 | -19.547 | -56.66293 | 2024-10-22 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5978ee73-37c1-3568-89b4-eed06777a181 | -19.54569 | -56.66911 | 2024-10-22 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b1f901fc-f9b4-3df5-985f-f0fec94a4a9d | -19.54199 | -56.66175 | 2024-10-22 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| cbb60b4f-a2a7-3f5e-a8ce-1fe5e562c326 | -19.54134 | -56.66484 | 2024-10-22 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 433f2f2e-3935-3dab-9d49-193851a58bd0 | -19.54068 | -56.66792 | 2024-10-22 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 68c1f6e5-5b60-3943-97c5-439f55c99491 | -19.53976 | -56.65417 | 2024-10-22 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 009e001f-2957-3ecb-babe-7cec9d3511c6 | -19.53786 | -56.66347 | 2024-10-22 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 110fd2f9-94f1-313c-b741-bedc81594be6 | -19.53723 | -56.66656 | 2024-10-22 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 7148e013-a7f7-34f4-b0be-56e85190101b | -19.53633 | -56.66365 | 2024-10-22 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c7bd60f7-35d5-30f1-b178-89382ddb1125 | -19.53567 | -56.66674 | 2024-10-22 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2123f0c5-2dad-34b7-a241-1f6587ec1b13 | -17.97857 | -52.79655 | 2024-10-22 04:21:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README24.md)
