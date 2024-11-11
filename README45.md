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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24603680-8f2f-3615-b8a0-99dfcbefb0f6 | -17.70243 | -54.0917 | 2024-11-11 05:40:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1eb0861a-346e-37f3-afe6-303eb62c8e0f | -16.94446 | -57.6551 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| badb624f-3df2-312f-b7f7-f03f6585c4f4 | -17.28652 | -57.30927 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7be08e15-ce75-3c41-8183-d8a8edec5bb0 | -17.61779 | -57.49513 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 37a0829a-eacc-3fe6-bd21-026cb5406b1a | -17.62972 | -57.43428 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 26917419-9ac9-3d62-a995-9e7302012561 | -17.59913 | -57.52209 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| e8abbd06-1149-3c68-92e6-258f1efa558c | -18.32346 | -55.57493 | 2024-11-11 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a00c2195-da5b-3c1b-ab61-66ac6b662cb9 | -17.60569 | -57.5099 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 43789295-aab2-3d6a-902b-ff798c8de7b3 | -17.64078 | -57.52412 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.9 |
| 87abf918-09e1-353a-bdca-9a6abdafde66 | -17.61273 | -57.4453 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5541778a-afc5-3329-a55c-84801704dcda | -17.28719 | -57.49614 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 30ce1be2-2d2d-3336-8285-6ea981939fa1 | -15.9919 | -59.34742 | 2024-11-11 05:40:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b086f7d9-de3f-3355-8f09-544ec119ff6e | -17.30885 | -57.48921 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 5d84b87d-8853-3068-b6bd-09aa94d9fc42 | -17.29961 | -57.47832 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 893ac4b1-e2b2-3b54-bfaf-fd7e6c80ba02 | -17.30814 | -57.49558 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 83798f11-3d01-3c8b-823d-e4ead6018357 | -17.23851 | -57.49207 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5778c328-679a-371b-b714-e570584bca28 | -16.00537 | -59.34865 | 2024-11-11 05:40:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1f80a850-8049-3db8-a70e-f3d48d3bf5f6 | -17.6093 | -57.42837 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 03bd9ac2-5d5e-32bb-871e-f33a12230644 | -15.15945 | -59.91817 | 2024-11-11 05:40:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed2ec8ca-ccc4-3a3a-bbdb-a6f661b65071 | -17.6415 | -57.5177 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 98eb7cd7-6e5a-3617-9a74-ef64da407699 | -16.94007 | -57.64831 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 02d97740-e6c8-3d8d-847b-1aa78d10a5cf | -17.25027 | -57.48064 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| f5166802-bd39-3d37-a313-a3d0aab8de13 | -15.42848 | -60.27393 | 2024-11-11 05:40:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 122da79f-64ef-3052-b6ea-d07382475d9e | -17.6077 | -57.53943 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 7ec7a739-3b62-3b8c-b603-de8a6dd3f0b6 | -17.64114 | -57.52092 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.9 |
| 6fb8a910-8a5b-34a5-ae8c-90ed2956e8a5 | -17.29209 | -57.30666 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 22163edf-3af2-3862-9145-fb33ad090d2f | -17.68494 | -57.51934 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| da297e16-6458-360f-923b-a4ea5d553964 | -17.29304 | -57.49042 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 75265a7a-f914-379f-a738-3956dc1ac463 | -17.62387 | -57.535 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| e1369c74-d057-31e4-a594-4cf8404b8556 | -17.30032 | -57.47192 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 4a4eb9c8-3fce-3305-b695-f7b054538664 | -17.61708 | -57.50157 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ff27861c-378c-3d49-9d8f-d0dced5d596d | -17.63597 | -57.52027 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.9 |
| b2c3ca1c-b1df-3834-a3cb-1cd69ead4609 | -17.29855 | -57.48789 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e828a301-6e1c-30fb-858c-0da4a606ea5d | -17.69773 | -54.09051 | 2024-11-11 05:40:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 36bfde32-00ef-37a8-a9ce-2d1668bd7571 | -13.48494 | -60.66597 | 2024-11-11 05:40:00 | NOAA-21 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e92b6d57-55b6-3e9f-a4c2-2dd771b7dc3f | -17.27724 | -57.49163 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| adffb594-191b-3adf-bffb-39049ee04539 | -17.59878 | -57.5253 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| ff926872-f93d-3cdd-b242-b618fdb4d691 | -13.4889 | -60.66653 | 2024-11-11 05:40:00 | NOAA-21 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4419898-867e-3be7-b31b-86af0c9c9368 | -15.97689 | -59.32131 | 2024-11-11 05:40:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b944d2e7-71f8-3e61-b973-bb80870b9de2 | -17.61343 | -57.43882 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ef4d54de-1d12-31a6-87a4-80e9bc8138d1 | -17.62489 | -57.43036 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d816fa70-bbee-3ad8-b66f-e55577d7da06 | -17.2941 | -57.48085 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| c8d6aa0d-9f44-399d-a6b0-9716bd72491c | -17.59948 | -57.51888 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| cfbf15f8-d76e-3630-ade2-6b8cbb469b35 | -17.59432 | -57.51822 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 4cd8c7b8-154b-38a0-90ac-d68673a08e73 | -17.28344 | -57.48272 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| e903ae1d-ccb8-35c9-9f28-3b6e160377aa | -15.99854 | -59.36722 | 2024-11-11 05:40:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 27838ae8-074f-3945-ac9e-d738a2586ab8 | -15.41916 | -60.28049 | 2024-11-11 05:40:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c7e41b7-17d9-3890-9f10-9f7b20f4fb14 | -17.28789 | -57.48977 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| eeedc5fb-6862-31e6-b68d-9997b1e06d00 | -17.23779 | -57.49841 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4e1a1938-317a-3ff8-b70c-ff639edcc639 | -17.23815 | -57.49524 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c9f8b0f8-f7a0-31bf-8726-d8e9c09ec2df | -17.59962 | -57.42054 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b5d89adf-9907-3227-82d5-24388e136f45 | -17.61308 | -57.44205 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2622db62-5a45-3e0a-936f-b62474ebd13a | -17.24085 | -57.49016 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| fde3df33-3ae5-3354-a630-7bba11dbf542 | -17.28824 | -57.48657 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| e77d952b-94a9-39c0-adf8-bf55c9ca1969 | -17.6064 | -57.50347 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| e71b6abe-9e2f-3ff8-b1f0-b630bc812db1 | -15.98683 | -59.35171 | 2024-11-11 05:40:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2c71bac2-c90f-3b61-bb0b-bc91923ef118 | -17.2989 | -57.4847 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 86a7508b-cd9c-3e69-9e98-a070ac16c8d4 | -17.67977 | -57.5187 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f1f723bf-c9ba-3cf8-999c-9392226ad3e8 | -17.59501 | -57.51179 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 217d0b98-71f8-30be-8f9c-bfb9c2b4e042 | -17.27829 | -57.48206 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| a1ef745b-34fb-31d2-960f-ca8de545960f | -15.97239 | -59.32094 | 2024-11-11 05:40:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 3e72a9ae-0d70-32de-a394-353ea28a80fd | -15.96731 | -59.32536 | 2024-11-11 05:40:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7698f6d5-d31e-37ef-a1a4-f84a2e76c15f | -17.60604 | -57.50669 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| bf364db4-1f21-369b-9249-abb8ca38c800 | -17.71736 | -57.51043 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 42b02a29-cb16-3cc3-96ba-88eab6fa2db9 | -17.69597 | -54.0915 | 2024-11-11 05:40:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 60ae0fe5-82a0-3748-9564-03ea38b1208c | -17.61744 | -57.49836 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1de28bf5-3564-361d-b038-713fc8d67efa | -17.24476 | -57.48317 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| cbb5fe03-05ea-3f72-a09b-ce5d578042d4 | -17.30548 | -57.47258 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 670edc0c-4308-3005-8d63-68e4c5d2ad05 | -17.63526 | -57.5267 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.2 |
| b1044a38-9ebd-3215-8f12-7a2738a003e1 | -17.28895 | -57.48019 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 2e8b3e94-0d68-3975-a634-92e1039bcff3 | -17.24403 | -57.48954 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| aafa4944-b3e9-3e02-83be-f852ccd202e7 | -17.25115 | -57.49149 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 17478b68-e042-337d-b16d-695ab540cc9d | -17.31365 | -57.49305 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c6a8048f-0f85-3eda-8ac0-3d6855d07af0 | -15.9997 | -59.3578 | 2024-11-11 05:40:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 514b0cbc-273d-365d-87d0-8bc792c13dca | -17.25595 | -57.49534 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 22cb1e3e-806b-3063-ab93-d534fca1841a | -18.32303 | -55.57935 | 2024-11-11 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 091c9ec3-e0f4-34d6-9370-17d852d0d764 | -17.59362 | -57.52464 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 7d52c06d-2160-3ab9-bfa0-b29350be80a4 | -17.25149 | -57.48831 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 926a924a-6671-3bda-8638-88dc0c369432 | -17.61907 | -57.53114 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.5 |
| f14d2fa2-8da9-341f-bb30-850db7346f2c | -17.59983 | -57.51566 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 955d9339-ed85-3115-9b33-84637e5a2a66 | -15.99579 | -59.35267 | 2024-11-11 05:40:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 4b124cfb-cd8d-3c8a-ada0-f8d5ac5a63f8 | -17.63455 | -57.5331 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.9 |
| 3500cbef-fefd-3d71-a206-f35705d0d391 | -17.36146 | -57.44068 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e40ea5b0-bf2e-3aea-a718-2049da5e3d3c | -17.28684 | -57.49932 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| cca6dcb9-6870-3d72-bd1d-792280fed847 | -17.28239 | -57.49228 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 41196e26-8b0e-364f-89b9-8ffa62edcc5e | -17.64595 | -57.52477 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f20b33ad-a8b2-3938-be91-bd28d2af2123 | -17.77091 | -57.51634 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 07f1f5ee-6507-3f34-9890-26587e51c873 | -15.98627 | -59.35632 | 2024-11-11 05:40:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6ae6c7f1-5ca0-3b1c-948c-2ae1cd407dd3 | -17.24549 | -57.47681 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 9350043c-f0cb-3256-bb5f-38d6916c9d33 | -17.59467 | -57.515 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| c8a10daa-2bf2-3656-9c8f-c5a241457f21 | -17.60018 | -57.51245 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| bf846a6d-549a-3aaf-997d-f87160aa542e | -17.36219 | -57.43425 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9243f1e4-f41b-37e6-80e4-f2c815c2f67c | -17.63633 | -57.51705 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 728851be-b785-3ae1-a19b-28dfe9493b1e | -15.9718 | -59.32585 | 2024-11-11 05:40:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9dad16ca-e63e-375c-96d7-2f6a7446c50e | -17.3085 | -57.4924 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| da1f5e24-9a73-35d1-abbb-70677b41cb3e | -15.96673 | -59.33016 | 2024-11-11 05:40:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 6a52f464-b1ac-340f-8604-715f2df181af | -15.99639 | -59.34778 | 2024-11-11 05:40:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5f1e6a75-a6d1-3c49-bb24-5f18bc0cc41a | -17.60254 | -57.53878 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 5b497c1c-5c2a-36d1-a84d-3271e532dfa3 | -17.60735 | -57.54264 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| c044c4f0-ec8d-3476-aff8-dc2e92408fb3 | -17.28688 | -57.30599 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |


[Clique aqui para ver as próximas entradas](README46.md)
