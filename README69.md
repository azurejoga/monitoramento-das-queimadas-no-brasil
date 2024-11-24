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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf966cdf-d383-3188-8904-5d189023b816 | -3.23673 | -54.2263 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ab6442e-3b1d-322c-a333-d12df8ee6581 | -2.81248 | -54.02551 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9f040b60-58f3-3ae8-912a-3345d3d4312b | -1.73494 | -52.72406 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0d942098-a6f0-386b-9fda-7de4045b3127 | -1.25396 | -53.32242 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 526fb681-6a84-3c48-a00b-71cc52b2dbdd | -1.46715 | -46.03877 | 2024-11-24 05:14:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41b4fcc4-98c2-372d-9e0a-2718f3de391e | -2.84194 | -54.01107 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be201e55-eb17-39a7-8b32-78b9c7048315 | -2.58399 | -54.23126 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 09c2459d-34a7-366b-924c-6f1d56b6ff4b | -2.82029 | -51.79639 | 2024-11-24 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f441f701-6d4b-3418-9c1b-34a2a3867bd5 | -2.92771 | -51.45115 | 2024-11-24 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bd1c130-357a-3fc5-98ea-cae38add0340 | -3.8618 | -50.05756 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 060c5d77-30c6-3b64-9870-e84334277f7d | -3.49902 | -50.46444 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e80737a2-0f0d-3dc5-9eac-87dc3332ad56 | -2.57734 | -54.04973 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f5a528f2-d1a6-32d7-a676-8953f41757d3 | -2.75239 | -54.11468 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4935af4a-6492-3c4d-9b45-c80179ef736a | -1.513 | -54.40969 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 887ce8e0-95f2-34e0-94f9-ae6576440e9d | -1.42847 | -53.38155 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 131ab220-73f7-3735-946c-7d7820af5ff7 | -2.76099 | -54.08339 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 58bdba6d-e19f-362c-97b3-387c18d403ce | -1.48369 | -52.52109 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54667614-a757-3136-be14-2877e61c83f8 | -2.73934 | -47.53629 | 2024-11-24 05:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3ec2189-8f2b-3a55-957b-3d61c347bf12 | -3.05592 | -53.21913 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d0a5cdc4-9dab-3717-9a12-edbe4c297602 | -2.45553 | -49.09142 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b5480cd4-1075-350e-90bd-530573a790b9 | -3.20283 | -52.57234 | 2024-11-24 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebb8557c-1c3f-39cb-a16f-06b9f48ff117 | -3.07014 | -49.20246 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1dd3b0ae-ec7f-3f24-a857-1ad2a89b30d6 | -1.19263 | -51.77181 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2d0ea239-a9eb-34f0-96a7-9dece10f24d8 | -2.56533 | -54.00141 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 51d667e6-4311-37ca-ae34-6029cc5b0c0f | -1.06551 | -51.75343 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8d928835-592e-3e70-aba0-88f36bcaee73 | -0.95034 | -51.64671 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96b6a57b-c542-3f53-8e14-0c40a6de52f5 | -3.2498 | -53.28113 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9a946780-3a30-31f3-8109-38b7951270c8 | -3.43937 | -50.01838 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8cc21670-3a48-3f18-a11b-8a4ed58a0bde | -3.70473 | -47.60061 | 2024-11-24 05:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ada6c754-01ff-342a-93e3-56bb449aa294 | -3.47869 | -50.43403 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79a0645d-272b-34bb-b657-a8bf9c020d13 | -3.22813 | -53.92562 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 80beae01-4bd2-39c7-bc02-33e01c742b72 | -2.82388 | -54.02722 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1f6e558-9df2-3c1a-bec6-dc7e05ec77ed | -2.00862 | -51.17178 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b486fb88-31f2-3d74-b7ef-d94a365f5ea7 | -1.45939 | -51.12016 | 2024-11-24 05:14:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| debf0a14-0ce9-30ca-9975-a0295a2951ea | -2.74087 | -54.39194 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c7e2ecd-02c8-3a8a-8c3c-3e8f8ffcb435 | -1.94748 | -49.52468 | 2024-11-24 05:14:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29568695-bcea-3277-bb22-6ba466017c58 | -1.60213 | -52.58683 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 217456c5-ae43-3223-b991-14b30e637da6 | -3.13297 | -45.37671 | 2024-11-24 05:14:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e47f2371-978a-3d00-844a-2286cdc06d3d | 0.08664 | -51.48834 | 2024-11-24 05:14:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1976a6ae-ee3a-3138-a2bc-d66adf441ef2 | -2.82768 | -54.02779 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d71608a2-5f8e-3759-89fc-10a7c8b9694e | -1.06776 | -51.75429 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| afeb5e3d-dd5f-3df8-a05c-9e843d87f6c2 | -0.96792 | -51.71826 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c399ef0-2ddf-373f-8fee-d13cf000e882 | -1.61807 | -55.13349 | 2024-11-24 05:14:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ebd2cad0-8ffb-330c-b812-c4e5a294190f | -3.03763 | -49.45611 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4b92d72c-ef95-33d4-ba5b-01f112a22e8a | -0.74644 | -52.4143 | 2024-11-24 05:14:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c7022e7-d880-3761-a469-9d3d52fee8d1 | -2.69512 | -51.7966 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e92a0d04-fd8d-3642-b972-d0558f982d27 | -3.48233 | -49.90474 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7dafb99a-95a7-3323-97a5-968ea0e3d695 | -0.91028 | -51.64879 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 713fa672-de4a-32ab-9f16-2de08aa90a9f | -2.28458 | -53.63305 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 006dbb30-358f-3f66-b0ed-598f87e1d739 | -3.2917 | -49.90818 | 2024-11-24 05:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87b0f5c6-2310-32c4-b98a-954f5be2b2d6 | -3.19375 | -54.33036 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93d4f0e3-dc58-34d1-8bd8-a25e290447ae | -1.53182 | -52.45378 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbcfde99-1ea8-3d45-8e4d-947386212e53 | -0.96363 | -51.71759 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5bf66055-3f3a-39f8-8087-0e23bd25d498 | -2.17063 | -53.78453 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0269242e-f56d-33ce-9c2f-74324934524e | -2.62651 | -53.98244 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d074e098-2421-3490-9237-b0b1851b85b4 | -3.61194 | -47.51277 | 2024-11-24 05:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 49b884b8-c8c5-35a8-9dc8-01044d6a0def | -1.07442 | -53.36941 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 838fd9cc-8c5f-3cd7-820a-510b73cb8d98 | -1.22572 | -53.68572 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 80b98a2b-c80e-3a15-bff4-5991ef5a7a4f | -2.58842 | -54.22739 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9f8f08bc-1a5f-3770-a684-6cbe2b44f25d | -0.28402 | -51.60464 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| feab2cfa-0a19-3cd2-867a-75818ab7ddf3 | -2.80939 | -54.02032 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ffdc645e-b0de-32e5-9a54-6560ad5106ea | -3.2928 | -50.53932 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91025fa3-e3e2-37de-bea0-058c1c5ae6e1 | -2.20776 | -53.67013 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 154c1456-07be-387c-bb44-05e40dcbb654 | -3.0594 | -53.22314 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6d92f950-4651-3fac-84f7-084ede27a233 | -3.07568 | -49.19666 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 718b8212-d001-3f79-8fca-9703cf9c3a69 | -2.31564 | -52.17128 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50b31aff-c1cb-3ee3-92ee-4cd5237d7d4e | -2.4493 | -49.09707 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4300fd44-b476-3bc0-ad2e-21b23b471c76 | -3.23127 | -53.93085 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf3622ed-1d06-396d-82c6-7259450d1113 | -3.1757 | -54.32287 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d628c4d1-a71f-33e1-b157-b5354fc6dc97 | -2.86109 | -51.27846 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c7185da-0522-3b54-9c53-fcacceeb714c | -2.57354 | -54.04922 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d616fee9-c704-3338-a352-0a73f32132c8 | -0.92016 | -51.64202 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f8ed426-e623-3f91-8458-e4d299247c73 | -0.98571 | -51.71696 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7994137-8f7b-3966-832b-b20cae055636 | -1.94474 | -49.51911 | 2024-11-24 05:14:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62584806-83c0-3dff-a83c-f6699c077a09 | -1.4027 | -54.25553 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11eddd36-7cab-3e82-b3f7-4de68039b150 | -2.88302 | -53.96238 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5a7e758-5696-33a2-b59d-4ce667bd4a1f | -2.99687 | -53.73245 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1726e21-db1b-3b91-b350-0098fb2402c8 | -3.06536 | -49.19842 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 165577ed-ea4a-3130-9186-135a18ca1758 | -3.13364 | -52.98172 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e512d20-6885-387a-acc6-25d1d0fd3ba3 | -2.86752 | -45.83761 | 2024-11-24 05:14:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 37b8fb1b-7fdf-3d26-ae5c-acb1079dc0d6 | -2.58491 | -54.05084 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fd4196b9-83cd-380a-8b96-813d13f96855 | -3.1339 | -52.98225 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f5491b1-db68-3898-9fef-e8cc751d20d9 | -2.74677 | -49.11538 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 77dd4281-db25-3b53-acb5-122c497c7025 | -3.16996 | -49.07376 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcd3f9f9-0c57-3272-9b67-1bf0046a2ea1 | -3.48603 | -49.91444 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e942ace-dcd5-3645-aba4-1a9428e55a70 | -1.70454 | -55.10929 | 2024-11-24 05:14:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bedaefa5-53db-32a0-908a-e62f528b345b | -1.40993 | -54.47169 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 629fab04-703f-322c-a609-a56cf0a5b725 | -3.28493 | -53.83749 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc76fb0f-5050-369d-be04-7a5387065451 | -1.88984 | -53.31721 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68e518a8-d46f-3c6e-bc52-f0876ccb2c81 | -3.10156 | -53.99587 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb1fee2f-ed4c-3d99-a384-17b4d7c31267 | -2.84563 | -54.16114 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d2d4897-8c05-33dc-af5e-bc77b52f78f0 | -1.208 | -51.75765 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9bf4002d-d3c4-3fcf-a062-fc44be77fc8b | -2.31404 | -50.59264 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7aa95bb-2861-3257-94cd-dec9747555e1 | -1.81288 | -55.13296 | 2024-11-24 05:14:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c3cd1c1-432b-3acb-9ef8-ab5ccfed5efd | -3.10677 | -53.98722 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c1a3c81-d50f-3652-8202-94d94600d233 | -3.26135 | -53.70526 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06f17728-018e-33cd-9df9-4e764e04fb5f | -1.24224 | -53.39289 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 19be1e66-0341-3e50-bbd2-a7c9ea0c2231 | -2.45411 | -53.70267 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd7ca187-40da-3c55-9379-8bddf528a7b1 | 0.41142 | -50.85948 | 2024-11-24 05:14:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3f0e96d-8186-3509-9849-b68061f20dd8 | -0.81881 | -51.60302 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README70.md)
