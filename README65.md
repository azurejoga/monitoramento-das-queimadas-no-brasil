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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 983d7676-08dd-36e6-88bf-eacf6fa0aaca | -2.68026 | -54.03557 | 2024-10-15 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a13c6cd0-49b8-3fb3-aa23-aff46bb1eb42 | -2.65558 | -54.62386 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec711eaa-9fe4-3dde-a23b-d179d1c15bf6 | -2.65493 | -54.62786 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d37ff123-d91b-3ce2-89cd-e5499d3396e7 | -2.65202 | -54.6233 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a280259-4dea-3e60-ac53-5e19ee6162e1 | -2.57191 | -54.01168 | 2024-10-15 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03e2c76d-84e2-3909-baee-d2aee7949ed3 | -2.56905 | -54.00732 | 2024-10-15 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cab0dc34-433b-34f7-8334-460b0f9507f9 | -2.56845 | -54.01114 | 2024-10-15 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b466e000-0e7d-355a-858a-e4949e9b9761 | -2.55226 | -54.61267 | 2024-10-15 04:49:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 15873672-59e0-3a44-adf8-35a665a33c22 | -2.51886 | -54.25568 | 2024-10-15 04:49:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6892780-d10f-3202-bcd3-3da1b0dcf504 | -2.51823 | -54.25962 | 2024-10-15 04:49:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5dc40d0b-f63f-3db2-9666-c147be677ae9 | -2.41815 | -53.81068 | 2024-10-15 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 30b1bffc-bdcb-3a77-ab2c-7910f3fe457a | -3.15808 | -54.92283 | 2024-10-15 04:49:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 540ffcfe-0f1b-39cd-a5d1-a9f36cc43cb5 | -3.15742 | -54.92693 | 2024-10-15 04:49:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98f67b99-5874-3ae4-9105-8f8a5a34878d | -3.12998 | -54.24438 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9b850a3-2460-3b6d-9cf6-7c7a28ba7d7f | -3.1288 | -54.2406 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4dcd7860-c5af-375c-9bc8-6a8421879ca7 | -3.12819 | -54.24444 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 65381ae3-5d5a-305d-96d9-e1e6dcb32eb6 | -3.12774 | -54.23614 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9702c2b7-762a-3a20-8dbc-37d87fa7641a | -3.12712 | -54.23997 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0013ae63-0a4b-32a3-bfda-9209f0618c32 | -3.12652 | -54.23238 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25eefca7-9d4b-3fbf-8d97-ca1229a6af8b | -3.1265 | -54.2438 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1d752ad-73db-3ad4-977a-abbedc441115 | -3.12592 | -54.23621 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 577b3422-1a7a-388d-bf6b-34bb6b7910c9 | -3.12532 | -54.24004 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fa6f5cc0-2d92-3918-8cd5-4974ab2f1000 | -3.12472 | -54.24387 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bca7cc3d-4d39-3145-a7ee-84c3bc77d37d | -3.12364 | -54.22802 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d2453f83-511b-3084-9875-ee8ea7c25c20 | -3.12304 | -54.23185 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 128de4bc-965c-368f-bb39-dc139cd6ce53 | -3.12244 | -54.23567 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8e346185-23e9-319d-8983-ca9aa1adda78 | -3.12184 | -54.23949 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 94838251-950d-3074-b0ff-0cbdaedb7a38 | -3.12124 | -54.24331 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77c12fc7-4c3a-33bf-b47b-ac9ec1942afc | -3.12077 | -54.22363 | 2024-10-15 04:49:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e1dbdc6-b8e6-3d24-a287-8890f8753b00 | -3.12016 | -54.22747 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fc401798-b81e-3484-8ce7-ec4dc9e84994 | -3.11962 | -53.7417 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e95c9f5-e4a2-3478-8906-e6de618a773a | -3.11956 | -54.2313 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c5e1023f-60a1-3b3f-884d-c71925cb24d6 | -3.11896 | -54.23512 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3cc860a6-ad10-39f3-b103-f1496e67f6c4 | -3.11836 | -54.23893 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9045a632-0cec-3463-a2a2-0256698c0adf | -3.1179 | -54.21919 | 2024-10-15 04:49:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9336f0c1-ed17-340b-993c-c5aa638e9a3e | -3.1173 | -54.22305 | 2024-10-15 04:49:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f1452a7a-51d1-3db2-8e68-e90600acf7e6 | -3.11669 | -54.2269 | 2024-10-15 04:49:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fb0a9512-9b1e-31cf-b797-8a9b7e3f55b8 | -3.11621 | -53.74116 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| afa5e943-cd62-3cfa-b481-d47c8b5bb8c9 | -3.11609 | -54.23075 | 2024-10-15 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 51adbec8-5325-3a09-b32e-0e2ff32dad85 | -3.11516 | -53.72589 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d938c956-9a8d-3a6c-88aa-56ad4a60e65f | -3.11504 | -54.21477 | 2024-10-15 04:49:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3dd6f91c-a405-3e08-9fde-3a404423f004 | -3.11443 | -54.21861 | 2024-10-15 04:49:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ddc950e8-83af-3d22-aa55-a0dca174cc85 | -3.11382 | -54.22247 | 2024-10-15 04:49:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6ec7739b-8ac5-394a-9c37-848c6a9977cc | -3.11339 | -53.73694 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 63a78f06-a853-346e-968b-818c28622739 | -3.11322 | -54.22633 | 2024-10-15 04:49:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4ffead11-ca07-3e58-a295-bb452fa424b8 | -3.1128 | -53.74062 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5b87ebb-0ccb-3022-81fd-922b04b853ec | -3.1122 | -53.7443 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2de9ccda-69e1-368e-9fd5-c5c51efa4c86 | -3.10938 | -53.74009 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 34e4b667-dd65-3576-b47a-8940fe3c64d8 | -3.10879 | -53.74377 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cd2ef6d8-c56d-3c2c-a670-6231d0729ad6 | -3.10656 | -53.73586 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 51b84e97-c5d5-3728-bc11-0ad26b9a8d95 | -3.10597 | -53.73955 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d3b1250f-032e-3aa0-8776-4fb87ca2b0fd | -3.06524 | -53.88638 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57c5e4b9-1466-33c0-adfe-3cc97998b85a | -3.06466 | -53.89008 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 435ef93e-3cf7-3114-a2b9-fd4ab6ce1342 | -3.03923 | -53.93972 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 63ce754d-f019-378b-80ce-a3c39549f507 | -3.88868 | -54.6826 | 2024-10-15 04:49:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 202660f4-5a77-3a36-b0ff-5cc7e7d7895b | -3.76476 | -53.85277 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 424aa02b-0a78-37c0-bf28-15369fc92b90 | -3.72244 | -54.20533 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd2d64fd-196f-323f-9ab0-fa92c1edc06c | -3.71959 | -54.20102 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c498c4c9-5cb4-35b3-8953-bb33d43477c1 | -3.71899 | -54.20478 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00772b70-194b-3f22-8039-6dde44d455a0 | -3.71614 | -54.20049 | 2024-10-15 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64f9ac89-37a1-370e-8a75-6e06dd8d4098 | -3.62208 | -54.67392 | 2024-10-15 04:49:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b4e4d69-2275-3f27-b900-05753d16b42a | -3.61855 | -54.67337 | 2024-10-15 04:49:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 274c1102-822c-3571-b519-63662bd4ee83 | -3.61788 | -55.30191 | 2024-10-15 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5d942ab-38ec-3964-9292-c11edc8e817e | -3.60892 | -54.73288 | 2024-10-15 04:49:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d7080c5-7011-302d-be64-e62f7fac541c | -4.47561 | -55.08958 | 2024-10-15 04:49:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec02bf5c-26c6-3961-baf7-690764619cb6 | -4.45068 | -55.08547 | 2024-10-15 04:49:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4ad6523-9dde-3071-a954-acde6b6e2b0a | -4.44712 | -55.08488 | 2024-10-15 04:49:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a76abe9-027b-34bc-874e-de324ba0fe60 | -4.44692 | -55.01843 | 2024-10-15 04:49:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 867a46bc-9b0e-3e75-ad7e-3d91a0247192 | -4.44355 | -55.08434 | 2024-10-15 04:49:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eafd83ad-19fd-3749-a876-c2ca1789f04b | -4.4261 | -55.05677 | 2024-10-15 04:49:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 454917e0-0ccb-317d-96c7-e2a0a4d6151c | -4.35623 | -55.13427 | 2024-10-15 04:49:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e9d9512-1c07-31fc-95b1-46c68c2979a4 | -4.35557 | -55.13834 | 2024-10-15 04:49:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ab8c711-73eb-367d-93eb-6d70b9fa85fb | -4.34615 | -55.12848 | 2024-10-15 04:49:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98be5b5d-3d6d-3332-aa5e-52f594e98088 | -4.34549 | -55.13257 | 2024-10-15 04:49:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a87239e3-837e-3412-aaca-3c261a4de28d | -4.33584 | -55.05623 | 2024-10-15 04:49:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ec1ae49-216a-3dc2-a723-db3d867c5904 | -4.33223 | -55.21505 | 2024-10-15 04:49:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d113ce0-6e4a-35c9-8bc7-f9c74f581d96 | -4.2221 | -54.6366 | 2024-10-15 04:49:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79072d5d-d56e-31d8-a7d9-c662de29780e | -4.19665 | -53.91563 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f9ff81e5-4db9-36e1-bd21-829adca296c3 | -4.12822 | -54.23264 | 2024-10-15 04:49:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1fe57124-202a-313a-b5ed-069c7afb6112 | -4.06226 | -54.70815 | 2024-10-15 04:49:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 175602a5-5d4b-3e36-997c-fde49ea49bd9 | -6.14018 | -55.59553 | 2024-10-15 04:49:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b75ec863-87b1-3d87-b38e-836a2672cd44 | -7.87697 | -54.72071 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb6b7fc3-c637-3830-946b-ce356adbe06c | -7.87595 | -54.70545 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7734b516-e845-3c60-ad66-93be7d568a7f | -7.87518 | -54.73174 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b85e434e-bea1-39c3-ab02-0a559b94d3b8 | -7.87356 | -54.72018 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f86db7ff-02e3-3dfa-b605-133a7a74d873 | -7.87076 | -54.71593 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d061543e-7506-3ef3-8493-a644eb742d67 | -7.87016 | -54.71964 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fe61f01-c090-31d3-a33a-5dd2e48cdcf2 | -7.86855 | -54.70801 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bcb1403-76ec-337a-a39d-3ae099b70b38 | -7.86796 | -54.71169 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa720c68-af89-3258-9a83-8ee79bb51f0d | -7.86736 | -54.71539 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e0f4a40-1e9e-34d6-a5ac-8e51bc50de0d | -7.86456 | -54.71114 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77c29e80-bd8c-3aab-a118-6bae4dad5781 | -7.86395 | -54.71485 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bec49467-6db0-3a1f-8cda-ca9fd379db2b | -7.86013 | -54.69538 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e37d1f01-9ba1-3871-a9ea-4b4a3fbdaa7b | -7.85733 | -54.69117 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4660339-7f69-3431-b5ff-a8c2d76644b5 | -7.85673 | -54.69484 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 24b677dd-357f-33a2-9096-1419e81b7324 | -7.85614 | -54.6985 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ea860a32-82e9-3152-a36b-f123a99379c3 | -7.44566 | -55.1264 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dab24cb8-a0ab-3bab-bced-d00cac89f4c5 | -7.4436 | -55.1268 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6839d507-d4ed-3a54-acb3-9a6bed16ef1a | -8.48204 | -55.16579 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f140c336-5e01-38df-bfc2-91f6a9c118c9 | -8.29603 | -55.10203 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README66.md)
