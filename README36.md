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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cacee4b4-b60d-3245-8dbb-642917c56f33 | -12.5879 | -53.129398 | 2024-10-04 01:28:46 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 045cb807-4bbb-3d02-a92d-adfda95a64a8 | -12.5699 | -53.0994 | 2024-10-04 01:28:46 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1a50617d-4a4d-3002-9576-75fa3173f0e5 | -12.5741 | -53.1157 | 2024-10-04 01:28:46 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b1e92b2d-8f53-35c2-a197-3145027f1458 | -12.5782 | -53.132 | 2024-10-04 01:28:46 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| efc023ba-5f9c-3782-97f0-c885fa14acba | -12.5603 | -53.102001 | 2024-10-04 01:28:46 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4478aa61-1c9a-3629-954d-b660ab0eec5c | -12.5645 | -53.118301 | 2024-10-04 01:28:46 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 18c6fb37-94fd-3d46-be17-5a619259eb45 | -12.6002 | -56.470798 | 2024-10-04 01:28:59 | METOP-B | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e0a56d4d-f9a3-3359-899e-4e9e7881edb8 | -12.6026 | -56.480801 | 2024-10-04 01:28:59 | METOP-B | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8ec0603a-4e63-3dd7-88bc-bf5c27b825c7 | -13.4018 | -61.945202 | 2024-10-04 01:29:06 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 553005b7-e271-359b-85f2-379a89e3a1c6 | -13.4033 | -61.9524 | 2024-10-04 01:29:06 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 458c010f-8164-32e4-9ab9-0ee11459f4b4 | -11.8084 | -56.572498 | 2024-10-04 01:29:12 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90a28219-2368-31eb-b955-586d42815cd8 | -11.8108 | -56.5825 | 2024-10-04 01:29:12 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0327543e-fc96-35e2-ba8b-9ce58a5451d4 | -11.8133 | -56.592602 | 2024-10-04 01:29:12 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3fa35c24-15e4-3fb2-bb2a-f3d94fc1b71b | -11.8157 | -56.6026 | 2024-10-04 01:29:12 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 45b4402c-7630-3a7f-bdc7-600bcb8cef76 | -11.8955 | -56.935299 | 2024-10-04 01:29:12 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9ebfdd5c-21b4-3a5c-8f1d-721f96c30951 | -11.8977 | -56.944801 | 2024-10-04 01:29:12 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9c269c7-f502-32f6-b9aa-3301ff085796 | -11.801 | -56.5849 | 2024-10-04 01:29:12 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e8ab670-8ce8-3a3f-9789-16d82c592cda | -11.8035 | -56.595001 | 2024-10-04 01:29:12 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f1779186-4fb7-3bdf-8298-45466a09bec9 | -11.8857 | -56.937698 | 2024-10-04 01:29:12 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a005719d-5d92-3cd3-8274-65e1ffc0bec2 | -12.9839 | -62.672001 | 2024-10-04 01:29:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8cfa6826-85cb-3784-8917-11b59257fb42 | -12.9854 | -62.679401 | 2024-10-04 01:29:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ddaec926-6769-3c94-a3ca-19656e1151c2 | -12.9756 | -62.681599 | 2024-10-04 01:29:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 23ebfb1e-c46f-394e-b6c7-4aa7d75db1bd | -12.9788 | -62.6964 | 2024-10-04 01:29:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b43928b0-def0-3413-9d81-b37695636450 | -12.9804 | -62.7038 | 2024-10-04 01:29:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4aee569a-9a8a-38d6-af2f-a19949935e8f | -12.9037 | -62.4436 | 2024-10-04 01:29:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b6d99c31-54d9-3ca1-9cf2-f88b14d5a07b | -12.9053 | -62.450901 | 2024-10-04 01:29:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 87769a37-5475-3309-9529-35fcfb8c0343 | -12.9068 | -62.458099 | 2024-10-04 01:29:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7bbb3b8c-c967-38bf-9404-c29978f331da | -12.9084 | -62.465401 | 2024-10-04 01:29:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a277fcab-7186-395e-ae06-676f30afed20 | -12.91 | -62.472698 | 2024-10-04 01:29:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fc566931-f5ef-361d-822e-6c4575ca2dc0 | -12.9116 | -62.48 | 2024-10-04 01:29:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 740ef497-d414-393e-9683-97b19e0d42c9 | -12.9132 | -62.4874 | 2024-10-04 01:29:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7dffbf1f-99ed-31ea-a26c-f7b756aa45ab | -12.9147 | -62.494701 | 2024-10-04 01:29:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0d6eeca2-2fa0-314c-8c4b-46a26fcd7bf6 | -12.8825 | -62.440701 | 2024-10-04 01:29:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c608f651-a145-31a1-a9fb-7892007e168b | -12.8727 | -62.442902 | 2024-10-04 01:29:17 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| df60b836-5176-3eab-bcbc-4ccae3e33cba | -12.8948 | -62.5452 | 2024-10-04 01:29:17 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2e79ac9a-bf9a-3d39-89a4-fcb2f157a84b | -12.9004 | -62.713799 | 2024-10-04 01:29:17 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f19e192d-a8ea-3d50-8df8-590137596eb5 | -12.902 | -62.721199 | 2024-10-04 01:29:17 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9947dc78-77ba-3a0b-ab8f-3cdde8c54a6c | -12.8922 | -62.723301 | 2024-10-04 01:29:17 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6392c297-d204-35e6-875c-99fde258ece7 | -12.8253 | -62.461102 | 2024-10-04 01:29:17 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 12afa1d9-def5-347d-948c-2304a812fee2 | -12.8139 | -62.456001 | 2024-10-04 01:29:18 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6b89ab14-e1b5-359b-8512-5d61fcc39657 | -12.8155 | -62.463299 | 2024-10-04 01:29:18 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 01a318e8-9be9-3b3d-bd8b-16b8d560b824 | -12.8171 | -62.4706 | 2024-10-04 01:29:18 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4a39f495-b8cc-35f3-8506-9eaab2f507da | -12.8806 | -62.7649 | 2024-10-04 01:29:18 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 12fffdde-3f37-341c-88f2-bb4934aa593c | -12.8057 | -62.4655 | 2024-10-04 01:29:18 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 54c22e51-cb06-30f1-b570-ac3aadd6d4eb | -12.8073 | -62.472801 | 2024-10-04 01:29:18 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 57981946-a6cc-3f1b-b4bb-b01ed380a7da | -12.8724 | -62.774502 | 2024-10-04 01:29:18 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d728045f-57bd-3b5f-8cce-07d97a3bee10 | -12.8446 | -62.788399 | 2024-10-04 01:29:18 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 97915416-cd29-39ff-b788-080ea0e2cd3b | -12.843 | -62.780998 | 2024-10-04 01:29:18 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1a97e8fb-140d-3d9f-ad1b-44be9d0f4ae9 | -12.779 | -62.912399 | 2024-10-04 01:29:20 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 660f3d24-d8d5-3de3-9083-8112b66db92f | -12.7806 | -62.919899 | 2024-10-04 01:29:20 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ab388099-94e6-3c80-9413-a12d1a1e3952 | -12.7692 | -62.9146 | 2024-10-04 01:29:20 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2837a80d-baa2-33f9-9e9e-59322a93d983 | -12.7708 | -62.9221 | 2024-10-04 01:29:20 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e50069ae-7a49-3483-a0d9-ebbb57c8287d | -12.7465 | -62.856998 | 2024-10-04 01:29:20 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 00e01de1-0238-3566-ad37-e7f0d5c96e96 | -12.7367 | -62.8592 | 2024-10-04 01:29:20 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3584b917-1b9c-393b-9648-683211373687 | -12.7398 | -62.921101 | 2024-10-04 01:29:20 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 11a8beb8-251d-3eaa-b31a-e696bf87bec0 | -12.7414 | -62.9286 | 2024-10-04 01:29:20 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c1d9c93f-afec-3782-90db-e60b30930f75 | -12.7251 | -62.900799 | 2024-10-04 01:29:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 69bcbd3b-3b30-341d-9a1a-a9142a919e79 | -12.73 | -62.923302 | 2024-10-04 01:29:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cec7bb8e-69a9-30c7-9c73-e25035d0ee5b | -12.7316 | -62.930801 | 2024-10-04 01:29:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 38fab41d-a637-3be1-9715-65ffc96a8c8b | -12.7121 | -62.8881 | 2024-10-04 01:29:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b28263e0-367c-3cab-b1a0-d9ab908b43df | -12.7137 | -62.8955 | 2024-10-04 01:29:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 605f0f8a-6089-3f23-b748-ed4305105e53 | -12.7169 | -62.9105 | 2024-10-04 01:29:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a4163e18-029d-33ad-9c20-ce5da86e75b2 | -12.7185 | -62.917999 | 2024-10-04 01:29:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 503adc20-bb30-3842-8c2b-c609098d1f85 | -12.7202 | -62.925499 | 2024-10-04 01:29:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aa8e0fc3-ebd7-38ec-8e0d-627a254e1cbe | -12.7071 | -62.912701 | 2024-10-04 01:29:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 552d7c6e-3f6e-34b0-9857-a1ed7a65ca99 | -11.7645 | -58.880001 | 2024-10-04 01:29:22 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d0bb0358-035e-3fad-b6ea-67e3fe413b78 | -12.6415 | -63.084801 | 2024-10-04 01:29:23 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 77527398-71a0-3cb3-b091-6bf8dc07c10e | -12.6431 | -63.0923 | 2024-10-04 01:29:23 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 95ed6591-92e2-3444-833b-f71b4d98e497 | -12.6448 | -63.099899 | 2024-10-04 01:29:23 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6ce657b6-940d-3a54-9e87-eceffff9958b | -12.6317 | -63.087002 | 2024-10-04 01:29:23 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4f899478-d242-362c-bafc-7adc9a07f71b | -12.6333 | -63.094501 | 2024-10-04 01:29:23 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0cb6f953-8ee6-32fb-9c2f-440085ac3a82 | -12.635 | -63.1021 | 2024-10-04 01:29:23 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fba5ed40-193d-3436-837b-73529987433e | -12.6366 | -63.109699 | 2024-10-04 01:29:23 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 671bf9cd-4429-382f-8a1a-bdd1c064b8c3 | -12.6399 | -63.124802 | 2024-10-04 01:29:23 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7976e7e0-aa2b-39fb-90c7-bb2c7e9fbeb4 | -12.6415 | -63.132401 | 2024-10-04 01:29:23 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 18255c50-e7e9-35f2-8d12-3abee981629d | -12.6235 | -63.0966 | 2024-10-04 01:29:23 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 22c6714c-a424-3247-ab18-dcfe3c172179 | -12.6252 | -63.104198 | 2024-10-04 01:29:23 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 54239c11-51dc-32a4-bd10-7a4e3aebcd07 | -12.6268 | -63.111801 | 2024-10-04 01:29:23 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8b5ff141-6e29-37a3-aed2-984c1a8983d2 | -12.6284 | -63.1194 | 2024-10-04 01:29:23 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6dd62d57-65eb-3da1-8016-d88cabffdcc1 | -12.617 | -63.113998 | 2024-10-04 01:29:23 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 662c406c-a3d7-3655-adf1-788cd71d94e8 | -12.6186 | -63.121601 | 2024-10-04 01:29:23 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 506d0eab-0df5-39f3-9f08-45698812764c | -12.4262 | -62.990601 | 2024-10-04 01:29:26 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 16225c0c-a31f-3bd1-8cc7-1f3904eabc38 | -12.4278 | -62.998001 | 2024-10-04 01:29:26 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ba4c79ea-82b9-327d-9038-c8d1d1c11478 | -12.4294 | -63.005501 | 2024-10-04 01:29:26 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 48df43c5-58e1-3816-ac48-b9c9da1d6f0c | -12.418 | -63.000198 | 2024-10-04 01:29:26 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e81d6d9a-64d0-3c18-a87d-ca5386083dcf | -12.4196 | -63.007702 | 2024-10-04 01:29:26 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8be3575a-82d4-30b1-a57f-cf59d888e922 | -12.4066 | -62.9949 | 2024-10-04 01:29:26 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6ecffc57-b4c0-3548-bf2c-c1ebecf0d41f | -12.4082 | -63.002399 | 2024-10-04 01:29:26 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7bca9f9d-7e23-3c33-a341-666243d9d49e | -12.4098 | -63.009899 | 2024-10-04 01:29:26 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dd6845ca-d8a2-35bf-bba6-010602499bc5 | -9.3007 | -50.772099 | 2024-10-04 01:29:29 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6410b39-ffd8-3f5d-9461-898db9793a65 | -9.3076 | -50.798599 | 2024-10-04 01:29:29 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ba757dd-084a-3b09-9f24-18ad998c220f | -9.2911 | -50.774601 | 2024-10-04 01:29:29 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ae89098-0382-3b16-9f2c-e0029cd43ee8 | -9.298 | -50.801102 | 2024-10-04 01:29:29 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cae9ef9f-19cf-3860-b096-0b492828fd14 | -9.2815 | -50.777199 | 2024-10-04 01:29:29 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af7d2e6c-85b8-3d5a-8488-6f888e44acf8 | -9.2884 | -50.803699 | 2024-10-04 01:29:29 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1734a97-1aa8-371d-b567-10abd13d185b | -8.6284 | -50.002701 | 2024-10-04 01:29:37 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0cd1b57-5810-3a18-b575-5f29acdbd46e | -8.6364 | -50.033501 | 2024-10-04 01:29:37 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fea7119b-7c00-3779-84b7-3162db76b7ca | -8.6188 | -50.005299 | 2024-10-04 01:29:37 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa3c9a77-bc9d-3892-a679-94e83c910efb | -8.6268 | -50.036098 | 2024-10-04 01:29:37 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 659b6f82-836c-39cd-9008-d7423256330d | -8.6173 | -50.038601 | 2024-10-04 01:29:37 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README37.md)
