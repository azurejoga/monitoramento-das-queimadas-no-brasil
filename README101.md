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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8aa1853-9ddd-35a2-b81d-3a5b203470b5 | -3.9956 | -56.2651 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 66d7efad-1991-3d07-bab2-9b4d6c48c645 | 1.76511 | -55.57072 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68b73c1c-4588-3f2e-a6a6-35465f965775 | -2.59958 | -48.25882 | 2026-10-07 05:40:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9bc44478-b5a6-390c-997f-493fd062e470 | -3.17745 | -50.4396 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f718b6a-b123-343f-8708-00296705fdda | -3.10824 | -54.16808 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 74bd3a57-d184-3a14-8d16-049ec0ab4222 | 3.1503 | -60.60505 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 93c5e38b-14f6-37c6-9814-6d21543065b1 | -3.17137 | -58.63978 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a3a4af3-524e-3d60-a17c-3e5aad84f579 | 2.43701 | -50.84643 | 2026-10-07 05:40:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 25abfc3c-ae9d-37e0-aa7a-7afe20192ab2 | -3.38534 | -58.20127 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66b8e09c-4ff3-3e0a-83a8-266998ca1886 | 4.14648 | -61.24752 | 2026-10-07 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f3409c9-5fca-3b09-9990-6d484d8a2da1 | -2.99494 | -54.04743 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c2ac1b7-34e3-3895-bce8-8cd674ced457 | -3.35273 | -54.16932 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3dd91bb5-6e3e-301c-83a6-521b6832207f | -4.3049 | -50.78455 | 2026-10-07 05:40:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7abe83dc-69e1-3cc3-ad17-ead5eee9da55 | -3.49414 | -59.2724 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79562dcd-74d9-3978-8bd4-e9f5704f3e60 | -3.08343 | -54.26819 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ed4c3be4-facc-384a-a4c8-6f8f75c9fa15 | -3.00966 | -54.14009 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 780648b6-4cdf-38ed-9189-4fac428b43c8 | -3.4792 | -59.45809 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 129cfd18-c547-3662-9fab-7b3ebdbe4804 | -2.77448 | -54.08583 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| f5505d5d-4059-3d82-a7f4-cd88254df309 | -3.26903 | -50.40438 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| edb55cd3-7c73-3eb8-8142-d41f210f63b8 | -2.13311 | -54.80001 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5ad23b89-ddd9-3577-b48a-345cddb30137 | -2.55787 | -54.59402 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6376f65c-cdc1-35b6-ad69-2fb1ebaec6be | -3.0557 | -54.15211 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06438e09-ffb9-3b92-8388-5452df496b30 | -3.54382 | -59.49045 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4407d624-dd85-3442-a88c-7a45df91b8b8 | -3.17072 | -50.44352 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 969084d7-cdf8-3518-899c-7fdb8ea93045 | -3.36347 | -59.418 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4afda85c-65c2-3abf-abee-a169c587f678 | -2.94797 | -54.06396 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 99b3ed79-b46c-3c1a-bfc3-646fd23a8f88 | -3.10205 | -54.17724 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc0cb05f-e302-3953-a5f3-d237482c0935 | -3.5184 | -54.66064 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 04272412-b30c-3a1f-a692-57e51f245f2e | -3.29968 | -54.03379 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a7336f75-3ce1-3028-bc53-14c510651dba | -1.28629 | -56.98007 | 2026-10-07 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbf1f575-24fb-386a-ab97-1e679f882a8c | -1.28256 | -54.56183 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6bb759c3-043c-3ff6-a399-80483ad16435 | -3.09663 | -54.18142 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 270876ea-01eb-3eed-9969-6e613e0cd550 | -3.484 | -59.58396 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb4eef21-c012-3b90-a971-c4bc8ed97adf | 1.29301 | -54.70016 | 2026-10-07 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 412f726f-989a-3cb8-89ea-55d242d0aeae | -3.49761 | -59.27293 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 281244d5-04c5-3fb3-b2da-4213c7c3b1cc | -2.52649 | -58.09351 | 2026-10-07 05:40:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6791d080-f711-35e2-b417-b65c4b86f5a9 | -2.76979 | -54.08514 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8014bce5-08cf-3e52-9551-c2da32e2aa6d | -2.70991 | -56.88001 | 2026-10-07 05:40:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5a803e6-5acd-313d-81bd-4080fc1ca687 | -3.35642 | -50.76632 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1c4f946-8995-3c95-ad2b-a180b17410a6 | -3.16301 | -50.44061 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ada30cf7-2780-38da-b77e-c04e19e2bfd9 | -3.00178 | -54.12894 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 906a53ab-09ac-36bb-8fc6-ccb16ef3c902 | -4.34473 | -55.12654 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd3f19d4-8223-3440-9c16-2529194d4cea | -3.18582 | -50.55006 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0d5f731a-d477-39fc-9b31-06e676bae3e5 | -3.5461 | -59.49843 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2ab72f5-c5d7-3a71-9e0f-1cd4d335f7b2 | -2.94058 | -54.17258 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9422ff52-9d82-38d4-b3a5-3e6a33f9ac11 | -3.53815 | -58.64885 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09157b4b-c40a-38fd-b177-72ab0433fdb9 | 1.97025 | -55.88189 | 2026-10-07 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e383e7b8-835f-3f58-8406-41ac697d1617 | -2.78852 | -51.67947 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 239b2f06-e6b9-3647-a912-e16b5adee019 | 2.44357 | -50.83447 | 2026-10-07 05:40:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9bf5c852-8f2e-3f5d-9853-756abe93c540 | -2.78986 | -51.67289 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a8ec59d-40c9-3658-b614-0c169e8fe643 | -3.04466 | -53.91165 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e45245be-c624-3ad4-b1d8-457e2816b4af | -3.52296 | -54.66132 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 569376ea-ad3a-3f38-91bd-52857b0358c1 | -3.09794 | -53.71729 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b0b6f33-da6a-368c-aa18-0c191cb302c3 | -3.08562 | -54.15936 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9178708e-26d6-39af-bc96-16c00c52440e | -3.50196 | -54.64648 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 58deacb9-2d83-3465-875a-62bcf1b45050 | -3.50576 | -51.69274 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bd257b7d-fffb-3467-ac34-fd5209b4f32c | 2.4449 | -50.82772 | 2026-10-07 05:40:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61fd06e0-c4ab-32e8-a407-ac6ba4197670 | -3.08978 | -54.28886 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f4267e84-c0d1-3ab8-a4f0-e424e089d8e3 | -2.99464 | -54.11283 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 36a925eb-9e18-3804-ae44-7852d40e957c | -3.09877 | -51.37436 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30a893d3-41dc-3ad1-b69c-108b4f425a28 | -3.05128 | -54.22901 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00894559-d31e-3127-b5a1-6c542070bb23 | -3.50268 | -54.64187 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c9fdb81-492c-3e16-bd8e-6a1cbf24e03e | -2.10245 | -52.06081 | 2026-10-07 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74ee7b7e-868b-3f84-a058-27009ca09cf7 | -3.04621 | -53.90152 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab267712-c126-3008-ad74-86dfd1f67b01 | -4.34408 | -55.13087 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f6b0c7a7-4c13-3cc5-86c6-91ecb231381e | -3.18518 | -50.55442 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9a1f4ade-02a5-3ba6-aa97-3ac33b0c039a | -3.74013 | -59.44436 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e70cf16-bb0e-369a-89a7-e67de2df9d48 | -3.0964 | -53.72776 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c2dc894-6bfd-39b6-b3a5-143d6545a235 | -2.4906 | -58.06254 | 2026-10-07 05:40:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ad40da6-59eb-355a-a3aa-3cdf7ffc47a2 | -3.49956 | -54.63189 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c7b1cbd-0c63-3125-a6ae-7033bc40b9c1 | -3.49202 | -59.57766 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e17b22e-44f8-34d5-b233-a88d44679517 | -3.6784 | -55.95258 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd20f40c-df31-361f-aa43-c762cfa53ed4 | -3.48089 | -59.46977 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 218c2b1c-8d80-3a3d-8188-a733405eb249 | -3.78039 | -59.19845 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6fea7ae-bc57-36e4-97bf-4a5fd1aac12b | -3.54132 | -55.52436 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77091e6e-637f-3dd5-a6b4-aeb8edc6d359 | -4.16384 | -55.14225 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 616a2605-4814-3b6d-96f8-d3231fe8c617 | -3.47747 | -54.62384 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6b4dd02-e2f1-30cc-85b3-002f3bd79f35 | -3.01435 | -54.14077 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 256b4c8d-f0b9-3970-87fb-55aeaf578948 | -4.16123 | -55.15931 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c024ed46-6723-3835-8a39-1a6bfb79777c | -3.27215 | -54.04844 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 42778a57-92ea-3680-9234-c22949ac0e58 | -3.99785 | -56.25055 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3b55cd3-3abc-3bbf-8f58-0fbf20484759 | -3.04416 | -54.14842 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06541f0f-c60f-3acf-adb2-1cb05aa51e84 | -3.99431 | -56.24624 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23b4cc73-f6c4-3715-a02d-6008933cd7a1 | -4.13762 | -54.9209 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a735f87e-6e3c-3c63-a03c-15977c2bfcf2 | -3.27345 | -54.01451 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f33a036e-74f5-32ce-bee5-d2656e917e45 | -3.05494 | -54.15699 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 65f6f02d-1974-3521-b43e-a121114062ba | -3.50864 | -54.66368 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cee2404a-4eb4-30c3-9bfc-dc6647df35b9 | -3.06314 | -54.24511 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3fcd3669-f0e1-3953-a444-7894fd4b6c33 | -4.14344 | -54.02859 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f51310d9-1c82-3ee6-adb1-cf6248a49fcd | -1.61419 | -55.11841 | 2026-10-07 05:40:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f264e71-6d6a-3694-b218-dfcbc23cc65b | -3.06632 | -54.25559 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dec7d141-99f2-374d-bdf7-fbc0cad5e375 | -4.34853 | -55.13163 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c66fe198-22b9-3cc4-9ec5-425823a91357 | -3.1918 | -50.55097 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12d295e6-6253-3b59-8291-cf90ad05836d | -3.2912 | -54.05822 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 50dee453-a952-3aad-aa1a-1d7f9c38345c | -3.49914 | -54.66469 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3baaeaf6-451d-34c5-b32c-26c5b3853374 | -3.28647 | -54.05753 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c90a3494-efd7-309a-81d0-4372ef63c5d4 | -2.9937 | -51.04813 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ed56a3c-c340-35a1-8c51-ebcf317b38f0 | -3.47576 | -59.45755 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a3f1bb7-2f26-3c71-904e-4dedce21e423 | -1.79318 | -57.11736 | 2026-10-07 05:40:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a5ebd9c-4841-31f7-8674-6bedb8f5611b | -3.27835 | -54.00845 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README102.md)
