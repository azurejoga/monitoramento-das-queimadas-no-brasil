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

## Dados Diários - Página 167

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2993b8f6-f126-3d84-aae7-872ce11b089d | -12.86231 | -62.4612 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee3d2e66-1dda-3f9e-a611-11a94cd804ee | -12.86168 | -62.46504 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a40b99df-5917-3fd4-ae2a-d0a5e3ba0e8b | -12.85824 | -62.46444 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88c13381-fe15-3cb3-850f-137c95067c93 | -12.8548 | -62.46385 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ddd1eee-1f7e-328c-8ce7-8c793b2386ab | -12.84882 | -62.47861 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 616ed2c3-937f-306d-8df0-aa286527c31b | -12.83442 | -62.48008 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c4af0345-f171-30f4-8919-afa704d1233e | -12.83379 | -62.48393 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1f44ab25-d169-3a67-886f-59e512395a45 | -12.83098 | -62.4795 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e5b695a-f834-3c45-9faa-6b154a2a1288 | -12.82346 | -62.48216 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac331d35-78b9-3ff9-a8ff-9b801993a05d | -12.81593 | -62.48482 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 749ac3d8-dbab-3a8d-98cb-a19f338e8b08 | -12.81529 | -62.48866 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9888d7b8-7110-3cc1-8a99-e753b771bf46 | -12.80175 | -62.50611 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 10c29623-5b2d-3670-965e-7e35f472e9bc | -12.79831 | -62.50551 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 455d5314-957c-30ea-9f26-ed8ff9e892f9 | -12.79486 | -62.50491 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 17.2 |
| d8c94658-1f86-3e51-989b-34cf0668bc0e | -12.78896 | -62.50465 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 13.4 |
| fbbbfc3e-d106-33f3-be79-a090fa508b17 | -12.99824 | -62.71819 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 75259ed2-de81-34ff-a0a6-2062d58a2f4a | -12.98895 | -62.68849 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d246516-e9e7-39a1-8b04-bbbc58f0442f | -12.98856 | -62.64843 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 7cb172c3-20b9-39d2-aeda-04533c5e67ce | -12.9871 | -62.64505 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 63608063-9c4c-3f97-98ae-b6db625a3063 | -12.98549 | -62.68789 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59754a5f-5611-3d52-9b3c-aa78ec23bf88 | -12.98503 | -62.71187 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e650dcf5-ec26-3b89-bd39-0b290d2bfb7d | -12.98428 | -62.64057 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5333f100-be07-33b7-9505-3a85255787a8 | -12.98203 | -62.68729 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d17415b-6d9e-3bbc-ab6f-2a7282460f77 | -12.98137 | -62.69118 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d86a408b-15d9-3f72-8be7-4c7731a8e223 | -12.98072 | -62.69508 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 750a5b41-271b-33cb-a142-00b86b2633ae | -12.98018 | -62.64385 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3106864e-f62f-3374-8e4f-dbca5c04db1a | -12.97882 | -62.69565 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf0dc691-bc6a-374d-b546-14126c786121 | -12.97875 | -62.70677 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fadfc4b0-b7bb-3ac3-9274-09499b3e7858 | -12.97754 | -62.70345 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 39f1ad42-4f09-3acc-8e3c-4b8b77a0bb7a | -12.97725 | -62.69448 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7414382e-6583-3129-a6ec-525fdaf32c74 | -12.9769 | -62.70736 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3efc0980-ba66-3fe6-ab3a-4fd165b39921 | -12.97626 | -62.71127 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1bc6fb7-53af-3a45-909d-974df1dfbd04 | -12.97529 | -62.70617 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60b99f86-6556-3ebe-8429-caa09ee9f478 | -12.95905 | -62.66417 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f137416c-876c-3a00-970f-df722d54aaf8 | -12.95751 | -62.65191 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 19a7aea0-bb14-32fb-94b4-c5d7568d0004 | -12.91471 | -62.71668 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e0fce66c-8cd2-342d-bc0e-ce5db6ed9d09 | -12.91189 | -62.71217 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 1bc40e87-4c7c-3aa1-b0af-07f1f3382fad | -12.90908 | -62.70767 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce23efd0-cd71-3f9e-be94-66cfdbdbe196 | -12.90626 | -62.70317 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fb963c25-568a-37e6-aa25-f88b392d52b1 | -12.90344 | -62.69866 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 23d45e0c-94be-357c-8ae5-2b3d01e0b29a | -12.90279 | -62.70256 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| daf6e763-55d1-39cf-9e2d-f99e7efe37e9 | -12.89571 | -62.53819 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 708e3fff-dac6-364a-a30d-f006a04adfcc | -12.89508 | -62.54205 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 6a476ffa-1416-3f27-b2e6-64e8764dc040 | -12.89481 | -62.53757 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e4c33f2-7299-3ceb-81c2-7702a80618f7 | -12.89437 | -62.625 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f03d43a8-5ed9-350e-bb5f-c6808ad5659b | -12.89416 | -62.54142 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 4b816be7-8e4e-342a-9e88-a884c7c72988 | -12.89307 | -62.63277 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 02daafb1-0c7b-336d-af03-69047391ca93 | -12.88957 | -62.69626 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80ab1ce3-b8df-3322-9667-a4802e0c8749 | -12.88755 | -62.54471 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d9e8ba1b-ea8a-33aa-9a47-00d2dbf95e4d | -12.88692 | -62.54857 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 18e12d7d-7239-38b8-a218-e96e3c450150 | -12.88629 | -62.55244 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 20be5e7c-4cf6-3356-8d4d-b98d40339767 | -12.87626 | -62.75435 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be2f8d8e-a4db-360f-9820-ee046b0da113 | -12.78833 | -62.50852 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05e1f0fa-22bc-3e16-9aaf-9e5a34976bc7 | -12.78489 | -62.50791 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9130638-4668-3721-acf4-28a319504ddb | -12.78426 | -62.51178 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c7cc672-fc43-3d2b-8175-d125fc335d1a | -12.76982 | -62.76072 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2be50e6-c0e6-310b-ad4d-e6f34c761054 | -12.7622 | -62.76344 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8416aec8-01a2-341e-8471-dcac15928768 | -12.47343 | -62.68809 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4cf6882-9e13-3fcf-894b-ee02a5d569e7 | -12.47278 | -62.69201 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3314833-b338-3515-a179-378bd5239a21 | -12.46969 | -62.73201 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 516dc56f-27eb-3104-bea4-80575f83fedd | -12.45593 | -62.74993 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ccfc6de4-4294-3871-b0a9-8868e80e98c9 | -12.44961 | -62.7448 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52b5ef18-3bc1-31f7-8df7-88b8a746a49c | -12.81188 | -63.00535 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75cf249d-e641-3007-bd4e-696988c60b00 | -12.8077 | -63.00875 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5108fdbd-9446-399d-8651-549d51f2a1e7 | -12.70899 | -63.07876 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e626ef87-d3db-3963-89a2-beb1bace1abb | -12.70546 | -63.07814 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fa25edc7-2af3-374d-9e43-5e0aeb1138a9 | -12.68232 | -63.08783 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6bd887b-1c1a-3ae7-8481-86053cec6236 | -12.67811 | -63.09128 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68c61272-b940-329b-8023-8dd62e8a7c9a | -12.67458 | -63.09065 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9b484623-9ae3-3cbd-948a-bbaf1fc230f5 | -12.65706 | -63.10851 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5f782d1-48e7-3376-801f-9bcd6cc108ad | -12.65488 | -63.09975 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c4659663-1f6c-339e-a581-aa04797d9fc2 | -12.65352 | -63.10789 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4add5f92-3939-3c53-8b9a-e1ecc022a6fe | -12.65285 | -63.11196 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0856108f-7279-36dc-b418-b6efed3a0dc9 | -12.65135 | -63.09912 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b36a266-bce1-35de-a19b-1129af12cfe3 | -12.65067 | -63.1032 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22c70e77-da60-31fb-bce6-096aa3f6c008 | -12.64999 | -63.10727 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8899ddac-64c7-3747-a0cc-d765ff8091c5 | -12.64931 | -63.11134 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fc5582d-f7af-3fda-a7fc-bf457b53b47a | -12.64863 | -63.11541 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a936073-988c-3f99-9c9f-69e959c37528 | -12.64713 | -63.10258 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a269047d-1149-32f2-9d77-8f3a38508338 | -12.64645 | -63.10664 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b7308ae-94a0-3e7c-9509-a70da948126a | -12.64577 | -63.11072 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86a23311-4ec0-3d5a-a7fb-bd0a726af682 | -12.64522 | -63.13582 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 912792d0-4e3a-3403-adf1-4a2c6afc1eb8 | -12.64509 | -63.11479 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1d932fb-a74e-3fe5-88b1-eb2b617f215a | -12.64441 | -63.11887 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9621639-b621-3148-840e-f3b53e09db7c | -12.64292 | -63.10602 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cebe1db5-a64e-3e3f-b85a-9c2c35a4643e | -12.64236 | -63.13111 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 92edf8d2-104e-3c12-acbd-97c795f83adf | -12.64224 | -63.1101 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3ac10980-a9f8-33dd-a34f-b8a15dcb5842 | -12.64168 | -63.1352 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 176c0aa9-dc38-3f6e-a899-1049bdb63129 | -12.64155 | -63.11417 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7cebd3a6-181f-3134-af32-cf3a9c702642 | -12.64087 | -63.11825 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 710dd65f-aaca-37a7-8f9e-46021158623e | -12.64019 | -63.12233 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 8606d614-2dc8-3657-a878-5ec604d460c1 | -12.63951 | -63.12641 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 19de5e78-cb0c-3f59-b87f-db6b6205a255 | -12.63802 | -63.11355 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a53dab46-ac8d-388f-9741-0db096d1d1b0 | -12.63733 | -63.11763 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 040c83ee-8dc7-32cf-b950-01f53970cd11 | -12.63689 | -63.16381 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38d220a2-0920-38a2-be92-b88161832269 | -12.63665 | -63.12171 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 7c8fdb08-c80e-3aaf-a6f7-5e42c7d38d56 | -12.63597 | -63.12579 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 851fa75a-550c-32fa-b318-cd86c3b61342 | -12.63311 | -63.12109 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9824140e-89c3-3501-ab5e-564e14628a31 | -12.63243 | -63.12517 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f150cb65-b18d-3b3f-a5b1-efa81e16fde9 | -12.63174 | -63.12925 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README168.md)
