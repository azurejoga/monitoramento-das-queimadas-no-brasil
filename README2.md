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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 257d55a4-8e8c-3da0-8e4d-ff6915384b1b | -2.1945 | -46.5958 | 2025-12-18 01:00:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| e190b0eb-1816-345e-895d-35276ccff428 | -2.213 | -46.6174 | 2025-12-18 01:00:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 05f87349-1b5b-38af-aad9-5dcea564dcc6 | -2.1945 | -46.5958 | 2025-12-18 01:10:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| b82b25f3-b3da-3140-8fe0-0382032bda63 | -2.1945 | -46.6179 | 2025-12-18 01:10:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 08a04ea6-969c-362b-8fee-7cc561980758 | -2.2131 | -46.5954 | 2025-12-18 01:10:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| ffc8a615-6085-33b5-b344-2dbaddca5960 | -2.213 | -46.6174 | 2025-12-18 01:10:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 15c79e41-b41b-3a26-bde2-03fb0b0fad46 | -2.1945 | -46.6179 | 2025-12-18 01:20:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 59a92510-adfe-3ebf-a90a-c01595135fe9 | -2.2131 | -46.5954 | 2025-12-18 01:20:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 47fca38c-1082-3294-96a8-8e663471cd1d | -2.1945 | -46.5958 | 2025-12-18 01:20:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 10a10f3e-9af0-3739-bd47-a643526d4357 | -2.213 | -46.6174 | 2025-12-18 01:20:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| b7df6f5e-47ef-3c92-9e03-120fd33f3041 | -2.1945 | -46.5958 | 2025-12-18 01:30:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 265bb75a-1fb8-312e-bb77-09bcef93db81 | -2.213 | -46.6174 | 2025-12-18 01:30:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 4c3944f6-bc10-3362-99bf-1db53b3c70f7 | -2.2131 | -46.5954 | 2025-12-18 01:30:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 96b3b1d1-ea0a-3919-873f-96483423a11d | -2.2131 | -46.5954 | 2025-12-18 01:40:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| e2539aad-5d91-3244-b963-c2fac9cc7760 | -2.213 | -46.6174 | 2025-12-18 01:40:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 9b09b43b-629d-3cbf-8ed4-43f2a0783f3c | -2.1945 | -46.5958 | 2025-12-18 01:40:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 25ea623e-c121-3ed2-bf79-2205385785e5 | -2.1945 | -46.6179 | 2025-12-18 01:50:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 65c75200-7cac-380a-b04b-cfd3fc0a8d8b | -2.213 | -46.6174 | 2025-12-18 01:50:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| ad0834d6-3a1d-32e5-b5fe-262f9aa8abfe | -2.1945 | -46.5958 | 2025-12-18 01:50:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 1d007060-3fa2-3e95-bebb-41fe3c35a104 | -2.2131 | -46.5954 | 2025-12-18 01:50:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 28ad987c-29ec-348d-b0a8-0a96b7685a5f | -2.1945 | -46.5958 | 2025-12-18 02:00:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 3e02d84b-8534-3d05-987f-4d641e34b34e | -2.2131 | -46.5954 | 2025-12-18 02:00:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 087b1a3f-798e-36e0-ad1c-90778b8e6477 | -2.1945 | -46.6179 | 2025-12-18 02:00:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 737528fd-6c48-31a8-a6ac-b70d2b7c0e5d | -2.213 | -46.6174 | 2025-12-18 02:00:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| ed1cbb64-9e08-39d0-852b-5ec4a5866553 | -2.2131 | -46.5954 | 2025-12-18 02:10:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| ace5c6c4-705b-3155-a126-a1f61cff7a1a | -2.1945 | -46.5958 | 2025-12-18 02:10:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| c52c363b-b3af-37a1-890d-dda98ca48ea7 | -2.1945 | -46.6179 | 2025-12-18 02:10:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| e8c9610c-d9d1-3a88-8d98-dd75ad7f31ef | -2.213 | -46.6174 | 2025-12-18 02:10:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 9d5b07bb-c385-3d83-9282-893ec7255570 | -2.2131 | -46.5954 | 2025-12-18 02:20:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 3f57f2a0-1cb4-3721-b4a4-c4784387a739 | -2.213 | -46.6174 | 2025-12-18 02:20:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 342d32a6-da6d-354f-ab40-b7ad393dc0ef | -2.1945 | -46.5958 | 2025-12-18 02:20:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| abc1a229-cb67-32b5-93aa-cb99c8b3772a | -2.213 | -46.6174 | 2025-12-18 02:30:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 69645ad6-2ef5-308c-b5be-283a599d17ee | -2.1945 | -46.5958 | 2025-12-18 02:30:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 62cf45a2-f292-3bdf-854c-015c832fd808 | -2.2131 | -46.5954 | 2025-12-18 02:30:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 59449414-310c-30d1-8f59-db66c41bf54a | -2.1945 | -46.6179 | 2025-12-18 02:40:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 56296fef-eab2-3170-8ed0-0baeeb0c3d75 | -2.213 | -46.6174 | 2025-12-18 02:40:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 268c4b15-4bbd-3943-a5eb-504053b0c71e | -2.2131 | -46.5954 | 2025-12-18 02:40:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 700773d0-36fb-3dc9-bf6c-9d60d0afb640 | -2.1945 | -46.5958 | 2025-12-18 02:40:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| aa9bf1cc-076a-3e2f-9b87-bccfc0df49dd | -2.2131 | -46.5954 | 2025-12-18 02:50:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| fe91767f-9b78-3a0e-bc6f-321d9629d291 | -2.213 | -46.6174 | 2025-12-18 02:50:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| b92b0969-fdce-3468-aabc-948234165971 | -2.1945 | -46.6179 | 2025-12-18 02:50:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 0b74b847-1494-3a63-8914-1f2c615d0795 | -2.1945 | -46.5958 | 2025-12-18 02:50:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 5e5d008b-4843-350c-8ec6-1ccecc2438d7 | -2.213 | -46.6174 | 2025-12-18 03:00:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 1e13dfb8-c3c3-37d9-aa44-8c616a8520a6 | -2.2131 | -46.5954 | 2025-12-18 03:00:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 6e9ef72e-2609-3a3c-95eb-de910481d3bf | -2.643 | -45.6723 | 2025-12-18 03:00:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 01f2d754-b6aa-3c8e-8f66-7219316ec83f | -10.0677 | -36.1546 | 2025-12-18 03:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 78.7 |
| 86cf9536-c75d-3604-bf7d-9e1e8c2905da | -10.087 | -36.1511 | 2025-12-18 03:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 91.8 |
| 0296b7ef-c5c3-374f-b995-7b21b4b8716d | -2.1945 | -46.5958 | 2025-12-18 03:10:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 7f9ad519-bbf4-3b26-8874-f69b5c6fdd9c | -2.213 | -46.6174 | 2025-12-18 03:10:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| c7554661-4402-3c87-8f36-1079450a0ba8 | -2.2131 | -46.5954 | 2025-12-18 03:10:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 8cbf5682-cd05-3f2d-a6b5-09851c1a8be1 | -10.08419 | -36.15467 | 2025-12-18 03:17:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 78b7faeb-f4c7-33dd-801e-31bfdbf2edd0 | -5.28567 | -38.07428 | 2025-12-18 03:17:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8b979247-f162-35f2-b9e3-140feacf9f4d | -9.78734 | -36.2701 | 2025-12-18 03:17:00 | NOAA-21 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a300b2db-5dff-3629-b102-32b05c162eb7 | -8.46569 | -35.1063 | 2025-12-18 03:17:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 20e45dfa-e835-31d4-8bfb-e054a4a33bbe | -9.02805 | -35.64638 | 2025-12-18 03:17:00 | NOAA-21 | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0354cde0-a388-3f1d-9867-d9a28b383aa2 | -5.28507 | -38.0778 | 2025-12-18 03:17:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 176ff4ac-5bcf-3481-a969-0d8808a8cb61 | -10.08056 | -36.14959 | 2025-12-18 03:17:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 4e71ff6f-8bf1-35b5-b07b-89c49e9eddac | -9.02876 | -35.64229 | 2025-12-18 03:17:00 | NOAA-21 | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 250760fa-761c-3180-b931-e2bfd1f701b8 | -8.95785 | -35.70648 | 2025-12-18 03:17:00 | NOAA-21 | COLÔNIA LEOPOLDINA | ALAGOAS | Brasil | 2702108 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0c0a75d7-0166-3df5-8561-c71f01ae551a | -9.28027 | -35.90951 | 2025-12-18 03:17:00 | NOAA-21 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 80666615-f49a-35a1-98a9-6d3da623b583 | -9.28003 | -35.91357 | 2025-12-18 03:17:00 | NOAA-21 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| be2bc9f2-a31a-389c-9f7e-bcce526e9e39 | -10.61859 | -37.13603 | 2025-12-18 03:17:00 | NOAA-21 | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8d3528e5-f1b1-3ad0-8df7-011773b07d63 | -9.27956 | -35.91366 | 2025-12-18 03:17:00 | NOAA-21 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f0484859-a357-3cc8-9eab-8bc172b8f403 | -8.95805 | -35.42501 | 2025-12-18 03:17:00 | NOAA-21 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 215f51a0-b94e-3341-8b31-12ad5d3bbc7c | -9.28077 | -35.90943 | 2025-12-18 03:17:00 | NOAA-21 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 67d91482-a106-31b0-8774-903379d45d5c | -8.34744 | -38.91187 | 2025-12-18 03:17:00 | NOAA-21 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 446a7679-5b9b-31f0-a255-321a9b223651 | -10.08494 | -36.15038 | 2025-12-18 03:17:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 7632fb84-23c0-3ce6-98d8-37063969c7f2 | -11.15346 | -43.32402 | 2025-12-18 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 877f4ee7-dc8c-37af-8f79-2aebbd9e54f0 | -7.8161 | -35.2434 | 2025-12-18 03:19:00 | NOAA-21 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d81452c6-ecc4-3d58-8afd-050225d16b12 | -7.13842 | -35.21329 | 2025-12-18 03:19:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 130e9e8a-3706-306e-b650-90514eb923f7 | -7.05859 | -35.20082 | 2025-12-18 03:19:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 443a120e-74a4-3eef-9026-8887bf928f4c | -16.79462 | -40.30702 | 2025-12-18 03:19:00 | NOAA-21 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e3b26a40-620e-3d33-aca6-369d379e8e6a | -7.46053 | -35.09007 | 2025-12-18 03:19:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ba8aac76-79b4-32a5-9a50-2d50452851de | -6.4172 | -35.142 | 2025-12-18 03:19:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 888098a8-1dfe-3c70-9662-e76b00b72d6f | -8.1572 | -36.54351 | 2025-12-18 03:19:00 | NOAA-21 | JATAÚBA | PERNAMBUCO | Brasil | 2608008 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5a9a00af-7f95-3665-9d16-5cdfc7fb7dd7 | -8.42054 | -35.11404 | 2025-12-18 03:19:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a5434a4d-722b-3f3e-8a27-8f95e2a7de9e | -7.05356 | -35.20419 | 2025-12-18 03:19:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f9342f18-be21-36a6-a025-d45c9441864a | -7.8118 | -35.24275 | 2025-12-18 03:19:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 95988bf2-fb5b-39f9-a363-134f488eb7d0 | -6.99201 | -35.05826 | 2025-12-18 03:19:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 340399ca-380a-3314-b8dc-b9e33e3e3e6d | -16.794 | -40.3101 | 2025-12-18 03:19:00 | NOAA-21 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a8bfc01f-b1f0-35a4-a939-7d2e5aaa9a1e | -2.2131 | -46.5954 | 2025-12-18 03:20:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 4e72aede-cce9-3c8d-9602-6558545135a2 | -2.1945 | -46.5958 | 2025-12-18 03:20:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 8c58c047-fe4f-38b9-9237-c76bf1f619b2 | -32.35149 | -52.37085 | 2025-12-18 03:25:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 5.4 |
| 81d26857-aa44-36a2-b194-73445e053961 | -32.35572 | -52.37392 | 2025-12-18 03:25:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 11.1 |
| 446e522d-b08d-3327-9126-f730a053caa8 | -32.35838 | -52.37372 | 2025-12-18 03:25:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 5.4 |
| a77e84a8-5594-31e1-8101-8d5c2a8cb91f | -2.2131 | -46.5954 | 2025-12-18 03:30:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 13ee6c29-d5ae-39d4-82cf-425c12947115 | -2.643 | -45.6723 | 2025-12-18 03:30:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 8dfa9e02-5eaa-3b2f-99b3-d0f34e66458e | -2.213 | -46.6174 | 2025-12-18 03:30:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 6340ff00-be23-3cf5-8877-7a2d58bbf860 | -2.2131 | -46.5954 | 2025-12-18 03:40:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| c6f90c54-7f29-36df-b92c-67ba7f294824 | -2.21332 | -46.60969 | 2025-12-18 03:46:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eec980ef-ac89-39f8-9a14-9fa54122273a | -2.2012 | -46.60155 | 2025-12-18 03:46:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4ca157c0-14cd-39a6-b173-baa4f9f6990c | -2.25836 | -47.85878 | 2025-12-18 03:46:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9d5c574b-5191-33fb-8cca-2b3c7a092a72 | -2.19934 | -46.6128 | 2025-12-18 03:46:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d9679281-b2bd-3c38-a0ce-1c98a320f28a | -2.19976 | -46.60294 | 2025-12-18 03:46:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a25056f6-03e8-3dee-bf08-3385afecc06c | -2.21281 | -46.60537 | 2025-12-18 03:46:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 14a20472-cecf-33bf-9e97-fd738c221274 | -2.20533 | -46.60967 | 2025-12-18 03:46:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 214d570d-9d39-36e2-b302-6583c28092e8 | -2.20774 | -46.60273 | 2025-12-18 03:46:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 320e8679-a656-396c-a874-92f802aa0e5a | -5.80333 | -35.46716 | 2025-12-18 03:46:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a8183d94-bdb1-38e4-a3f3-3305f1dd98d6 | -2.20631 | -46.60404 | 2025-12-18 03:46:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 090a223e-0f90-3481-aaef-d05c1d232728 | -5.69608 | -35.33613 | 2025-12-18 03:46:00 | NPP-375D | EXTREMOZ | RIO GRANDE DO NORTE | Brasil | 2403608 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |


[Clique aqui para ver as próximas entradas](README3.md)
