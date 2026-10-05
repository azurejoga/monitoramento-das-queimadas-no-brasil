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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e4d03f7-0b84-38fb-963c-68d75634fd9e | -6.49279 | -53.4375 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 25f84749-7c6d-3f38-beea-05a3953386cb | -3.52335 | -54.62632 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d96172e2-b9c9-3384-a18e-78c11bb79c37 | -2.99214 | -54.11624 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 7db18ccb-a2e4-36e6-89c9-1a6866b28a4a | -3.08147 | -54.16911 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3da4f4bb-8060-353a-99b0-dc46bf534f43 | -7.60328 | -45.29679 | 2026-10-05 17:15:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 234d3d0e-576d-3ec9-8742-c3809f776bd1 | -4.44352 | -54.96327 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 2e137d49-d699-3545-83b4-5b48567601d9 | -4.46357 | -54.96023 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 92290f1d-11b9-3807-a4a2-b00286380a35 | -3.28311 | -54.1834 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 347788b2-c5a0-301f-88d4-f7ccac44311f | -3.07642 | -54.18046 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 28641cf9-a430-3c12-b3c2-733da1f387a1 | -9.12309 | -65.90736 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 84f39f9a-7016-3042-b04a-314452dc6218 | -2.178 | -48.13766 | 2026-10-05 17:15:00 | NPP-375 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 51b4a0df-b62f-385f-bccb-f14b1f46d4ee | -8.8804 | -67.00432 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 9b35b337-8edb-359c-bd41-fa12e6df4eda | -8.03603 | -46.98347 | 2026-10-05 17:15:00 | NPP-375 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f50a2190-3153-38c7-82b3-07bc672b30e9 | -6.68262 | -45.22529 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| dce79c44-76e4-3dcd-bb05-1b796c4413ba | -8.85734 | -47.14589 | 2026-10-05 17:15:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdb2aaaf-fcc4-3a33-9beb-ac7f3810c56b | -5.6806 | -53.50217 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 08bcecec-e571-3cac-a7c0-c888ec605605 | -4.7538 | -42.59745 | 2026-10-05 17:15:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 8593f162-c7dd-3952-9a84-8c8880de1b7e | -2.99002 | -54.10242 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 73c365ff-fc82-3628-9d36-6619387239e3 | -8.53401 | -54.56064 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2c10001b-e802-30da-a1f2-e49870371119 | -5.81332 | -53.83624 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| ac4441f2-94f9-33a4-ba10-0133598e3f7c | -4.91397 | -41.73761 | 2026-10-05 17:15:00 | NPP-375 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 36a50e8d-9d68-3e59-bb16-54a781af4ac3 | -6.41845 | -43.46492 | 2026-10-05 17:15:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 2bb2103b-d05c-39c4-82b3-bf7ddcf07843 | -7.22826 | -55.18188 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 0e1ec3bb-3b1e-3458-9d13-3cb66d283d00 | -9.18172 | -65.79551 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 647c8729-c6ab-366f-89c1-ffdaf21d76a4 | -8.52265 | -54.60665 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 750455b5-ad35-3344-b92c-09e729b4c6e9 | -3.07921 | -54.17651 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dcdfa0b5-eba7-3afe-b2d9-33597cabd46f | -6.20408 | -44.8061 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 0fa36edd-e401-34a2-b1a3-b0ab760b06dd | -3.23258 | -53.87655 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| d7447748-bf59-3ba3-b1ef-88dd05944673 | -3.91397 | -44.14892 | 2026-10-05 17:15:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9dd8a991-2f2c-3589-bbc4-e3f6253f883f | -4.06336 | -54.04574 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 90ef7701-0efe-392e-a859-3dd4ffb833a7 | -3.32405 | -53.85203 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f2d18e78-b485-3371-8c58-19d0487c59c6 | -5.18499 | -42.72492 | 2026-10-05 17:15:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3e4774c6-7e68-3caa-b024-8e3ca455dc70 | -6.06754 | -53.84184 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5a616c72-2f88-39e9-a680-1fd9615a145b | -3.06819 | -54.17112 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 1fe2d723-fb77-3116-9495-6f264043f3a2 | -7.55129 | -46.72488 | 2026-10-05 17:15:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| fad3d83e-a5a3-3c60-9fa1-90bcf6687bce | -3.27046 | -54.01233 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3b69ce32-2f8a-3898-b27c-8290b90e9cca | -5.27177 | -47.91228 | 2026-10-05 17:15:00 | NPP-375 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| a577fd0f-f906-3b5f-ac5d-09a3b69338ee | -2.78461 | -49.45245 | 2026-10-05 17:15:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c7d9f01e-bb91-3fc6-8ce7-eaaccd4dbe31 | -8.80893 | -49.30867 | 2026-10-05 17:15:00 | NPP-375 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1df443dd-9851-38a7-a1ce-3c9b6c9d04a8 | -7.2139 | -55.20291 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a6c901e7-cfb4-363c-bf5c-92a867eaafdf | -9.5158 | -46.82014 | 2026-10-05 17:15:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 4ec02bbd-9a8a-3044-8344-3ac1d53e5582 | -3.27831 | -53.81995 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c7abac35-a69b-3195-ae37-ce2ba4b57895 | -3.12168 | -53.70584 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 6d739114-9501-3e51-83f4-f19b7221bcf4 | -8.52869 | -54.59487 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 320d6b32-6a06-3b4b-978f-726841c42006 | -2.19555 | -47.72029 | 2026-10-05 17:15:00 | NPP-375 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5dd0d5ce-c794-35fb-b74f-dd5288df8fc1 | -8.54223 | -66.97944 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 249812a1-4ad6-3126-bb50-261f666dd9eb | -3.23484 | -53.86911 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e358a4a2-73c7-3000-b94a-3b36d5740305 | -3.5655 | -44.56882 | 2026-10-05 17:15:00 | NPP-375 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f428fc7c-118e-3a7e-bbbb-15cf35a82e8f | -4.90014 | -43.46163 | 2026-10-05 17:15:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4e8c1dbd-4179-363b-9776-9cbdd5fd5ce5 | -3.06607 | -54.15732 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 67adf649-70e5-3227-8703-d4de59dcce4a | -7.53415 | -45.88114 | 2026-10-05 17:15:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 096260b1-0546-3026-963a-b89a93bfd6fb | -6.62014 | -41.7687 | 2026-10-05 17:15:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| dbff4004-ca0d-3558-acad-c10cb4dc9f42 | -3.69125 | -55.95795 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| f7333226-3d40-3432-9eb3-9430d1e30651 | -3.18149 | -49.44609 | 2026-10-05 17:15:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc0283ed-2a37-3826-828c-71f0e4787290 | -3.28656 | -53.82936 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| aa94eee4-b2bd-3f9a-9e2e-379ac4e6bfea | -3.22733 | -54.30542 | 2026-10-05 17:15:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 947d1a8b-bbb8-326a-824d-71c932be137f | -5.89352 | -55.53079 | 2026-10-05 17:15:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b1881d02-e11c-3cfa-b5b1-a955a9a13ea5 | -7.22143 | -55.18294 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 7c4c7efc-00dd-3874-9f1c-519f2cddac50 | -5.80578 | -43.81762 | 2026-10-05 17:15:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0001fec5-46e6-3d19-a976-459d7f694e5d | -3.51444 | -54.63474 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 171c960a-b248-33be-bb1a-4a6f9dfe834b | -6.88527 | -43.67596 | 2026-10-05 17:15:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 0c0253f7-b779-3d95-9eca-d1fdb15d2291 | -6.32955 | -43.81546 | 2026-10-05 17:15:00 | NPP-375 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8863f74e-0da7-3244-9c30-83e3c596ecf4 | -3.37307 | -42.95414 | 2026-10-05 17:15:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a547272e-caf0-3edf-9d21-1e253bb1272e | -4.45449 | -54.90068 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| ca11c511-2a47-37bc-902e-9666a916c716 | -7.23154 | -55.20401 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 7e0fa3aa-0742-3f45-9a1b-ee3ca2f12678 | -2.22718 | -44.79529 | 2026-10-05 17:15:00 | NPP-375 | GUIMARÃES | MARANHÃO | Brasil | 2104909 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cb0eb328-43d0-3577-9572-109d0d7c9755 | -7.90319 | -44.19226 | 2026-10-05 17:15:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7366e60f-a2f0-3dc4-931d-12b02ce09a68 | -6.90271 | -43.677 | 2026-10-05 17:15:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9b45deab-991d-394f-afd7-11caa4a24092 | -5.89736 | -53.6376 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b1648758-8293-3aee-a0a2-4558c3ea412f | -4.45688 | -54.96124 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 271f4ddf-a7fb-3660-af81-4c7c7985ad10 | -6.7266 | -44.28095 | 2026-10-05 17:15:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 4669b2b5-413a-371a-829e-24ea97a8ba88 | -7.22198 | -55.18663 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c73c3c0c-a768-342b-a7c8-f3911881500d | -5.44026 | -42.64284 | 2026-10-05 17:15:00 | NPP-375 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| f9007448-37db-36e8-a094-8daff697d7c2 | -3.0393 | -54.24678 | 2026-10-05 17:15:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 608f0692-3ea6-34ea-abb1-53abd21e0456 | -9.03406 | -45.16547 | 2026-10-05 17:15:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fcc8bc65-12ce-31ea-a78b-e4a3c0346326 | -7.90333 | -44.20081 | 2026-10-05 17:15:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 44398d23-f834-3362-9e58-90a63dc6f144 | -3.58665 | -54.53115 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 67b0a261-e895-32ac-ba62-ac62e6311219 | -3.09301 | -54.17795 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| dcab9729-ce29-36ba-8d31-75bc944ba755 | -3.68166 | -55.94062 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| e19e333a-1152-34ed-b3f8-80c2bbae1df1 | -3.82384 | -58.88313 | 2026-10-05 17:15:00 | NPP-375 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 529c2392-7744-34bd-9cc4-c355a19bd0b3 | -9.34314 | -65.32814 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e6ec8895-4203-3b7f-bd3d-ab00e06c1ef9 | -3.47909 | -55.42713 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6c49cc12-56ab-3082-8467-b0a914bcd65f | -4.37591 | -43.93664 | 2026-10-05 17:15:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 974c6c97-c929-3121-bd79-e23c3716b5c5 | -6.60532 | -42.26303 | 2026-10-05 17:15:00 | NPP-375 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 2b8bb51d-f1e1-3cfb-959f-b0d97460abae | -3.07868 | -54.17306 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 72ec66e8-0001-3382-93d3-25b0f0f84cfd | -3.13715 | -53.71772 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| e22bd659-2eaa-3423-b0cf-e8651dd88a8c | -3.09998 | -53.71981 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| f679d4f1-01c8-3b95-ae98-ef205b1a520b | -3.67146 | -54.53512 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 834d8035-3af4-3e71-90a2-a9748e03a275 | -8.78431 | -47.55159 | 2026-10-05 17:15:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2271f733-24c8-3c0b-b597-212c014768a6 | -8.65688 | -54.54534 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 137a2206-2e1d-386e-be14-ee6461819b95 | -3.60885 | -55.36718 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6832f24e-10f9-3b91-a938-e0ee83e6823f | -5.24095 | -60.19935 | 2026-10-05 17:15:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d72298e5-aef1-3dba-96eb-5cca8777cdca | -6.15907 | -53.91228 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9bd5519c-de51-3610-a7c5-1f7406ceae62 | -5.55764 | -44.08765 | 2026-10-05 17:15:00 | NPP-375 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 04176d04-8a11-3bff-8826-54e34da0a296 | -3.47369 | -43.24919 | 2026-10-05 17:15:00 | NPP-375 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 3408b459-c6d6-3030-a6d6-f44516285c9a | -7.94523 | -43.85017 | 2026-10-05 17:15:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1c62afdc-6641-306c-8ab0-44725a1730c3 | -4.33902 | -44.38016 | 2026-10-05 17:15:00 | NPP-375 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0b778ad1-32e7-3d69-b86b-237ab6265d32 | -4.00794 | -55.67567 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 67fdb09e-c94c-31a7-a3c9-5e94d8119c9a | -5.12479 | -43.99764 | 2026-10-05 17:15:00 | NPP-375 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 02d356d3-1033-3b13-a2ce-2e42af12ec54 | -4.11811 | -54.42605 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |


[Clique aqui para ver as próximas entradas](README110.md)
