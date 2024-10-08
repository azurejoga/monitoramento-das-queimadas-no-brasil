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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d162beae-c2d6-3462-a357-d8fbb598d428 | -20.37614 | -48.83016 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a9948665-d2e4-3e68-9baf-97995eafad9c | -20.37556 | -48.83418 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fad5ee71-5650-3e0e-8aa5-249b14df9421 | -20.37555 | -48.80952 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 62404ae1-f0e2-39a7-b6f8-bc4dc7c0f439 | -20.37497 | -48.81356 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c357695d-07d2-3f36-ab0b-800d0d3ec161 | -20.3744 | -48.8176 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a649ac27-ea70-34f9-b0e0-d1a22325f7a5 | -20.37383 | -48.82161 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73ceee0f-808b-3c85-b60e-c9546903dfab | -20.37325 | -48.82561 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3874636b-9498-32bd-a26c-fced57282452 | -20.37268 | -48.82961 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 498f38c7-9c3a-3c4b-8837-997b27212a0e | -20.37211 | -48.83364 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 84.2 |
| bb4d1695-f14a-3fa0-a0c9-215a890f505d | -20.37094 | -48.81705 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 97487734-ae3e-3713-87fc-544267c94dbe | -20.37037 | -48.82106 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83f2b5ed-0c60-35e2-80e3-eff8c96787ca | -20.3698 | -48.82507 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f083edb-091e-3330-b3e7-753e4cd0aa20 | -20.36923 | -48.82907 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 84.2 |
| ddeda752-b7ce-3f2c-8210-7aab6259c37a | -20.36921 | -48.80439 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 47ad6e29-39c6-3fc1-af2d-7ff7d80bf187 | -20.36865 | -48.8331 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 135fb5de-e360-3473-9c9e-e9c0c488080f | -20.36808 | -48.83712 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 209.7 |
| 3dd40e86-5077-3c4d-9705-62a6fbd33f85 | -20.36689 | -48.79583 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 15.9 |
| b42c31ad-feb8-32f7-983f-96a70c63c2ac | -20.36634 | -48.82452 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03321796-90a5-342e-8ed8-8dca069cb8cf | -20.36632 | -48.79984 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 7bc246ca-acf8-3f75-bec1-6666354efe5f | -20.36577 | -48.82853 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b18fcff6-3ae3-38b7-8f26-f79932b6d4cf | -20.36575 | -48.80384 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 791f209a-3468-3084-990b-43fa7ceb9cb6 | -20.3652 | -48.83255 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 947a76da-791e-39ea-b674-ce40b38698fb | -20.36462 | -48.83657 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 93a727a8-ec3d-3f65-bd5c-d7e4da0600e0 | -20.36346 | -48.81994 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b224c9f-18f5-3343-accc-46e0479b27b6 | -20.36289 | -48.82396 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e99cec6-5ad7-34c3-aad9-06652af8e40d | -20.36286 | -48.79929 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c105bddf-7a3a-3b72-a130-fd4095342e3d | -20.36232 | -48.82798 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 27cc9961-47b6-3d21-a813-3b9f1e778c24 | -20.36229 | -48.8033 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f4a22983-da12-3b62-984f-9d4ef282c70f | -20.36174 | -48.83201 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e477c659-f2f5-3a8c-91f0-1b84d0f607c4 | -20.36117 | -48.83602 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 28.2 |
| b6fcfdbb-a747-3c18-8ada-d55e68dba85d | -20.36 | -48.8194 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 201539fc-f572-3bc6-a131-80152fce5510 | -20.35829 | -48.83146 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1c3f3c74-0233-37e9-a3df-1032a265d5fa | -20.35826 | -48.80679 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6b9c95c4-0fb9-3bb7-8162-7faef8d7bcf6 | -20.35772 | -48.83548 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 059a4e39-c372-3105-9b31-f5a642af31cd | -20.35712 | -48.81485 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5c0ee93c-625a-3d5d-8de1-ba30ff650f63 | -20.35655 | -48.81886 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 22b932ed-8bfb-39f5-a290-e07255e7d83f | -20.3842 | -48.84788 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 14.8 |
| a09faaea-4396-39ac-b2b9-537bebd2a0b9 | -20.38362 | -48.85191 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 01d47ef6-df9a-3e61-bd2c-e8b40942506c | -20.3819 | -48.83929 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 57f73d0a-b380-3821-9ae2-b51f27a1f761 | -20.38132 | -48.84333 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 21.5 |
| e3af421f-99e4-3502-ac4a-afe802152e04 | -20.38074 | -48.84735 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 66fca6f3-d007-3b92-b7bc-5d46dc00dec3 | -20.38017 | -48.85138 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 47067fa0-5025-3c31-9e6a-ba01e01e1c44 | -20.37959 | -48.85538 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 72b33e2e-3fac-32b7-8da4-2cb0a75dea36 | -20.37902 | -48.85936 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5087de6d-9604-36ec-808f-2b34ed486bec | -20.37844 | -48.83875 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 32.2 |
| e880a787-bce1-3ba6-82d8-61be45fc3a47 | -20.37786 | -48.84278 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 32.2 |
| ca3a7871-c0e0-34d7-b98e-0e9859c52321 | -20.37729 | -48.84681 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 31.7 |
| cd870112-4b72-3f35-89f2-2764c7748cfb | -20.37671 | -48.85082 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 31.7 |
| af59b109-526c-39cd-ac7d-f262c7a31cb7 | -20.37614 | -48.85482 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 17.6 |
| bd60860f-fe39-31d2-8061-ebd6e4158424 | -20.37557 | -48.85879 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 4a3a05ff-51fe-3b09-9ea0-33bd7fe6c2d7 | -20.37499 | -48.83821 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 383ef9dc-ee61-313d-9d9c-7509e73b0be7 | -20.37441 | -48.84224 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 78e3f689-dae4-3cbb-9fd3-20a0b348a909 | -20.37383 | -48.84627 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 343dd9e6-dfd2-3d3f-82aa-24d2f159df91 | -20.37326 | -48.85026 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 0fac8ddf-5e72-3f31-8bb7-a4be43d13209 | -20.37269 | -48.85424 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 5c0380ba-a991-324c-8fb8-1bbf6dab2588 | -20.37212 | -48.85822 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 17.6 |
| d3b8445e-29f5-34c3-9c90-e8831ac9ad6e | -20.37155 | -48.8622 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 37.7 |
| f4f986e5-c95c-3fb6-af1f-e8cfc68f2222 | -20.37096 | -48.8417 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 209.7 |
| 27da223e-68c7-309f-ba1e-6bf006bdab41 | -20.37038 | -48.84572 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 60.2 |
| b76713e3-dd8f-3f27-a3a0-e60164de2904 | -20.36981 | -48.8497 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 60.2 |
| d9f29165-9af9-3f00-9a0c-cae0f576683c | -20.36924 | -48.85368 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 187a8ff8-d4f1-3cf4-aa13-b5c3d0c9a765 | -20.36867 | -48.85766 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 60192fca-07dc-3e4e-a821-4bf1f7939983 | -20.3681 | -48.86164 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 587b6bae-1527-3d6f-aeec-3429c8a5d969 | -20.36693 | -48.84515 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 60.2 |
| e64ca921-ec97-3ee2-862c-984c681e0527 | -20.36636 | -48.84914 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 0f5db196-ebb7-3f3a-aa2a-052ab76af49b | -20.36579 | -48.85312 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 9e5c55d5-998c-3da2-b5d4-ca9596eeb58c | -20.36522 | -48.8571 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 241e9bbd-f840-3ae8-9fcc-86a5e81c9afd | -20.36465 | -48.86109 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4ac5ee29-e537-3939-8f85-d49f408b031c | -20.36405 | -48.84058 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 9f965484-af45-3a2a-99a8-a4bc2d033774 | -20.36348 | -48.84458 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 7a061aac-6dc9-3d22-8d0e-f74b3143f3ce | -20.36291 | -48.84858 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 20.5 |
| dfae0d5b-2fc9-327d-879b-bbd361cb5acb | -20.36234 | -48.85256 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 2c3c92cb-7e7d-3fe2-8b54-2cf356168235 | -20.36177 | -48.85655 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 8696a8fd-44a8-3b21-a596-8f61e771c5be | -20.3612 | -48.86053 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 253.7 |
| 964e5f1a-c540-353a-96c9-550071cab640 | -20.36063 | -48.86452 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 253.7 |
| 48e29dd3-d255-3e61-95fb-032d6e90faa0 | -20.3606 | -48.84003 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 7d16b9a3-63cd-3cb9-ac0a-649a95e36bf7 | -20.36003 | -48.84404 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 20.5 |
| d3d7f45b-1946-378c-b381-e1cecaa270cb | -20.35946 | -48.84804 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 8c6177f6-781e-3d32-bdc6-fffa1f42f4d8 | -20.35889 | -48.85203 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 766aab41-5744-323c-b0d7-50713afe78b1 | -20.35714 | -48.83949 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| dd1521ca-bedb-390c-9f59-4ab70327f460 | -20.35661 | -48.86797 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 74c19e84-eae1-361b-80e1-712956b01817 | -20.35658 | -48.8435 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2de9fbd7-37e3-3902-b6cd-476fddba71be | -20.356 | -48.8475 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 89e8ab26-1932-38f1-8adb-39f5f04ae6ef | -20.35543 | -48.8515 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 6315b0cd-5d75-3b3c-91fe-b68cf9e4088f | -20.35487 | -48.85549 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 23.8 |
| e432cd6f-1765-3cda-9fbb-4d2946fe2463 | -20.3543 | -48.85945 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 5126445b-047f-3fbd-aef5-62c815e74a67 | -20.35316 | -48.86741 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d371aec8-ad84-36cc-bbdb-670171e17068 | -20.35312 | -48.84296 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 73b136da-7339-36e5-b887-4101e941be90 | -20.35255 | -48.84695 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2b3ba4f4-1c00-3793-bd1e-43d61144ecd3 | -20.35198 | -48.85095 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 8cfd85fa-a6d5-3bc8-969b-516ca7d3e694 | -20.35142 | -48.85493 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 23.8 |
| f964b3ac-b578-333e-8f35-e92d3a5866a3 | -20.35085 | -48.8589 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 92a1749e-ada6-3a88-86dd-dbf2ea65b261 | -20.34972 | -48.86685 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 681e8ade-262f-3cfe-afbc-68e8266773b2 | -20.34853 | -48.85039 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1326bbae-7dec-3e12-b50f-9cf86ec157e4 | -20.34797 | -48.85437 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36b432df-fb39-3be3-ab7d-7d7a66c4e14d | -20.3474 | -48.85834 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ca53f46-bc10-343b-9f13-a02519f4085b | -20.34395 | -48.85778 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 239b0e2c-07b9-34a4-b4b4-d73b938c5eee | -20.34339 | -48.86174 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00461a5f-ef0d-3290-83d8-ed14b814cdf4 | -20.02174 | -48.91058 | 2024-10-08 04:38:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| abd01776-f02a-36a0-ab79-28eadf1d9b55 | -20.41356 | -48.81572 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 12.0 |


[Clique aqui para ver as próximas entradas](README75.md)
