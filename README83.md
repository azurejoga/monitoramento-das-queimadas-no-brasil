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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e2faea0-5a4c-33a5-b3d6-983f686d7b8c | -6.77205 | -59.44887 | 2026-08-22 07:41:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 19c7b4dc-fbc1-39b6-bf56-3f9dc387f41a | -6.76066 | -58.66785 | 2026-08-22 07:41:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 720e24b6-15a0-3047-b3cf-a8b9b4d58a57 | -10.8172 | -50.9711 | 2026-08-22 07:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 52.0 |
| c904a9c6-a423-34fc-b953-2415213caefc | -8.3903 | -62.6963 | 2026-08-22 07:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 79a9623b-784a-39b1-bd56-c26bc1ee1fa8 | -6.7833 | -59.4208 | 2026-08-22 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 5e009d4a-0160-3b43-bae6-bf2eff227750 | -6.7507 | -58.6687 | 2026-08-22 07:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 8acbc4ae-a10c-36a8-a8e1-3c91c17b4b6a | -8.3904 | -62.6774 | 2026-08-22 07:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 435acdb6-5274-3927-a767-34a5e56efeda | -6.8019 | -59.4008 | 2026-08-22 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| ebcb561d-af55-3fce-91d8-875082ad07f3 | -6.8018 | -59.4201 | 2026-08-22 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 499741c9-4566-302e-848c-9ae0fa698cc5 | -9.1722 | -59.4629 | 2026-08-22 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 952e4368-b828-3790-888e-e8564ed652d2 | -14.3744 | -51.8038 | 2026-08-22 07:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 60a73839-5011-3112-b11f-b13190a6b217 | -8.3719 | -62.6781 | 2026-08-22 07:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 92f7ea2b-161c-3a4b-b4ab-995146a0407d | -9.106 | -60.9127 | 2026-08-22 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 1ff2676b-0049-3eee-ada5-3cf02399ac6b | -6.7692 | -58.6679 | 2026-08-22 07:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| fd07adaf-0b1d-3207-aa8c-f4d35773efdc | -6.7833 | -59.4208 | 2026-08-22 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 77dd9e6c-fd84-316d-840b-2058e2827b75 | -9.1722 | -59.4629 | 2026-08-22 08:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 08ec6052-2fc6-308c-bba3-d27510272d11 | -6.8017 | -59.4394 | 2026-08-22 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| de49ebd6-4d10-3fd8-8416-aa567e100cdc | -11.4733 | -54.322 | 2026-08-22 08:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 39ef1e0f-e64e-397e-8f7b-d178adeb9f78 | -10.8172 | -50.9711 | 2026-08-22 08:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 34dfeb35-ac3e-3ccb-b136-944ac16ebeea | -6.8018 | -59.4201 | 2026-08-22 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.5 |
| bfe6351c-5907-33ee-b4f8-2f86924a7c8b | -6.7507 | -58.6687 | 2026-08-22 08:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 5632c154-2ee6-3b77-aeb8-de89cbcb4054 | -6.7692 | -58.6679 | 2026-08-22 08:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 1c8389c0-fd82-3e21-ae62-9e7b1142010e | -9.106 | -60.9127 | 2026-08-22 08:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 292966a8-a891-3a86-9ccd-d4f787edc63b | -8.3904 | -62.6774 | 2026-08-22 08:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.5 |
| f0e85b6f-1a7a-3d3a-abdc-b45755d9a482 | -6.7833 | -59.4208 | 2026-08-22 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 83b460ea-5907-3b17-9f9b-2778355378c1 | -9.1722 | -59.4629 | 2026-08-22 08:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| d1b3e210-8744-3f46-a95c-81dd9cc0e467 | -6.8018 | -59.4201 | 2026-08-22 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.7 |
| aac0a11f-219c-37c0-870b-9aac182c78e9 | -8.3719 | -62.6781 | 2026-08-22 08:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 9509d9ed-f440-3c1c-9e7b-fc8e8d51c38e | -6.7692 | -58.6679 | 2026-08-22 08:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 39e61f5d-dd93-3bf3-8c95-b2af8cc29627 | -8.3903 | -62.6963 | 2026-08-22 08:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 0e583815-28b7-3581-8481-407b830e7ded | -8.3904 | -62.6774 | 2026-08-22 08:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 69097bdf-235d-3da2-a6e7-1ee1c7cb2a04 | -6.7833 | -59.4208 | 2026-08-22 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 1f634416-90ef-3765-8e73-05700c9d83af | -8.3904 | -62.6774 | 2026-08-22 08:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 81.8 |
| d0c4eb1a-8dc5-3581-9543-bb0d3966e2d1 | -6.8018 | -59.4201 | 2026-08-22 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 24f3ca4e-f1b1-396a-a1d0-95f064ad7bf2 | -11.4733 | -54.322 | 2026-08-22 08:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| b3b27d2c-9df6-38d3-af6c-9640612f9e6c | -9.1722 | -59.4629 | 2026-08-22 08:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 6cfb0174-ea72-31a3-930a-3ac4944ea423 | -8.3719 | -62.6781 | 2026-08-22 08:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 09a4284d-17ad-3e2a-8b81-59254fbadfef | -18.2855 | -43.3119 | 2026-08-22 08:20:00 | GOES-19 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 106.0 |
| ad3bbdfc-59a0-37d5-876e-8827bfe35fd5 | -6.7692 | -58.6679 | 2026-08-22 08:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| b1ca17af-2446-3317-8711-f6e8ec817e3f | -9.1722 | -59.4629 | 2026-08-22 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 606403ed-bfc3-3b9a-aab5-d7796e10adeb | -11.4733 | -54.322 | 2026-08-22 08:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 7983d05b-a125-3a41-b843-50d61633f710 | -6.7833 | -59.4208 | 2026-08-22 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 22ad477f-616a-3a41-a8b2-000e325ddc71 | -6.8018 | -59.4201 | 2026-08-22 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.2 |
| b24bd20f-3f09-387a-a5e9-20c53e92c483 | -8.3904 | -62.6774 | 2026-08-22 08:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 4dba3726-b951-3115-b52a-f6c832408064 | -18.2653 | -43.3169 | 2026-08-22 08:30:00 | GOES-19 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 33ff7917-b44b-3917-9cc9-e558291aeef1 | -6.7692 | -58.6679 | 2026-08-22 08:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 7c3c887e-d7b6-3e85-9457-8cf0cfc1597a | -18.2855 | -43.3119 | 2026-08-22 08:30:00 | GOES-19 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 107.7 |
| 44eff56e-e0cd-376f-b674-001a08bb2832 | -12.7605 | -48.401 | 2026-08-22 08:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 9f25a1fe-7148-3311-b8fc-5b8584b5c6de | -6.7833 | -59.4208 | 2026-08-22 08:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 9cb96ce1-0fa0-3884-8ee0-3d7c44b2fed0 | -8.3904 | -62.6774 | 2026-08-22 08:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| c89390df-06de-3a0f-9d81-af9e17ad4489 | -6.8018 | -59.4201 | 2026-08-22 08:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 48d381bd-5268-38cf-9073-69cfdb8fee17 | -6.7692 | -58.6679 | 2026-08-22 08:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 9544d02b-d4ab-333e-8687-285fba48232b | -9.1722 | -59.4629 | 2026-08-22 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 3abb3425-e892-35df-a39f-157a45f351fa | -6.7833 | -59.4208 | 2026-08-22 08:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 962b1336-2652-379a-8a98-5a3cd81018c1 | -9.1722 | -59.4629 | 2026-08-22 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| bf625fba-ebfe-36c5-b734-07e9a32a82a2 | -6.8018 | -59.4201 | 2026-08-22 08:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| a9eff393-a6ba-37ab-982d-caf49bd638d4 | -6.7692 | -58.6679 | 2026-08-22 08:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| c82ad3c5-33a4-332e-8296-b4e39817aea0 | -9.1722 | -59.4629 | 2026-08-22 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| dc243048-36ee-30ae-b7b1-895334dfa60d | -6.7833 | -59.4208 | 2026-08-22 09:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 1c0ff924-acb7-3464-b629-be48b7c91e35 | -6.7878 | -58.6477 | 2026-08-22 09:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 4fd67493-4eab-3e3f-95cc-402cf0ed878a | -6.7692 | -58.6679 | 2026-08-22 09:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 6601efbc-15de-3354-9323-42e9b5293d46 | -6.8018 | -59.4201 | 2026-08-22 09:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 6a5036b4-5d66-3f90-9990-66d2efc7f488 | -6.8018 | -59.4201 | 2026-08-22 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 4b4b2477-b8c8-3e70-9d4a-35312bd15dca | -9.1722 | -59.4629 | 2026-08-22 09:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| c7bed17d-9d0d-3401-945c-63a8ce3bbcd9 | -6.7833 | -59.4208 | 2026-08-22 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 8a3623ac-3353-31ab-b4f1-106b5afea07c | -6.7692 | -58.6679 | 2026-08-22 09:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 13fc4741-902f-3c49-b109-dac37f99c3b2 | -6.7692 | -58.6679 | 2026-08-22 09:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 1ecb130c-e5c8-35a5-8b53-3db8c91fa37f | -9.1722 | -59.4629 | 2026-08-22 09:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 3b1e57da-61c9-38d6-8f8c-aed7e6453843 | -6.7833 | -59.4208 | 2026-08-22 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| d2ace580-f682-3c55-803e-98e21a615702 | -6.8018 | -59.4201 | 2026-08-22 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 27e733ee-7445-3772-aae1-228b6007c8c6 | -11.4494 | -44.5353 | 2026-08-22 10:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 14fed8f5-856b-38e4-91ab-7cbdcf34322b | -6.8018 | -59.4201 | 2026-08-22 11:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 9385c046-fc0d-380d-bf16-eab297db3eef | -11.4494 | -44.5353 | 2026-08-22 11:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 264.6 |
| acfe9e65-0a6f-3ca6-b6f0-6ac4489a6ecf | -8.522 | -54.8209 | 2026-08-22 11:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 508bd4e0-277b-343b-bac6-8f3467e40750 | -11.4494 | -44.5353 | 2026-08-22 11:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 412.8 |
| 5392aacc-51ac-3c43-b51c-e16e21a75bbc | -11.449 | -44.5587 | 2026-08-22 11:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 066e43c5-8201-3b07-886d-f7da856c5f95 | -12.37654 | -43.44772 | 2026-08-22 11:15:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| de27ce71-506c-39d8-9bab-594ea65f6e34 | -7.1507 | -43.10918 | 2026-08-22 11:15:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| ede6a861-714e-3738-9a81-9d5aa41a2477 | -7.65147 | -43.9739 | 2026-08-22 11:15:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 54eb9358-50c3-3258-8278-e0ad0111b881 | -12.87616 | -42.52914 | 2026-08-22 11:15:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 7a58499d-a058-3555-a6f6-963530227e61 | -12.27738 | -43.16558 | 2026-08-22 11:15:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 040ca3f0-51d7-3652-b70c-74a3fec29f1f | -11.4469 | -44.53446 | 2026-08-22 11:15:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 476.8 |
| ac2386f6-9043-34cd-b5b1-4301453f7255 | -11.45562 | -44.55061 | 2026-08-22 11:15:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 4ce8cccf-28c1-3444-ae19-5636d6dc11f5 | -8.58153 | -36.91551 | 2026-08-22 11:15:00 | TERRA_M-M | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 5754c641-ad20-3c97-9023-8426e4637667 | -4.70427 | -37.38127 | 2026-08-22 11:15:00 | TERRA_M-M | ICAPUÍ | CEARÁ | Brasil | 2305357 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 6c3f7475-e5b9-3368-aa48-13251c88ec69 | -11.58881 | -46.57648 | 2026-08-22 11:15:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 85511023-2572-3ecd-ad64-156931e9facb | -11.4579 | -44.53623 | 2026-08-22 11:15:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 0391bb0a-38d7-3ff9-9a0c-7b23859f279c | -7.14006 | -43.10771 | 2026-08-22 11:15:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 59b05eed-a3b9-344c-bb8e-c13589aee41e | -11.6324 | -46.5494 | 2026-08-22 11:15:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| bb74c988-02c3-3fc7-af0f-47d1c482e471 | -6.88167 | -43.7395 | 2026-08-22 11:15:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| c96024f9-dfe8-3914-a48c-79a46aa83dae | -11.60505 | -46.5583 | 2026-08-22 11:15:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 35.4 |
| e36ea279-3b60-3c2c-ad6a-eaac61be7ec5 | -9.1781 | -38.73117 | 2026-08-22 11:15:00 | TERRA_M-M | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 0e2821fa-a821-36db-90f5-205d0344752e | -11.44918 | -44.52014 | 2026-08-22 11:15:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 68e59f68-f38f-38d9-8cd4-42c2e4899179 | -15.73136 | -42.3823 | 2026-08-22 11:17:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 658cc1fd-5888-3909-a360-9ac0a3a278b5 | -17.96621 | -44.43268 | 2026-08-22 11:17:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a40a718e-eada-39a7-98ee-dbdac6af4cf1 | -16.83776 | -46.34276 | 2026-08-22 11:17:00 | TERRA_M-M | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 86865046-a9f8-3dca-8c06-4166a1046811 | -17.71506 | -42.25915 | 2026-08-22 11:17:00 | TERRA_M-M | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| e2baa480-bbd9-376c-bc46-dfdee1085032 | -20.42225 | -45.44192 | 2026-08-22 11:17:00 | TERRA_M-M | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| e03d78e5-64e0-3b37-8f4c-a0ceb9ea1208 | -17.60867 | -44.61996 | 2026-08-22 11:17:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 76.8 |
| d53bafeb-b727-32e7-8cd0-69b59466097a | -12.83462 | -48.45309 | 2026-08-22 11:17:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |


[Clique aqui para ver as próximas entradas](README84.md)
