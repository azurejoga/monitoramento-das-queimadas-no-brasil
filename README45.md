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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcdd7a38-579f-393d-8b3e-26196d901e65 | -2.46018 | -53.97465 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c799678f-3592-3ddf-8300-6abe85dcd021 | -2.39825 | -53.73583 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2f545a5-a907-3f5d-ad69-f617d62a7d33 | -2.2532 | -53.75043 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3d0a762-6034-393a-aea2-011e887af00a | -2.11931 | -50.6815 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18bc1313-bb46-31bc-a195-87f42769e516 | -1.71146 | -52.46835 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b69e8114-ef6d-36cd-9b40-4cc8eca2ac5f | -1.40191 | -51.10231 | 2024-11-13 05:20:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c84b87d-8a40-3e26-8ca0-7cb3955e8977 | -1.62601 | -52.65585 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8fc5bf9-c27c-3d93-80ab-7601f1f6b33e | -2.40768 | -50.30382 | 2024-11-13 05:20:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c03fd17-3b6d-310d-9dfc-eeb92e7f064c | -2.14286 | -46.39645 | 2024-11-13 05:20:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 837009ba-23de-349c-9e4b-177180b28160 | -2.3867 | -53.66907 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea4a7ba2-b00d-33c8-9c6e-d42ab5b03708 | -2.35864 | -53.68089 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb2d3c94-c507-316e-835e-7dd555ec6ed3 | -1.42148 | -53.47712 | 2024-11-13 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0ba8dec6-cb57-3684-a52f-2fc1bd321ec0 | 0.55781 | -51.67193 | 2024-11-13 05:20:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22488980-31a6-316b-b875-e5f968f9a32e | 1.05735 | -60.59259 | 2024-11-13 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d370230-90f2-3de4-9506-cf28d143c495 | -1.65029 | -52.53069 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4eac6319-5685-358e-8e13-e05dac68ac80 | -2.1288 | -50.68945 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 878e75a5-820d-39d8-9e88-06c9c7e09366 | -1.21429 | -51.77001 | 2024-11-13 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6c800d3b-9faa-3254-89c9-adaf2e4ad149 | -1.64502 | -52.53461 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7196d4ab-697b-3147-a5d8-f44516d4a323 | -2.40312 | -53.73254 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fef9d97e-7951-332b-a1e2-9ec26069bd90 | -1.7373 | -53.28223 | 2024-11-13 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7eb990c0-189a-3461-9336-f15c457e93db | 1.05965 | -60.60736 | 2024-11-13 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3dc87e4b-120c-3bff-be3b-470ae4fab0c1 | -1.64959 | -52.53532 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 20cf22af-f174-3c1c-9e3f-07381d75892d | -2.35437 | -53.68018 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e0cf50e-8b0e-35ac-8763-b8a519930dac | -2.78031 | -50.29822 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c0ffa08f-a04a-36be-af58-9702c8a4afab | 1.06193 | -60.59943 | 2024-11-13 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 59e5decb-9300-336d-802b-f166f6e0d67d | -2.04043 | -53.956 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ebfe35cb-151d-3387-8403-8ad289325887 | -2.24835 | -53.75372 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 84b14e04-c7d1-3f0e-bbe0-82f88bc7a95e | -1.84629 | -55.52146 | 2024-11-13 05:20:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58dda868-ec4c-3539-b3c7-b7a62ce17f64 | 1.11377 | -59.19928 | 2024-11-13 05:20:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 68b44128-19f9-384e-98a0-8165f3a725f9 | -1.47124 | -52.29836 | 2024-11-13 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6cc1f1f-aa97-372b-8ecf-2f7854c70935 | -2.47014 | -50.12155 | 2024-11-13 05:20:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cfebe74b-969e-3baf-9beb-850328961aab | -0.94635 | -52.40053 | 2024-11-13 05:20:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cbcfcc3-d4bf-3a48-8433-f104f134d300 | -2.47067 | -50.118 | 2024-11-13 05:20:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 490588d3-108d-358d-b1a8-126ecb459337 | 3.59887 | -59.94416 | 2024-11-13 05:20:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d5a784a-a1f9-3b31-aced-aa71e89c10fa | -2.24919 | -52.07533 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c44bbf60-52e6-371c-b4fc-2900a36b3748 | 0.91584 | -59.4044 | 2024-11-13 05:20:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e1171748-6404-336f-af14-a237d33fe9ac | -2.12356 | -50.68871 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3121e771-6a59-31b9-a608-5ce9d6250078 | 0.82329 | -51.8727 | 2024-11-13 05:20:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b08b0ede-42b2-391c-8862-19e4d4d9ff21 | -2.14989 | -46.39887 | 2024-11-13 05:20:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a1c2a95-a226-3815-95ed-16b670980be9 | -2.37811 | -48.51418 | 2024-11-13 05:20:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c8f7b31-7370-3c9c-84af-fde47337828b | 3.2782 | -60.03408 | 2024-11-13 05:20:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47b93abb-11af-33a3-8c4c-3ff28c3f4e28 | -1.88604 | -54.20293 | 2024-11-13 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f06ab072-1c95-31e0-89d6-01ec493d2412 | -2.03932 | -56.65901 | 2024-11-13 05:20:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e46ada0-53c3-36b6-b844-f1310915e9a5 | -2.144 | -46.39135 | 2024-11-13 05:20:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1fd2b04-c73f-3a12-960b-df062d3734db | -0.87164 | -51.9553 | 2024-11-13 05:20:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f226cd1-ad26-3c75-b944-999cf94aa29b | -1.03493 | -48.84595 | 2024-11-13 05:20:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 517a94c4-0dc0-3bde-98cd-556f040183ac | -1.6222 | -52.65061 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83a57a9b-61c4-3907-b153-6f2ab34a9352 | -1.62251 | -52.65343 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7daf5415-dbd1-3c62-ad52-c892e66c60cd | 1.57958 | -55.76247 | 2024-11-13 05:20:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6b884bf0-4c2e-3cda-8f2c-e441fd203c68 | -2.21171 | -53.74532 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 93c5272d-a554-3e45-8934-21de8f4b06b5 | -1.42208 | -53.47316 | 2024-11-13 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a5288311-466b-38a8-9dae-5beb22b6e203 | -1.4172 | -53.47647 | 2024-11-13 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0ca14e8e-c753-347b-a4f1-93c31478a1d7 | -2.28413 | -53.77519 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b1a7388-4f63-3c84-9b9f-b291e0238043 | -2.12405 | -50.68553 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39976376-22a3-311e-9d1f-1d252a8e3527 | -2.40925 | -50.3072 | 2024-11-13 05:20:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5b26784-6ced-3c68-b18c-9c1f3af634cd | 1.58023 | -55.76652 | 2024-11-13 05:20:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95dc1fe3-b242-34a5-a495-bf4cd9a630c9 | -1.98742 | -51.09665 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f65435d-74eb-3e9d-82c7-6d50d749e5a3 | -1.64946 | -52.53732 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2314653-1e85-3908-a4ef-ab816cab0e8b | -2.78781 | -51.39962 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9331a0f2-6509-3c74-9b0b-b5ad1d309d0e | -1.90066 | -54.58984 | 2024-11-13 05:20:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de73c11c-67fe-35d8-ad3d-b4a843c18d24 | 0.81794 | -51.86869 | 2024-11-13 05:20:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f25bc6c-037d-3e21-b3c9-33c8eac25321 | -2.3946 | -53.73121 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b906ac5f-9be4-34d8-8a6d-5db1a6ec0885 | 1.29817 | -50.8833 | 2024-11-13 05:20:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 077b1722-59fc-34c1-b16c-f181d569fcf5 | -1.62319 | -52.64887 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 470c5b91-b62e-3b72-96cd-27f5aebb3896 | -2.72701 | -51.74357 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0621c628-5d99-34e2-9c22-e09537d38904 | -1.95678 | -53.31651 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4718e83-49d0-3a03-a16a-3e6bf4a8b509 | 1.30221 | -50.8771 | 2024-11-13 05:20:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46bd1e3f-624d-3aff-8089-627fb1c0150f | -3.02989 | -48.08115 | 2024-11-13 05:20:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34bd8ea0-1644-3bf7-8c8d-831339b1b615 | -2.45768 | -53.93502 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4d91452-faa0-3733-a5a3-0ad567b6524d | -2.215 | -53.74442 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edf1de12-13ae-32a9-8a5e-1985d7161f3f | -2.40251 | -53.7365 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65a99bef-474f-3127-9684-37e983b4481d | -2.82827 | -51.04577 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f13a080-f1bc-30fb-8a8a-d3f45523ded8 | -2.46467 | -50.12067 | 2024-11-13 05:20:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b02e4a49-7e32-3139-b34d-9dcbf4bb78ba | -1.03373 | -48.84779 | 2024-11-13 05:20:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c5aaa798-9b60-31aa-8e03-b9e5cfcfcee5 | 0.84862 | -50.20953 | 2024-11-13 05:20:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da10477a-da66-3f9d-8836-a6c50dd4da14 | -1.97959 | -53.13449 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b3a2f5b-452f-3ff9-a30d-2fe630c2e48a | 1.06023 | -60.61105 | 2024-11-13 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65c0f071-8fda-34a4-838e-b16361985f2f | 0.62245 | -60.08476 | 2024-11-13 05:20:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8d80739-6ebb-3606-a178-27598763131b | -0.38656 | -51.75008 | 2024-11-13 05:20:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fabe0ab-d371-3188-983a-1a7c3d80ac7f | -2.69682 | -49.35126 | 2024-11-13 05:20:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6fb3dc5b-1582-33e7-9364-81d2da974fe3 | -1.57437 | -55.15585 | 2024-11-13 05:20:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8867d090-78fe-3ca6-b05d-6fbe129edb9a | 1.06651 | -60.6063 | 2024-11-13 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9a0ee22f-7d79-3154-b7a6-5d2062baf0d1 | -2.38791 | -53.66117 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 385b773a-9325-353b-8b02-18cc5965810f | -2.12873 | -50.6898 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1c8f3d5-4c18-37a6-b733-5e6b31ad13d1 | -0.37709 | -51.74859 | 2024-11-13 05:20:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb8d0dae-7663-3e77-adba-f7cc2297664a | -2.71614 | -51.70752 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a97eebc-6d28-3a48-b030-b7a7c63cf85a | 1.60065 | -55.77991 | 2024-11-13 05:20:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75e4fa61-725b-302e-be2d-797d1fe78139 | -2.11981 | -50.67828 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e33e1f9d-3abb-3722-b315-2c67048acd75 | 0.62086 | -60.08546 | 2024-11-13 05:20:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5463239a-0d9e-3eae-8a60-a2f18826bec6 | 1.05793 | -60.59628 | 2024-11-13 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 64bd0584-f726-32e3-af81-1e84e9641451 | 0.84813 | -50.20647 | 2024-11-13 05:20:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bf92ef7-3083-39a5-ae50-4f44022b3912 | -2.21134 | -53.73988 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7b63deb-9b40-3a12-9d42-ee833997aef5 | -1.39643 | -51.1044 | 2024-11-13 05:20:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 51a57580-c4b5-3b73-a254-dc210f8aac09 | -2.31164 | -50.68048 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04994735-b7f6-3e9e-8c58-562c7efce981 | 1.11323 | -59.19582 | 2024-11-13 05:20:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5c30adc-f1f3-392b-96d6-dd73fb828143 | 1.59936 | -55.77181 | 2024-11-13 05:20:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 78a788be-0019-359c-9cc1-736571fdcbcb | -2.11734 | -50.69422 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e21953ac-d653-3d69-9306-352fbfef772b | -1.51254 | -55.87869 | 2024-11-13 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6794af2b-13e7-3262-9f35-cdf54525c49c | -2.12825 | -50.693 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2464d6a-53a9-395d-b402-3cd709e0e1e6 | -2.3873 | -53.66512 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README46.md)
