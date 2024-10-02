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

## Dados Diários - Página 177

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf1e801a-de1a-3c14-b45d-8d7536443d4d | -16.8196 | -55.89116 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a4c494d1-eed8-3a6a-a92e-3515ede723aa | -16.81918 | -55.89503 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 267b6267-7d2a-3f9d-915f-9049404cd1c4 | -16.79825 | -55.93143 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 36e8b8c3-f150-3503-9824-ebc7d8c493eb | -16.79267 | -55.93077 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1f43742e-2871-3fd8-8d4d-e47712589adb | -16.68027 | -55.93513 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| faad324f-60e3-301f-acdb-5d73ba2de12d | -16.67986 | -55.93895 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| bc5bb693-ff91-3076-9361-021bd1d6b51b | -16.67945 | -55.94275 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 6c568475-e4c8-311e-baf7-5d6d603a4c90 | -16.67388 | -55.9421 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c7234cc7-10c6-311e-ad16-6b922b1a0c5f | -16.66832 | -55.94144 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| aa5a1026-8f4a-352d-8f4c-d7d0d98c30d0 | -16.65841 | -55.92862 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| bc6c4913-52b2-3ddd-a34a-7bcceb553d61 | -16.65283 | -55.92797 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 32538b6d-bd49-3724-adae-3ea8c9606569 | -16.6488 | -55.92451 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1780d9a4-0762-33f8-b40d-f6536b8b531d | -16.64836 | -55.92834 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5e70f323-2647-39b6-bb98-9df82e240191 | -16.64766 | -55.9235 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a7da0c0b-ca20-3a61-a86d-fdb6d203bed0 | -16.64726 | -55.92734 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d6365064-c04b-384d-91b2-f59ca7696c5a | -16.64365 | -55.92004 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 01996ef9-0bbb-3baa-bcf2-8c0d06fc89f3 | -16.64322 | -55.92387 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9197df2e-1a13-34d6-a489-5b392870a6c2 | -16.64279 | -55.92769 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e0495579-0dd7-3819-9a7c-413159ceeb00 | -16.64249 | -55.91901 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| bbaff0d6-1ba8-3bf8-a0dc-61a78f8bcd03 | -16.64236 | -55.9315 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 2b5103ed-c4dd-3407-8173-cfea0297f9d1 | -16.64209 | -55.92284 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7ab7390b-7f46-3238-a18a-a512a3edb925 | -16.64194 | -55.93528 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| fee4f1ef-ab7f-3f08-8cdb-f43e4648bd80 | -16.64151 | -55.93908 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| a439376d-851c-31a6-907f-2ebfcd6975e7 | -16.64128 | -55.93048 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b1800876-97b3-3390-9246-cd3559afb921 | -16.64088 | -55.93428 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2edbef02-66ad-3cd5-be9c-bb7a4c28ef5c | -16.64049 | -55.93808 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7390a0e8-855c-33b7-95bf-f6e15d4b8358 | -16.63765 | -55.92323 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 854328d1-7048-330a-9fdf-2985f2d87563 | -16.63652 | -55.92218 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9a910b49-24f2-3685-b56f-fe1e825fc75c | -16.63594 | -55.93844 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f3156a8f-884f-3eb2-ae1e-3bd8ce6f91f6 | -16.63552 | -55.94224 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6c9160a1-6de4-32a9-8a86-614c89620145 | -16.63452 | -55.94123 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0f5c5272-7cbf-3a91-9090-b6a5a7d57bec | -16.63037 | -55.93782 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b6408260-52d2-30e9-8e4b-e8abe5919013 | -16.63015 | -55.92915 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f391fe51-4670-3b8f-9a54-4ed0e38a10e9 | -16.62523 | -55.93335 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 80d6f09b-c2a4-37a5-8b56-094648b4b63d | -16.62418 | -55.93229 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3cf2c751-8798-37ef-8177-e2e168731c0e | -16.60183 | -55.992 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 634dbc85-1f9e-3360-934a-73d4e5153e74 | -16.88229 | -55.92463 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 948e5779-932e-3a72-b2fa-18678d7c48bb | -16.88188 | -55.92847 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 10b214ac-3096-3d51-b67e-a43a488b075c | -16.88147 | -55.93231 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3460a774-ff1e-3228-b00e-7f53eff5aacf | -16.88107 | -55.93614 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ae2fd832-6301-3950-8864-9a3c2a2410b6 | -16.87711 | -55.92015 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 817aaab9-59d1-382e-8894-2736e308e098 | -16.8767 | -55.924 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 14e1ba0e-7431-3152-915d-4f1055206c17 | -16.87629 | -55.92782 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 7aee218e-900b-37ae-8ab2-5b53933b6e0e | -16.87589 | -55.93166 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7d4a54b1-d038-3e59-a51d-565e19c5688f | -16.87548 | -55.93549 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a1044b09-6baa-3307-a9ba-bc4ea7d77a2c | -16.87151 | -55.91953 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 591fab74-f07d-3952-a5bc-edcb56fb0484 | -16.87111 | -55.92337 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 452876c8-ea63-394e-920f-3803763396cf | -16.8707 | -55.92718 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 30b80307-1108-375a-abae-11adaa34b714 | -16.8703 | -55.93101 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7d464e96-79f3-3a90-923a-4eb05d2136f1 | -16.86633 | -55.915 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| df358c91-7d62-31a7-91a5-28ebeb2e35e5 | -16.86592 | -55.91885 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 3655c393-6360-3169-801c-8bc4e17c9136 | -16.86552 | -55.92268 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 7b2e41c5-7d17-31cd-b699-251eaae16722 | -16.86222 | -55.91556 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c8155414-390a-3b3f-81de-36ba25f2d739 | -16.86179 | -55.91937 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 32d43713-dc5a-339a-9664-bee2540e529d | -16.86136 | -55.9232 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 15d9cef9-091a-33b8-af3a-18fe071b2afe | -16.86108 | -55.96486 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 438c21ed-898c-3efc-bd09-1bbc15a9f031 | -16.86074 | -55.91434 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 01f1d348-4268-3570-ad88-c619c024acae | -16.86068 | -55.96868 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5967c735-4c88-3ab8-b8cf-daf4e77aab14 | -16.86034 | -55.91817 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 10213344-c6b3-3c51-8328-103c6babc05a | -16.85663 | -55.91489 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 85bd124b-d5a3-360a-a97c-8b96eb598a87 | -16.8562 | -55.91873 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d4be39f1-5391-340a-bb22-cc29d6a0786b | -16.85515 | -55.91365 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f1c611dc-9b41-3115-a50d-f8a28754df46 | -16.85475 | -55.91751 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4ec64034-b3a2-3f11-a508-c0814d28dc1e | -16.85435 | -55.92135 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b0898001-cc49-31ce-a7cf-05006763dd8f | -16.85061 | -55.91808 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3890fb79-6794-3fff-a6b1-109bfe0cd640 | -16.85019 | -55.92191 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f8e3dbbf-3714-3b00-89a5-95bea1977bcc | -16.84916 | -55.91684 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6f9f15d2-a970-3549-b009-c6ba6f1ae67e | -16.84876 | -55.92068 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 792c875a-a8d0-35e6-a99b-d2c9669448c3 | -16.84503 | -55.91743 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a367657f-8733-36b9-9e45-cb0fb769742c | -16.8446 | -55.92126 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1eafddc8-36da-3fe5-812a-433229826f77 | -16.84357 | -55.91618 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 30646b9a-8bcf-3032-a3c0-ef7c6be6d262 | -16.83944 | -55.91679 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b0a222ec-7c72-3e5c-bb1c-dd74ad2854ae | -16.83798 | -55.91553 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8eb5fd06-dd2b-306f-bebb-6b5f90cb486f | -16.83385 | -55.91618 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 38d270da-cbd0-3864-99cd-a9fb36b1ae7e | -16.8335 | -55.97038 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 855941ab-540f-320e-9bd1-9cf220520891 | -16.83243 | -55.96918 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e3f9fdfb-daca-388e-8409-2dc7a903c919 | -16.83203 | -55.97299 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ea649e64-ae75-3fd2-8f53-4c5111207937 | -16.82825 | -55.91557 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 11cd5b3c-8673-345e-8ead-452a39c3cd9d | -16.82783 | -55.9194 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 5ababc74-e119-3a64-bb67-e08f450d2f9c | -16.82751 | -55.97353 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e36359ff-597d-3844-8292-fc2118ee8862 | -16.82741 | -55.92323 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 306c4f3f-3bb4-3cff-92d6-f958a443b97c | -16.82267 | -55.91489 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 64eca92c-0706-3dd8-a017-331093fc3bd9 | -16.82224 | -55.91874 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a0896e6f-7335-3770-ac79-757ea3de513f | -16.82194 | -55.97288 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| afa63396-d00f-3c83-a70c-6ade11e25168 | -16.82183 | -55.92257 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 8374b811-7dbe-31e4-93a2-e8af851698ba | -16.81708 | -55.91422 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 86a9476f-0d77-3c95-bd1c-315ee7fe423e | -16.81679 | -55.96843 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 7b7ff8f3-14fc-3cdb-bef3-8eca5b1eadb5 | -16.81666 | -55.91806 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| f3143c5a-a68b-38f6-a80e-2a0d01eef76d | -16.81638 | -55.97223 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 86806ba4-c2bd-35dc-9c85-7462d8da969d | -16.81624 | -55.92191 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| f8a460f9-2790-353a-94dd-2b0f1567897f | -16.8094 | -55.93278 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 88a5bf64-8756-361c-bd88-464efad31288 | -16.80899 | -55.9366 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a74a0c55-d4c7-354b-bf3a-cfb607c5d84a | -17.23424 | -56.18738 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 9a0778f8-3409-3523-9ed0-7e76d9bcc8bf | -17.23394 | -56.18832 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 5f502b72-d311-35f6-b6b9-0c3cf752de5f | -17.23382 | -56.19111 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 159ecea3-b4e7-3f98-810d-81720c831227 | -17.23355 | -56.19205 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| bd101d2f-7303-32d2-bbb0-95fc7a6d7b73 | -17.23341 | -56.19484 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 53515430-15d1-3c53-bfb8-a0d6270087c1 | -17.23317 | -56.19579 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| b048de3a-5104-3b39-8abb-0b90a83218c1 | -17.22954 | -56.17928 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| eeb5770f-49ab-31d3-a562-ff6b929ef4ba | -17.22872 | -56.18674 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |


[Clique aqui para ver as próximas entradas](README178.md)
