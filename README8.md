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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d85cb2f4-53e6-3e27-8592-56a440b7b961 | -3.00079 | -50.46942 | 2026-09-26 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f00a3e8f-76d5-3013-bfd4-35e59a1407ba | -5.7308 | -45.06473 | 2026-09-26 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bba879fc-0963-3fc8-99db-d920ba0de0a0 | -5.48443 | -45.93895 | 2026-09-26 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aec856d0-9f77-38cd-aa6d-e0b5b4168bab | -5.77734 | -45.09689 | 2026-09-26 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a364c52d-bf5d-3b40-b506-f60405ae4e32 | -5.68125 | -45.87058 | 2026-09-26 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22a04b54-0193-3007-97eb-de6b19e7bde5 | -3.94044 | -42.98959 | 2026-09-26 04:06:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 483986b0-7970-36b1-b7c9-38f0719ddaa7 | -3.94864 | -42.99098 | 2026-09-26 04:06:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ab693ba7-1c4a-3ba4-a488-c7d4a796a422 | -4.26981 | -44.58749 | 2026-09-26 04:06:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 017114ed-f932-31e9-9c3f-05da2d221c2e | -5.74532 | -45.06255 | 2026-09-26 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0a292dd3-b382-37cc-a602-dd2b416269e2 | -1.7839 | -47.83911 | 2026-09-26 04:06:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96d64e65-b2ce-35a6-8bed-29721220b919 | -5.73995 | -45.06643 | 2026-09-26 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e9637bff-64ff-3bb8-bb01-5b12674288be | -5.74294 | -45.07668 | 2026-09-26 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7985a34d-977b-38b9-91be-b7b585ac54d7 | -3.42486 | -50.4253 | 2026-09-26 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f6045d0-7f48-39f0-b284-0c6fb05ff540 | -5.6861 | -45.87144 | 2026-09-26 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78a82a59-b2ef-3ea2-bcae-b12b31159f43 | -4.28526 | -48.61026 | 2026-09-26 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0e3b4c15-32dd-34f3-af05-f9686308828d | -3.93396 | -40.59301 | 2026-09-26 04:06:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d52c411c-3d6a-31e4-b7b2-749b1684a8bc | -3.48937 | -43.34705 | 2026-09-26 04:06:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 034ba6ff-fcbe-3b5e-b21c-f7d6ff837156 | -5.74075 | -45.06168 | 2026-09-26 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cd742ce1-f08e-3425-bf99-af29ec935540 | -3.41913 | -50.41829 | 2026-09-26 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e1532290-ba97-3c50-8f7e-5967aec7da31 | -3.42384 | -50.43122 | 2026-09-26 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 131fcfa0-b7cf-336f-bd1b-7d3e8b1eba42 | -1.78459 | -47.83496 | 2026-09-26 04:06:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24d51292-4a1b-310d-bdbb-a4fab9d4c890 | -4.82824 | -43.55644 | 2026-09-26 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdaa3f65-20c3-3f87-a57f-62488469e14c | -3.97047 | -47.20291 | 2026-09-26 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f420b925-f579-3489-b3ab-3f8e8f5cdfa0 | -4.30592 | -49.13188 | 2026-09-26 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4508348b-59ad-32ea-9bb1-264c6b2ca91e | -4.30436 | -49.13293 | 2026-09-26 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e13acc1b-0dbb-33c4-a29e-90e06cbd99ae | -5.73538 | -45.06557 | 2026-09-26 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c156b077-98ad-3ead-b81a-46934b3fd8c9 | -4.30756 | -49.12237 | 2026-09-26 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35a705e7-9623-3c99-9d63-1c1b5ef2d5f4 | -4.29978 | -49.13073 | 2026-09-26 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d6bbb96-f277-3ccc-8224-2f171fe2a558 | -5.51794 | -40.88195 | 2026-09-26 04:06:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 870dceed-9d2c-3811-a814-fbbc0f1b39a9 | -3.93753 | -40.59358 | 2026-09-26 04:06:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e84cbd34-8d0a-3458-bc6e-ee404a1eef2c | -3.94513 | -42.98666 | 2026-09-26 04:06:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0a227c59-3958-3e4d-a3fd-88e10f045b7b | -4.30061 | -49.12597 | 2026-09-26 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0781edaf-94a6-307f-9bd1-99844045165b | -4.27358 | -44.59285 | 2026-09-26 04:06:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aed67f55-ce94-3139-887f-7177568a49db | -6.00038 | -44.91159 | 2026-09-26 04:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a3cd014-765f-3f31-918f-62508cc8b227 | -4.30692 | -49.1187 | 2026-09-26 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa6ceb0a-0a9e-36ea-b75e-34b4f8d96f3b | -3.24198 | -43.22461 | 2026-09-26 04:06:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d7f264f-65bd-3a58-9ce7-4d87472bb801 | -5.77412 | -45.08412 | 2026-09-26 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 28e655c6-7e72-35ae-99f1-00285ea2f5e2 | -5.77494 | -45.11135 | 2026-09-26 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8088a1a-96eb-3bb5-ab8f-e1f6dacea67d | -5.68218 | -45.8652 | 2026-09-26 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03267335-35bf-312e-8c37-087a6d9c1a8d | -5.77655 | -45.10167 | 2026-09-26 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8e41605-d364-308c-9c2a-0d862badb8bf | -2.99903 | -50.47615 | 2026-09-26 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af00dd16-c119-3c7b-9508-41ca306ca8ae | -5.77354 | -45.09135 | 2026-09-26 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8c0f8d08-a871-37c7-9b37-76c8ce8266ad | -4.30674 | -49.12713 | 2026-09-26 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e645af48-d72e-3780-8c3c-0e700f2929f5 | -2.99219 | -50.47522 | 2026-09-26 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06badbf3-fb20-3f17-b7f5-693bfa08c391 | -2.99972 | -50.47548 | 2026-09-26 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fa420804-c0bf-3c17-9c67-e4735a7c28f4 | -5.36443 | -36.84822 | 2026-09-26 04:06:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b0c98ad6-bda7-3019-8730-b476c26a8e4f | -3.41808 | -50.42434 | 2026-09-26 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c8cb830-7bec-3fe3-ab1b-7a98fddcf6f3 | -3.80172 | -51.02636 | 2026-09-26 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a02609b-d8c5-31c2-afcc-02a11b684901 | -3.44995 | -50.08285 | 2026-09-26 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b80ac03b-404b-3dd2-bb74-8d4c46a986a4 | -6.02136 | -35.43644 | 2026-09-26 04:06:00 | NPP-375D | VERA CRUZ | RIO GRANDE DO NORTE | Brasil | 2414803 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1fff12bf-f594-3817-b529-08c8409cf7ad | -4.29897 | -49.13547 | 2026-09-26 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 71a793d7-ea76-3a33-8e01-f0f239b83db7 | -3.987 | -48.43177 | 2026-09-26 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68c380fc-dd04-3ff0-8e23-990d9afe5e80 | -4.26903 | -44.59209 | 2026-09-26 04:06:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ca522cc-bd22-301b-8739-ee042833904e | -3.98111 | -48.4306 | 2026-09-26 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adbc032d-3359-3223-8d72-5506ecfb22c9 | -5.7733 | -45.08883 | 2026-09-26 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 33fe841b-e6dc-3292-951a-ee89275978eb | -3.77158 | -42.39857 | 2026-09-26 04:06:00 | NPP-375D | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f2955fa4-e314-354a-ada1-d0e511934b3e | -5.77575 | -45.10649 | 2026-09-26 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34976ebf-a3aa-3a33-bd13-a538966cd01f | -4.29823 | -49.13178 | 2026-09-26 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 38997978-d059-3108-a7ed-6d8555c9ebde | -5.73915 | -45.07118 | 2026-09-26 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6402ec4e-f417-380c-9bd5-a58afd93d5dd | -3.23715 | -43.22774 | 2026-09-26 04:06:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5a249ea-ae7f-3c34-9f82-f3212b8150ed | -6.02492 | -35.43699 | 2026-09-26 04:06:00 | NPP-375D | VERA CRUZ | RIO GRANDE DO NORTE | Brasil | 2414803 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d5c32543-f077-350f-a327-48e366494d54 | -3.42421 | -43.16599 | 2026-09-26 04:06:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eab3ee84-2662-3207-8023-291a0141c04f | -5.21367 | -46.02739 | 2026-09-26 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cde5c16d-e725-3903-a14b-b416ee88e0c0 | -2.99322 | -50.46918 | 2026-09-26 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c5f8248-7940-3f29-a7fc-4df03c5a18cb | -4.30521 | -49.12819 | 2026-09-26 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7c9fb7bd-6f60-398a-a53e-e414b18e4830 | -5.74373 | -45.07202 | 2026-09-26 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0148e849-c506-32f7-94f1-0d5996d03705 | -4.60623 | -44.65151 | 2026-09-26 04:06:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8f0765dc-472e-38f9-9187-b2433f0d0525 | -5.73457 | -45.07033 | 2026-09-26 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e816e33-a78e-3829-b321-d2794b16f77b | -3.94454 | -42.99028 | 2026-09-26 04:06:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 02db5918-ad84-3edc-96dd-a271da02c7f1 | -3.77553 | -42.39926 | 2026-09-26 04:06:00 | NPP-375D | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d56e57f6-538f-3f41-a496-3bb5c46f927b | -3.00007 | -50.47006 | 2026-09-26 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5683c45e-1c02-39bf-88f8-7b37fee93edb | -5.74452 | -45.0673 | 2026-09-26 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 41fe671a-cf98-32ea-869a-f3fb04de26f9 | -5.76894 | -45.09062 | 2026-09-26 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8f5ff2c-c3bd-335f-b048-cb3de517616b | -5.77433 | -45.08658 | 2026-09-26 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d882e02e-30a6-3bc3-b9ce-1d47579c939c | -4.30607 | -49.12342 | 2026-09-26 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da4320d4-fa0e-3d36-b964-bfb1233eb28e | -3.69146 | -39.57555 | 2026-09-26 04:06:00 | NPP-375D | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 810ed63d-a342-3f81-a2b8-f90f80db7887 | -4.37233 | -42.98983 | 2026-09-26 04:06:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c10448b4-1bf6-3f6d-a757-f4c87f6827ba | -3.98184 | -48.42635 | 2026-09-26 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81223c7a-63ea-30bd-b581-ed74ce7ed923 | -2.99287 | -50.47455 | 2026-09-26 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f3d3750a-0030-3b72-a8b6-031634e8ecde | -11.93677 | -50.58659 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 39e5b3fb-7903-3428-9b2b-f36a021026f8 | -9.47755 | -40.34203 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a4f2554e-6053-3f0f-86ea-6db2b6e8ced1 | -8.15008 | -44.44656 | 2026-09-26 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65799194-2405-3b1a-a3ff-3e44bdace1c0 | -9.47475 | -40.33785 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f6498d9e-1d4a-37ba-9826-3864055be938 | -9.48384 | -40.32448 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c3957d68-682a-3429-b34f-2d6d1fa837c2 | -13.42169 | -43.67086 | 2026-09-26 04:08:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e177539-c59e-3e9c-8dd5-f25ea748ba03 | -9.48326 | -40.3281 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 14df2fb2-1216-3c59-b2b0-5fdf4d04679e | -7.35368 | -42.0857 | 2026-09-26 04:08:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6a429492-49e9-35b0-ae76-f9249c6a05f5 | -13.47701 | -42.48121 | 2026-09-26 04:08:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0729494b-0f68-3afc-8317-893c3bbac1b1 | -6.84101 | -43.50846 | 2026-09-26 04:08:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8652b413-b715-3278-a0b1-8c561ad241f4 | -6.96858 | -41.34233 | 2026-09-26 04:08:00 | NPP-375D | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 1181ef3f-ee38-3bc2-808c-ba776df69437 | -12.26467 | -50.72676 | 2026-09-26 04:08:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b1a62c4a-6225-36fa-acec-b13ca3a6887c | -11.79675 | -50.65544 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1140cf1c-716a-34aa-ad85-f0317d7504b1 | -7.34998 | -42.08508 | 2026-09-26 04:08:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5ac80758-87e3-3291-bb07-14a3adfd69d2 | -8.34381 | -44.15589 | 2026-09-26 04:08:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dacc25e1-4f0c-3eb6-9bc9-49f991a32077 | -9.46786 | -40.35904 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 09d7bd5d-53b5-3e9b-be60-c6d20e4277dd | -13.79937 | -43.75048 | 2026-09-26 04:08:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a4d898d2-df56-3d14-aed5-fc985d8137b6 | -11.94607 | -38.29299 | 2026-09-26 04:08:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9a835ac2-c680-3986-a86d-4afc88a6b47b | -9.48547 | -40.3359 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 382612af-e7e0-3d9d-a5d1-9b3c60c486a5 | -12.2715 | -50.7236 | 2026-09-26 04:08:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2c0a40e0-6b7a-30a9-90d7-1eb9e4036bca | -9.46975 | -40.32587 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 193.4 |


[Clique aqui para ver as próximas entradas](README9.md)
