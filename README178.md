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

## Dados Diários - Página 178

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 687cf456-e767-38a1-869d-4048b38669f6 | -7.96934 | -47.03657 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 10053e5a-83e8-381a-a7d2-aee3b24c2f86 | -7.75944 | -47.0273 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4eacca1f-3216-326c-9a0d-ec484f8d2f2d | -7.75838 | -47.03102 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 689099f9-527f-3019-8b3f-50e7aa18985d | -7.75772 | -47.02686 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e529be14-8662-34f7-806f-03414caf788a | -7.75584 | -47.02787 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2476261c-2458-3135-a60c-fbbf5db160db | -7.75412 | -47.02744 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 783d2ffc-219e-3fd0-8ae2-0a7bbb4d98e1 | -7.73427 | -46.94897 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bfebf108-2197-3e17-8e38-d4cc6abfa350 | -7.70269 | -47.36691 | 2024-10-25 16:52:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7e7380b7-1679-35a9-939d-2273792ccbc8 | -7.70253 | -47.36822 | 2024-10-25 16:52:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ac27ba03-8dd0-3a90-a12b-82b4681abfb3 | -7.65464 | -47.3622 | 2024-10-25 16:52:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| ffe967dc-5725-385e-afea-ca8dc8ae8fd5 | -7.63698 | -47.15993 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c0085553-cd88-37a1-a9db-b1ec7ad89614 | -7.63632 | -47.15579 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ef861205-c7e7-3310-9ef1-00722f67d56e | -7.6334 | -47.16052 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0b1e34df-2286-364b-b1be-1b0072f04c36 | -7.63274 | -47.15639 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ca93a471-f83d-3bbd-8c43-6e612544dffe | -7.62397 | -47.17054 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 0538cf5a-9213-3c9d-a41b-3888bbcc1ef7 | -7.59864 | -47.19579 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8a6962a2-9f87-3827-8156-cf09f966ab87 | -7.5853 | -47.04484 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7a5e63c3-21c0-3a28-b0fb-0d41aa98c91f | -7.57384 | -47.47001 | 2024-10-25 16:52:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8610994c-e07a-3ae6-b6af-6bca27ee6679 | -7.57244 | -47.03405 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 03f73ca6-89ba-37e2-886f-c96aac51915e | -7.4876 | -47.52049 | 2024-10-25 16:52:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b244f698-d317-3514-a307-1119dda44b0c | -7.44234 | -47.21169 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d19f7ce1-0181-37b0-95b6-d450149825cf | -7.43876 | -47.21226 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 082ef43b-27dc-3eb5-b1e6-aa8b242d4e00 | -7.35944 | -46.99409 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82773131-b403-31d3-9ff3-813e6f6c7af9 | -7.31092 | -47.43673 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1da32304-da4d-3ea5-a373-9594dabe8db6 | -7.27568 | -47.19541 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 265f6229-4052-3582-b33d-bad2ed033ca9 | -7.27344 | -47.13579 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 9db0eefe-1b98-3a37-a93a-c24a4a4e15d0 | -7.27148 | -47.30575 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d8c5f1a4-32b9-375c-b657-a4cd83e66601 | -7.26271 | -47.38173 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| cbaec67b-3cf4-3240-9a0c-ebeb71ec9d32 | -7.26022 | -46.89167 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 348d9190-31c3-391e-ad66-9fbf40c0e785 | -7.25955 | -46.88751 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0254b6e5-31a6-3c84-b548-9ba19dff8b93 | -7.23554 | -46.87801 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| b5f33634-7c87-3964-aeca-dfbfb296e1d8 | -7.22492 | -46.83557 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1f0b76f8-b5c8-37c1-bcf9-f42351aaa243 | -7.20455 | -47.47434 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2ab67666-510d-3278-a3ce-357661ca89c5 | -7.19049 | -46.8319 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2842f1c2-e291-30f4-aeee-c59d0d7607b7 | -7.13464 | -47.04179 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 7f4e6b8f-d85b-3872-9608-74c73a8b36b5 | -7.10455 | -47.20938 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b08f2ff9-9426-3c6a-908b-4f5e43d63769 | -7.10356 | -47.22634 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8cccf494-b7f6-3505-a9d5-1231e3123bd8 | -7.09589 | -47.31652 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7fe49117-1b5d-3d7c-974e-b290fdc280f5 | -7.09177 | -47.19867 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a03ee01a-95bd-39a4-a465-f63ad3115e24 | -7.08361 | -47.21687 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1f58ef58-10bf-3dbb-b026-f57c1203d723 | -7.08295 | -47.21278 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 93a3ce97-8e1c-31ae-93bc-31c88adc645b | -7.0735 | -47.22287 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9b4857ba-455c-361d-9342-328fd7f566f1 | -7.06991 | -47.22344 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 60615802-c5cb-3806-850b-b2ad96cb0ecf | -7.10867 | -59.38517 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 94d5ab03-1e72-3913-9eec-8b6fd529339e | -7.10822 | -59.38185 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 11af50af-d44a-3059-8d4a-5ade88c9eb68 | -7.05424 | -59.33701 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c9576fa8-1288-38bd-a809-2e9a76658a98 | -7.05379 | -59.33376 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e550aebe-875f-369b-85ad-f596fe5f8792 | -7.04127 | -59.80315 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e7d8141a-eac1-3e5c-b66a-9f53db436396 | -7.03967 | -59.3094 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9f6a2456-5604-3b63-acd0-31a943e1bfca | -7.03932 | -59.80195 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 68a4c388-04cb-3c8d-a9d8-30f93adfb604 | -7.03921 | -59.30611 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2a98df34-7b5f-3a30-8b07-4382f97217c4 | -7.03491 | -59.79704 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a2f06f97-e58e-3193-9bb8-374136513b1e | -7.03341 | -59.79932 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6f96c9e0-202f-344b-8472-f6219d9e7eb2 | -7.02556 | -59.78281 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 86becd10-6b21-3280-8b3f-51a3b7dec99f | -7.02057 | -59.78675 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1b70548a-e250-3ccc-8538-1a23df3dec8e | -7.0201 | -59.78337 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2380b080-7445-3430-9f67-f893a5d7695a | -6.93522 | -59.21502 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8ad90ad7-543d-3de3-9ff1-4e6a40e71eea | -6.89765 | -59.79157 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 113fd622-72a1-3d75-91db-b4a94f173652 | -6.89222 | -59.79229 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c17f84a8-a085-312e-8984-8bd6af132b10 | -6.89175 | -59.78885 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bcf4b35f-8521-382d-9ff1-93c1300d35e9 | -6.88632 | -59.78958 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.7 |
| bac9456b-82a2-381e-a980-aaaed1df0070 | -6.8809 | -59.79035 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 0b1c70ec-12f6-3359-9541-02a799a1f75f | -6.87098 | -59.79867 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 91501e6e-cec2-3aa8-9f54-7ad4a19e46f1 | -6.87051 | -59.79521 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.4 |
| b149fe13-1eca-32bf-ba52-e18d5da6c002 | -6.87004 | -59.79181 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 6c047888-98fb-3c19-b8d3-50ff6be29b30 | -6.86509 | -59.79604 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 4918a486-b614-3c8b-80e0-cf9f760cc405 | -6.86463 | -59.79262 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 748e7635-f3e3-33c0-81b7-e3be268f1cf6 | -6.86416 | -59.7892 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| af9bf567-bb6e-313a-be00-1c617651e377 | -6.8636 | -59.27571 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 5fccb28d-4185-3b5b-b477-90aabc224ef2 | -6.86331 | -59.27615 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7df8c13c-a628-3585-b816-84923c04564e | -6.86316 | -59.27246 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 84d82e99-0cca-380b-a5fb-e8ae4d14d885 | -6.86285 | -59.27289 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 093d3887-857d-3461-b51f-e402cd75eadc | -6.85919 | -59.79332 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 3a5c4ec0-3e41-3f49-bd83-07ca311b8b5d | -6.77979 | -59.44432 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| e70d17e1-1b71-3c57-98eb-6bbbd61bbe7d | -6.77944 | -59.44573 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 2ea8b4c9-8e06-3b45-9b26-8d4025e14b11 | -6.77933 | -59.44109 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| aa348602-e562-3f0c-abc8-46afcf08e7b2 | -6.779 | -59.44249 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 6b36949b-8402-3371-ae23-9e9258d69ac9 | -6.77857 | -59.43926 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.4 |
| a584c1bf-b6fb-3b05-a29f-6425c0afe250 | -6.7412 | -59.32351 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a7278d47-2336-3fc4-a273-ba201612c546 | -6.73596 | -59.32427 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6aca9d44-4e64-3f0b-8d1a-4f978569d723 | -6.7355 | -59.32104 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7153ea65-fa00-3b57-89b0-2f874bcc33a2 | -9.31835 | -60.50289 | 2024-10-25 16:52:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 2d9c7ad0-0542-3635-a4a1-23a053d5c0dd | -9.31781 | -60.49865 | 2024-10-25 16:52:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 6cd944a4-90ab-3da5-af62-ba9c2c17d9cd | -9.09384 | -60.3667 | 2024-10-25 16:52:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 0d3b3823-f002-32c1-ae80-0cf034480a74 | -9.08801 | -60.36734 | 2024-10-25 16:52:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| b341c5ce-d676-30c7-848a-ebd54046f174 | -9.02531 | -60.66273 | 2024-10-25 16:52:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3c2f5dca-aee9-33ab-8648-24a0b1099f34 | -9.99171 | -60.0741 | 2024-10-25 16:52:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 67c75016-57dd-39c9-a1da-5f16de63293d | -9.97832 | -60.01362 | 2024-10-25 16:52:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 1493b112-5b50-3327-ad1e-cf132208a82c | -9.97781 | -60.00955 | 2024-10-25 16:52:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e79d73d5-c3e2-38f4-8b88-5c9346714a5e | -9.97629 | -59.99727 | 2024-10-25 16:52:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c147ea0d-2804-3b92-bf6d-e89f5051bdd3 | -9.88191 | -60.32889 | 2024-10-25 16:52:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 986af53b-6c1d-379d-b658-ef328f06a979 | -9.98938 | -59.7795 | 2024-10-25 16:52:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| abce3d3f-77ba-356b-a176-5f523de1ad9c | -3.61544 | -60.31075 | 2024-10-25 16:52:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 819aa199-6b2c-359b-86d6-146aa0c438ab | -3.61496 | -60.30742 | 2024-10-25 16:52:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| eb455524-8399-3c10-a631-865119d9f5d7 | -4.51996 | -61.13954 | 2024-10-25 16:52:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e4e71f8f-1d62-37ea-be5c-f709e2d3e769 | -3.77172 | -61.22545 | 2024-10-25 16:52:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 363cd5fd-3328-3c85-adda-74a57e45e2f1 | -3.76775 | -61.2781 | 2024-10-25 16:52:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5c702196-34a0-3703-b9da-1ec621634e94 | -3.75861 | -61.29567 | 2024-10-25 16:52:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 5430aa5a-ade0-3289-a866-9f57681c0548 | -3.66795 | -60.48109 | 2024-10-25 16:52:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| de33415a-1876-3b86-b17b-7d7a8cceb0e1 | -3.66743 | -60.47762 | 2024-10-25 16:52:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |


[Clique aqui para ver as próximas entradas](README179.md)
