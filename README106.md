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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9cacb1d-da52-35ac-9f79-e81a8afa68ac | -19.65208 | -56.80437 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 6e050f36-bb90-3d55-b76c-e53b06eda962 | -19.65173 | -56.84671 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6df91147-6708-36a9-b78e-d12006479caa | -19.65161 | -56.85797 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 8cf9d03f-f7a6-3dfa-bcaa-476f7ad7975c | -19.65154 | -56.80902 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| c2ed8584-300e-3d4a-a58d-cf11285e9c1f | -19.65119 | -56.85133 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 49af8524-94ca-3152-850e-c964248b1ffd | -19.65066 | -56.85595 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| c762a233-c581-3639-a576-78f0429a8b78 | -19.65063 | -56.79199 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 8b71677c-cbd5-3c8e-97bd-54d340aa1d0e | -19.65007 | -56.79664 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 86c72cce-ca0a-306c-ba5b-fce8206fb477 | -19.64999 | -56.83432 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1fc8b1d8-2d92-34b6-b2b7-5d4ef8fb0c14 | -19.6495 | -56.80129 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 96756b4e-872d-38e6-90c4-60fed0a7636e | -19.64942 | -56.83894 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 87cc4e20-3bda-3998-ac5f-030e3cfd340d | -19.64922 | -56.78981 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| f35a729d-c95d-35e9-bcf6-636f3f3fb4c3 | -19.64893 | -56.80593 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 19b22171-1c89-3b46-86dd-0f319b3528ca | -19.64886 | -56.84356 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 605fb5bc-7175-34e9-b89c-edf3c86b4fad | -19.64868 | -56.79447 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1f82474a-09ac-3275-a349-c4cf244c5aa6 | -19.64837 | -56.81057 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 73e94a73-c468-3c07-af49-6fa5fd85165d | -19.64834 | -56.83687 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| a44f9e05-42b4-38e7-909f-b73bce2128e4 | -19.64829 | -56.84817 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 416e7bad-cadf-36d4-904d-8d1fcbf511ec | -19.64781 | -56.8415 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ae2b734b-28f2-3f4b-9f3e-3e5bc172ac8c | -19.6478 | -56.8152 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7905484d-067f-31ba-aa77-f110aeff6e97 | -19.64772 | -56.85277 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 1c78982c-5764-3eba-96b1-5b6ef908db4b | -19.64762 | -56.80378 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| be6ef0c6-3b2f-3f75-b94f-aecc92264425 | -19.64727 | -56.84613 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5a44cecc-57a0-3a40-9195-433381c349af | -19.64708 | -56.80843 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 2134398a-92c7-39ca-a6a9-399ff59d3f42 | -19.64674 | -56.85074 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| c68e123a-37a0-3c87-88af-7cbb6e1e9c12 | -19.64655 | -56.81307 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d267f6b2-2ce6-3b55-b29d-9071d2aefaae | -19.64621 | -56.85536 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 0a8ebf4c-ba0b-36a7-906d-edbfc3e75fb4 | -19.64617 | -56.7914 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 192de4c3-3269-3db0-b2ac-14134f74340a | -19.6456 | -56.79605 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b59b10a4-e04e-3a00-9a67-da2ee4ff0049 | -19.64553 | -56.83373 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 54f4f383-e699-3633-b006-77ec1f12eb46 | -19.64504 | -56.8007 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 16e3d03d-3742-35c8-a41a-387f44f4f99b | -19.64475 | -56.78922 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| e35ee21b-774c-3019-9cd8-3940dde5b3e1 | -19.64447 | -56.80535 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 040b6753-4501-3e16-a241-77fa33158fc8 | -19.64421 | -56.79388 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 16bac238-05fa-3b9e-b982-f931d3f7ade1 | -19.6439 | -56.80998 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 3000a3a4-be4d-339a-994f-31f973a6abf0 | -19.64388 | -56.83628 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 3b9010aa-0c5f-3dbc-a0cc-08c075a17154 | -19.64384 | -56.84759 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 0a46fadd-a8cf-3ac6-a353-c489b75cdb0d | -19.64368 | -56.79853 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c8e7b723-ded4-3431-a09b-a0095fdaaf15 | -19.64334 | -56.81462 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bab112b9-aeb7-3b80-a4f2-644aa794d6fc | -19.64327 | -56.85219 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 20.3 |
| 933b9264-7fc5-31a5-8129-45483e38fd83 | -19.64315 | -56.80319 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 063162eb-2c86-3b71-8f16-424a88b75faa | -19.64282 | -56.84554 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 00063956-a4ab-31d9-ac3d-11d44a897e39 | -19.64277 | -56.81926 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 33859b09-8959-3d9c-8cba-a5ccdd58160f | -19.64262 | -56.80784 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 75a42465-af5c-35f0-b9fa-5a1d95888258 | -19.64229 | -56.85015 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 41929c94-80d3-3ba4-890b-927bb9b81b9f | -19.64221 | -56.82389 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1a5e7a5c-4fa6-35f6-9ec8-b21a3fe687c2 | -19.64209 | -56.81248 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8702d762-b7b4-3e07-a77c-afe11eada2eb | -19.64176 | -56.85476 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| b355accb-72a6-35f1-b114-34ae25a05010 | -19.64155 | -56.81714 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 30f17d62-473e-3479-93e0-d7206a76ce0a | -19.64114 | -56.79546 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ce624849-32a5-3a8d-95e1-9e0fda318a7d | -19.64108 | -56.83315 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6111c661-85a5-3c9b-810a-33badecec407 | -19.64057 | -56.80012 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 57d1233b-45ed-3861-85b6-36730e8d41b2 | -19.64049 | -56.82642 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| a100f264-47a2-315b-b60f-1a045cedc16b | -19.64001 | -56.80476 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 00da8b06-e394-396f-8f75-62f322b30530 | -19.63969 | -56.98912 | 2024-10-24 05:25:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 9bfee993-87a7-350c-91bd-954c0a3fc349 | -19.63944 | -56.8094 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| aa08f496-88c4-3432-a190-1da9aee32b59 | -19.63939 | -56.84699 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| fca4c925-b345-3890-8792-25e092c26adc | -19.63888 | -56.81404 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| da5f64b2-2029-390a-a9e2-e3aeef2ff368 | -19.63883 | -56.8516 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 20.3 |
| 4c059822-e317-3a0a-ad45-65856f8737fa | -19.63837 | -56.84493 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9e56e126-e8b0-3950-bb65-44432908d63b | -19.63784 | -56.84955 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 69a1674a-72b5-340e-873f-5e948033ef49 | -19.63775 | -56.82331 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2fb8976f-6c36-3790-996b-bdd0a1ae6c71 | -19.63731 | -56.85417 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 765a8552-3f79-399e-aa89-8985160ff1fe | -19.63719 | -56.82793 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8a9ff0c4-9919-38b0-935d-597ac2fd4b2f | -19.63662 | -56.83256 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 3073adec-f8ea-3d04-abf9-f445a60abfdf | -19.63438 | -56.85101 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 66fd1bd7-00a8-38f7-8e52-560f716c9579 | -19.63386 | -56.81808 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c655dafc-7a4c-322d-ae27-7e4bb1d0e37b | -19.63329 | -56.82272 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 6ac6b7fd-7e45-3de4-83b9-de859d9d0eff | -19.63273 | -56.82734 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 88b99b4d-bad3-383a-b407-bacf9560353b | -19.63217 | -56.83197 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 27470144-ab35-33e6-9634-9f41ae19e0b8 | -19.62993 | -56.85043 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 5e029bd8-7b1e-32ee-90f6-675e1f83fc5a | -19.62604 | -56.84523 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 867ff94d-7171-3330-9b7d-0aba43db29cf | -19.62548 | -56.84984 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| de1a1b6e-4583-3351-b1d8-b7205fdc165a | -19.62159 | -56.84464 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| f9371ff2-9f34-3bc0-bd79-4544a508463f | -19.61714 | -56.84406 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 41fa2d0e-ee99-3b5e-9671-fb65dbb806b0 | -19.57527 | -57.00516 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| a2b1373d-b050-3fab-a449-14a74ca4b978 | -19.65583 | -56.77172 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 68d89801-1672-3ef8-811d-341b942e0840 | -19.65576 | -56.74998 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 58710082-4b3f-30a5-a1ed-656c59a687f9 | -19.65565 | -56.73361 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 33.5 |
| 9c5d615e-1caa-3eb9-b024-ef0411a52321 | -19.65529 | -56.7764 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| efe7f6f3-778f-351e-9639-e64ecfdbfe43 | -19.65511 | -56.73831 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| afcc971c-cb74-3178-ad91-0be46b753eed | -19.65476 | -56.78107 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 5b0f086d-d9c9-3c0b-8176-61ede3d8ab15 | -19.65462 | -56.75933 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f54ed8cd-48e8-30f1-bdbe-68b2749c6dc8 | -19.65457 | -56.74301 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 2fa4fc23-294e-3362-96c2-9afa2c032735 | -19.65422 | -56.78574 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 902707d3-9187-3a81-adad-981ab220bf6b | -19.65405 | -56.76402 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| b52586f3-12f7-36cf-8b96-a03804f7afdf | -19.65404 | -56.7477 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 176bfc95-ecb8-3873-af6a-0c34873135fb | -19.6535 | -56.7524 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 4f684856-2092-3038-8e8f-3bc26333f638 | -19.65348 | -56.76868 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.5 |
| eed4f6f8-a47b-3d4d-a01b-fdd0d4bf73bb | -19.65299 | -56.73532 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 26.2 |
| 4c7564fb-87e6-3071-a0b2-f55f11af5a06 | -19.65296 | -56.75709 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| f18dc923-40f0-3f55-a86c-81f41212ff77 | -19.65291 | -56.77335 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.5 |
| 86dcaff9-83e6-32f8-bbc8-1b12ddfef498 | -19.65243 | -56.76177 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 85348257-a052-3137-ab06-518397ac4a41 | -19.65242 | -56.74002 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 3d71872e-97c5-3ae5-bcda-e2dfdf9a95bf | -19.65234 | -56.77802 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| e07a44ee-6789-32be-8137-87e87c8938c7 | -19.65189 | -56.76645 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 6c61e16a-a648-3e31-bfc9-d4739f2f3e9b | -19.65185 | -56.74471 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 9cf574be-af45-315c-83a5-7492b5638658 | -19.65177 | -56.78268 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 613f27fd-b4d9-3b11-8cf4-e70dcaa7dc5a | -19.65136 | -56.77114 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 83f10393-eff7-3b63-bc8d-0ebe142119cf | -19.65128 | -56.74939 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |


[Clique aqui para ver as próximas entradas](README107.md)
