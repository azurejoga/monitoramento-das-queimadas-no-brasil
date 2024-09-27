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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 997e83ea-f8c7-3f42-86fe-c6788d8f3087 | -2.7236 | -46.73534 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48f29691-c342-3fee-bf8a-2a0db26a84f7 | -2.72132 | -46.72749 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 479b6bea-fee4-31b4-a43e-0b9e12eb3781 | -2.72076 | -46.73116 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5f70eeba-bf83-31d5-bdfa-c0475fc8165d | -2.71792 | -46.72696 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 598f7d81-29ed-3bd1-a579-c05559f212e3 | -2.71736 | -46.73063 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f07186ab-46d4-3d53-a75a-802bae8172fb | -2.71395 | -46.73011 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9455d1da-e958-3037-bff9-174e19a54cf9 | -2.7018 | -46.73621 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94a6ff8a-9346-350c-b39c-818351650c23 | -2.68536 | -46.72993 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77658db0-e3c6-3143-b181-f1d56e40876b | -2.44558 | -46.08422 | 2024-09-27 04:38:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd94537d-fdce-3bdd-8d69-0db862306472 | -2.38821 | -46.51931 | 2024-09-27 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9134a222-1aaa-3c5b-87cb-bfa0656250ca | -2.3859 | -46.53409 | 2024-09-27 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7b7e1e3-2abf-3340-81af-d3be26645ea0 | -2.35583 | -46.45724 | 2024-09-27 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5a28043d-322f-3c73-be0e-17ae7618215c | -2.3524 | -46.45672 | 2024-09-27 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 272c1a67-e542-3a96-adbd-dcfa4bc63f44 | -2.2685 | -46.38715 | 2024-09-27 04:38:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6cb2e64e-a22e-32b7-a680-ead3b9328815 | -2.22541 | -46.73132 | 2024-09-27 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca684c10-7d81-3f1e-b79d-d8f63e9a42f0 | -2.22484 | -46.73495 | 2024-09-27 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db5040fb-1052-343b-a4bd-a7810c8522ba | -3.31702 | -47.00832 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf80fe01-ad7b-3e8d-8a67-cf271b9b3fee | -3.22038 | -46.78848 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fde3f70d-a473-3464-b01a-5c7300524807 | -3.21697 | -46.78795 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| f651869e-0bdf-3e9a-863f-a6e13d74db10 | -3.2164 | -46.79163 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d6c74cc0-88ea-317e-a463-953cbe36a0c1 | -3.21357 | -46.78742 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 05887f23-8d8e-357b-8d15-760960e2b673 | -3.21299 | -46.79111 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8d73ad45-9c10-3e82-937b-a80b3d2d1456 | -3.15187 | -46.53064 | 2024-09-27 04:38:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d928e0d6-cda8-39e4-8239-7eb78cc07059 | -4.4878 | -46.31133 | 2024-09-27 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5d2947d9-1f62-3dc4-b046-73152006a228 | -4.48719 | -46.31532 | 2024-09-27 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a1f89648-cd8f-3a6e-ae2a-dd424c03f873 | -4.48429 | -46.31078 | 2024-09-27 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2a06f0ff-1ec3-327d-a149-af324f526049 | -4.48368 | -46.31475 | 2024-09-27 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 80ac9458-df18-3e7b-abde-5c22fde5d0ba | -4.48078 | -46.31023 | 2024-09-27 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d53dc5b5-b7dd-3040-8e6c-2ae26ca137a4 | -4.3868 | -46.55032 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27e5d85d-a4db-3c0e-83fa-c109b29f87d1 | -4.15734 | -47.20341 | 2024-09-27 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 96f3d9f0-d460-3e7a-b0b2-65eb117daf14 | -4.15396 | -47.20288 | 2024-09-27 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 71680923-ba94-3524-9d5d-f982348308a6 | -4.14278 | -46.43203 | 2024-09-27 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea8599aa-b103-3960-8e8a-9783a2fb6bb4 | -4.13707 | -46.69283 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e62ed1aa-4811-30d1-8bcc-fb3b177ddef1 | -4.1365 | -46.69658 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4ea89251-0d6c-39fb-b4ac-9621e91ba75f | -4.13419 | -46.68861 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e270b966-cfa0-3af3-9d97-9846564557c7 | -4.13362 | -46.69235 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 09bc5766-d3c1-3047-91d5-288e26f0293e | -4.13017 | -46.69187 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 26068864-a635-3b37-95f8-51ef0d87e878 | -4.12671 | -46.69139 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 105a2067-44f7-31c2-b2ec-3712e08c3b1c | -4.1136 | -46.80079 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6fd9826-5eac-3f89-b580-3f19299118a6 | -4.11016 | -46.8003 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 327d33de-40eb-3c74-a36b-e6a3564e57ae | -4.10959 | -46.80406 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbc67e14-30d0-3375-9f9b-526d4c6354bf | -4.10902 | -46.80778 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75bc6898-1844-3adc-8af4-1f272ea7a8f0 | -4.10676 | -46.79996 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 24a5713a-3872-3957-878b-c70615e28446 | -4.10673 | -46.7998 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dcbad984-8878-3c11-9556-7e7b32851418 | -4.10617 | -46.80373 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8f3676bb-89fd-3162-bdf9-8b98a297239c | -4.10615 | -46.80359 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7fda0bf-94b4-3d7d-a873-66716fb01bee | -4.10559 | -46.80745 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fbb1d423-39fa-3d36-9bae-948211b9fc04 | -4.10559 | -46.8073 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d738db0-d71a-3cee-b0fa-5ccd98d2dfd3 | -4.90736 | -47.39132 | 2024-09-27 04:38:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe29b052-610a-3c8d-9933-5fb6fa190335 | -4.86856 | -47.00184 | 2024-09-27 04:38:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| edbe2a3c-60c8-33f2-95e2-ae37fb9898a1 | -4.84359 | -47.69497 | 2024-09-27 04:38:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75fefb73-94d3-3669-b9dd-670a1ed2a062 | -3.92331 | -46.44428 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d71d7158-3597-39a1-8031-f9a3fd2d76a2 | -3.92104 | -46.43603 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36240235-e7aa-311b-89a5-8b6e9bedcf1e | -3.91984 | -46.44374 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 72c43b6d-69d0-30bb-a031-89356c5d9f65 | -3.91924 | -46.44759 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| da49931a-3c0c-35da-893c-5b175c4ac0e1 | -3.91865 | -46.45144 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fe34f72-f18e-36de-8ba4-6aa35ff4c178 | -3.91805 | -46.45527 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7ab2c54-8d7e-3be9-b567-7a48a114fe47 | -3.91756 | -46.43552 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 278586be-a2af-381b-a9aa-f7a415304696 | -3.91696 | -46.43937 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22de34ef-8be1-3c0d-8118-fbb143fb73c2 | -3.91637 | -46.44322 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 138d996b-fb17-34e4-a7a7-1597e6bfe6dc | -3.91518 | -46.4509 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a8c2c0d8-6f7c-357e-9336-6a19523f76b9 | -3.91458 | -46.45473 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 37b5c6ab-8c47-3b1f-9ec8-a7baa8ae3b09 | -3.91408 | -46.435 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e31c5d9-f6bc-31a4-b007-928661f8ea06 | -3.91399 | -46.45857 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 141e8337-a796-3695-81db-8f2cc4f72cab | -3.91349 | -46.43885 | 2024-09-27 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 552f338c-f31c-3672-9cb4-2f70191a6028 | -4.04917 | -47.62384 | 2024-09-27 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8c9c962-2858-3304-8b2a-26283e5d36e1 | -5.83894 | -47.67786 | 2024-09-27 04:38:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a083f2a-c943-3917-a663-42a881675bec | -5.80717 | -47.0793 | 2024-09-27 04:38:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a8e7e04-8b2b-3d77-9d70-f1e8a7857bff | -5.72658 | -47.33172 | 2024-09-27 04:38:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3aca773f-2100-3205-9fef-2334f4ac33de | -5.41703 | -47.56911 | 2024-09-27 04:38:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99e4ce70-ed8c-312a-84bf-453e09c19b63 | -5.40367 | -47.53405 | 2024-09-27 04:38:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ed65b6a-23f1-3762-b55c-7c7527913a6c | -5.40029 | -47.53353 | 2024-09-27 04:38:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d67e260-2ae3-3c2d-86d3-2606247ebc9b | -5.39973 | -47.53717 | 2024-09-27 04:38:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55b764a3-a252-3f01-a140-2ac874dfd34d | -5.39691 | -47.53302 | 2024-09-27 04:38:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 284e1e60-8f3b-3664-ab54-8190350d0328 | -5.39634 | -47.53666 | 2024-09-27 04:38:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1dfa6edc-34e8-3fa5-b207-c9c4ab7705c9 | -5.38225 | -47.51592 | 2024-09-27 04:38:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3837e498-1df4-3b56-8c8d-82e323f79a1b | -5.38168 | -47.51955 | 2024-09-27 04:38:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed0a42e4-770f-3850-94df-b22f1e06d7c2 | -5.38112 | -47.52318 | 2024-09-27 04:38:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a71eb38c-5c74-3cb8-a5ef-322fc08baccd | -5.3783 | -47.51904 | 2024-09-27 04:38:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2850b5c-77bc-3a51-bcdd-d2b949ede3f2 | -5.37232 | -47.81614 | 2024-09-27 04:38:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c5476e1-b023-31c1-b0f9-ac0deaeca542 | -5.36951 | -47.81205 | 2024-09-27 04:38:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6de1898-e8b0-3e32-b30e-39d0db25994d | -1.94025 | -47.90141 | 2024-09-27 04:38:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28b7c9eb-9788-3580-a66c-bb223019d7bb | -1.7912 | -48.07161 | 2024-09-27 04:38:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c056c707-f251-3297-b936-b161786beac7 | -1.49533 | -47.70135 | 2024-09-27 04:38:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0399a596-5021-35e7-9f1a-a5102988ff37 | -2.16773 | -47.94779 | 2024-09-27 04:38:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a73fadfe-e467-3774-82a5-11885342e207 | -2.16719 | -47.95123 | 2024-09-27 04:38:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49e87032-8b0d-36c2-bb71-c91b30db0c17 | -2.16497 | -47.94384 | 2024-09-27 04:38:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e803e601-d09e-3d6c-a1ee-f178fb74f4d9 | -2.16443 | -47.94728 | 2024-09-27 04:38:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ddf6d50-e287-3fe0-9c01-8a332145d828 | -2.16389 | -47.95072 | 2024-09-27 04:38:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02623c17-b854-381c-ae8b-e0827e595634 | -3.69962 | -47.61706 | 2024-09-27 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 54a04cf9-09d1-3bf0-9155-3765d6e40b8f | -2.61239 | -48.36967 | 2024-09-27 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2eab67e7-c03b-3b71-9e32-00d59b607804 | -2.58216 | -48.21747 | 2024-09-27 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 093ec296-3399-3575-98b7-6490c893097a | -2.46138 | -47.83484 | 2024-09-27 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18851643-e277-30d8-8c36-7d7f3f024378 | -2.41879 | -48.40907 | 2024-09-27 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3cb46141-d0fc-3dae-81b3-5009c84d6662 | -2.41825 | -48.4125 | 2024-09-27 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 309366da-3785-383b-a8c7-5b4f0bed5ccc | -2.41549 | -48.40856 | 2024-09-27 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2445223d-66f5-32aa-9795-94fcfe9deada | -2.38565 | -48.51267 | 2024-09-27 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91a6c7d4-a6a3-3f37-9005-1768c3ed9f11 | -2.36088 | -47.6063 | 2024-09-27 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 8d7dca70-27c7-38b6-a293-949c950d0d63 | -2.36034 | -47.60978 | 2024-09-27 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| edc2ed97-d315-3c73-8429-93554ff831b6 | -2.3581 | -47.60231 | 2024-09-27 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |


[Clique aqui para ver as próximas entradas](README73.md)
