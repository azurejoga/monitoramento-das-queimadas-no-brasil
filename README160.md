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

## Dados Diários - Página 160

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7d0eb4d-d5bc-3a16-be11-23516d5e35d1 | -12.4716 | -64.03689 | 2024-10-02 05:12:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62d3d8ec-91d6-37dd-9aa5-cf6daf48ada3 | -12.47225 | -64.03317 | 2024-10-02 05:12:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d036c61-2794-31ac-a48f-c587a59d0af2 | -10.52059 | -65.28548 | 2024-10-02 05:12:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44fbae51-afd7-3900-b7a5-a3dfb6247de2 | -10.44258 | -65.08844 | 2024-10-02 05:12:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49b9c130-7a4c-3c54-bc0e-618c5909c974 | -9.98659 | -64.77065 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7e025b0a-78f5-3806-8b7b-cabe582c9759 | -9.98398 | -64.76752 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b2c883e-fc9d-3480-aa48-4944d4f0e721 | -9.98316 | -64.77204 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b35b226f-b75d-3b26-b44a-981a15ff338c | -9.98211 | -64.76986 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f20c29c-f221-36b2-8b21-560d4a682277 | -9.97079 | -64.78167 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c55aa7d-93dc-30d0-bdbc-600b96a436e3 | -9.96787 | -64.77193 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2eb9ec61-3527-3073-b4d6-765b8c4feae7 | -9.96709 | -64.77638 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a16f1d6-9e58-3299-aa1b-90ddc51388f7 | -9.96701 | -64.93675 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2136cb39-b757-390f-8d46-0385ae055427 | -9.96684 | -64.93857 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2095418d-eb07-39cf-88bd-e2322f897eb5 | -9.96631 | -64.78084 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 781b81e5-ae52-3237-81c1-73c9ef866ca7 | -9.9634 | -64.77108 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e9e5389-9c7b-32a7-a1b4-cba57f408441 | -9.96247 | -64.93596 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2768e4fe-eb5c-3a77-ae1a-f895f517afa8 | -9.96231 | -64.93777 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ca82a1b-bd82-3734-9bdd-3d55d387a83c | -9.95373 | -64.90574 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1365776-6883-3d2c-b6c5-ef868697cc82 | -9.95002 | -64.90028 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 26b4d157-57c6-372c-aaa9-42a4c34a5298 | -9.94921 | -64.90488 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bf2f6f73-3077-3723-93c5-1b4ed6b3e046 | -9.9484 | -64.90951 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.3 |
| b3546c59-4ca5-332d-ae1a-ff09daaa72ce | -9.94759 | -64.91415 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.3 |
| f6bd554e-7e41-30d7-96f6-2658d71a3b6d | -9.94677 | -64.91884 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e354dfc8-66ee-3cf6-b235-a0a3c402087d | -9.9455 | -64.89946 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a7c3988f-8732-33e3-910c-13baea69f2bb | -9.94469 | -64.90406 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7102f045-025e-3133-9ade-bb2489f12a9d | -9.94388 | -64.90867 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 00fe3a80-2e6c-3c38-b4b7-c4cfb8d1a671 | -9.94307 | -64.91329 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 1d9769a6-a076-307c-8db6-3837fffb7705 | -9.94225 | -64.91795 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 00208856-624a-3bb1-9c3a-f92ee0664fb2 | -9.94143 | -64.92261 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 65926424-74f8-3d52-b8a6-71861a566087 | -9.94016 | -64.90324 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 32729de6-4706-3c74-9ed0-39aadaa27995 | -9.93935 | -64.90784 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 08f03675-5e87-3ff4-af51-c310284ab419 | -9.93854 | -64.91245 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.9 |
| b633b87b-0978-3898-8b9c-1534f9bc8247 | -9.93773 | -64.91706 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2d9dc8d7-b9cb-3b3a-b7c0-9e8fc13c27d9 | -9.93692 | -64.92169 | 2024-10-02 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c1f0900e-1348-3700-82db-dea4f61e27c5 | -11.65291 | -65.20177 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2078ae9a-475a-3e61-a13e-53119c57d9ae | -11.68631 | -65.00283 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| adb16339-7774-3ee1-b36e-fb5580ffddfc | -11.68385 | -65.00016 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4f7752fe-3f5e-32d4-b7a0-65860ffe3b2d | -11.68308 | -65.00453 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 15.7 |
| cdda8bc3-5987-34f4-b5e1-a005f1af080d | -11.6819 | -65.00195 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 77410061-fb97-3333-9d41-7ceef05ccb28 | -11.6811 | -65.00631 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 30931c86-5a1c-3755-ae68-aa8bdb2cecae | -11.67944 | -64.9993 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5b12d192-5619-3eab-93ce-178926ec18a7 | -11.67867 | -65.00364 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f301fee5-ea7f-3509-ba7e-a8a52b006924 | -11.6779 | -65.00803 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9398754f-d983-30f6-8cce-4c4eb2c1e773 | -11.67749 | -65.00109 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5cbf4a2d-34d9-364b-8bcd-1a5f43aecca3 | -11.67669 | -65.00544 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0f8839f7-4cd3-37e2-a050-e7ed9870946a | -11.67588 | -65.00982 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 40716463-ebd5-3c18-bbde-1c8508eaa50f | -11.67426 | -65.00278 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6901668d-7377-3024-816b-710f863c27d6 | -11.67349 | -65.00716 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 30091bf9-ff65-383c-a394-bb217782df48 | -11.67308 | -65.00024 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c0974191-eb41-3f3f-bb36-2f1c150fa812 | -11.67271 | -65.01157 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a30d0ab7-02d4-30c9-b815-80270f609b7d | -11.67228 | -65.00458 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 56ceb5fa-edfa-3f9f-a16b-0d18dcab4599 | -11.67147 | -65.00896 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f64ac5a9-ed54-3c9b-9a5c-7d8174d95911 | -11.66907 | -65.00629 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0ca7b28b-95de-3423-83cc-61fc6a90a71d | -11.66829 | -65.0107 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 782dce12-bd78-3a53-98fc-8dd830444dbe | -11.66776 | -64.98792 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 791ca2c3-0093-3cb4-97fc-57d147a14bc6 | -11.66466 | -65.00543 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 856c1adb-f93a-3584-9bfa-8f9b997d0215 | -11.66413 | -64.9827 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7c3e05cf-fc6a-3559-9850-0d35e5634f46 | -11.66387 | -65.00984 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2f0d6f2e-f70e-379b-b37f-43b34cc71f1a | -11.66335 | -64.98711 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ec808482-7b67-3075-9d58-48b7b092e7dd | -11.66309 | -65.01427 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5f82a85e-5c5f-3a18-8ba4-75e0d5bce6e5 | -11.6605 | -64.97747 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2eb47559-fbd7-32e7-83f0-c6251bc7a97d | -11.65971 | -64.98188 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 63de2e73-34a4-3a52-b402-8edb3d0d52a4 | -11.65893 | -64.98627 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d722879d-453b-36de-8570-01fb803c13aa | -11.65867 | -65.0134 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a7a5b38d-1071-38f2-87d5-814f770e89cb | -11.65788 | -65.01784 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6c24d9d4-ba61-34ca-903d-52d3388dc699 | -11.6553 | -64.98103 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66adb307-b441-38a9-adee-ca9a88e9882a | -11.65452 | -64.98542 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 235defd4-d614-38da-b057-fd1aaea55fae | -11.65392 | -65.20397 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f2e6c086-f5b2-31da-a60e-d1597959d705 | -11.65374 | -64.98978 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b98c3e1e-e2ef-3731-9d1b-c4739cf42d00 | -11.65347 | -65.01696 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 42b8cb4f-6754-3fc0-9ead-715410e2e567 | -11.65011 | -64.98455 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1085febf-016f-36ae-b597-10eb79b73aa1 | -11.64933 | -64.98893 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2ad70b2-f61b-3fb9-ba2e-8735978633cc | -11.64904 | -65.01613 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2b44b89-8853-3bb7-b582-2159c3f98803 | -11.62569 | -64.9934 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7910df16-20b2-373c-b247-a761878734f1 | -11.62048 | -64.99699 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59481f46-abac-3592-be8b-4e7ceb35cf81 | -11.61606 | -64.99613 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e47157f-58b7-3d70-b01e-c6017f6879bc | -11.61526 | -65.00054 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41fb493e-95bb-3d35-a1f6-0c4b584bac2e | -11.61446 | -65.00496 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6193a365-2565-3357-bc04-9ff7e618f434 | -11.28815 | -65.27158 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a53c0eae-07e4-374c-81b3-d4404ba4798a | -11.28362 | -65.27072 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2a4284eb-3c7b-32e9-9c1c-e121f7ca9d28 | -11.25456 | -65.02045 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b2bf436d-e410-3f94-8a4d-53ef8f4dd10c | -11.12477 | -65.06374 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a811615-8305-3d7b-91d6-75c78ea6b3d9 | -11.12273 | -65.06433 | 2024-10-02 05:12:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9f1e095-b994-39c7-bacd-500bb7d1b6fb | -10.90623 | -69.2979 | 2024-10-02 05:12:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1503113a-6e14-32ef-8954-0f449a569b1c | -10.86684 | -69.49789 | 2024-10-02 05:12:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c05c7a06-cf6c-335c-8f82-b35490c84e7d | -10.86597 | -69.50227 | 2024-10-02 05:12:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5507fa38-7a66-3c17-815c-f18d07a1f2e4 | -10.86086 | -69.49657 | 2024-10-02 05:12:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 11e98001-92ea-32dd-91ba-5c4dadfe5995 | -10.85999 | -69.50095 | 2024-10-02 05:12:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 5957ea1e-8516-3d87-b2ca-bbe0833dc204 | -10.7047 | -69.38815 | 2024-10-02 05:12:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b5bf5e3d-10d6-38a1-8c42-7610f136c056 | -10.69956 | -69.38264 | 2024-10-02 05:12:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f743499d-5c69-3c6a-b275-52fdb534e122 | -10.6987 | -69.38706 | 2024-10-02 05:12:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7aa54856-3abc-3d31-9bca-b7dfc2130b8b | -10.69781 | -69.39161 | 2024-10-02 05:12:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 181910c7-fae1-37dc-93ad-dc13470e5e15 | -10.69182 | -69.39048 | 2024-10-02 05:12:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bda83d56-7178-3bd6-a112-c83a732c603a | -10.67261 | -69.29874 | 2024-10-02 05:12:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d70b4999-f46b-36fb-84fd-f55a2d95a9c7 | -10.67179 | -69.30293 | 2024-10-02 05:12:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ef7ad95-bc28-3a3e-9e3b-567209c4157a | -10.54154 | -69.32534 | 2024-10-02 05:12:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3dc4267-fe7a-3464-bb3b-a5448288b392 | -10.54081 | -69.31776 | 2024-10-02 05:12:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0111e4f-3c73-3e9c-ab83-989249646160 | -10.53998 | -69.32214 | 2024-10-02 05:12:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e538ca0-35cf-36ae-9bf4-d8f0e7a7947a | -10.53734 | -69.31522 | 2024-10-02 05:12:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bb467950-51fd-3f8a-9759-7ae20e7d8f50 | -10.53646 | -69.31966 | 2024-10-02 05:12:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README161.md)
