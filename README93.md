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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b695b98-448e-3fa0-8047-2c04cb3302b9 | -10.68312 | -50.9769 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6add667c-0c33-33d9-a1ea-6870c7a6bc25 | -10.68256 | -50.98041 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20cc8410-73a7-3acd-a2bd-9e5a815ae9f0 | -10.54987 | -50.93742 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d5311cf-0ef5-3278-b099-24e20ba62677 | -10.54931 | -50.94093 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cc07dcf-fc4d-3af4-b052-beb1f7e68ddf | -10.48855 | -50.83044 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7eae7414-bf02-337c-aebe-1bc704d3c1f4 | -10.48799 | -50.83394 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b404bf7-7e7d-3423-af1a-ea7c0186cd0c | -10.48249 | -50.82587 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be14a527-fc31-3a80-b904-19cdd7ca6da8 | -10.47918 | -50.82533 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad4e124b-63af-38e1-9d2d-c341d87c9293 | -10.47587 | -50.8248 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 31f403ac-3b1a-3c59-8544-e65a71e427bf | -10.47313 | -50.82077 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ca733b6-3967-3e2c-a2f6-696170ebd403 | -10.47265 | -50.75968 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a90b657f-151a-3f4f-9269-14ddf85b3e8e | -10.47257 | -50.82428 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f42f3a5e-c305-322a-874f-a455c4fb1be1 | -10.471 | -50.74869 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93b5fec9-4ff0-398e-816b-96e48edb98cd | -10.4699 | -50.75566 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 116c2a37-6513-379b-b799-143a7a66d696 | -10.46935 | -50.75915 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f48bfb7a-4fd0-3e2a-8a0c-12c46e8ff6a7 | -10.46763 | -50.8127 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4031ae49-5823-35da-b309-5339996da10b | -10.46707 | -50.8162 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b89fc295-ca55-3318-a0d1-91448affacd2 | -10.46651 | -50.81971 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77859925-2c3d-386c-a93c-50e8728fa5f9 | -10.46543 | -50.80518 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bba8b63a-097a-35b5-a2eb-df4ecaa29fb8 | -10.46493 | -50.76562 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 04ee1de0-6bf9-30be-9e71-4875cee1874e | -10.46487 | -50.80868 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8beb88c9-a0fa-380a-815e-e914aaedb17f | -10.46432 | -50.81218 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2dc8f148-7a15-3ddb-bcdb-86d17878b7dd | -10.46376 | -50.81568 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7b7bdb7-ea7b-35fc-a46d-fb032842e3e1 | -10.46267 | -50.80116 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c943ba4e-e51e-3ef1-b87b-414372e7adea | -10.46051 | -50.7721 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09c72b11-0d8e-3803-89c4-72e994cc512f | -10.45995 | -50.7756 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75483598-cf4d-3bfc-a3ec-f76c22f028f0 | -10.45992 | -50.79713 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e81de595-8fb2-3430-b6f0-8f0a9983293a | -10.4594 | -50.7791 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71b7c7e5-1dae-328e-8a39-308bd6427154 | -10.45773 | -50.7896 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 305261b9-0f3b-3493-b070-0e80598d6ffb | -10.45498 | -50.78557 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2b156ffe-a197-3241-aa24-954bb7fdcab9 | -10.87422 | -51.10223 | 2024-09-27 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f7109d0-d13b-38d9-a677-f07760993cf1 | -10.62254 | -51.12226 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dffee186-940c-3dba-8546-2ec15efbcaab | -10.62197 | -51.12578 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40f5f029-1421-3ed4-944c-e650a2160ed0 | -10.62141 | -51.12931 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10a92a8a-08e2-3b42-b820-991e8ca39a48 | -10.62084 | -51.13284 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 669e2f75-52c5-305b-a9d2-92a99b9d85fc | -10.62035 | -51.11467 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2a774f6-ce55-3739-9e76-784f8c5d20ec | -10.61978 | -51.11819 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e1a87b8-7ea0-38ce-b64d-4e2155f101ea | -10.61922 | -51.12172 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9648b9f2-d282-3391-be3b-4db6d8376198 | -10.61865 | -51.12525 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c3ab08c-5b9d-389a-ad6a-651fc7614eed | -10.61747 | -51.11069 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 05e34e0c-6472-3b19-8dba-312db2f28204 | -10.61692 | -51.11422 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51106a5e-1919-3e59-a1d2-2df93344af34 | -10.61636 | -51.11774 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47e86fb7-ff05-39a8-9887-54f1b8c979bf | -10.6158 | -51.12127 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 132d4b0f-b1df-364a-9a67-e1cf672702a2 | -10.61524 | -51.12479 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35320454-3c63-3533-9cd5-48685687825f | -10.61472 | -51.10664 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5160814a-371b-3741-b8b6-790800a5d745 | -10.61416 | -51.11016 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1bb8a20-d847-31ce-ae05-3ac3fbf4c843 | -10.61084 | -51.10962 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0418b30e-0281-3d38-ad9a-831bd2f207f9 | -10.61028 | -51.11314 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64a035bb-9eb2-3ad9-b685-e0277f2052f2 | -10.60752 | -51.10908 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c18341d-a91d-3fa6-8df0-f1150bfaf61c | -10.60697 | -51.1126 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61916b4d-4cc5-356b-bbab-0219cc99ce56 | -10.60421 | -51.10854 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66ce03c3-6eec-32b3-80d3-00da7b11293b | -10.60365 | -51.11206 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1cabdfea-85fd-3c5f-a4f3-f30558309b04 | -10.58099 | -51.10477 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 40dc08ac-82b1-38fa-991d-7bbe2926fb48 | -10.5738 | -51.10722 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6cc07228-f422-3748-af83-5edbb801ce4f | -10.57324 | -51.11074 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 00755a2d-e142-35fc-a254-eede6ed28a3d | -10.57048 | -51.10667 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5cd047db-9a73-3a9c-957f-c522377f23cb | -10.56717 | -51.10614 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f565168-050c-3b6f-b7f7-08f5f38623d5 | -10.56441 | -51.10207 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff5eaa42-7706-34f3-88c4-1c1cb7b85f5b | -10.56385 | -51.10559 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f10880b7-a109-37f7-a03b-32d3f0e78d37 | -10.56109 | -51.10154 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2e71fbf-1f33-39a0-8ffb-e16f1aaa2c7c | -10.55834 | -51.09747 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7717cc2c-4d54-30d8-ade2-229f2c48adf8 | -10.55778 | -51.10099 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d1dfe37b-7399-3db2-b8ab-6b2e57fd504c | -10.55446 | -51.10046 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d193cda1-78bd-3716-a003-d38f8d242421 | -10.55115 | -51.09991 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 189e3b2e-3426-3b6c-8a29-14b378c0e8b5 | -10.55058 | -51.10344 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60d15fdb-dcde-3e91-9b1d-db3928352ef0 | -10.54727 | -51.10289 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a106d6e2-d04e-3782-bff2-16b33d3a81c7 | -10.54395 | -51.10235 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2fb8316b-e253-3bba-b8bf-79155d9b0bd5 | -10.54339 | -51.10587 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4c748242-5bbc-3c15-b0e3-d8f09009eb8d | -10.54008 | -51.10532 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3205bee-c0fb-350f-a692-196dfc9e40e3 | -10.53952 | -51.10882 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 25b6e47a-8146-3e50-a0c6-7d5af3747364 | -10.53621 | -51.10826 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 06ed077c-8719-33e2-9f25-118035ff8ce9 | -10.53565 | -51.11176 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48ffbabc-388c-3899-9c2d-2351d1631980 | -10.53234 | -51.11118 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ffb7f8ba-f81d-3091-891c-91bd2a669234 | -10.53178 | -51.1147 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80bcb963-7c55-3aa4-bdbb-2a7ba3aa9bef | -10.53065 | -51.12175 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f2be3f4d-2354-3e90-bf5f-3fea3561d8b7 | -10.53009 | -51.12527 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 34a1f11a-6faf-3a15-a723-1e1ed9a41817 | -9.88385 | -51.62695 | 2024-09-27 04:40:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d9b6e1d-2375-3b2b-a4f0-6275616c9312 | -9.88175 | -51.6269 | 2024-09-27 04:40:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4edef8a8-153e-329b-a661-7e764922c37e | -9.80073 | -51.8082 | 2024-09-27 04:40:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00b8303d-710c-391f-b5cb-972a87507795 | -10.06398 | -51.92277 | 2024-09-27 04:40:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e8ae3e2-2ac3-3118-9f7a-936ac081ee85 | -10.52621 | -51.12827 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e2c3c0b-331c-35a6-af0c-10b38cce44a3 | -10.52507 | -51.13536 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e49acd68-f452-3804-bca2-0f26fa64bed0 | -10.5245 | -51.1389 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9dccb295-0b94-3ebc-a48c-b70a5dce4192 | -10.52441 | -51.18211 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b082542-56f3-362d-8efd-7453a3a24ea5 | -10.52394 | -51.14244 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 112629e6-4de8-3b58-a85d-ab715c95b24a | -10.52384 | -51.18566 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fcdb43c-1269-3428-b503-b9efddc115de | -10.52289 | -51.12774 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 67dc282a-26c2-3283-985d-95e4c07c45da | -10.52232 | -51.13128 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 635f4e62-e08c-3146-a5e6-8664110f99a2 | -10.5211 | -51.18155 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ac266b1-3550-33d0-bf16-83b17a688cfe | -10.51949 | -51.14895 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b9a9de5-e646-3a5d-b3b6-40af581affb9 | -10.51562 | -51.15186 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8909eeef-802f-3e29-94e1-a77388c03bfb | -10.51352 | -51.27127 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28099244-0064-3f6b-8e74-3bccddf82f38 | -10.51231 | -51.15129 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ba86ef11-a72d-3f80-a252-93d4463bf6f8 | -10.50926 | -51.23413 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 18fd1ed0-4448-3e66-b139-56cce76b1b73 | -10.50899 | -51.15078 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e50cfeb4-135f-36ee-9705-eb00fd1112a7 | -10.50566 | -51.15029 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6ceebfc9-1103-370f-a322-95589d37c3b4 | -10.5051 | -51.1538 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cb25ec73-7150-3c81-a65a-034be645a215 | -10.5026 | -51.23309 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40ad2b83-f556-33b8-937f-0574749c7220 | -10.50203 | -51.23666 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d31e6577-2285-3ae0-b2b9-4e198024f45d | -10.50185 | -51.15334 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README94.md)
