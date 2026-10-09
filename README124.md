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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb555671-bd04-3116-99c6-872195d9f736 | -2.77836 | -54.08475 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b08e369-2360-3b08-81bc-745915bd1ad0 | -3.16995 | -50.45376 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53294008-fd44-3b29-a2bf-aaf12cafe9a2 | -2.46791 | -56.09051 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a77b8343-32f8-3241-8c0f-74719d23ac18 | -2.73353 | -54.90532 | 2026-10-09 05:01:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eb10c01c-f903-392e-ae0a-7a418bae227c | 3.55714 | -51.279 | 2026-10-09 05:01:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc6c32e6-d3e4-351b-bc77-8bd824751dd8 | -3.18466 | -50.5804 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2b3f30fc-47c6-3c88-9497-989eeaa438f9 | -1.19953 | -54.21519 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df771612-e976-3f54-949b-762a8ad5047e | -2.83969 | -54.12922 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddc8330f-e949-3dd8-bff5-b1ce6f74217c | -2.3793 | -48.22575 | 2026-10-09 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c71d1693-635e-3dfc-a634-964e87192e83 | -2.46396 | -56.08669 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4a46a4bf-db03-3043-8b62-ff60beb4de8d | -3.53514 | -49.47226 | 2026-10-09 05:01:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cc43c3c-f72b-3f7e-843a-72681268f40b | -3.34797 | -50.47383 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e027d9be-ac62-3da8-93d7-85cfa94b714a | -1.10794 | -54.15629 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc10f592-16e0-33bb-8d6b-72a697ecfb9a | -1.18751 | -54.17574 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d81bad0-83b4-3c19-9371-4faebf0a8f31 | -2.33586 | -48.86419 | 2026-10-09 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e6f25b4-bdca-3198-97c3-939302afbde3 | -3.27294 | -50.39958 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8e6107d-a2ca-3c40-9ca4-7f3cf0a5357b | -1.20437 | -55.68681 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 001cb4ec-da95-3c2e-b8c8-221921688608 | 1.73086 | -55.5914 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 07ee7b6c-b4da-3d1e-9330-9f3a7fe9b619 | -2.506 | -56.14898 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9610609c-fae8-386f-8652-cf8bc57cfa16 | -2.73837 | -54.11012 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc6111d2-42a0-357f-991b-d2f158eb604d | -1.40551 | -53.23304 | 2026-10-09 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46161274-a110-3977-932e-2915f8253662 | -2.47496 | -56.09666 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 169edc9d-f55a-32d9-861c-1e63cdefc7ae | -1.26225 | -54.68633 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33581853-eb3e-3a84-bd80-727617da0fd3 | -1.37635 | -55.45477 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d0a0336-6cf0-3d9c-a758-ae2460a3e9a1 | -3.39195 | -50.21795 | 2026-10-09 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e74cc6e0-f793-3ee2-8f75-489188794cd8 | -4.15159 | -43.1903 | 2026-10-09 05:01:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 849e27fd-c9c0-3838-9e8c-4419e5c86705 | -3.19252 | -50.55244 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc4bade2-8a90-3193-a4b4-6a8c297e51d0 | -2.74001 | -54.12232 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8e2ffea-7457-3c45-9104-e65e7035a294 | 0.50352 | -50.77985 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69f9ec1d-044b-39ef-9091-9ef1568cd232 | -1.77791 | -55.02108 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5db72f1-0ba3-3583-9a5c-1335cd0a1406 | -2.46801 | -56.06228 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c46bdf83-9085-3052-bc60-8bd01b052d6a | -2.84031 | -54.12535 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86f04dd8-fcc0-3ce4-a929-b5e897d8197f | -3.19477 | -50.56009 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a97c5efc-0ab4-33f1-bd37-370fbf5ace83 | -2.83104 | -54.11593 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eea95787-ccfc-3094-9971-df4866404971 | -2.51273 | -56.25737 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be733935-c63e-3482-885c-f5e7388e5a7d | -2.49101 | -56.16684 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1ebe6c9-f9a6-3ac0-b46a-dbd871bcb7df | -3.19028 | -50.58857 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d8a9a2e-b3cd-3f61-9196-fedbf7a154ed | -2.84195 | -54.13753 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 944da12f-50e6-300d-801c-ef9482c3cf4a | 3.74232 | -51.61097 | 2026-10-09 05:01:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ea99c66-d0d1-38d7-b1c8-19cc046c2ccb | 0.78705 | -59.198 | 2026-10-09 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bea0fc19-555d-3470-b03a-16e9c1f15f85 | -2.51902 | -56.26865 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 037817a2-50f0-3107-b668-f434934e7033 | -3.17905 | -50.59411 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a31b8e4e-f997-3cda-a809-bcc416876577 | -3.52872 | -44.33439 | 2026-10-09 05:01:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e14d6a04-a93c-37d5-ba7b-9d1b345f2d40 | -2.23844 | -51.9226 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe4ce7fd-b4cc-323a-9490-8f681f20431b | -3.35079 | -50.47794 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c9606b9-fe1b-3059-8b44-e72d50e344b7 | -2.51227 | -56.16002 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f1abcc2-60e4-3cfe-a0f9-40fab480981e | -2.84794 | -54.1226 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc1a2e7a-7253-3103-bff9-7094e5de7cbd | -2.51007 | -56.32454 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5cbce6a-2b43-3a4e-9ad5-cfa0ec94cd7c | -2.75549 | -54.093 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 408e2de3-c618-34d6-aec3-879ba0f8ecbb | -1.52608 | -56.12298 | 2026-10-09 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 01890aac-21b0-3b7b-aa0f-c3f75d974650 | -1.1862 | -54.18393 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7a80e6bc-cf4e-3532-b5b0-7c9f59a7363e | -1.54722 | -54.5605 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4471672f-ebf9-3e02-b625-95ce72d316be | -1.19302 | -54.21001 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4069912d-b1d1-31cf-8dba-580ba46a2b25 | -3.00584 | -51.0075 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b78ec85f-7231-338a-b650-dbd04909fbce | -2.83018 | -54.14363 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 849e3bb2-a673-39ad-af6f-67f587820dea | -1.89386 | -54.67627 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e7dbc7a-6e41-3830-9171-890b06314f1e | -3.17287 | -50.5895 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44922236-3dce-3db2-9a1c-ab464a3c180d | -3.16601 | -50.45682 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5448879-24ca-3dc0-9245-63dc8d7c2c1a | -2.36182 | -48.88456 | 2026-10-09 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2de0f46b-e8f5-3a70-a16c-6e86d648e11b | -2.83618 | -54.12866 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d589531-811a-32a1-ad21-916c66d33ba5 | -2.5695 | -54.03746 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 529141f8-feff-32cb-9995-5641403ed13b | -2.39702 | -51.3036 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e48d623b-0da6-3b58-a09c-ec6c5f9134de | 2.45501 | -50.8158 | 2026-10-09 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f65d4b5-be28-3dc6-b416-3f2ee4b6938f | -2.41116 | -56.52948 | 2026-10-09 05:01:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78036f76-e648-362c-a6de-83b6de5e0a63 | -2.46555 | -56.08014 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d0ca9b4b-0ba9-3448-9cf4-b5d0c4219123 | -2.99086 | -51.0373 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e100e61e-e1e5-345d-b28b-7186a2987747 | -2.07346 | -46.57177 | 2026-10-09 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c85ee33f-9a21-3105-b782-694068757bd8 | 2.41947 | -50.82493 | 2026-10-09 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 19.8 |
| adf0f598-9a0c-35a7-b6d4-3a3410ce2389 | -2.41404 | -56.5371 | 2026-10-09 05:01:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| da2060f6-8a38-37d8-aa70-e243c3d0c887 | -3.03515 | -42.10949 | 2026-10-09 05:01:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84df4974-9511-3838-9713-7fee761598f5 | -2.74827 | -54.11569 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bdf69562-f327-35e3-a1a1-33a26a685304 | -1.11609 | -54.1742 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fef8ab1-f984-3a74-9b3a-6c47c286c4ca | -3.16668 | -50.58489 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89dbd499-29d7-3aa5-bfd8-1e4c295ab3ca | 3.55659 | -51.27547 | 2026-10-09 05:01:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a9962813-06c4-3af5-a97e-668a72a939df | -2.84257 | -54.13366 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0712dd6-890c-31fd-8501-02dbb3dd6fc7 | 0.9458 | -50.19992 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbd56e77-77ef-3718-abe4-5b88e4c7d204 | -2.50431 | -56.18425 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1f2e822-4d63-3877-a416-9add4831d512 | -3.30022 | -49.13039 | 2026-10-09 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 530b6225-3f2b-3aae-b1df-8e119f30b53e | -1.10116 | -54.17589 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 41ff8b34-b44e-34b2-b9c5-c3d3264aa730 | 2.76345 | -60.00406 | 2026-10-09 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 113a986d-508b-34a3-80c4-534ea0d87949 | -3.26586 | -50.39517 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| acb77a50-ccc6-3928-acde-c912b10a64ec | 3.46221 | -51.47113 | 2026-10-09 05:01:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b100ad90-7bd7-33f3-a70d-6e890bcd93e9 | -2.48489 | -56.13041 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3dcd8a76-9490-367f-b5a0-ac4ae4ee16d4 | -3.27406 | -50.3924 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23ea5774-31d0-3a55-80ad-1eb06e8384ee | -2.4796 | -56.08923 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8815420d-9d1b-3c62-9387-a7fbe0adf3d1 | 0.92582 | -50.2598 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dce8f712-a78d-3d1b-83d9-f08801f714f3 | -2.73463 | -54.1334 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39f557ea-c7e3-3bbe-8b16-56a63126e4cf | -2.47574 | -56.09177 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b7df9f2-7cf5-3b92-9792-61b4b8c4d839 | -2.50216 | -56.12316 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1b20b04-ca0a-3274-926c-37c87ab55686 | -1.1018 | -54.17184 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bfba43a0-1562-328e-ac39-5ddebce3f2a2 | -2.11262 | -58.13134 | 2026-10-09 05:01:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6410a5e3-507f-372e-b2ef-ddf259df88fa | -1.47456 | -54.64008 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f774bac6-b160-3141-a212-73dd98d7c1ff | 2.77866 | -51.40741 | 2026-10-09 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 411e2e8f-6632-3e35-a5a1-2d9f8edd2957 | 1.6898 | -55.61924 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8507eccc-e7f7-3c4c-8747-e6ed31269d33 | -1.77624 | -55.02225 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b23f8acb-2b10-3c7c-a5cc-40417f71f18a | -2.16696 | -54.45913 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 893e774d-7b15-3733-bf1b-57ad97ebfc99 | -2.49924 | -56.06728 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| b8a636fc-3335-3ead-b1d5-68eab0c49562 | 2.76952 | -60.00677 | 2026-10-09 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3110146b-02e8-3717-9ac5-d2258e953444 | 1.7762 | -55.5349 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3acb4954-feb6-3b31-8b73-c19717ec6fc6 | -2.34004 | -48.86074 | 2026-10-09 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README125.md)
