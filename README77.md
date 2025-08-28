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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dba8cd53-a7a3-3a04-a625-214b4548e3d6 | -9.16465 | -65.80027 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 408e6e74-d016-38af-90a6-7bc17f97a067 | -10.24621 | -59.66562 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6742927-c736-3cb5-a634-114f395b5fde | -8.25669 | -61.46804 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 105de860-c8d1-3085-b599-55d7b69f2c3f | -6.91789 | -62.93787 | 2025-08-28 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7583debd-d197-3e8c-ad55-127e02e72be7 | -9.183 | -60.80636 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 134c3d7c-5c68-3189-9baf-37ccf611238a | -7.56315 | -63.8627 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f472c578-e60f-334e-8b28-626a36968e87 | -9.31175 | -57.69859 | 2025-08-28 05:25:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f38cd6d6-31c4-3617-9b09-7c9fe2079376 | -6.92363 | -62.94678 | 2025-08-28 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 579e7d45-588d-3d50-96f5-3333389438df | -12.67578 | -48.17786 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4065e7aa-00a7-3224-9a59-de008ff4d9f6 | -9.17186 | -60.76877 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85179631-e858-3548-9972-5311282ed246 | -8.96077 | -65.95194 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87ffeb75-79e8-3f83-b9f2-20e3b0c8c5cd | -10.15722 | -64.25045 | 2025-08-28 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1e3b7b38-0ddd-3322-8b9b-02b8a925230d | -9.12371 | -65.77744 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 52b6ce04-7e41-3839-88a2-e2e35bb9f31c | -9.18699 | -59.45566 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fcfbd89b-da15-3a51-a935-f35bb5094e3a | -8.69446 | -64.20068 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0985860b-fba1-3db4-944c-2f1d402b3bab | -7.413 | -60.62194 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 858667d1-f54c-3bce-8605-dec1a151cba4 | -9.17224 | -59.46088 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d26fbd5-1408-336c-8f50-9962cde6c973 | -10.46654 | -57.9597 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 90a710ea-ebf2-3acc-b711-6c8414b847c0 | -12.86168 | -48.1214 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c46142f3-dc63-39aa-adea-3e2eddba3cdc | -8.9107 | -60.71289 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4657e5ed-e8bd-3c7a-9338-d1906170ddbb | -12.12067 | -55.1941 | 2025-08-28 05:25:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f15ed9a-9092-36b0-a674-6dd7a83c5a1a | -9.1593 | -59.56773 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba343ffd-40a6-30d9-935b-087480b83f17 | -8.33835 | -62.94592 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4eaf541-bac9-34ae-9ac0-fb89f8a46076 | -9.4065 | -60.54317 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d55f3b5-9896-320b-a08f-d53d3ab062d5 | -9.49496 | -60.53966 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18f391f6-6b75-3e0f-887f-9a0ab4dde4a5 | -11.36315 | -63.2683 | 2025-08-28 05:25:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 36e5c534-de74-3302-88d0-4afa5c929ba9 | -8.34607 | -62.93086 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 93256f32-cf05-33ab-a9af-f498a5c8433e | -9.01077 | -65.7085 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d777bac-ff39-320d-8de8-2e6f4b92af43 | -7.41577 | -60.62594 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bb6e555-d3ab-30db-9c59-4dd4db779f22 | -7.40154 | -64.34219 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8a61eee-4df8-33d2-9532-0d79832e6ae4 | -9.19742 | -60.28678 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcc210c7-9751-366b-a7ff-113e247e8353 | -9.31607 | -57.69479 | 2025-08-28 05:25:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8a542944-df25-3cd9-8750-1da76451c875 | -9.13437 | -65.28499 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 687932c3-d5a2-3d15-9413-7a0eb2c66aac | -8.96137 | -65.94843 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d46b579-a366-3535-a7f5-baff73989ad8 | -6.00033 | -57.84824 | 2025-08-28 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf4348b6-e61b-33da-959f-04fe79c5a861 | -9.10616 | -60.32307 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cd18b11-2f54-3e4f-a557-bfd2e5231c7d | -9.66219 | -48.31114 | 2025-08-28 05:25:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 776b4b1b-6f8c-3287-b8df-7c58b450be60 | -9.41587 | -60.50496 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f56f94d7-033e-3ae5-9686-874c282fa406 | -9.17968 | -60.80583 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e906eab-c219-339f-8043-6763e06ba752 | -9.63667 | -59.64089 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b2fd3b4-a777-3ee9-b0f3-3d47a72dc58b | -8.89025 | -60.75621 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88cac22d-4d2f-3b8c-a38c-d210fe988b26 | -9.16099 | -59.55671 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 654a57b8-5f5b-327e-8d12-0534d43b9fc6 | -9.4983 | -60.54018 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0aaddab-113a-38e3-962f-ff609be05c6e | -13.01466 | -56.89116 | 2025-08-28 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98546262-65c6-3ff4-91c2-0b0d2c31c8fc | -8.90071 | -62.46835 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96f84d2e-349e-36f0-9413-64195dc898a9 | -9.49219 | -62.39649 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a08694a7-31a1-3736-a2f0-008d51c40e4f | -6.90677 | -62.94004 | 2025-08-28 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d4761b2-4e7d-3a32-b8b3-4f493b2909bb | -12.80263 | -48.1637 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f384dcd3-69f6-33d7-a308-b01b04a4db37 | -8.57922 | -63.92664 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a266308-896c-3a39-a1bc-edba2325417c | -8.07337 | -61.5326 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9692a2d1-a4a2-350d-8b8c-b5713c0d61b6 | -12.70885 | -48.1699 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48b41f54-03fd-369d-8c3d-b25448bb7b2c | -8.57777 | -62.60814 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5304f96-b67f-3942-9c99-1f7c73176fe1 | -8.95775 | -65.96946 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a7f06e3f-5601-3381-a0c0-310c62c85e9e | -8.93093 | -65.92918 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9caa21be-458e-3ebf-86cc-d95d133c1380 | -12.86224 | -48.1161 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1266dbb5-8ea4-37c1-b66e-c2e1ea1897fc | -12.67514 | -48.18385 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8806c523-e296-3683-b24c-358d3b1fd900 | -12.7886 | -48.16085 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 197053d2-39bb-3376-a0e8-dd9f0c577f8a | -9.19549 | -59.78913 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d17c43c2-e18e-3bc6-aec5-90bbac8fa720 | -7.44455 | -63.1633 | 2025-08-28 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9384c949-5fbc-387c-be2d-d75caec40f3b | -9.40586 | -60.50336 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 414c1028-8822-3f63-867b-3933f787af0c | -8.91951 | -65.92358 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| acda675a-efbb-3996-9d77-ac1c337a2760 | -9.23246 | -59.68364 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39861d75-a229-3b1a-8271-e1b17c08573c | -8.65051 | -67.26973 | 2025-08-28 05:25:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14dfb1ad-e763-3351-b7a6-16d61eded463 | -9.13742 | -65.29042 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c9c05c5e-6c53-3ea4-81ff-f74dda439de8 | -10.4758 | -57.94775 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f365949-8ff9-3a44-a52b-c6f18fa59ad4 | -9.11804 | -65.78686 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 7dc72ebc-a38f-3789-9142-85d331d3ce5f | -9.19075 | -60.80047 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eac39521-aff9-3d17-a0be-17331c5189ef | -13.73092 | -51.90471 | 2025-08-28 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e8d69b2-09d3-3d49-8c30-bb25d6999521 | -10.47038 | -57.93348 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 0b23f9ff-9c70-3274-a685-2849889f148f | -10.28171 | -64.49152 | 2025-08-28 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9033cb03-b56f-36bc-a0e0-575b2163c677 | -9.74554 | -67.69774 | 2025-08-28 05:25:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62343fe7-60bc-3a7c-9958-9548e4b2331e | -9.6777 | -47.07079 | 2025-08-28 05:25:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5e72437d-fe97-3eaa-b9d8-e256033814e7 | -8.68198 | -66.91025 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 437454c6-8cd8-3eb0-a50e-d39e43bf9c09 | -10.42862 | -64.37395 | 2025-08-28 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b435ca03-f2f0-331f-bb66-81d3bbb1ca69 | -9.18473 | -60.86042 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af8a432a-9a64-3e2b-8788-94c2b05dce13 | -9.40422 | -60.51394 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 879481b1-e2fc-382e-ba1b-4aa6e5d4dc86 | -13.6215 | -48.24289 | 2025-08-28 05:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 23cf7571-498b-357e-a8c3-8f9acc47ecba | -8.95215 | -65.95402 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8d90deb-485c-37a5-95da-0a4d3b85d727 | -9.14058 | -65.27142 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e33c25f-095f-31e7-a380-7749cd6f658e | -8.99236 | -65.41737 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22d0d2e5-0a11-3c66-adba-4389514878a7 | -13.61461 | -48.23996 | 2025-08-28 05:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cf864200-25ae-3e78-8e04-3ddf81c4b8f5 | -9.15986 | -59.56404 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7705cf6-665d-38ae-a270-277c546478da | -9.15591 | -59.56716 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c6e19255-f8be-3b77-9316-bf6d5d1f0c2f | -9.50355 | -62.77962 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 800d7735-dd68-3c36-9c47-4210f0242c29 | -10.79773 | -60.77372 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| dfef51e2-89e1-3fd0-bd03-77c93512c3cd | -8.26415 | -61.45836 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac610dbc-fb28-398d-9b98-710ba425bd42 | -9.22075 | -59.75978 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af2cca1f-981b-398a-a956-aa6435411064 | -10.48126 | -57.96161 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee4b28fc-034d-387c-a43c-11bd975e6299 | -9.17738 | -59.51805 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4153cca8-2a2c-3547-8685-abfa48c25552 | -9.40308 | -60.49932 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba11d9ce-3e76-34fe-a88e-1715040eca80 | -12.81259 | -48.13803 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 38546c60-2614-370b-a1e1-964a66fbe159 | -9.36601 | -61.53162 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d2a23af-ec47-3c88-b43b-8095ac8da6a4 | -8.065 | -61.54207 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ecd76a7-46b0-3ecd-b2e6-ea6f3997a265 | -7.35307 | -57.63791 | 2025-08-28 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ded3127-1147-3be7-9b1f-28e22abd12e6 | -9.18755 | -59.45198 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| faa2cc7f-1451-370f-b939-22dea85b4c9f | -9.41199 | -60.50795 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2b48207-50ea-3517-9ffb-20fe120ff86a | -9.18245 | -60.80986 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f740711e-ba56-3b1b-a615-be0822cb2207 | -9.41756 | -60.51605 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f692375d-3e1d-3339-b255-d92bca5e5ecb | -9.69369 | -61.28239 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0e1947bc-ac40-309d-b62d-a16ba41de285 | -7.44125 | -60.02979 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README78.md)
