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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d14531b2-8813-3fdb-ac64-b792efdda620 | -11.2657 | -51.3898 | 2024-10-07 01:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 91908f65-80a0-353d-a4c2-f58964638481 | -11.2844 | -51.409 | 2024-10-07 01:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 20e33fea-503e-384c-b482-42365620d1c9 | -11.2847 | -51.3878 | 2024-10-07 01:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 38aec132-9248-3a25-adee-315da40b880a | -11.2583 | -60.3885 | 2024-10-07 01:16:10 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 62.6 |
| dca67687-f9a6-38ad-9647-91d93a73d636 | -11.2585 | -60.3691 | 2024-10-07 01:16:10 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| dde822f2-8bec-3a5b-bf49-a1d27714df2c | -12.0585 | -63.7841 | 2024-10-07 01:16:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 69.6 |
| d5cb2879-e24a-31ec-a868-18a1742a9471 | -12.7089 | -40.2155 | 2024-10-07 01:16:17 | GOES-16 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 60.2 |
| b153448e-630b-3e07-a7d8-54dd855e4729 | -13.5911 | -50.3197 | 2024-10-07 01:16:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 91.7 |
| cac9e526-3f9b-3954-8b9b-777e1814c6a1 | -13.5915 | -50.298 | 2024-10-07 01:16:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 105.1 |
| a8000bfc-570f-30ae-afa7-6077aac39013 | -16.6195 | -55.5892 | 2024-10-07 01:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 65.1 |
| c3f72a37-a4c6-3551-b9ea-5f2bec21b228 | -16.6199 | -55.5684 | 2024-10-07 01:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.4 |
| 7119253b-d86b-3eb3-8b20-60970ddce6c3 | -16.992 | -56.721 | 2024-10-07 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.8 |
| 0c875158-9e7f-3b80-9224-42c2ab1d23a6 | -16.9924 | -56.7003 | 2024-10-07 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.6 |
| 23a9ae9e-a71c-321f-aae4-00a07d2513b6 | -17.0116 | -56.7186 | 2024-10-07 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.1 |
| caac638c-4477-39aa-a0e4-345aadf56e02 | -17.012 | -56.698 | 2024-10-07 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.5 |
| 13084822-6438-3bed-b46e-e1059b77e802 | -17.0123 | -56.6773 | 2024-10-07 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.6 |
| d9add511-5d80-350d-bf8c-d84ec8fdf5a3 | -17.1581 | -57.3582 | 2024-10-07 01:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.1 |
| a90f03d0-40e0-31f1-bf46-ea4d71ce2ca3 | -17.1584 | -57.3377 | 2024-10-07 01:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 131.5 |
| c61988c6-7a92-32f1-b723-cb24e48e2d5a | -17.6279 | -53.1094 | 2024-10-07 01:16:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 1c548813-8f28-367e-a3b6-b3e1d86c7692 | -17.6283 | -53.088 | 2024-10-07 01:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 108.1 |
| a9056c14-3425-38bd-a401-47eee708695b | -17.6481 | -53.0849 | 2024-10-07 01:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 33f7db88-c67f-3d88-8852-b3333ea965bb | -17.6679 | -53.0819 | 2024-10-07 01:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 141.9 |
| c5d92ab8-5073-3707-9f6a-0ad4b90c224c | -18.4518 | -53.5165 | 2024-10-07 01:16:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 9c8ef590-0ff3-33d9-a0f7-409101543853 | -18.4718 | -53.5134 | 2024-10-07 01:16:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 73ded072-c978-3547-9ecf-95ea10854e9d | -18.4722 | -53.4919 | 2024-10-07 01:16:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 39.5 |
| e72db0ef-d7ec-3837-8a0b-e99ba6c032aa | -18.6391 | -57.2578 | 2024-10-07 01:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.2 |
| 440ed10e-22cd-39cb-bc92-76ecbb45c7eb | -18.659 | -57.2552 | 2024-10-07 01:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.6 |
| d82671e7-d333-3d68-9584-c978c855d0ca | -18.8686 | -54.5617 | 2024-10-07 01:16:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 7143a8a5-c942-33a5-82b1-e9142b50e96c | -19.8112 | -42.36 | 2024-10-07 01:16:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 149.0 |
| e4593542-727f-31ae-a44e-42791aba0a3f | -19.8318 | -42.3542 | 2024-10-07 01:16:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 195.6 |
| babc2924-875c-3fe2-8e9f-1de5c5b808f6 | -19.8838 | -42.641 | 2024-10-07 01:16:55 | GOES-16 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 91.9 |
| 4e3dee19-7ccd-39f6-83fe-2ce89a3e82e6 | -19.9044 | -42.6353 | 2024-10-07 01:16:55 | GOES-16 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.4 |
| ffc621a9-a5f6-3bb6-aa55-a91c810e2857 | -20.4456 | -47.664 | 2024-10-07 01:16:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 129.1 |
| de5278e2-b159-323f-a609-fa11f4c5b094 | -20.4655 | -47.6827 | 2024-10-07 01:16:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 7fc26813-d957-3d9f-a90a-27cf8d25658f | -20.4661 | -47.6592 | 2024-10-07 01:16:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 435.4 |
| 1da6e2f7-f450-318b-b8d9-f1f1eb935d23 | -20.4668 | -47.6357 | 2024-10-07 01:16:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 130.6 |
| f5fc999d-80d5-3031-b7cf-448243ef7ed5 | -20.4866 | -47.6544 | 2024-10-07 01:16:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 209.7 |
| 5118bff7-358a-397b-b551-4be2aa557a50 | -20.4873 | -47.6309 | 2024-10-07 01:16:59 | GOES-16 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 57b2a888-667a-3efc-ab8f-dcfb272d9a80 | -20.5855 | -48.4904 | 2024-10-07 01:17:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 8f21fd5e-b365-328a-b38a-ac20593ccc86 | -20.606 | -48.4858 | 2024-10-07 01:17:00 | GOES-16 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 444b77f6-5b47-31e7-a7e2-c566d0419ba7 | -21.0031 | -46.0863 | 2024-10-07 01:17:02 | GOES-16 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.8 |
| a7b2f5aa-7f4e-32ad-a93c-1f792942f657 | -21.0705 | -47.2568 | 2024-10-07 01:17:02 | GOES-16 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 726f853c-8daa-379e-9662-cbfab81e717d | -21.0712 | -47.2331 | 2024-10-07 01:17:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 212.1 |
| 739fa482-49cf-37fd-b38a-82615143dea3 | -21.0719 | -47.2094 | 2024-10-07 01:17:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 3a2da644-0a8a-3d38-a165-0db2ae9b6195 | -21.0912 | -47.2518 | 2024-10-07 01:17:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 806309e4-b53c-34f5-ae9c-ef90bdb64581 | -21.0919 | -47.228 | 2024-10-07 01:17:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 229.0 |
| 49a79df3-4ee4-326a-8c59-4c79d7c84be5 | -21.0926 | -47.2043 | 2024-10-07 01:17:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 69.3 |
| a2681cbc-fcc7-39c4-a8e2-e445ae1bc5cd | -21.3575 | -50.1516 | 2024-10-07 01:17:04 | GOES-16 | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.5 |
| 8ae02128-0894-380f-873f-c14251a8204a | -21.3582 | -50.1287 | 2024-10-07 01:17:04 | GOES-16 | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 119.2 |
| 96b7d700-02b6-3837-b339-2196f8fab127 | -21.5843 | -47.9536 | 2024-10-07 01:17:05 | GOES-16 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 0907d2ac-4dce-3ede-bc73-30efc31389f3 | -21.585 | -47.93 | 2024-10-07 01:17:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 72d3a212-4b08-3684-92e3-31da0500ed97 | -21.605 | -47.9485 | 2024-10-07 01:17:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 465b2329-4820-3489-81b4-e2df8d3c6136 | -21.6529 | -47.7255 | 2024-10-07 01:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 61.7 |
| c72abdc6-6929-307c-821f-f503124b117c | -22.1974 | -48.1778 | 2024-10-07 01:17:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 534d1927-3e05-3b4f-ac54-ed0f49b783ce | -23.151899 | -45.528999 | 2024-10-07 01:18:29 | METOP-C | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d6cc7169-f2af-3d24-9360-1e1e062953fe | -23.156099 | -45.5443 | 2024-10-07 01:18:29 | METOP-C | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 94de3827-9f4d-38f2-b94a-0ed70f6b61a6 | -23.4403 | -47.044899 | 2024-10-07 01:18:31 | METOP-C | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c9b5d394-0abd-302d-b68c-76f776bc0268 | -23.437099 | -47.0326 | 2024-10-07 01:18:31 | METOP-C | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a821f9d8-43c6-30cf-b2c1-0d9d43b388b2 | -22.943001 | -48.561901 | 2024-10-07 01:18:45 | METOP-C | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 108c0acd-b153-39f6-9ccf-1d009552bc80 | -22.933399 | -48.564701 | 2024-10-07 01:18:45 | METOP-C | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 07478e89-683b-3e0b-be13-abfe3bdf8ce9 | -22.940399 | -48.551601 | 2024-10-07 01:18:45 | METOP-C | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e56800bf-b19a-3c70-aa8b-b8d84be5e1a7 | -22.930799 | -48.554401 | 2024-10-07 01:18:45 | METOP-C | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 151dad4c-fc9f-366d-8d74-b49930ee3542 | -23.145399 | -49.806702 | 2024-10-07 01:18:47 | METOP-C | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1261d3cd-2dcb-39c0-ac48-d1a1f9f4763b | -23.038601 | -49.836601 | 2024-10-07 01:18:49 | METOP-C | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b850beec-2546-3d85-91df-127a4cd03683 | -23.040701 | -49.8456 | 2024-10-07 01:18:49 | METOP-C | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 09064ffc-5301-355b-88cd-230a7014d785 | -22.476101 | -48.3587 | 2024-10-07 01:18:52 | METOP-C | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6ea3c67a-96f0-380a-9e75-b126ec34e6fd | -22.3734 | -48.570599 | 2024-10-07 01:18:54 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a6a4f3e0-7c0f-3ba2-8d12-eee0dfc8a3c6 | -22.376101 | -48.5811 | 2024-10-07 01:18:54 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| efbbb65d-acbe-3b2f-a588-e964d67d02f7 | -22.3787 | -48.591499 | 2024-10-07 01:18:54 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c63088be-0b0a-3640-9bc4-5737a1479659 | -23.1035 | -51.607201 | 2024-10-07 01:18:54 | METOP-C | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8ad4d260-d1a4-352d-bba7-159fe6bb6f4d | -22.206301 | -48.156101 | 2024-10-07 01:18:55 | METOP-C | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fecf286f-ce04-3ce5-ae6a-d7c8bf7fafb0 | -22.209101 | -48.167099 | 2024-10-07 01:18:55 | METOP-C | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 73e5ce29-f866-388d-a874-3b6e9dd3ba34 | -22.3664 | -48.5839 | 2024-10-07 01:18:55 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 27183379-f5ae-34fc-9a50-b3030e009462 | -22.1966 | -48.158901 | 2024-10-07 01:18:56 | METOP-C | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d17439d6-318e-3048-8500-19f373c57490 | -22.1994 | -48.169899 | 2024-10-07 01:18:56 | METOP-C | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b90e9d64-5fae-3e05-8705-eb576c832fb3 | -22.187 | -48.161701 | 2024-10-07 01:18:56 | METOP-C | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5053c44e-ef5b-3e6c-96bb-bda0ec27d61c | -22.1898 | -48.172699 | 2024-10-07 01:18:56 | METOP-C | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 547f5597-4a56-3c19-b4cd-b11e49a39e5b | -21.655199 | -47.7103 | 2024-10-07 01:19:02 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 591f127b-b453-3d35-86f4-c5cd59bfddfb | -21.658199 | -47.722198 | 2024-10-07 01:19:02 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b2596256-2f71-302f-9740-321875955ec7 | -21.642401 | -47.701199 | 2024-10-07 01:19:03 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 234d6485-3e72-36f5-a29b-e33b9591fb40 | -21.6455 | -47.7132 | 2024-10-07 01:19:03 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| aa3e4633-5543-3872-a9ee-42e1cf67955a | -21.6485 | -47.725101 | 2024-10-07 01:19:03 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 25735013-f436-3686-8ca3-a64f3c83f9f9 | -21.632799 | -47.703999 | 2024-10-07 01:19:03 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4a8ea448-8dd5-342c-84f7-b01f2b0c7f4d | -21.6359 | -47.716 | 2024-10-07 01:19:03 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ca074d93-2c11-3a0a-9efd-35b58b4fb8ae | -21.6262 | -47.718899 | 2024-10-07 01:19:03 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 43b181bb-742f-3d2f-b597-e2b2b7973411 | -21.616501 | -47.721699 | 2024-10-07 01:19:03 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d1c1fd78-39b1-3887-8b02-e90d32069903 | -21.6007 | -47.7005 | 2024-10-07 01:19:03 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 87b6457e-a54b-3293-8ed9-e25dab3c6345 | -21.6038 | -47.712502 | 2024-10-07 01:19:03 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 713199e6-6015-3059-80b9-3664ed0b2298 | -21.591 | -47.7034 | 2024-10-07 01:19:03 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| cd5977d0-3ef7-3f96-99d3-26fb1e8ea09f | -21.594101 | -47.715401 | 2024-10-07 01:19:03 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b2902550-db2d-3012-8edf-3ffcf1ce8403 | -21.5972 | -47.727402 | 2024-10-07 01:19:03 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| aa8ef144-ce03-3ff7-a7bd-0d548e1f532a | -21.5877 | -47.9333 | 2024-10-07 01:19:04 | METOP-C | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 62fbbbe4-5e8d-3b3d-90d7-edc84c674d47 | -21.5907 | -47.945 | 2024-10-07 01:19:04 | METOP-C | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9e3b8759-e118-305b-bf28-276e2c9bd692 | -21.5937 | -47.9566 | 2024-10-07 01:19:04 | METOP-C | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e154224d-0083-3b07-9415-462570dd7aff | -21.581301 | -47.7062 | 2024-10-07 01:19:04 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4aad33ad-6af3-3aea-a185-459c3567f60f | -21.5844 | -47.718201 | 2024-10-07 01:19:04 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 38bfd111-dd47-3b5c-8d27-a9efbf9d24bb | -21.5875 | -47.730202 | 2024-10-07 01:19:04 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e30a848a-f835-306f-a89e-2fc1c2d4d059 | -21.5716 | -47.709099 | 2024-10-07 01:19:04 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 83b56904-3267-35fe-aad5-eca4d1246b06 | -21.574699 | -47.7211 | 2024-10-07 01:19:04 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b3337f24-a4b9-3901-a607-7900a45777c2 | -21.577801 | -47.733101 | 2024-10-07 01:19:04 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README16.md)
