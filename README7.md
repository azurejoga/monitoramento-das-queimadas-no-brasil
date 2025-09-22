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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57bb3cf5-265a-380f-a85b-c8f699dbbf15 | -20.274 | -55.4927 | 2025-09-22 01:50:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 32b0d9f1-73d4-38fe-9712-1927fbff94a7 | -22.9044 | -48.1873 | 2025-09-22 01:50:00 | GOES-19 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 0fda01dc-9723-33a6-987d-3b3134c83638 | -22.8529 | -50.6155 | 2025-09-22 01:50:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.7 |
| 990f6532-514b-3909-99b8-30d4f2955563 | -11.8814 | -64.9323 | 2025-09-22 01:50:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 10c48277-74ca-31c3-86e8-6732f8ea7f2b | -15.9591 | -59.3887 | 2025-09-22 01:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 2de2891b-f49c-31e7-a0fd-768fd9db5b49 | -11.6436 | -52.8605 | 2025-09-22 01:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 4fd5f7ad-11be-3167-b0a9-0abd192b9128 | -15.9969 | -59.4651 | 2025-09-22 01:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 1cc7759f-3d8c-3824-934f-f4fbbc4c9841 | -22.9278 | -47.446 | 2025-09-22 01:50:00 | GOES-19 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.0 |
| a3020b52-f962-3deb-bb7e-97201c9ff2a7 | -22.9285 | -47.4219 | 2025-09-22 01:50:00 | GOES-19 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 123.2 |
| aa00674b-1086-3185-83aa-278b863246cf | -11.6439 | -52.8397 | 2025-09-22 01:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 36e9d5e3-f3a5-3ec8-90e3-e6e5554a6a4a | -22.9075 | -47.4275 | 2025-09-22 01:50:00 | GOES-19 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.1 |
| 52f57935-6d86-3ce6-aab6-bd9d01bfca66 | -4.3197 | -48.0908 | 2025-09-22 01:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| bd9519fc-3066-3d15-9ad4-3047d7f8c54a | -10.2391 | -36.2586 | 2025-09-22 01:50:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 65.0 |
| 5852e28d-6d6f-3a1a-a818-261b9d778b8d | -11.8626 | -64.9332 | 2025-09-22 01:50:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 9112a98c-7fef-38ca-8f29-98064dd94384 | -10.16829 | -68.78909 | 2025-09-22 01:52:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 98f70ec7-fd5f-3da1-8e90-403f3c17f5ef | -7.2524 | -72.5117 | 2025-09-22 01:52:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 114d52a9-dfe4-3f15-8b06-7b9f0cc7a0a3 | -6.59453 | -62.92162 | 2025-09-22 01:52:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 6f20ef97-df34-3a83-948b-f845b15d8981 | -9.71976 | -69.07936 | 2025-09-22 01:52:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 5.7 |
| be7aaf39-14e5-38cb-b896-86158010b033 | -9.89139 | -67.90201 | 2025-09-22 01:52:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 1678ec7f-0744-36e6-ad97-4ac04f11fd46 | -9.4651 | -67.10374 | 2025-09-22 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8e05cca4-8024-3bc9-b018-1971545dafb0 | -9.8369 | -67.97917 | 2025-09-22 01:52:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a354817f-170d-3666-9b0b-8d543ab200f5 | -7.59158 | -69.89249 | 2025-09-22 01:52:00 | TERRA_M-M | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 048f9b6e-b1f7-3bda-85cb-9b0e65384874 | -8.63983 | -69.26643 | 2025-09-22 01:52:00 | TERRA_M-M | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0823d0ee-f9a7-301c-b9e9-9eee34349c8d | -9.47422 | -67.89288 | 2025-09-22 01:52:00 | TERRA_M-M | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7d6f210a-f186-3bca-b259-ac0b0cbddaa9 | -10.19851 | -69.35343 | 2025-09-22 01:52:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 958d1342-8e0f-3391-bdff-11bffc6c4433 | -10.02431 | -68.41031 | 2025-09-22 01:52:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c58b31ce-6617-3397-b8f0-43e9b7b757ff | -9.10808 | -64.00396 | 2025-09-22 01:52:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 76a637ea-56ad-386f-a6ee-4bb871bdc12f | -9.47272 | -67.09339 | 2025-09-22 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b35f6e32-2a37-3285-86de-3d0ae33cc695 | -9.09754 | -64.00559 | 2025-09-22 01:52:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d2b3c9de-22d9-3b66-93da-bad549e4a12e | -9.24719 | -67.39278 | 2025-09-22 01:52:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a100f803-0854-381c-b4f7-7bf2035fbff6 | -8.68789 | -64.2058 | 2025-09-22 01:52:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1765173d-f030-390d-8dba-0a336dd47557 | -10.17721 | -68.78783 | 2025-09-22 01:52:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 7.3 |
| caffd692-0d46-3e57-9e78-dfa3cc9095a4 | -7.3166 | -72.74829 | 2025-09-22 01:52:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7a134b70-a11b-34d4-9414-64c0e498228e | -9.8036 | -68.88364 | 2025-09-22 01:52:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 33c696c5-860d-305b-a1fa-6acee85fbb4e | -10.18943 | -69.35473 | 2025-09-22 01:52:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 77a913c9-b1f3-33fc-af53-18c2a1e9bec5 | -9.11604 | -65.50945 | 2025-09-22 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 7a319a97-46c9-397a-b126-785a474dfc0f | -6.63309 | -62.93315 | 2025-09-22 01:52:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 49597252-f93b-3233-ad28-395a36581e3e | -8.06584 | -70.33415 | 2025-09-22 01:52:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a7307516-991c-3f34-8b57-aec7571a986b | -8.69835 | -64.20423 | 2025-09-22 01:52:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| c1df052a-a03a-3e7b-ba43-ae5eeb0479a7 | -9.47399 | -67.10244 | 2025-09-22 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4f964bf6-c6f2-382c-ac4c-de949bd8a3c8 | -10.16477 | -68.69675 | 2025-09-22 01:52:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b7b67bad-f293-3155-a49c-380ceb97f66b | -7.56688 | -69.91146 | 2025-09-22 01:52:00 | TERRA_M-M | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b58fbdc8-ca48-3fc7-b596-1d452a5af3be | -10.19662 | -68.78851 | 2025-09-22 01:52:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 11.0 |
| bea87d64-6cc4-3849-b231-45d018a6b82b | -9.55736 | -68.56183 | 2025-09-22 01:52:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 689fed42-bbe3-318f-9bd9-557a5bf35f78 | -10.3572 | -46.0585 | 2025-09-22 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| a9d4eea6-4fd1-390b-959d-d4b30eebc1c2 | -4.3197 | -48.0908 | 2025-09-22 02:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| d379b4af-1d95-30cf-9a82-001979626d4e | -10.3952 | -46.0538 | 2025-09-22 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| c15d2f9b-67d3-3bac-b980-dcfdfaf5ddb5 | -11.6439 | -52.8397 | 2025-09-22 02:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| d7ee7557-9b52-3269-a9ad-a45ea5ed9ee7 | -11.6436 | -52.8605 | 2025-09-22 02:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| d9ab44df-d4cb-34c0-98c8-107854767c03 | -15.9969 | -59.4651 | 2025-09-22 02:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 198ebcf5-0c66-3cd4-bb5f-2731529ca9a0 | -22.832 | -50.6203 | 2025-09-22 02:00:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 101.8 |
| e582effa-0c96-3678-aa2a-0a808317bb23 | -20.274 | -55.4927 | 2025-09-22 02:00:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 2cbf99d9-c861-3351-9111-7e0e3e5c0fc9 | -10.3568 | -46.0812 | 2025-09-22 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 955a2fcc-bc68-3f04-8a33-449c18e421ca | -10.3759 | -46.0788 | 2025-09-22 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 166.6 |
| 83119c81-0a63-343d-85e2-962cc4a3c903 | -10.3762 | -46.0562 | 2025-09-22 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 243.1 |
| 3a484edf-2015-3cbb-9687-0cbfe9e60b62 | -10.3949 | -46.0765 | 2025-09-22 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| b8e6a8c3-f1fe-3353-b009-64ff596c5be0 | -22.8117 | -50.6021 | 2025-09-22 02:00:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.2 |
| 3c10c17e-f16e-3563-bbd4-dd4641fec307 | -22.8529 | -50.6155 | 2025-09-22 02:00:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.3 |
| b1038c42-3e2b-3ad3-8ac8-b0121333e935 | -22.8326 | -50.5973 | 2025-09-22 02:00:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 97.3 |
| 2b9d10e5-cefd-3f38-baaa-9eeb483e8c5b | -11.8814 | -64.9323 | 2025-09-22 02:00:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 9f909f6f-2387-38af-90a7-6191b97b5e20 | -15.9591 | -59.3887 | 2025-09-22 02:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 4c25e534-6823-3b91-9f95-a0f8baf41300 | -22.832 | -50.6203 | 2025-09-22 02:10:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.6 |
| 7c1ebe60-3ba6-3e14-a418-c8f21bd1e127 | -22.9285 | -47.4219 | 2025-09-22 02:10:00 | GOES-19 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.5 |
| 876c28f1-2c25-32c7-af89-c57dcfe3a9bf | -10.3572 | -46.0585 | 2025-09-22 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| c2bda7c8-8bf0-3c3c-a606-ebe0a5cb2358 | -15.9591 | -59.3887 | 2025-09-22 02:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| a38f07b9-8db4-3b6a-81c2-c63b974544c9 | -11.6436 | -52.8605 | 2025-09-22 02:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 5826c071-1f78-3a39-9b6f-7a5cdf133aa7 | -4.3197 | -48.0908 | 2025-09-22 02:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 7986e58b-4c42-3086-aa94-c571549db6a6 | -10.3762 | -46.0562 | 2025-09-22 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 4c0ed888-e432-3d6f-92aa-7269ee665003 | -22.8117 | -50.6021 | 2025-09-22 02:10:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.2 |
| a3057492-64fe-314c-8fa6-8ad1a08e6cdb | -6.9024 | -44.7656 | 2025-09-22 02:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| e34d462a-af9f-36c4-828a-539f500a490d | -10.3949 | -46.0765 | 2025-09-22 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 2e248224-b3bc-3402-83e1-948ccd8ba08a | -22.8326 | -50.5973 | 2025-09-22 02:10:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 107.1 |
| 92649dcd-fa85-3269-bc3d-30e026d15344 | -10.3759 | -46.0788 | 2025-09-22 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 244357a8-39ba-3c56-8717-fa67f20363e4 | -15.9969 | -59.4651 | 2025-09-22 02:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 2ffaf2d9-b550-3aa5-9e9e-53af136055ef | -10.3765 | -46.0335 | 2025-09-22 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 08d38672-a835-3b05-b281-9ac6c0a71e98 | -10.3568 | -46.0812 | 2025-09-22 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 1eadac3a-5dbc-307f-a14d-0c4c0893f973 | -10.3949 | -46.0765 | 2025-09-22 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 37603efc-64f5-37ff-845f-3552a6905eef | -10.3762 | -46.0562 | 2025-09-22 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 518.3 |
| ed73dcad-61af-3a51-bcb0-2e608b0639d0 | -14.8067 | -51.4024 | 2025-09-22 02:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| ce0ec759-bc05-375f-9b98-8cc297bc06f1 | -22.9285 | -47.4219 | 2025-09-22 02:20:00 | GOES-19 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.6 |
| e6174ec7-e23a-3a07-9392-01c43edf6352 | -22.8326 | -50.5973 | 2025-09-22 02:20:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 123.7 |
| 037b8886-bad9-3145-9a40-1b877e8d118b | -10.3572 | -46.0585 | 2025-09-22 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 272.2 |
| 85aaae44-9b20-3a11-88b4-13da05ee0a98 | -10.3759 | -46.0788 | 2025-09-22 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 202.6 |
| 78e446c2-124e-356d-88d8-71273541ab15 | -4.3197 | -48.0908 | 2025-09-22 02:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 3ce57633-6431-3a0b-a58d-faf7df927fb3 | -22.8117 | -50.6021 | 2025-09-22 02:20:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 106.1 |
| fa2b00a5-8e4f-3e90-acf5-3c46365eb846 | -22.832 | -50.6203 | 2025-09-22 02:20:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 103.0 |
| bbe87ce8-b9f7-3bcf-a722-b570b12d0cea | -22.832 | -50.6203 | 2025-09-22 02:30:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 116.9 |
| a8f6b902-92fb-39dd-bd6a-a188f15f8519 | -10.3572 | -46.0585 | 2025-09-22 02:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 3a816e19-ef40-36b4-922b-3118f049b556 | -10.3759 | -46.0788 | 2025-09-22 02:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| feaf800c-f347-3aaa-99d5-63b1cdb688bb | -22.8117 | -50.6021 | 2025-09-22 02:30:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 108.9 |
| f26ba625-627c-39be-8482-61c94d4e1e6c | -16.0163 | -59.4633 | 2025-09-22 02:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 9d0f81fa-3913-3f2c-9566-ec095a297768 | -22.8326 | -50.5973 | 2025-09-22 02:30:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 151.9 |
| 76683a9d-5fee-396d-86b9-f302d661e7d9 | -22.8529 | -50.6155 | 2025-09-22 02:30:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 104.6 |
| 55ef2bf9-5c43-3fd9-a73f-cafb15c8af06 | -10.3762 | -46.0562 | 2025-09-22 02:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 203.1 |
| 19be6c7e-5bba-373b-8df3-a21ef0545ef3 | -11.8814 | -64.9323 | 2025-09-22 02:30:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| e5d0c15e-8d0b-3e79-ad5c-2197d814293b | -15.9969 | -59.4651 | 2025-09-22 02:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 136b61f1-416c-3beb-acb4-2823703a4c1e | -7.233 | -43.7449 | 2025-09-22 02:30:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 60f28f99-489c-3d33-98df-bcac791e0949 | -10.3572 | -46.0585 | 2025-09-22 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| d929c8ad-0297-3893-9734-ece3108c29c5 | -4.3012 | -48.0917 | 2025-09-22 02:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 44549ab6-3127-34ec-be3a-28eac37903f2 | -20.2537 | -55.4959 | 2025-09-22 02:40:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 71.3 |


[Clique aqui para ver as próximas entradas](README8.md)
