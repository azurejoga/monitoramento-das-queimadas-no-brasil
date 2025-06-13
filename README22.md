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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13bd0c9c-8b3d-3f75-8c07-64360fb73ca8 | -10.29872 | -57.14394 | 2025-06-13 05:50:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8fb6c363-c94e-3bb8-8e53-46e4ac6f255c | -9.40043 | -57.55264 | 2025-06-13 05:50:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcdcdabc-3198-3a0f-b75a-eb6bfe709b22 | -9.1794 | -61.86636 | 2025-06-13 05:50:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 221a4d70-3b4f-3abf-9161-f545a5e964b2 | -9.22115 | -62.47644 | 2025-06-13 05:50:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 024e3d14-4c4f-3c9f-9dc5-ef48f1c2b5ea | -10.36646 | -57.50513 | 2025-06-13 05:50:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac8e3791-d46d-3b21-81a4-3a8df3c7838a | -10.86207 | -54.30517 | 2025-06-13 05:50:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8445ac85-ddab-3a57-b4d9-66e74d9c1707 | -8.68155 | -64.8731 | 2025-06-13 05:50:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b644bb4-3777-34d4-bc87-8a2351722a2e | -9.25022 | -57.53349 | 2025-06-13 05:50:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0abf8740-c124-3357-ab11-1070b86e43c7 | -10.36776 | -57.49886 | 2025-06-13 05:50:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1eda5a7-78b5-3039-b089-9d8f86f087a5 | -10.30234 | -57.13794 | 2025-06-13 05:50:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 474c5a93-0aeb-3a56-b964-d94f012b3b34 | -10.29334 | -57.13868 | 2025-06-13 05:50:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4eb12ece-2c1c-3eab-8592-237fa13da260 | -10.27575 | -60.53994 | 2025-06-13 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33d39ccf-b7e2-3f23-9769-e4e357f1a153 | -14.19577 | -57.40874 | 2025-06-13 05:53:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e79e43d3-071b-3dce-9881-2e0bc6cc8bf1 | -11.91647 | -57.47581 | 2025-06-13 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 32c0f69e-9ec3-3c5a-9bca-e888d0237e61 | -12.47041 | -58.47058 | 2025-06-13 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3b14d41-a923-3324-b842-aeb24ccb4956 | -14.19589 | -57.40271 | 2025-06-13 05:53:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ccb2a963-1e86-303f-b1d0-1f1e839e3d9f | -14.21517 | -57.40116 | 2025-06-13 05:53:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff619041-e8e1-3451-9019-72f9069dfe5f | -12.4709 | -58.46672 | 2025-06-13 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 671a1475-0f21-3997-aedf-4ee2fd484e47 | -12.52129 | -57.2394 | 2025-06-13 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 427c1adf-5206-3fbd-bd83-2cb987da35b7 | -13.89881 | -54.62659 | 2025-06-13 05:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 414931c8-c235-3120-9cf0-1b53da642caa | -14.19524 | -57.41369 | 2025-06-13 05:53:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3de52518-0832-32d3-866b-9c0a8f8e090d | -14.20241 | -57.40458 | 2025-06-13 05:53:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 32195f3e-fdc4-3ae4-b859-c39b280619cd | -14.20295 | -57.39966 | 2025-06-13 05:53:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3baec761-525c-3344-b5de-cc8c945525a1 | -12.5172 | -58.34485 | 2025-06-13 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0cf1892-58db-336e-960c-b887e64bad97 | -11.36812 | -56.55967 | 2025-06-13 05:53:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 868f1e75-7c76-3777-88c6-535f3d92d891 | -10.92041 | -56.82825 | 2025-06-13 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f3aaeebc-75b1-34f7-aec1-f07d5db39bcc | -11.12721 | -53.95052 | 2025-06-13 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9015464e-e3eb-309b-88fe-d18190de6313 | -13.89238 | -54.61835 | 2025-06-13 05:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3afc93f6-f4b0-37d4-866a-4fec4e9b2287 | -14.20905 | -57.40045 | 2025-06-13 05:53:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a1531c37-062c-30b6-bd55-c9def16e3d4d | -10.92483 | -56.84269 | 2025-06-13 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7a6a2794-267d-37b2-87c0-507c06038f68 | -14.0358 | -55.12024 | 2025-06-13 05:53:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34d38789-3e4d-3bc9-aead-029a4e74df1c | -12.52183 | -57.23487 | 2025-06-13 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47f59622-8a66-35e8-8bba-1ed571d1f489 | -12.47396 | -58.4697 | 2025-06-13 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bccf1282-24e3-3679-b6de-973297c4f104 | -10.22916 | -67.68848 | 2025-06-13 05:53:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| fd1694af-9c94-3044-adfb-ea615738dc8d | -14.19475 | -57.41261 | 2025-06-13 05:53:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5e79d2b3-7cc5-35b0-9057-9ce99d16acd9 | -13.89089 | -54.63315 | 2025-06-13 05:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2d089894-1a7b-351a-8e79-0dbc8cbe1c23 | -13.89018 | -54.64016 | 2025-06-13 05:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 45f09420-ffa7-347a-8530-0a1ec97fdde6 | -11.80318 | -56.96951 | 2025-06-13 05:53:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b69fda2e-b071-3260-8dad-3d2e7bb8cad0 | -10.91985 | -56.83284 | 2025-06-13 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4dfd568c-6587-342c-b019-c2cb632dcd6d | -12.46838 | -58.46902 | 2025-06-13 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f27679ea-69e1-3299-a294-0cb05bed2a73 | -14.21572 | -57.39613 | 2025-06-13 05:53:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43d3541e-9b38-3964-995f-b1e4198783a4 | -12.47648 | -58.46743 | 2025-06-13 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e6c3dce-7ea1-30b1-b3fd-d98e2eaef1de | -14.20199 | -57.40347 | 2025-06-13 05:53:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e42bd35-f037-381b-9ed2-e914e68cd428 | -10.04687 | -64.98505 | 2025-06-13 05:53:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d55a72c8-381c-30b8-9f91-b4ad8c43e73f | -12.52329 | -58.3418 | 2025-06-13 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eacbe5be-7658-37ea-b12a-02dc7c6a4e16 | -14.20143 | -57.40833 | 2025-06-13 05:53:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 539d9341-de32-3c9d-969d-575ddc238752 | -14.18964 | -57.4082 | 2025-06-13 05:53:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46f602d7-34d2-37a9-9f49-f734a6894e20 | -10.51733 | -59.39085 | 2025-06-13 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d39cf6aa-3545-3593-8f81-06a7a11be463 | -13.89735 | -54.64103 | 2025-06-13 05:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 744fa4e2-ec5b-3a4a-bb32-41a3123b2357 | -11.56745 | -54.57315 | 2025-06-13 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0c100b5b-375a-350a-8677-159b7cb5a643 | -11.1284 | -53.94885 | 2025-06-13 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 01683d1b-59ec-361a-a16b-b89e58109204 | -11.81252 | -54.50365 | 2025-06-13 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f19a9e28-91be-3801-83b3-1cc196c3d9b3 | -12.46792 | -58.4729 | 2025-06-13 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffab2139-b9ea-3e5c-b4ee-36e327c16656 | -14.20256 | -57.39855 | 2025-06-13 05:53:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 905de87d-26db-3bb3-b0e9-4c46c5bee3e3 | -11.80339 | -56.96866 | 2025-06-13 05:53:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 888f81b6-af70-3cc7-997c-5b7585aabaa3 | -11.13532 | -53.94397 | 2025-06-13 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 396af52f-bc92-36ea-b633-c9069f6d00c4 | -11.91805 | -57.4627 | 2025-06-13 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efa99e4b-cc70-3f39-823b-69c997e98cf7 | -11.91108 | -57.47074 | 2025-06-13 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 988942e7-6683-3037-94ea-3f7d2428cc6e | -10.27505 | -60.54498 | 2025-06-13 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb72496b-00ff-3381-8f1b-1defde9c2b0a | -10.27644 | -60.53491 | 2025-06-13 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19bec09d-eed9-3cc4-9efb-a9238d61e042 | -14.20959 | -57.39547 | 2025-06-13 05:53:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2359045b-9146-3816-9936-a5c631996474 | -11.9116 | -57.46639 | 2025-06-13 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38c6fe2b-aa33-35ad-8fb5-c42f037733ee | -10.92537 | -56.8382 | 2025-06-13 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5bfea735-d7ac-3005-b5e9-b59c0fdb1fea | -11.80927 | -56.97034 | 2025-06-13 05:53:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8882719e-1c20-374d-981b-d872e5b831ed | -10.8658 | -54.30398 | 2025-06-13 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c102c267-7294-3c64-ac53-d5cc0118cefd | -11.13564 | -53.94968 | 2025-06-13 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 821c42f6-c652-3785-b882-b17cff86d834 | -11.56844 | -54.58056 | 2025-06-13 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| dd8dcf9d-ce4e-3f28-a001-9150652fbddf | -11.56998 | -54.56729 | 2025-06-13 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e6e4d3ef-291e-3e47-8aaf-bf2226e47a27 | -14.20852 | -57.40535 | 2025-06-13 05:53:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b33f0051-2a7e-31cd-9e8c-13e9dbaf4e4c | -13.89807 | -54.63386 | 2025-06-13 05:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dd112e7b-5dfb-3181-8e5a-0fd032c9b047 | -13.89957 | -54.61904 | 2025-06-13 05:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6fb916f8-bb4f-36f7-8478-b197330376b5 | -12.52346 | -57.23433 | 2025-06-13 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| caaf661c-6701-34fd-a7d2-594057a79d01 | -14.19532 | -57.40763 | 2025-06-13 05:53:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2c0f198f-2530-3369-80a4-e9f38dedaecf | -11.56217 | -54.57323 | 2025-06-13 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8e54e27c-fe80-3647-9b77-22469d8d0aa3 | -13.89661 | -54.64828 | 2025-06-13 05:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 05ae3427-467d-3540-86e2-f0574e473d56 | -11.57625 | -54.57462 | 2025-06-13 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 97ca90b0-83c3-337c-808d-1ac5b3642831 | -10.91876 | -56.84183 | 2025-06-13 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7546b879-ce93-360e-b7d4-2ab0f4961b84 | -11.91752 | -57.46709 | 2025-06-13 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b000aa87-f910-3b99-84bd-6f2c890bef37 | -11.80284 | -56.9732 | 2025-06-13 05:53:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7821d94-3aef-3253-8a90-4c3b468dc65f | -10.92593 | -56.83365 | 2025-06-13 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bee4caa0-65f4-3189-b2ba-5bc5985f1845 | -11.917 | -57.47146 | 2025-06-13 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14b89bf5-a876-3d43-bddc-78bb55c89cc5 | -10.9193 | -56.83736 | 2025-06-13 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ecaa0fe5-44e8-365b-a4cb-a6d213f8609e | -12.51524 | -57.23864 | 2025-06-13 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3fed644-85f1-3929-a22c-102270d23c1c | -12.51741 | -57.23354 | 2025-06-13 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 798cd7fe-6c15-3efd-b5c0-1654ced3e6dc | -11.57449 | -54.57385 | 2025-06-13 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00212381-d73c-3713-8bec-3df68459a4ae | -10.52241 | -59.39175 | 2025-06-13 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 22c7eff8-8c29-368a-85b8-c961067808d8 | -11.56673 | -54.57978 | 2025-06-13 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ae00865a-1c8a-3ba0-94fe-820a06024e15 | -12.51579 | -57.23411 | 2025-06-13 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b489647-8419-318d-8553-338b613094d3 | -10.04748 | -64.98102 | 2025-06-13 05:53:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 564dde79-be6f-3431-ab8e-41378413726b | -11.56043 | -54.57232 | 2025-06-13 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5d0fdd76-ad77-3eb0-a267-c988d65df9d2 | -10.93201 | -56.83438 | 2025-06-13 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 98ff4276-2087-39a6-b878-0d2a6a0e3ddd | -13.89162 | -54.62589 | 2025-06-13 05:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 543915fa-a2d4-3b3d-a6a5-bfdc49553937 | -11.36868 | -56.55495 | 2025-06-13 05:53:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c41c28e-75d6-3987-8319-959c3e042e43 | -11.5692 | -54.574 | 2025-06-13 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c33f117a-f1f3-36fd-80c5-968874b48b2f | -12.47442 | -58.46586 | 2025-06-13 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2a9fdc4-746d-3010-a094-81d1eec9cfd1 | -11.5682 | -54.56636 | 2025-06-13 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6afec02e-1383-35d6-b03c-f58696f2f2a5 | -9.96179 | -64.97675 | 2025-06-13 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a50ca3af-fe33-3dc5-9354-9f640eded367 | -10.93145 | -56.83899 | 2025-06-13 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6144c615-6d42-3596-921a-bf3ebd4480d1 | -12.51689 | -57.23809 | 2025-06-13 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f66ff6d0-1fb1-3d64-be15-ac16e637fc2c | -11.80948 | -56.96948 | 2025-06-13 05:53:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README23.md)
