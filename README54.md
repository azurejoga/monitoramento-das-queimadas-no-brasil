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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e686b7e-f5b6-3f9b-897a-a101c6aa54d2 | -2.93562 | -54.35868 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d79859a-64ee-3476-a670-b6ac47281326 | -2.93499 | -54.36248 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab28c923-bd5c-3124-a9e5-ba51f251aa03 | -2.93139 | -54.35802 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15b9d571-84cc-31af-9476-8c75da4a4d33 | -2.93077 | -54.36181 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6bad420-8f21-3eba-be56-2e0f2495edf0 | -2.93046 | -54.36139 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6f26757b-ae65-32b7-8a84-6b9925437d6d | -2.90333 | -54.15502 | 2024-10-29 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1aca64e2-37fe-3711-8ee3-ba6a85d13f65 | -2.89179 | -53.99172 | 2024-10-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a9f38faf-d864-34d8-9a44-55ea5ca162a3 | -2.87137 | -53.96968 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14b19feb-11dc-3b88-8724-9de18d32c1f2 | -2.86546 | -54.25574 | 2024-10-29 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c55993c8-4e66-3471-a2bd-7bf56cf1e87f | -2.85998 | -54.47572 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63645235-c115-3ed2-94f9-f9df0f5152a9 | -2.83586 | -54.05957 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e86cff1c-20b8-3fec-a8a9-826085e46d8b | -2.83485 | -53.98674 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6004d9c-6763-3074-9250-7a9d86049a2c | -2.83359 | -54.20758 | 2024-10-29 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2eccb9d4-a652-3805-a2c2-6b45ae8bf052 | -2.833 | -54.21132 | 2024-10-29 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a69d253b-584f-3679-b538-c259dfbf6832 | -2.8324 | -54.2151 | 2024-10-29 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5d097372-2a3f-3f3c-af7c-8e8806dc10bb | -2.82821 | -54.21447 | 2024-10-29 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5615d6e1-b894-3184-a796-e9c43ec7115e | -2.81384 | -54.09074 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52339dba-b6be-3aff-a916-daeca4021392 | -2.81139 | -54.10586 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46aefcb4-3e33-38d4-b16b-31abf2643177 | -2.77806 | -54.7341 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a60006a2-5e61-3c5b-a1a6-e38e297dab26 | -2.77739 | -54.73821 | 2024-10-29 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f429687c-56f1-3cda-9016-df04d5ffd547 | -2.7648 | -54.03734 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dcd89414-74a2-386e-8052-421a0f1cdee8 | -2.76314 | -54.03659 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ceaeed3-450d-3abd-b92a-bba9c2944267 | -2.76253 | -54.04031 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e60f798-07e4-35d9-ad81-db0a42b8c0db | -2.76066 | -54.03669 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4aab9fc-c121-342b-ae4a-41177307cb97 | -2.759 | -54.03595 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a29c2184-6a3f-309f-ac4d-0eea6605a09a | -2.75237 | -54.0354 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 647fee9c-a2bb-3b74-a6a1-3f3d9f31d8d1 | -2.74823 | -54.03474 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22b081d4-7a09-3819-a1cb-8cf2f804323d | -2.7386 | -54.12222 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 986ee50a-23f6-3574-afbc-1394a4f6a1a2 | -2.68176 | -54.96318 | 2024-10-29 04:38:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff05ac3a-538d-3ca2-b8e5-da8c68b041ab | -2.64151 | -54.24497 | 2024-10-29 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f664ce16-1253-39f9-8d25-1c2678e6dc92 | -2.63952 | -54.33642 | 2024-10-29 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6803a534-5fe0-34bf-82bb-127104a7a17c | -2.56614 | -54.01694 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5f2eaaab-16f4-3504-b757-a4c41e9554be | -2.56323 | -54.00875 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9be93198-6127-3d51-91e6-87b32467336e | -2.56261 | -54.01252 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c08bb210-343a-31ed-ac74-34cc859cc4b2 | -2.55909 | -54.00809 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07c6fedd-39bb-35b9-b050-baa9617502c9 | -2.55846 | -54.01186 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d88d01f-b41e-3023-b9d0-8a8580aa3708 | -2.55722 | -54.0194 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 33de2242-fa99-3f1d-9bd2-4516c65cef16 | -2.49812 | -54.13582 | 2024-10-29 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 476b9472-7ab8-31e5-99d9-7c1d69c0ab12 | 1.59878 | -55.63633 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 697c087f-7d14-3467-a905-c8ca00feeebd | 1.5664 | -55.63268 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae56a101-4281-3c63-adcf-f97fb1b2c55c | -2.14076 | -55.75209 | 2024-10-29 04:38:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b972607-74b3-376e-9b31-49bacb4c8139 | -2.12429 | -55.89157 | 2024-10-29 04:38:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7983b0a-4ea6-313a-82ee-2b9ba658248c | -2.12344 | -55.89665 | 2024-10-29 04:38:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ec90aff-a861-3e2e-8faa-01bef9163f0a | -2.12295 | -55.89417 | 2024-10-29 04:38:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 933cd5f9-913e-3ef2-954f-13bc8599a495 | -2.00053 | -55.71111 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 33c10805-3476-3ee3-b33f-1b0291bf2fcf | -1.99972 | -55.71613 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 96e98c16-99af-3cef-92dc-b61605b7caa5 | -1.85729 | -56.36519 | 2024-10-29 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a4dba74-c31b-30a4-afc1-d88d692d5b7e | -1.77144 | -55.5537 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de7dd457-8515-37aa-9296-509b474c703c | -1.76931 | -55.54951 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3c45c60-1ac0-391f-8f03-362a01975954 | -1.76853 | -55.55448 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d6048d8-99ad-3efa-b0d3-baf237414f7f | -1.76678 | -55.55296 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c830b6e-dafa-3099-8b51-62f4073b8829 | -1.7617 | -55.64226 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a35134fa-eb89-302c-bb4a-0e296f4ec4a7 | -1.75933 | -55.22493 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2866114a-fd8d-3c4f-a20e-c57e09f3d812 | -1.75859 | -55.22956 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 104ab79b-5988-3889-a305-3aabd462a1b7 | -1.75588 | -56.19613 | 2024-10-29 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a99360ee-b990-3c90-a036-993e4ef7b6b5 | -1.74496 | -55.25592 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e01d9a29-10f9-3f6e-95c1-fb889817f7f2 | -1.74134 | -54.99321 | 2024-10-29 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3e7771bb-dcee-3570-9001-6fb270061f98 | -1.73864 | -54.99458 | 2024-10-29 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2f70ffab-0a3b-36f9-9ab1-859f34b504e1 | -1.69277 | -55.08007 | 2024-10-29 04:38:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3f15a64-ed0d-3e6a-84d1-a22a3b53e8db | -1.67991 | -55.30859 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cebd9d0-ff85-3a52-9354-5ebf9f5f3139 | -1.64705 | -55.68192 | 2024-10-29 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3ab7305d-dee5-3c21-989a-4831a30ada04 | -1.59908 | -55.8846 | 2024-10-29 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07607c3e-3564-3630-a4af-aa50723a629a | -1.59839 | -55.88774 | 2024-10-29 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7760cb90-20e5-3ef5-9574-7a209274f7af | -1.59822 | -55.8898 | 2024-10-29 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52130ba4-e3a3-3dd1-9682-35b7c31601b7 | -1.54038 | -55.47838 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c171469c-8011-36d8-b24b-fb76530fe96e | -1.3007 | -55.72499 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d9d9c55-01a7-3bfa-ad12-da3804741ca2 | -1.30041 | -55.72271 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95630a5a-2a42-3d20-b1d2-8c288b97973b | -1.29594 | -55.72424 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3a0b0fb1-88a0-3103-8344-c46ac2c9ba34 | -1.29565 | -55.72194 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 832dbe68-3db7-3787-b1f5-2f4621a14f1b | -1.2951 | -55.72936 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bc2fcf7a-1541-3a55-88d0-70f4e6806e66 | -1.29485 | -55.72709 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8e1757cd-d130-33c6-b78e-7927faa03939 | -1.29427 | -55.73441 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4c4b096e-0153-3817-b5bb-1268625c1035 | -1.29405 | -55.73219 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 90b3023b-c7c7-3b18-a960-bc0b6ff96498 | -1.29204 | -55.71831 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1e326716-b3f5-36d0-93c2-afa3609e468a | -1.29173 | -55.74982 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 071091b4-cdab-3635-9ec4-9e53e02e2791 | -1.29171 | -55.71598 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a9468b94-f833-3d9c-988f-a0957daac29f | -1.29119 | -55.72345 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b70cdd39-e6e1-3407-9e5c-510c8052ea32 | -1.29082 | -55.75277 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bdf930ab-9f29-3820-bb94-70fddfdb9ac0 | -1.29034 | -55.72858 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2009aea3-aff5-3ad5-bbcc-1d527ca270ac | -1.29009 | -55.72629 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b07d11b9-38c6-3e31-8ad8-afb4cff607df | -1.282 | -55.77781 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89919f2c-c69f-3cbc-b329-d376e1191eb2 | -1.28187 | -55.77996 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34270965-1162-35be-9e54-b1d6f3927289 | -1.28119 | -55.78302 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c3802e5-4e3c-39f4-ae9a-8b3e4b2f9529 | -1.26149 | -55.90841 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17823b73-e019-3660-8ccc-c7ecfa175dc6 | -1.25947 | -55.91562 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b5ebc387-1de8-367c-b93b-674c69fe6bfa | -1.25498 | -55.91839 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b42548a6-a142-31bd-b181-a038cb5f2aed | -1.21436 | -55.86314 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 53942f39-3d31-34d7-9c89-827e41540831 | -1.20957 | -55.86228 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 723f7422-10a4-37a8-b196-b9ccd8967031 | -1.20847 | -55.89979 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c692a578-3ae9-30dd-aed4-950cecf51fb6 | -1.2079 | -55.87264 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c7d82dd-fd87-31a6-877c-78ca45e8b0aa | -1.20765 | -55.90487 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| f7638adf-8272-3e62-8568-c9319795d523 | -1.20312 | -55.87165 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2cbc0b90-2d75-3ba9-be8b-4facb98159bf | -1.4004 | -55.37866 | 2024-10-29 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| efda4919-3690-359e-9010-c59181513c12 | -1.39962 | -55.38349 | 2024-10-29 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 310cb65a-9d98-3fb3-b462-f6b937fb0c2c | -1.39929 | -55.99498 | 2024-10-29 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e703cb6-7828-31f5-94e3-7b6cc52e4fa1 | -1.37752 | -55.85625 | 2024-10-29 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 481b12d4-bed4-39be-8cc2-d0245ef2623f | -1.37723 | -55.85849 | 2024-10-29 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d9929b26-0171-3baf-89a8-40e466a8987e | -1.37665 | -55.86147 | 2024-10-29 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 85972161-a349-3dfa-9db9-fe0895225f4b | -1.37641 | -55.86372 | 2024-10-29 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e5943f5-4c54-3300-9d0d-3a5cc2224bad | -1.37184 | -55.86079 | 2024-10-29 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README55.md)
