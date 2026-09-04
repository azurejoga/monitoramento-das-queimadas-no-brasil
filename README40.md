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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff674a67-c672-3eba-9fb4-10174de688a4 | -9.04182 | -65.73758 | 2026-09-04 07:44:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4df7b41c-cfed-39b3-a1c3-9e6cc86c9af7 | -9.57648 | -64.29163 | 2026-09-04 07:44:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 54c8e68a-8c4d-3f4a-bcee-05c3697c4a7b | -8.60262 | -67.16486 | 2026-09-04 07:44:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 33.1 |
| fbafb1dc-d4a0-3c96-ae39-15810b78aea9 | -3.07442 | -61.08028 | 2026-09-04 07:44:00 | AQUA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 269364b7-106e-30c8-9fd4-9ff977297568 | -8.59799 | -67.19274 | 2026-09-04 07:44:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c8cabe6f-2fdf-3767-9115-6a7aa0d3c2ae | -7.01168 | -62.98129 | 2026-09-04 07:44:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a0b0d28a-5936-3654-9554-1684a7a79324 | -6.6803 | -59.94012 | 2026-09-04 07:44:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 44ed93ef-af5a-376c-a9e9-a6250a47d016 | -7.55233 | -61.35363 | 2026-09-04 07:44:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 989d81c9-698d-3871-ba6d-9dfe4ea07bd7 | -6.67884 | -59.9502 | 2026-09-04 07:44:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 6cedcbb8-d5d0-3a0e-972c-1d1f02b4287c | -6.99272 | -62.9875 | 2026-09-04 07:44:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ef6c3db0-d928-3d4b-9a5f-6986be4a7f5f | -3.75698 | -61.75596 | 2026-09-04 07:44:00 | AQUA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e37b3127-789b-38c5-bca5-59fb897b30f6 | -3.07748 | -61.17894 | 2026-09-04 07:44:00 | AQUA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9600f97f-ce35-3ef2-a6f8-be3c3fbdd5e6 | -6.68677 | -59.96163 | 2026-09-04 07:44:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 98ef25dd-1b4e-3731-84ad-873f921097fe | -6.6853 | -59.97174 | 2026-09-04 07:44:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| bdbc7692-2052-3561-b6f6-736f939905bb | -6.67091 | -59.93877 | 2026-09-04 07:44:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 82ed9d1f-f9ea-3f64-9300-5de53f03b16f | -8.59895 | -67.17168 | 2026-09-04 07:44:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 0c08262d-9a2f-37ea-809d-e7953b8ab9ea | -5.55807 | -60.16758 | 2026-09-04 07:44:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| f7ebda2c-b590-34f6-9a0b-3405a36c54c6 | -3.21672 | -61.16946 | 2026-09-04 07:44:00 | AQUA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| c9c2ac7f-0622-3c0c-a9bb-cd129090a3c7 | -8.16142 | -62.77785 | 2026-09-04 07:44:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5f8952d2-fa7d-3a47-b165-0e621a3a3af4 | -6.14577 | -59.93912 | 2026-09-04 07:44:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4225ebc7-e050-36c0-a4b9-2f74dcdf38de | -8.60031 | -67.1788 | 2026-09-04 07:44:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 109.3 |
| b6c356f7-630c-3c1d-b60b-02749d6a30f2 | -6.6932 | -59.98315 | 2026-09-04 07:44:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 36.9 |
| ceb2f927-5019-368d-9adc-31eeac26eada | -8.59673 | -67.18564 | 2026-09-04 07:44:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 34.5 |
| cb84d483-7ad9-38e4-aa29-973e6ca27923 | -7.55506 | -61.33543 | 2026-09-04 07:44:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 668282f8-0b61-3df6-95a2-b56180c15c0b | -6.69783 | -62.86157 | 2026-09-04 07:44:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 12324d38-a078-3586-9227-0ca19909d7d9 | -6.69468 | -59.97307 | 2026-09-04 07:44:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 14d38087-ac88-31ef-a5d0-86c1af51a89a | -7.37054 | -60.59324 | 2026-09-04 07:44:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0b75e7df-a3f9-3902-9331-ad63296ee3ef | -3.14047 | -60.63977 | 2026-09-04 07:44:00 | AQUA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 919cbc30-1cc3-37a8-9d2f-75b3cd68e65c | -6.68383 | -59.98186 | 2026-09-04 07:44:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 39ff0cfc-7326-3145-9862-ea7e68c57f84 | -7.5537 | -61.34453 | 2026-09-04 07:44:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 32.9 |
| c6979ecd-79a0-3689-b540-4ea12641c9be | -6.68177 | -59.92997 | 2026-09-04 07:44:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 09d8a681-e3f1-389c-80f4-afa161141b95 | -3.77449 | -61.75854 | 2026-09-04 07:44:00 | AQUA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b5cff76d-f0ce-332d-a6aa-0682a5c861f4 | -6.67738 | -59.96032 | 2026-09-04 07:44:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.5 |
| af624b04-c6d3-3d09-8e0a-24d2ec90d587 | -6.67592 | -59.97041 | 2026-09-04 07:44:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| f8c13e25-1a7e-35e3-85ed-d8f2bd2a2ba5 | -7.36913 | -60.60278 | 2026-09-04 07:44:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a5f49b7c-a14a-3ec8-ae97-e914ae1998a3 | -8.6101 | -67.1783 | 2026-09-04 07:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |
| ae5551d0-00bf-3a00-a47d-19fe69dec07c | -6.6882 | -59.9628 | 2026-09-04 07:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 4e7a7abd-c9b4-3939-a715-a42d8a0dff09 | -6.6881 | -59.982 | 2026-09-04 07:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.9 |
| eb9139f4-3e4f-3942-96bb-61cb63adf9b2 | -8.6101 | -67.1783 | 2026-09-04 08:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 1b1d0d73-5166-3bcb-a940-273dabd668c4 | -6.6696 | -59.9827 | 2026-09-04 08:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 72919454-7e22-36d5-9543-4969a02008fa | -6.6881 | -59.982 | 2026-09-04 08:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 4c1df79f-b42e-3bf4-8922-d41a6d5a3484 | -6.6882 | -59.9628 | 2026-09-04 08:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 0828b4fd-5db3-3652-bb35-9a667f6550e7 | -8.5916 | -67.1788 | 2026-09-04 08:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 1912fcf2-8683-35f8-a5c3-3d4733c7f66e | -10.5103 | -51.3194 | 2026-09-04 08:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| a0d4c671-f197-3d25-8289-157e62d40d0d | -6.6881 | -59.982 | 2026-09-04 08:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 14e84922-3f2a-3061-aa4d-67df3b6f641b | -6.6882 | -59.9628 | 2026-09-04 08:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 6a3064bf-f184-3213-9437-c1bc79987e97 | -8.5916 | -67.1788 | 2026-09-04 08:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| e28b5c25-ac8b-3195-8440-daa19c774c6f | -8.6101 | -67.1783 | 2026-09-04 08:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 14f60a95-6005-3e41-b641-f1c70136c612 | -10.5103 | -51.3194 | 2026-09-04 08:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 9bb721b3-b63f-3e50-a104-d35764d38669 | -8.6101 | -67.1783 | 2026-09-04 08:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 68321487-f50e-37d2-9d77-bc9c116622f6 | -6.6881 | -59.982 | 2026-09-04 08:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 43e2542f-a1f1-3c56-a802-b3f999cf90d5 | -6.6882 | -59.9628 | 2026-09-04 08:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| a766a7bd-5baa-37a1-851b-9dad77221782 | -8.5916 | -67.1788 | 2026-09-04 08:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 7128ce1e-81a0-39a2-97b2-9ba4663ad34a | -10.5103 | -51.3194 | 2026-09-04 08:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 96ba3476-2ff1-3809-8c41-35beb5e15bd5 | -6.6882 | -59.9628 | 2026-09-04 08:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| d25df373-e3fb-30b3-acdf-6df4478bee6e | -6.6881 | -59.982 | 2026-09-04 08:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 52d74737-9ebf-3b43-b313-da96368aa0d1 | -10.5103 | -51.3194 | 2026-09-04 08:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| b16850ac-1dbd-3ee9-a540-65a81a65ea73 | -6.6697 | -59.9635 | 2026-09-04 08:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 83490c80-ab4d-3a10-b218-e2e47c491898 | -8.6101 | -67.1783 | 2026-09-04 08:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| b4b8a90b-b148-3548-969f-bbf1f7edf863 | -6.6882 | -59.9628 | 2026-09-04 08:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 51b6e01a-2d58-375a-b90b-38a078bc6478 | -6.6881 | -59.982 | 2026-09-04 08:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 31473a04-1f57-3b8a-b576-fe5b624ff582 | -10.5103 | -51.3194 | 2026-09-04 08:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| e61d493d-1e83-324d-8dda-1a8b20171a42 | -6.6882 | -59.9628 | 2026-09-04 08:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 69938b52-1339-3944-82f4-bb523add1136 | -6.6881 | -59.982 | 2026-09-04 08:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 03904e4b-b0b5-376a-ae38-595d60eeb686 | -6.6882 | -59.9628 | 2026-09-04 09:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 1d31033c-208f-3472-8156-9524c88f8f8c | -6.6881 | -59.982 | 2026-09-04 09:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.0 |
| d25bc535-fc92-3ea1-80d4-6a543c1fb607 | -6.6881 | -59.982 | 2026-09-04 09:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 8499585c-a412-33db-80bd-cc486dd6fb31 | -8.6101 | -67.1783 | 2026-09-04 09:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 547b8c2f-8e90-38be-9318-1366672958e7 | -6.6882 | -59.9628 | 2026-09-04 09:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| cdec366f-8ecb-3ee6-8397-5d91bd7ccede | -8.6101 | -67.1783 | 2026-09-04 09:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 2758a6df-62a6-312d-bea4-95104c52906b | -8.6101 | -67.1783 | 2026-09-04 09:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 2767fc38-8cd7-399e-a29c-34259fa7958a | -8.6101 | -67.1783 | 2026-09-04 10:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 105.0 |
| c2aa3f36-2c47-329b-a2e8-5a9e2b6beabd | -8.6101 | -67.1783 | 2026-09-04 10:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 211.3 |
| 5f0c323f-0e1d-3bd8-a5de-17fcdbd1819b | -8.6101 | -67.1783 | 2026-09-04 10:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 144.8 |
| 411fb518-10a1-385e-bdac-255cec367554 | -8.6101 | -67.1783 | 2026-09-04 11:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 139.8 |
| ad3f6bf2-c623-30ce-96c6-fc1a26277639 | -8.6101 | -67.1783 | 2026-09-04 11:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 163.4 |
| 806c5e64-ee30-36fc-967f-c366c7431d03 | -8.6101 | -67.1783 | 2026-09-04 11:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 4147b3c0-68c0-316e-a439-7bb1cbe8b13a | -5.598 | -43.9978 | 2026-09-04 11:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 7ea5b0f5-0029-3c17-991b-c66708f65468 | -8.6101 | -67.1783 | 2026-09-04 11:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 1d070bd9-6219-35f8-84ba-4dd4ef5ff836 | -3.98162 | -42.10466 | 2026-09-04 11:30:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| cce0486d-fd0e-39e6-bbe8-9e5ca9c08bdf | -3.98288 | -42.09578 | 2026-09-04 11:30:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e9673241-faa8-3a37-865a-da975d31c7d7 | -5.31125 | -43.64479 | 2026-09-04 11:30:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 2ab01cf4-287f-332e-ac21-47ad1cb9dfd8 | -5.59369 | -43.9926 | 2026-09-04 11:30:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 715a89ec-e6c9-3f32-8b8e-7e790b63f06d | -5.49495 | -45.11915 | 2026-09-04 11:30:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| c019810f-fb55-3c7c-b2fa-fc35bc1a616d | -8.08599 | -44.35792 | 2026-09-04 11:30:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 53477018-7764-3472-b611-c6c09b906452 | -3.95805 | -43.11881 | 2026-09-04 11:30:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| faef67ed-1f5d-3eba-ba49-c2af4c274eaf | -7.13428 | -42.24203 | 2026-09-04 11:30:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 93c40127-9def-38f7-bd72-fbc22cd46aaa | -5.17441 | -39.74879 | 2026-09-04 11:30:00 | TERRA_M-M | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| d328b01f-be9e-3ffe-bbe0-20f87d3cc7a0 | -4.40079 | -43.31049 | 2026-09-04 11:30:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 50a6002f-11aa-3ef5-bdad-c173507e1800 | -5.59238 | -44.00159 | 2026-09-04 11:30:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 913cb108-081a-3ef5-9a69-6ff28e6777fa | -4.45463 | -40.20578 | 2026-09-04 11:30:00 | TERRA_M-M | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 871765de-b2a2-3eb7-90c0-00b09d5ad116 | -5.62656 | -37.48116 | 2026-09-04 11:30:00 | TERRA_M-M | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 86710e4d-4067-39a6-bdca-436004571ba0 | -9.66892 | -37.24639 | 2026-09-04 11:30:00 | TERRA_M-M | JACARÉ DOS HOMENS | ALAGOAS | Brasil | 2703403 | 27 | 33 | nan | nan | nan | Caatinga | 27.4 |
| d0376f99-b27c-3e86-a237-a5a8648dc61c | -8.08469 | -44.36693 | 2026-09-04 11:30:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 46e8f4fa-d8da-3bc8-a7a6-ddea597eebfa | -7.12402 | -42.24997 | 2026-09-04 11:30:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 28.7 |
| d63eb3fa-b983-36be-be9b-6b52b6337dfa | -4.15488 | -43.09576 | 2026-09-04 11:30:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| c79fdb00-9adb-358b-bdd5-d5f6affaec9d | -4.15615 | -43.08696 | 2026-09-04 11:30:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 187542f3-dda0-3e28-94f3-d41e6de495d7 | -4.45922 | -40.20152 | 2026-09-04 11:30:00 | TERRA_M-M | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| ea9ca548-16b1-3a70-a2d4-00ce804e52a5 | -5.4935 | -45.12918 | 2026-09-04 11:30:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| c4dd2dc2-3b31-3e75-80c6-1d64a496246c | -13.40569 | -41.88435 | 2026-09-04 11:32:00 | TERRA_M-M | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |


[Clique aqui para ver as próximas entradas](README41.md)
