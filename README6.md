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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9aaac0d-f3d2-32e7-8a29-70acecc57bf9 | -3.9516 | -48.0681 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07994068-1ff6-3f7a-b528-f8e69110dfea | -3.9664 | -48.042801 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61c086d8-4b0e-336e-b940-0a1e93d23099 | -1.7712 | -52.737202 | 2024-11-26 00:41:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 584bdc1a-fb73-3774-b44e-1a8d74b7a714 | -1.781 | -52.7351 | 2024-11-26 00:41:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3330a116-93bd-39fd-bd0a-f07cb2028857 | -2.7887 | -52.9128 | 2024-11-26 00:41:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 511e236c-e716-358e-9c51-4127be8487ae | -3.5969 | -50.3927 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0eaeb7bf-364b-3e7d-927f-dece51b133c9 | -1.0383 | -51.738701 | 2024-11-26 00:41:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| aba24dc9-7df5-3eaa-a762-508ae0c545ab | -3.5921 | -50.371601 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac167306-f61c-3393-8b74-1dcf04aed4dd | -3.2724 | -48.748798 | 2024-11-26 00:41:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95795943-0c8a-318c-9800-a275af23cb7e | -3.2215 | -50.781399 | 2024-11-26 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b14c5f3b-a8ca-3369-92bd-cae8dfef1bb9 | -3.9232 | -50.513401 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62cd3905-4ac8-340c-9de3-a20e8fbd0afb | -2.1866 | -45.970299 | 2024-11-26 00:41:00 | METOP-C | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 30dde2cd-48ab-37fd-a8b8-6e0232c36705 | -3.0645 | -50.952 | 2024-11-26 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2fb68aa-2799-3289-8ab6-f6a2613c3609 | -3.5145 | -50.212502 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15ccb72f-80f5-3fd7-ac5c-2bc6ac183241 | -2.8005 | -52.9193 | 2024-11-26 00:41:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92899951-f021-3d9f-b41f-2a496c3a7ed0 | -2.7929 | -53.0219 | 2024-11-26 00:41:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db2f6b69-fcbb-342c-a2fd-8a5a08549d88 | -3.4872 | -50.453999 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea835f41-f729-32dc-83b0-19d6489ad0d2 | -3.1885 | -48.428799 | 2024-11-26 00:41:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d526980-205d-35bb-8c0b-164d418a4012 | 2.7013 | -60.424702 | 2024-11-26 00:41:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d5d88ca2-a317-353f-9dc4-535e686cacf9 | -2.8027 | -53.019798 | 2024-11-26 00:41:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf27690f-5b27-3e96-868e-93e0f2d41a7f | -3.9646 | -48.0797 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a3870f5-75d8-323c-a1c1-d57e6170d0d2 | -3.9648 | -48.035801 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9eb8fb70-74d8-3e3c-b4b8-de71ffe0a86f | -1.5938 | -47.462898 | 2024-11-26 00:41:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f05a2290-82ed-3949-a6b6-7387bbf4e938 | -3.3749 | -50.097599 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d46057b0-136b-3101-b63f-3779c218ef55 | -3.8575 | -49.140701 | 2024-11-26 00:41:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1fe83a8-d9c1-38d2-bca9-55634e003db2 | -3.242 | -45.676102 | 2024-11-26 00:41:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 15c9a81d-b38f-39ef-a01c-edefc338ba40 | -3.4376 | -50.011002 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa9bf5ef-5018-348c-80b8-06b435505254 | -3.9484 | -48.054199 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61655e75-ab2e-3bb0-8df5-99a3279fc1ef | -2.9172 | -45.168499 | 2024-11-26 00:41:00 | METOP-C | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4a281b4f-407a-34a2-8b01-ec1feeb2d0c5 | -2.9275 | -48.0121 | 2024-11-26 00:41:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 252578a7-9c73-3e57-9641-5bd2937084b8 | -3.7222 | -49.947701 | 2024-11-26 00:41:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 802247a4-fac4-3a7d-b9dd-42387d164c86 | -2.8428 | -49.1245 | 2024-11-26 00:41:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 090d4b7d-1e86-3277-905b-b5a49c53ca8e | -2.6654 | -53.003899 | 2024-11-26 00:41:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51743cef-344c-3c70-9494-d82a2f58ffe5 | -4.6409 | -50.679001 | 2024-11-26 00:41:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bfb9076-68fc-33e0-930a-e35824e76d03 | -3.2904 | -50.2696 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b032318-9421-34f2-8036-8f0801745322 | -3.2725 | -50.642799 | 2024-11-26 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9f30e78-f558-3f1a-a377-93ace5d0d38e | 1.9472 | -55.721901 | 2024-11-26 00:41:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd5a2e0c-0a34-3a88-897f-f221570de57b | -3.9566 | -48.044998 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc7ed8f6-cee6-34be-b889-9a8793495a2c | -3.4621 | -50.253502 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2312aed-1e6f-316d-be9a-5952fb62daf1 | -4.6392 | -50.6717 | 2024-11-26 00:41:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ff13003-7620-3bb5-8053-8bd778c1ff36 | -3.2727 | -50.011501 | 2024-11-26 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4503e7b-f9a8-3db1-83fe-b9458391f02e | -2.8046 | -53.028599 | 2024-11-26 00:41:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efef1d4c-a45f-3670-82da-b9dd68cc0107 | -3.95 | -48.0611 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17985f16-70f4-3a71-9805-826a5cff243c | -3.6533 | -50.232899 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0a5ed24-a56f-384a-85e2-d44ac41a87bb | -2.7868 | -52.904099 | 2024-11-26 00:41:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b48ae8da-82d8-35d8-8c71-8922cebc9c91 | -3.7238 | -50.180599 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cb4925e-a659-3cb1-ba48-91beb55081d3 | -3.4986 | -50.4589 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5040d95f-d3af-3562-a439-59849b3bcee8 | -3.1771 | -48.424099 | 2024-11-26 00:41:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de58a631-7e3b-30a8-bf3c-6b5d9836b233 | -3.823 | -47.466801 | 2024-11-26 00:41:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82b70496-616f-30e9-8109-3ef13c7cb4a4 | -3.9762 | -48.0406 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f91685a-98b8-3f78-81c0-cc7c82710134 | -3.4505 | -50.836102 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19c98775-6cef-38b2-be01-d9818ba44a83 | -2.5332 | -45.5989 | 2024-11-26 00:41:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 392c82d9-6f4c-3423-9126-6ad21934c4da | -2.7948 | -53.030701 | 2024-11-26 00:41:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63df2a3e-437d-303a-8ccf-93535ef8748e | -1.631 | -53.296501 | 2024-11-26 00:41:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70183692-821f-381c-8f75-4ae9a414861b | -3.9778 | -48.047501 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2513dcf2-dd22-37ea-9cb1-e60a8cd7019a | -1.4817 | -53.815899 | 2024-11-26 00:41:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 839f0a0a-1265-313c-9047-2165fb380259 | -2.9783 | -49.580399 | 2024-11-26 00:41:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2be799b9-01bf-3a5d-bbb1-9461f655bbe9 | -2.8444 | -49.131302 | 2024-11-26 00:41:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3aaeb277-85f9-303f-a905-7db375dc073e | -3.2241 | -51.608898 | 2024-11-26 00:41:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3358c4ef-7c0e-396c-987b-116ad0dde2b9 | -3.4637 | -50.260399 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 783b4052-9288-34b2-a255-fb22184ddf47 | 1.9375 | -55.7197 | 2024-11-26 00:41:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18bd614a-6f88-3bac-9e13-a1523cc6e34b | -3.6811 | -50.219398 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f41ea68b-a59a-3f15-b1ca-f3d266b34204 | -1.7791 | -52.726799 | 2024-11-26 00:41:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aadf810d-9a20-39a0-9803-ec0cd3a2ad6d | -3.6827 | -50.226398 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7968c795-d554-3ecf-ad94-a50b5d4209b8 | -3.6762 | -50.8773 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38865f11-3424-3206-b1f7-078a8bca0c0f | -2.8599 | -45.364498 | 2024-11-26 00:41:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e8ef99e3-dcbd-3f61-829d-dfa9c23de330 | -3.7124 | -50.1758 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdd10c81-1641-3005-b1dc-d0e97bc8f58b | -1.9304 | -45.754501 | 2024-11-26 00:41:00 | METOP-C | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 951a583c-7f10-359e-8309-13a1f900f2ee | -1.3473 | -54.624298 | 2024-11-26 00:41:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0f1bab7-b8b8-3b62-8a4c-7e5080c3a7c3 | -2.7652 | -52.8997 | 2024-11-26 00:41:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f6d4618-e005-32ee-97ac-cad57ecc7338 | -3.9858 | -48.082298 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78a3270b-d891-374c-8aea-f27cb8c4d422 | -2.2469 | -53.471901 | 2024-11-26 00:41:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4c9fc49-5138-3d7b-9360-a6ca231798c7 | -1.4709 | -47.1092 | 2024-11-26 00:41:00 | METOP-C | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1980f8d-d737-31d7-9152-0cdae24dd7db | -2.7811 | -53.015301 | 2024-11-26 00:41:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de1c92bc-1116-342c-a9ed-bb81250bca7c | 2.697 | -60.399899 | 2024-11-26 00:41:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 37de027b-450f-3e1d-babb-e59c276d97c3 | -2.7909 | -53.0131 | 2024-11-26 00:41:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82affc95-2f60-3b41-9c42-ea1c43cf9a75 | -3.0629 | -50.944801 | 2024-11-26 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1b79f53-1d67-30cb-b183-d2ba15b7b179 | -3.714 | -50.1828 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b36c0690-3773-3692-9b30-bc363e514d4a | -3.5161 | -50.219398 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 009bc261-4e06-35ff-82c1-4d90a2bd2bce | -3.981 | -48.061401 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f59e510f-7dbf-3659-9e2c-ba8bc4931572 | -2.5214 | -45.5924 | 2024-11-26 00:41:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9689393a-14d9-3356-8bfd-04a8e58c3dbe | -3.7238 | -49.954601 | 2024-11-26 00:41:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cff00040-21f4-3439-87e7-215af1c5529b | -1.6036 | -47.460701 | 2024-11-26 00:41:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5df85e4e-16bc-3977-b188-581900e608f2 | -1.7693 | -52.728901 | 2024-11-26 00:41:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7694538f-686b-3a97-9e7d-40d5c53a55af | -3.963 | -48.0728 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c734753-23f5-3a0a-92a9-2efb245d1063 | -3.6843 | -50.233398 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15edb18b-8c0a-3f82-a94f-a71a7dd659f7 | -3.4704 | -47.681702 | 2024-11-26 00:41:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c96e188-78f8-3e16-a9f2-d1b1dffc896d | 1.8239 | -55.9417 | 2024-11-26 00:41:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a73bba1f-aa15-3224-a099-a883f36059c3 | -3.9842 | -48.075298 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab982631-35f7-3ef5-9f53-35696578a38b | -3.976 | -48.084499 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 985dfd04-d4b8-3b11-9289-551218d16cad | -2.915 | -45.159302 | 2024-11-26 00:41:00 | METOP-C | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 25a6aba8-6bee-3023-b6c0-c5e6d3c538d4 | -3.5855 | -50.387798 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee45bfda-b8a0-3141-bd8c-78462eb520ee | -3.2843 | -51.1479 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a38fc04-1e91-3253-8270-41c51ccdc4a2 | -1.7829 | -52.743401 | 2024-11-26 00:41:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c20d7291-c7a7-3974-8dab-abac0f8d2b32 | -1.5603 | -45.669399 | 2024-11-26 00:41:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 834c6adf-8cf2-33b9-b5ae-6f9507e971ee | -2.7985 | -52.910599 | 2024-11-26 00:41:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adc2a05d-aa17-360d-bd49-c6df853e4c94 | -3.9248 | -50.5205 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce631b67-2037-3318-9dfa-c684a0beb94d | -2.7695 | -48.5807 | 2024-11-26 00:41:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f6060a3-0acc-33c3-8ff6-c3d9fb8ea7fd | -1.9801 | -53.293701 | 2024-11-26 00:41:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d54ee1ce-4dc2-3986-9b82-a1f88bc61443 | -3.5823 | -50.373699 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
