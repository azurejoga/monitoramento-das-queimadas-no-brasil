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

## Dados Diários - Página 153

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84c06ee7-4289-3fa1-9653-4ea884eee9e1 | -9.42117 | -67.23999 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1baa04d1-a793-3a84-8c26-c307c827edc6 | -9.98568 | -66.87437 | 2024-10-03 05:16:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3737ad73-3a20-3e2a-99c9-0ccd88318c9a | -9.98278 | -66.87104 | 2024-10-03 05:16:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 332c76be-6cce-3b46-a816-8c7dcb643e7d | -9.98193 | -66.87592 | 2024-10-03 05:16:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e4d51d14-2017-3c51-a781-8bb64340d4e3 | -9.98105 | -66.87353 | 2024-10-03 05:16:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 57320b66-8939-3563-9e07-d05ec07f2c55 | -9.95943 | -66.96576 | 2024-10-03 05:16:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aaac45b7-c6ef-3ea4-bc01-73d286a9f51c | -9.92278 | -66.77955 | 2024-10-03 05:16:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e66c194-ca65-386f-821e-e1bfeb9d7621 | -9.92075 | -66.84405 | 2024-10-03 05:16:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b51a9a48-ed81-336d-9244-e9bf3e495d5b | -9.91613 | -66.84322 | 2024-10-03 05:16:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e11dc47-78de-3b24-9b0b-0867b3169dc1 | -9.90142 | -67.33646 | 2024-10-03 05:16:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 63ceab88-d61f-36fa-9df4-ed56a3ac0696 | -9.90086 | -67.33885 | 2024-10-03 05:16:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 662b5995-14ae-334a-be70-ee57f16febed | -9.90049 | -67.34177 | 2024-10-03 05:16:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bae27f2d-949e-3ecc-afc8-a255df11b01f | -9.89664 | -67.33557 | 2024-10-03 05:16:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6a754c65-32e1-3477-ac58-539a1d1f787c | -9.89608 | -67.33795 | 2024-10-03 05:16:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 15fa8313-1293-390e-b472-ec9f0208cdb3 | -9.89571 | -67.34086 | 2024-10-03 05:16:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7b0e54c7-a8b1-3cf5-81fe-23e6e6c5f451 | -9.89511 | -67.34324 | 2024-10-03 05:16:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 08082ddf-f189-39cd-bc86-55696f7e1a61 | -9.89186 | -67.33469 | 2024-10-03 05:16:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18dc8e69-2e74-34ef-b58b-4594e29f2466 | -9.8913 | -67.33708 | 2024-10-03 05:16:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c4c120d-f6ed-3501-aa43-f57784bac9c1 | -9.89094 | -67.33997 | 2024-10-03 05:16:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47bf6ccd-a468-3496-b277-18b552001ebb | -9.89033 | -67.34235 | 2024-10-03 05:16:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ea4b73ab-3f73-3380-a76f-f5ef49570deb | -9.88616 | -67.33907 | 2024-10-03 05:16:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d1fe941-46ab-3d3e-b931-d4b93171fb68 | -9.88556 | -67.34147 | 2024-10-03 05:16:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de12de81-6801-3b2d-9c39-d3e76e05fe4a | -9.88523 | -67.34435 | 2024-10-03 05:16:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6820e78f-7422-38fc-b768-b4d483d89ba6 | -9.88458 | -67.34674 | 2024-10-03 05:16:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f57b4266-10f5-36a8-bcdd-ff1a9d656b4e | -9.88138 | -67.33819 | 2024-10-03 05:16:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a60a9fa6-d00b-3a78-914c-a6c50a4e2465 | -9.88078 | -67.3406 | 2024-10-03 05:16:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f39b7ce-7cc5-3539-818d-853a8d885b18 | -9.88045 | -67.34346 | 2024-10-03 05:16:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa68626c-2c10-36fc-b2c4-0b873c7f0d85 | -9.75705 | -66.84087 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06979e3a-e060-3744-afa1-8fdc6b28d6fc | -9.75539 | -66.84202 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df5d9aa5-7c31-3f92-85ff-60b3ef1f4e66 | -9.75242 | -66.84002 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78c5b9d5-cb51-3d29-a0c1-8d07193919c1 | -9.75076 | -66.84119 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8dd9ab9c-d49b-393a-bb4c-fb0df6f659f5 | -9.6395 | -66.81215 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6200c9e4-5384-3089-8456-6d2051c916a4 | -9.63487 | -66.81129 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ec3283d-0d9d-3628-ade1-734a490db6eb | -7.37401 | -68.01472 | 2024-10-03 05:16:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24d8b6ab-02a9-31c4-b389-6a2fc943b161 | -7.37344 | -68.01797 | 2024-10-03 05:16:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a49bd89e-6620-3018-bb75-1ee838d89188 | -7.3723 | -68.02448 | 2024-10-03 05:16:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d6de75b-1421-3f5a-aaa1-d88b943d849c | -7.36878 | -68.01383 | 2024-10-03 05:16:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 913182d9-e1c4-391e-8048-59c68b013a88 | -7.36821 | -68.01707 | 2024-10-03 05:16:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67030795-0c23-3f1b-bcdf-28188509bbd3 | -7.36764 | -68.0203 | 2024-10-03 05:16:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fceff7e-8ab9-308c-a82f-727beffccd9c | -7.70993 | -67.12277 | 2024-10-03 05:16:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f00191b-fc6d-314d-9627-3d2ec80886cd | -7.64397 | -67.20102 | 2024-10-03 05:16:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 70086253-f599-3eaf-b672-a398813ca701 | -7.64125 | -67.19594 | 2024-10-03 05:16:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 50aa97d1-d390-33be-b4da-da416fb81765 | -7.64024 | -67.20153 | 2024-10-03 05:16:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2a16a2ce-7700-3dd8-9741-2f391b1a30d7 | -7.63923 | -67.20712 | 2024-10-03 05:16:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5f46d3c3-0386-3170-be22-c5ff136d8623 | -7.63905 | -67.2001 | 2024-10-03 05:16:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9e3a139d-9272-3585-bf89-33b87964e9a9 | -7.63809 | -67.20571 | 2024-10-03 05:16:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a076f11e-0b97-3eb1-891e-8276a5641b2a | -7.63532 | -67.20062 | 2024-10-03 05:16:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3e308520-6cc5-33f0-b0ba-4cffecda405b | -7.63432 | -67.20621 | 2024-10-03 05:16:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6da83156-3bd9-32cc-800d-3cce9dd8a139 | -7.63414 | -67.19919 | 2024-10-03 05:16:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b9b0e208-29cc-3b68-a4f7-f7491e6209f6 | -7.63317 | -67.20478 | 2024-10-03 05:16:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 45d7daa8-3d83-30fc-a003-41e6284b684b | -7.6322 | -67.21039 | 2024-10-03 05:16:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9eeae977-ce11-30fa-9a26-1b14b8fdc173 | -7.6294 | -67.20528 | 2024-10-03 05:16:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9685827a-6f11-3862-8c49-4aec973eabeb | -9.42122 | -67.6173 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2adf39a8-3c70-3fa0-94d0-7a1dbad44ca0 | -9.42021 | -67.62279 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 45efd0db-3c0a-3b4b-8794-c0e0edc7d0cf | -9.41879 | -67.62061 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ed5f06c5-1d5d-384f-ab02-ed0d31b16003 | -9.4153 | -67.62189 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec62a67c-aeba-36e4-b475-b770b0a9483f | -9.38035 | -67.84 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a99bec90-27e3-3188-b1cb-a9922ac55848 | -9.37981 | -67.84293 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab9f58ae-3279-35ee-9d14-d9c6b3825200 | -9.3759 | -67.83615 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8657bce-e099-3ae1-b705-af5306d9fe58 | -9.37537 | -67.83907 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 890cf427-2445-32a3-bbc7-4164cdd1ca78 | -9.35761 | -67.39924 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0822a34c-0296-3552-8708-17bc1de0d97b | -9.28504 | -67.85309 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bbef3ac9-fb30-3380-953c-429365ef90bb | -9.28479 | -67.82624 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3e2ba52-cb56-322e-953e-19cd354f868e | -9.28373 | -67.83202 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ae1ba8d-e3d9-31cf-ac40-2b044b6e0114 | -9.2832 | -67.83492 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6fb61420-6a1b-39e3-b3ec-cc663adee273 | -9.28111 | -67.84634 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f38836d8-ebf5-3cc2-bb5b-c332955a3e31 | -9.28058 | -67.8492 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10359fa8-5af7-3f74-a52d-dfb842e39c4e | -9.27823 | -67.83385 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63de009f-498c-31cb-aedc-a347dada54ee | -9.27041 | -67.82024 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef2d916b-0aef-3002-9eb0-309c0d8abcda | -9.26573 | -67.81847 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69d29a90-222e-3b6c-86b9-b2ac774659a5 | -9.26542 | -67.81933 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdc53882-e5d8-3668-a01f-a159569e2375 | -9.26522 | -67.82137 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c63ec759-b2ba-3f29-bf94-65fa70e2cff4 | -9.26427 | -67.59631 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b5d89c1-c568-3242-bf91-314b1cc69bf5 | -9.25972 | -67.82334 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b40d4606-0193-3d54-b98c-f274fc7c6eef | -9.25935 | -67.59541 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 732aacba-7dd9-3c87-b5fe-890ea82e5b95 | -9.25421 | -67.82531 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3043e41-4800-3791-9526-b442b977fd7a | -9.25384 | -67.82617 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b689b1ea-0da9-3db7-a691-4619f3a35962 | -9.22427 | -67.81968 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4ca8284-80a0-3e14-9539-3afe15d250b3 | -9.19694 | -67.85667 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 905ec1e9-267b-3dbd-a074-23a285de7f01 | -9.19246 | -67.85282 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 251dd937-eea6-3e48-b91c-c32e7c49bfd0 | -9.19193 | -67.85575 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72f1f172-8809-36a5-90c6-30d5dfab999f | -9.18745 | -67.85192 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c0161f6-92c2-3ce7-b9af-7803b9f22e1f | -9.09931 | -67.50629 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5cb50bc8-3acd-3b28-a1f9-4e57aa4b1cc1 | -9.09915 | -67.51746 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ad5daddf-1473-3127-84a6-710fd08c1fe4 | -9.09629 | -67.50547 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cd9a1ce0-2532-335d-bc55-af635c3637f7 | -9.09528 | -67.51099 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bc5a6277-6e35-3d4b-af45-f39b2421ead5 | -9.09246 | -67.51645 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0b85e17e-775c-3e9c-a9e6-be5d87bbd3e1 | -9.08935 | -67.51565 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 281c670a-8c5e-31e0-b3be-8bd0a8c8848e | -9.08297 | -67.57789 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3d3a48be-f048-3268-bbc9-74563e7b02ae | -9.08052 | -67.67132 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aaa6842d-8e9d-3144-a020-be2dcc022e92 | -9.07805 | -67.57697 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a16f8a24-625c-311b-95a1-7f665c3e73a2 | -9.07557 | -67.6704 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ca58580a-4e28-37d0-8eff-d95db2844487 | -9.05092 | -67.86433 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc4e0b9b-974a-3fd0-a250-d57746788d66 | -9.04536 | -67.86636 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| d793a823-d875-328d-b69f-3279a4b3e278 | -9.04482 | -67.86931 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 9f7ae269-7d30-3045-9846-e4f23b584ab4 | -9.04428 | -67.87224 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1151c7d3-4d41-3f9d-b0cb-05641972b7ea | -9.03953 | -67.50089 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e9ed0f2-8503-34e7-9fb7-b0e2ae18222c | -9.01708 | -67.38641 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67480a92-8062-3506-a152-f8ee2c6f0b66 | -9.0163 | -67.74406 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| d5b02c02-1765-3d73-ab1a-39d4b21a19ff | -9.01222 | -67.38548 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README154.md)
