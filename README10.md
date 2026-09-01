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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad4c86ed-d22a-3254-b741-ca5c0050cd18 | -5.87106 | -57.78144 | 2026-09-01 00:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| be1b9174-4772-3683-a15a-0dea5c37ee13 | -6.42524 | -53.56317 | 2026-09-01 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 4585f4f5-a126-393b-9c5c-4a5be366aceb | -4.49546 | -46.39714 | 2026-09-01 00:26:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 44.4 |
| fbc04083-3fce-3379-a2dc-9e002d459726 | -6.1192 | -53.55633 | 2026-09-01 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 5196c228-47f6-3061-81b1-d78972a1b175 | -7.63599 | -55.29181 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| e5a9b393-aa4e-38f5-8ec2-9eef8ba6a527 | -6.18792 | -57.73033 | 2026-09-01 00:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 41a90825-e6d8-3cc7-8fe8-02641ffb1170 | -6.82155 | -58.86769 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| a742d3d3-0ad5-317b-adc6-1ae78d55c1e0 | -4.97136 | -55.83237 | 2026-09-01 00:26:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b225d479-1531-367e-8003-39b0c3f5a6cc | -6.56617 | -58.56237 | 2026-09-01 00:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 33.1 |
| d9dcf1f8-6548-3afc-9c34-281460a452d7 | -6.78802 | -55.63417 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4cad7915-bc87-33b6-a6c8-37f045522bb7 | -4.79897 | -55.9849 | 2026-09-01 00:26:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5f526189-c9df-3473-812a-32d1f88a89cd | -9.4118 | -51.67918 | 2026-09-01 00:26:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b7f6d3b4-3221-3157-b720-feafe7459f95 | -8.71423 | -52.36449 | 2026-09-01 00:26:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| a29195ca-34a1-33f1-8afb-258cb6c576fd | -5.49166 | -57.14788 | 2026-09-01 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 7a720ff0-2f7c-3dbe-a2ac-0c70b6bcae8d | -7.25409 | -61.10435 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 8bf1be97-be99-3869-a8be-e9f1b73a37f0 | -4.48327 | -54.97131 | 2026-09-01 00:26:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2cbe741b-801b-3d56-b398-22f647d727f4 | -7.67841 | -55.33971 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 10bd3943-b724-3146-ba9c-667d2941d4c9 | -5.95147 | -57.69391 | 2026-09-01 00:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| f44396b8-f4ff-3661-bf2f-e5e64886b083 | -7.33754 | -60.60176 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 87f2b388-7658-3fa8-bb47-12ba184222f6 | -6.69094 | -55.4027 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 9deda663-0202-3f38-a45e-7c64c87b0b33 | -3.11893 | -61.21829 | 2026-09-01 00:26:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 05f81405-013d-38a2-b770-54712cbbd359 | -6.12665 | -57.69809 | 2026-09-01 00:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d7f2fa6a-845e-3574-b485-c7fe3f6fc617 | -7.03226 | -59.2242 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| d2a336ea-546d-3299-9424-1d56bbdf9f1b | -8.50545 | -55.32053 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fc837eb7-eed6-3476-a7a8-4ede3bb5481b | -7.04267 | -59.22284 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 3f853cfb-ba40-3572-938f-7d8c390b95bc | -6.22405 | -55.49035 | 2026-09-01 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c57861dd-cd7f-32e1-b6ba-db4a61f779ea | -7.28943 | -60.66366 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 3f8282a4-3625-3d68-be91-823b56b6c93f | -7.34512 | -60.56789 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.7 |
| d5caea3e-d3a4-3e6b-ab8e-7f6d27d28a29 | -6.1559 | -57.77531 | 2026-09-01 00:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 0a63b8d9-6328-3615-b2ed-d4ec373c5f63 | -5.25079 | -55.91768 | 2026-09-01 00:26:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7c7ec713-1079-380d-92a6-bcb15f02f473 | -7.30227 | -60.5794 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 53cf1025-cdd9-31fe-aeb9-d0ddb15b079a | -6.41521 | -52.2029 | 2026-09-01 00:26:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| c7318d04-abbe-3eca-a2d4-71117ed0598a | -7.6872 | -55.33847 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 9f6128af-5a94-33d5-b167-9633ac057a1b | -6.9445 | -55.62687 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| bed619e3-0863-3e45-9d3c-46f84eb89fe0 | -7.18197 | -55.49142 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b326ca9c-f1dd-36d0-829b-0ccd55d0da91 | -8.14437 | -54.96714 | 2026-09-01 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cd5bd477-769d-3233-a7a7-2d49da368332 | -3.62919 | -60.57632 | 2026-09-01 00:26:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 22bf0e19-a9ea-304a-9273-35a4385de5e4 | -7.61793 | -57.62363 | 2026-09-01 00:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 1925005d-7c84-32bf-a29c-0744e3f2ae7b | -4.95741 | -55.86111 | 2026-09-01 00:26:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bf655fec-0fda-377e-9e4f-e1bd20dc4e89 | -8.50424 | -55.31168 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 80c5a9e7-1264-38ed-b45d-d2b7a2c126a4 | -7.19026 | -60.6983 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 3d8b3ac6-7c27-3eb0-be6b-b380c196704a | -6.18926 | -57.74027 | 2026-09-01 00:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| bf54a1f3-79f4-331c-9646-e031f82763d4 | -9.15731 | -60.95628 | 2026-09-01 00:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| e7cd8b04-9a51-3ba4-8f70-c69c5b2767eb | -5.85017 | -57.55404 | 2026-09-01 00:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4bf45219-27df-358d-afa6-2f1b76388a28 | -6.92524 | -55.63541 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 4454eda2-66ee-329f-b4dc-ba7396dbc3d7 | -6.91974 | -55.72601 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a2a6424b-67c6-3b44-b856-4ce6e38d5a81 | -3.18307 | -48.02758 | 2026-09-01 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| cd647f21-44e1-313e-8f64-7a373000d02f | -7.57434 | -57.6981 | 2026-09-01 00:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c90e5c46-cdf5-3769-b4aa-30a4107e6330 | -5.24838 | -55.90015 | 2026-09-01 00:26:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 12455528-443c-39a9-846d-9aec35971616 | -9.48082 | -57.02529 | 2026-09-01 00:26:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| fdf82e0e-d07b-3af5-be69-4dc3e88c62d1 | -4.50735 | -46.42524 | 2026-09-01 00:26:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 796c407e-d9b2-3f38-8a76-01ba074804bb | -6.81125 | -59.10184 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 398a87db-767b-3c5b-8886-7a8ace6b4ab5 | -6.71009 | -63.19406 | 2026-09-01 00:26:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 19.8 |
| c457a9db-bad9-3444-b7a3-6a5296c3f6f7 | -6.1178 | -53.54653 | 2026-09-01 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0e775f50-3d8e-3b12-a9e8-112f913618af | -10.06388 | -59.41092 | 2026-09-01 00:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 8eac1c10-cf1b-3302-b889-2d4cc6d4cd9c | -6.15724 | -57.78535 | 2026-09-01 00:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| a12946a8-f044-31f5-bb53-5fac8a0fbb74 | -3.60786 | -59.07331 | 2026-09-01 00:26:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 65cc9d67-f929-3397-bb90-3cc084e6e502 | -6.96247 | -56.43829 | 2026-09-01 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 8ae4aca0-c649-3574-90db-d3f65991a724 | -5.8607 | -57.56249 | 2026-09-01 00:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 4d441211-5607-3487-868f-f4f0811cef9b | -6.69215 | -55.41149 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 140.4 |
| 39760bb0-91b2-3340-abe6-12e4984cd5e9 | -8.59397 | -54.75488 | 2026-09-01 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| af035c89-472b-33b4-8482-bf7a91a812ee | -8.61647 | -54.78778 | 2026-09-01 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 09102c94-d0b1-3c05-97d2-1ed3a1664e73 | -5.95016 | -57.68412 | 2026-09-01 00:26:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 18f136cc-c9d3-345f-8dd7-d377024ea7f5 | -6.8892 | -59.45049 | 2026-09-01 00:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0a70c912-8cef-3414-899c-2077abf5eb11 | -6.93282 | -55.62536 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c79a5c65-061d-3755-a5da-2ecd260be4f2 | -6.13501 | -55.64304 | 2026-09-01 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| a549c709-1217-3bcd-af5d-7c125f45ce7f | -3.62728 | -60.56236 | 2026-09-01 00:26:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 4e86e8a4-11d7-3fb1-af8d-b5581bd72f65 | -5.89072 | -52.2585 | 2026-09-01 00:26:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| ac3a4ea8-9d7f-320a-b39b-e8b56a4cd79a | -7.02727 | -55.64217 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 318d0722-2ee1-3c71-a0e6-6ce5640d9b57 | -3.64025 | -60.55439 | 2026-09-01 00:26:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 395047d5-07ee-3865-a833-1a6d8dfd8344 | -6.70972 | -55.40901 | 2026-09-01 00:26:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| ddcb270a-9d9f-3561-9ead-2f9e54ad6724 | -1.77781 | -53.50348 | 2026-09-01 00:26:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fe953bce-0a9a-34f2-8859-ed0235c2a2ab | -1.46495 | -54.2138 | 2026-09-01 00:28:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e707831c-63bd-3a13-9b0d-017105a43f0e | -1.44069 | -60.27863 | 2026-09-01 00:28:00 | TERRA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 78b4081d-70bf-3e6b-870d-6148030704ca | -1.46634 | -54.22392 | 2026-09-01 00:28:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 48f4cc00-5ce4-35ac-8c82-97f0b042a874 | -2.31016 | -60.2706 | 2026-09-01 00:28:00 | TERRA_M-M | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c73b4c58-e7d3-3679-b5a3-40c01f348182 | -1.43901 | -60.26634 | 2026-09-01 00:28:00 | TERRA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 8acf67e7-1391-319d-b0a5-75bb32d4d431 | -17.372 | -42.3544 | 2026-09-01 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 138.5 |
| facb8bb3-d20d-3fcf-8610-501a04fde9eb | -3.0612 | -39.9346 | 2026-09-01 00:30:00 | GOES-19 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 51.0 |
| dbc1469b-caeb-3dd7-9648-d58a54c2d5e9 | -7.3302 | -60.589 | 2026-09-01 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| a53fe7ec-5d71-39cd-a38c-2bea3b8d1587 | -11.277 | -50.5815 | 2026-09-01 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 5f514129-20bd-3cac-b809-24ffea257b5d | -14.1266 | -52.7895 | 2026-09-01 00:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 208.0 |
| e3b4d564-015b-3e98-b1ea-bc6b73c0588f | -7.3488 | -60.5691 | 2026-09-01 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| a568e461-eac2-3a75-bf2b-71a54d84b942 | -10.3199 | -49.9996 | 2026-09-01 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| b33bdf94-fa4c-3bdb-8502-2e99d0a8b8cb | -3.0425 | -39.9355 | 2026-09-01 00:30:00 | GOES-19 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 50.2 |
| c77927b3-afc3-30fa-a084-c9beecebc2ef | -17.3914 | -42.3744 | 2026-09-01 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 3749344a-9faa-3c20-bb7e-6006dcb5f954 | -7.3487 | -60.5883 | 2026-09-01 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.4 |
| bd0d65ae-e465-32c3-9cef-3897827d88ae | -17.3928 | -42.3245 | 2026-09-01 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 19e22a0c-4fa9-3c97-bca2-95020bef55eb | -6.1844 | -57.7395 | 2026-09-01 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 417a9214-d23d-3963-9063-6dcb06d99c4c | -10.036 | -44.7056 | 2026-09-01 00:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 265cfde1-56e2-30f5-8577-e861c5ad6b45 | -11.2577 | -50.605 | 2026-09-01 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 171.5 |
| 30fabb38-0283-33df-a6ac-39a958f110b9 | -11.2767 | -50.6029 | 2026-09-01 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 5c953588-4210-3907-b1b4-1893ebd4ddf9 | -17.3921 | -42.3495 | 2026-09-01 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 288.7 |
| 40dcb1b7-4fbe-32d5-9217-a585841c9c01 | -10.3385 | -50.0191 | 2026-09-01 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 9f653f47-9c4a-3a67-a388-f4d35735c932 | -10.3574 | -50.0171 | 2026-09-01 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| c82bf162-c413-3b6a-90c4-cc1c5324427e | -10.3388 | -49.9977 | 2026-09-01 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 62df892c-92ee-3b20-9a4f-874b8d5fc578 | -6.6036 | -58.5972 | 2026-09-01 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| c44e5c04-3808-3511-8629-6635b5b52e8d | -7.2005 | -60.6897 | 2026-09-01 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 91182dae-1905-357e-9147-cf309101ee82 | -17.3713 | -42.3794 | 2026-09-01 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 115.3 |
| e0a335a6-5e13-34b8-8c6b-e00a6f304a78 | -11.2391 | -50.5857 | 2026-09-01 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |


[Clique aqui para ver as próximas entradas](README11.md)
