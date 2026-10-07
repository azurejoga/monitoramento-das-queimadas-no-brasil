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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 112c8e46-d212-3c64-8c2d-a4e604f26d87 | -4.13527 | -54.90543 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67fc199e-1f04-3250-9cc9-421d4e0a499e | -3.74298 | -59.44328 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 66a28dd0-7169-37d8-ba72-7441b65acdbb | -2.92688 | -54.14456 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9fb4a580-5f60-31fa-81b4-49cee7b1626d | -6.60815 | -53.02281 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ee29b98-6507-37d2-a91b-741e1a0e05ea | -2.98959 | -54.04603 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 162c5724-9198-3954-a0bd-4352337e08e5 | -2.93912 | -54.15362 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 41a20fde-d577-3de5-96ed-b71eb3152037 | -3.28389 | -54.03736 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f68a463e-594d-317d-836d-6e078bf22824 | -3.05985 | -54.22941 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e73772a-caa7-3b07-a0f8-f092f78c56af | -4.2672 | -54.86921 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ebe9d97-955c-3379-9c93-ffcd449b9a53 | -1.20757 | -49.03867 | 2026-10-07 05:04:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a88d1d7b-4d63-3e65-953e-7a4f29729908 | -2.94299 | -54.15062 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c81ea2d7-98ff-3771-83d6-325ab1fc6ba5 | -4.15789 | -55.15579 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f163aa37-01ae-3ce4-976f-fd60bb32999f | -3.29172 | -54.05304 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 43e035ac-3938-338c-97fd-5ce47e4a3fcb | -3.09498 | -54.28849 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 88b12e4a-b9a2-3a7c-a7c6-6a7dd6c7fc1b | -5.72581 | -45.17108 | 2026-10-07 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| dce921d9-ea52-3a63-a8b3-a0fd0891e06c | -3.58529 | -54.30712 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 90c969d3-1b1e-3eed-894d-30794d33d705 | -4.18844 | -51.13893 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 824df880-635a-3ec9-8eff-aacd1881049a | -2.59476 | -47.35347 | 2026-10-07 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db8946c1-e3d3-3470-a4b7-787bd1a381f0 | -2.9982 | -54.123 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6256132c-9fc6-3c76-8157-ee63cac02f19 | -3.65093 | -55.50526 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6e5cfa7-8055-3af6-a49e-701b39139c77 | -1.8863 | -56.25201 | 2026-10-07 05:04:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 663ed971-99eb-35b9-90ab-2b7b89154bea | -5.95596 | -55.3419 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bb8a5bf-fc59-3467-8709-d60edf52e6f6 | -3.29507 | -54.05355 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f6d4c641-eaae-3bd1-a0cb-50cfda429bd4 | -3.73728 | -51.21014 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d8a4195-af9d-3c85-8204-d9acded7643e | -3.12492 | -53.76113 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f4d79ea-0f98-31cb-91d4-33ac0ed086d1 | -3.08817 | -53.71895 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b633c74d-15e0-3506-b0f1-c3e5ef983ef8 | -4.08067 | -54.88637 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8872a9fa-5a14-3dd3-9f42-12407859be21 | -2.25328 | -51.93951 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16bdfbf5-c8b0-3888-be4e-f554f80e638b | -3.60919 | -50.2041 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c1d33a5-3a33-3c71-a468-e39ec43c4f18 | -3.04732 | -54.22388 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1445c2c4-7eea-3e0a-a33c-755a047a2c92 | -3.28104 | -50.41373 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| defb1b38-a7e8-3f11-a5c9-6eca739626a9 | -3.7207 | -59.3644 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 397cd1d8-14ff-3072-bd75-a3c82822c3d4 | -3.27497 | -50.42686 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d76480c-d3b9-340e-ba68-a6877a5512a2 | -5.24159 | -50.90986 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3b588250-65dc-3f84-abca-80f32fc2ab5b | -3.4991 | -54.64345 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05d0bbc0-0fd8-3571-a45a-ca07f6dd2c88 | -3.78173 | -59.19796 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b67a741-31e4-308b-90dc-8e3fafe6440a | -3.10047 | -54.27503 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6a806119-92e6-32b0-83ca-49fc595b2c39 | -4.76532 | -55.66645 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 797187e0-1e30-3e94-bfa4-1722ef84a00f | -3.4662 | -50.1019 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9ba3da5-13ba-3e09-b850-ec4000a1be97 | -2.95344 | -54.10553 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b709a481-b4c0-305e-a1cd-ffcc044eec73 | -2.77766 | -54.68997 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80cced15-0168-3991-b964-96f6bdca7257 | -3.17231 | -50.44275 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 52c6f21c-8df5-39f7-a8e5-03e01ae61962 | -3.52103 | -58.75842 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0d5646b-a254-3012-9107-301ceeb7710b | -3.48448 | -50.08998 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1ef2cbc0-920e-3ba6-80ee-1848f84271b8 | -4.96236 | -55.82087 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70f7f504-c967-3ab5-98a0-b2a767ad46af | -3.27835 | -54.05099 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c7af3b10-6bb8-3df8-92d8-4bafa778b594 | -3.86021 | -55.99213 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 12ce4473-087d-32ca-a544-51975014162a | -4.92793 | -55.86827 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 04c267b8-d084-3481-a3d4-c920ccea7260 | -1.28219 | -55.41776 | 2026-10-07 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 680eaeda-a06b-3afb-8ee6-47f9c2b76201 | -3.58945 | -55.56882 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 890ee044-ee31-3f9e-824b-5b5adcb3f6a3 | -4.55585 | -49.34796 | 2026-10-07 05:04:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a89c437-171e-3d94-97b6-64af3bfc205c | -3.60667 | -55.48015 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76b083ce-a64b-3f81-9c0e-09d43f592ce8 | -2.76283 | -54.08293 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| c67b6299-bc69-377c-8af3-6995c933e72e | -3.51173 | -54.62767 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6bec9cb-c621-397b-a996-184c07adbff4 | -6.02227 | -53.85321 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a31a6fb-16c4-36c3-b615-8ac661f7cab0 | -4.1562 | -55.14498 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 15da829c-8850-37f0-bb75-c035aeb8b3f2 | -2.99564 | -54.1836 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de9fb10f-a5bf-360b-b001-22e78a7b5e2b | -3.22099 | -53.88955 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 86954c9f-3f8c-327b-8f9c-e0d194c7ea82 | -3.16393 | -50.60137 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 93837820-af9f-3eea-8e8d-4b2a5bebbfca | -3.29448 | -54.03535 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5905bcb3-4140-381a-a10f-fe0ca4c6bdc8 | -3.55419 | -59.48148 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9e4118a4-6348-3c59-80e8-2da5a9e38ac9 | -5.47984 | -44.26022 | 2026-10-07 05:04:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 84b9aa1a-a63e-3abe-b5c9-413d6fa548d4 | -2.94125 | -54.11804 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6bad7dea-3f2a-336e-8a5c-ea4d5af0cb8d | -3.99277 | -56.25472 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3753a469-805f-3d43-b297-e8c61b91a1d6 | -3.28728 | -54.05959 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4520df24-f483-3fad-820c-d5b998c88bc5 | -3.655 | -53.50374 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 125aea2a-3f1e-3983-ac9f-c2135cfbe6c2 | -3.10842 | -53.76611 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 50a40d3c-b294-3b96-b8d9-17e82154cee0 | -6.30964 | -54.79178 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 250b98b9-3cba-36ab-93b8-c3c4186d9a74 | -3.00487 | -54.12403 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| fa9e01a0-0910-34c5-ad9d-67dad1ab521a | -3.69617 | -58.2915 | 2026-10-07 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76a9e6de-ed33-3c1b-b8f6-1bee8690a1e9 | -8.71385 | -45.21027 | 2026-10-07 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d1144905-3641-3743-9652-f46f621da1c7 | -3.80211 | -51.03261 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e178c9ef-ce6c-322e-8793-5960210ea589 | -7.2165 | -55.17388 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de1207d3-4696-33e3-9fa0-f02829ce47d2 | -3.07732 | -54.16029 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3da33da-327d-3ec3-be9d-b42f14732029 | -2.93244 | -53.93259 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a260b86-c5ea-3373-8bc5-312fa2c9dc55 | -4.35527 | -47.77916 | 2026-10-07 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a6091442-4269-3132-8348-5d588babd6ec | -7.25174 | -45.25894 | 2026-10-07 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb94a05b-e4db-36d0-ad64-a9ce379cb7d6 | -4.38728 | -59.90274 | 2026-10-07 05:04:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a4d462c-52e7-3cc5-949e-f40bd7f13964 | -2.83944 | -54.07314 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 25a6050d-0c55-35f4-941b-6d19195e7076 | -3.66816 | -54.54141 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9d50c54-412a-32bf-a8a7-7df47fefe418 | -3.28613 | -54.04495 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 425d3f99-e09b-3d09-86bc-2dfca724353b | -3.27102 | -54.01002 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7230fe78-76ed-37a4-9d87-45bbd118240e | -3.31705 | -54.17214 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1be3415c-a568-3eb9-80f4-3e3e1ba34e8c | -3.17286 | -58.63757 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11f7e422-6c86-3892-ba13-8bf63072de86 | -3.60519 | -50.97834 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 017acf70-42b8-31af-b8e7-0e7c3b1db327 | -6.4671 | -55.44685 | 2026-10-07 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db7a2282-1786-372e-9d87-30e8fa12ca21 | -3.144 | -54.36782 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ae357d5-6a7d-3a8e-ba7c-da2beb3de00d | -1.28992 | -54.56271 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 175bd7f3-76fa-3516-8b21-217a6ca2ab33 | -0.04679 | -53.25678 | 2026-10-07 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 876ad57d-06dc-3d5c-beae-21c58a7bed65 | -2.98625 | -54.04551 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71a1ffde-1f8d-3150-a099-7e0969110145 | -3.28055 | -54.03685 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| fba3f509-9e23-339a-aef7-ce2400972e5f | -3.2833 | -54.01915 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 651366cb-2644-3c29-84b2-44a8d83fc8a0 | -6.88081 | -43.68456 | 2026-10-07 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b8bd1cb8-65ca-3018-8fa8-8c94fd10e6e5 | -3.30037 | -53.86525 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 286f31b6-3722-3db5-b1fe-82f55886fc49 | -3.0774 | -54.18191 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57f434ae-e91e-3c84-bf62-a54fe93f0217 | -3.91092 | -55.8877 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bcfdd752-7e2d-363f-91b4-a3d689578894 | -3.26321 | -50.39686 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b69b86eb-1b74-3a93-9b3c-1309ff581c31 | -2.96442 | -54.14291 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 76e2795a-6236-391d-8d66-1b558cd669fd | -3.58583 | -54.30363 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1d9cbf0c-2bb2-31e6-965e-d313400bfbea | -3.03934 | -53.92336 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README75.md)
