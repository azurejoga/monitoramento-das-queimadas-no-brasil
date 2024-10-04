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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1939c530-eb13-360a-b567-7b9da96825fb | -10.73937 | -47.64795 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 679696cd-5771-31e2-90ef-afc958e6850b | -10.73896 | -47.7178 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf2b016b-1b25-3ac5-87b3-846feae16a99 | -10.7384 | -47.72139 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 953039c6-a2e9-3bfc-bf82-6e4a32a71021 | -10.7382 | -47.63308 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1585a0be-7cc8-36eb-9e3d-afede4b86220 | -10.73785 | -47.72497 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42ac5b02-503c-3760-9324-0b494b295763 | -10.73765 | -47.63666 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e68b809f-6475-3fbb-ac8d-093297fcb585 | -10.73725 | -47.70653 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6970bd7c-e0c8-306b-93bc-fa2db1b530a4 | -10.7356 | -47.71727 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ae26b06-dc9a-3a76-afe9-8e70dcda403a | -10.73539 | -47.62897 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b2c317c6-cb6d-3a80-837e-bdb6b7eda5ad | -10.73504 | -47.72088 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23b3dacb-edeb-3c35-a69a-7ebcac331e48 | -10.73449 | -47.72447 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4e1bb90-581a-3483-b3dc-54ba50b63d3b | -10.73444 | -47.70242 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b199bd8-6307-3f80-974a-ea1420c17b3e | -10.73389 | -47.706 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96732b43-f4ee-34b5-a849-fc02fea13bfa | -10.73279 | -47.71314 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b45351c1-5c11-3f46-9bf0-5c68a8c0f595 | -10.73224 | -47.71675 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8a33490-7c38-3bb7-9a66-3ed522fc172d | -10.73203 | -47.62843 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04c356a6-da8f-3127-b687-f4a3d29de67d | -10.73168 | -47.72037 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c94c0bc-e2ae-3091-aebd-c6e101444702 | -10.73113 | -47.72396 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9ed39d6-d948-3b2d-bca1-84b293b5574d | -10.72943 | -47.71261 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55780c36-c157-31a8-b83a-262e12dba1cb | -10.72888 | -47.71623 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37a2f101-f858-3270-be96-bb8a4d72302c | -10.72866 | -47.62789 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7db30be0-d70c-3bbe-b136-11eeea0a5d4f | -10.72832 | -47.71984 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 475a6c86-455d-3ab9-b338-a86f2e67fd41 | -10.72827 | -47.69778 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d10dddfd-9d26-3ce0-b974-6b0ad0cff72b | -10.72773 | -47.70135 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6daa554b-f0a1-3c53-b5a0-0bd9df58d979 | -10.72585 | -47.62376 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99510bd2-e546-3f97-8b0a-5473084e4d49 | -10.72552 | -47.71569 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9d8cf67a-4305-3e8f-8a21-7bf764fc4d4a | -10.72497 | -47.7193 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 723e630f-0026-33a2-b19e-817a8285b0e5 | -10.72491 | -47.69726 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59b1f829-0b90-31cc-903d-960246ca851d | -10.72437 | -47.70082 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc14ded8-7d6b-3786-89db-5f9832eefeb1 | -10.72382 | -47.70439 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36b6159b-af1b-3a42-9840-3d66435fff27 | -10.72327 | -47.70797 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4f8a5ee8-67c7-359d-ae3e-f1c461f0aef8 | -10.72216 | -47.71516 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c066011-4281-30c4-8782-94db5b8b76ce | -10.72161 | -47.71876 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ff3b7ef-947e-359c-a958-bfd70de2232e | -10.72106 | -47.72236 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 704fcce8-9f0a-35e3-8c82-a532d511cc0a | -10.72101 | -47.70029 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a51b0fdb-bb5d-351f-8dea-1f817278f4eb | -10.72046 | -47.70387 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f77c8740-b5b0-3343-8f06-dd9577a47d88 | -10.71991 | -47.70744 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 15155882-b4e9-3824-be16-25d944fd624d | -10.71825 | -47.71822 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0927d901-48fa-3c53-a0a4-6f30ee69f57f | -10.7177 | -47.72182 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb99c8ae-c69a-3c13-8930-13857a902982 | -10.71659 | -47.72905 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5ecfc027-ae2c-3ac5-8175-85f9b3a8b90c | -10.71379 | -47.72491 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a64a9942-b7d3-330e-a35f-accc98685074 | -10.71323 | -47.72853 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5e8082f4-cfdd-38b7-94c3-d9d4a08b2990 | -10.71209 | -47.71358 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92c91085-1ac3-3723-8367-1eb29232a3fa | -10.71043 | -47.72438 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba83e4c9-6e7c-3849-85fe-a8339f13df79 | -10.70988 | -47.728 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91ca2366-1726-3c3a-bb28-059ed85e90d2 | -10.28354 | -47.68804 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 26f5ec8b-3cf7-3c42-8312-bea09dba1f1b | -10.27683 | -47.68695 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 937e77e2-78c0-3cb5-ba17-68c2a1e0724e | -10.27629 | -47.6905 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 421bbaa3-a34e-3dee-85cb-910a5b1457c1 | -10.27574 | -47.69404 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7a0d82a5-2ea0-31a9-af36-86766116c342 | -10.20418 | -47.72263 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f9db34f-9981-3f1a-8912-e7e6bb32e148 | -10.20028 | -47.72564 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6edf4edb-6a02-320e-9566-ca112c23fd5f | -10.87289 | -48.14034 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a551e03-b857-338f-9117-5e51e940a9d9 | -10.86512 | -48.14637 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8a9cf507-a2b6-30a6-bca2-58a17320b50a | -10.83204 | -48.27148 | 2024-10-04 04:32:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 25a64c5b-fd8a-3f72-8f5a-2bfbea43d1a5 | -10.83149 | -48.27502 | 2024-10-04 04:32:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1c4158a2-3c49-3a6f-b071-eb4f50a3109a | -10.82816 | -48.27448 | 2024-10-04 04:32:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8bb34f46-0f33-3cff-8719-59b59d603193 | -10.78384 | -48.73257 | 2024-10-04 04:32:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d4ea8936-a385-31bc-a059-04604ed78fce | -10.76446 | -47.98565 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 945b6e96-eb63-3fe6-9d4f-054628f6ae99 | -10.76391 | -47.98918 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61b1f6a7-39c9-3d6e-9a91-da9cf4bb9ed9 | -10.75103 | -47.9723 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7607d7ec-07a7-348c-ba5f-61072eca46b4 | -10.74992 | -47.97941 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d32505b9-4033-398c-99af-1db91b03968e | -10.74937 | -47.98298 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5a4d31d9-fa5e-33bd-9f6b-230f764c3dbd | -10.73288 | -48.71369 | 2024-10-04 04:32:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ce911f12-7b7e-38c1-a089-8db50f74152e | -10.61307 | -48.05233 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e902bf72-076a-35e0-8d02-a5918ed40521 | -10.61253 | -48.05583 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cf6f394-2728-37e7-9a99-b228ad589455 | -10.61199 | -48.05933 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff3e490d-010a-3035-b555-5011d62c55e5 | -10.60973 | -48.05183 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8f89c20a-e20e-333b-8d13-c22f79f981d4 | -10.60918 | -48.05535 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2262324-824b-3f00-baea-66cc933db1d7 | -10.60864 | -48.05884 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5586c36-5a57-3b1a-8829-b1f62b485cba | -10.60748 | -48.04427 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4b08494c-7de0-3f5e-b8db-d22b7608c3e7 | -10.60249 | -48.05437 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 49260ed9-496f-36e5-8342-ba4132589626 | -10.60154 | -48.12643 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1a6179c3-0859-333e-93cc-b6b8d9411abb | -10.5997 | -48.05033 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 66d49f6f-75e8-3844-9407-8f95d9d04575 | -10.59915 | -48.05386 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 65dd1ef9-86d6-367e-ab27-bedce6e318fb | -10.59876 | -48.12236 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48dba69f-9d97-3653-9ae1-3267fdd8e0d6 | -10.59861 | -48.05737 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 60470de2-bae6-3f10-9fef-e6e6dd9273de | -10.59821 | -48.1259 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bc7eb1d8-5f65-3f8a-a3a5-e992db7e6c48 | -10.59691 | -48.04626 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4c679616-b6ba-317e-a2d2-c67b9fd57f82 | -10.59636 | -48.04981 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b289693-bbd1-3c34-a564-d854ced88137 | -10.59527 | -48.05686 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d3544d2a-1314-36d4-abb4-24a12f2748c2 | -10.59377 | -48.13243 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c16bd995-3979-3c7a-bb2d-310f0d136f8a | -10.59322 | -48.13596 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5173745-4682-370b-91c6-f7a5a8df6d8e | -10.59099 | -48.12836 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2b3d0cbd-0412-31d9-87b2-f66ae146ce08 | -10.59044 | -48.1319 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b406586-b418-3e79-bf82-4baf2b3e0ff3 | -10.58377 | -48.13083 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e050040-3e3a-38ba-b62d-d501bc207078 | -10.57908 | -48.02895 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9b8cc415-b0c1-3483-b038-830f181962ad | -10.56332 | -49.0173 | 2024-10-04 04:32:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8ac266cc-f7d8-3153-8113-e4d80f9a35f3 | -10.56276 | -49.02081 | 2024-10-04 04:32:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a5b091f6-2bf0-3483-ad8d-ad97705b217e | -10.55999 | -49.01676 | 2024-10-04 04:32:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6439c749-0ec7-3c2a-b5e4-24fc12d609a0 | -10.55476 | -48.07553 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8941873d-6b76-3fe8-b649-97c1d7928f34 | -10.52491 | -48.03524 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1cb33cd-ec14-3da4-9e24-99ae8ab97bbd | -10.52157 | -48.03471 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ba16320-df22-362a-90bf-3c80d24abbb2 | -10.49572 | -48.17872 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a4c9326d-11c7-3077-9068-44a7114a6fc3 | -10.49293 | -48.17469 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| c4c998bd-e3b5-38ed-a206-e3081373e706 | -10.49238 | -48.17821 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 414db0ec-7f18-30d1-8c0d-5227a8c125fa | -10.49183 | -48.18173 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 135ca020-399b-3f81-b252-9485f586e5da | -10.49128 | -48.18525 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd6dfa91-8234-300a-9fc9-5d1d3a5f5c9d | -10.48959 | -48.17419 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 24d9836e-4c54-3383-a6d4-9fb0a77b9f07 | -10.48904 | -48.1777 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 646d0490-257a-3870-be2b-bacb2ebc2712 | -10.48849 | -48.18121 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README103.md)
