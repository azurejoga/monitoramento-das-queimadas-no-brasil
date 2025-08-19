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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97bed32f-a148-36f3-9f8a-8409da44f3b2 | -8.8235 | -52.0383 | 2025-08-19 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 71a67dac-7747-342a-b0d6-a63a9094886f | -8.88276 | -62.39844 | 2025-08-19 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93698bdf-a40e-35aa-aa98-cced6196e548 | -9.22912 | -59.65213 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a68983e8-a1b7-3b8d-95d9-cf123551ee6a | -7.55123 | -63.85045 | 2025-08-19 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c5ee38d-6ced-3e07-aba5-0bcaf02eb3b1 | -3.37583 | -52.71918 | 2025-08-19 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 06c27423-214d-388d-88e5-3df6ab3dac62 | -7.59983 | -63.44788 | 2025-08-19 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b576253-6517-39c0-8f74-ec0f9341863d | -9.22967 | -59.64865 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b2b8c11-467d-3fb0-8a79-5e090408e633 | -8.76998 | -50.02417 | 2025-08-19 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e99fdfcb-0394-3b58-882f-271bcac3dfa9 | -6.13637 | -57.93187 | 2025-08-19 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1112b3bd-d1c4-32ac-b4ff-03afe5195bd8 | -9.7157 | -51.96785 | 2025-08-19 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1b113dc1-ce6e-376c-84c0-f0f6df448762 | -8.61487 | -62.61206 | 2025-08-19 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51fdc436-684f-3d46-a22e-40ae4d662d23 | -7.04694 | -59.23005 | 2025-08-19 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 968eff04-6a91-39f8-a137-ce1d01d58c82 | -9.18968 | -59.64254 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 19845c5c-93e7-3e78-9bbf-c6f26aa2ad27 | -6.18987 | -53.52043 | 2025-08-19 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40c38c1b-1c8d-3f87-a2ca-1e7ea38fd306 | -6.20984 | -55.66625 | 2025-08-19 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a18822d4-5bfb-378c-9560-c26218443472 | -7.30573 | -46.28855 | 2025-08-19 05:16:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f72bc796-b63a-3606-8267-61f8fd06b54d | -3.06205 | -52.47875 | 2025-08-19 05:16:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29abbceb-8f48-39d2-bb22-6362f9dc33e3 | -7.93269 | -63.29114 | 2025-08-19 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dec1b545-7613-3945-8a15-b6bcd07ab63b | -9.19384 | -59.66077 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f537e9d7-43e5-3076-abfe-23e722f6fa43 | -8.40319 | -49.49953 | 2025-08-19 05:16:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d58dda0-b746-33fc-a2bc-318516f51f87 | -7.44592 | -63.02749 | 2025-08-19 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06eefe4e-5256-38dd-8bcf-3066a01b6e55 | -8.43901 | -63.85948 | 2025-08-19 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a200e4cd-ae39-3d11-9103-a9f5f2a05567 | -5.94806 | -60.01263 | 2025-08-19 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| baa1952f-33fd-34f0-b7f3-408142b1fea0 | -6.41916 | -53.3734 | 2025-08-19 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ca2b5e2-7029-38c7-b7a2-cad328e60d9c | -9.16447 | -58.91558 | 2025-08-19 05:16:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1b4f844-b5ad-375e-9a32-db0720584717 | -4.01228 | -48.06572 | 2025-08-19 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2145f20-a89d-3fd9-8b24-1a66071f3469 | -7.55207 | -63.84549 | 2025-08-19 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1836a2e6-70ac-3697-b42d-ab3a75f8e9df | -9.19713 | -59.63988 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be44d05d-765a-3936-81b4-c02c7af9b60f | -4.14655 | -46.45635 | 2025-08-19 05:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dacd49be-cefb-3633-9d1e-86e5ac8b7d33 | -5.87665 | -48.11729 | 2025-08-19 05:16:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e269c58b-b37e-3871-823e-4bf6c71ddf3f | -9.71495 | -51.97343 | 2025-08-19 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c4ba6e8c-8646-3148-9609-59f98a28b6e7 | -9.04101 | -50.17687 | 2025-08-19 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74324f4f-eb44-3a81-89a1-25622ebadb45 | -8.40061 | -49.49832 | 2025-08-19 05:16:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5ec1e118-8e92-376e-bf5d-2bc4f7f0f9a2 | -9.20153 | -59.63346 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21961e5c-2901-3513-8fdd-f84a39ff587a | -9.24069 | -59.64327 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cefa43ae-97a7-3c4c-b037-3053a26b3f51 | -9.18528 | -59.64897 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4462a59-4f32-31a6-b848-e0be265171ae | -9.18248 | -59.60216 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd418069-2955-31d6-90a9-0fdc5098508c | -9.07339 | -60.41841 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e3f123c-188c-344c-8f22-73035e4bf1fa | -9.19217 | -59.6498 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8987d9e4-d477-3b9a-8721-2974f799f998 | -7.30037 | -46.28825 | 2025-08-19 05:16:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a32175be-a984-3424-ada7-1bab3c921790 | -9.18859 | -59.6495 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08495cc0-9171-3307-8528-acb46bc32ce4 | -9.17811 | -59.65139 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5f40bcd0-5816-39b2-ba83-bf9ef155849c | -6.13583 | -57.9354 | 2025-08-19 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3bb3a336-7c50-3f4b-829a-fbc861b66332 | -8.97252 | -60.49641 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35085b56-8c6a-3e1b-a15e-b1a96be1b781 | -9.23738 | -59.64274 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce1ba214-ae37-397d-99c9-e5cf679dcc04 | -6.1604 | -47.28149 | 2025-08-19 05:16:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c0eb92a-9efa-3595-85ff-5de48a1b8efe | -9.19188 | -59.62862 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| eba936cf-2901-31fe-9fec-7009815627af | -7.79055 | -66.95305 | 2025-08-19 05:16:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b72cda21-497a-305c-98b0-ff4c8c2aaedb | -7.42061 | -60.59358 | 2025-08-19 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22bd87f6-ebd0-3339-882d-4d9294bb0a36 | -4.02345 | -48.06933 | 2025-08-19 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbdbccaf-9e1b-3a50-9a1d-f251437cacfd | -5.88656 | -57.75188 | 2025-08-19 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54a29db6-2019-3ef2-b185-2e8bcba4e4a4 | -8.97309 | -60.49287 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b9dd9d3-31eb-32ed-8a9f-b27121573afc | -8.61638 | -62.62509 | 2025-08-19 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8e74bb5-ff8b-310d-a08e-75a302597784 | -8.71142 | -47.86057 | 2025-08-19 05:16:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 848dabbb-d4ea-3958-a359-042c1da2ef80 | -3.45471 | -48.96863 | 2025-08-19 05:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e1e8df8-0218-3a00-8573-7213512edcb1 | -8.97139 | -60.50347 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1c24aded-6020-3079-96a9-faa826cf15f6 | -7.78486 | -66.9574 | 2025-08-19 05:16:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 75473afe-78bc-332e-8e5d-29bb1c5bfaa0 | -8.97529 | -60.50047 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af183735-f579-321a-a5c6-30efcb101a03 | -7.21878 | -49.61001 | 2025-08-19 05:16:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb77b488-6c28-314a-ba97-460e94baa40e | -3.94047 | -59.40966 | 2025-08-19 05:16:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ec459e1-835a-37b9-adaf-d89f7b523ab7 | -9.0368 | -50.17873 | 2025-08-19 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02100022-78c5-3cbf-86ef-8807dd7cb6dc | -5.87606 | -48.12152 | 2025-08-19 05:16:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 872b5591-704e-38ca-8ccc-a7691e605789 | -7.21928 | -49.60633 | 2025-08-19 05:16:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbd9695a-5bed-3863-b586-60900dc9ca0e | -9.19437 | -59.63588 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c3f9854-c0e5-3a91-8927-d08caa7ce728 | -9.14834 | -60.81952 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e35202e-da07-35e0-9630-7eee92d992fd | -8.23631 | -47.86109 | 2025-08-19 05:16:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73fa6494-e2d4-333e-bf7a-700e7e1f3774 | -9.1218 | -60.32892 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcbb7e33-56cf-3a45-93eb-b5ed80fbdf4a | -8.77045 | -50.02058 | 2025-08-19 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b3411d8-bc84-3d2c-936b-94e051a94c69 | -9.17862 | -59.60511 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9a5db31-7a6c-3098-bf52-15d44b85c773 | -4.33946 | -55.78678 | 2025-08-19 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81fa5c3b-8a96-3c5b-9551-242054703905 | -9.17312 | -59.6185 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 034a2035-8e26-30e4-8fcd-24e4d61e468f | -9.07615 | -60.42248 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b5c9509b-ad1f-3042-8f0f-53497ac5fa6c | -7.30646 | -46.29483 | 2025-08-19 05:16:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73aec9d2-91fa-3400-89c6-aa5d6e263d21 | -8.46125 | -64.05957 | 2025-08-19 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7a7c555-771a-3600-ac7c-966cc0685b15 | -9.18307 | -59.64148 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9676dd2-ade9-34c3-b045-df879349bb28 | -9.17917 | -59.60163 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 099ce8f2-06f3-35fd-9d61-2844ad0592b9 | -7.91544 | -63.27886 | 2025-08-19 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 2e4095a6-92c9-3d78-b2c0-4da5c9984a30 | -8.82759 | -52.04408 | 2025-08-19 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c1b81f89-5c53-3212-8b1d-80b00324a803 | -4.01746 | -48.07088 | 2025-08-19 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3fbb61e-2628-3e1d-b0ff-9c883bb1fcf6 | -9.18583 | -59.64549 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dc3e7ca-e020-3f80-bf64-8460d8118f20 | -9.17535 | -59.64738 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 849cd720-99a1-3593-a444-ef9dedfef4d4 | -9.17698 | -59.61554 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cf30958-5b1a-38be-9e8d-808af73482b7 | -8.70448 | -47.86469 | 2025-08-19 05:16:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b015b85c-0151-3dd8-bb19-d0e681304879 | -8.96976 | -60.49234 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 306d2b2c-e152-302d-96e7-7f8cc58b4e96 | -9.11848 | -60.32839 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fea00886-6c37-3b71-ba7a-679e79daccdc | -9.11071 | -60.33433 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da85890a-9c9a-3bb2-8b02-80779e11bbb9 | -4.01823 | -48.06425 | 2025-08-19 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e09b02c9-732b-3c34-b3af-084226cb2564 | -9.04771 | -50.18004 | 2025-08-19 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c57a231f-210e-30b5-9f3f-f4ec24efa7db | -9.19242 | -59.62514 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a9252fb2-721e-3951-a291-d30c4c75a84a | -5.88711 | -57.74833 | 2025-08-19 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b33aa0d-40c4-3b70-962a-781a7c6bd352 | -9.19768 | -59.63641 | 2025-08-19 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 80487678-9bae-3e99-9f39-26437a4da892 | -6.49456 | -53.39101 | 2025-08-19 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 362dab71-cec3-3948-8aac-a80eefeefcf9 | -9.05144 | -50.18171 | 2025-08-19 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9f33061-feaa-323b-9e39-fc7c8c3ad38c | -5.88139 | -48.12685 | 2025-08-19 05:16:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2b019fb2-423c-3f18-a8a7-467060c54716 | -3.28041 | -48.81095 | 2025-08-19 05:16:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| def459f0-0e14-32db-a2cb-7d7542fe3804 | -8.23567 | -47.86597 | 2025-08-19 05:16:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8bd0157d-726c-3b13-ad42-9c0e36959b39 | -7.59715 | -63.44601 | 2025-08-19 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c6692bf-4436-3ba9-ac72-99290e6fc2da | -8.62424 | -62.62217 | 2025-08-19 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d75ee674-a686-3809-9a43-df650b8c90d4 | -6.19402 | -53.52101 | 2025-08-19 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d22585e7-bd63-3bf3-b771-fd977471f8be | -3.45331 | -48.9677 | 2025-08-19 05:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README49.md)
