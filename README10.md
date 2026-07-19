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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e49ce3d3-08af-351f-95e1-00d5483cbcb0 | -11.98627 | -47.10923 | 2026-07-19 05:06:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba4f3031-5f35-3f4e-aa3d-e6d0b0802be9 | -10.69873 | -46.61881 | 2026-07-19 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 76099c7b-56af-355a-aef4-edd1721df623 | -9.17505 | -49.64003 | 2026-07-19 05:06:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 652ea27c-c046-3d39-8946-8aae5dab4494 | -13.6772 | -48.78567 | 2026-07-19 05:06:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 07302a70-11b3-3edb-82a0-1a5d8855a574 | -11.98581 | -47.11298 | 2026-07-19 05:06:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 436341c8-a5fb-38eb-ae44-2e5a11a68e02 | -10.90431 | -50.32373 | 2026-07-19 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8e2bf1bb-e6a6-322b-ad95-8d7716b88420 | -12.16217 | -59.7636 | 2026-07-19 05:06:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9425d8e6-c8eb-3dec-b831-e6e626b792a0 | -9.48204 | -57.32516 | 2026-07-19 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| baa3b784-6d8a-3892-8388-8c2dde8bb1e1 | -10.72185 | -46.57078 | 2026-07-19 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a3110b6-84bb-3b39-b6f3-39be4f5548bb | -13.67682 | -48.78875 | 2026-07-19 05:06:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| d514a6d1-0dd9-37b4-92bb-2ef8655c392a | -10.68918 | -46.6243 | 2026-07-19 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ec778c5-dcb2-3341-a5af-896466c07a02 | -9.66356 | -56.49482 | 2026-07-19 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59a0b85b-3827-363b-806b-3d06c5b63fdd | -9.47928 | -57.32111 | 2026-07-19 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ed7a2b6-8976-3377-a606-bd493052c999 | -11.77351 | -45.97702 | 2026-07-19 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 252ddee5-d4d1-3efb-bd72-49b0bf3e918f | -9.10456 | -50.61382 | 2026-07-19 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e1ea755-0ee3-3796-88e4-b9d8bf01a71e | -7.80547 | -63.83642 | 2026-07-19 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc05a229-116b-32f5-9b17-f2c117e7b5e6 | -13.67758 | -48.7825 | 2026-07-19 05:06:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| dc0f1b1d-a58f-32d8-a332-338a19386ece | -13.67177 | -48.7877 | 2026-07-19 05:06:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| aafb3e0c-5b11-3a82-94a0-6e59565cfe58 | -14.57108 | -52.08047 | 2026-07-19 05:06:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 19beee26-cfa5-3e94-a135-c24f6d8216e9 | -10.82153 | -50.23844 | 2026-07-19 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 146bd4de-41b7-36ca-9678-a1d310d633d0 | -9.09841 | -59.40412 | 2026-07-19 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c527c37-f250-3c30-b408-db450888f7b1 | -13.6667 | -48.78671 | 2026-07-19 05:06:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2853b5eb-b46f-3ec3-8976-0ef4fb0a43c6 | -11.99192 | -50.58008 | 2026-07-19 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b753f9eb-2b2d-3bd3-be68-ea1d219328bd | -9.09908 | -59.40003 | 2026-07-19 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6089299-c74c-3340-ba3f-3034a6a30699 | -9.08079 | -50.59595 | 2026-07-19 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6aa33247-f8f9-362c-9af3-d59f230d748a | -9.09613 | -50.61255 | 2026-07-19 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9f6eb11-856e-3a5c-b3c0-20727be2d921 | -11.64491 | -51.68017 | 2026-07-19 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c5fa815f-b1e4-3e01-9d33-9c8bb685d20a | -9.10035 | -50.61319 | 2026-07-19 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c088e60c-a719-3a7b-a6ff-29fc9d80d77e | -9.0867 | -50.58697 | 2026-07-19 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e974d1e-cde4-3aeb-a013-cc1a059929f7 | -11.38021 | -47.51498 | 2026-07-19 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0a24dd7-2d64-3520-adbf-3b76c6a1735c | -11.99252 | -50.5757 | 2026-07-19 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 102df7f7-92a3-3ba5-9fde-c2a2fdd2d2e8 | -10.70441 | -46.6194 | 2026-07-19 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a6ec6f19-7d12-360e-a3b1-f71b6b6dc545 | -13.67251 | -48.78151 | 2026-07-19 05:06:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 65c16830-9279-3276-bf44-5f10e39d66d0 | -9.95816 | -50.55376 | 2026-07-19 05:06:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cba8a439-5035-3c01-bd0d-976e88926c0a | -10.82657 | -50.23466 | 2026-07-19 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 57c7e4c0-6618-3ed2-81b7-96074473834a | -11.99187 | -50.57874 | 2026-07-19 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9e7fa23-913c-3761-91e2-91feb58efcd5 | -9.16123 | -61.40929 | 2026-07-19 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b52d8cd-4142-3522-a0bd-ce0ca811e0cc | -9.49887 | -46.66259 | 2026-07-19 05:06:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ecdbb99-7b05-307a-a6b5-5631b1584d37 | -13.35497 | -54.31447 | 2026-07-19 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8cdbedd-db3e-3790-85d2-ffb73c516162 | -10.69776 | -46.62683 | 2026-07-19 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 57d7d6ca-7cc9-3314-affe-a2d166741310 | -11.62954 | -47.95876 | 2026-07-19 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e28efb84-6f93-3958-ac95-bfd9d8178612 | -13.67106 | -48.79358 | 2026-07-19 05:06:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d65bcd77-f0a1-338f-a621-0f59cca65e69 | -9.4826 | -57.32163 | 2026-07-19 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73896150-8ae1-3304-9b3f-586d28f0f5d7 | -11.78677 | -57.01177 | 2026-07-19 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2b3424b-befa-35ea-8702-44a6b410f95d | -12.67237 | -48.21374 | 2026-07-19 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed4bad4e-6210-3739-9527-91bcb53674c6 | -12.66113 | -48.21873 | 2026-07-19 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8a5c779d-e5fd-3bb3-bb8a-eb20622547ce | -10.90754 | -50.33313 | 2026-07-19 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3949b45b-441f-3ee8-ae53-37aa99e21a9b | -10.70345 | -46.62738 | 2026-07-19 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 597d921c-006d-35ee-818b-c1c993abea04 | -11.38436 | -47.52558 | 2026-07-19 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2fe59f5-5633-3c56-a0fd-498a2ab26ea0 | -10.69825 | -46.62283 | 2026-07-19 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3eaf91d7-5423-3aa4-a263-3639e6040f2e | -11.99684 | -50.57497 | 2026-07-19 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4beb26c-4cf4-34a3-aa5a-242d766bdb51 | -9.87694 | -53.33227 | 2026-07-19 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4dafc581-1e67-3f98-b2aa-fdb68a6beda7 | -9.10089 | -50.60919 | 2026-07-19 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a3e9a55-2504-34a9-a7c6-bcd5e8609b58 | -13.67647 | -48.79171 | 2026-07-19 05:06:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 811a37dc-6e48-32d6-91f7-209a07c8c0d3 | -12.66595 | -48.22279 | 2026-07-19 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a7152681-f519-3eb0-af6e-25748e856c0f | -12.03896 | -55.45739 | 2026-07-19 05:06:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 36459a17-4a52-3a48-af9b-cc65a0c60515 | -12.07999 | -53.34765 | 2026-07-19 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| ec0406bb-8fe6-36ea-a5d0-d801da707a37 | -10.69211 | -46.62605 | 2026-07-19 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4844c5d-306a-3e98-9510-74c97b09c3ed | -9.95613 | -48.85783 | 2026-07-19 05:06:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 16973f64-3fdd-346e-a298-67c121a0e601 | -10.55303 | -56.32984 | 2026-07-19 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b2fc9da9-e37b-3ccc-9977-cf0bcfe42f2c | -10.90372 | -50.32811 | 2026-07-19 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6a79a2b0-6033-31eb-9af0-ec17937d2c87 | -10.91709 | -50.19476 | 2026-07-19 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 498f8361-5389-3db8-b52b-3b4303dad965 | -11.74295 | -57.80919 | 2026-07-19 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77ba3e15-cc98-3e6d-8966-7b420ce1ce13 | -11.97512 | -47.10775 | 2026-07-19 05:06:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4cb635e2-084a-3505-864c-3e0b763504b6 | -9.95561 | -48.85819 | 2026-07-19 05:06:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 1cc021cc-4b6e-38e6-a8cb-94f5a3f51b16 | -9.08563 | -50.59484 | 2026-07-19 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38a37cbf-7ef0-3926-a3f9-ac361b2b18fa | -10.69728 | -46.63081 | 2026-07-19 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 49e891af-de66-36a4-9b0e-b08ce2080866 | -10.70296 | -46.63136 | 2026-07-19 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 37b3512d-cb63-3968-917c-18106013575f | -10.69257 | -46.62216 | 2026-07-19 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7df40c7-eb8f-303a-8824-369660b7f481 | -7.81029 | -63.83727 | 2026-07-19 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16e4a4e5-e762-3030-9923-346018d740a1 | -12.67276 | -48.2105 | 2026-07-19 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1be76c94-2dc1-3935-8158-2afe8be5fd14 | -11.37896 | -47.52504 | 2026-07-19 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a045ab77-5b8f-3d66-b93a-eb282b4e3e17 | -11.68203 | -54.58358 | 2026-07-19 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b530021-4e98-3f22-99cd-12336d97491b | -11.97466 | -47.11153 | 2026-07-19 05:06:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b871b093-f815-3ea7-8024-f7b3899e5269 | -11.74627 | -57.80974 | 2026-07-19 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce928d9f-4709-3a6c-b1c9-58d22bf8210b | -10.89606 | -50.31807 | 2026-07-19 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32752da7-b7e2-315c-a131-f3af60c616d2 | -11.62994 | -47.95554 | 2026-07-19 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a648b1cc-7bec-3181-9523-994cb81b30f2 | -12.06007 | -58.04042 | 2026-07-19 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e25b952d-e7de-3f8d-963d-cb6fe9f068b4 | -10.89989 | -50.32309 | 2026-07-19 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b17b2a1a-f1f5-3f75-82e3-129604adaa27 | -12.0068 | -50.56745 | 2026-07-19 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03f6aafb-affc-3508-804a-b34767a1636c | -10.81829 | -50.22897 | 2026-07-19 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bdba1737-7f54-3efe-9639-d2e44ca1b737 | -11.68145 | -54.58749 | 2026-07-19 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5e32f8a-e881-314f-b574-5c8ad0585c55 | -10.69921 | -46.6148 | 2026-07-19 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ee4662fe-3791-3113-a04d-b4101e11d405 | -9.87842 | -53.33134 | 2026-07-19 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fe67b88-043a-3ec5-ba59-008891087e0d | -12.66153 | -48.21545 | 2026-07-19 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fd405704-7647-3f8e-b769-7f989081919f | -9.91679 | -53.39745 | 2026-07-19 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb9c5cd5-1e00-353f-8481-74fe48fb55b0 | -10.82597 | -50.23908 | 2026-07-19 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bdc4d06f-c255-3569-b9a7-b69ce874cb79 | -9.91703 | -63.06851 | 2026-07-19 05:06:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98613cda-31ae-3029-b79e-53eaf9b5720a | -11.74903 | -57.81382 | 2026-07-19 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5097b688-2f7e-3548-92fc-564bca7a4df2 | -12.00238 | -50.56682 | 2026-07-19 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17a496da-ad99-32fe-91a1-b537a466996d | -12.66754 | -48.20972 | 2026-07-19 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6988a6d-4fa0-380e-abe3-d333fba86f2f | -13.67214 | -48.78463 | 2026-07-19 05:06:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 7331d7a1-22ce-3a0f-b8e7-e0d1ee381195 | -10.82273 | -50.22961 | 2026-07-19 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0fb7b9a0-00de-3fe1-8ccf-ab5bdeed9f6c | -7.76703 | -63.85717 | 2026-07-19 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d76ec76-ae45-3ce6-9899-b457b67a213f | -11.98023 | -47.11226 | 2026-07-19 05:06:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6095c447-8a53-3b8e-8e8a-217dc0ae20ff | -11.64443 | -51.68381 | 2026-07-19 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 859de4de-260a-359b-82fc-48c66cf4a620 | -20.53421 | -57.39375 | 2026-07-19 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2943dcf5-efbb-3fe4-8e72-a903bcd35deb | -15.46347 | -54.35178 | 2026-07-19 05:08:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1dbf25e6-ec8b-3c33-9480-23beec06c45d | -20.56836 | -54.57316 | 2026-07-19 05:08:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d3b61702-1430-3265-834c-b802e7013cbd | -15.46285 | -54.35615 | 2026-07-19 05:08:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README11.md)
