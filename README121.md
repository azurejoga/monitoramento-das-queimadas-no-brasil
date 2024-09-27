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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b3fb53b-ceef-36cc-bf9c-51bfcea40144 | -10.69179 | -60.73389 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9357d4a6-f06f-3c13-8e14-532aa80f6710 | -10.69121 | -60.73773 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09644ac9-7eb2-3e08-a010-5de17a0b8a8d | -10.69063 | -60.74157 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 033964af-c1b8-3d23-ad2f-c7938e990765 | -10.68833 | -60.73335 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e37ce05-cfd4-3000-9028-7300cbdb1d4f | -10.68775 | -60.73719 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8a57968-0b51-3f2d-9e31-117643d22063 | -10.68717 | -60.74104 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8d7898e-70a4-31c5-848c-cc03e8fbe33b | -10.68429 | -60.73665 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a73652d0-8a18-3115-b124-80117a93010f | -10.68371 | -60.74051 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75047f72-10d6-38ad-aa3b-b33241da6978 | -10.68026 | -60.73996 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f4c60d0-1cb3-317c-8f3c-e8303dc7c479 | -10.6664 | -60.76143 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79e4dc5f-8441-323d-936d-517986555428 | -10.2188 | -60.49915 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26561788-0a6e-3c6b-82ad-cea4cc5ce881 | -10.03851 | -60.44507 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23e329ea-978b-32c2-917a-88003639bc53 | -10.03561 | -60.44064 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e7a7d55-49e9-3757-8932-594e973af7f3 | -10.03503 | -60.44453 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6023e15d-bcb1-3cd1-ae3c-979dc2234383 | -9.60867 | -61.02277 | 2024-09-27 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb246f88-cc41-3078-971a-b9eae5390cda | -9.60811 | -61.02645 | 2024-09-27 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17b88d41-cbe2-320e-8c5f-cc63a78cc232 | -10.22913 | -61.27034 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed174165-8edc-32c8-bfbb-dbc466ee724e | -10.22857 | -61.274 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b7998a2-e9f0-34bc-83ae-3c7c371db9ae | -9.57721 | -59.78226 | 2024-09-27 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d3f1e2da-c6d0-3021-a3b7-510dcac02955 | -11.62879 | -60.29434 | 2024-09-27 05:27:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2da63426-95e0-35a5-b3dd-2a541d19ed2e | -11.32691 | -60.57551 | 2024-09-27 05:27:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20179570-bdbf-30a6-a322-979e107a855b | -11.28492 | -60.59327 | 2024-09-27 05:27:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7557374-3bf1-39bd-9466-b8d57ea7e159 | -11.28434 | -60.59726 | 2024-09-27 05:27:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acebf82d-1ff9-3529-9021-b9812258f116 | -11.28377 | -60.60116 | 2024-09-27 05:27:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59d10abd-3ceb-34e3-84e8-4b57298e7b92 | -11.25118 | -60.62091 | 2024-09-27 05:27:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 686ca882-6fdd-31c0-a00f-7a3a572869a5 | -11.13357 | -60.46642 | 2024-09-27 05:27:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1c29344-50a3-3291-aa69-af6eaba87ae2 | -11.09377 | -60.70937 | 2024-09-27 05:27:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 066b8dc7-ead9-3753-bd35-ceebad0d4934 | -11.0793 | -60.75866 | 2024-09-27 05:27:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13b4ad84-5b66-312a-91b5-4620b69717fe | -10.97843 | -60.5409 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e04b573-7248-3034-85e8-3f33b46ab538 | -12.01353 | -61.2253 | 2024-09-27 05:27:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6289e912-2670-3b6a-a155-379e5e3b5635 | -12.01067 | -61.22095 | 2024-09-27 05:27:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1993d108-6c59-3d52-8540-f68fa1dd0793 | -12.01009 | -61.22476 | 2024-09-27 05:27:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a1d4109-23f2-3627-a148-18c4f9732b60 | -11.18365 | -61.20578 | 2024-09-27 05:27:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8a76cfa-3200-3d19-bd6e-36472439fbef | -11.18023 | -61.20523 | 2024-09-27 05:27:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61cfadcf-25e0-37d1-9425-d84e3a1a83bd | -11.17626 | -61.20845 | 2024-09-27 05:27:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5700f7ee-b05d-37a1-b670-85f649d6c14e | -11.1734 | -61.20416 | 2024-09-27 05:27:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76eef10a-005f-3d6e-87e3-400ee7035ff3 | -11.1733 | -61.2047 | 2024-09-27 05:27:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc768fd0-0ef3-38f0-a58e-8cce3ebbfe1b | -11.16078 | -61.19511 | 2024-09-27 05:27:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa0c8653-ac9c-396e-a9a2-69290f482dbb | -11.16021 | -61.19885 | 2024-09-27 05:27:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6d24bdcd-2193-30a4-9a96-9ce1a92676f3 | -10.96981 | -60.97753 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 353dcc66-e5cf-3d95-a3a4-ae7de25206aa | -10.95777 | -60.98736 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05e7d8a4-1c60-3152-9f96-2a570fa7076d | -10.94459 | -60.9582 | 2024-09-27 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06878a77-f26b-3fcd-8182-4aa4d13e65a5 | -7.79826 | -62.39238 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d00fab4c-8c1a-336b-adb9-599a0266c7e9 | -7.32157 | -61.18201 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d2c85c57-576b-3151-aedc-12ecd959b10a | -7.31933 | -61.17443 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 807eca01-3a66-3e5a-a11d-ff97e52893a6 | -7.31878 | -61.17796 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8a4fbb1e-ca26-3c1c-b3b8-3202ed514287 | -7.31823 | -61.1815 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a6bb2154-4466-3ccb-a47d-2c6782e6e21a | -7.31769 | -61.18502 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f0d55238-0e53-3d5b-9bfe-30b1fd68ab09 | -7.30017 | -61.09898 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5e083c2-abb3-3194-b2a3-4d2db745f5ae | -7.29682 | -61.09846 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50b5714a-ef4f-3593-94e8-c47ea00bf363 | -7.29628 | -61.10201 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e10b65ae-3b1b-3e58-9a7f-315149130732 | -7.29293 | -61.10148 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30f44d78-8005-3247-ad0a-20a0abc0024e | -7.28625 | -61.10043 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bb45942-c419-3951-bdc1-e1a825b72a2a | -7.2829 | -61.09992 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10c27bf5-9f99-3c2f-a9ad-181319582d36 | -7.28236 | -61.10347 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2969638c-c2ad-3f87-b13e-4799dc005907 | -7.28181 | -61.10701 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92f84c1b-d7ea-3dc1-bcd8-cdc4b628e5c8 | -7.28057 | -61.09967 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d820e5cb-2ab7-359b-97d3-3713cef9557a | -7.28001 | -61.10321 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65b06314-47bc-3800-adcf-1b3da700d75f | -7.27946 | -61.10677 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6bbbb612-c03b-36e8-bccc-4de370132778 | -7.27667 | -61.1027 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d93d1e7-0343-305c-87ae-702b21cd1e61 | -7.27612 | -61.10625 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 818f2b69-4514-3d48-9378-8145fda01017 | -7.26664 | -61.10115 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32208740-c2df-37bd-ad90-2aecf652ac68 | -7.26329 | -61.10063 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2199c319-8ee6-3dfd-b975-0eb6fa50c885 | -7.26274 | -61.10417 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c6dfb37-843b-3c45-b9ea-63991c6cdb7e | -7.25995 | -61.10012 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e4230aa-3891-324c-8f60-6dbd281825cb | -7.25661 | -61.09959 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b3d4c11-a7b7-308d-b694-0625e573352e | -7.25327 | -61.09908 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af26b359-6aa0-3402-ac72-7193b1ac6ad2 | -7.24827 | -61.10918 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db1685fd-aecc-3bf2-a5f5-44277488d938 | -7.24603 | -61.10157 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec07ce6f-5527-30c8-9552-e59580277f1e | -7.24548 | -61.10512 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb538b5c-38ac-3a51-80a9-06243c3c2b8a | -7.24493 | -61.10867 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91384f0f-7904-3b4f-804c-6833acacc5ed | -7.24438 | -61.11222 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 334ac5c5-fe78-39d2-8cc9-1c128f165ebe | -7.24268 | -61.10106 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 050ba8e9-1bcb-3416-8cba-b43bff97b8eb | -7.24214 | -61.10461 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e21b0b81-8d12-3a5b-ab30-c91ec575b6e0 | -7.23879 | -61.1041 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74aa1587-fd82-3ced-95c0-860bd5bba245 | -7.236 | -61.10004 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 669aa4d6-5ea8-38c8-b973-165e962b08ce | -7.23265 | -61.09953 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc300a88-764d-3a64-b7bc-b268e4394d41 | -7.22931 | -61.09901 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c173dea-6afe-34cf-94f8-550da707db97 | -7.94307 | -61.31071 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 947e671a-4f14-3db3-bd9c-37f43b63c5e5 | -7.93141 | -61.31977 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c9ce94b-4071-349e-977d-20bef4e52926 | -7.928 | -61.29752 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a20a6238-f858-34ff-859a-91eaab318744 | -7.92753 | -61.32279 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 720155c3-5fe5-38f3-8ef4-b728745d4e8b | -7.92466 | -61.297 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38512542-2711-37b5-b0fc-2c3170ce39a7 | -7.92404 | -61.27876 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8e3d9173-c98d-34c1-885b-eabb2e23b52f | -7.9235 | -61.2823 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e0e8f958-7b6a-33a4-b936-1841da0d0b9d | -7.92125 | -61.27468 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d63e324c-c928-3983-b89f-25e1cdcf786d | -7.9207 | -61.27824 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cdbe4930-3cd0-377f-8e24-dffbd010f620 | -7.92016 | -61.28178 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f3f7b882-d08e-307e-bebc-8e0d9b5749d1 | -7.91961 | -61.28532 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b82f24ea-e733-36e3-97a6-321c45fbbe33 | -7.9179 | -61.27417 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2c4a88dd-654b-3f38-9618-e4d7328fc3ca | -7.91736 | -61.27772 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d49a67f1-f230-355d-9623-c8739e86bd4b | -7.91681 | -61.28126 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 74862f99-fa65-3e5f-ad42-c3473eff4b09 | -7.87677 | -61.12598 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43886900-c918-3bca-81a7-b06e293957c3 | -7.8528 | -61.34749 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b32f20eb-551e-3321-8af5-d472896ee537 | -7.84084 | -61.24784 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 479655f6-eb9c-3978-893a-d0033d370393 | -7.8226 | -61.12122 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a6762ed-30e0-3b81-9dcc-0e2e7fa0a068 | -7.78714 | -61.26833 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8375ef8b-3709-3a88-9008-62481e18a5e1 | -7.78588 | -61.18823 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20961ee1-7a95-36c4-9147-d230ed3faaf2 | -7.78533 | -61.19179 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b303215e-e053-339d-88b4-a6e770ff77e1 | -7.78478 | -61.19535 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README122.md)
