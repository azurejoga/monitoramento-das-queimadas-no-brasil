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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45816447-cd63-354d-81a0-bd9ae9d791e3 | -15.03141 | -54.89239 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b069e722-6e9b-32f8-bb49-81effb4641e3 | -21.95258 | -45.5907 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 60310687-9a71-313f-96ef-919df5ed6cbd | -14.66796 | -54.92659 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 89f774cc-1d4e-3abf-95f1-7728a775d449 | -22.65958 | -46.91374 | 2025-08-23 04:04:00 | NOAA-20 | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4aa682b3-de7e-3ce0-a7f6-02396f907872 | -17.69633 | -48.50002 | 2025-08-23 04:04:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c832f40-4efd-39e5-88cb-88b24ef122ee | -23.46803 | -46.14499 | 2025-08-23 04:04:00 | NOAA-20 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4e5eed42-a30b-3f7c-99a0-6cf0669b1d0d | -16.61648 | -49.41539 | 2025-08-23 04:04:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a5f7c5c6-5247-36a6-9bf3-4c608ebf0c10 | -20.0877 | -46.12166 | 2025-08-23 04:04:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd449543-a664-3360-9388-1b785cc06b90 | -17.57514 | -48.74905 | 2025-08-23 04:04:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0fa50732-ebaa-34ff-9704-e978c24d4330 | -20.09524 | -47.7692 | 2025-08-23 04:04:00 | NOAA-20 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0b1a37d-8d15-3ca4-82c1-8d831a9a6d2c | -20.09042 | -47.75204 | 2025-08-23 04:04:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5653b874-e47a-3c64-8bfc-5377ac214157 | -17.26743 | -46.76273 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 46bd05c5-de2d-32d0-8652-bb0ac23a7068 | -17.2667 | -46.77132 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e79fb060-0803-3b96-ac72-075a0e1bce53 | -18.91516 | -47.77342 | 2025-08-23 04:04:00 | NOAA-20 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31e13e1d-7836-3d6f-98db-60a21d1fe97a | -15.71914 | -48.21572 | 2025-08-23 04:04:00 | NOAA-20 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3f66edc-10d3-3c35-82d6-6aa453ac70f6 | -20.18761 | -50.96854 | 2025-08-23 04:04:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2f4f8319-c1d8-3357-a084-b96512a5e21b | -20.24694 | -46.63509 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96b60918-61ff-33eb-ae84-86ab5e786d2a | -21.44518 | -52.66499 | 2025-08-23 04:04:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e4c91bb-0d8f-3722-927a-31e7b0bce46c | -18.06765 | -47.87624 | 2025-08-23 04:04:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 166ce7da-853d-3fef-84ac-d2882074d3f9 | -14.67042 | -54.87471 | 2025-08-23 04:04:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eae6f997-7237-3d56-bc43-7b81fcb71654 | -14.61398 | -54.85846 | 2025-08-23 04:04:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 85c39521-f35c-3e32-abe9-87d036417763 | -21.75296 | -47.35651 | 2025-08-23 04:04:00 | NOAA-20 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 10717eab-a0e4-3f0f-87a1-2ad0eb07b1fc | -20.00077 | -48.52662 | 2025-08-23 04:04:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9bdfd22a-35e2-3347-a965-516361ff8cbc | -20.44466 | -42.13216 | 2025-08-23 04:04:00 | NOAA-20 | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 7a3029ef-4bc5-3855-8bbd-581794049f0e | -19.94921 | -47.48145 | 2025-08-23 04:04:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5313afe9-ed83-30ac-9535-6ad358d6d0d9 | -14.61124 | -54.80823 | 2025-08-23 04:04:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0487887d-d328-394e-bf6e-efe3b53708d9 | -15.64842 | -52.68681 | 2025-08-23 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f6f0066-1e56-3429-9cc9-50e0979caab2 | -21.0184 | -42.35709 | 2025-08-23 04:04:00 | NOAA-20 | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 04ca5975-795d-359c-9efa-d77f97e3ef82 | -15.65493 | -52.68387 | 2025-08-23 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2687c6ec-10ff-336a-a8ac-35b9741ef080 | -22.90348 | -46.39478 | 2025-08-23 04:04:00 | NOAA-20 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 3fc31e2e-379d-3a17-bc37-1b4b14fe483f | -15.01748 | -54.86876 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6342708f-f132-3fae-a26f-eaf09fc65602 | -23.10428 | -46.80267 | 2025-08-23 04:04:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 36d2a61d-3025-31b0-b6f1-9bf2b308c94f | -15.00969 | -54.87327 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dfdd94e8-8ffd-30f3-89fc-6eb3f0874d16 | -21.47691 | -43.92225 | 2025-08-23 04:04:00 | NOAA-20 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 2cdfbd77-5480-3a80-ac50-efd530b35a32 | -19.95208 | -47.48725 | 2025-08-23 04:04:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e37fed88-258b-3cbf-9b32-6deccf8d1a89 | -22.16881 | -43.28162 | 2025-08-23 04:04:00 | NOAA-20 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9533d6a7-108e-3cd5-9209-14b27f66cf53 | -22.95653 | -46.46147 | 2025-08-23 04:04:00 | NOAA-20 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 80b6deeb-f3bd-3693-9cee-07c235bab168 | -15.54527 | -51.70741 | 2025-08-23 04:04:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6e7ec62-d861-3423-8d67-9a5589122add | -21.67705 | -49.05205 | 2025-08-23 04:04:00 | NOAA-20 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdc4c041-61a7-3c04-b5ac-0c74c7457a1b | -20.0885 | -47.76255 | 2025-08-23 04:04:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 095a6fe1-b301-3c8f-83b4-73dba9580bc9 | -18.75285 | -46.68553 | 2025-08-23 04:04:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d82993ed-5448-37a3-950e-0129d2c720c0 | -18.4964 | -46.793 | 2025-08-23 04:04:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 708ccd8a-1e66-3008-96a8-8bfd8d9984b4 | -20.09139 | -47.76847 | 2025-08-23 04:04:00 | NOAA-20 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2eea37f-f273-3352-a23e-aa137abd2d3c | -17.59146 | -46.56169 | 2025-08-23 04:04:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a0e4a596-cc3d-31a0-829a-49f6b3355c3c | -17.26756 | -46.76646 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| abbf508f-dc38-3780-a3b3-7a62ba705bcb | -22.52735 | -43.72427 | 2025-08-23 04:04:00 | NOAA-20 | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b5cbb06d-cbd7-30b7-937c-20c6c2665504 | -19.03965 | -45.26504 | 2025-08-23 04:04:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24621c17-1bc8-39fc-87c3-cf9550e84db4 | -22.48011 | -44.44476 | 2025-08-23 04:04:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5855cea5-935b-3ce6-87b8-60bdd2847506 | -17.61004 | -46.69958 | 2025-08-23 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5e6b098-1484-38de-9704-fc4c77e707b8 | -18.25848 | -45.5687 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4ff0702-b747-3187-ac59-8bbfa2b5030d | -23.10077 | -46.80196 | 2025-08-23 04:04:00 | NOAA-20 | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 183c9f15-5a40-3be9-81ec-47dace2d2e90 | -18.26833 | -45.57482 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 996fc2db-4f9f-354b-86be-af95edd7ca4b | -16.4894 | -46.74538 | 2025-08-23 04:04:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d15e18e-17ee-3bb0-8aa4-f19aba450f7c | -22.47285 | -44.28256 | 2025-08-23 04:04:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 93b8d372-69ce-3f02-a61f-694482bb82f7 | -22.63133 | -47.43176 | 2025-08-23 04:04:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41b2b99d-69ec-3d3a-8e59-456617446f3b | -18.29095 | -45.54919 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 015ad840-8839-354d-a8c5-440aebad0e17 | -14.69528 | -54.91784 | 2025-08-23 04:04:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7c7662c-5c82-3763-bd28-f05fb9d8c676 | -15.56495 | -55.01513 | 2025-08-23 04:04:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 052aa308-6e68-3b24-a092-8f4f316f6d6a | -22.66236 | -46.91885 | 2025-08-23 04:04:00 | NOAA-20 | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| efc5c81a-193f-30d0-b18a-45b6fb3ac758 | -21.4517 | -47.02527 | 2025-08-23 04:04:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70f26f59-895c-37e9-bd2c-2ab80f367fdf | -17.59863 | -46.09435 | 2025-08-23 04:04:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d74bf7a4-4188-35fb-b0fe-3c3383669499 | -19.96572 | -47.52057 | 2025-08-23 04:04:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3edf2b76-522f-3b4f-a30c-e70361f8d9b8 | -14.67196 | -54.92996 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2a6847a2-816c-3bca-a5b3-8bb6449634b4 | -18.25702 | -45.57704 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acb62410-9dfa-36ff-90fa-66502e16068f | -22.30405 | -43.17468 | 2025-08-23 04:04:00 | NOAA-20 | AREAL | RIO DE JANEIRO | Brasil | 3300225 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f554bb94-17bd-3be7-a651-f637157e3e30 | -22.6659 | -46.91962 | 2025-08-23 04:04:00 | NOAA-20 | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| acbb7daa-c30b-31dc-bc95-a12cc147ca62 | -14.7501 | -55.99326 | 2025-08-23 04:04:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c64a9974-fbbc-363f-90b5-e62857427968 | -20.72532 | -43.22173 | 2025-08-23 04:04:00 | NOAA-20 | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 07e35503-e3b7-3ebd-92e9-a468232e591c | -20.87155 | -42.54073 | 2025-08-23 04:04:00 | NOAA-20 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| f13d3596-ac65-3e90-ade4-c0a0ea939e34 | -14.66418 | -54.93397 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5623de50-036e-356e-bca8-bdb98bd5bc67 | -16.23742 | -48.76057 | 2025-08-23 04:04:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51d693e8-9dbf-3e90-a6a6-f0e265e1f080 | -23.49245 | -46.00097 | 2025-08-23 04:04:00 | NOAA-20 | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2e6ae293-40ce-3718-9f0c-d557ef74b083 | -14.69011 | -54.91005 | 2025-08-23 04:04:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b27d589a-de40-3266-be21-d442c6f74fed | -19.77926 | -45.65922 | 2025-08-23 04:04:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5056710e-6589-3314-8982-09f153d10e5e | -20.08371 | -47.74531 | 2025-08-23 04:04:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0cac2f9-2836-3506-a30e-428d34fd256e | -21.44286 | -45.9976 | 2025-08-23 04:04:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9e03202d-ad44-3508-97de-93be012c37eb | -22.1727 | -43.27849 | 2025-08-23 04:04:00 | NOAA-20 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1b331d91-bd1d-3b88-a123-2cfbf488c3b9 | -17.28163 | -46.77082 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a210320a-437c-3420-8aac-f6b1a72ec747 | -14.65619 | -54.91735 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6afff0f3-79f3-33f8-8d43-04269f65e137 | -15.56625 | -55.00924 | 2025-08-23 04:04:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| af61abed-5c80-323d-a5d6-b59c1df06720 | -15.01948 | -54.89127 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a8a67546-4465-36de-8287-963f0d2950d3 | -20.276 | -46.68176 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cef03484-b4bf-3a51-85f9-d76cbabe73c5 | -23.49177 | -46.00497 | 2025-08-23 04:04:00 | NOAA-20 | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3aa275d0-2ab3-362d-9121-fba8ba71ff80 | -19.94833 | -47.48631 | 2025-08-23 04:04:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 739883c7-74c7-320d-91bd-942f17d300dd | -18.2704 | -45.58386 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ec53678-9b64-3b2e-b48b-afdf9b72f768 | -20.56331 | -44.85118 | 2025-08-23 04:04:00 | NOAA-20 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 4696ffcc-6d7d-3d0e-ab13-7f60deaec72f | -22.74563 | -46.54565 | 2025-08-23 04:04:00 | NOAA-20 | PINHALZINHO | SÃO PAULO | Brasil | 3538204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 428e7486-666d-344e-bc06-d92defca94f9 | -15.01605 | -54.86918 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 69088807-554f-3e91-a9db-2f6c2cb2619f | -17.79481 | -42.5342 | 2025-08-23 04:04:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6bcf1df7-68be-3807-8fc9-bcc56f933c8b | -14.6125 | -54.81053 | 2025-08-23 04:04:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4ff90ec3-b507-3198-88ac-5bc4b48efe87 | -14.61654 | -54.84672 | 2025-08-23 04:04:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 11576156-aabd-30d2-8ea3-4562866d0983 | -20.27788 | -46.65012 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| deb16d1a-b6d7-3f27-ae5d-98707b6a66c2 | -22.42125 | -44.4968 | 2025-08-23 04:04:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 6fb00fc1-4a40-3493-8e1e-56e71eb6a7a8 | -18.86367 | -47.39086 | 2025-08-23 04:04:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ac8e53e-616b-335c-8f3c-ed6f1991911d | -19.96952 | -47.5213 | 2025-08-23 04:04:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb793e34-21af-3d6a-beed-bc77538ecd3c | -20.08754 | -47.74611 | 2025-08-23 04:04:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b688f4a4-6cb1-3986-a920-1f4e925c69e7 | -15.69942 | -48.08932 | 2025-08-23 04:04:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fea8f56a-437a-3b9a-9d73-6bce44501303 | -15.22461 | -53.8594 | 2025-08-23 04:04:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1dca5364-61be-3079-b30d-12a7cb3ee81f | -18.85977 | -41.96657 | 2025-08-23 04:04:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a5ea33df-45ed-3d55-934f-a1610c958553 | -17.26566 | -46.77241 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |


[Clique aqui para ver as próximas entradas](README33.md)
