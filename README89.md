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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74d6b0ac-134f-3e94-ac67-72ef9e99d987 | -10.86445 | -53.73906 | 2025-10-08 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| df3fe7ba-b903-31aa-a444-3464986e3378 | -8.58576 | -63.17312 | 2025-10-08 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 183a0a4d-c1fe-36fb-9ec8-0363f0a5e026 | -6.76734 | -63.02478 | 2025-10-08 05:29:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7055d71-c6f5-32f0-84f3-09d3cea777ee | -11.1714 | -54.88342 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8f007a72-3057-3d07-8a93-ada689882b6c | -10.91879 | -51.01771 | 2025-10-08 05:29:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a352baf3-4c03-3a15-8ba1-416a3ce5a657 | -11.75001 | -50.91511 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 23.0 |
| b6330dae-8421-3e28-ace1-4bf56178428c | -11.17236 | -54.87306 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2f5d4fc9-ada9-3b00-93be-27de341edb51 | -11.73586 | -50.92652 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 26068fda-cb76-3c20-af61-953550c84ff0 | -11.76331 | -50.91859 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| efc4c35d-7e86-344c-aca9-4d5b04282e4d | -11.42311 | -56.29113 | 2025-10-08 05:29:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 487e2ab0-f80b-302a-af34-9ea8e5e78f7a | -11.15094 | -54.88337 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cb910f9-3f1f-3d24-9104-4e88b21864f0 | -11.73134 | -50.96583 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 29b6081c-ed7a-336e-8a33-4c988a6a944d | -11.17918 | -54.90057 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df94f57b-1781-37dc-8a3d-e15a9e44d0fa | -11.18097 | -54.88614 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 2c752e18-09b8-341d-84d8-cf786b679c36 | -11.17604 | -54.88697 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| ab5e9949-5166-300c-b422-4824196f23c1 | -11.14787 | -54.86761 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6986f453-37c7-37bb-bc52-bf99f6d2856f | -11.17954 | -54.89767 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de85d4bc-5057-37bb-99e8-66fb380a47e0 | -9.33112 | -60.52976 | 2025-10-08 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1b11245-c231-3220-9e83-66a4e0e3caae | -7.59528 | -64.50111 | 2025-10-08 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb1fdfc1-ac49-3977-b059-6316da3c8724 | -6.80547 | -63.04153 | 2025-10-08 05:29:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dda6588b-1e6c-30aa-9454-4b1e10cf8bf5 | -12.32387 | -50.26324 | 2025-10-08 05:29:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 995b98b8-6e78-3d81-83c3-c9ac3b7caa64 | -10.6435 | -58.76725 | 2025-10-08 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15c70185-85d3-335e-856d-4bd1d2fb58f3 | -11.17295 | -54.87162 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3886c0a2-c1b0-3c42-8ff5-197a3066dcf6 | -12.37583 | -50.30655 | 2025-10-08 05:29:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67af03f8-1c8d-3b23-a748-62d24b86b17f | -11.74239 | -50.92736 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3f6676ef-b542-3ca1-b780-00cb150b3cb0 | -11.73632 | -50.91903 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 82e5e922-a757-3ba7-8ed3-3cced43e05b9 | -9.17057 | -59.55667 | 2025-10-08 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b18c0c60-9453-3da2-b2df-3ddcc183ca14 | -6.58887 | -58.64119 | 2025-10-08 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52144a80-585f-3da7-9717-34c6f604f1b2 | -8.03052 | -55.12878 | 2025-10-08 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87fca5ff-cf4d-3105-8a03-bf43aaeae055 | -11.15751 | -54.87224 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 014c6a56-0488-3ab2-85a5-e1daeace9dca | -7.59125 | -64.50433 | 2025-10-08 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75abdd88-7787-39f1-acad-1d908e3dba72 | -9.453 | -60.48876 | 2025-10-08 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dfbacac-a109-3f14-863b-08084d9f1e53 | -11.75808 | -50.90647 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 98dd71f3-4c08-3534-9c73-05a7749dbd52 | -11.16059 | -54.88781 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09aaa60c-231d-3e52-a121-5338531026f0 | -6.40534 | -62.85941 | 2025-10-08 05:29:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2b292ed-20c3-3965-952b-caff35833e67 | -11.16832 | -54.86788 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06f3490e-d8ee-31b2-b0d7-1df13690c7a4 | -11.17776 | -54.87079 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8faad8c-b92f-3ab3-8aed-8af6479e390d | -11.14208 | -54.87282 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4708beef-f0d1-32d7-84f2-c92b88515a85 | -11.17347 | -54.86406 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5789c749-b466-3088-97d8-9fb3b635fc29 | -11.17019 | -54.89063 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0fb334d4-dc61-36df-922e-886009f85a57 | -12.37504 | -50.3018 | 2025-10-08 05:29:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9fb1adce-3290-3242-8d61-88d6aeb540c0 | -11.76247 | -50.92247 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| a316e0c2-dc3f-3fdd-9914-7e2cd421ef1f | -11.17216 | -54.87756 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 131b7ace-7da6-33fe-ac34-30732410a362 | -10.35014 | -50.25153 | 2025-10-08 05:29:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 18430904-ea01-33c7-ad9f-9e9f2139a1eb | -10.36315 | -58.51405 | 2025-10-08 05:29:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 963529e9-6abe-33db-b6ea-8ef8a5d3a3b2 | -11.75655 | -50.91598 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 23.0 |
| ee0570f9-63c5-3160-a8a6-9f6a0e8191a2 | -11.76462 | -50.90731 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 940e55ac-da53-359d-a86c-d9a93e7746e9 | -11.45314 | -50.21097 | 2025-10-08 05:29:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b57ed89e-a8c9-37ff-b0c2-bc24e1d69ec9 | -11.16369 | -54.86409 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0eda370e-d330-3ffa-bdfb-936b668779b7 | -11.17643 | -54.88407 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| c84f4345-887a-3015-b1d4-57ac387abe15 | -9.62164 | -54.3205 | 2025-10-08 05:29:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 059c0075-d770-39e2-9650-98ece34803e2 | -10.34668 | -50.25497 | 2025-10-08 05:29:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 180f2fbc-dca1-3ac1-a5ca-ea99598099c6 | -6.86379 | -59.96958 | 2025-10-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de117d48-3e78-3020-8ab2-8d5a6de4c97c | -11.14479 | -54.89141 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e05ecb50-2b68-371b-9018-c16823dc6e98 | -11.17522 | -54.89128 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4b7a9ce2-8043-31ec-8dbb-1a648bc1f008 | -10.41109 | -50.22711 | 2025-10-08 05:29:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8d240562-b115-3398-a6ed-e43f01060922 | -6.69426 | -58.81395 | 2025-10-08 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4c6f5850-b641-3cc9-b6cb-4267e7f63f26 | -9.79396 | -59.9692 | 2025-10-08 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e9c6cf9-539f-3f25-a3b6-15b70b70457f | -11.17452 | -54.85965 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26fc0847-7659-3c37-9be5-9406c75f4c1e | -11.70717 | -50.94567 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 2d66bef6-2252-3029-a126-58cc32642ea0 | -8.48223 | -54.94474 | 2025-10-08 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9a2b776-1c83-3dae-9833-40244f4cc135 | -11.18711 | -54.87794 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28b4ca1b-24e4-38dd-8163-cf741f3efb9c | -11.17451 | -54.89702 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 24cff87c-8ecd-311b-a6c0-cdc486a2e639 | -11.18025 | -54.89191 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| bce523c5-50d0-3053-8452-3aa0a858a776 | -10.90026 | -51.01979 | 2025-10-08 05:29:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c16bbe9a-fa54-374a-a7fe-c4daa82da97d | -11.17594 | -54.88551 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 58828246-f219-307c-bc21-395e38e8218d | -8.16025 | -50.16401 | 2025-10-08 05:29:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 568ac158-de93-39f3-ab1b-44438359f274 | -12.39231 | -51.13516 | 2025-10-08 05:29:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 966f0425-1789-31d8-a2de-bd06ce1b4cb6 | -11.1691 | -54.86189 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb286b69-23cb-30e6-a673-b49e072d213a | -11.74225 | -50.92553 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a47165d4-f06f-3701-928e-256dab1794b5 | -11.15366 | -54.86249 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cb273a9-61a7-301f-803e-38f33446986a | -10.89241 | -51.01974 | 2025-10-08 05:29:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6502c654-63ea-3386-8d6c-1e1bffbc6052 | -11.16638 | -54.88269 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0c615bf2-c5a1-3427-86a8-8ab17c03a71f | -11.16949 | -54.85889 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d977a77-3643-3c97-9645-0acc8e13dcc9 | -11.15249 | -54.87144 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60c875cf-4d9b-38ef-bc45-30c287a0c0ee | -10.38357 | -50.22952 | 2025-10-08 05:29:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 03c62c82-5ed8-365e-9e6b-152137a340ce | -11.17378 | -54.90417 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 323c543b-a409-31fa-b81a-376608b840b9 | -11.75063 | -50.90945 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 23.0 |
| f8378628-517c-38f4-b416-296e632f05e9 | -11.17422 | -54.85806 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b16a239a-daed-3f8d-8047-e52bec91acf0 | -6.9494 | -63.09999 | 2025-10-08 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b76876fb-a670-37bb-807c-69174074f93c | -11.15172 | -54.87743 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a6279f4-0664-39b5-89d2-e61b54051c6a | -11.17558 | -54.88841 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 0b4156fd-9dbd-3061-b2c6-a3e29cc702b2 | -11.17918 | -54.90198 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8edb93a4-18ed-3ce6-b8f9-3df735c4ab26 | -11.15906 | -54.86031 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f6edf40-1f09-3aac-a1b9-eae1da85e5f7 | -11.42294 | -56.29381 | 2025-10-08 05:29:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e426b56-6141-35e9-8647-e62c2404a250 | -11.33649 | -56.20473 | 2025-10-08 05:29:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b43577cd-b9cf-3522-9c69-437c52c5844d | -11.17064 | -54.88921 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 271f35e5-aa1f-38bc-9d68-0392697b958b | -8.15945 | -50.16331 | 2025-10-08 05:29:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 20a07b1a-1f15-3289-a38d-051ec1c875e8 | -11.41744 | -55.07419 | 2025-10-08 05:29:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aea915f1-68e2-3712-bd11-0ca290a2e66c | -11.17412 | -54.86264 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a3cd1c6-81c6-327b-8e2f-3b30e499a5da | -10.34274 | -50.25661 | 2025-10-08 05:29:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4dca42f5-cc66-3ba6-bc33-3768d964a867 | -11.76309 | -50.91683 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 911e05e5-88fa-370d-89ab-3a912c7efd77 | -7.82731 | -61.68726 | 2025-10-08 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2550627f-4fd3-3d4d-acc9-74d702edc1b0 | -11.15828 | -54.86628 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac0f5c5a-184c-3b37-a10a-145c207f3b17 | -11.17529 | -54.89269 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 3527bdd0-a6c9-33e4-9a95-ae93e2feedd2 | -8.58521 | -63.1766 | 2025-10-08 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c599107-4a28-3fc3-92a5-6c72e6210629 | -9.99474 | -60.0057 | 2025-10-08 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad5d0a75-8840-371e-a470-600ecc787579 | -11.17994 | -54.89618 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4cbc948d-4bfc-34bd-ad9e-14a104680be1 | -11.11442 | -54.04001 | 2025-10-08 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 623077bb-20a4-3ece-99ce-d9a1f602bd0a | -8.1587 | -50.16942 | 2025-10-08 05:29:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README90.md)
