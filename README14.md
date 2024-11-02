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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e26030e-0c42-3d73-bcb5-a809eb4a8cd9 | -2.56039 | -48.95692 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f41d5844-a18b-3c18-ab87-b167cb49a2ce | -2.55917 | -48.94812 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 84187873-c2f6-391f-b4db-2c6b7c3ab5d2 | -2.55358 | -49.63392 | 2024-11-02 00:54:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| dbfe08f5-1cb5-326f-991b-531d887af63d | -2.51664 | -49.23893 | 2024-11-02 00:54:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 5e37cdd1-4d8e-3ed9-a78a-cac837e05362 | -2.49445 | -49.0799 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 026bcef1-4135-3377-897f-966fb96411d2 | -2.4335 | -49.62967 | 2024-11-02 00:54:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 149e735a-30e2-3d60-95b7-0b8742fbd03c | -2.43307 | -48.96281 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 886fedb0-ae14-3d23-9153-2de58e4860c8 | -2.38697 | -49.1644 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 08654afb-5317-3445-8482-a2bab417276e | -2.37075 | -49.1127 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6ccc4d4f-dc1e-304e-9f9c-730855a9e325 | -2.36952 | -49.10388 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| d2047a58-dbb3-31fc-9c15-5e75ed949c6c | -2.35141 | -48.909 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| fea93818-2029-33ea-9d00-7b61069a0dd6 | -2.35018 | -48.9002 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 21513caa-4f28-3898-ad00-12ec0ed56a37 | -2.34298 | -49.10762 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 39ab286b-c4b8-3110-af18-03ad820c29e5 | -2.32858 | -48.93911 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c24fb975-ce35-37ac-a99d-de1d79ffbaac | -2.32097 | -48.94915 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7664be84-3379-3efa-8694-d2b625220f41 | -2.31974 | -48.94035 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 63533ae1-6db7-3879-97aa-9b29a82fa5e7 | -2.27875 | -49.11351 | 2024-11-02 00:54:00 | TERRA_M-M | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 98eab578-fad3-3c25-ae96-65e91b66e2d0 | -2.27603 | -49.15885 | 2024-11-02 00:54:00 | TERRA_M-M | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b03c329a-0988-3e96-a299-4cb1ce9e4161 | -2.22286 | -49.57076 | 2024-11-02 00:54:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 17acbd47-cbd7-323d-8974-5d36675ed927 | -2.21395 | -49.57201 | 2024-11-02 00:54:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9c67e4c9-76bf-3daf-8fe6-0e8f228a1fd3 | -2.47129 | -49.83639 | 2024-11-02 00:54:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bd6c523f-9422-3788-88bc-f6a9153d926c | -2.46499 | -49.79095 | 2024-11-02 00:54:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 2e78ec4b-7779-347a-b4f9-e8e16189001e | -2.46373 | -49.78188 | 2024-11-02 00:54:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2076e79d-1dc3-34e4-8160-181b8f4d5d0b | -2.45602 | -49.79222 | 2024-11-02 00:54:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| aac5b667-310f-3478-b265-e7fc5ce19b35 | -2.42105 | -50.40778 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d966cfc3-9d32-3b04-ac57-10b1f0d140c4 | -2.41448 | -50.42807 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7b13d5ff-6478-3f0d-b754-47e57804590c | -2.40613 | -50.42579 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 04630589-5f39-3d35-8177-8423c5c61562 | -2.4048 | -50.41631 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fcf2f835-40c6-3e05-a877-e380c4553b91 | -2.40025 | -50.32383 | 2024-11-02 00:54:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ec21dd86-f143-3954-866b-db76787181b6 | -2.39896 | -50.31441 | 2024-11-02 00:54:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 622ccaff-efbd-3c08-a7d7-e2b30970ad9e | -2.39211 | -49.79779 | 2024-11-02 00:54:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a49d4aaa-dec6-3098-a486-0c725154b81a | -2.23424 | -50.32087 | 2024-11-02 00:54:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8a25f4a6-7bfc-364e-a758-80866482f9d5 | -2.216 | -50.32342 | 2024-11-02 00:54:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 70e1f421-b6a2-31da-9be4-db0e23f392e4 | -2.20718 | -50.32129 | 2024-11-02 00:54:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e475d924-2126-39f4-9705-938b5ec45e47 | -2.19675 | -50.31319 | 2024-11-02 00:54:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4b449bb3-afff-3c3b-b41b-6552375a0192 | -2.16426 | -50.14682 | 2024-11-02 00:54:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a355acd9-2848-389f-b401-ccb5e351020a | -2.15521 | -50.14809 | 2024-11-02 00:54:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| b5f1ebdd-9495-3d41-a5ea-b176b83fdcbb | -2.15392 | -50.13884 | 2024-11-02 00:54:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c4b9135f-b3f9-3d3b-ab71-31a448abb1bf | -2.12678 | -50.14264 | 2024-11-02 00:54:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a6f4ad47-03db-3ef4-a300-59eaa204fa6d | -2.11773 | -50.14391 | 2024-11-02 00:54:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 0187f023-02db-38e9-92c1-4d5c341e507d | -2.07209 | -50.34613 | 2024-11-02 00:54:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d413d735-a2f7-3c0c-9b47-310d25e3a059 | -3.07153 | -49.57983 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7d72f4b7-439d-3c8b-b665-818f8382d47c | -3.07028 | -49.5708 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c1712787-cbe6-3c31-807b-b9fd4ba028ec | -3.04616 | -49.5282 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 19b67b13-01b3-3d80-8899-7219a6b2bdcb | -3.01382 | -49.63105 | 2024-11-02 00:54:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 87b7527e-315a-3961-8049-bd698798bda2 | -2.98982 | -49.524 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 35b5c2a6-283f-3723-9980-f7e129260c79 | -2.98857 | -49.515 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0b06837a-a81d-30f4-8911-228fc7eae389 | -2.93155 | -49.43153 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 3fc676fe-c8e9-3e38-a284-305bbf540c9e | -2.93031 | -49.42258 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| fe4d00f4-e5f1-3a93-8802-f81993329dd6 | -2.90423 | -49.50527 | 2024-11-02 00:54:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| ff111b24-1285-368e-8bf1-82c9b395c0b8 | -2.89531 | -49.50652 | 2024-11-02 00:54:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 89434860-8f4d-3533-9edd-66d6772282e7 | -2.89406 | -49.49754 | 2024-11-02 00:54:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 3f33e942-ec97-342b-a282-b8ad38c580c6 | -2.893 | -49.42461 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| b5925685-3eb2-3be8-9316-58dd77dd0b36 | -2.89175 | -49.41565 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 8893a8d7-91ff-331a-895d-634f036219d5 | -2.88514 | -49.4988 | 2024-11-02 00:54:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6ad89308-fe46-3e36-aa89-c395f9ec47f0 | -2.8841 | -49.42588 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3e6dde4a-a451-3b71-823f-a3d1e914e02b | -2.88285 | -49.41692 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ea72232f-eca2-334f-94b5-b495360518d4 | -2.88161 | -49.40797 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7d02f2dc-2709-35ed-9a89-1386c2e00c82 | -2.86133 | -49.39261 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| efa95f83-1f6e-34fe-b541-53158d38aa3d | -2.86009 | -49.38367 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 2c31e65b-d204-3ce5-a8a3-ddcbddc5c5f0 | -2.85985 | -49.4475 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f5219c24-5bd1-3628-9d80-94cbde068796 | -2.85861 | -49.43856 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8d25054b-cb8a-3e87-b57b-c846743ec797 | -2.85761 | -49.36582 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a88b8dc8-c938-3073-9fe8-5b055b9aec35 | -2.85342 | -49.46668 | 2024-11-02 00:54:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 325cc7cf-35b3-3dae-8df5-337344c89778 | -2.85243 | -49.39386 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| c6329974-9920-32ad-b61f-895e1e53e898 | -2.85218 | -49.45772 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f4bbd951-35cb-39df-abf8-59ed42c1f4fb | -2.85119 | -49.38492 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 732e4281-8830-310c-a815-9387fa37fb2d | -2.85094 | -49.44876 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 05c2a990-2ceb-3cfb-9008-c99074d4b1e8 | -2.84353 | -49.39513 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0a10eed8-b9a7-3fff-b8f4-db5215b34cc4 | -2.84229 | -49.38618 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| c4540ce6-08d9-3f1b-8eb4-8de44447b5eb | -2.84106 | -49.37724 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| a81cfabb-bb39-3c74-ad11-791a3f47b8d3 | -2.83982 | -49.36832 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4e754051-4f58-3ff4-91f1-2ce335b6469b | -2.8393 | -49.49609 | 2024-11-02 00:54:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| aeedd8eb-0404-306b-a94d-0032761f0256 | -2.78937 | -49.47287 | 2024-11-02 00:54:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a329b2a9-4502-3968-95e1-11f480aa56d5 | -2.78273 | -49.55615 | 2024-11-02 00:54:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 23e9d90d-098b-3809-a9eb-6bd75e109268 | -2.78046 | -49.47412 | 2024-11-02 00:54:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2e24d7d4-d7a4-3168-852c-abe4f0813ec4 | -2.77775 | -49.52021 | 2024-11-02 00:54:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d047aa80-514f-32a2-953f-f486d5e524a6 | -2.74729 | -49.49707 | 2024-11-02 00:54:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9b791c98-5a69-3fc0-b113-503593e61baf | -2.74632 | -49.42422 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 57d30924-2947-3775-a26a-8adc39d32347 | -2.74605 | -49.48811 | 2024-11-02 00:54:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e89e8c65-ba1b-39dc-a51a-ebbd2eb8216e | -2.74551 | -49.55807 | 2024-11-02 00:54:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 32ee651c-ed59-30aa-b4a3-fcf83dbd0889 | -2.93823 | -49.34856 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 74d1c0f5-9c39-3fe8-9ffc-c7aad298ff42 | -2.937 | -49.33966 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f755bc9a-116b-3ea1-94cc-6c35966704ef | -2.91289 | -49.03558 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f99b3e04-4cd1-3d83-969c-c13c7e8df34b | -2.89558 | -49.2366 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 28bf02c0-c705-3cc6-9a8a-0e880e279ca0 | -2.88078 | -49.27177 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 155fd37b-8734-3945-9e9a-4295a9c693c6 | -2.87954 | -49.26289 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ffc86923-ab12-3566-a5fc-8d8bcf1a587b | -2.87583 | -49.23623 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 18a03969-7514-34e1-9a02-88dfc94efc98 | -2.87066 | -49.26413 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 93aa1514-5c35-34c2-a541-77f9f03aba8b | -2.86695 | -49.23748 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d82bbf81-a6e8-32ef-b62a-c7f650894eab | -2.85808 | -49.23874 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1df4f7d0-87b8-312d-871a-94b10b19ef64 | -2.84403 | -49.26788 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8c268a7a-f186-32a0-bcf4-b34b2b026629 | -2.83515 | -49.26913 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d89e3285-b143-31a0-9a30-2d1e6d00739f | -2.82354 | -49.3161 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 7915292f-d069-3b0f-b794-86138cd8e168 | -2.82231 | -49.3072 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 62779561-5737-3a47-a213-0b7406014acc | -2.82013 | -49.22599 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 945d3fb2-5105-332e-ae57-32898f12bf73 | -2.81862 | -49.28053 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a8f617b6-bf5c-32cf-ad02-901cbbccadb6 | -2.81739 | -49.27163 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8971fb03-733f-30b6-9a88-f3a331eeae93 | -2.81589 | -49.32626 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| db957ba8-6403-3520-ba03-e02e92ea6683 | -2.80632 | -49.33394 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |


[Clique aqui para ver as próximas entradas](README15.md)
