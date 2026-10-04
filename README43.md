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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95095f7c-1d39-3764-9792-3c65b4ab6e5e | -4.27729 | -50.27679 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 7d82b16c-e2a7-3607-a185-4bb95d6b3126 | 1.94138 | -50.91519 | 2026-10-04 04:55:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57bae917-ab71-381a-931e-959c3602e298 | -3.18323 | -54.0998 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d44b5ff3-fc00-3e22-98e0-8bee78f06977 | -3.1363 | -53.73006 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3123a3c5-9ebe-3e21-9e53-6248da2771e0 | -3.16477 | -59.08974 | 2026-10-04 04:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab2dbb53-f08a-3b8b-a2ac-20bffd38ce12 | -2.96927 | -54.08992 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ddbaea2f-5e73-311e-a622-379b5b4d3825 | -2.75068 | -51.55249 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5d523bc-ddfd-3e9f-b561-e1c7631891bc | -2.79546 | -54.11126 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8655cff0-b0f9-364d-8eae-555d1ae36656 | -2.77186 | -57.69728 | 2026-10-04 04:55:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 324290aa-54d7-3a7e-8671-f462d3eb5a38 | -2.80536 | -54.12228 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2172088c-8e06-3c3e-8922-076e65ff3e20 | -3.17868 | -54.08054 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6fd18077-af35-3cb4-a7a5-1c5a8888220e | -1.49609 | -49.44936 | 2026-10-04 04:55:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8e79c5dc-9ec1-3a65-80af-0db9d0da3df0 | -4.28836 | -50.27143 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| e71e691f-13a9-3601-bfe8-ee1b62ad888b | -3.30543 | -53.84472 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88e92eed-c961-35f7-a4bc-cf8bb51341c4 | -2.95978 | -51.51177 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b875f592-8edc-361e-803b-f0670429c9ca | -3.475 | -50.08995 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5dd4f67a-7a72-35ee-aaea-588fe970d743 | -3.09448 | -51.10079 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc20fcd5-627c-31f4-8af6-968890672c03 | -3.30914 | -53.84531 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c4a2476-3eab-3aa4-bd63-b50bc6424725 | -4.29001 | -50.26104 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5095742-398c-35ec-8086-35ebe7cde42d | -3.15833 | -53.06993 | 2026-10-04 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc550919-8721-380e-aa0a-e849e4132014 | -3.10913 | -53.74447 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| de5c9f8c-bb9e-3b74-9dc9-f2e4de9c7db0 | -3.04661 | -54.20829 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0397501e-be47-3933-a1e8-9800f5170079 | -4.14946 | -49.69353 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c811fd2-4757-33c4-af1e-3526abf8eef2 | -2.61551 | -51.21706 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e89d1a3-fed8-37f2-b108-7511b8fcb971 | -3.16369 | -59.09622 | 2026-10-04 04:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36f453f0-0d99-36d0-bb57-ac5c89006da7 | -3.06837 | -49.53542 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| af2124c7-c04e-3a57-8c6f-4207669eb6fd | -3.17747 | -50.53572 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a97a6f13-1d38-3835-98f0-2c2a15cebd59 | -2.58459 | -51.86966 | 2026-10-04 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c064704c-ebb1-3024-bb9a-1e98daeb0cd1 | -3.18784 | -54.09839 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0354ec19-932c-3ee8-9ab8-7958d204beaa | -3.29495 | -49.51384 | 2026-10-04 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c2981b6-4182-36aa-ad9e-cd13ba02362b | -2.93156 | -54.10726 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 627623f3-1367-3249-8d92-2596cffb0b14 | -3.13785 | -53.74369 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95820771-817f-3b7e-a054-d9c1ca8b2652 | -3.51375 | -54.61631 | 2026-10-04 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 08c13783-6114-3bb6-94e7-cc1082b163d2 | -2.94181 | -54.18925 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8cfa7862-f410-3bba-ac44-53ff2ad9f3e7 | -4.27893 | -50.2664 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| d6f0dbf7-e52b-3c15-be06-019fd96c3e04 | -2.97262 | -53.26917 | 2026-10-04 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89121a77-a757-37a2-b216-f82112a48e44 | -2.93654 | -54.19784 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbac0830-18b3-302c-beb2-693fc545df28 | -3.06558 | -49.53141 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6d7e57f-fb1c-3ebe-9a39-ff79e3607566 | -5.54672 | -44.21695 | 2026-10-04 04:55:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8642f8d1-c076-3bfd-a368-1979488efc7f | -3.03974 | -54.20245 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c4bc96d-792f-37d5-99df-9623bcf62be0 | -3.2761 | -54.00355 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c559ba5-c02a-3d2a-80cf-2eb81af0b394 | -2.84639 | -54.13366 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f599502-08bd-36b9-b077-d497aabfabc4 | -2.61214 | -51.21653 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e920d112-5362-3d67-8955-14d8d7e94367 | -1.16881 | -49.27002 | 2026-10-04 04:55:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d0ef811-512b-3344-abd9-38812b1ae0c3 | -3.05321 | -54.16685 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1ca527a-2993-3653-87be-4a76cc6df093 | -3.15897 | -59.09207 | 2026-10-04 04:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a108a36-d9e7-345b-bafa-448778d97dff | -4.80154 | -48.22062 | 2026-10-04 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8fc8c43-6eac-3c9f-b4db-63d3a96a26e9 | -3.07395 | -49.54344 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 855f8a87-393a-3b09-87b4-353d21fe8ef7 | -2.92326 | -53.94333 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b765f95-0b4b-39f3-b5ce-2ce9aaa204ec | -3.35662 | -43.37872 | 2026-10-04 04:55:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5881eb60-7346-30e7-8436-0674f0ee8d90 | -4.2674 | -50.74339 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b46ece0-a9f7-34d7-b42a-2ed55401d9bb | -3.1808 | -50.53624 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2a23ec0a-adb4-32d4-96fc-2954838dece7 | -3.51838 | -54.61218 | 2026-10-04 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6602952-1d5d-37f5-976e-573203fbfc40 | -2.95281 | -54.1202 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ee80cf53-5908-309a-903d-e6085de34dd8 | -2.24963 | -51.93112 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14241c18-3a22-353c-af87-b6b4ae309be3 | -3.30242 | -53.83974 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e9a86c55-9c07-3179-9d11-00fb787c7995 | -3.51992 | -54.60262 | 2026-10-04 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a38d839b-99cc-3d06-b705-25d938a914f8 | 2.35188 | -50.75064 | 2026-10-04 04:55:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a88fd59-39fa-36e7-a03a-72a876326115 | -3.04354 | -54.20306 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb55a016-aa43-307b-9294-fe44d323db5a | -3.1207 | -53.71956 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 6ea96a12-7e5e-31a2-8e4d-8f8c121c2330 | -3.47168 | -50.08942 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 7ceaa580-8422-3b11-8005-98abd25d0b97 | -1.62323 | -55.01769 | 2026-10-04 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eabe02aa-8644-37dd-a0cc-f84efd395317 | -3.7643 | -49.56517 | 2026-10-04 04:55:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 8163d183-7959-33aa-8058-45174bc7454a | -2.9303 | -54.16361 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0dd50b8f-1bca-3944-ab9d-f341629274bf | -2.81665 | -54.10054 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| df9be5ce-2ff3-3512-93de-2e0853e95511 | -3.61385 | -55.50937 | 2026-10-04 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50c2477b-870d-366d-9385-4502dbcf2673 | -1.16658 | -49.26256 | 2026-10-04 04:55:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 87f29338-fbb0-32c2-bf2a-d5f0ebec0eca | -3.00087 | -54.17744 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f605981-0d19-3526-9974-ec1d706ba1bc | -3.04587 | -54.2129 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5d289f92-d292-3417-9737-517f0dee6c65 | -3.19001 | -54.10564 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e087bcd-3e14-346e-b69f-785557ca5c11 | -3.13189 | -53.73381 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf251e00-b0b7-3953-9792-757b58341450 | -3.27141 | -50.02975 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51d6fdd9-faf5-3f40-b233-744532a1fea8 | -1.27633 | -55.41201 | 2026-10-04 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc49b9f7-4179-3b04-9f8a-55574f70939e | -2.77998 | -51.36998 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 762055b3-e628-3a2f-9a51-e64cd47a62fe | -3.05774 | -54.16285 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 26a001cd-6327-354f-855d-3a8b32868037 | -3.43183 | -49.84541 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6be736a-6ecc-34dc-90f0-59de63940e91 | -3.28686 | -53.84174 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c63119ee-5dbe-3c05-b280-da2141e27669 | -2.5984 | -51.84929 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c6604fe-b5ae-3ed2-afa9-0239f1a047f6 | -4.46825 | -50.97048 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d69d34ab-fa8a-3889-a541-151da6245f05 | -3.1817 | -54.08565 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5bbb2fe8-50e1-388b-9e96-df496da3c1bf | 2.01432 | -61.09127 | 2026-10-04 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 140a6a35-94cc-3723-9939-340e45ec8366 | -2.82655 | -54.11158 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 64e5c5a9-9d89-3960-aab8-1ad0d48b114b | -3.71238 | -50.66299 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f27a9e3d-277b-32f7-973c-b952a7d9052f | -0.49483 | -49.10736 | 2026-10-04 04:55:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f741cc65-967c-3fa2-af46-528e22f47140 | -3.27163 | -54.00742 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8ef8a28-8d90-3008-b37b-b6f1685ec7a8 | -3.30844 | -52.9704 | 2026-10-04 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 414dd728-48ed-3cb7-8156-8bff2233f10b | -1.48497 | -49.43344 | 2026-10-04 04:55:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25da74ac-2a89-3dcb-bb78-bd9da4289b4e | -3.47613 | -50.1043 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 408b6f67-d4f0-3169-913c-e477df1a952c | -2.90134 | -54.12587 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f5c88f8-3514-383b-9954-225103ea4983 | -3.27537 | -54.00803 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9301838-5674-3014-9fa0-dbe05275d3a7 | -3.12232 | -53.73319 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a8bc02c-04e1-3411-aba4-632482b60184 | -4.27011 | -49.98449 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f194dd7-d9f0-30b6-9a6f-bebcf75b2af4 | 1.03725 | -50.02221 | 2026-10-04 04:55:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa751ed8-fde3-31ae-a0b8-074565dcf8e0 | -2.58518 | -51.86599 | 2026-10-04 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cfe17eac-5bb9-378c-b19b-cb6033b2e5fd | -3.09504 | -51.09728 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f0ee17b-6764-3742-b361-fa66bd52ee9a | -3.07654 | -51.27856 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 767224b1-5083-340e-a6d7-30d59acfba12 | -3.18444 | -57.86447 | 2026-10-04 04:55:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e773e4e-614a-3f59-99b6-240fc8eec625 | -1.24967 | -55.87966 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e07a2b9f-e2ea-360a-9543-42c639212ef7 | -3.05654 | -54.16594 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e4e67b1c-1860-377f-ac74-68d6e2598850 | -3.18774 | -54.09595 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README44.md)
