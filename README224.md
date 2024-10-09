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

## Dados Diários - Página 224

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86bf4342-e75a-3c22-89ef-f9e7e8ace69a | -11.70508 | -65.01226 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3eeaa87b-91dd-3598-8017-b2c95b9e99f5 | -11.70338 | -65.00125 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e620bd7-961a-39e3-9186-9abc65025c9f | -11.70284 | -65.00569 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04436fa7-fe82-3c6f-adc6-f4355ab4acaa | -11.70229 | -65.01017 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 114fa148-2567-3aa9-8703-7bf70342b0ac | -11.70175 | -65.01461 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 38966aab-81ec-3caa-87b4-33b4f9877c10 | -11.69633 | -65.00935 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ff90da20-f51f-3877-93e1-ef234dc97e36 | -11.69079 | -64.02025 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e434189-add1-3433-aff1-f05af47533ca | -11.68439 | -64.0199 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7bd0e542-a076-38dc-ba41-308e35e6c765 | -11.68358 | -64.02686 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efe272e7-7f53-34c1-8c33-2f24b1fb85d5 | -11.68294 | -64.03229 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a187fc63-c653-32dd-b253-2ef64c73535e | -11.68242 | -64.03674 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e469eb0c-fdc4-3933-b287-eab41a719791 | -11.6819 | -64.04119 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12acda22-495e-36b8-a06a-edf7c2b955c1 | -11.67861 | -64.01429 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 476966fa-6608-3cef-be30-fc16091c455f | -11.67797 | -64.01975 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| eea4d067-2b60-3460-a4f9-932fa037e8fa | -11.67719 | -64.02647 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2ace4054-7c00-3417-93f5-3e975a916ca1 | -11.67656 | -64.03182 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 28.1 |
| b6ffdc50-7e6b-3ad4-89f1-b15e2178ac90 | -11.67604 | -64.03626 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 28.1 |
| f6a92d76-ca75-31ea-a680-c17db3eef6df | -11.67548 | -64.04108 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac6699cb-545b-36ec-86af-16d401952316 | -11.6749 | -64.04606 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f12bf18-0c1a-39a0-89af-24b6876604df | -11.67081 | -64.02591 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 10b74e78-8978-3a1b-94be-e026f639cc88 | -11.6702 | -64.0312 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 28.1 |
| c46d72e6-9d0e-34c1-b369-7438c98f1bb2 | -11.52057 | -65.14457 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9440303-dd78-321f-9f8a-705ff279b634 | -11.52008 | -65.14871 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3debd1e0-ce5f-3890-98ba-8bf59f071ac8 | -11.51958 | -65.15286 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 08fe3e22-b5d1-3422-9c58-6a43def96699 | -11.51516 | -65.13961 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da871c8f-2bbf-3390-87f8-218c94960c98 | -11.51467 | -65.14379 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a400bfb0-b9e7-3371-bee8-694812e5ef3b | -11.51417 | -65.14801 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9b084ae5-efd2-3c23-bc23-0e3cc28f2056 | -11.50424 | -65.09735 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f194e37c-5314-3b81-995b-6355eeb0d71c | -11.5037 | -65.10168 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 534e59ae-0c17-3ceb-9d59-992202a08c9f | -11.48379 | -61.97609 | 2024-10-09 06:20:00 | NPP-375D | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aeebac71-c8f1-350d-8ace-26f5ba9dd908 | -10.91045 | -64.16437 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb03138a-c108-363a-a3cd-83df253f1884 | -10.9041 | -64.16453 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1e7d278-d50c-3a74-b471-590c262c74a7 | -10.89485 | -63.9172 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77b1c848-a2db-3a2b-a48f-70d17ff36110 | -10.893 | -63.91629 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2afd85c-3130-3da5-bf62-e86748d6783b | -10.89237 | -63.92142 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70b58f15-069a-3429-a41c-df56b562e091 | -10.88784 | -63.92231 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 871f2cd2-0711-31fc-b01c-65e8d19ea17c | -10.88597 | -63.9213 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a64dde01-6dd1-3b70-a848-cd8f5ebf64bc | -10.88539 | -63.92606 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08c1a0be-a979-3c6f-86b0-68e56e3cd299 | -10.88211 | -63.91638 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 564831b2-7399-32c2-8d32-7b963cb2cce2 | -10.88151 | -63.92154 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99c39777-cb2c-31cd-9c66-4f85aa3ffed2 | -10.88096 | -63.92632 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 018fca52-37f5-3a2d-8736-2d8a6e88b94b | -10.87965 | -63.92046 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51b6c39f-709e-3a87-9e4d-cb54b7b7a4bd | -10.87906 | -63.92527 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36cacff9-67e2-3626-8637-0565a3128821 | -10.87537 | -63.90277 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5cca1c7f-71cc-3f39-9ccd-e44b6c6ff219 | -10.87465 | -63.90873 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f628172f-4e85-3d70-98a9-9bbf637a22b0 | -10.87276 | -63.92429 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a64d9f4-5734-3959-ba77-747cc8e0625e | -10.87222 | -63.92872 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ca0b3fb-2c96-3367-ae6f-0ab49602206c | -10.86913 | -63.90125 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6bdbb3f8-50a8-3215-911c-2dfad1a3170b | -10.86843 | -63.90702 | 2024-10-09 06:20:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8dd11343-54d9-332b-a195-e372b6b9913d | -10.86645 | -63.9234 | 2024-10-09 06:20:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 100bfc4c-54db-318f-97d5-d532dacb989d | -10.86219 | -63.90543 | 2024-10-09 06:20:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 93decfe0-d8d8-3398-8b20-54ebce45955f | -10.8615 | -63.91121 | 2024-10-09 06:20:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04eff740-5e30-3ccd-a03b-54c361da55fd | -10.86084 | -63.91668 | 2024-10-09 06:20:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 004be5dc-4f05-300d-ae2d-e2a2109da3fe | -10.80016 | -65.17388 | 2024-10-09 06:20:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 765d0518-d330-3501-b0f1-60f820da3088 | -10.69673 | -63.63962 | 2024-10-09 06:20:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4daf0a50-74a3-30f4-8c75-9269922edee7 | -10.69616 | -63.64436 | 2024-10-09 06:20:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68296731-b440-3a16-b85e-7486645495c7 | -10.68969 | -63.644 | 2024-10-09 06:20:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 300e0227-3f7d-3412-aeac-9650352aa32d | -10.66669 | -69.10379 | 2024-10-09 06:20:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd97cad7-3f7c-30e9-9d39-b2f998a62e1e | -10.50066 | -68.77652 | 2024-10-09 06:20:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f980c216-add0-3e8b-b1b5-31f051077726 | -10.47704 | -62.898 | 2024-10-09 06:20:00 | NPP-375D | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5f775ae-2b6d-3669-9d55-2908ed2ac895 | -10.47387 | -62.89746 | 2024-10-09 06:20:00 | NPP-375D | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0a1010cb-9996-33cb-ab38-85bcd915a8ca | -10.47042 | -62.89645 | 2024-10-09 06:20:00 | NPP-375D | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65b2aac7-28b6-362b-9137-e910d1de9e56 | -10.4689 | -69.04933 | 2024-10-09 06:20:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c15ff56f-eb68-33eb-bd53-64eff3f82743 | -10.46743 | -69.04602 | 2024-10-09 06:20:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ccdac9f9-400b-38d3-b71a-288bef950d6a | -10.3962 | -68.65504 | 2024-10-09 06:20:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d8a4904-83c9-33f8-8cc8-cab3c070a716 | -10.39565 | -68.65702 | 2024-10-09 06:20:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 522a2d6b-8070-321c-8d42-4992eb2bd0fc | -10.38063 | -64.83105 | 2024-10-09 06:20:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19c432ca-f7e7-3e06-a46b-9c638113093a | -10.38008 | -64.83537 | 2024-10-09 06:20:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b360ee9-5a06-3d85-b261-f78448aa552a | -10.37783 | -64.82788 | 2024-10-09 06:20:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f25ee909-f5fc-30c1-9721-0218a30d5cd8 | -10.37731 | -64.83219 | 2024-10-09 06:20:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4ec07ed6-cb70-3f54-81d4-345a4f2056df | -10.37679 | -64.83646 | 2024-10-09 06:20:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ede39d44-892b-341d-95b3-19ada2e2417a | -10.37525 | -64.82601 | 2024-10-09 06:20:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d08833ee-2efc-3a3a-9014-823b24e57bea | -10.37469 | -64.83032 | 2024-10-09 06:20:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d7452363-aca8-3844-b66d-cd72c9377c62 | -10.37415 | -64.83455 | 2024-10-09 06:20:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1695e81a-7e45-3427-aa0e-3866196efbfd | -10.37361 | -64.83877 | 2024-10-09 06:20:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7a8a6711-e9f3-3541-af91-5e738dc98279 | -10.37189 | -64.82714 | 2024-10-09 06:20:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6ae501fe-4d20-3e72-9ddd-a58dfe2cc7d2 | -10.37137 | -64.83141 | 2024-10-09 06:20:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7ebcd59a-5757-31a8-9ec5-5ae044af47a2 | -10.37086 | -64.8356 | 2024-10-09 06:20:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 723044ff-465c-32e5-8b94-6c0a0f9b06f9 | -10.37035 | -64.83984 | 2024-10-09 06:20:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a29a2268-3f34-3254-b0e7-5e24dab77ad9 | -10.36875 | -64.82958 | 2024-10-09 06:20:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6daac8d3-5ef7-30dc-a581-34c05922b81d | -10.36821 | -64.83382 | 2024-10-09 06:20:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2deacbf0-5fe5-31e2-a136-d6f9676514b3 | -10.36767 | -64.83804 | 2024-10-09 06:20:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d4a6549c-f75c-34b7-8037-b8489bd1a157 | -10.30513 | -68.74209 | 2024-10-09 06:20:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a39884f-0ae1-3a3b-80bb-e9dafa33cc4c | -10.30119 | -68.73683 | 2024-10-09 06:20:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b093cfc1-113d-346d-a054-1f939e6d0cfd | -10.29822 | -68.68911 | 2024-10-09 06:20:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22cba323-0459-3cef-9fea-2f2857f64f53 | -10.10696 | -68.39387 | 2024-10-09 06:20:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fabb5b8-d8ca-3a23-905e-1f515069abee | -10.1023 | -68.39326 | 2024-10-09 06:20:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b012cf26-7e12-3d03-baf6-a8032c99c21b | -10.0957 | -64.83788 | 2024-10-09 06:20:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c066bd51-5152-3e02-ad0c-1d7d8bb76482 | -10.09518 | -64.84203 | 2024-10-09 06:20:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc7f1db1-9460-34af-88e6-53deacf3b8c9 | -10.0898 | -64.837 | 2024-10-09 06:20:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ba49629-503f-3db1-a6d9-69e6e0025e88 | -10.08943 | -62.51616 | 2024-10-09 06:20:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc97ad7a-494d-332b-9ec1-e603d0d712fc | -10.08928 | -64.84117 | 2024-10-09 06:20:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9845884-3a08-31b1-bee8-7ed4f844a205 | -10.08261 | -62.51535 | 2024-10-09 06:20:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce109dc1-645b-3f00-86b2-b5d3bb5d2d4d | -10.07772 | -68.46875 | 2024-10-09 06:20:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ab51483e-e058-3987-8e67-c9da05d6a11e | -10.07376 | -68.46323 | 2024-10-09 06:20:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ef20259-ba6c-3841-9963-ffeb9ec4b407 | -10.05996 | -68.52965 | 2024-10-09 06:20:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddb35e5f-8360-3c7e-b46b-96e27ee9863f | -10.05931 | -68.53439 | 2024-10-09 06:20:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27d8aea5-573a-3e62-a177-f7652cd5a6ca | -10.0321 | -68.45735 | 2024-10-09 06:20:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3617fb50-b9ed-32ea-8c2b-06a71ace43e8 | -10.01192 | -68.44151 | 2024-10-09 06:20:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42b04047-e635-3f2e-bfac-d56a2cadca8f | -10.01125 | -68.44632 | 2024-10-09 06:20:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README225.md)
