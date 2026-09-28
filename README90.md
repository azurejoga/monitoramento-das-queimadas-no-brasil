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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 161f1006-4097-3b40-8d56-be56f6f8f3f9 | -11.7332 | -50.5516 | 2026-09-28 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| f381c0d1-d13b-39a7-ad12-f5c73fc30ddf | -12.2639 | -50.7034 | 2026-09-28 16:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 9da41bf8-ca02-3e3e-9589-5a087b9784b8 | -11.6951 | -50.556 | 2026-09-28 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| e7938fd5-6541-3615-add4-dd02050f6e01 | -13.5911 | -51.458 | 2026-09-28 16:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 209.3 |
| 173d20cf-114f-3059-8dc5-2cd2cc20ce02 | -1.467 | -49.0163 | 2026-09-28 16:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 377892ba-d647-3360-8bc3-1a6d410909d0 | -9.9582 | -50.2499 | 2026-09-28 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| bb2e8ffb-6cb5-3178-af8d-42e59f568545 | -11.1364 | -51.1496 | 2026-09-28 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 07a174bc-a460-307e-911d-0092795cb230 | -12.3088 | -50.2688 | 2026-09-28 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| b803b36e-de80-3e15-aca8-465bf2e50b61 | -11.9244 | -50.4866 | 2026-09-28 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 83804e4f-ce0c-33d9-8716-4a2d981b16a1 | -10.8967 | -50.6866 | 2026-09-28 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 7d449309-ecea-3ebc-961d-6d948ed8405f | -11.7329 | -50.573 | 2026-09-28 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 21b79952-6b6f-34ff-a01c-7b250a865728 | -12.1952 | -52.7821 | 2026-09-28 16:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 22a7ddf5-3bf3-3ee3-8c09-661d022e67fd | -11.7141 | -50.5538 | 2026-09-28 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 233ba296-f003-3104-8d31-76203cc67fab | -11.9964 | -50.7563 | 2026-09-28 16:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| e2628e86-c810-3c3e-b6d2-7ee0bacf0677 | -11.0991 | -51.1111 | 2026-09-28 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| a9bfe4f1-5d7e-39e1-a4bc-6f229b84f747 | -1.2818 | -49.3803 | 2026-09-28 16:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| d2f77f21-8d3b-3923-8c91-0bf171a58b98 | -10.7115 | -60.7312 | 2026-09-28 16:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 1c9800ba-7827-3b18-9508-613383f0660a | -12.7674 | -54.0502 | 2026-09-28 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 4b652313-abee-3d1c-beb3-6009b48766d4 | -10.9156 | -50.6845 | 2026-09-28 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.2 |
| a25c2afc-2335-38e1-bc85-aef89c5783cf | -11.9421 | -50.5702 | 2026-09-28 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 96c8798d-53a0-3732-8514-c69901bae969 | -12.0178 | -50.6041 | 2026-09-28 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 5dc96f4f-c00c-378d-b135-04cd7bd86474 | -11.5625 | -50.5283 | 2026-09-28 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 3513be10-c082-35d8-847e-c7bb6eb20c5e | -10.6928 | -60.7322 | 2026-09-28 16:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 0294adf0-ea08-3388-af8a-f27c41a2b5f8 | -13.3632 | -51.3163 | 2026-09-28 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| b44eba6f-f335-3738-82a9-07f339af425f | -12.2897 | -50.2712 | 2026-09-28 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 2f456d91-abc5-3879-8670-52b09f62c0cb | -11.8659 | -50.5791 | 2026-09-28 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 14a8248e-b89c-358a-9417-a7a0403e63c7 | -9.9967 | -50.1821 | 2026-09-28 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 67eb9ef1-e0ea-3483-b447-a874f7d4a001 | -11.6186 | -50.5861 | 2026-09-28 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 9bee49f5-b6d3-3b81-9026-df57700e8ae4 | -11.5818 | -50.5047 | 2026-09-28 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 7725f4fd-aee4-373c-8ec1-b625a7928ac4 | -11.1181 | -51.1091 | 2026-09-28 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 3391a454-3e79-3486-b556-396917cfa2f7 | -11.9593 | -50.6965 | 2026-09-28 16:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| a12ba005-a71c-3f9a-9c61-76d731dc339e | -12.0921 | -50.7237 | 2026-09-28 16:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| d38d5ba1-4b2d-3d48-b285-086fb566c5bd | -12.1115 | -50.7001 | 2026-09-28 16:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| bb1ac889-fd7f-3822-bc6e-bc31ef032c26 | -12.2445 | -50.7271 | 2026-09-28 16:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| fa3e3811-3d5d-3738-9315-9293c601f155 | -13.4325 | -57.061 | 2026-09-28 16:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 2f9c6c42-603a-3462-9dfe-5b27617bfae4 | -11.058 | -51.3482 | 2026-09-28 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| c5361a07-f635-3d0e-adc7-fb18bf750326 | -11.7138 | -50.5752 | 2026-09-28 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 679f8458-364d-37d6-a888-4200e9123561 | -11.7126 | -50.6608 | 2026-09-28 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 5fbbb75c-40aa-358c-af52-624899ac162f | -11.5815 | -50.5261 | 2026-09-28 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 96a58c91-86ab-3940-9632-a357080c3c05 | -13.3439 | -51.3187 | 2026-09-28 16:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 109.3 |
| d9b2a8f4-aed1-3836-9fe3-d705dec0330c | -11.8472 | -50.5598 | 2026-09-28 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 71ad6e60-a433-3289-998f-eea9e1dafe5f | -11.809 | -50.5642 | 2026-09-28 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| d62ef777-bd64-376b-960a-512f2525344e | -11.7138 | -50.5752 | 2026-09-28 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| ddf25705-c959-3333-943c-9b0c046563d3 | -11.7894 | -50.6093 | 2026-09-28 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 1e35e051-84ba-3ce9-ad26-b0fff24a4ee6 | -11.5625 | -50.5283 | 2026-09-28 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 4abbaf14-5734-3f05-8009-d0d26d40b1d4 | -10.9159 | -50.6632 | 2026-09-28 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 1fb9c246-5c4e-32b4-9d57-4c061cd13578 | -1.2818 | -49.3803 | 2026-09-28 16:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| bbce61fb-89ca-36ea-a7f8-ae6444375a18 | -9.9784 | -50.1412 | 2026-09-28 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 207.5 |
| c0f93c7c-7b6b-3a29-9dc8-0dafc3d07b19 | -10.9156 | -50.6845 | 2026-09-28 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 9ef32416-6867-3c5e-8cb9-217a66162e3f | -11.2859 | -51.3031 | 2026-09-28 16:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 20641334-3aeb-3912-9d96-370eca2d1b37 | -11.77 | -50.6329 | 2026-09-28 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 0ea24ec4-bbfa-30e9-accd-2b258839e19f | -10.6889 | -50.6658 | 2026-09-28 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 9b4a67fd-7fda-341b-8b31-bf406019af1d | -12.2435 | -50.7914 | 2026-09-28 16:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| a32ed61f-f55e-3690-84c8-bfdc9ed1ff24 | -11.8472 | -50.5598 | 2026-09-28 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 86340579-5e53-3bc9-86f3-603e962b204d | -13.4325 | -57.061 | 2026-09-28 16:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 88b489f8-f0dc-3b23-9056-03527a348bc5 | -10.6928 | -60.7322 | 2026-09-28 16:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| bc73bdbe-5fdd-3933-8f48-e9c31fa07e57 | -10.9671 | -49.7152 | 2026-09-28 16:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 1ff8f7e0-965c-3c9f-97c2-956c87d63d39 | -12.2119 | -50.3666 | 2026-09-28 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| f0576938-8eb1-323e-97bc-2bbecd84ebe8 | -11.7141 | -50.5538 | 2026-09-28 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 2528aa86-4cac-35fc-bf78-6858a670a274 | -11.7903 | -50.545 | 2026-09-28 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 31feec06-2b32-3e03-8276-d1fef18a34e8 | -12.1557 | -50.3089 | 2026-09-28 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 48c827c1-4597-3ee8-a18a-f1cf56372ff5 | -12.2445 | -50.7271 | 2026-09-28 16:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| aeb869d5-3e38-3e4f-97a3-fd1fab1dd30c | -1.3003 | -49.3801 | 2026-09-28 16:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| f0555380-a03e-3f75-86a7-6f230ffddae8 | -11.9971 | -50.7135 | 2026-09-28 16:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 8e01e01f-98ee-3211-b612-cb85f5026fc8 | -11.8281 | -50.562 | 2026-09-28 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 139da13c-4ac6-335d-807b-a7cc76692a9f | -11.7316 | -50.6587 | 2026-09-28 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 5bc0dfd6-dda7-3f01-8a6b-353d5958c29a | -11.978 | -50.7157 | 2026-09-28 16:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 90ddbd29-d8f8-3855-826e-8ce5bda412c6 | -11.5628 | -50.5069 | 2026-09-28 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| cebd3168-1f85-3db6-8f99-93b32e836c87 | -12.3088 | -50.2688 | 2026-09-28 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| fecb73c1-5e6f-3291-b94e-a5d174b88956 | -12.2442 | -50.7485 | 2026-09-28 16:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 07901a7a-bac3-3b83-84e0-2e0f3dd1b029 | -10.9536 | -50.6805 | 2026-09-28 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 303.3 |
| 6e85d5a9-33b9-3535-9fed-45efaa60688b | -11.0991 | -51.1111 | 2026-09-28 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.5 |
| edea40a1-e757-3485-8088-72b2fb56e730 | -11.1178 | -51.1304 | 2026-09-28 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 97560292-236f-3f0a-b7d2-5f8dd4c48368 | -11.5818 | -50.5047 | 2026-09-28 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| eb66a7a5-a367-3065-ab13-ebf3721a2403 | -11.171 | -50.0366 | 2026-09-28 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| eca6c274-8a7f-3a3e-ba33-40491c071a40 | -11.7313 | -50.68 | 2026-09-28 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| aeaed3bf-f023-306b-b5b3-3ec22684a7cc | -9.9781 | -50.1626 | 2026-09-28 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 00017834-24b5-368f-b255-b21bafa261e0 | -11.924 | -50.5081 | 2026-09-28 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| b565473b-0957-3a97-ba39-c89b3fe3031c | -11.1181 | -51.1091 | 2026-09-28 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 115.5 |
| ac57fefa-af13-3087-8ba0-ce5b26dc8e27 | -11.6199 | -50.5004 | 2026-09-28 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.6 |
| b6f681ef-1ce5-36fc-878b-41c04313777d | -10.8967 | -50.6866 | 2026-09-28 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 761c6758-d089-3aac-9e50-1d1f92b3c71e | -12.2448 | -50.7057 | 2026-09-28 16:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 069bb70b-4f2d-3075-bf97-7c7e339d8c1c | -12.0158 | -50.7327 | 2026-09-28 16:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 4fef25f3-ef4d-3386-82a8-36404a8a157e | -12.2639 | -50.7034 | 2026-09-28 16:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| be19bf98-d133-3f91-886f-d1b15e1c9d5f | -11.9612 | -50.568 | 2026-09-28 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 630c2d44-edca-338f-b718-7fb4c9b04da0 | 2.1266 | -50.8788 | 2026-09-28 16:10:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 3f479ad1-2634-3d88-9bc1-433e0a59eb7d | -11.58 | -47.43 | 2026-09-28 16:15:00 | MSG-03 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 10a63eeb-3f12-3240-8dac-51cd9939a804 | -7.99 | -43.28 | 2026-09-28 16:15:00 | MSG-03 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3977670e-e4eb-3b8a-97e7-0e6fea3aba17 | -10.98 | -50.69 | 2026-09-28 16:15:00 | MSG-03 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 56b4befa-d685-38e8-8c03-b0a7b8759d71 | -20.78 | -51.31 | 2026-09-28 16:15:00 | MSG-03 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bd1f2386-5d4d-3b2e-8f84-d9312c2e2079 | -11.22 | -44.86 | 2026-09-28 16:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ad6a0bf1-f04f-39e1-87a6-4c2763e66bad | -11.15 | -50.03 | 2026-09-28 16:15:00 | MSG-03 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3bd708f5-3d96-36ff-abab-bfa3b35fc5b4 | -11.58 | -47.38 | 2026-09-28 16:15:00 | MSG-03 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1e75261b-b2d8-31d9-ae2f-c1d82ac28790 | -10.95 | -50.68 | 2026-09-28 16:15:00 | MSG-03 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 14e5e3c1-b24a-3c39-9402-14d0c7c4a39a | -8.01 | -42.84 | 2026-09-28 16:15:00 | MSG-03 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9075d159-a841-3069-a908-f6412f7d2644 | -7.99 | -43.24 | 2026-09-28 16:15:00 | MSG-03 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a34e0b15-f660-3866-aa6d-e1dba8d07602 | -11.15 | -50.08 | 2026-09-28 16:15:00 | MSG-03 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d41358a-7625-30ba-9f92-a9d39715d151 | -11.19 | -44.85 | 2026-09-28 16:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 39b452ba-43bc-3711-a4a4-06db2a243520 | -12.8 | -54.0 | 2026-09-28 16:15:00 | MSG-03 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 09399dbf-7b98-3780-8e22-af2432bdbb1c | -10.8967 | -50.6866 | 2026-09-28 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 128.7 |


[Clique aqui para ver as próximas entradas](README91.md)
