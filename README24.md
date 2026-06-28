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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 926f88ef-f2eb-3b26-8ea6-5bac934b8d05 | -11.65771 | -57.25793 | 2026-06-28 05:53:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e560c5d1-d0aa-3468-a1bb-d18d5bb89163 | -12.45624 | -58.49198 | 2026-06-28 05:53:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fbd2d64f-af30-3178-8927-9ff989f0a802 | -12.22825 | -56.54839 | 2026-06-28 05:53:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f7bc6724-0600-3dd4-88f1-f1b942510841 | -12.16935 | -59.75641 | 2026-06-28 05:53:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ffcafe0e-28e6-345e-a8b1-1be6793612e1 | -12.60183 | -57.88342 | 2026-06-28 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 08370090-de3b-3dae-8aa3-b2c9cc026bb8 | -12.18298 | -57.14666 | 2026-06-28 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b829307a-a1a9-3ce3-87d9-abc4ffe8eac4 | -11.92451 | -58.67146 | 2026-06-28 05:53:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e25b8379-87c1-36fc-abc2-97e2257f703c | -11.92432 | -58.66467 | 2026-06-28 05:53:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad5e3aa4-c591-34a0-9da7-99d4a082ca5a | -12.45669 | -58.48835 | 2026-06-28 05:53:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1049b077-ef02-3e96-9a91-bbe1b1e9272d | -12.60665 | -57.8924 | 2026-06-28 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a5844b81-5e3a-36a1-afa6-b984c44f4cf5 | -11.66688 | -57.25689 | 2026-06-28 05:53:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3d63b678-ac9f-344b-8f77-cfdd51f3ff03 | -11.87754 | -57.81981 | 2026-06-28 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d864639-126c-3357-96c8-909f964b71c5 | -12.23452 | -56.54924 | 2026-06-28 05:53:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4b080716-b8a9-31c3-965f-29f3ef5b8c62 | -11.9257 | -58.65379 | 2026-06-28 05:53:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9b3b2a8-172f-3a30-9a24-7307e78f64b1 | -12.62451 | -57.8906 | 2026-06-28 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f940cd74-94c8-3ea7-a56e-1abdc45bdcbc | -12.45113 | -58.48764 | 2026-06-28 05:53:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 70bf136f-d130-38ac-8453-a2c5f48ef6ec | -11.86698 | -57.81032 | 2026-06-28 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 011ac1b1-ce42-338b-8b7e-52670f461d83 | -12.98593 | -57.7783 | 2026-06-28 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50589bfb-173d-32fd-8def-f69c369fa766 | -12.60135 | -57.8875 | 2026-06-28 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7ea90b8e-3637-37bc-a22c-edfb5c39bc54 | -12.4609 | -58.49994 | 2026-06-28 05:53:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3665d252-be2a-363d-9014-d9cd3dbbde03 | -11.93397 | -58.63262 | 2026-06-28 05:53:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79752b23-d6de-3a6b-848a-4aface1e6a0b | -11.9298 | -58.66518 | 2026-06-28 05:53:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 572c346c-e0d2-387e-93d3-8bf2f19204c8 | -11.92538 | -58.66426 | 2026-06-28 05:53:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 056e3155-b007-3432-88cd-31af2b48b5ab | -12.60713 | -57.88829 | 2026-06-28 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 60d0cf4f-6de4-325b-8fb3-2b54d6e245ee | -12.45159 | -58.4839 | 2026-06-28 05:53:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 53a680b5-3a9a-3f7a-865a-325c3637da92 | -11.92581 | -58.66064 | 2026-06-28 05:53:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e09e88e6-432b-3958-bd61-f06fba26248e | -12.23333 | -56.55955 | 2026-06-28 05:53:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dbad0dff-c06d-3521-b50a-2f91aa65c251 | -11.93673 | -58.61101 | 2026-06-28 05:53:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 952f3990-12db-3fad-bc98-49f55d9c6464 | -12.4618 | -58.49268 | 2026-06-28 05:53:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 18dd4255-6de9-3a4f-9a97-f16342c6655a | -10.05624 | -59.11272 | 2026-06-28 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 859ca54b-4d02-3000-b1f7-059ccdb80e18 | -10.90298 | -56.85664 | 2026-06-28 05:55:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d51affe7-35ec-3410-a0a6-a506438a4eaa | -10.29356 | -57.12533 | 2026-06-28 05:55:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 015031f5-97c9-3742-85b1-ec1cdd02bef4 | -9.08922 | -59.41616 | 2026-06-28 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7e23444e-631f-3294-be46-d3416a3ac6e2 | -10.29686 | -57.13386 | 2026-06-28 05:55:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ee885555-3221-3ae1-aa2a-2c56d2cbe5af | -10.05484 | -59.10807 | 2026-06-28 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7eea0045-e729-3e7f-991c-c76f655d8f1b | -9.18932 | -58.06633 | 2026-06-28 05:55:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 792fbec9-b92c-3956-8c15-c03d0793037b | -11.20956 | -54.3046 | 2026-06-28 05:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 21247388-d36c-37c0-8c5d-2bae94ac3476 | -10.30479 | -57.13134 | 2026-06-28 05:55:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f74fbf02-e7e5-3f96-9582-e179bf546c56 | -11.32158 | -54.46971 | 2026-06-28 05:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b52d7d2-9898-3482-a6da-8a0f19e39ea1 | -9.03304 | -61.32782 | 2026-06-28 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c8bc30c-d7ab-3abf-8ecc-2b83dc9747e0 | -11.2066 | -54.30404 | 2026-06-28 05:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| f6877bd8-124d-3d22-b3be-3639e0c4340e | -10.29739 | -57.12949 | 2026-06-28 05:55:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 54aa8c9a-6dbb-351c-8d1a-6aa6247ea1e3 | -10.06 | -59.1088 | 2026-06-28 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73149deb-5f3d-34e6-a451-76a1a3ee4b07 | -9.16652 | -58.07037 | 2026-06-28 05:55:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82751dca-275c-3f1c-94ee-a5966af203ae | -10.29888 | -57.13063 | 2026-06-28 05:55:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b1fb944e-a9bb-3cae-b2cb-d246c13a862f | -11.52978 | -54.79058 | 2026-06-28 05:55:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d91c800a-0e77-338c-868b-0b6b21f6af6a | -16.19188 | -59.32798 | 2026-06-28 05:55:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 966b3780-5c57-37b2-af5c-861463f65b75 | -11.20739 | -54.29698 | 2026-06-28 05:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| a75ca249-9502-3088-983c-1298547910a8 | -10.93442 | -56.85099 | 2026-06-28 05:55:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3dc4717d-b61c-360f-93fa-1290bbf63526 | -9.09234 | -59.39297 | 2026-06-28 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 92c6ed38-431f-3aca-b3b4-bde44c06c8ba | -10.30225 | -57.13889 | 2026-06-28 05:55:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f26ec41-6daf-3e3a-95a5-3847daeb4170 | -10.05958 | -59.11185 | 2026-06-28 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12ea862b-f8b6-3beb-acd3-1bb728f8c9e4 | -10.77701 | -54.10826 | 2026-06-28 05:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6e53016-cece-3564-b33a-efeef166ce6b | -10.78415 | -54.10897 | 2026-06-28 05:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3bdc06b-de66-33f2-8d7b-7f8c17b7d8b0 | -10.05663 | -59.10963 | 2026-06-28 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 441d740d-6f24-32fc-a003-de46ad664c66 | -11.21039 | -54.29757 | 2026-06-28 05:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 5b9ac6e0-daeb-324c-97bc-e28206012c52 | -15.44172 | -59.23593 | 2026-06-28 05:55:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bcbca5ad-4392-3b6a-ac4f-7501d89bedb4 | -10.30437 | -57.12144 | 2026-06-28 05:55:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1f4796ed-99d0-38b6-a2f0-f4b1b24810cb | -11.52931 | -54.79729 | 2026-06-28 05:55:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 46bfed1c-d9bc-328d-b193-26b5adc6863f | -15.44215 | -59.23217 | 2026-06-28 05:55:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b7a6252-2b27-3456-807f-a09ca802b81d | -10.30368 | -57.13999 | 2026-06-28 05:55:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a105a2a-32b7-3600-b597-a4534c57bcf6 | -10.30278 | -57.13455 | 2026-06-28 05:55:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 97e8293e-c8f4-3506-a4be-a24b1fc33421 | -15.43623 | -59.2351 | 2026-06-28 05:55:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 505b9207-0562-3403-9b91-336f8b76ef01 | -10.3 | -57.12189 | 2026-06-28 05:55:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 0a4618c1-77ea-3c1d-a528-6a2288aa7b55 | -10.05442 | -59.11116 | 2026-06-28 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bbee20a2-64a7-322d-81f8-6a415f16b337 | -9.03187 | -61.33628 | 2026-06-28 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 983bd190-fc3b-3f50-af56-78a6c2b90fa5 | -10.30424 | -57.13564 | 2026-06-28 05:55:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0a6488d2-e4c9-331e-ac9f-5fc82f4fa49e | -9.09156 | -59.39882 | 2026-06-28 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0cb398cc-2c82-3dbf-9171-18d4ac2b648c | -11.21367 | -54.30499 | 2026-06-28 05:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| baea0c20-0ddf-3b27-a4cb-4e8349ce6b39 | -11.2129 | -54.31188 | 2026-06-28 05:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 8cf74e8d-be99-3e6e-823c-68528ad53a54 | -9.03245 | -61.33206 | 2026-06-28 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfaf1eb3-c167-3a6e-990f-f62a52f9b551 | -9.08424 | -59.41545 | 2026-06-28 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a562c07b-c3f6-3e52-bbd5-0a5244b72ce6 | -10.3033 | -57.13022 | 2026-06-28 05:55:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6d06b8ae-7ca9-39d0-8aa8-9f3d35dfd225 | -10.29776 | -57.13933 | 2026-06-28 05:55:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16d6eded-edda-3c80-8a59-2d04de493278 | -10.29944 | -57.12627 | 2026-06-28 05:55:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| a37de2be-9654-3ec4-86db-d4d2426c830a | -10.30172 | -57.14326 | 2026-06-28 05:55:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f364e521-2d6f-365e-b7f6-b63cbb84ee3d | -10.30383 | -57.12584 | 2026-06-28 05:55:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 79da3eba-7a0e-3149-8904-ae172addc00a | -11.53007 | -54.79071 | 2026-06-28 05:55:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f350f673-23a1-3b96-93a6-557b764b9794 | -11.52285 | -54.78987 | 2026-06-28 05:55:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1726094e-3789-319c-86fb-269a89bccbe2 | -11.52213 | -54.79654 | 2026-06-28 05:55:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9c1cfeec-313a-3f45-8ea5-549f3ef1ceb6 | -9.08003 | -59.40898 | 2026-06-28 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 36b317e8-cc07-300b-b004-471141fe8c07 | -9.08501 | -59.40972 | 2026-06-28 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 91ded7ea-fcf0-37fa-91ba-96fbef32472d | -11.52314 | -54.79004 | 2026-06-28 05:55:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 64383589-ad20-379b-ba61-d401444759af | -10.81392 | -56.61419 | 2026-06-28 05:55:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6cc5c7d-a0c0-31b0-9072-01a824c5cec5 | -9.09293 | -59.38861 | 2026-06-28 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 457eb2d8-97df-30d4-b088-bd7bd8d6e690 | -9.08578 | -59.40396 | 2026-06-28 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e754ccbc-bfdf-3d80-9613-21357fa250e0 | -10.29832 | -57.13499 | 2026-06-28 05:55:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 27fd922d-901e-329c-8d99-6b33fdeb9466 | -9.08999 | -59.41045 | 2026-06-28 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 637d3cef-9feb-3430-9cfc-25ef6f7bb718 | -9.03128 | -61.34049 | 2026-06-28 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33ea4f35-4892-3d5e-aaab-74d2fc3d4cde | -9.03564 | -61.3411 | 2026-06-28 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| febe8265-2833-32b8-9cf5-463d4dce903e | -9.18885 | -58.06989 | 2026-06-28 05:55:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5ce9dcb-9f38-3abe-8f7f-d293ff801ead | -9.08793 | -59.3879 | 2026-06-28 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 003c2c08-e137-37f3-b853-57bbcac64751 | -10.29792 | -57.12511 | 2026-06-28 05:55:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d91e13ae-18f4-3428-9671-ba19dbbd2d1b | -11.21447 | -54.2979 | 2026-06-28 05:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 86175d1a-3344-34d7-be99-d749245b6a73 | -10.30763 | -57.14392 | 2026-06-28 05:55:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f6eba88-b8db-3812-9da8-738d8936f681 | -11.52906 | -54.79717 | 2026-06-28 05:55:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 28d5bc46-d118-3d08-ae71-cbddee5e4a08 | -10.30312 | -57.14436 | 2026-06-28 05:55:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a6690ad-e413-3826-9b3e-a3d96dc3dac7 | -11.52237 | -54.79669 | 2026-06-28 05:55:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a09e1c09-1c55-3bc2-8efe-6ae7a5480e53 | -10.80779 | -56.61328 | 2026-06-28 05:55:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99972af0-892d-3148-b73c-b472f0829ec2 | -10.05703 | -59.10654 | 2026-06-28 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README25.md)
