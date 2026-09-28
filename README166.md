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

## Dados Diários - Página 166

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7ff3bcc-c579-3305-a9c1-7d4c4d9a5e99 | -3.14754 | -54.08327 | 2026-09-28 17:11:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 765b2a22-9af2-3ced-b8ee-629358a29b27 | -2.14126 | -48.96096 | 2026-09-28 17:11:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1ed78e65-fb84-3d0c-a0af-3ae4b852cf1c | -2.07271 | -48.13632 | 2026-09-28 17:11:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 5e2a1002-d481-3a2b-9425-5e0d428be676 | -1.4621 | -51.7023 | 2026-09-28 17:11:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 35f1606b-47b7-317e-91dc-fa54cb75da20 | -3.01383 | -54.21845 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| a8edf070-8b69-3d63-91a2-7a861291934d | -3.07597 | -58.00911 | 2026-09-28 17:11:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 35869c51-bb08-33ce-8fbe-2953cfa5f6f7 | -2.47624 | -54.87406 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e7963fad-0ae3-30d1-99f8-760297b4b910 | -1.90477 | -52.0667 | 2026-09-28 17:11:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| af81c9bb-f429-31c5-aca7-01e968f3e61f | -3.51244 | -50.31184 | 2026-09-28 17:11:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| fbe971e3-745c-38ec-b955-dcba16809ce5 | -3.12535 | -54.62577 | 2026-09-28 17:11:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 894acd38-87ca-3315-8f15-989e1bc0ddd4 | -1.2093 | -49.22099 | 2026-09-28 17:11:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| fc6c8012-20cf-3a55-970e-78e90110b9d0 | -3.00426 | -50.44206 | 2026-09-28 17:11:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| eff6f0ba-ccdb-37b8-8666-95e7c11c40d5 | -3.87291 | -51.79959 | 2026-09-28 17:11:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cb3389e9-6543-3bdb-8a00-5e481032a4d8 | 1.13007 | -50.00641 | 2026-09-28 17:11:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 3f837ae8-e0e0-3e36-90e3-6b3f0d80f225 | -3.0009 | -54.74866 | 2026-09-28 17:11:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 0bef99c5-d4fe-321c-895c-9b0f9f1192d4 | -3.51181 | -50.30788 | 2026-09-28 17:11:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 04df5096-7cef-32ad-ac69-d024a52fe9e3 | -3.80988 | -55.41228 | 2026-09-28 17:11:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f6c29539-dad6-3cfa-b7fa-cb4be0b7fb37 | -3.63787 | -49.96348 | 2026-09-28 17:11:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ee46461d-8d71-3328-9bfc-a0be064da0dc | -1.46902 | -48.93406 | 2026-09-28 17:11:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 81609451-f764-328b-a4c0-5d0efecd7d56 | -1.42683 | -48.88641 | 2026-09-28 17:11:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 7f9b820f-b031-3e9d-81a8-66592eb95dd0 | -3.2034 | -42.45613 | 2026-09-28 17:11:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| beaed0f6-024a-3e32-9e06-35ebfc7fed92 | -3.15156 | -54.08648 | 2026-09-28 17:11:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 6532fc11-9042-3ea7-ac1a-c006da508bab | -2.95408 | -57.80837 | 2026-09-28 17:11:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 24f38d05-dc18-34f9-a2d9-31f976ae29d0 | -1.68514 | -54.6572 | 2026-09-28 17:11:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 7b9decc2-e263-3b86-ad15-2c52902e13c0 | -3.76201 | -51.8103 | 2026-09-28 17:11:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f55dd043-0cae-341d-a6f7-fdedb3de79dd | -1.43167 | -48.88565 | 2026-09-28 17:11:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 16456383-7c66-30c8-9a13-a97adeed9d51 | -1.97467 | -54.25771 | 2026-09-28 17:11:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 21fc325d-4dbe-3b68-80c9-1cba526ed530 | -1.71302 | -49.68455 | 2026-09-28 17:11:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| d62935d4-c9e3-3dc6-b211-bd5727514515 | -3.81584 | -50.72191 | 2026-09-28 17:11:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8aa0afc2-d68e-3231-85eb-c78840076dc7 | -1.7896 | -47.94606 | 2026-09-28 17:11:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 653fa992-7e90-3973-8cbd-be121b6a79aa | -1.46838 | -47.76087 | 2026-09-28 17:11:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 460eec68-d486-39c9-8a10-cec7bfd0dc5e | 1.25628 | -50.70962 | 2026-09-28 17:11:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 23c3004f-d49c-3429-974b-1114655a7a6c | -1.03069 | -49.23599 | 2026-09-28 17:11:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 1407a280-b243-35ed-abf2-9f6501d1f42c | -2.85977 | -54.13101 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9ea0ed61-de5f-3329-b353-96d444a7b5d5 | -4.31575 | -50.4003 | 2026-09-28 17:11:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| eea88188-90e4-374b-b107-ce207d7c31fb | -1.04852 | -53.56025 | 2026-09-28 17:11:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5dfcb9f2-70f1-375b-b778-21d783c149e4 | -1.6304 | -47.69555 | 2026-09-28 17:11:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e6255e7f-236f-31b2-85e1-7f92abc3a4d2 | 1.13079 | -50.0015 | 2026-09-28 17:11:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 7b85c11c-da32-380a-841b-e543eb4ea658 | -2.29029 | -54.71804 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 97898d91-4611-3e27-9092-f81357eaa9b4 | -0.30108 | -48.38961 | 2026-09-28 17:11:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 95790078-1da9-350b-85ce-7763c5eea1de | -3.80083 | -56.80424 | 2026-09-28 17:11:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8f9a21a9-8ac5-3321-a289-cbd3d6fae5f5 | -3.70811 | -50.96335 | 2026-09-28 17:11:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| dbc2ac54-1dce-396d-97a6-d60673017667 | -3.72726 | -50.64453 | 2026-09-28 17:11:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 9f33c0eb-4382-300a-9e8b-3253ea9a668a | -3.70785 | -54.21422 | 2026-09-28 17:11:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e174e92f-368f-3e61-ab63-904d4730bfe2 | -3.21382 | -53.40695 | 2026-09-28 17:11:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 17796625-4505-36bc-8ecd-b3d59a38de09 | -3.68839 | -57.07156 | 2026-09-28 17:11:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 895c22a8-447b-3df9-a71e-6fcd9296f303 | -1.97351 | -54.25008 | 2026-09-28 17:11:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 21cc13cf-fdeb-3fe7-91a3-0328a8a512f8 | -1.68799 | -54.65298 | 2026-09-28 17:11:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 27465e44-deec-37b3-810a-d0f027260e03 | -3.14697 | -54.07951 | 2026-09-28 17:11:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a17f6e16-61f5-3a1d-92a0-29b3b92eb88b | -3.07542 | -58.00546 | 2026-09-28 17:11:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| cb7000c1-722b-30a9-bbf7-01cdf25bdc2e | -3.67939 | -47.49762 | 2026-09-28 17:11:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 68ccb0b6-b325-3a34-a330-f379f4976913 | -3.23221 | -53.95 | 2026-09-28 17:11:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f1adaec0-b34d-3b01-9b5d-f2cc49ec5d70 | -2.0484 | -48.72079 | 2026-09-28 17:11:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| d4a1511a-214b-3d89-8397-b97f080832fd | -2.09808 | -49.56093 | 2026-09-28 17:11:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| ff47c5f1-cca5-3de0-9cd9-15aec267954a | -2.15158 | -53.70783 | 2026-09-28 17:11:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8fcc555a-8ad2-3b06-b966-493aa91d18df | 0.34983 | -51.44537 | 2026-09-28 17:11:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 15.9 |
| cba98d32-78e5-37b5-90f6-eed3b870fb95 | -1.40796 | -47.38291 | 2026-09-28 17:11:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bed0afbf-1322-3b3a-92a7-5469b8f38d25 | -1.44304 | -48.89477 | 2026-09-28 17:11:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| b2294322-172f-30b6-9a79-957e40d34fd7 | -2.95354 | -57.80477 | 2026-09-28 17:11:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 98c98503-bde4-34be-bf85-ab2e6dfbbe95 | -2.11251 | -49.21078 | 2026-09-28 17:11:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3f8739f3-234e-3a48-bd9b-ccbbc865cb8f | -0.43185 | -52.02868 | 2026-09-28 17:11:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3439cde0-0f34-39c8-a4b0-a38bf170afd2 | -0.44772 | -52.02611 | 2026-09-28 17:11:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| eab97fd7-ae97-3710-bcc7-53ec98fb6d7b | -3.73078 | -50.64012 | 2026-09-28 17:11:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 631c72a0-22d2-3b38-bc72-e6dfb8a5ad0b | -1.97064 | -54.25447 | 2026-09-28 17:11:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 0fb0935c-01a1-3fde-9536-d0a3aaadd975 | -2.95778 | -50.31447 | 2026-09-28 17:11:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c387a14f-d208-3837-b975-cfee2ce4613e | -2.1522 | -53.7118 | 2026-09-28 17:11:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 73e4c94b-439d-3951-93a4-78010014a134 | 0.09554 | -49.84457 | 2026-09-28 17:11:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 03ba9ca8-df64-3fd7-ad39-6450042d6dfc | -2.31929 | -53.99416 | 2026-09-28 17:11:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6127ea76-c046-399d-8e79-480eb9cc0189 | -3.36653 | -49.16596 | 2026-09-28 17:11:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ec92825d-0a2e-3d82-9f19-58fb6db20d2b | -2.89815 | -54.08266 | 2026-09-28 17:11:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 227b7fb8-d908-3824-b1b4-a7af89369325 | -3.42066 | -48.33516 | 2026-09-28 17:11:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 22db4fe5-6cf0-3aa7-a3d2-cd4c5b331075 | -1.65119 | -45.02256 | 2026-09-28 17:11:00 | NOAA-21 | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 5580acd8-bb21-36f6-9da7-a20a879f8243 | 0.63922 | -54.38785 | 2026-09-28 17:11:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d9622948-3138-3867-8fc6-37b4507123aa | -2.0669 | -49.5419 | 2026-09-28 17:11:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| ef8a9863-d6c7-3758-8266-5e96bd9e2e42 | -3.79436 | -51.79063 | 2026-09-28 17:11:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 089716b9-4c2d-3a1d-8f80-95887f061aa4 | -3.07756 | -49.36053 | 2026-09-28 17:11:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 189c96f4-c082-3fe2-9f7a-e4941de23ed8 | -3.15041 | -54.07895 | 2026-09-28 17:11:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| dd4a6d8a-d4e3-3d79-858d-f13640c6acc8 | -5.85948 | -63.93183 | 2026-09-28 17:11:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 182e3660-9476-3e63-aab7-d4cd5b677708 | -1.23376 | -54.09937 | 2026-09-28 17:11:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 08b20c54-b809-38b7-a6e8-b7302fd44e93 | -1.29683 | -49.05644 | 2026-09-28 17:11:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a5ec13cf-5e24-3b09-8b66-1a50a4c07446 | -2.8982 | -54.10584 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 8952da6e-affa-3abe-917f-b982b944001e | 0.35043 | -51.44154 | 2026-09-28 17:11:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 13.7 |
| cc227f22-5d0b-3f72-9210-3b71a8d68434 | -1.76539 | -53.76512 | 2026-09-28 17:11:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 44187292-6f93-375f-8c01-fda293cca28f | -3.20593 | -42.44755 | 2026-09-28 17:11:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| bef894d0-210c-3050-8179-d605246af4ab | -1.42842 | -52.58922 | 2026-09-28 17:11:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8e81b8a0-0ecc-3899-9050-0186c1f266f8 | -1.20852 | -49.21591 | 2026-09-28 17:11:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| e69e4fd1-af58-3de3-9361-da220a73eb3c | -1.68564 | -50.00956 | 2026-09-28 17:11:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cbf1205c-08bc-3ade-85f3-d408d959d8ec | -3.07658 | -54.37555 | 2026-09-28 17:11:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3f84f240-a6ab-3eba-a762-3a28f01277a5 | 0.63629 | -54.38338 | 2026-09-28 17:11:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| ca320705-60d0-3ae0-a97e-debc266ed3cb | -3.02007 | -53.86889 | 2026-09-28 17:11:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 46255b4f-e277-3694-8557-8ddb17845723 | -2.96067 | -54.0807 | 2026-09-28 17:11:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1e16dc4d-379a-36e4-9e9b-385de0c33895 | -3.57961 | -45.05844 | 2026-09-28 17:11:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 17c981bc-0739-313e-988d-5df26c4ae7b0 | -3.22876 | -53.95054 | 2026-09-28 17:11:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1df601ac-18da-3b51-a1bc-b011d8677cd2 | -2.96008 | -54.07693 | 2026-09-28 17:11:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9777ed95-ecca-370b-8962-b466888c9ca4 | -1.76478 | -53.76115 | 2026-09-28 17:11:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8c6538ef-e495-3f34-a464-420d9260b1c5 | -1.88736 | -48.68927 | 2026-09-28 17:11:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 21ea01cf-8cbf-3cbe-813e-29242ec4b216 | -1.42136 | -51.41188 | 2026-09-28 17:11:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 616f976e-7657-3900-afe4-95e0bc7adc50 | -2.79831 | -54.64302 | 2026-09-28 17:11:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 9ea180c5-4f33-3aa0-ab53-9e34fc5072b6 | -3.86284 | -52.00774 | 2026-09-28 17:11:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 20a7fb1b-569a-3b36-ac67-85e49a58a419 | -2.82906 | -49.6543 | 2026-09-28 17:11:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README167.md)
