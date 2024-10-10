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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7aca3e5e-f977-3228-a943-ad474eacbbb8 | -6.64139 | -55.38188 | 2024-10-10 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15260c00-cef3-31f1-beb2-8de4f7992270 | -6.63632 | -55.38123 | 2024-10-10 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 819f51fd-7155-3c04-a67d-84fb0d157205 | -6.56187 | -55.3973 | 2024-10-10 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ce96ccd-881f-31fd-92bb-1949901edadb | -8.52206 | -54.97754 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34db9f1c-b52c-3a85-b2c5-5072c74737cb | -8.52051 | -54.97586 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fc24b5f-7890-35f4-a866-6e73235a00d4 | -8.52006 | -54.97936 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3bdf39f-bc1b-3ef3-b30b-b3357edc4417 | -8.49566 | -55.17075 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9cbb869-34e5-3172-8eca-30353486951e | -8.49555 | -55.16957 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 056bbc54-a5b3-3e03-a35b-fb291b9c1ca2 | -8.49083 | -55.16678 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 88338f4d-ef29-335b-9728-99856a38a64e | -8.4907 | -55.16555 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9df1431d-f518-3c0d-bbbc-e95334434fdb | -8.49038 | -55.17009 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3fe6730b-9af0-31d6-abb1-f4167084186a | -8.49026 | -55.1689 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e5cf66a-5d18-38dd-88ab-8cecf851af0b | -8.43859 | -55.47143 | 2024-10-10 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 947c6b1d-34af-312a-a416-edc4086ea9a9 | -8.43817 | -55.47454 | 2024-10-10 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f856b858-1c47-368b-9c96-8e6f301beb57 | -8.2904 | -55.38506 | 2024-10-10 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b66d3e2c-8d35-3b6e-ac6e-a0e3805bb68d | -8.28999 | -55.38816 | 2024-10-10 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd41e88b-1325-35a1-8e3a-27bcd94a8965 | -8.28957 | -55.39127 | 2024-10-10 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6927b31-e283-38e9-877d-5864a9a7ccd7 | -8.28522 | -55.38429 | 2024-10-10 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b6946d4a-fc34-3385-b3a7-169f6ce80c4e | -8.28481 | -55.38739 | 2024-10-10 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ee692aa-3a10-3510-addb-9427cf8d51f9 | -8.28439 | -55.39051 | 2024-10-10 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df207e0f-a509-3c4e-8de2-c9bc7d7b078f | -8.27963 | -55.38663 | 2024-10-10 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e220463d-8da9-36ad-9479-83eb0007b960 | -8.20535 | -55.25788 | 2024-10-10 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 256410d7-1e55-3403-b8db-810b6169800a | -8.20014 | -55.25706 | 2024-10-10 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa35b242-dedb-31b3-af04-1b115bf14a6d | -8.14082 | -55.18007 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 636f9912-36b4-32a4-9405-e8c46b3d4709 | -8.13645 | -55.17283 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05663b83-ade7-32d1-be42-81f4a392cbd0 | -8.13601 | -55.17607 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c14dc8b-4a96-3cbd-a1e8-56cc15a0e57a | -8.13557 | -55.17933 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9042a5c4-78ed-3d5f-8e21-6707bb3a4ae5 | -8.07685 | -54.77934 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf817c10-8f97-3107-9acc-549cb62c389d | -5.07425 | -56.23275 | 2024-10-10 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dcaf5943-3f95-36e4-ad7b-6c740f9b0690 | -4.90099 | -55.90794 | 2024-10-10 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bab1d789-af76-3b91-b740-a628d6ad9d26 | -4.86264 | -56.0062 | 2024-10-10 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4859b0ab-3cac-3fe4-9dc3-3e77ef441f3a | -4.85865 | -56.00035 | 2024-10-10 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5459fa4a-99b7-39e2-a82f-0ddd6cba6d83 | -4.85788 | -56.00577 | 2024-10-10 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd23b5ad-f2d5-3961-a661-585a2d6903f1 | -4.8373 | -55.80707 | 2024-10-10 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce0d2b5e-d6af-3c0a-864e-393e062045f5 | -4.83325 | -55.80138 | 2024-10-10 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ae1577a-6bb4-3c4c-a3b1-68dead714e6e | -4.82428 | -55.89554 | 2024-10-10 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b5f172b-2a78-39eb-b54f-563b9dadec7f | -4.66553 | -56.10997 | 2024-10-10 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bc307786-82cd-3be0-a412-bff7d8017670 | -4.66087 | -56.10916 | 2024-10-10 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6eec1157-5bb9-36bd-a543-e4c438396b0f | -4.6067 | -56.12117 | 2024-10-10 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a1d7949c-f6be-3d5a-a14b-4e3e166e5650 | -5.33799 | -55.90014 | 2024-10-10 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1373d1c-df69-37e1-a9b5-d50d119e2fb6 | -5.30017 | -55.99398 | 2024-10-10 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b032d439-aebf-37f6-b587-41790f12d56e | -5.20206 | -56.02907 | 2024-10-10 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77f0b5df-55fe-3772-b38a-7179d85743db | -5.20133 | -56.03411 | 2024-10-10 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a95a8f04-b5c6-3806-8783-80ccb8254a17 | -5.19731 | -56.02842 | 2024-10-10 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9e02f6a4-28ba-30a3-9e0f-696f9c415515 | -5.13042 | -56.0124 | 2024-10-10 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 95cc0e51-96f7-3fb7-a9cb-4b779766af9d | -5.12639 | -56.00688 | 2024-10-10 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fbd9afc3-8e41-3abb-bfcc-ddc8517d1121 | -6.47519 | -56.02372 | 2024-10-10 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5da7ea46-efaf-30b3-a2ac-8c4ac68bd94c | -3.14537 | -57.06227 | 2024-10-10 05:36:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2229891-a3e6-3ace-82a7-84e9591498b9 | -3.14111 | -57.06158 | 2024-10-10 05:36:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c674dabe-1621-3a2a-8f65-6fb893070f59 | -3.12285 | -57.61346 | 2024-10-10 05:36:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| abb2a2f8-883e-372a-962a-4a2a9b97e419 | -3.7777 | -56.99986 | 2024-10-10 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ccb1c17-7db8-3683-a442-721efc90c850 | -6.47855 | -58.43217 | 2024-10-10 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5b18ae47-31f5-35e4-879c-7ec74dd9dd25 | -6.47802 | -58.43577 | 2024-10-10 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1ef0a3df-36da-3f9d-b406-d56eb26780b9 | -6.47392 | -58.43518 | 2024-10-10 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f39b957a-08eb-3b77-bb55-c03a3aceb6b8 | -6.46984 | -58.43454 | 2024-10-10 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 184bba83-7af2-3bd9-8895-11c7ed36f123 | -6.8152 | -59.03699 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f6ea94f2-0518-3984-ab37-10e8248c72c0 | -6.81002 | -58.98911 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b53e258e-38b6-3956-9221-c67128409dfd | -6.89328 | -59.05072 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e157f497-789b-3e66-b991-23d62828535f | -6.52441 | -58.40506 | 2024-10-10 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba1c2639-47bd-3710-8362-63360bcacd00 | -6.5203 | -58.40449 | 2024-10-10 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a25540dc-86a1-3bfa-a682-e5ecde497214 | -6.51565 | -58.4076 | 2024-10-10 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74f721e5-fcb8-36ec-9851-17d41d15f013 | -6.48675 | -58.43326 | 2024-10-10 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b60721f-a3eb-3283-aa88-3c4ea3582c3a | -6.48265 | -58.43272 | 2024-10-10 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f15c8e6-c1d6-35ee-bebd-c2d5154d56f7 | -6.48212 | -58.43633 | 2024-10-10 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72ee6333-409a-3224-86b2-ab92f0218be3 | -6.48159 | -58.43994 | 2024-10-10 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 362c17f1-dd32-3444-83b4-ac134ac0a5da | -6.91947 | -57.77826 | 2024-10-10 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b5d0b637-0f7c-3742-858d-b59ce5de4512 | -8.12142 | -58.03695 | 2024-10-10 05:36:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 90dd5984-9fb3-3a8f-b6a0-b04e272e6e2d | -8.12085 | -58.04105 | 2024-10-10 05:36:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0a14094d-b72e-346d-a321-6a408cbcd4f6 | -8.12028 | -58.04514 | 2024-10-10 05:36:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f8475161-dded-38e7-b872-25c2faab2b1a | -8.11711 | -58.03637 | 2024-10-10 05:36:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d580c6bd-09f7-36b1-8999-e0722ce6d836 | -8.11654 | -58.04041 | 2024-10-10 05:36:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 03a775d2-653e-39c9-b3cd-93718f611cd4 | -8.11599 | -58.04445 | 2024-10-10 05:36:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a2316558-cafb-3068-ac6e-6a3cfe3ceba8 | -8.11279 | -58.03577 | 2024-10-10 05:36:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f353b928-3c92-37a7-bc16-ba2b5deff0b9 | -8.11224 | -58.03978 | 2024-10-10 05:36:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3d5d877c-073b-3eac-b637-4279411f07bc | -8.11169 | -58.04376 | 2024-10-10 05:36:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 26b4b170-8015-39b7-8472-8b43162025ea | -8.11 | -58.03744 | 2024-10-10 05:36:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bb976801-da06-3619-880f-c5ed2cf99969 | -8.10942 | -58.04142 | 2024-10-10 05:36:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8df2659b-a1dc-3dee-8da1-ce63d3d117e6 | -8.10884 | -58.0454 | 2024-10-10 05:36:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 162a3fc2-be8c-3eac-a400-0a748051625c | -8.10794 | -58.0391 | 2024-10-10 05:36:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7c42f1cb-bd9b-3438-826a-5f38d8d6684d | -8.10739 | -58.04308 | 2024-10-10 05:36:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ac4f937b-533f-3956-98ee-60ccb9347dde | -3.50691 | -59.65054 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6883aa0-1d3a-343c-a0c8-a2310dff76b5 | -3.43688 | -59.88906 | 2024-10-10 05:36:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c2e46f9-3111-3d5b-bed0-232facedc314 | -3.42301 | -59.63765 | 2024-10-10 05:36:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f07c469-1d9b-3bc7-8c38-10e8d6a873b7 | -3.42254 | -59.63873 | 2024-10-10 05:36:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db6f4fa5-9eeb-37bc-ace5-b8e124704178 | -3.20836 | -59.37582 | 2024-10-10 05:36:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d29a316-b481-343c-b5c8-d65b691b167e | -3.20769 | -59.38019 | 2024-10-10 05:36:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 259274e3-ff12-39a1-8c9a-7794c09d982e | -3.15164 | -59.57459 | 2024-10-10 05:36:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf1cd52d-ecc9-3117-b0dd-a806127bef18 | -3.14449 | -59.10904 | 2024-10-10 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7483b15-7c9d-3e58-aeca-a40a9a0a2d65 | -3.14075 | -59.10848 | 2024-10-10 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e65c379-7907-3c2d-8976-15ba7a78ad0a | -3.018 | -59.1012 | 2024-10-10 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9c1682c-fdb5-3657-a0f7-cd926d0de836 | -3.01426 | -59.10065 | 2024-10-10 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec655002-7cdb-3034-8647-51086036d7bf | -3.01357 | -59.10516 | 2024-10-10 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 343ff3c3-0900-305e-99e7-9f3f2f0a4e5a | -3.01289 | -59.10962 | 2024-10-10 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5355892-1d0e-3f01-936b-53108e03a5d0 | -3.00915 | -59.10904 | 2024-10-10 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 230be218-337c-3d88-873a-99906e780ec6 | -2.77511 | -59.58361 | 2024-10-10 05:36:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 618de7b0-81d9-3582-b711-e3ea3d2b6570 | -4.52552 | -59.89854 | 2024-10-10 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3cbe00c5-044e-3e3a-b61f-e02126a6f59c | -3.96515 | -59.17023 | 2024-10-10 05:36:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51e01965-7da1-37c7-ada8-3defc94aec37 | -3.96447 | -59.17481 | 2024-10-10 05:36:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44eceadf-acaf-3745-9e67-5a129ef4a1ae | -3.96138 | -59.16966 | 2024-10-10 05:36:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fda04681-1cc9-3ba6-88e5-f86c95bc9185 | -3.89691 | -58.79768 | 2024-10-10 05:36:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README130.md)
