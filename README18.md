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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfc6abd5-b719-3f23-8bfa-d5f669bd887b | -12.47584 | -54.47829 | 2025-05-23 05:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c9e6fcfb-f0f2-33e5-99cc-f7c52c166367 | -12.29368 | -52.49041 | 2025-05-23 05:18:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3e74f322-dc3d-3893-8950-c3841ccd3ce8 | -12.72443 | -54.97515 | 2025-05-23 05:18:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aa77fb98-f879-338d-b858-4146bb4976ab | -14.0188 | -55.13424 | 2025-05-23 05:18:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6da3f4cd-082d-352e-ae75-a749d9a084a6 | -12.33545 | -49.99375 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c16cccd5-39af-3789-a402-0d6fd8649105 | -13.987 | -56.02428 | 2025-05-23 05:18:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa15a00f-60e9-3cde-af0c-fd91aa95f7ca | -11.80677 | -57.36119 | 2025-05-23 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5e5b3833-aca1-362c-b64a-95eb2902e00d | -13.98052 | -56.01311 | 2025-05-23 05:18:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| dbe0d077-7a3f-3801-9113-16987dc67044 | -12.302 | -52.50258 | 2025-05-23 05:18:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c05e0908-79a1-3fff-b440-b95e3b030f97 | -10.30127 | -57.14232 | 2025-05-23 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14b3fbce-3404-3d79-b5ab-e20d1c7f87c9 | -12.8401 | -47.39365 | 2025-05-23 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 029b9e51-ee58-3ced-aa92-07a83023f1e6 | -11.51775 | -48.55817 | 2025-05-23 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2e1d754-3212-3269-9514-7e9a36c8e171 | -12.84687 | -47.39443 | 2025-05-23 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f213f8c8-6af8-3153-ab1d-115f2630702c | -10.75808 | -54.77551 | 2025-05-23 05:18:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 33565177-e725-32a8-a72e-f9df53da593f | -9.29282 | -57.55476 | 2025-05-23 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3da6533d-6e93-3692-a2fc-a6e560394976 | -11.30869 | -54.02327 | 2025-05-23 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52489eaa-ff51-3bf5-b0df-a69cd53f5bd8 | -10.8212 | -56.95256 | 2025-05-23 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb164052-15a5-3d11-95b2-b4c6b142aacb | -12.33373 | -49.99232 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5b90056b-a38d-315d-adb6-2f7b1ee075e4 | -12.293 | -52.49584 | 2025-05-23 05:18:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6d9e53eb-6ca9-3c7c-a60e-baeed59fd163 | -14.03071 | -55.13997 | 2025-05-23 05:18:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d08a027d-47d7-349c-8ac4-fe60d44deb6f | -12.42467 | -49.97704 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 678d40cc-e7e6-3f9b-960c-dbdaf085ae65 | -12.39454 | -49.98572 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f0e4076-fc96-37f2-a786-15f7649b3602 | -12.28816 | -52.49516 | 2025-05-23 05:18:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ad0fc7a9-88f5-3d50-9c0a-4be829c1de5b | -14.06966 | -57.10458 | 2025-05-23 05:18:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 90a9faf8-9628-3c9a-8fce-142eb45da002 | -9.85524 | -59.94575 | 2025-05-23 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e1430ff-d660-3f04-9f66-e039c9522c8d | -11.75103 | -54.72068 | 2025-05-23 05:18:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 361310b4-0e17-3fd9-9c9b-d6d9d80aeaf4 | -11.29722 | -53.97934 | 2025-05-23 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c92e1da-364f-3eac-a219-362bd0b0a291 | -14.02657 | -55.13937 | 2025-05-23 05:18:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea845837-0306-3f6c-9521-0111631df8bd | -11.7469 | -54.7201 | 2025-05-23 05:18:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6fd22f4-5897-3ab1-badc-93f009434cc4 | -10.7184 | -48.82804 | 2025-05-23 05:18:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44204e4b-6178-3100-85c7-5ee102a4f687 | -10.31284 | -59.56598 | 2025-05-23 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7eab8341-72db-3d57-a47f-369add89cfc3 | -14.02708 | -55.13548 | 2025-05-23 05:18:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50f929c0-e1d1-3740-81b6-2c4989829e86 | -9.42066 | -58.31245 | 2025-05-23 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 389a99bc-d70b-3234-b92b-d60c83b7c04b | -10.6962 | -59.10913 | 2025-05-23 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ea6f83e-79f1-323c-b297-ee47bc958034 | -13.94145 | -54.48608 | 2025-05-23 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 331c68de-26a6-312e-b4a0-43fd28f5532a | -10.75403 | -54.77488 | 2025-05-23 05:18:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fef363d-7af4-313d-b5dd-81f465fb12fe | -11.55877 | -47.45736 | 2025-05-23 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7e5b7866-cd63-3ccc-87f8-58d3be71b5da | -12.13648 | -54.65872 | 2025-05-23 05:18:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e907e0a6-5e5c-3586-addb-ff391628d2b5 | -11.56285 | -47.46199 | 2025-05-23 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5b57b51-3154-36df-9b77-9568a9e6113e | -13.09914 | -52.2881 | 2025-05-23 05:18:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc446c32-b71d-33e9-8a99-702325a9b1e7 | -12.06478 | -47.3449 | 2025-05-23 05:18:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53e23045-6012-31b3-8ea7-f42997fb0428 | -12.3285 | -49.98745 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7ac8ec3e-df90-3857-a8ac-87398b9bc7a6 | -13.78195 | -54.30826 | 2025-05-23 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 18cec445-9e63-39d3-a3e2-fc44333748bc | -12.0782 | -47.34689 | 2025-05-23 05:18:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0e4231de-bb36-3f74-ab4d-5928532d98f9 | -11.81087 | -57.35861 | 2025-05-23 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 26531241-6d87-3fbe-9412-7c78cade9e38 | -11.56415 | -47.44995 | 2025-05-23 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b11aacba-a73f-3504-afd9-e8b4cdb1c5a7 | -14.04051 | -53.37387 | 2025-05-23 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2eecd55e-1a25-3cd4-b86e-131b771ee869 | -11.55751 | -47.4491 | 2025-05-23 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4d292265-a630-335e-a0fe-98c11a461a85 | -12.02989 | -57.09718 | 2025-05-23 05:18:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 754ac9d9-88e7-3fd7-81c4-be60642f6b31 | -12.07216 | -47.33981 | 2025-05-23 05:18:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9afb18f9-1b90-362d-9fc5-531e9d29b197 | -13.75381 | -58.59011 | 2025-05-23 05:18:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 117aa3e7-be6e-3c96-9a39-ab8f18be4ccd | -12.29716 | -52.50192 | 2025-05-23 05:18:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d99f824e-804f-36de-af9a-94918c92e172 | -12.30131 | -52.508 | 2025-05-23 05:18:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb7cb654-838d-3ae1-981c-f9630752c482 | -14.04391 | -53.38454 | 2025-05-23 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93796d7f-7b5d-32ea-8d4d-b18ac7eef371 | -13.18306 | -53.57434 | 2025-05-23 05:18:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a49b6990-f3c2-39cb-857c-4298dc57f6cd | -13.18368 | -53.56964 | 2025-05-23 05:18:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1fd1c85-3bac-3b26-9758-73e2c272cdee | -12.85429 | -47.38895 | 2025-05-23 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8dd5c9cf-65a5-3e2d-826b-df912907f6ad | -11.80672 | -57.36216 | 2025-05-23 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1c253d95-fb8b-3325-bb77-4dd2d2dff9ea | -12.47321 | -54.46562 | 2025-05-23 05:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a667b34-c5a5-38c8-b4cb-7f52bd27f8cb | -11.29609 | -53.98753 | 2025-05-23 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 53d90ddc-739c-38a2-aff2-dd41078c24c2 | -13.98769 | -56.01918 | 2025-05-23 05:18:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fce9e45d-f780-3da0-b1b5-dcf602e5d3b1 | -10.68223 | -57.59521 | 2025-05-23 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d7baa70-f063-317a-a1f6-91a542fa2bbb | -10.75454 | -54.77127 | 2025-05-23 05:18:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a73f9f99-d1fc-388d-9c87-e40381d5b2da | -12.28748 | -52.50057 | 2025-05-23 05:18:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc5c370f-6cb0-3e70-bcbd-475af1eca6b0 | -10.3054 | -57.13883 | 2025-05-23 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f91a0794-69f5-3612-a6e6-e827e2991785 | -13.72429 | -58.67138 | 2025-05-23 05:18:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1c8d656b-ccac-3c7d-bce3-25eb37b6969d | -11.74934 | -54.72297 | 2025-05-23 05:18:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e70dfc89-0a06-33bd-b464-6eaf563ed78d | -11.3004 | -53.98818 | 2025-05-23 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc2e345c-41e7-3901-8744-a420ab43266f | -11.65809 | -58.26097 | 2025-05-23 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 95f15daa-adde-3238-af5f-4d1295a172c5 | -11.74984 | -54.7192 | 2025-05-23 05:18:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6427c5f5-707f-3697-8c59-53136feb1f0d | -11.55944 | -47.45145 | 2025-05-23 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f18fe61-afe5-3f40-8747-842e24b8304b | -13.98907 | -56.00899 | 2025-05-23 05:18:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 134f9133-7b85-3d8e-a946-7ee2dd072beb | -13.49531 | -55.66521 | 2025-05-23 05:18:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3128f05-97af-3617-bc90-4e7202b02b78 | -11.57014 | -47.4568 | 2025-05-23 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c1284bf-4e42-3ca8-84be-f1aeba3d75a7 | -10.36974 | -57.50618 | 2025-05-23 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70bcfd46-5d93-3891-8c73-2276e1896cc7 | -10.9375 | -55.31536 | 2025-05-23 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0cd476c9-5756-3132-9cf0-a9b212875485 | -12.40026 | -49.98649 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ab4ea43-d7ab-32d5-88bc-09f2f1a19097 | -11.7505 | -54.72443 | 2025-05-23 05:18:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10b4dbb7-dce5-303f-9358-ba138ad5d33a | -14.05452 | -53.37581 | 2025-05-23 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ca75a54-1748-3d8c-8df8-026051719a41 | -13.9818 | -56.0151 | 2025-05-23 05:20:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 46.1 |
| ff79f906-79e5-3499-b470-2f59235ea2c1 | -15.39286 | -60.18406 | 2025-05-23 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8525888c-3e0d-3523-9f24-5752ce299a58 | -17.61762 | -54.17122 | 2025-05-23 05:21:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e21eeb1-7ca0-3c38-b2eb-7a35949edf92 | -20.70708 | -54.89428 | 2025-05-23 05:21:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df83d373-ff08-379e-ba8d-4ec0eb03f50c | -19.7365 | -54.51263 | 2025-05-23 05:21:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae6a65d6-5f84-3527-90aa-8b998eb1c396 | -19.79764 | -53.83215 | 2025-05-23 05:21:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a23ad411-49a9-367d-8300-72224d081f85 | -17.344 | -51.91104 | 2025-05-23 05:21:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9282dc45-6567-3a3d-8393-27977ada1395 | -16.62335 | -58.38058 | 2025-05-23 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f2f62992-f203-304f-bfd0-c3b8a4e6d5a6 | -21.60381 | -56.04268 | 2025-05-23 05:21:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 827e292f-7b1c-34d3-bb08-47a54231134d | -17.34436 | -51.90759 | 2025-05-23 05:21:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b875f2d6-5dc7-33de-bbde-38159ec81a05 | -15.39618 | -60.18459 | 2025-05-23 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e008513d-c833-360b-8db6-22cb073eb0fd | -20.95087 | -56.58953 | 2025-05-23 05:21:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 393cb9b4-f36c-32fa-86ea-2dbbf379e18c | -19.73481 | -54.50925 | 2025-05-23 05:21:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 730303a8-51cb-3e50-a1fe-e1eb1044df7a | -14.87419 | -51.98178 | 2025-05-23 05:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d499b110-5bfd-33a8-9e7f-bba6b5a89cdf | -16.02011 | -53.20186 | 2025-05-23 05:21:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff88f514-1076-341b-a457-bccbf4d6f642 | -16.28471 | -58.67238 | 2025-05-23 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 5a31737e-375a-35ab-9abf-6dfa4f70cf8d | -17.61704 | -54.17632 | 2025-05-23 05:21:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3138060c-9860-3903-a9b3-728a514d700b | -21.7196 | -55.37365 | 2025-05-23 05:21:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d0639344-8af5-37e4-80fe-c84ec4e705fa | -19.79704 | -53.83786 | 2025-05-23 05:21:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7b13c9ec-e55d-3718-b557-4d9fec4b7712 | -16.28246 | -58.67064 | 2025-05-23 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b6945fd0-9ed0-3272-81b6-44ada288fe90 | -20.8565 | -53.75277 | 2025-05-23 05:21:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |


[Clique aqui para ver as próximas entradas](README19.md)
