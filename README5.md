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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b09a0a67-9b5e-3499-84c1-3b02f9a770bd | -21.5675 | -51.92976 | 2025-09-11 01:07:00 | TERRA_M-M | CAIUÁ | SÃO PAULO | Brasil | 3509106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| ae90abae-a292-32e1-b718-564ba61007fa | -20.57708 | -47.69621 | 2025-09-11 01:07:00 | TERRA_M-M | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 10e35eb9-af76-3e26-879f-d0bd40ca97e3 | -19.18843 | -47.98866 | 2025-09-11 01:07:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 96c50257-b6c2-35fa-9587-b4849201d433 | -19.00146 | -46.25166 | 2025-09-11 01:07:00 | TERRA_M-M | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 37.2 |
| fc0898f8-7f2c-390c-9cd0-045bde007e3f | -21.10549 | -48.06556 | 2025-09-11 01:07:00 | TERRA_M-M | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 0c95eb2d-18a4-300b-9578-cc53f7503384 | -19.01211 | -46.24363 | 2025-09-11 01:07:00 | TERRA_M-M | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 41cd93b2-1acf-3d66-adc3-5eb5b7ef70a2 | -12.40372 | -63.83564 | 2025-09-11 01:09:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 62c917f8-5f79-3f12-aaa9-f90565e3afe2 | -9.03014 | -49.7664 | 2025-09-11 01:09:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 23a6f61a-7a55-3997-914c-4810d69e103a | -10.57074 | -52.03326 | 2025-09-11 01:09:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 18c42de3-8f30-3e9a-b7d0-cc5e1dc57479 | -14.92229 | -55.83821 | 2025-09-11 01:09:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 93caf52f-afc0-3e27-a53f-51a3a59d5c7b | -12.40144 | -63.79811 | 2025-09-11 01:09:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 21.3 |
| ae2934ff-d4ae-345d-9217-b956e7398879 | -16.52251 | -55.16614 | 2025-09-11 01:09:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| f44d5ed7-2b4a-347e-8a0d-e934f203fa56 | -14.46989 | -53.32128 | 2025-09-11 01:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8e5503bf-eadb-34b6-a06b-91944ca8e496 | -14.50732 | -53.95865 | 2025-09-11 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1a093f1d-4685-3e5c-86ce-62421f3c2a0d | -10.54379 | -49.88136 | 2025-09-11 01:09:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 83db5887-88e4-350e-9bec-8e083d74e098 | -16.53423 | -55.17714 | 2025-09-11 01:09:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 40c06c39-fde1-3ad2-8bd2-7e8c9bef1164 | -11.99775 | -47.63202 | 2025-09-11 01:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| b2fd32a5-a6b1-3ad3-bfcf-0cc5c4034b22 | -12.01632 | -47.6004 | 2025-09-11 01:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| f0933a01-ffa5-3dd8-8176-ea371e9582df | -15.80483 | -52.22753 | 2025-09-11 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b1d0fc34-8baf-36cb-8275-636d9d473884 | -14.921 | -55.82903 | 2025-09-11 01:09:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4317c344-9f13-329c-ad1a-a0054d36c58d | -12.93106 | -54.75392 | 2025-09-11 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 1ad056a1-b166-3bf0-b1a0-69907e353068 | -11.17212 | -52.05746 | 2025-09-11 01:09:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| d3e5e6d1-a937-3862-acc1-6131f2909caa | -14.2737 | -53.10924 | 2025-09-11 01:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 22c77fa5-2471-332d-a788-00c6ac8ab697 | -14.28198 | -53.09542 | 2025-09-11 01:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 7edc9475-1638-33c5-85e9-2beb71a46ae6 | -9.52082 | -54.63081 | 2025-09-11 01:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 0f1623d0-51fd-3069-b300-2c56e27d915a | -15.55247 | -54.7709 | 2025-09-11 01:09:00 | TERRA_M-M | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 412b46f2-7fa7-3b15-a1af-83aa7982f3c7 | -14.74879 | -60.24057 | 2025-09-11 01:09:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 23.0 |
| a6f1fdd9-8809-33db-b388-2e70ec065201 | -14.7371 | -60.23028 | 2025-09-11 01:09:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| c121c6e5-090d-3d94-afdf-5f6688b7b088 | -12.06518 | -64.18731 | 2025-09-11 01:09:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 21.7 |
| dd4138e2-6c72-323f-b768-997b287d8c53 | -12.94039 | -54.7524 | 2025-09-11 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 029905ed-461e-383b-8b19-f6bf2687c52c | -15.55103 | -54.76118 | 2025-09-11 01:09:00 | TERRA_M-M | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 012fa61e-4ca9-363d-8a88-e569ec5e8475 | -16.29575 | -50.05227 | 2025-09-11 01:09:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| c97eaead-688e-3ea0-bb0d-da7067474a93 | -8.0238 | -48.6651 | 2025-09-11 01:09:00 | TERRA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 9e8a8435-067c-38b3-b081-d55312309cbe | -13.01928 | -48.73381 | 2025-09-11 01:09:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 44.1 |
| ef63e448-7ec8-3d1e-8411-3821e6df88a0 | -8.03197 | -48.65888 | 2025-09-11 01:09:00 | TERRA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 3bf4950b-9c4e-3e59-8242-ebadacec2b75 | -12.38325 | -54.1675 | 2025-09-11 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 48062b05-3557-3e38-8178-2675084eecf1 | -16.52117 | -55.1567 | 2025-09-11 01:09:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| f156f0f1-1bec-3807-ac20-fc2169f7e1bd | -16.18405 | -53.86635 | 2025-09-11 01:09:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 61954fb0-e1ae-3d9e-9c08-2a3c958e925e | -11.16954 | -52.04148 | 2025-09-11 01:09:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 123.2 |
| d89df9a4-8fa4-3193-8ca3-ea06e56b8072 | -15.87217 | -54.93774 | 2025-09-11 01:09:00 | TERRA_M-M | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| e70f5649-223e-36a6-8a2c-a8af355b5a9f | -9.02826 | -49.77348 | 2025-09-11 01:09:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 90ce2225-9737-3f9a-9f85-e66f033f3aa7 | -9.51259 | -54.64319 | 2025-09-11 01:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| a8ae870a-1941-311a-8c1b-b2e1664da8d6 | -15.54959 | -54.75138 | 2025-09-11 01:09:00 | TERRA_M-M | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d14e4a8b-a829-3afa-a5c3-db8fa59bc288 | -14.31417 | -54.75164 | 2025-09-11 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 36385d47-269e-3a89-bb5c-530aa3b81a00 | -12.94925 | -54.81318 | 2025-09-11 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 21.4 |
| a8767368-5321-32b6-9488-f7adc0bb8eed | -14.88812 | -55.85279 | 2025-09-11 01:09:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7747e5c6-f7dc-35f9-aaaf-fcfeee71d453 | -12.0955 | -51.01389 | 2025-09-11 01:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 94ba7788-993f-3498-9434-d98561454382 | -9.5999 | -55.01332 | 2025-09-11 01:09:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| fab2413a-a93c-3325-b6a6-2a82e50f85b8 | -15.14793 | -52.4035 | 2025-09-11 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b60cc8a7-77cc-3da6-8f70-ccc4c46d909a | -9.80569 | -61.52813 | 2025-09-11 01:09:00 | TERRA_M-M | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 17.4 |
| fe29e99f-3411-3242-9aa2-6fe0fa748081 | -9.60148 | -55.02395 | 2025-09-11 01:09:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9fe57b93-6af8-3dff-992a-8c357781302b | -11.22428 | -55.00024 | 2025-09-11 01:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 22.1 |
| c212d601-fd46-3e7d-834c-d822dfcca6de | -11.87544 | -58.81348 | 2025-09-11 01:09:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 8988c28f-5902-3354-b87d-54cc525664e0 | -15.56157 | -54.7695 | 2025-09-11 01:09:00 | TERRA_M-M | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 9fa9c8af-006a-31ab-9320-5bcd49f8f974 | -14.50244 | -53.9547 | 2025-09-11 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| de1bee80-d73e-3864-bb0c-306624aad4e3 | -12.85199 | -47.96032 | 2025-09-11 01:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 0d7e92b6-2cb7-3d7e-b2f2-5ee1cb74680a | -12.92768 | -54.79589 | 2025-09-11 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 7daf2ecf-ef2c-3dff-b9d8-8dd2862969aa | -12.38488 | -54.17847 | 2025-09-11 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 4b334266-dcee-37be-ade1-48d6b156dce7 | -17.32767 | -46.68311 | 2025-09-11 01:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 6de1f63b-12db-3234-b578-5298e53c2ee1 | -12.09007 | -51.00139 | 2025-09-11 01:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 5ab7b8d0-8ca6-3872-83ce-b72e834fa9c0 | -15.11421 | -52.39432 | 2025-09-11 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 1f243cb6-5081-3c2f-af32-f794a8e46513 | -10.38692 | -50.53872 | 2025-09-11 01:09:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 38.0 |
| c7586461-a6fa-37ee-a5a9-32f6fc1c9c71 | -11.16164 | -52.04845 | 2025-09-11 01:09:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 247.4 |
| 2c4c54ad-2096-3da3-bc4c-86597d5752cb | -14.47169 | -53.33311 | 2025-09-11 01:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 31.9 |
| a935d9d9-3d8e-3f95-b43f-da270084307f | -14.46177 | -53.33475 | 2025-09-11 01:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 7a55de76-7612-353b-901c-b600ce1032c5 | -11.16059 | -52.05945 | 2025-09-11 01:09:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| e86b20d6-7b37-37bd-ab1f-bce5d29e1dc5 | -10.00704 | -51.72546 | 2025-09-11 01:09:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 29829b4d-18e1-346e-b79f-337bb84570c4 | -9.80404 | -61.51533 | 2025-09-11 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 3c45c3a3-9477-341a-9c9f-de25925e0032 | -17.33277 | -46.68867 | 2025-09-11 01:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 68.7 |
| aec3b95e-f3af-31a4-849e-853ee087c9ca | -11.88586 | -58.822 | 2025-09-11 01:09:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 33ee6f73-5b51-3d22-ba0e-c7bd0d25e0dd | -14.27186 | -53.09708 | 2025-09-11 01:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 42d31040-ce1e-39dc-a1f4-9098207a5d26 | -16.51983 | -55.14725 | 2025-09-11 01:09:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| f2b047f4-0d26-305d-88bf-b7ce345b0ced | -11.19571 | -55.0673 | 2025-09-11 01:09:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2cbfe9ac-d924-3b13-8b13-0fab199ab0fd | -10.01915 | -51.72343 | 2025-09-11 01:09:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 9d7d142d-2348-376a-88cb-c506653096d8 | -12.93699 | -54.79446 | 2025-09-11 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c2ebd8f0-e7b4-33a5-bb72-705b0b376a5e | -15.1289 | -52.41905 | 2025-09-11 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 5f6cb07f-a443-3bfb-bc67-7e89ed0e4ab5 | -14.28186 | -53.10204 | 2025-09-11 01:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| bf1cc3c7-4395-35d4-b4b3-07d412e4df04 | -12.95906 | -54.74947 | 2025-09-11 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 296958af-0dbd-34f4-a53f-701d099fe960 | -12.61046 | -56.97039 | 2025-09-11 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6b75a7ff-36ce-3f43-a42c-a105cba64815 | -11.88458 | -58.81227 | 2025-09-11 01:09:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 74f14b15-0014-3d0e-b4fe-f36f4a3eeecf | -11.35823 | -56.31635 | 2025-09-11 01:09:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3b549142-5cba-3028-8dbc-e4c080e02f9d | -10.02185 | -51.74104 | 2025-09-11 01:09:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 4126d432-6ca2-3ddd-bdaf-2e063ebb94c5 | -16.53287 | -55.16772 | 2025-09-11 01:09:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 13.6 |
| d66e33b5-4076-37c0-b07f-f472fb8bee29 | -10.06712 | -50.37823 | 2025-09-11 01:09:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 71b12863-cd7d-3dec-b142-150892a089be | -12.92173 | -54.75538 | 2025-09-11 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4b9f2de5-304e-3812-b9a8-69d323bbf133 | -14.88682 | -55.84364 | 2025-09-11 01:09:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 1b237e88-4d07-3598-84ae-6c3d746cb24a | -12.85512 | -52.94741 | 2025-09-11 01:09:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 06c6a8b5-7a00-32e7-aef2-80cb2c7ffe77 | -11.35867 | -46.54256 | 2025-09-11 01:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 188.7 |
| e6e2ab50-973c-3923-bf9f-8ffc13f1a917 | -12.85646 | -47.96509 | 2025-09-11 01:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 6178e52c-96d1-39a7-80da-803e04d03d19 | -14.57859 | -48.76247 | 2025-09-11 01:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 26.1 |
| eb186126-bd85-3bfd-975c-21f09f7ff1e0 | -14.92767 | -55.94035 | 2025-09-11 01:09:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b9a53c15-5121-319e-afce-e6c4980349c8 | -12.42822 | -47.80198 | 2025-09-11 01:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| e3ced7c4-9603-380f-b8f8-d7c3fd4f8115 | -12.06271 | -64.16492 | 2025-09-11 01:09:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 4fa56770-2ce4-30ee-a39e-f085e8fa0430 | -16.54314 | -55.17567 | 2025-09-11 01:09:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| c74030cc-7ffb-38e2-8559-128ce8e0bf91 | -10.1914 | -51.69504 | 2025-09-11 01:09:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 714249bd-1d81-3f6d-8121-52c9717f96fc | -13.02048 | -48.72813 | 2025-09-11 01:09:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 52ffee50-fdcf-3642-ad48-b031d337b4b9 | -12.41446 | -63.81282 | 2025-09-11 01:09:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 9f395edb-c5a3-35cb-a764-e5ea8144212c | -14.45996 | -53.32291 | 2025-09-11 01:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 5a41e99a-f224-305f-9c85-0eacbd70e607 | -14.74722 | -60.22773 | 2025-09-11 01:09:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 24ece889-5469-34b3-9807-eebbdddf18f3 | -12.21699 | -53.87675 | 2025-09-11 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |


[Clique aqui para ver as próximas entradas](README6.md)
