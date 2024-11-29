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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b2d53d4-ef07-3e06-8be8-fa7670ad956d | -17.62439 | -42.74715 | 2024-11-29 05:01:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 855c94ed-8440-3795-9c6e-f8bb737a15e8 | -15.52564 | -58.8093 | 2024-11-29 05:01:00 | NOAA-21 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6325c2d7-a2f5-38d1-a64a-a7b072709226 | -9.82094 | -63.24679 | 2024-11-29 05:01:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 13c215e9-28bf-38ce-a640-dfba40c47bca | -17.65201 | -57.57145 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 0ac6a3a8-1314-3736-8d35-45f441e5cf08 | -17.56516 | -57.475 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e872b3a1-8d72-384a-bac8-145bbbc439de | -17.57974 | -42.76358 | 2024-11-29 05:01:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 1fb5e739-77d9-38ce-b336-0fc74d228ff8 | -17.63874 | -57.56916 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 04795839-90ff-384b-9f65-209c3a60bfa2 | -17.70098 | -57.58338 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6e00f0a2-c106-372b-911f-a67194d8c89f | -9.82296 | -63.24973 | 2024-11-29 05:01:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9a367852-d604-3684-a37a-1d8f7830a281 | -17.63816 | -57.57279 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| d0785fe9-2c2a-37ac-93f8-d55756eb143c | -9.6169 | -64.69016 | 2024-11-29 05:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6111f92-7403-333c-b1ec-163c211c33a6 | -17.66585 | -57.57011 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 429e780e-828c-3947-b64a-02aabd3125a8 | -15.0949 | -59.63688 | 2024-11-29 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2d1bede6-09b3-3e31-93c9-99d105ec3e7d | -17.70429 | -57.58395 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3fa43cf2-449b-3faa-a617-a8906015c9fb | -12.10272 | -58.24131 | 2024-11-29 05:01:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 315fb54e-0c1e-36f4-942c-d51531ea391f | -11.36238 | -56.21712 | 2024-11-29 05:01:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5546306f-53c7-39ba-b261-d617c77f2a5b | -17.66311 | -57.56591 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e9f03bb0-79b7-30fd-9a56-39f36b709c0d | -17.58035 | -42.75643 | 2024-11-29 05:01:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c9dce3f3-6860-317f-92ff-2b11482f680b | -17.65909 | -57.59131 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c9fb27e7-8acd-35b5-b719-b7decebb422b | -12.31042 | -56.69614 | 2024-11-29 05:01:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8707d4d-4c30-33b3-8624-e0a623544fc9 | -11.4193 | -55.66041 | 2024-11-29 05:01:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d55289d-d87d-30db-ac16-46a06daf15a5 | -15.07621 | -59.63793 | 2024-11-29 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40bc5390-d358-30bf-b5a4-64153adca3e3 | -17.64205 | -57.56974 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 2b80c54c-bc52-3b00-8676-4cc0bff16a12 | -17.62376 | -42.75438 | 2024-11-29 05:01:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42c286b4-bf61-387a-a09b-52aeaeb52a13 | -19.55641 | -56.70867 | 2024-11-29 05:03:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a7f13682-0c89-3957-b8e1-2442b897583a | -19.15413 | -57.55646 | 2024-11-29 05:03:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 64c1edb3-39b1-3961-9d1f-c09dea35b619 | -20.11622 | -57.13911 | 2024-11-29 05:03:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e44d420-f99a-32c6-8478-40d0b4724a70 | -21.71876 | -56.64537 | 2024-11-29 05:03:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9cbb25c2-551f-3a9c-bc79-a58f5c5c979d | -21.57322 | -55.96725 | 2024-11-29 05:03:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 177951d3-269a-34e3-80a1-260b1854ab74 | -19.55585 | -56.71236 | 2024-11-29 05:03:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 72981d8d-7365-36f8-9650-a550b97ef05e | -21.57207 | -55.82824 | 2024-11-29 05:03:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad20e614-5878-344b-a37a-197132d84eda | -19.02497 | -57.62052 | 2024-11-29 05:03:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 650c054d-2f41-3714-a48a-78088c27e464 | -2.6684 | -48.7767 | 2024-11-29 05:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 151.8 |
| 90bf6ac3-0311-37eb-ac06-df1cc8228b31 | -1.5897 | -52.2915 | 2024-11-29 05:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 1b175f6e-f55d-32cf-9128-0a1ab6b1a12b | -4.7786 | -46.1131 | 2024-11-29 05:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 9656e014-6013-34f1-a16d-ab5d89835187 | -2.6683 | -48.7981 | 2024-11-29 05:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 166.4 |
| 3164a853-5c2d-3ab8-a0d5-859437f6c791 | -2.6499 | -48.7772 | 2024-11-29 05:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 865229a1-191e-36b5-a95a-e39f203e1a9b | -2.966 | -53.3027 | 2024-11-29 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| b676ea36-e106-3013-a40f-cc3062781784 | -3.259 | -53.6388 | 2024-11-29 05:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 5f591398-30f0-3cab-9fbc-9da033d79c01 | -2.966 | -53.2824 | 2024-11-29 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 2a8b6a6d-5b62-396f-843e-c3a89b44e75d | -2.6498 | -48.7986 | 2024-11-29 05:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| d51434f0-cf72-35b5-a2b5-cc75acf1d672 | -1.718 | -52.4532 | 2024-11-29 05:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 7c3965b8-c388-367b-8c32-b83a05f2aecb | -2.9844 | -53.2819 | 2024-11-29 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 142.0 |
| 2da10e8b-2e6e-3b2d-8240-90139f26114e | -2.9844 | -53.3022 | 2024-11-29 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| f9e35985-98d5-3d5f-b8fd-916a96a4ddde | -1.6997 | -52.4535 | 2024-11-29 05:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 127.4 |
| 4e29dcce-e51e-3f12-9ff4-557251119c34 | -2.6498 | -48.7986 | 2024-11-29 05:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 93c2493d-7bf7-39f0-8264-1de3f8475d3e | -2.6499 | -48.7772 | 2024-11-29 05:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| a1473aa6-364d-3ce0-8d81-599ceb02dd9e | -1.6997 | -52.4535 | 2024-11-29 05:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| c669d8b0-fa93-31c2-b81f-0590a5baa728 | -17.5805 | -42.7483 | 2024-11-29 05:20:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 64fbed28-a3cf-3c51-858e-75677e8fa211 | -2.966 | -53.2824 | 2024-11-29 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| e3727314-42b5-3db4-a0e0-308f2a5d11db | -2.6683 | -48.7981 | 2024-11-29 05:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 133.5 |
| e1b73200-d5f8-334a-a38b-476f6b288845 | -1.9726 | -46.4467 | 2024-11-29 05:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 397726e2-e160-3fd1-b4ac-bec4eae317e9 | -2.6684 | -48.7767 | 2024-11-29 05:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 2e19f3ef-e394-3db0-9606-4ee400c737b1 | -2.9844 | -53.3022 | 2024-11-29 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 88953a52-6ef4-3d7a-9121-ab2f41a60ed8 | -3.259 | -53.6388 | 2024-11-29 05:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 71af9723-78cd-3628-9e3b-d26e5130ac64 | -2.9844 | -53.2819 | 2024-11-29 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 151.5 |
| bebf7446-5666-3f36-a7e0-166ed64520a8 | -1.6997 | -52.433 | 2024-11-29 05:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 987fd646-1cf5-3fbe-86e1-4633d5857673 | -1.63461 | -52.27101 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9cb60cb9-e2d5-3954-98ad-9a4b193b5e7c | 1.21751 | -55.9465 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 15c39b61-d1cf-3a76-9969-5ab86b193c5f | -1.1604 | -53.54853 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a622b294-4030-3443-bb1c-4e8b1abc2cd2 | 1.23051 | -55.93625 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 55a8278f-7459-3f73-a33d-cc4298f69ea9 | -1.07385 | -53.63558 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2becebf5-0601-3289-a536-1242ae6333e6 | -1.16677 | -53.67329 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 667d4c8f-4e0e-3f16-b8f7-5d58fb77742b | -1.10933 | -52.3471 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dfd649ce-602a-338d-9c6d-768c9f78da65 | -1.5952 | -52.29297 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e54f2dd9-43dd-3843-97fa-330aca74585c | 1.99143 | -60.56258 | 2024-11-29 05:20:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee3bcb44-e9e8-3e7d-851f-5b4e70240a3e | -1.04267 | -52.41361 | 2024-11-29 05:20:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 486dea54-dc25-3a3a-ab3d-e51bce8fff9a | 1.45569 | -55.9083 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e40b7e81-9dcf-3416-a7fa-14797fdc97dc | -1.34312 | -52.13074 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3fa93f58-b744-371c-84ed-d02d4c78f2fb | -1.33486 | -51.92936 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0255c2d-d75d-3caf-aa87-5cdd1fd4dffd | -1.21588 | -53.55046 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f153d8ea-937a-347f-b25d-9e24b5419980 | -1.16613 | -53.67733 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ff7a52a-7ff0-39ac-a6fd-67da575ea873 | -1.31094 | -52.86594 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 176458ad-7715-3639-9516-77e8af3e7d51 | 1.67461 | -50.6666 | 2024-11-29 05:20:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 52c4f132-9f23-3472-a220-dce645c3224f | -1.09956 | -54.12431 | 2024-11-29 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a5788e80-f6fa-3686-b7a2-f1da0d9545c0 | 1.22107 | -55.94594 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec47e90f-01ea-366d-bae4-a77ca6bbc96d | -1.07315 | -52.33658 | 2024-11-29 05:20:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b73e3c4b-09e3-3f1f-86cc-f00d41b203b6 | 1.67876 | -50.65945 | 2024-11-29 05:20:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9ce978f4-d3ef-33d9-be64-23708899d239 | -1.34797 | -51.97158 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92d4f759-03c3-319e-969f-6d6b81d9bde4 | -1.24088 | -53.35749 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc6b8a19-c1c5-3708-b41f-22dc2379d25f | -0.95748 | -51.65271 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5318f4c8-bd99-3279-8329-d04cee311f5d | -1.0914 | -53.387 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c1226a8-6e00-3c68-b7c4-9dd768b28380 | 0.94006 | -50.7417 | 2024-11-29 05:20:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| abe7ad77-fe9c-349c-b88a-b04cdacbfbd1 | -0.14041 | -54.59729 | 2024-11-29 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f5398cc-3815-3f0d-8d00-be21c2692de1 | 1.22562 | -55.93773 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0b184345-54dc-3dec-a78d-ea3be0ef7735 | -1.62849 | -52.374 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 428354ad-8ad9-3e9d-aa51-612f6eae4dc0 | -0.7757 | -52.3917 | 2024-11-29 05:20:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d9f28582-95b8-3f78-9abf-427f059e583e | -1.10426 | -53.38907 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea80d1c1-8dab-31be-a1cb-e33344afefc1 | -1.22017 | -53.55085 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2dcf223e-aec5-3b6c-8594-fdcb16a8c1c4 | -1.21089 | -53.75191 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3336ad4c-5169-3ff0-a953-d3e4a346e74e | -1.23325 | -51.79922 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 56950224-39cf-3573-a917-3d46f03ac61e | -1.21957 | -53.55478 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 58f895e7-889b-3560-bdc5-0f4fe4bd55e9 | -1.36268 | -52.12875 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e910279-2239-39b1-97b6-59c1e3efc1ac | 1.30462 | -60.41068 | 2024-11-29 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6edb62af-12cc-31f1-a716-258ab52317eb | -0.24331 | -53.76145 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6d3b815-a4d0-3b8f-a7ac-5827a5a60b6f | -1.26413 | -52.19727 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f0cf302-bdf7-378d-a3e0-28863981a28a | 1.45925 | -55.90774 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7266c1c-6c5a-314f-8b1c-99a007507922 | -0.29308 | -55.87026 | 2024-11-29 05:20:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cff07b26-74f2-3662-94a7-5e92ecab6734 | -1.36757 | -51.97077 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a82d52b9-978c-34f2-8b05-6212289ec717 | -1.37494 | -53.63813 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README84.md)
