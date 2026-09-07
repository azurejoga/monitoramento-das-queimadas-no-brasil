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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 265631b4-2432-3dc4-beab-5c44e3750f1e | -5.36372 | -56.02725 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 840fd512-431b-3766-8d21-8c121eb8f3a8 | -2.91264 | -54.11995 | 2026-09-07 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d388a2b4-8e25-3320-a2cc-1a0ea2112f32 | -2.95561 | -48.70712 | 2026-09-07 05:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 36f183db-761f-3713-b0c7-27b00bdc9a7b | -5.68357 | -60.24256 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 438d61ae-9f06-3c93-ac22-0a66519b95c3 | -8.7549 | -62.42319 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecc5b927-4dbc-3352-800c-e10aced8c2ba | -5.30378 | -60.13503 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 24405658-8942-3d9b-9a2a-86e2702e270e | -8.71271 | -62.43673 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 891fed24-bf4f-37e9-91f2-1993833fe07d | -3.37987 | -59.41807 | 2026-09-07 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e370740b-3e7d-3d5e-9199-5748306e86d0 | -3.61212 | -60.57766 | 2026-09-07 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 542ccea2-be6b-3e7a-826e-d551e1c3e408 | -9.86766 | -60.28039 | 2026-09-07 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d052bd7e-7b9e-300a-9c96-8f031152afd4 | -5.26497 | -60.1836 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f92894f2-af06-3c5f-a7c0-44a6b8bcf5bc | -3.25388 | -60.64595 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81725451-9bc4-3bad-8ad4-f5ebc70e6717 | -5.28872 | -60.12169 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4393982-e337-3344-a0a8-a16b188f30e4 | -3.38277 | -61.32775 | 2026-09-07 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97dfa722-38f1-3609-8cb8-676a8b241dd5 | -2.82462 | -49.22889 | 2026-09-07 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9df66cb-833c-3dda-81a7-3e545815731f | -4.95262 | -56.25809 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68e007f7-ab6f-3071-88a9-39f61e302cd1 | -3.89906 | -60.9323 | 2026-09-07 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7374d1bd-094f-3db4-8377-9a23e8ad04a5 | -11.65052 | -52.87057 | 2026-09-07 05:23:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8a45f79-0885-3560-aad3-eefe43ba258b | -5.35392 | -56.02697 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ef7ee23-6df5-3639-afa5-a1ba0b38f985 | -6.06077 | -57.80188 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f043a83-d279-3833-93c0-05bee7f331e7 | -8.52822 | -63.87376 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 054a3f66-f1f6-37aa-8273-8a8b7e4f86c3 | -5.26707 | -60.1144 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d04a1922-bc59-3904-aeb8-8c520ca79d13 | -8.72685 | -62.43908 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94af3980-22d2-3289-884c-f3ef9adfa37b | -6.05965 | -57.78707 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd8af238-cf78-34a7-bb7b-e9127ae0f7b7 | -6.13436 | -57.74015 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cfd958e-e222-3731-bd62-eee39d297e2f | -8.5244 | -63.87311 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ee27f5a-97d7-338a-b87e-671b40d3c41d | -4.21689 | -48.56455 | 2026-09-07 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28525622-9773-3d54-83f0-9d02dbf65e40 | -12.75827 | -52.85653 | 2026-09-07 05:23:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 971f6419-c07c-362c-8661-be3e5da257b3 | -4.66587 | -55.63818 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1901299-d93e-3284-949c-8ae967e0f91d | -4.21062 | -48.56757 | 2026-09-07 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d53a3656-d85c-3ad8-8855-b15cd1a1c6e5 | -5.36652 | -56.01641 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e76bb7cd-7989-31ef-ba74-15be00bc8c42 | -8.7191 | -62.44193 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7f4c83d-e97f-35e0-9338-a1c746873876 | -5.15002 | -55.96598 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65ec4635-2f5c-3390-a07e-f6eaf652c71b | -3.37709 | -59.41404 | 2026-09-07 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20e5b7c5-020d-3597-a879-2ceb64626b72 | -3.38406 | -61.31973 | 2026-09-07 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0805a1ed-acb2-3519-8b84-8fc97bb180c9 | -2.71362 | -59.76685 | 2026-09-07 05:23:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8c540da-c23c-3e6e-bf2b-55e93671a74c | -5.26917 | -60.11492 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1982fd8b-61bc-3a58-a432-a541390cb41a | -8.71776 | -62.44995 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cb5a1c1-a5a9-34c5-b972-8dd35ac7940f | -5.37024 | -56.03237 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 609cae02-a977-306f-be18-2595c39a609b | -4.5941 | -50.9846 | 2026-09-07 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6ba0edd0-d304-3459-b726-e56e772263fb | -9.86324 | -60.28684 | 2026-09-07 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b129833f-8d0b-304a-97d4-08534d9abdcc | -8.72618 | -62.4431 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6447944-b3aa-3b7c-ab46-54a424e074d6 | -5.29257 | -60.14054 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 813d83a2-93e6-31d5-8905-a0b8f5b071dc | -8.74431 | -62.42139 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d5be17a-38b1-38b4-ab6b-71eebdffc317 | -5.27292 | -60.15565 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 983ae9a8-358f-384e-a74a-1f19edef256d | -4.1199 | -56.34949 | 2026-09-07 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d1565b8-5901-307d-b906-1821b289d1ea | -6.01924 | -57.69281 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 79ffb2d4-a0d0-323a-b3f8-66de018d27b2 | -5.22859 | -60.29125 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29717255-239a-3043-9525-28aab9a33e08 | -5.28815 | -60.12523 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2bc7f148-22f9-3b24-b75e-381c1fc86f2b | -3.23898 | -58.89339 | 2026-09-07 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 549a5d3f-2128-3984-8288-52772b2aaf1a | -6.86945 | -55.60105 | 2026-09-07 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b75e627-d0c9-3f25-bd5c-bcd0a4d43687 | -4.97355 | -56.28535 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb405b46-a641-3090-b0ca-cfa84f098a97 | -3.08326 | -61.53019 | 2026-09-07 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c38fac9-fcef-36af-98ac-dc247ac3700a | -5.15699 | -60.221 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99dcf2cd-918b-3bff-b11d-d3574d89e33a | -3.37876 | -59.42508 | 2026-09-07 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63e10c94-7685-368e-91b7-a46c9aff3d4a | -3.04831 | -60.794 | 2026-09-07 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86799279-a171-35b4-9d18-ac83545c9c82 | -5.35979 | -56.03611 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f505c8ca-9e54-3085-8686-76d14fe59450 | -3.07702 | -61.17924 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 44bcb36b-ed7f-3cf8-94b0-0d0fece09379 | -5.35329 | -56.03101 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea4f11c0-23f4-3e9b-b50e-010092a2cc9d | -8.75909 | -62.4198 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b85b029c-102d-3004-8207-2a01df6eadc0 | -12.76515 | -52.84105 | 2026-09-07 05:23:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd70008b-0ff8-323d-be3f-8e81afb99b6c | -4.12398 | -54.41514 | 2026-09-07 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf9ba03a-0305-3826-8df7-78258d4ba316 | -3.39043 | -59.41615 | 2026-09-07 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d95db968-ed62-31ba-8bc5-531d44cf1430 | -2.62862 | -59.40038 | 2026-09-07 05:23:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 752cabe6-ba8e-3446-a289-93e115a47210 | -2.76809 | -54.1772 | 2026-09-07 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 616a47ac-a085-30de-ba84-760d6ff63f6c | -3.01002 | -61.48026 | 2026-09-07 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 853b4987-359e-35b6-a062-5f42e5cdac1d | -5.29093 | -60.12933 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 717dd5f8-b6e6-3ec2-bb7b-4d52594fddb8 | -3.7957 | -55.881 | 2026-09-07 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ef7044e-1471-3fdf-bc33-1dbd8f069352 | -3.37598 | -59.42105 | 2026-09-07 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a378b07-722b-33f4-bbeb-59fa088fca54 | -5.25333 | -59.98501 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8705336b-7c43-3e07-b2eb-e5d26e2bd1f1 | -5.36882 | -56.02505 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ac0aca38-1198-3639-a7d9-9607c2e85ff0 | -3.12395 | -57.68844 | 2026-09-07 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79c4214f-4385-3ebb-bed9-f2784554ba3c | -1.2039 | -55.72548 | 2026-09-07 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe8a6d90-bc72-32fc-a88d-dde046382f51 | -4.21615 | -59.37135 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5085a7a6-8f98-321b-be25-ed35c6dc8c65 | -4.67078 | -55.63042 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b87f0ed7-97bf-32da-9510-f2b7e5bb7e0f | -5.99399 | -57.69992 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c9240622-c5ee-3bd2-a81c-93854e2d35ff | -5.2019 | -60.02759 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13bdb529-269c-3e2c-838a-6107053d176a | -8.71136 | -62.44474 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6f8e658-d9f2-3227-b63c-03cc78418d2b | -5.16049 | -55.96153 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ac74abd-aa3a-31e3-bc61-9ee3d3e6f8dc | -8.75645 | -62.43578 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff2b2ba9-739c-39d2-91c6-9f60278f8036 | -5.36399 | -56.03261 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77b1f3f3-6246-31f9-a8ab-a0759849126e | -2.67496 | -59.42561 | 2026-09-07 05:23:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 65c9adfe-c536-325f-b0c8-596b5b382f79 | -4.28367 | -59.97358 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 873044dd-69b0-32c8-9d61-e50f37e69fc7 | -5.84885 | -60.2543 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bee3d99d-3271-3009-99ec-9e2e0c530289 | -4.3778 | -55.69325 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e7e4b0a-a2bf-3e54-8b66-6a1537f94c88 | -5.32222 | -55.87622 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79f94b61-de4e-328f-80c0-c569d342b33f | -4.41768 | -59.96552 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9345ddee-3b5e-343b-b83b-abc2dce34b5c | -6.13095 | -57.69552 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0da5bc0f-bf07-3cb0-b3ef-16d5f0dd9927 | -5.99736 | -57.70044 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d82e9285-6a07-3ec5-8f63-0fbf8757d695 | -5.49332 | -60.20176 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad025730-2f75-3a89-9814-5daf04b823e1 | -5.14163 | -55.97298 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a5c0162-c788-3015-9353-73b5ae4ebfec | -6.05518 | -57.79366 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8ec16b97-1158-3bcc-ac03-edb80c2d0198 | -5.36819 | -56.0291 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a39dc284-1a7b-337d-8492-1ead922c9943 | -6.43987 | -58.15522 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63a3f049-bf64-3164-92f4-53df5280fce9 | -3.76922 | -61.7632 | 2026-09-07 05:23:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6495a53-b427-3e6c-a360-53f5a31ba467 | -3.26784 | -57.87415 | 2026-09-07 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c41887e9-533c-3ce2-b852-5c160a27716a | -3.15713 | -61.06561 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 630b5a34-aebd-301f-910a-2da004728ff5 | -1.85905 | -47.97858 | 2026-09-07 05:23:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a35e5be-79ad-3cfb-9cd5-ddf459efb8f7 | -4.97967 | -50.63059 | 2026-09-07 05:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 086ddda5-99fd-316d-8b8a-f2c4c2ad8b46 | -6.10507 | -57.66202 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README29.md)
