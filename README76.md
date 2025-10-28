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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71aee8ce-2256-3585-acee-d35355b3e08e | -6.63715 | -47.19814 | 2025-10-28 05:04:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1015636c-4f96-33f2-92a3-74dac7c64e17 | -7.97754 | -46.71725 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63311e6e-8acb-39f7-82a8-ec7b883e6add | -10.94038 | -48.02852 | 2025-10-28 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5e171e4b-86e5-3315-8ff2-548e28352837 | -7.89506 | -45.69225 | 2025-10-28 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9690da5d-fe02-3a2e-93c4-c5ee1dffa94d | -9.95574 | -47.07735 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1fc7a2e4-a544-3c9a-a94e-a33cd4722692 | -13.63124 | -46.46735 | 2025-10-28 05:04:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66d7299c-7f18-33f4-b6e7-02c129090022 | -9.22127 | -46.36726 | 2025-10-28 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d31f12e-88fa-30b7-b14b-a3fb064ce3aa | -7.80654 | -46.48946 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7692a29b-79e4-3556-82af-4d6d8830a0f0 | -7.45541 | -47.15898 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb9ed9fe-d694-3469-b35f-747c34429129 | -10.5665 | -47.89697 | 2025-10-28 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff41a4ce-b400-314d-b012-34a5407fbe98 | -7.86989 | -46.40105 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92b4ad9c-345e-31ad-89b7-61f4f14b5f01 | -10.30144 | -47.2227 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1795e7c8-5e72-3ed0-8a22-fb6a824efff0 | -13.624 | -47.03627 | 2025-10-28 05:04:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fb0653c9-43bb-37a0-aab7-73095726b13a | -10.29693 | -47.21514 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7cad76c1-807f-38a6-adff-a791533656e9 | -10.242 | -52.6937 | 2025-10-28 05:04:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fec0e6fe-7905-3f76-ae07-3ddc9317eb8a | -10.93513 | -48.02862 | 2025-10-28 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b8c4a4a-ee40-3018-85ad-f5cf8854d394 | -7.94418 | -45.49969 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 44ad8e01-c4f6-3ff6-85cd-61771a5a254b | -7.97609 | -46.72766 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd766edd-735d-3f66-a4c6-dff7680ae6c1 | -13.66486 | -46.52263 | 2025-10-28 05:04:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2ea4eb2-269e-396f-b27e-d643054de812 | -10.32145 | -47.15251 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74c45d44-b9f2-3464-9af6-76533c13e6ea | -8.058 | -54.93008 | 2025-10-28 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c607c683-5e63-3166-894f-a547e7fd8f6d | -7.94634 | -45.48397 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7b61964-bd6f-3a1f-bf96-9390290e66d1 | -12.08226 | -45.64906 | 2025-10-28 05:04:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9492d64f-aa42-34e9-8c62-67dc0829c721 | -10.96618 | -47.82646 | 2025-10-28 05:04:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee327309-a296-3233-a8de-56235ac1d3af | -10.32189 | -47.14904 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57b08f65-d289-3cbb-b0da-28de498b534c | -9.55345 | -46.97202 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cdf919f6-ed4f-377b-b500-2b340e0031cd | -7.47186 | -47.15504 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9707bf1c-3b68-30fd-b178-199dc99eed72 | -12.61778 | -44.25148 | 2025-10-28 05:04:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43fc66a3-b3fd-3486-820c-7f343376aec9 | -6.22142 | -55.63785 | 2025-10-28 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 348f80d9-5ae5-3dfa-8cdf-66539893a3e3 | -11.15821 | -47.78702 | 2025-10-28 05:04:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c14bab46-dcf3-326b-9040-ffa06d76eee7 | -8.1884 | -44.44324 | 2025-10-28 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8b71aa41-d54c-37ad-9471-fb070e4bb247 | -8.10259 | -55.07875 | 2025-10-28 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79ef9baf-9da3-3bb5-8885-8c23b735de81 | -8.0389 | -45.14227 | 2025-10-28 05:04:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6eb7d0d9-d9ee-342a-8714-144fd2b966ce | -7.81514 | -46.43375 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41367d70-ac1f-3176-a7df-be3ab8468938 | -10.92234 | -50.26959 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b23baf8f-0930-30e4-8031-7107d73054a8 | -10.93446 | -47.65944 | 2025-10-28 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04df9197-47f4-3895-989c-993c824d2bd8 | -12.97707 | -48.39309 | 2025-10-28 05:04:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 616c379c-286d-3811-90ee-086e8cd44ffa | -7.97515 | -46.73442 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe077fd1-6627-3dcb-bae9-60582c01398b | -9.47184 | -46.90708 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5940f09c-8d76-35e8-b156-3c420d8bf657 | -7.80998 | -46.46493 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e1b4c480-9fc8-3f22-afa5-4558decd36a9 | -13.61319 | -47.02962 | 2025-10-28 05:04:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2670d5cc-0364-3fb9-93ae-7bff65aa469b | -10.29285 | -47.20411 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c40b71aa-e2ac-391f-8061-3059465c62c2 | -9.46455 | -46.87754 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 78893ea6-143d-3b08-9d3b-3380a2b7f6b2 | -7.94218 | -45.51141 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0b6f51f-aa15-33e5-a5e4-bd696fbcf869 | -10.99426 | -50.36818 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eef23f04-4cc1-3dce-a327-9d3f8aec1b86 | -9.2222 | -46.36 | 2025-10-28 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f163f150-94a7-3ec8-9107-fbfff7cd2ee8 | -9.54173 | -46.97739 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb7f8ded-8c9c-3964-b4b5-4be748fb50cb | -13.30678 | -47.6921 | 2025-10-28 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5884357a-7611-3f03-b433-baaeb25a1769 | -10.89015 | -48.37919 | 2025-10-28 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f85f69f-7df2-3a7a-b00e-b6564ec2dd62 | -7.83488 | -46.41148 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 086a4ce7-6bde-36cc-a303-7d06b4cc38a5 | -7.32491 | -47.21414 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 60688519-cfa7-3707-af59-9cdbddd20293 | -9.41676 | -49.33145 | 2025-10-28 05:04:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29f90685-da42-3ed5-b64d-e276e4255c6e | -12.23845 | -46.52508 | 2025-10-28 05:04:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dc9ac2a-afb7-3d6e-b946-1da01a55bd69 | -7.95439 | -45.50898 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0f71dea6-3312-3523-a781-cf4de4444034 | -9.95676 | -47.11298 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f98d3c5e-7adb-3e38-953e-22275e3b84b3 | -10.85932 | -47.91042 | 2025-10-28 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a288bfa6-0a73-3336-8dca-1a8cf59e585c | -10.93059 | -50.27521 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8430839-3799-3e13-8f83-803ab44bec4e | -9.96439 | -47.09611 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7dc0c7a5-9cf4-3e92-96bf-3fe5a4e69280 | -10.3475 | -48.05275 | 2025-10-28 05:04:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe074fa5-e231-352f-a84e-61777bb57790 | -9.14457 | -51.30016 | 2025-10-28 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ded66831-bd4c-36dd-a76d-981bbbe2ae90 | -7.97277 | -46.75147 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dea66bb4-1512-3b2e-82c8-08853d4572de | -10.91803 | -50.27033 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2fa7d006-2f39-3bd1-8f08-ba0e3b7469c3 | -10.563 | -49.80509 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a708fda5-16af-322d-a94e-e8215f56ea43 | -9.53642 | -46.9627 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0262d105-4584-3410-903a-03885a1deff9 | -11.28153 | -45.51793 | 2025-10-28 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 002107b2-ed46-30a6-a95a-31d7b576a922 | -13.3676 | -47.41198 | 2025-10-28 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 56a7e143-a778-3276-8c69-586b35e1669b | -10.72363 | -48.13179 | 2025-10-28 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c10d3c2-91e2-3ae6-93ca-a56e2ad7d457 | -12.698 | -46.32288 | 2025-10-28 05:04:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ef8eea3b-c92e-3fcf-86f2-9b2d6b5928bf | -10.99486 | -50.36388 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0fdb7ca-4031-3b16-83b2-a16dfa983b5e | -10.67554 | -47.27147 | 2025-10-28 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f40c47a3-327a-39fc-8438-5600d266b6a5 | -13.03593 | -45.85627 | 2025-10-28 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08144311-4484-3917-9e33-9bed26dc39e6 | -12.07685 | -46.39868 | 2025-10-28 05:04:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6faae308-664b-3822-a989-f8430e82568b | -10.78478 | -49.26033 | 2025-10-28 05:04:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3cdc2be0-3c5c-3c4d-b5d0-3e3fd830b01c | -7.5088 | -46.28725 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba0dc165-d0fe-3f11-ba60-cfbefc77f00b | -7.61307 | -46.47306 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8e549f7d-3f49-3118-8b1f-da7df689631b | -13.55751 | -47.16471 | 2025-10-28 05:04:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dc41e5dc-4a10-37fb-91c9-e4fd367ebc48 | -7.94474 | -45.49559 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 742abc3f-209a-36f5-9f0d-267b65920795 | -9.91589 | -47.68382 | 2025-10-28 05:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae134820-a058-316a-a1e8-da176afe62d9 | -10.22339 | -49.89975 | 2025-10-28 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66988de7-2340-3474-80db-8918496c908c | -6.97608 | -47.33464 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 484867dc-0b3d-3bcb-ac8e-0d8be43d85b2 | -12.19982 | -46.50406 | 2025-10-28 05:04:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8dad072-2d0a-3660-afc6-2909a343d991 | -10.22079 | -49.90166 | 2025-10-28 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad36b17f-1bbe-37f4-9a61-b0e8b7ee1a04 | -7.95329 | -45.51733 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a05e3c6-c072-3890-b1d5-bf477db24aac | -12.08782 | -45.65453 | 2025-10-28 05:04:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 78a2ec63-0e0a-31d9-9727-7697bb5fadd9 | -9.22068 | -50.20814 | 2025-10-28 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ca11315-bb89-32f6-9ca9-f61eadac829e | -8.57047 | -47.03057 | 2025-10-28 05:04:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ba4b5b5-5812-3eb3-b707-70c26a0bdab9 | -9.55887 | -46.97282 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03cef639-3a4f-3604-944a-42fedca588a3 | -7.78959 | -46.4511 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3129c524-e8ab-3ced-8c9c-6fe66529bd6f | -5.6529 | -51.10395 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 322ee60b-84cd-3c08-a51b-9364abf90d8c | -7.93597 | -55.01648 | 2025-10-28 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 971509bb-a1f2-3db0-be26-5f752aef135c | -7.81092 | -46.46555 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b34540c3-6383-31bb-9e59-4be7f1eee00f | -13.26208 | -47.73016 | 2025-10-28 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f403a566-f022-3602-b9b4-4aa1e5368b51 | -9.87012 | -47.46269 | 2025-10-28 05:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4826f1c-f432-32ad-a5c8-3239ece03125 | -7.45509 | -49.40395 | 2025-10-28 05:04:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6ef5b60c-490d-376c-b9bf-1ef4467cf7ef | -7.25834 | -45.00183 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8f147fbd-5cdb-3aaf-af81-2cbff419a1ef | -7.47142 | -47.1582 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3488bb7-53ba-3390-8644-be6d14da2afe | -7.45445 | -49.40836 | 2025-10-28 05:04:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 141d892f-b50a-323f-9f88-82440cb2ef4e | -7.96963 | -46.75534 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aeb457f8-d7a3-3b95-b753-3f2f7f93d76d | -7.83991 | -46.41568 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f038e1d3-7913-358a-bb65-ad3d41d72720 | -7.46534 | -47.16373 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README77.md)
