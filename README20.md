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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eacfa99e-b721-35db-90eb-3c780b897a3b | -2.88907 | -50.44129 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7005aebf-d008-3799-9783-637d3a6d9538 | -3.13835 | -60.65604 | 2026-09-07 05:01:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79976b1d-486a-3e87-9651-405eea87f5e4 | 2.36474 | -50.77662 | 2026-09-07 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74c0d2be-05f2-3134-afc4-e0b1b152f4e1 | -3.62144 | -54.60147 | 2026-09-07 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4d78577-7bfd-32be-b88c-a63781be8c0c | -4.35224 | -48.9734 | 2026-09-07 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b67ef416-56bc-3efc-a9a9-d58e96b090a9 | 2.36142 | -50.77713 | 2026-09-07 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d2878c5-30ac-373c-912c-ef5d37ba3908 | -1.84533 | -47.94654 | 2026-09-07 05:01:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c24314b-a083-39ac-8bf2-10e05e5aaf42 | -1.86393 | -47.97967 | 2026-09-07 05:01:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24769403-13e9-39d7-b4fc-1f4f9bc08000 | -3.55233 | -48.18182 | 2026-09-07 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81535ee3-ae58-3f03-847d-b52044f4734d | -3.14356 | -60.65691 | 2026-09-07 05:01:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3ea89eb-366d-33f8-bef7-2974a8b905c2 | -2.86659 | -50.44558 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb76710f-aaf8-315d-933a-29cc6cc4b4ad | -3.95988 | -55.40293 | 2026-09-07 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5f56d1d-10dc-3da4-9250-1a642ebee6e7 | -2.03286 | -48.57572 | 2026-09-07 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3aaf024-4b5f-3f19-94a7-fc50d0ffb6e8 | -2.36688 | -44.5791 | 2026-09-07 05:01:00 | NPP-375D | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1435066c-1d1c-3c5c-b6fb-1892fca25f9b | -2.8615 | -50.45582 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 278eda77-fa49-37bb-9edb-1636d329959d | -3.54799 | -48.18328 | 2026-09-07 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e5ab2f4-a07a-3536-acb6-1c5036f17283 | -2.86602 | -50.44917 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bd9a5ad-a41d-3a60-8fc4-e718b921b602 | -3.14202 | -60.66624 | 2026-09-07 05:01:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 7f6017d2-1247-393d-bd02-2b703c7380ad | -2.7866 | -54.67612 | 2026-09-07 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4de8ccec-ad73-3c06-a43a-0e9e882da66b | -2.87507 | -50.43585 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b2f6faa-61c4-3a41-b531-77a188fa00dd | -3.20836 | -42.97967 | 2026-09-07 05:01:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5578b8ad-8f88-377d-894e-4a4f4b426021 | -3.11539 | -57.69443 | 2026-09-07 05:01:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06308d4d-f539-3308-8ebf-73bf03f9b5ce | -3.14929 | -60.65462 | 2026-09-07 05:01:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 664b315e-de60-3359-8689-88d62c5e5378 | -2.87779 | -50.4469 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ea05862-0b7d-3af0-ba7b-b08a6415ed78 | -2.88004 | -50.43251 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5f6f4e57-43c5-37a3-95dd-ab7d4ab8b9fe | -2.87948 | -50.43611 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 90a9917d-72ee-3db3-bae8-1f249574e3ec | -2.8795 | -50.45821 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b1fcab7-e9ad-3db1-8c00-87b3a743b911 | -2.87336 | -50.44663 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d37fa60-d3b3-3649-9ba9-81a39027a3de | -2.45778 | -57.91366 | 2026-09-07 05:01:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab7e5360-3b82-3c7d-85a1-3496a3af7c2d | -3.14717 | -60.63503 | 2026-09-07 05:01:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49907822-6089-3c7f-9238-70d570c73335 | -3.13989 | -60.64673 | 2026-09-07 05:01:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a375bb40-5434-3111-8bf4-f6b50a1fbf4f | -2.09187 | -49.533 | 2026-09-07 05:01:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d45f9c2-0469-3dc8-9fb2-262363b41d11 | -4.03567 | -50.87451 | 2026-09-07 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| adf41508-2e5c-3d91-98d4-4e1eef632d51 | -4.0794 | -48.95623 | 2026-09-07 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38cbc3d4-0833-3672-95bc-895ff88000e0 | -2.87279 | -50.45022 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac473347-ab69-3ad7-85fe-9601322af533 | -2.91213 | -54.1186 | 2026-09-07 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8cbf3a63-c11e-32b9-9a8f-9d56765256f6 | 0.22046 | -51.27958 | 2026-09-07 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8c42bc3-15ad-3fa6-bd01-bc6be31a5614 | -2.30251 | -48.58894 | 2026-09-07 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbdb4062-6856-3b86-ab09-1d6fcd572a9e | -3.24082 | -58.89525 | 2026-09-07 05:01:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 118ff309-06dc-3dae-8c74-dc4cf9e4cde9 | -2.8677 | -50.46047 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 384ec762-13df-3c39-9ca1-1876daa7a103 | -2.88118 | -50.44743 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69e3522b-fb34-3fa4-ba22-d4e34688f372 | -2.98254 | -54.02413 | 2026-09-07 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b1b4b52-28d1-3eb0-8459-ad3a2e89b5f4 | -3.07727 | -61.53297 | 2026-09-07 05:01:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7924e8b-4499-3629-9b36-c199b90a31fc | -3.54786 | -48.18571 | 2026-09-07 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab9dd909-55a2-36e2-9361-cd7f65d17242 | -4.11463 | -49.08947 | 2026-09-07 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b74824ec-1470-30e3-84bb-1bcc56cc5e6b | -1.49012 | -54.8262 | 2026-09-07 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f02e2326-fa1b-36e7-b491-d9b8aa456271 | -4.03904 | -50.87503 | 2026-09-07 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b69d839f-825c-3923-94cb-a64e79b3b266 | -3.37719 | -59.41663 | 2026-09-07 05:01:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73f36170-c13b-325c-ab42-206478313de5 | -4.04185 | -50.87912 | 2026-09-07 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1fbefe7-e099-3c74-923c-fcba76e0ab36 | -3.96352 | -55.40354 | 2026-09-07 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b85b8a3-6951-3d90-8ac8-659b7d0e055f | -3.38109 | -59.4225 | 2026-09-07 05:01:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 459135bc-2e66-3547-b253-0588a197f329 | -4.21892 | -48.56066 | 2026-09-07 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3624a98-8033-3616-9eb5-acd3a378a137 | -2.87846 | -50.43637 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79fa6314-70fe-354f-9a10-986d3f922599 | -2.884 | -50.45156 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ad73213-96c0-3e62-b7c3-8024cec4ee2e | 0.21546 | -51.29094 | 2026-09-07 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7405f1a1-9cf7-3928-8502-f15b782ae78d | -3.06079 | -51.24675 | 2026-09-07 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e67102af-a39f-3e2b-94e0-a6eb7fdc4ee9 | -3.67219 | -48.91307 | 2026-09-07 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e994501-1640-3aac-b7aa-1d9ddc9beb68 | -3.15958 | -50.82711 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e15bcb8-6ca0-3e51-8c63-4d24ec33f23d | -2.88569 | -50.44076 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64668d59-c523-3238-b55a-58c3cb34a6a7 | -2.86264 | -50.44864 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f97a5373-0b92-3007-abed-035c41400b4c | 0.21382 | -51.28061 | 2026-09-07 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 553c4949-2418-382b-9418-faa4c3180384 | -2.88625 | -50.43717 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25eb033b-2b9c-3104-8384-91b43de4ebdb | -3.14407 | -60.6538 | 2026-09-07 05:01:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02afab9c-7ec3-3fec-b6c2-8f18d73a763f | -2.8823 | -50.44024 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 80565ebe-c3e9-3525-827b-cff4c66c7bbc | -2.88174 | -50.44382 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| da5aa01d-7ab2-36ce-8898-dfdd59930e49 | -4.38351 | -44.39271 | 2026-09-07 05:01:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 83e6c835-c501-35c6-bf7e-ea11b6d86f38 | -5.15067 | -55.9697 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11c16e27-353a-31a2-b5d4-49733a48bde2 | -5.75831 | -47.63961 | 2026-09-07 05:04:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40ab7961-0a25-3aff-a4ac-1adec165d906 | -6.12674 | -57.73964 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d0bb6a1-d5a4-31a2-9117-54e8ed172d8c | -4.2948 | -59.95308 | 2026-09-07 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f82e6c25-99f9-3709-a83a-9e05a63b87ff | -9.74349 | -43.40413 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 68eedb0e-4409-3a24-bda1-db126e43a6d0 | -5.35383 | -56.02664 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab2b184c-51a1-3fa2-a91e-a8189f478603 | -11.32594 | -45.06302 | 2026-09-07 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61c6b18b-91c2-390a-b6fa-c2035b8f3fdf | -3.38297 | -61.32822 | 2026-09-07 05:04:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13e10dcd-dd6b-3ee8-b9ff-fea269e7fc38 | -4.43162 | -55.09953 | 2026-09-07 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1072f7c-2a7a-38e5-836c-1b1874732043 | -11.51268 | -49.61822 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 82bf8861-e833-35d0-8da5-27257fc70409 | -5.14253 | -55.97287 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff7ea772-e1dc-3d0f-8ec4-734175af7abd | -3.70247 | -58.93846 | 2026-09-07 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73678d43-6e4a-31cd-8c93-2eb7da8bee5d | -5.36269 | -56.01914 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 855040cc-0502-3997-8443-03c3e295a67e | -6.11482 | -57.63562 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c9fbd63-3783-305d-a214-5da657c5885c | -4.51134 | -55.71183 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c057a72c-3893-3c81-89e8-63754c372894 | -8.76165 | -62.42055 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f96c807e-7943-37d4-a42c-8135e303001d | -7.41615 | -46.55231 | 2026-09-07 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1154d63-2709-39d1-8093-baf6628b8cb2 | -5.35456 | -56.02226 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5f348db-9a6f-3a3a-82ad-9ddc593237e5 | -3.6393 | -59.54811 | 2026-09-07 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e54a8859-cac4-3fb8-b914-4ecaa95f9c8a | -8.76105 | -62.42388 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10d99d50-e3e8-3d44-8ce2-81b7f797bdbf | -9.74502 | -43.39229 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| a19adc28-96ec-3c15-b93f-8ab2fa24377e | -4.47285 | -55.09387 | 2026-09-07 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c193b5de-fbc5-3daf-8e19-d633b7add3dc | -5.35528 | -56.01789 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48bc0a4e-98ac-3527-b42c-c529bad3f751 | -8.75696 | -62.41605 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8188df6b-3bc1-3358-9f0c-a8ab30b9438d | -9.73065 | -43.41434 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b578f29-a906-3ec8-bfd3-d012485f6470 | -10.74273 | -45.07929 | 2026-09-07 05:04:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 7c2fc528-d64a-3b86-a25d-f86367b06d99 | -8.76417 | -62.4207 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c8ee7eb-c513-3a89-a79a-a35e1f975953 | -8.54047 | -63.88589 | 2026-09-07 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| acf52c10-b71d-3b97-b311-5b5b1d360d62 | -11.51409 | -49.60857 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0731ac0b-1eb1-34f6-a647-ec11aa5a31b7 | -11.52915 | -49.62245 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ddd9ff0f-e19e-3093-87a4-b2cf6b8dc883 | -3.95971 | -59.35896 | 2026-09-07 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c1247a8-9d71-3e54-b3ae-f2a564930ca3 | -5.98683 | -57.70414 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ab06372-808b-3b4f-a1df-eae5bbf4e7ba | -4.66824 | -55.63771 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14c4ffa5-2648-352b-93ba-81dd5aa0b443 | -6.13406 | -57.74064 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README21.md)
