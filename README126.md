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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92f87b11-d0ab-33dd-940f-8997be012b88 | -2.09393 | -52.06326 | 2026-10-09 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc7fff56-c734-3587-a655-ae307a57b4a3 | -3.27745 | -50.39293 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e6d75d5a-6f10-3d49-98c5-93fbee2f4e99 | -2.50521 | -56.15386 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d446d0b1-5928-3592-94bd-2d9d815c2614 | -3.21807 | -42.96157 | 2026-10-09 05:01:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 043ab227-6f30-39e2-a483-dbed86c5c5dc | -3.16557 | -50.592 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0e2ef80-62a0-3172-8de8-8b243debb311 | -2.40477 | -51.29773 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 720e4d42-0184-3eba-abe4-18cd2bc54117 | -1.32786 | -56.39947 | 2026-10-09 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1929af2a-99d7-3222-b461-216a5b483961 | -0.99595 | -47.65281 | 2026-10-09 05:01:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3ec5694-848a-38ff-b6e9-e51f23ac5637 | -1.18648 | -55.67414 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e3f92f6-8a0e-33e5-9e60-b500b214f813 | -0.39107 | -51.77085 | 2026-10-09 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af6ab855-d9a8-30a6-a44e-92d6464cab85 | -1.51617 | -54.5185 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 63c01274-4f92-3483-a875-e35bf76faf7d | -2.78948 | -54.08257 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66cc0c0d-8c5c-3b5b-8af6-e68bba9a823d | -1.21437 | -55.64878 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d34fea32-0db0-353d-9811-ee1cd9200a94 | -3.15883 | -50.59095 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0832d1e-326e-393a-9bfd-0d37a2b6505d | -2.32684 | -48.48908 | 2026-10-09 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be50d771-7ca0-3f03-b2a6-62932a59cae8 | -2.18599 | -48.2474 | 2026-10-09 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 89a1499e-6ed8-3c54-bf0a-d9337a39edb1 | -2.13634 | -54.46668 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd39949f-3463-3323-8bee-1d49a846f83d | -2.4711 | -56.06781 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3caf50ff-2c61-3c23-b2fa-fbef34807824 | -2.08503 | -46.57716 | 2026-10-09 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 948c878f-7045-3823-a8ed-5f7d560c59a1 | -2.77197 | -54.07975 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17c46324-4e8d-3274-9c7e-351df9e43b0f | -2.84104 | -49.87873 | 2026-10-09 05:01:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ba7d084-de70-36d4-aadc-c11bb9742c83 | -2.75137 | -54.09631 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1304be69-358f-37ee-aa08-cf31afd0e473 | -2.45924 | -56.091 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f0c24523-ecb4-364c-8383-53aba5f06c51 | -3.0761 | -50.96453 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 865fe5a3-769c-37e7-af5c-311eb510c3e3 | 0.55204 | -50.89239 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a909324-3471-3f0f-8078-26ebea26dd70 | -1.6042 | -55.15947 | 2026-10-09 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba609532-69c0-3ad6-b383-957c1c7cb21f | -2.77258 | -54.07589 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed62cf29-4f60-3b5e-b98f-f617c563c3f5 | -1.48231 | -55.87321 | 2026-10-09 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 537998c3-a778-3de5-99d0-84443c444855 | -3.30145 | -49.12244 | 2026-10-09 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06a336a5-daed-3b45-bcd3-c8e0dea47358 | -2.78142 | -54.06545 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f2b63dd-858f-396b-9643-f0f81f56f17f | -3.27067 | -51.07003 | 2026-10-09 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06f1e2ec-30b2-3b6e-94f9-aba88d587f54 | -1.18725 | -55.66928 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1013ce4f-45bf-35d4-8d34-194d01b64a69 | -2.22729 | -53.69914 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3ee8ec6-98cf-33bb-b309-d1f462740f38 | -3.17343 | -50.58595 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff619211-f674-30e1-bea7-b4244fbef795 | -2.09726 | -52.06379 | 2026-10-09 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ba2920f-b406-31c1-b14c-5460863b1195 | -0.655 | -52.52561 | 2026-10-09 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1eb2ae2-1e5d-3111-a04a-55bab8328fc2 | -1.4243 | -54.62722 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f00b3193-b820-3f68-8946-897ab13177ec | -2.82792 | -54.1353 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1ea36257-12ab-3f19-9ced-7b711559b219 | -3.69484 | -47.6825 | 2026-10-09 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0bd8bb57-0ff7-3743-9c2b-d9df334313c2 | -1.47028 | -54.7616 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4cd1cf6e-0100-3903-b9d2-762243f46819 | -3.17846 | -50.5539 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3954af77-e986-368b-b002-bf18cae9de7b | -2.48659 | -45.6724 | 2026-10-09 05:01:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c18325a5-b7c8-3a2d-a61d-b4b32b4e046b | -2.84444 | -54.12204 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 855e9701-907b-3a4a-8522-42508e4f0a71 | -1.47819 | -54.64072 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac387683-904d-3128-acab-734badee51bb | -1.49644 | -54.5493 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f38c19b-1f13-3e59-870b-0a1134aa7524 | 1.23093 | -52.90339 | 2026-10-09 05:01:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d079c5d3-80f7-3ea1-9982-7ac3f475e942 | -2.75448 | -49.526 | 2026-10-09 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24776119-6e52-3b64-b60a-235d27be0ab2 | -2.95757 | -49.17686 | 2026-10-09 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 784fd9b0-c417-3f71-a64d-193e6eb303be | -2.5076 | -56.13916 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ffe294ca-02ec-3793-84f2-fc0fdbdbdbbe | -3.18073 | -50.58344 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4b7961b3-b7c5-3e66-a94f-6d67d67e2170 | -2.83494 | -54.13641 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce27da8a-b316-34b8-af8d-35ac66553195 | -1.32749 | -55.44176 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73680f6b-241f-33cc-9ea2-849ad129b6b0 | -3.34804 | -50.4076 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5ce9fcda-268d-3bf3-ae81-c1cd73ab32e8 | -4.15732 | -43.188 | 2026-10-09 05:01:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a60ac1b-1337-398a-9890-477df479f5aa | 0.55314 | -50.89929 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8739d11-7084-37ec-b01f-829cfcfdf0af | -2.46478 | -56.08499 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 330cd556-db31-3eab-ae93-c434957868cd | -3.17848 | -50.57579 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2bf1cd56-7f42-3a6f-91ee-1ce142fa7392 | -1.45865 | -54.52984 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b493227-4e60-3638-bc99-a04de9d1559e | -2.76477 | -54.10244 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96821486-d233-3916-98b8-a4f5d446f11a | -2.99815 | -50.30196 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 031d9af0-d22a-363c-8fe1-eb517d817b83 | -3.18128 | -50.55799 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdf1b739-3466-33ec-a756-0486f0a3edc0 | -2.7429 | -54.12676 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8dc1d964-d00a-3df4-a5f3-36a6fe9f1ddb | -2.73815 | -54.13396 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2bb6d6cb-b157-312a-95b6-e83d5bfac530 | -1.11252 | -54.17361 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f06add68-feeb-36a6-b987-f385c5ca378c | -4.08413 | -44.10871 | 2026-10-09 05:01:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c0eb091d-87ce-3c6e-a03a-e25cb189387d | 2.41669 | -50.82891 | 2026-10-09 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d3bc22b7-08f4-3f9b-9cae-accd28cb332e | -2.82337 | -51.28129 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b33cb46d-ea69-39db-8572-3bc508e0e915 | -1.52637 | -54.5245 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9186433e-b5db-30a2-a96c-75326fc433da | -1.40208 | -53.23248 | 2026-10-09 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef1639a5-69ab-3b14-8b43-b2f2297c5bad | -2.75487 | -54.09687 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 255c8340-f61b-3267-a430-a4cf1bb3d38d | -2.47489 | -56.09346 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c541ae99-b329-3ba9-9ff3-757890bd8f0f | -3.23723 | -50.17941 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff65d45b-e74e-388c-9f97-233ffdc636fb | -1.89453 | -54.67208 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ca85950-8b80-347e-b01c-ea3936e4303e | -2.83624 | -54.06135 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c182aa33-ac61-3e60-b9d6-c33bc89bb24d | 0.93857 | -50.19749 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79bbceea-ba4e-3344-bffb-d6ac4196015f | -1.2224 | -54.0948 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 169c5499-49fb-30fa-9fe4-d822fe52705c | -3.25852 | -50.39771 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98a96b07-fabe-3940-b34b-e0643b16e3a0 | -3.01142 | -51.01554 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 999e9159-a9a7-31de-84ad-ef54f4b56f64 | -3.20207 | -50.55758 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4696fc64-3618-3b2d-8726-02e39e28cbca | -1.10538 | -54.17241 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 25540a10-f3d8-36c2-bbf1-9b1ea5e9ea31 | -2.50559 | -56.25138 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ed3c0f31-4961-36ff-acc8-97f0600674e3 | -3.27945 | -50.08867 | 2026-10-09 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8eda4b8b-a1c2-3547-b883-aebe688c7fbe | -2.46865 | -56.06054 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9ea9c29c-b6f4-3082-9304-37d7f16e3d57 | -2.74951 | -54.10794 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b0e162aa-a849-301d-88a2-602249fcfdcb | 4.23244 | -60.8394 | 2026-10-09 05:01:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb96ee55-6ccb-3ca8-b106-b23ee0184fe9 | -3.32494 | -50.17766 | 2026-10-09 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31cd6a30-c4db-354b-9401-f6891742ef30 | -1.10602 | -54.16838 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25b69bdc-72fd-3034-8a7b-e496881b927c | -3.16545 | -50.4604 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a06ecc7f-46dd-3c96-8d45-4690e528545b | -1.80434 | -57.12213 | 2026-10-09 05:01:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c85a970-08f3-3728-aad0-9ab3bfedc83e | -0.85361 | -47.54813 | 2026-10-09 05:01:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 938f39bf-ebde-3a66-98dd-6964ad7c37e1 | 0.53598 | -50.89844 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01e3ec14-01c2-3902-97e7-65c5a3367076 | -2.07749 | -46.57241 | 2026-10-09 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b04daf0-5038-3527-baca-d03da3a3cc0e | -1.39179 | -53.23081 | 2026-10-09 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 868976ff-2560-3b27-87f3-bc3edd39e6db | -1.36991 | -55.60582 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e3c447c4-f904-3d41-be8a-cc5331f3d2b8 | -3.20826 | -50.56219 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd484793-a66b-3d32-a95d-2f39585a34e6 | -1.41549 | -53.23027 | 2026-10-09 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b36d33ae-de05-3e2d-80fc-a243b1e38233 | -0.99967 | -47.6534 | 2026-10-09 05:01:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cdd3c2a7-3369-3d82-9218-333e1f52f4a5 | 1.69625 | -55.60751 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0cdcebc-2d7b-3242-b6d4-3abab369c9d4 | -3.17454 | -50.57883 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4468982a-ac6f-3d70-9f40-e8b312e82bf7 | 2.76897 | -60.00321 | 2026-10-09 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README127.md)
