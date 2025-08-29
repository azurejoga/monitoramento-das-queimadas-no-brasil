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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fc0c226-9662-3e94-a28e-755008b65a9a | -8.8944 | -69.43983 | 2025-08-29 05:29:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73409800-b77f-3944-a41d-9a5f194d1dd7 | -8.16961 | -61.37458 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| caa41a79-7238-3af8-ba77-98b8b8b79eb8 | -10.36596 | -57.81552 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b7d33e7c-a326-3d42-b366-df461b85dd1c | -9.0219 | -65.39002 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9bb92e37-a53b-3b8b-ad55-4bf5b6dbbf5c | -12.98198 | -54.75957 | 2025-08-29 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ac5dffd5-00a7-3bd8-86b9-051c58cb65b8 | -12.43032 | -63.91469 | 2025-08-29 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d273038-ebc5-37cb-8ed8-fc0b04ce8871 | -9.45496 | -60.56456 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9fa350fd-a78c-3792-ad46-2aa43f82e151 | -9.45974 | -60.31024 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df17194f-708a-3e89-9741-7c2a26e98a23 | -8.64888 | -69.57523 | 2025-08-29 05:29:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ee2a6e8b-2b26-3c2a-b501-db3b676ae170 | -9.02002 | -65.68673 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba9315a1-762b-370c-85e6-4fe86124dd30 | -9.8012 | -64.27284 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 972c3097-9249-3b98-b30d-f4e8e804aa9c | -7.47529 | -61.34075 | 2025-08-29 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5078e46d-9d21-3f1c-988f-529bd3ecaf75 | -9.11892 | -65.76917 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5ec7db61-f632-301a-99ae-e4713b2d4a90 | -8.58559 | -63.93272 | 2025-08-29 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cb9f63c-31d1-390c-b7a4-e7542202d6a6 | -11.23292 | -55.07111 | 2025-08-29 05:29:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e60a393-d514-30ea-8ef2-6d8af6ccdb50 | -11.70108 | -60.19513 | 2025-08-29 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d5ba3ad-eeb1-3427-b4a2-fd983b81ba01 | -9.77664 | -64.25399 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| eae91ef9-9b3c-3286-910a-967470f63b4c | -9.12047 | -65.78201 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d85a51b-0de0-3c65-9917-f545c1d5fbb7 | -9.16072 | -65.79593 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8aaab3e-e0b8-3c56-88e5-c141a9b9f8a3 | -10.46448 | -57.93782 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c6ec9d0b-a70e-36eb-b0b0-cb5c8671ab49 | -12.9369 | -56.97663 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c325cd03-c0d6-3596-8716-a61d79428222 | -12.43694 | -63.91578 | 2025-08-29 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61886f70-e984-3652-ae7b-816b645ff574 | -10.46855 | -57.93836 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8c73210c-57ec-300a-ac43-3b9c797a2735 | -10.03232 | -59.35899 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5566e84d-e926-3fb9-906e-22bd723d1b59 | -9.76876 | -64.2601 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 93ee3630-54f5-350b-afc2-cf705a50f545 | -12.43251 | -63.92229 | 2025-08-29 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1de862bc-7bb4-3e1a-9774-b4cfa4aaadfc | -10.25303 | -64.49838 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bc74097a-b051-3dd1-b732-ecf98fc25c5c | -7.47584 | -61.3372 | 2025-08-29 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8edb6e99-e82d-3de2-8c08-4132a03e906a | -9.45901 | -60.56122 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19b9ec8e-f2f4-36c3-8540-84d8298a2ad8 | -10.36739 | -57.83451 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2efa697a-7e94-3e0c-9903-5a2cdef264f2 | -9.13071 | -65.80907 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e909ceed-b6ce-3d5c-95f4-e12022689948 | -10.31506 | -62.61916 | 2025-08-29 05:29:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f884591-0edf-3ad4-98cb-fd3d9364021d | -9.02358 | -65.68734 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eef3a948-f9c9-3cc0-b9ad-33a37db27886 | -10.48615 | -57.96267 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e3f2292-acaf-396d-8d12-cc06b79acf3b | -11.38176 | -63.26429 | 2025-08-29 05:29:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e98299a-9be7-3b79-a764-57c08f27a82a | -12.9967 | -56.9212 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f42dba6c-e80b-3a8d-b2df-4a9a76c74332 | -9.53375 | -65.69221 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a98cb6ac-3120-3a6d-a4d4-9bde3656575b | -8.58224 | -63.93217 | 2025-08-29 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b5eb733-599f-3906-9b47-faf1b77468ff | -10.94006 | -63.63087 | 2025-08-29 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21b236dd-436f-3870-af0d-edb4d028d6db | -9.19854 | -59.54348 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d17c972-469f-3a88-a91a-fcf58f9c2ea6 | -9.11757 | -65.77732 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e252995e-a5a5-36da-ab08-3c713338a7bf | -10.31818 | -62.6196 | 2025-08-29 05:29:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f892dd0-dac0-3b54-8fe4-adb4d4412895 | -9.47232 | -62.38519 | 2025-08-29 05:29:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c31dd5c-a66e-3cb0-8d08-4f292b5ee8d7 | -9.24502 | -65.89821 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8093a0d9-8b83-3197-9e96-9a2daf0aa0ac | -9.17388 | -60.785 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d1601de-a0cf-3da6-b7e6-e975d0deaad7 | -10.45765 | -59.12286 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 97ce68ec-54bd-3847-9437-4ae16e03adf2 | -10.46501 | -57.93416 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de7ff64d-b29f-3f3f-85b9-b3ebed767957 | -9.01223 | -65.68958 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d25c6f2-12bc-3095-8d08-60eb6062ebb1 | -9.77839 | -64.24317 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3f044d62-fb19-3cad-8bb6-820c76663a64 | -9.31089 | -57.70334 | 2025-08-29 05:29:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 290f9544-08f7-356d-a1d9-86c1b2e81cfc | -9.05253 | -65.73418 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 783f823f-e61f-305f-a115-5c6ac628fef3 | -8.95331 | -65.95599 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81388267-f070-3e6f-baa0-774d91097d79 | -10.36451 | -57.79651 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63d2a78b-b301-3e2a-b89f-6b4d67825474 | -9.10226 | -65.73685 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72ad01e5-e582-3bf4-b4aa-f79d347ca024 | -9.72968 | -64.91061 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 693ce3eb-26ab-30c8-853f-7937bbf5abb6 | -8.77162 | -70.57732 | 2025-08-29 05:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8089e444-e315-3d2c-b2da-bc13cd950844 | -8.95401 | -65.9518 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 154f4400-1237-39c0-a616-ee444f4081d2 | -10.37558 | -57.8314 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8c61b8b2-cc81-3179-9751-6ddcc05498e2 | -8.9526 | -65.96022 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a9ac792-07af-36f5-a88b-cde923feb981 | -7.5701 | -63.86186 | 2025-08-29 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f54577cb-4319-39eb-a255-c4e93cb346a5 | -9.18284 | -65.79545 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79b0e474-4f48-3b77-8e68-2a2c493927e6 | -8.18078 | -61.369 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4233f7f4-c96d-3e68-9afc-8d3c8c3e0c3d | -10.47742 | -57.93601 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88fd03e2-42d6-319d-800b-02b738f45e9c | -9.54791 | -65.69458 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86f0f26f-9a4c-3f8b-a2f5-166f110b92b3 | -10.31451 | -62.62267 | 2025-08-29 05:29:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49e295bd-db86-3032-9d30-9fcc5c3a3d91 | -8.24958 | -61.44939 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 20c12854-0c7f-3de7-8608-9be4cfdd2635 | -9.0332 | -61.22618 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2661a2ef-615e-3e22-a815-84015d77bd4b | -10.46889 | -57.96788 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cac4407f-d7fd-3643-9333-1bb261db67f0 | -9.16498 | -65.79243 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5f183d1-c0ea-3896-99b7-8895c4c588f8 | -9.80717 | -61.20015 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dae2e7eb-577b-34f3-9744-deabe6b386da | -9.15395 | -65.77925 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 58dcd0ca-d19a-347f-9c06-87c00ac9cb74 | -9.77942 | -64.25816 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3993f3dc-f661-334a-a6b9-6597a2aa71cb | -10.46094 | -57.93362 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ff90c231-3bd3-3367-9fa1-b5093cf8c92d | -9.53662 | -65.69684 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 80818856-d109-3994-b420-1978e5daac83 | -9.21706 | -60.86839 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 047df611-f795-3335-96fa-a676ee083b4d | -9.18335 | -60.85938 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38acce30-f915-3cd6-a363-e83b18704d22 | -9.15663 | -59.57639 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1a4fb8dc-abc0-3854-b7d1-6bc5041b297d | -13.00121 | -56.92184 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1c501a0-edf7-38d4-b0c7-6cdbaf6d0484 | -9.10839 | -65.78844 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9144e2b8-563d-3d5c-a1a6-01a40eec02b1 | -9.11111 | -65.772 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| fdc1dce8-7c0d-38c3-a990-254f0e795e35 | -8.9353 | -64.16253 | 2025-08-29 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 22c0a5f0-fa46-3b3d-b043-f2c09f0ec85e | -8.90142 | -60.54614 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef69d178-c622-39c6-87b6-3d41603af427 | -8.93193 | -64.16198 | 2025-08-29 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7dfd68e-9fbb-3fa9-a59e-b6e0e50caf60 | -13.00751 | -56.90859 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ad5216d9-07fa-31f8-b41c-b29eb852f60a | -9.10686 | -65.77551 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 611ed141-a93e-3412-811e-d639fe165297 | -9.11043 | -65.7761 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 27f61ca5-9997-3756-8eb0-98faeb6852b8 | -12.9922 | -56.92051 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6bc3d7fd-b8b4-3d8f-aabc-1622e809c3a1 | -13.01473 | -56.92375 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 568b2cb7-83dd-3cd0-a6e1-e534721e60ea | -13.0006 | -56.92654 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e4f1fecc-6097-3a6d-80a4-76f0d07781f3 | -10.36701 | -57.80815 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6f4b158b-9367-34bd-b2f4-095357696559 | -9.58984 | -66.16296 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1c15828-a4a6-3e40-91e0-2d18d618916e | -9.10939 | -65.73804 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e06b127a-26ab-3fd6-8a2d-b8d4642efc3e | -8.88005 | -62.48059 | 2025-08-29 05:29:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4087ad2-cbed-37a5-90ad-629d393bf3b0 | -8.18023 | -61.37258 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8f28f9ad-7c13-329e-b05c-287ac60d3a04 | -7.5289 | -70.11691 | 2025-08-29 05:29:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ae912a6-0bf6-3655-bc60-07593cb53e17 | -9.44973 | -60.55198 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 33705040-e876-3e3c-9e85-04abd667c7e2 | -9.14958 | -59.56762 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 90ad3b78-2b29-3f3d-930e-674ae00d7c56 | -12.9928 | -56.91584 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 14bcc9e3-0fe5-3571-9e71-4c4e7380c14d | -8.24903 | -61.45297 | 2025-08-29 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4d29d47-1eac-3f46-8c51-6950407754cb | -9.52401 | -60.50775 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README81.md)
