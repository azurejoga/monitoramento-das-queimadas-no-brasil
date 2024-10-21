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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2816fc7a-1154-3a8d-b207-ca8d999aa5a4 | -12.50875 | -63.29311 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 480021ea-796e-39e7-9e39-fd468b0b22bb | -12.50766 | -63.30014 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b45236ee-b30a-3f6c-bbeb-1adf0e2ed57c | -12.50711 | -63.30365 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07881cdc-7a73-3be6-bb64-cacf18e0cb69 | -12.50656 | -63.30717 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57bd76a9-74fb-3415-aa8b-1e896a34c7d3 | -12.506 | -63.28906 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da873c36-ade2-35d0-b63c-377d472e65c3 | -12.50545 | -63.29258 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4e054c6-34a7-368d-8bee-e4be3fcc0b24 | -12.50489 | -63.18455 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2efef13d-b8ef-3e84-8bc3-5d10ccf79329 | -12.50435 | -63.29961 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c11796c8-82a5-32b2-a964-1665167325ab | -12.50434 | -63.18806 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5326d86-810a-322f-916e-e22a0a767a00 | -12.5038 | -63.30312 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 312db51b-96ec-3bab-8eaa-a1ecca7f187c | -12.50324 | -63.28501 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc068572-4f2b-3e56-8289-25feff57dee3 | -12.50269 | -63.28852 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5a9357a-ebac-3bd7-a72d-8182f815dce6 | -12.50214 | -63.29204 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a4f2b78-47ad-3bea-855e-29435dd33972 | -12.50105 | -63.29907 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29d3efc1-38ff-300b-a677-e7b251913ae3 | -12.50104 | -63.18753 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46467456-bf56-322a-ba61-00beafac9383 | -12.5005 | -63.30259 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aff8beb0-9968-395c-b839-613b4ff45cbd | -12.49994 | -63.28448 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46685078-85ea-3b8a-92cc-c05b9c3710a8 | -12.49939 | -63.28799 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 707c0c2d-d866-303d-a736-70b28aa92247 | -12.49884 | -63.29151 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3fa46801-7755-3093-8b7a-c209fa981369 | -12.49663 | -63.28394 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cc025e7-160f-38f1-9dfe-ef702b5417b1 | -12.49608 | -63.28746 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77460bfe-2c8b-3cf0-88b3-5cb43d737429 | -12.49333 | -63.28341 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 005fea3b-8641-3d9c-b219-de64380a9f2e | -12.49007 | -63.27943 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5444101-f4de-3e69-83d7-e347be6eaf95 | -12.48952 | -63.28295 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8230fe7-cc20-34ce-b0ad-95cbf591d86f | -12.48897 | -63.28647 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f8c085b-0b38-3b49-bd06-264fbe57c82c | -12.48781 | -63.1854 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 642d4cda-ffa4-3454-b0e7-7de7ec929441 | -12.48727 | -63.18892 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0968366a-82bf-3038-8cb4-d4b0da59cab3 | -12.48622 | -63.28242 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1a2493f-fd2a-3f8c-969d-a7cdb815e98b | -12.48567 | -63.28593 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75d04a6a-8820-3516-99c5-6a6adefa8409 | -12.48451 | -63.18487 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 51ea1e21-a628-3285-8d8e-68f55e179664 | -12.48396 | -63.18838 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 66d83e5e-effc-3e7e-af2a-111a05db5725 | -12.48341 | -63.1919 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5a386788-e9cb-3d91-956a-7bd890ea3ac2 | -12.4812 | -63.18434 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 278a17a1-c5f8-3df3-a76e-a667b9725a7c | -12.48065 | -63.18785 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e8937496-e882-3d82-b4e7-bb274b2850be | -12.48014 | -63.23458 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6619d7d-868a-3576-bfbf-5bb05f471cf8 | -12.48011 | -63.19137 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2a7e12d8-b11a-3fb2-8018-0d2e31541a87 | -12.47684 | -63.23405 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c57615bf-1c80-3d1a-85c9-ac2027e3e81b | -12.4768 | -63.19083 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5051812b-bcb9-3221-83c9-a8e3332ae95d | -12.47625 | -63.19435 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 02eae3d6-a76b-3f1f-9530-a1b8f4dffda0 | -12.4757 | -63.19787 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0a0ea527-39bb-339b-98ad-93431e0ba23f | -12.47519 | -63.24459 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc2aa62e-95ba-36f4-b738-43a6b8837e4a | -12.47188 | -63.24406 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b86e17b-9345-3a71-937a-ab30c1d20bf3 | -12.47133 | -63.24758 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18e1a7a5-2881-3dc6-b42b-0e3a73ce0045 | -12.18865 | -63.3383 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b14f1c06-bd90-3e73-a192-61832ecdd4e7 | -12.18315 | -63.33022 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b26661c5-9b3e-3085-a492-fc52739b905c | -9.34513 | -63.22461 | 2024-10-21 05:31:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37daf670-5df3-36d0-80de-a4b067826938 | -9.34159 | -63.22336 | 2024-10-21 05:31:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3a6a19f0-6633-3d12-b787-ac2f3d217238 | -9.06389 | -63.66425 | 2024-10-21 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 015097f8-1817-3027-8de1-c75020857ae5 | -9.06056 | -63.66372 | 2024-10-21 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e10e9427-e48a-3eec-b61d-6756a7331014 | -8.59287 | -63.8615 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 151a8a66-a371-3f73-a4a2-2f1643940951 | -8.58939 | -63.43896 | 2024-10-21 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 942d060e-368c-321e-9e45-dc9b35315a39 | -8.45646 | -64.05283 | 2024-10-21 05:31:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fe96cbe-77e2-3c92-acc5-9b5123d8bcd0 | -8.12531 | -63.87394 | 2024-10-21 05:31:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 092380ff-60c8-35fa-b0f3-bb13791e2ef1 | -8.12474 | -63.87753 | 2024-10-21 05:31:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18ec0078-ddf8-3148-9d37-271a99add8b9 | -10.10057 | -64.31239 | 2024-10-21 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6067e05-d029-3ca5-9122-c576bf1e5fc0 | -10.09999 | -64.31601 | 2024-10-21 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3b74a6f-a0f1-3b98-8b0e-20a017f11c1e | -10.02184 | -64.18886 | 2024-10-21 05:31:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4aebc32-cfe3-31cf-9944-7f41f88b939b | -12.34023 | -63.69448 | 2024-10-21 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3211f33-1824-3669-89e7-22bab8fa7300 | -12.21451 | -63.54036 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e940c5de-6f68-3a05-9c5a-be956603f34a | -12.01205 | -63.5077 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c5c59a1-683a-30e5-987f-90513b30237e | -12.01095 | -63.51471 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 025829a9-af12-3af3-8e3b-fa4931d19856 | -12.0082 | -63.51068 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62b9d75f-d973-3e03-ac22-a1b0108f3408 | -12.00765 | -63.51418 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27310d90-ecd5-33e3-bf35-aeff3a45fb1e | -12.00709 | -63.51769 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0ed3642-8711-3b3b-855b-440f40044a5e | -12.00434 | -63.51365 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e486c35b-a7b2-3134-accd-64aac6245db8 | -12.00379 | -63.51715 | 2024-10-21 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5634875-e0de-3da8-99cb-9dd02d4944b0 | -9.42076 | -64.32439 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6966c65-28d6-3997-936f-2bedbafe5cfc | -9.17133 | -65.44753 | 2024-10-21 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adf59b39-288a-3f83-be9a-26f0e5235725 | -9.03799 | -65.46349 | 2024-10-21 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e0f7348-f67e-3ac1-bd40-fbb19cb63c00 | -8.73179 | -64.1682 | 2024-10-21 05:31:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cf5689d-8180-3ea8-9cfd-de0b86380859 | -8.61981 | -64.16526 | 2024-10-21 05:31:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2c31d036-f898-324b-a601-7ee3e1b38d80 | -9.96339 | -64.87811 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5948735b-ed3a-3bcd-9453-cf3b75cde99f | -9.96278 | -64.88186 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef1475ab-790b-3303-9b6b-9499f6b2a640 | -9.95998 | -64.87756 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afb576a1-c923-3d5a-90a7-72617546f47d | -9.95949 | -64.77049 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd41f92c-b586-3b9b-ac25-6e53a79410ac | -9.95936 | -64.88129 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74f79987-c014-3996-a108-0a6e9227e745 | -9.87726 | -65.14822 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55c39993-7763-3c37-b20b-0872358068b1 | -9.87381 | -65.14765 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9874432e-6ba4-3acc-8c92-24c61926d9d4 | -9.81638 | -64.74371 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d6a4297-35d5-32ed-93d6-9bbbd5b4cf9b | -9.76714 | -64.72421 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0249e407-d222-33b1-bea2-e0222dda98d1 | -9.76653 | -64.72793 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae51a4bb-574e-3956-bc5f-01fd246ff1f5 | -9.76496 | -64.71622 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a313dc02-7f46-305d-ad95-531a5b4cea7d | -9.76435 | -64.71994 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4825ecf1-e18a-305f-b639-89bc214cf4b8 | -9.76374 | -64.72366 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af03fd7b-9db8-36c6-8ffb-ee5619d033e0 | -9.76313 | -64.72737 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 131d5d1e-b509-308f-8388-83f4d4ad2a99 | -9.76094 | -64.7194 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23f2c3f1-58b9-345f-9f3a-1ac5bb393a8e | -9.76033 | -64.72311 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7f4a211-eac6-3ba3-a952-330972216fea | -9.75972 | -64.72682 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 854935df-7d9c-3b13-8df6-890b3d0c371d | -9.75754 | -64.71883 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55cb8de6-6e1e-3817-b82a-e483ff06ff28 | -9.75693 | -64.72256 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0530e2e7-fc47-3b43-89d5-4746a3cbf2eb | -9.75642 | -64.72218 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d4e5bd8-e589-369e-8019-90bbe12cd049 | -9.68857 | -64.37937 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e94a9f2b-de92-30f9-bd4a-1747e8984594 | -9.6869 | -65.23224 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bba82286-3204-32f9-a612-5f5fbc55bec6 | -9.68626 | -65.23611 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3e70cab-4dba-3959-b3c6-4f1ddd3a1ec3 | -9.66056 | -65.74028 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58fd1ce4-760d-358c-823d-aa62014defce | -9.65539 | -64.95586 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e4c82f1-598b-3f56-9eff-942b0389127d | -9.57408 | -64.70028 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19d535da-2b19-367d-82f3-cddad4bbfc9d | -9.57068 | -64.69971 | 2024-10-21 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e61dd1f7-b496-3dca-9a50-5738f2c4e9d0 | -10.20834 | -64.84158 | 2024-10-21 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c112c441-a557-3c79-b6f3-02acde8d4e72 | -10.20554 | -64.83729 | 2024-10-21 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README58.md)
