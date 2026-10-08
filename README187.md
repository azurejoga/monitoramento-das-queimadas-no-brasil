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

## Dados Diários - Página 187

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0b017f6-3740-3469-a336-d000fa84b013 | -3.09673 | -54.28851 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ba9f9ad-f84d-3514-84fe-c52141d483d3 | -3.76945 | -59.40101 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c178f05-6f38-330e-a1ba-6bb28aa0caf0 | -4.30482 | -60.94988 | 2026-10-08 05:42:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8201a93d-474e-3eb6-bbe8-1670f5cc3be5 | -3.16696 | -54.74318 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33c33357-5d2c-3e52-8f42-cd67da684259 | -3.35158 | -58.21028 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97656bb2-0f6a-3ccb-9781-beef25843a12 | -3.30992 | -54.04242 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8363ea8-ab2b-3b79-a2eb-42cb4551e321 | -3.01348 | -54.12997 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 76d381cc-ee6e-3095-bffc-f7c5cbc90073 | -4.15974 | -55.14874 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56405f92-7b02-3539-b2af-65bfeeb2a964 | -2.85363 | -59.11324 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 615dd634-6bcc-3f40-9971-75c2b595861e | -2.92825 | -54.12609 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a13256e2-fe6a-345f-afb5-4e9df480a4fc | -4.52232 | -54.98136 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9820ebc-b3e0-37a3-9f5a-5d66ebcbcf2e | -7.75181 | -54.95803 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c97d2aa6-c9ab-335a-ad0e-074cf1ca7270 | -3.14312 | -53.72006 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89aabf90-9ac8-39be-b10f-4b2331a272f8 | -2.47856 | -56.10934 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b47f626-4b13-31ec-8ba5-6542f9184cce | -3.55345 | -59.47318 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65a5d2e7-6f10-305d-bfae-125be5a0e499 | -6.51343 | -55.38137 | 2026-10-08 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a93c0768-9fe6-3ede-958b-f4a8bedae9f8 | -3.04685 | -53.94489 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f1c575b-c17d-34ce-8601-9eef1d9e5a08 | -6.99224 | -59.11955 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b438a85a-80fe-3f89-80c6-a306e29962ed | -2.85294 | -59.11781 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8857cdbe-6e2a-3f42-b9d4-5b32616db4d1 | -6.85049 | -59.78944 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b608aaeb-a3d6-3ee3-bd65-8bd9694ff79f | -4.37756 | -55.16348 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 949c4c8a-54fb-3fc1-b769-f6920991d0bb | -3.52438 | -54.66577 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f47a218b-44e1-3a5b-9639-b8924a2be684 | -2.78321 | -54.09044 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1bddeaf-0967-3367-891e-2f3d2d2155fe | -7.75535 | -54.95427 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5c4e871-ffd4-3642-8e19-3d14ad988d6d | -5.29847 | -60.09067 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ba1279f-e3d9-3b6a-ac54-517c48c92412 | -3.99375 | -56.25645 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48cbed90-e276-33a9-bbcd-bde945e5ba63 | -3.11215 | -53.77959 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8226ea73-5a4a-320f-a7eb-483827195937 | -3.0466 | -53.91012 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| afdbc1f7-14c6-3a4b-9c4e-13ecf226fd32 | -4.92756 | -55.86985 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 646e5ddf-93b5-3c91-82d7-2b7326aef9fa | -2.87383 | -54.20068 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 934a8008-4560-3d3d-9c19-b90bb37c5ac9 | -3.09793 | -53.71706 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e486acbf-b38e-33f3-bfff-41e568b3a812 | -3.52057 | -54.65581 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0211fa39-d806-32af-a300-802b175fd8ee | -3.86208 | -50.41818 | 2026-10-08 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 322430b4-e114-3be8-9271-3fc5cf846c5e | -7.9045 | -54.71622 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 630f4f58-4ac6-303e-879d-490b3e942d1e | -3.28442 | -54.0454 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a03c0108-f078-34c5-b035-55dd3dcd44aa | -2.49572 | -56.15018 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f433a5d2-5e01-3792-9a1e-e9849da5c146 | -3.56091 | -59.47434 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6ac34073-ce54-3e02-a94f-1bbcfb04932e | -3.10038 | -53.77408 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d368763-ed3a-3aad-9650-b29a33941dd5 | -3.04634 | -53.94823 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 294d8fe1-717d-3a7a-bf5b-f1c010bc893a | -3.08567 | -53.96102 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 1163c53f-7363-3fef-91a5-bea434bb6d4a | -5.85691 | -53.46367 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| cc950015-a9a9-3261-a6fa-8e33a073dc6c | -3.72925 | -54.65966 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8fa4a615-9f6e-36a2-b7b5-45b086567d33 | -3.31427 | -54.05 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d3be2204-35a9-3169-a3fe-06dd59271919 | -4.11254 | -60.71488 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 75840c84-efd5-31e7-8b49-83308728dc64 | -3.08433 | -54.29964 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 073b2735-1e36-3988-9e7c-6f2e5445ee05 | -6.98925 | -59.11201 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1838106-1a8e-3586-a033-11e17b85644c | -3.57484 | -54.31909 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d51a46cb-1f28-358a-abfb-81f7d44e2117 | -3.17615 | -50.59916 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d63efd13-d39f-3322-992e-463527cf8295 | -2.85742 | -59.11378 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4da7545d-f86b-33d1-a4df-3a338aa96e38 | -6.99173 | -59.12301 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21204e62-4467-3480-9566-3ea47ecb057f | -3.29683 | -54.01965 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f1a93e7-a6af-3d5e-be8f-396fce989488 | -4.378 | -55.16054 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c6fd666-e370-3958-991f-0590b95cf4a9 | -5.23335 | -56.11687 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 67983436-b2ab-33a2-aaee-6edb6902d331 | -4.06997 | -59.84001 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 827761da-8e9d-3e74-9fce-80e36a3237ff | -3.82254 | -55.46373 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1c9eb776-072b-3cc7-931e-6f3a7a5d9631 | -2.77506 | -54.0726 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cd46c9d6-cd92-3292-b2a6-42b2eac9b669 | -3.11316 | -53.77268 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 700c318d-9f99-37f6-86f8-469160864b9d | -7.23033 | -55.12476 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2c39f94-44e9-382e-8359-1198a32ab7cd | -3.01447 | -54.12342 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| bcec2f9f-07f1-317d-b256-7aca5c1cabe5 | -2.94034 | -54.11782 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9735b253-34a4-3cb7-b1d6-f25829072597 | -4.30117 | -50.78386 | 2026-10-08 05:42:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 711b5c15-5ca5-3dcf-8138-5d1a6ea8fbf7 | -3.84836 | -51.9371 | 2026-10-08 05:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2bc3d2d5-7e0e-3452-9bcd-2ee7469a203c | -3.28704 | -54.04937 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f9ae6d7-2065-33c1-9b8c-f6b1b82acad9 | -2.75772 | -54.11647 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f6c652d0-bb25-36f9-a6ee-0439766a72c3 | -3.17354 | -58.64179 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 13834253-20a7-3c0c-895e-43aae1fbc0e8 | -4.13572 | -54.92477 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cca2f88-684e-341d-a49e-6a838cafc085 | -2.51038 | -56.17628 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d4100293-c515-36d2-b17e-d290cc01be6f | -3.25822 | -54.03788 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d5f02063-d838-3d43-9937-c997dfef747b | -3.18442 | -50.56871 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aea950f9-308a-3c1a-8698-f1c2cf68123a | -2.79186 | -57.65294 | 2026-10-08 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8018459-4fef-3300-8534-05fb59ff7a33 | -4.14049 | -54.03208 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af4abc5f-2d6d-338a-bcad-cef90d4f82e2 | -3.48536 | -59.46027 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bebb7c92-43f0-34f1-8de1-4ab0e32aa634 | -3.12335 | -53.70274 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58ab3873-6cde-375b-b878-8f003e760e1e | -3.52281 | -54.66087 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7940b6f5-90ec-3440-b16d-81038023012b | -3.5916 | -54.56799 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b10a99c-db2d-335d-a2ed-7bb181a239f2 | -2.1223 | -54.80853 | 2026-10-08 05:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2f52037-0a02-3145-9b10-f78c2487a313 | -3.02572 | -54.08482 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f7d8d130-b5f4-3d5f-b85e-2b51e37f991c | -2.9866 | -54.09226 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c4878aaf-4327-3551-af84-e640110624a4 | -4.44491 | -54.97528 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b97119ed-b4f5-3e0a-8ccd-55a22560a23f | -3.55007 | -59.49551 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 618ef773-e275-39f2-a2d3-aecacf21e739 | -6.73713 | -63.0439 | 2026-10-08 05:42:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e985fc53-ae4c-30a6-b0f4-a026f4b63354 | -5.29641 | -60.10957 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d4f67ac-052f-3d4c-b362-dbc022e03a23 | -5.29476 | -60.09599 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a35d4145-cb92-35dc-aa5c-1b082044c3d5 | -4.10747 | -54.41443 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afac200e-42aa-3632-a250-3a0f68534ee3 | -3.26991 | -54.03297 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 519c404d-e86b-36e8-9b70-955f77e5f175 | -3.30048 | -54.04766 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4533910-1e15-3744-9268-e4bb304f90dd | -4.44958 | -54.97905 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9890dec-88e6-3257-bb02-722322736143 | -3.52844 | -54.65845 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc0c8981-3145-391a-8722-c144b75e57de | -2.99337 | -54.08323 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 5fd43e83-1c6c-3284-a269-02d1b6cfcdfd | -4.80364 | -54.67852 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff672add-facf-36e6-8af3-7af87fee5d39 | -3.01263 | -54.24245 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4230e063-c8d7-3b70-9984-b87bdd59e0dd | -2.83062 | -54.1342 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e630a2d-b3a4-3b65-9365-72be08cd7882 | -3.50319 | -54.65145 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 551e03c5-2f40-37b5-b03d-e23379556106 | -7.21971 | -55.16322 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6db77c78-54ef-3a4e-89a4-6495cacc6eef | -3.47809 | -59.58157 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ed7643c9-9c47-36a4-823b-e95b6a8636bf | -3.29484 | -54.08421 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a5f813f-6325-3d12-8cf1-1abf77d42855 | -2.4863 | -56.12005 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad3e0d67-0fe4-3d51-9746-d1cbc599214e | -5.81726 | -53.832 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 963409bf-7266-378e-bde7-54f5af9b775d | -4.80304 | -54.68055 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4778565d-a998-3d09-93fd-8dc2077886af | -3.72335 | -54.22025 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README188.md)
