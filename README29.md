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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1009fd24-34b7-33a5-91ce-3f1627ceccfb | -12.61826 | -54.21542 | 2025-06-29 05:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bfefd1b9-9847-3c1c-9d6c-f2d57fe66115 | -13.14338 | -56.81001 | 2025-06-29 05:53:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 29a74f99-616f-3040-8463-00319b97b2a3 | -11.01615 | -56.25333 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d33fb308-75e4-345d-8883-f17a6b9fe6a6 | -11.03002 | -56.26621 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 65f8e6fc-a6c4-3388-a170-8846ef88ed0e | -11.0376 | -56.28712 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b321fe9d-46f0-3512-8d3f-e92b550210d1 | -10.84421 | -53.76406 | 2025-06-29 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 409f497e-1dc1-33a9-b300-d2d6ed570ab2 | -10.29715 | -57.14032 | 2025-06-29 05:53:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 75b72705-8824-39a3-b448-2e66b5ce3373 | -12.61513 | -57.8784 | 2025-06-29 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21aa1aab-4fba-3ae5-83e0-68e97b94b6e8 | -12.62776 | -54.21473 | 2025-06-29 05:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10bd07ed-2b30-3ecf-b041-3bc8d0ebf5e5 | -11.02829 | -56.28126 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7bab4ad4-5b1d-3694-8bfb-e14c94c7122b | -12.49199 | -58.47507 | 2025-06-29 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac99e8ad-0c3a-349f-ab46-817d0b6b0635 | -12.50633 | -58.35409 | 2025-06-29 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a98ada29-a575-3fbb-a6db-bb5af086c083 | -11.04704 | -55.37306 | 2025-06-29 05:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd394a02-5f71-3ade-b7b7-7c6f8fadb05b | -12.4772 | -58.47247 | 2025-06-29 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34bf2225-c559-3a67-8e56-1437d20a9183 | -10.85391 | -53.75586 | 2025-06-29 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd8350c6-c1cc-36b3-a621-d97c980d0ea4 | -11.02886 | -56.27628 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00edd5ce-a2de-3edf-b865-715d3f6b7202 | -10.84579 | -53.76243 | 2025-06-29 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| beabc097-3133-37d6-a77a-e1a5ee55540b | -11.03975 | -55.37792 | 2025-06-29 05:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c74eb3f3-36ae-3d83-9331-730ed7d90224 | -11.01166 | -56.23749 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 510e735f-8c97-3676-8980-04b59ba22b01 | -10.35038 | -57.50222 | 2025-06-29 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ca14bd1b-6d6c-3f0d-a32e-d8d5beb46d98 | -11.03119 | -56.25607 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90b9d4f5-78cd-3b7a-88b9-c5b8328b24eb | -12.60355 | -57.87675 | 2025-06-29 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d57b3213-8f14-3a96-bb32-d7513a78d201 | -10.22481 | -59.41243 | 2025-06-29 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33ca0cf4-2868-322f-b4b7-45d436728a29 | -10.29466 | -57.1394 | 2025-06-29 05:53:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c7e2fe65-0b63-3afa-9dc8-e0da3ac76814 | -12.4888 | -58.47028 | 2025-06-29 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43ebe1b1-e3cc-397f-a27c-04215db8b23d | -11.02505 | -56.28535 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15b28a21-f9f3-376d-ad2d-c34650c86ff6 | -11.05304 | -55.37961 | 2025-06-29 05:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62f97214-968c-3306-8c32-8c9ad1949cb9 | -12.62548 | -54.21634 | 2025-06-29 05:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 14992615-98f0-329e-a387-9ba5ff356f04 | -12.49244 | -58.47122 | 2025-06-29 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22002663-b324-348c-8124-d18c6785c1fe | -11.03457 | -56.28218 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e376c8c3-2c1c-3101-9085-feb663d0d522 | -10.83851 | -53.76152 | 2025-06-29 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 877f40c1-c2fd-3c89-94a7-d3a401151958 | -12.47576 | -58.46872 | 2025-06-29 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93d8f92d-ab83-3fad-ad23-ec9e02ed1ff8 | -12.50348 | -58.35349 | 2025-06-29 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c22f790-579c-3aed-a7bd-a17c4d09834d | -10.03921 | -59.36022 | 2025-06-29 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2c39d5be-bbea-31f8-8b41-76128f81adb0 | -12.48133 | -58.46948 | 2025-06-29 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2060c8c-712a-326b-9ee5-1715f7285bf7 | -11.02059 | -56.2695 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5ff66459-a204-30f4-87af-194fe498c0f4 | -12.47019 | -58.468 | 2025-06-29 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e5b5c6d-e65d-38da-8e9f-9c378d68183c | -11.01107 | -56.2424 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5bae0603-406d-3e5f-b8c0-45c96ff45197 | -11.5502 | -52.7659 | 2025-06-29 06:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| b300756e-6837-3fcb-8302-dfb030a7b980 | -11.5499 | -52.7867 | 2025-06-29 06:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| c829a3b8-b46f-3823-8b9f-4d49f5da20c8 | -11.5502 | -52.7659 | 2025-06-29 06:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 5bce1803-8cc2-35c6-a76a-e265f88bfe86 | -11.5499 | -52.7867 | 2025-06-29 06:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| f0baebbe-0c83-32fc-9e1a-a6bd8d383e1c | -9.2495 | -63.2936 | 2025-06-29 06:14:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1a2d041-bd52-3411-919d-320088c58384 | -9.2436 | -63.29295 | 2025-06-29 06:14:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18d38d7c-417c-34e2-bb86-67158d9dbe57 | -11.5502 | -52.7659 | 2025-06-29 06:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 5c4cbc77-c0c2-3c88-89ac-9bc8983517fb | -11.5499 | -52.7867 | 2025-06-29 06:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 4c7de358-a2b2-3333-8749-11fa331e26c0 | -11.5502 | -52.7659 | 2025-06-29 06:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 558b7c4e-7238-360b-93c8-45ca95800468 | -11.5499 | -52.7867 | 2025-06-29 06:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| b72449d5-ff65-3d18-bc57-d7e3e25bf282 | -11.5502 | -52.7659 | 2025-06-29 06:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 9a48a62f-33ed-3c83-93d6-987b2e6fce3c | -11.5499 | -52.7867 | 2025-06-29 06:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| e73ba474-092b-308e-bfac-7a2c89f79dfc | -11.54447 | -52.74915 | 2025-06-29 06:46:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 64f54bc3-5918-3554-801c-a0496b4f4018 | -10.29739 | -57.12277 | 2025-06-29 06:46:00 | AQUA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 560d2093-beb0-3f8a-b0cd-7aa793e46b27 | -10.55804 | -52.02652 | 2025-06-29 06:46:00 | AQUA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 5b5a256c-cbd2-3363-9673-96c7ec475d6c | -10.55434 | -52.02179 | 2025-06-29 06:46:00 | AQUA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 94bce427-2f63-3eec-af33-436f2e07ddf5 | -11.02343 | -56.26487 | 2025-06-29 06:46:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 9d679f42-13ff-32fc-8cfc-704e1fc263d3 | -11.02153 | -56.25766 | 2025-06-29 06:46:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| d6639f26-be2c-3fc4-ae5a-f5d38af99294 | -11.54045 | -52.78509 | 2025-06-29 06:46:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 5806bdbb-1f3d-3a2d-b2da-528f2fbef5fa | -11.53324 | -52.77924 | 2025-06-29 06:46:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| cd5d17c5-33a6-3947-8ca0-46d88568897a | -12.48413 | -58.46888 | 2025-06-29 06:46:00 | AQUA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d04ac2aa-a05f-3edf-b574-0ac4679df244 | -9.24757 | -63.28947 | 2025-06-29 06:46:00 | AQUA_M-M | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 626d22a3-670e-322a-9de5-344927baf993 | -11.55686 | -52.78722 | 2025-06-29 06:46:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 972e7fad-8fc8-36a4-a1f6-73f92a6d87fe | -10.34966 | -57.50306 | 2025-06-29 06:46:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 24.5 |
| ccfb0134-20e8-3feb-9d13-afb717e0e8a6 | -11.54965 | -52.78134 | 2025-06-29 06:46:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 41baf348-89eb-3a15-b2b1-5ed20d49dcee | -11.5499 | -52.7867 | 2025-06-29 06:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 28f77445-2ac4-3090-a45d-e905b0e38242 | -11.5502 | -52.7659 | 2025-06-29 06:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 893fe881-9e43-3aaf-8b8e-82ce6655ba80 | -11.5499 | -52.7867 | 2025-06-29 07:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 89da2b8a-8ba9-3ea0-9677-82dd1cf84d35 | -11.5502 | -52.7659 | 2025-06-29 07:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 42df25a2-1064-35fd-af72-02d6c0020a6b | -11.5499 | -52.7867 | 2025-06-29 07:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| d0b485ee-4749-3098-91f2-84ff27faca05 | -11.5499 | -52.7867 | 2025-06-29 07:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 6b84788e-0589-3471-9bd0-977b2c5e10c2 | -9.14768 | -46.35824 | 2025-06-29 12:27:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f693de53-218d-3a21-8530-04fdd6821cd4 | -6.84867 | -42.7971 | 2025-06-29 12:27:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.8 |
| afbd9592-80e4-3705-8501-be08f840ccc8 | -9.44056 | -47.94714 | 2025-06-29 12:27:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 251e7d74-29ea-3c7e-842b-6ecf9a59264b | -5.57837 | -45.20741 | 2025-06-29 12:27:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1979abe8-7526-3dc5-93e9-e561fb9ada00 | -6.81004 | -44.7589 | 2025-06-29 12:27:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7991394c-a66f-346c-bc97-7e37f612d6e8 | -7.17642 | -43.66608 | 2025-06-29 12:27:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 13767a85-5cc5-385b-a44a-658edeb1c6f0 | -9.15818 | -46.34989 | 2025-06-29 12:27:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6cf04b5a-aa79-3490-988c-9e32baf49150 | -6.90583 | -43.98861 | 2025-06-29 12:27:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| a632f06b-d3a5-39d2-afdd-71b358f4ed64 | -6.62821 | -47.28797 | 2025-06-29 12:27:00 | TERRA_M-T | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0ab24a7c-a509-31ca-8c0e-21765a9bd8ee | -6.74811 | -44.75528 | 2025-06-29 12:27:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 899db858-4f2c-350e-ad7d-03559d30e2e6 | -9.14439 | -45.1111 | 2025-06-29 12:27:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 582c4550-e4e0-33fb-a7cd-359e7bade379 | -6.74659 | -44.76608 | 2025-06-29 12:27:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f8f8a2aa-ff11-341f-acfd-7b728aa51373 | -6.027 | -45.02189 | 2025-06-29 12:27:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| bd797913-adfd-3f0e-9591-c37bb460f8b8 | -5.56903 | -45.20612 | 2025-06-29 12:27:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f1e60ce9-4aee-39c2-8fdf-e6cf36a1b724 | -8.01449 | -46.87704 | 2025-06-29 12:27:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 52abad6f-b4b7-3b59-bdc1-cf29b670e5e1 | -7.49443 | -45.45172 | 2025-06-29 12:27:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| a7fc39e0-7938-3005-b01b-fa2d8a083ccc | -6.62947 | -47.27914 | 2025-06-29 12:27:00 | TERRA_M-T | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 25231277-fcde-3599-81a4-84b5687f2f5d | -6.72992 | -45.53658 | 2025-06-29 12:27:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c2404be7-47b4-3985-857b-b3124dde5cd8 | -9.54071 | -50.77188 | 2025-06-29 12:29:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 7b6c42e2-257a-3849-b5c4-e52c0d49a895 | -9.5487 | -50.78389 | 2025-06-29 12:29:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 5db29bbf-893e-3c64-996a-d3c6c092c606 | -12.05752 | -48.47542 | 2025-06-29 12:29:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 302b1d02-1d14-30c7-8697-8c7139227041 | -14.66137 | -47.97964 | 2025-06-29 12:29:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bb7bed58-98ab-319f-b074-69a0cb07cd3b | -15.72852 | -49.55676 | 2025-06-29 12:29:00 | TERRA_M-T | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3e106fad-eae2-316c-8044-e7d1c287fb59 | -10.64754 | -44.49672 | 2025-06-29 12:29:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 1dc4f7d3-4c1c-3f0f-8d20-a99ba58882cf | -17.85544 | -45.98689 | 2025-06-29 12:29:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 37.3 |
| ad5da9b2-9ff6-3a6a-b0af-ce5fe27abd75 | -10.87488 | -53.76323 | 2025-06-29 12:29:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 31.8 |
| d731085c-45d3-39e8-9d81-0ee118cc2a1b | -10.98365 | -45.1073 | 2025-06-29 12:29:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 828fc883-1523-3779-a343-54a52c740284 | -17.85709 | -45.97359 | 2025-06-29 12:29:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 5b9d2d47-e0cf-3d66-b72e-5e6d157dcae2 | -10.6551 | -44.49054 | 2025-06-29 12:29:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 136.4 |
| b07a71d0-4786-3864-bf7a-4c939ec5c866 | -11.5719 | -44.82551 | 2025-06-29 12:29:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9d8a39b6-6c33-35cd-a5d8-9545c367da2f | -10.97359 | -45.1059 | 2025-06-29 12:29:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |


[Clique aqui para ver as próximas entradas](README30.md)
