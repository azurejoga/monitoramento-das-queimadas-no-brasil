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
| 83ac2adc-0440-3715-842b-06ce0d420290 | -4.40546 | -55.10949 | 2024-10-30 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c4ce7d7-d839-39d2-9000-5eb595359dcb | -4.36615 | -55.21103 | 2024-10-30 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d797fc2-2933-3ecc-bbfb-c9080a2776a8 | -4.36218 | -55.21038 | 2024-10-30 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 806cc2b4-83c2-3b57-b770-326f56dd1ab6 | -4.20577 | -55.2302 | 2024-10-30 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2889c15-0a34-3b19-bbde-42fbf314cb4c | -4.20179 | -55.22952 | 2024-10-30 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8350840-6f97-3933-9dd6-c21a63c1ac22 | -4.17795 | -55.15201 | 2024-10-30 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ce7fa0b-a67b-38d2-bfd0-5df8e9824ff5 | -4.17625 | -55.15022 | 2024-10-30 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31a0ce5a-bb73-3139-abf2-b111f792b183 | -1.74733 | -54.96749 | 2024-10-30 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 785df82b-9fd6-3127-a880-1dada06cfd00 | -1.63475 | -55.20278 | 2024-10-30 04:44:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc15be8b-e229-3126-8122-7239c7efbd1e | -1.63415 | -55.2065 | 2024-10-30 04:44:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba7edc0c-d7f3-3d9b-b4be-df5ffd3dc77a | -1.59256 | -55.89041 | 2024-10-30 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8782d79-0d27-3617-a87b-781b9c580437 | -1.51909 | -55.70498 | 2024-10-30 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23191612-4f5b-3663-900a-3cde7d72bc8b | -1.32255 | -55.45749 | 2024-10-30 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f91d9e6f-c409-35af-85f0-ab2907349984 | -2.124 | -55.90043 | 2024-10-30 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c28e4df-36d9-3f3e-a7df-78c3882601a6 | -2.11843 | -55.90783 | 2024-10-30 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e757bdd8-1b74-3714-bf54-683790da4964 | -1.92823 | -56.34389 | 2024-10-30 04:44:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8ceaf190-a502-33f9-b47f-77bc88e1156a | -1.74801 | -55.25052 | 2024-10-30 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e14d6fa-bae4-3844-90e0-3cf973315550 | -1.74393 | -56.06199 | 2024-10-30 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97e78c88-3fe1-3161-a2e2-dbc1e14b14b9 | -1.74387 | -55.24989 | 2024-10-30 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e57eae8-661e-399f-86fd-41671d741688 | -1.73687 | -56.07817 | 2024-10-30 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c3ebff9-1013-3ed1-ad41-7672e57fc0cb | -1.69215 | -55.08058 | 2024-10-30 04:44:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7db4f71-1fdf-35b0-a1f8-37c127115b58 | -1.63828 | -55.20719 | 2024-10-30 04:44:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ef4555c-16f7-3092-ab13-93a8eec3351b | -1.59323 | -55.88631 | 2024-10-30 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7fc4ffe-c126-3482-b54c-af68f89e0112 | -1.59164 | -55.88748 | 2024-10-30 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aaaec9c0-ec9b-3721-9bf8-a7ebd12d5201 | -2.19021 | -55.85589 | 2024-10-30 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf00100e-9fa7-32ba-a287-35d127497ef6 | -3.68903 | -55.56408 | 2024-10-30 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcf95ce5-b6a5-374c-9157-7d29acc6ed11 | -3.68653 | -55.5643 | 2024-10-30 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a78526d3-78bc-35e8-87a5-853c327cef26 | -3.72363 | -55.55861 | 2024-10-30 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e101d86d-88d7-3579-9412-33202eac0782 | -3.69784 | -55.56178 | 2024-10-30 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bb075a8-c60b-3e66-af6d-ba9aa52002a2 | -4.1463 | -55.43972 | 2024-10-30 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75665a49-e7b4-38dc-932e-8af2deda354c | -4.1457 | -55.44334 | 2024-10-30 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 432211fb-9947-3aa9-b621-fbb8b1954d13 | -4.14285 | -55.43553 | 2024-10-30 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a88b2567-e0a7-38ce-a0d9-a3a252776771 | -3.99004 | -55.72972 | 2024-10-30 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1493b3d-bd72-38a6-b16c-2f5955defb55 | -3.9878 | -55.72982 | 2024-10-30 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6adff5a6-f2a7-3e82-a1be-fa0f3ae5e3ae | -3.98592 | -55.72905 | 2024-10-30 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec4e557d-d276-33c6-8bb8-3ca20f7167c4 | -3.9573 | -56.05493 | 2024-10-30 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8722668a-b48f-3e0b-8852-31f3a095ebc1 | -3.95439 | -56.04638 | 2024-10-30 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21f49a7a-ee39-30d6-a62e-e2af39e16061 | -3.95374 | -56.0503 | 2024-10-30 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0f21d04-4d19-3d85-af08-8cc00e7d14c0 | -3.95308 | -56.05425 | 2024-10-30 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7197fab4-9dcb-39b9-b2b4-dc26526398ec | -3.93626 | -55.78601 | 2024-10-30 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2cf1b47b-b1c7-3c57-a7fb-9615920a337e | -3.93151 | -55.78907 | 2024-10-30 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e7adc94e-1437-30f7-b566-911d784b4c87 | -3.93091 | -55.79277 | 2024-10-30 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ada1ecbd-f434-32e9-9e24-38dcab7688b4 | -3.88122 | -55.99151 | 2024-10-30 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59c8d690-1d34-3d77-8a53-5adaa2a65f48 | -3.70134 | -55.56607 | 2024-10-30 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4ab7b84-1bbe-3b01-8187-adc1b80f7c0f | -4.52109 | -55.6392 | 2024-10-30 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3eb2e6ff-f011-3268-8ddc-cb5d9e08d758 | -4.52049 | -55.72077 | 2024-10-30 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40e88642-1523-3c26-90cb-72c58600c982 | -4.40174 | -55.76077 | 2024-10-30 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4bc3530c-9e3f-3286-946f-819dbbecdd6d | -4.30616 | -55.58165 | 2024-10-30 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8bb2225-796a-3b8b-bf25-39e454700daa | -1.9868 | -56.59697 | 2024-10-30 04:44:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 184b4183-04bb-3fab-b760-cccc7d631d7c | -2.45874 | -57.52874 | 2024-10-30 04:44:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d9c6ae8-b750-3edc-89cf-2b596ec5c2df | -2.38217 | -57.159 | 2024-10-30 04:44:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92098a83-4ba7-3749-9106-8fbdb8385440 | -2.73075 | -57.47853 | 2024-10-30 04:44:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f4920e20-f27d-3e31-be50-511c63b7b70a | -2.73058 | -57.4798 | 2024-10-30 04:44:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 69056b45-bc1a-37f1-a8e1-1c30dcda524e | -2.72994 | -57.48358 | 2024-10-30 04:44:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d86206db-2267-3866-a5e3-41b7c2f790bb | -2.72973 | -57.48484 | 2024-10-30 04:44:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 37054405-0c15-38dd-b45a-ec073a87bc0d | -2.726 | -57.47774 | 2024-10-30 04:44:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 307cdcf5-dd55-39a7-ac9f-4f484c5381a7 | -2.72583 | -57.47902 | 2024-10-30 04:44:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 57016c37-e1c2-377d-9082-871a9818bc73 | -2.72519 | -57.4828 | 2024-10-30 04:44:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a06da2ec-7e99-3a21-b58d-75415a720c0d | -2.72125 | -57.47695 | 2024-10-30 04:44:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12b927d8-0bb0-3038-8151-aad035e4581c | -2.72108 | -57.47824 | 2024-10-30 04:44:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4ad468bb-8158-3ca5-b966-74eb2d504fe2 | -2.72044 | -57.48202 | 2024-10-30 04:44:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0016ff66-9baf-3f75-8f2f-9201333af2ae | -2.72023 | -57.4833 | 2024-10-30 04:44:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 665c588d-1087-3714-bb4d-4ea01acafbee | -2.64106 | -56.95137 | 2024-10-30 04:44:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc140df0-1729-33be-b1e7-8cbbc401a61b | -2.54114 | -57.34969 | 2024-10-30 04:44:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37f236e9-b1f1-323f-8fe1-4ca54a90bca9 | -3.61636 | -58.55318 | 2024-10-30 04:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ec85856-107a-39c9-8469-9f8709dbb007 | -3.61132 | -58.55232 | 2024-10-30 04:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 51ff11c7-275f-350d-a901-5dccaf989987 | -3.55402 | -58.67863 | 2024-10-30 04:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f7c6ca61-b485-3a2c-a4e2-a9c6746bc5f7 | -3.54943 | -58.67481 | 2024-10-30 04:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98d2255c-e474-3a9a-b18f-e981876b1bb7 | -3.54894 | -58.67778 | 2024-10-30 04:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d31f10ed-97ea-3bd3-863c-9ff4e6238499 | -3.07391 | -59.21462 | 2024-10-30 04:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91d389db-daf8-33f2-9701-1a321579d741 | -3.06859 | -59.21375 | 2024-10-30 04:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8003d15c-45e2-3244-842c-8d73cbc0a47a | -3.98554 | -59.14553 | 2024-10-30 04:44:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 148ceef0-8dc8-39d6-b037-2a7b05d74dec | -3.98501 | -59.14869 | 2024-10-30 04:44:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a18d9962-47ad-34ea-a159-be01ec9e94b6 | -1.42784 | -60.28986 | 2024-10-30 04:44:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf617947-805f-3fd8-a5f2-089129e7852e | -1.42648 | -60.28711 | 2024-10-30 04:44:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b265b32c-3c0f-3bda-b3ba-f875eb1a1fd6 | -1.42266 | -60.28464 | 2024-10-30 04:44:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 827d9f9b-01e1-3c64-9015-ca4c7bcb136e | -1.422 | -60.28878 | 2024-10-30 04:44:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34de09df-dcca-3e8c-adda-f047440926ec | -1.42063 | -60.28609 | 2024-10-30 04:44:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dda57159-4c23-340b-b8d9-3c3971d73014 | -3.6583 | -61.09071 | 2024-10-30 04:44:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9eea2d68-157e-3808-8dda-a14b221a769b | -3.65234 | -61.0897 | 2024-10-30 04:44:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| e99d7f4e-87d8-3661-a6de-99be2d14e2a7 | -7.86874 | -46.89507 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25730bd5-c557-366c-a865-16d8cfec5b68 | -3.04469 | -40.06651 | 2024-10-30 04:44:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3af1fd9d-c2b9-34c2-97af-6fc6e99778d0 | -3.0441 | -40.07045 | 2024-10-30 04:44:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3dc9e05f-afec-3973-af66-a0cde54d8059 | -3.03837 | -40.06956 | 2024-10-30 04:44:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7a24bbe6-c49a-389a-9e9e-f7e85c0960b2 | -3.9584 | -41.47655 | 2024-10-30 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 68eb88f5-e494-3275-bf46-c9dad8d68439 | -3.95312 | -41.47574 | 2024-10-30 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 55153219-cc5f-3a62-ad04-3aefd411d35e | -3.95266 | -41.47893 | 2024-10-30 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 652b1ac9-87ea-3e53-9277-c58e01282fac | -3.94738 | -41.4781 | 2024-10-30 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2fec6595-76eb-3dcb-a511-225374b101f8 | -3.94691 | -41.4813 | 2024-10-30 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| af23233b-3545-3d0b-bc93-56d4b5e7a617 | -3.93731 | -41.48341 | 2024-10-30 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8f8c6cc5-d18f-3317-a28b-8ad5a574184a | -3.93588 | -41.48294 | 2024-10-30 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 664fb3f4-a919-3191-b756-d69ed24fc88f | -3.93202 | -41.48264 | 2024-10-30 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ddece17f-e9e0-3054-bf50-4cdbf32a6420 | -3.8514 | -40.70337 | 2024-10-30 04:44:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 04c6c955-e6dd-395d-902c-ebeaa6b24ba7 | -3.85086 | -40.70708 | 2024-10-30 04:44:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5aaa4ef8-eb44-3670-8bdd-644728c4f732 | -6.35208 | -41.5693 | 2024-10-30 04:44:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8e47ee4c-b7f1-335f-968f-e5cb35b6b68a | -6.34616 | -41.57188 | 2024-10-30 04:44:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c5976210-5878-3b6a-9bf7-31547bddd14d | -5.619 | -41.72635 | 2024-10-30 04:44:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1fe16301-c43a-3975-8899-cf1c10b840bc | -5.61367 | -41.72556 | 2024-10-30 04:44:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e5589375-bb35-3849-9ca4-803fb3544b43 | -5.61091 | -41.72388 | 2024-10-30 04:44:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2c07d688-d8cf-3552-b806-e9947bce399d | -5.60834 | -41.72481 | 2024-10-30 04:44:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README70.md)
