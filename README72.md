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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a4c1325-ba1f-352a-997a-9508f7ee5c75 | -1.29906 | -55.46239 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8935e9df-8b13-37ae-9c0a-c4ae22046999 | -1.29109 | -55.74826 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0315e745-2ca7-3f5c-80ba-2069b6f95ad9 | -1.28777 | -55.74774 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4f3f272-990c-3cee-9647-8d9598efdcb8 | -1.27063 | -55.40455 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a8f552f-4485-32ce-8891-76c504712481 | -1.2587 | -55.30638 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2f8e8720-d05b-321b-8bc9-819cc74e0ab4 | -1.20706 | -55.29519 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7cad9ed2-ce92-33e3-b1e4-53370ef585e4 | -1.20374 | -55.29463 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8e9bd95d-fbd7-3898-9357-9375b512ae2a | -1.19012 | -55.42441 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e66de9e3-1f09-3891-85ce-79c9877b22fc | -1.18678 | -55.42391 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d7469f8-fca8-3745-9e51-620d24b37f02 | -1.17527 | -55.75147 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84b69978-7759-3e77-82c5-f7ada7d1831b | -1.1723 | -55.40752 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2b7d713-5c3a-3e3a-b53d-4bef9eaac644 | -1.16177 | -55.40938 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d6f0616e-a0f7-37ad-ba2a-1822f63a7301 | -1.15845 | -55.40883 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15e6056d-41df-3438-b3db-adea2a084d52 | -1.14739 | -56.01533 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ccdb57f-c6b0-3583-b34a-0ec9e6f80aec | -1.13793 | -55.79882 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1268b44b-9753-3f23-9932-7e5a8af67c2f | -1.12826 | -55.70902 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f3c619e-c018-3292-b5e6-88022bd320e0 | -1.12494 | -55.70851 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49057fab-3ee1-36a1-a762-b14a0cbf8171 | -1.09552 | -55.67928 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42ad102a-3177-39b6-bbf3-88c73f7aa6a6 | -1.09492 | -55.66145 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e161b54d-a6f6-35ea-aef0-e245d19623e5 | -1.09383 | -55.66839 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 439e1dea-709a-3cc3-b8a0-c1262e931864 | -1.09328 | -55.67186 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7dfe3d8f-12e3-340f-a7ee-0573e4e02307 | -1.09267 | -55.65408 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9cbef35-ea24-36e9-be86-1228ab8e512a | -1.09213 | -55.65751 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7afd63f-1359-35c4-953a-f8010ad284dc | -1.09159 | -55.66095 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6bae815e-0379-3057-9d29-cae9cd34cee9 | -1.09105 | -55.6644 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 80ce1fc7-0e20-3051-8e8e-1861fda5b77c | -1.09051 | -55.66787 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20f9350e-39b2-3523-96a6-df50d4de7e3e | -1.0899 | -55.6501 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40111297-9392-3376-99db-a6dc347d6c16 | -1.08935 | -55.65357 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 549238ff-a8d9-334c-bc98-d49a31ded8dd | -1.08881 | -55.65701 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01c8b717-a96e-317d-a45a-d5efce4ec1cf | -1.08827 | -55.66045 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46688e70-440a-3317-89b4-b58106c0bcd3 | -1.08773 | -55.66389 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8169a00e-6a2c-34e1-a8ff-d0cd7f83dada | -1.08719 | -55.66735 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be6da0d0-e1cd-3440-acfe-43898a5c333f | -1.08657 | -55.64959 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c7623a9-2916-3940-bf08-36b896a1ea6d | -1.08603 | -55.65306 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62ab03c6-52e2-3450-8b83-2cae6cfddb86 | -1.08441 | -55.66338 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40526883-cb9f-3c92-9390-ffa951e87c05 | -1.05163 | -55.78547 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfef32a6-0c3e-3ab2-a04b-730d19dc6426 | -1.05109 | -55.78892 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b382d4a-996f-36cf-8668-ca851593f934 | -1.04777 | -55.78841 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9adc74aa-a545-3918-b26c-e2001c8d18b2 | -1.04724 | -56.13739 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 515a8c6d-48ee-337e-8f8b-b0230e04a87e | -1.04723 | -55.79186 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6aee1faf-7dc5-3df4-9e59-708e3670aadd | -1.04669 | -55.79532 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c83df0d4-7b5a-3b84-9dc1-873c4c8cd924 | -1.02278 | -55.66793 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 703affd4-f15b-382c-a41e-b1a3383b8cc0 | -2.17681 | -55.62361 | 2024-11-03 05:08:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08b66e14-d844-3ff7-bd12-dfa549702956 | -1.87372 | -56.02621 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 947e203f-33e1-3926-820b-2a3e25632340 | -1.87317 | -56.02966 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc8883eb-7cba-3f57-9a0b-feb440225371 | -1.87263 | -56.03311 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f0f12ac6-a6db-3b1d-ada2-66b7379b84e9 | -1.87209 | -56.03656 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c3c8a940-1892-3f0e-8de5-343a7f6b05e6 | -1.87117 | -56.23462 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97076619-fc0f-376b-a007-3abd33097ea0 | -1.86931 | -56.03259 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a34b5ab7-389a-3a52-8341-ffce06e6c46d | -1.64935 | -55.23803 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1626e990-8d42-3d74-8c68-a131ce399160 | -1.6488 | -55.24154 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e15023a-f296-3bdd-ad03-557d042be6c3 | -1.64545 | -55.24102 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8007a066-b9cd-334e-9170-3e7e1c357c79 | -1.63648 | -55.68183 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b7658e6-6466-3e32-82db-902248ee3bbd | -1.62958 | -55.407 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 38db3129-91ba-3882-8444-da997e802d58 | -1.62903 | -55.41049 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 891f28b3-d41a-3548-8c98-c7b86f938314 | -1.60615 | -55.62054 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9b138bd-64ac-3538-b3a7-257c45c3d1e5 | -1.60283 | -55.62002 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b740b45e-cb5f-38d0-be51-cd1245ee1d12 | -1.59844 | -56.24807 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba6fa97a-ccdd-3957-a6b4-365cc583444a | -1.5879 | -55.19252 | 2024-11-03 05:08:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3050270e-6763-3bb7-b255-c7fb5cdcaa01 | -1.58291 | -55.10171 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e50b3bc2-9e7e-357d-83af-88f60e534ca4 | -1.57955 | -55.1012 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15421dc7-1711-34dd-bde3-1e0f79e6264f | -1.54656 | -55.09249 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00abdb72-ae6c-325f-9562-a83b89ac6cff | -1.54108 | -55.73096 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 78b4fdf8-38ac-3a20-b8db-95d634b97320 | -1.53776 | -55.73044 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a78cab5c-d213-39d7-a8a6-d72a0c7c24f4 | -1.5168 | -55.75552 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1aa8e193-1bbb-3b80-a3ac-eedced288bf0 | -1.4398 | -55.42399 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed4e9b19-836d-3c62-bb9a-a24919f7dd84 | -1.39074 | -55.84548 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 569ea68f-cea4-3e18-bbd8-ba84af50d672 | -1.38356 | -55.8479 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f762fa6-999e-3dfa-abfd-da7b38a0bf6f | -1.37127 | -55.30228 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9022d1e8-2496-31b2-999c-ea1d6cf5cf45 | -1.36033 | -55.37206 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cd64953b-2f98-349c-8317-1056748ee9eb | -1.30844 | -55.81103 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0193552-2b54-3ea8-bd94-bcb65ff8f9ab | -1.28445 | -55.74723 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 927a65c1-c25e-3644-a325-a47c6fbee107 | -3.62186 | -55.59956 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 21cffb3f-1c7b-309a-8f8d-2d9585867bb2 | -3.53519 | -55.52867 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f9e5837-8267-36a2-a2fb-3f970a11bca9 | -3.45318 | -55.38171 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dd9d1a4-002e-39e7-bfef-b7f0c43361b3 | -3.4039 | -55.41046 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a91e237-6d53-30bd-98c8-1d4b779a604c | -3.38675 | -55.49862 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d59b6826-cb50-3834-93d5-481db97404af | -2.56486 | -56.49097 | 2024-11-03 05:08:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4240ca0-da6d-3196-954f-174f4d7d721c | -2.17537 | -56.47235 | 2024-11-03 05:08:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9170cd34-d63e-3a6e-8d68-ca84da1f14ee | -2.13335 | -56.24716 | 2024-11-03 05:08:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82f33b33-bf06-30ca-bd6c-3f867836c3b2 | -2.11444 | -56.38885 | 2024-11-03 05:08:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed4ee3a5-f095-3dc6-bc02-2214347455e4 | -3.62856 | -55.60059 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 31760a1d-5329-3255-9790-f4f22caf063e | -3.62521 | -55.60007 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9f42a7a-1610-311a-b825-6501299976e7 | -3.54637 | -55.52316 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8dce8276-11ce-34b4-ab10-904e3a26aa0d | -3.53463 | -55.53223 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14ba77e9-be10-3af0-9bdc-4a30fdda28b2 | -3.53239 | -55.52462 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 370f8d9c-fd80-3474-896e-d969882b61e5 | -3.53183 | -55.52818 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 814fd8f8-1a86-33fe-9a1b-fb9aa0dac9af | -3.45435 | -55.41827 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93fe381d-0825-3dbd-91ce-0f490bb05163 | -3.40335 | -55.41401 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb4b1bdf-a586-3fdd-8795-96aacb9e23cc | -3.92188 | -55.42778 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3578cce3-b5de-3edd-8a5a-1b65fe7ba310 | -3.89803 | -55.50448 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6944d010-c897-36c2-acbb-dfc7bf45c8eb | -3.8172 | -55.69136 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 816ace3d-582e-3883-9906-4888a9234c5a | -3.76949 | -55.39317 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e84b8e74-4264-3cac-b49a-7ce043677066 | -3.68683 | -55.94344 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34710f7d-6a92-32cb-a8f1-7612f98dc03d | -3.89467 | -55.50395 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 991ac7b4-5220-3402-b1fe-b6df774f6b2e | -3.77286 | -55.39369 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1293d307-b869-368c-8168-5ca6a2b62b16 | -3.76833 | -55.76298 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2be0a169-081c-3b88-83ff-9dfcbcbb640f | -3.73873 | -55.45769 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 350bfd6b-33a6-3356-8801-b82bef1b12aa | -3.68737 | -55.93996 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb92ff92-6d6d-36cf-bac7-e2fe3b53907f | 1.89559 | -55.87181 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README73.md)
