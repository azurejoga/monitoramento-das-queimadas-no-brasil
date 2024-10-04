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

## Dados Diários - Página 169

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 592d2fb6-416e-39ce-b050-d606f9b39725 | -17.04192 | -56.71627 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 55202907-0493-3bd6-a849-3f9b5dfc3034 | -17.04059 | -56.76777 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 79563fcd-15c1-3e03-ae8f-dee6e21294a4 | -17.04031 | -56.70491 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 88a7fa06-8cc0-315d-9688-bc0c1e40f31d | -17.04012 | -56.74922 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| fa1101e1-c8f2-3aac-a34f-cff9e89deffb | -17.04002 | -56.77137 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 3562281c-9655-357a-85e5-4c2d15b7857d | -17.03974 | -56.70851 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b6437ebc-72fe-31fb-af3f-3f91aa3731c1 | -17.03945 | -56.77497 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 483e3ea4-ab91-3a01-99c6-a6fcde47539f | -17.0386 | -56.71571 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| efbc95f9-b982-3743-8a6a-0db08f07784c | -17.03851 | -56.73785 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.1 |
| 85c52259-6870-3e3c-b15d-9a268e3c5c85 | -17.03841 | -56.76001 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c4973977-2bcd-3bb8-8be7-6a82db30076b | -17.03831 | -56.78217 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e9aeeff3-a040-37f9-9752-0e70474e94a5 | -17.03784 | -56.76361 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8272ad98-e31d-3511-b823-94af31f0e3a3 | -17.03774 | -56.78577 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e41b9728-45fe-3cfc-8f63-a3eb10f7a0c7 | -17.037 | -56.70435 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 897bd410-346b-37df-8c38-fe91c4709367 | -17.03681 | -56.74865 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| f055d04a-409c-3c31-b574-5938798290c2 | -17.03671 | -56.77081 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 62a27407-40d6-38c2-8c5a-74c3928ba185 | -17.03643 | -56.70795 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 761dc9ef-3008-36ec-8720-7649b7977c5e | -17.03614 | -56.7744 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| dd188b21-6bc7-308a-b1c2-397b5d7ed2c3 | -17.03577 | -56.73369 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c445d9b7-d11e-313f-8e9d-c860dd8b8c10 | -17.0352 | -56.73729 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.1 |
| 1cefe823-6815-36bb-8999-46210757ea70 | -17.0351 | -56.75945 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 3d75c475-d551-3198-920c-738806ae204b | -17.03453 | -56.76305 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| c8634efa-d17a-3109-898f-44cc7a7ca845 | -17.03369 | -56.70378 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 18721c97-b4d1-383d-b91f-faff2995c78f | -17.0334 | -56.77024 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 497ba61a-c6ea-3356-a603-3c7b3163a30e | -17.03312 | -56.70738 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 994eca3e-b426-3c71-ac3a-87b8ea9a49d1 | -17.03293 | -56.75168 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1e0930f9-ec8c-33a3-9a98-eca38c1fb03c | -17.03283 | -56.77384 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| a5d540f7-ebba-3fb4-a10c-dd01f7c1ebbe | -17.03189 | -56.73673 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 4a905b11-b2cd-3a6a-82cb-73ed7197d4c7 | -17.03179 | -56.75888 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 22c23132-c41c-3d04-a32d-2d2e724ad972 | -17.03169 | -56.78104 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 86622fdc-faa8-3e95-8d4e-bfc8573801ea | -17.03132 | -56.74033 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 0ec4501d-2dcd-3ff3-9f66-4af869f3ed7c | -17.03122 | -56.76248 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| dac5a420-8b28-3dc6-a693-097baa0e2441 | -17.03065 | -56.76608 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 92f66b0d-b92a-3cd5-8aca-697c75e619a9 | -17.03018 | -56.74752 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| b227d576-d9af-3efd-aa09-65d3622000d0 | -17.03008 | -56.76967 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c7f33f26-5bfe-310b-bb86-2bc91cebfc71 | -17.02962 | -56.75112 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 0c4562d3-06f8-35f8-a11f-f9d82bb08887 | -17.02952 | -56.77327 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9a8981af-9fbd-3a16-ae57-3a434459c4cf | -17.02895 | -56.77687 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 40855a78-6339-33aa-94e2-42bfd568b4db | -17.02848 | -56.75832 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8aaa4d9b-3a50-3c64-bed2-64bc07d2f682 | -17.02801 | -56.73976 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 06368248-cb2e-3422-b64c-31f83c5768da | -17.02734 | -56.76551 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 479d13dc-6bc2-3216-894f-8acd7d30b3b7 | -17.02687 | -56.74696 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 141849df-7231-3a05-b6b6-21250fcb13b2 | -17.0263 | -56.75055 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| d911cf5b-4769-3f84-b8da-f2e71ebd85e7 | -17.02574 | -56.75415 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| cccd41d6-04ca-3169-bf98-82d0343e973e | -17.02517 | -56.75775 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 17e79c30-0cec-373d-8ce0-15ed3bdd6515 | -17.0247 | -56.73919 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 74c99c46-b909-3146-8403-1906116973d3 | -17.02413 | -56.74279 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2e1a16b4-5fcd-33de-a266-367ee4c2eb73 | -17.02356 | -56.74639 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b529ccbb-e39c-3892-85e3-bd3fcc0e9aef | -17.02299 | -56.74999 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 50e2b626-f950-3331-8f45-fc8368897c9f | -17.02242 | -56.75359 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| d0dc9065-e8dd-3345-b638-aa466c4f15a3 | -17.02186 | -56.75718 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0e29d7ed-605d-3e06-8b7e-1c2f11472bf2 | -17.02139 | -56.73863 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 81ec6db7-85be-3a44-a5cc-7d4773eb9755 | -17.02082 | -56.74223 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9ce2c307-b9ff-3b8e-8740-e923599acbbf | -17.141 | -56.75505 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| bf638fbf-083b-3d00-98f2-3884f1805557 | -17.13106 | -56.75335 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9ab30d6e-52fc-3c75-947e-29c2396a2f5a | -17.12993 | -56.76055 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 89eb315d-a2c3-379e-9744-e425b0e90710 | -17.12832 | -56.74918 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8fbac887-f583-3c84-aa47-4a40944bf1b2 | -17.12718 | -56.75639 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 81297fd9-d13b-339a-b109-4fa58328ec56 | -17.12501 | -56.74862 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 92f80367-1c0f-36dd-9fe2-ee541b589b36 | -17.12444 | -56.75222 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 201f6bf5-86bd-3b73-96b4-9bc30ace56eb | -17.12387 | -56.75582 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 26bed006-c8ba-3dd8-a361-334e24ec1c4a | -17.1217 | -56.74805 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d70037e7-2e28-3cf1-8dc9-296dadd535b1 | -17.12113 | -56.75165 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 53b81aad-6a57-3878-8190-0e354bc87096 | -17.11839 | -56.74749 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 6a610eaf-4004-3350-ab05-5d810ceed9b8 | -17.11782 | -56.75109 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 2644a19a-064e-319e-8303-98bb88f78c65 | -17.11327 | -56.77989 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| adca12b6-dc65-3edc-9ab3-bd65b0229121 | -17.1127 | -56.78349 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| c033ba6e-89b9-37ba-a283-d0d00f9e6ca2 | -17.11166 | -56.76853 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| b182bbe0-eab9-3e3e-b99d-d7b1ede6dc0b | -17.1111 | -56.77213 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b9249a41-1e0f-3b15-94b8-1fea2513dc5d | -17.11053 | -56.77573 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c765dbc3-bcac-3d67-84fa-c24b13eb8e73 | -17.10996 | -56.77932 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| d9fb37af-223d-300c-ba20-6cc4e333f650 | -17.10939 | -56.78292 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| fad036b0-9759-352f-82d7-95cebd6b32ab | -17.10882 | -56.78652 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 65e1ee06-04ee-3980-80ad-f6a538b7d7d3 | -17.10835 | -56.76796 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 85c0663f-11d8-3e12-92e5-f2d6c3f5c42b | -17.10722 | -56.77516 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1b6d2ec8-8bbe-3fd5-baf8-c349be5f1daf | -17.10277 | -56.78179 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 4c23cb6b-8313-30a1-a6a1-e7e0df27a6ab | -17.1022 | -56.78539 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 954f0843-a429-3be1-b10f-ea6f385a2037 | -17.09945 | -56.78122 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| eb7dfaf9-3f6a-3412-bef3-1c6026aaddab | -17.09889 | -56.78482 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 717a1545-28f8-3d56-9a1f-90917944b93d | -17.09169 | -56.78729 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 3d3011a9-7626-3979-9ba9-3fe8b5e5ae11 | -17.08952 | -56.77953 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| cdf59ee9-43ee-3828-9e7f-f56997a49990 | -17.08621 | -56.77896 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 85357e15-46e8-3871-8b60-33e18e9b12d6 | -17.07975 | -56.77816 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| a2c3788c-4387-36f3-8816-86f51366f63c | -17.07862 | -56.78536 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d547c23e-6f89-3bc8-9ea8-57078fc826f5 | -17.07587 | -56.7812 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e1ae383b-ff9b-38d5-b6f1-3082cda89285 | -17.07531 | -56.7848 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 724cde30-8a37-31b9-b8ba-71c04c1586b7 | -9.6389 | -57.19364 | 2024-10-04 04:57:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8903d422-e3f8-3a60-b3ad-9d3d8139cc50 | -11.99047 | -57.19404 | 2024-10-04 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e59d96e3-0fd0-3686-8c0f-61b0d7ac7997 | -11.98707 | -57.19347 | 2024-10-04 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1727d0ac-4d7f-3fe3-9c33-8ca0e9963750 | -14.80622 | -58.59437 | 2024-10-04 04:57:00 | NOAA-20 | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de33d2cd-173d-31c8-8ed2-073ecf207a46 | -16.58278 | -58.21163 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 47086c0e-a467-37e0-ac0b-d56824e1d513 | -16.58215 | -58.21542 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 319917f9-6c92-32a7-9fae-ba015031f971 | -16.58152 | -58.21921 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 8a99cc62-4ae6-31e3-80f3-f96424c8edf6 | -16.58089 | -58.223 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 24f20146-ff3c-3d9e-98cc-6b596d25e9ef | -16.58027 | -58.2268 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 57ca9b30-7741-32b7-b633-3aabf97566bf | -16.57812 | -58.21862 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| de36cb8a-6668-305e-9700-627de03c3b21 | -16.57787 | -58.19906 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 0e7a6ce2-b8d6-3665-a393-ae24bd5b44b3 | -16.5775 | -58.22241 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5e500e52-ec54-3019-90f3-a0d4e9289348 | -16.57447 | -58.19846 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 82c3627a-7b2c-358f-8a67-aa6222f3bae1 | -16.57108 | -58.19786 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |


[Clique aqui para ver as próximas entradas](README170.md)
