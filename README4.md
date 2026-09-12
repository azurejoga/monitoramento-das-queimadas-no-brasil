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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60bb7927-5b65-3881-a79b-3ae69adda924 | -14.5697 | -52.639599 | 2026-09-12 01:03:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cd6701ca-d55e-3f01-a021-5deb6267301f | -9.1677 | -68.210503 | 2026-09-12 01:03:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ebd65337-1a88-3d22-a436-3078c69031f6 | -9.1725 | -68.233002 | 2026-09-12 01:03:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 504549c1-b2c2-3949-97f7-f72f0b24904e | -3.3596 | -57.7043 | 2026-09-12 01:03:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dffef125-431d-37d8-a7d2-0baa99d5255b | -5.7756 | -53.796501 | 2026-09-12 01:03:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d2aeb62-fbda-347f-8932-d5c2f83a44bc | -3.3382 | -59.4216 | 2026-09-12 01:03:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3cc99bd-8574-31f2-98b7-a104e9f924b5 | -6.6014 | -58.840698 | 2026-09-12 01:03:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a02e9bea-280c-309b-adda-74481a0ac5f8 | -6.0946 | -59.8909 | 2026-09-12 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0027ff6b-db19-3a95-be49-a56a96acd358 | -3.7375 | -61.7369 | 2026-09-12 01:03:00 | METOP-B | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c6fe3595-16c1-381c-846d-b3450892550a | -6.1801 | -57.713402 | 2026-09-12 01:03:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e960c6f-bedf-3eb9-b01c-f18be0c97216 | -8.6443 | -66.471703 | 2026-09-12 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ebf23df-41fc-3628-90ed-ae8ee0613447 | -8.1019 | -54.7757 | 2026-09-12 01:03:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f582030c-ac78-370c-8e91-c65b60289c87 | -3.741 | -61.751999 | 2026-09-12 01:03:00 | METOP-B | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eba408c4-6c2b-30ec-8f41-193380ab379e | -4.8047 | -55.745998 | 2026-09-12 01:03:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f9274d6-2e1d-392e-a0b0-32f0728e6686 | -5.7659 | -53.798901 | 2026-09-12 01:03:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15697a6a-8b4c-3174-b9f4-dfdd45648646 | -6.0804 | -55.628799 | 2026-09-12 01:03:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 441857ef-e67d-320e-a467-1c5abbc9518b | -6.6111 | -58.838402 | 2026-09-12 01:03:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cad526b2-fdc3-3816-902d-c29c06f6c23c | -9.469 | -67.072098 | 2026-09-12 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3485569b-259c-35aa-b130-25153e2bbaaf | -6.276 | -56.0117 | 2026-09-12 01:03:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb5b484f-6d36-3f19-9a75-8b65ab03f6fb | -6.8275 | -55.236698 | 2026-09-12 01:03:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5a16b9f-79d1-365a-a86d-bad94bbbbc2f | -3.3565 | -57.691399 | 2026-09-12 01:03:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bbda9c97-56f9-38fe-a0e6-2899bc2d4ae6 | -6.9027 | -62.917599 | 2026-09-12 01:03:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c98f124d-b7ab-3ce5-b9a9-68dd05e63ee4 | -6.2162 | -51.675201 | 2026-09-12 01:03:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c488695-d6a7-304b-a2fe-b12af5c51d5a | -6.1675 | -57.703999 | 2026-09-12 01:03:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 566c0aeb-74c6-302a-a6d1-750cf4b1ea3f | -6.277 | -59.921501 | 2026-09-12 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c3e9ad17-1787-38de-bb87-baaee7772b44 | -8.2028 | -55.224602 | 2026-09-12 01:03:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4dd2b8a8-fc6f-399f-9dae-2cdd9cee9d6b | -3.7294 | -61.7467 | 2026-09-12 01:03:00 | METOP-B | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fd27d13d-41ee-3515-9083-e2537c3cabf3 | -6.1037 | -55.640301 | 2026-09-12 01:03:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b39ec408-7bd0-36fb-a435-ec0ec46edc27 | -9.3505 | -68.254799 | 2026-09-12 01:03:00 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| d7f20866-70b9-3b27-91d1-46983eb1858d | -12.1505 | -64.128899 | 2026-09-12 01:03:00 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7a54c97d-4351-36d8-acab-b6404258c600 | -13.2302 | -61.5984 | 2026-09-12 01:03:00 | METOP-B | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 23edaaf9-8df6-3512-9697-2dce3302dfdc | -6.8702 | -55.6217 | 2026-09-12 01:03:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea475bcb-aa52-3f04-b31e-4c73f669a22d | -9.6947 | -67.365196 | 2026-09-12 01:03:00 | METOP-B | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 6d3d168e-5a89-3206-bf57-d6e085cc5a19 | -6.8372 | -55.234299 | 2026-09-12 01:03:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e7a819e-ba85-3bbf-afa9-adb58d20394a | -6.0524 | -53.466702 | 2026-09-12 01:03:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76609e4d-7edf-32cc-b4d0-db4eb92bc16d | -6.1703 | -57.715698 | 2026-09-12 01:03:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0060e39a-549e-3d47-855c-a05b271ddc2b | -2.7101 | -57.605801 | 2026-09-12 01:03:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 159abdca-0bc3-370a-8dcd-408518598944 | -8.9583 | -67.364403 | 2026-09-12 01:03:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 39aecb45-ae22-3246-875e-4960f3aa7a26 | -6.1024 | -59.880001 | 2026-09-12 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fc657994-7d9c-3df9-b706-304a28c77b15 | -6.173 | -57.727402 | 2026-09-12 01:03:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a50b16a-341f-3500-9efe-4a7cec2c7eda | -6.7577 | -59.418999 | 2026-09-12 01:03:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9450d36f-1d3e-31f1-aadf-d8903cf745fd | -6.1837 | -55.251202 | 2026-09-12 01:03:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 494cf81e-bb5b-3bb1-a03a-038512501df3 | -3.7392 | -61.744499 | 2026-09-12 01:03:00 | METOP-B | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 07488108-e986-31e4-8bb2-c434a44d81df | -6.2663 | -56.014 | 2026-09-12 01:03:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c4cc87b-c367-3f93-98f6-80ddd76d2850 | -10.6794 | -54.170399 | 2026-09-12 01:03:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ac39729-7d89-3473-9c1e-69a3a33bb86d | -13.3147 | -51.613201 | 2026-09-12 01:03:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c8fd93c0-cdfa-34c3-b613-4adae4da7972 | -5.7873 | -57.707401 | 2026-09-12 01:03:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7b433e4-d43c-3541-952c-9fdec99d82ea | -8.9562 | -67.354599 | 2026-09-12 01:03:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5cbc6413-fd6e-37c5-a4b8-a119e5e91d54 | -6.1044 | -59.888699 | 2026-09-12 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 72a3ac4f-1e2b-3b5e-882a-cd427de14f16 | -8.6462 | -66.4804 | 2026-09-12 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 095a2eda-26f0-33b3-be95-54af7138e0e2 | -10.6707 | -54.136002 | 2026-09-12 01:03:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5092c868-ebee-364c-a43a-7ba7743ae364 | -2.7164 | -57.6325 | 2026-09-12 01:03:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e24cd562-debf-3ca4-9363-38a4f39c4882 | -9.3407 | -68.256798 | 2026-09-12 01:03:00 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| bcd02655-0a1d-33a0-9b27-3f1482abbc93 | -7.0173 | -55.382301 | 2026-09-12 01:03:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b72449d4-0101-3ef3-ac5e-16fa2e51057b | -6.1647 | -57.692299 | 2026-09-12 01:03:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef9e6083-bd4c-3140-831e-6a9406d152d9 | -6.5968 | -58.821098 | 2026-09-12 01:03:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f675ee37-4b0a-3eb7-9ae6-0cedc2e9bc7f | -13.2286 | -61.5914 | 2026-09-12 01:03:00 | METOP-B | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a8a95955-2dcc-3dfb-beb9-971ebc4a7e5f | -6.2627 | -55.998901 | 2026-09-12 01:03:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c34df07-132a-388b-bf72-9157494f3549 | -8.6402 | -66.5 | 2026-09-12 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 73fe1051-5491-3aef-8e0f-fe367247f99a | -9.1701 | -68.221703 | 2026-09-12 01:03:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 94f6188b-208a-3107-82db-6ec4cfb5f1fc | -6.1773 | -57.701698 | 2026-09-12 01:03:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| beefde3a-25c6-3f52-875f-12874f4a4f9a | -6.2724 | -55.996498 | 2026-09-12 01:03:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 449a7610-6156-3c29-85c5-32591a1fea1e | -3.8759 | -55.807301 | 2026-09-12 01:03:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 306f5bb1-99c9-3631-b97e-375c1d264360 | -6.5991 | -58.830898 | 2026-09-12 01:03:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d18d2169-f6d8-330f-9d00-22510ae42d2a | -6.0901 | -55.6264 | 2026-09-12 01:03:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f93c4db9-d55d-32f2-8b1e-ae78da64d6d6 | -6.8605 | -55.6241 | 2026-09-12 01:03:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c52de31-ed16-38a7-b471-b098fc218be2 | -6.0998 | -55.6241 | 2026-09-12 01:03:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e882f64b-d996-35d7-8dd5-9e2fc68a66ff | -9.4711 | -67.081802 | 2026-09-12 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e7a63e6c-ee6a-3e28-a569-296110d1f53a | -8.6383 | -66.491302 | 2026-09-12 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd773bbd-8e6c-3c3b-9e62-d7b2dc6db97c | -8.5601 | -54.5495 | 2026-09-12 01:03:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cce103e-b02b-3ed1-95fb-8b85dacd2a67 | -2.7004 | -57.608101 | 2026-09-12 01:03:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 50e5fd25-2406-38f4-ae27-0e3be9682c2f | -9.445 | -67.006897 | 2026-09-12 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f7ea7921-5ba1-360b-a168-d33d04057a0b | -9.3481 | -68.243401 | 2026-09-12 01:03:00 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 71ecdb29-5fcd-34ff-a83e-cdeba342600f | -13.3243 | -51.6105 | 2026-09-12 01:03:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 85dc635e-dcb1-31fd-b2a7-823385087044 | -12.1587 | -64.119202 | 2026-09-12 01:03:00 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7c9e0dc5-51c4-3582-940f-1173154717c7 | -11.2233 | -54.118801 | 2026-09-12 01:03:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 412aaeef-f935-322b-ba43-cdc318c16154 | -9.3383 | -68.245399 | 2026-09-12 01:03:00 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| b8a5d1ba-8ba5-3c2c-b708-dc6477121cf5 | -6.275 | -59.912899 | 2026-09-12 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 234efa98-2f87-37d1-9869-e1e0f9176f60 | -20.723 | -54.614101 | 2026-09-12 01:03:00 | METOP-B | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e77ed42d-a4b0-3d53-b72a-06e70a4ad92b | -5.9628 | -57.752602 | 2026-09-12 01:03:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a2189c9-ac61-37c1-8fa4-6b6c00f211d0 | -6.0427 | -53.469101 | 2026-09-12 01:03:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f758350d-ec48-31d1-9953-8a1892fd8e5a | -6.8234 | -55.219898 | 2026-09-12 01:03:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cad012b1-66aa-3d96-8897-012d0e2ae843 | -2.7195 | -57.645802 | 2026-09-12 01:03:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c531d089-1ad0-3c15-b69d-966577b87f7a | -10.675 | -54.153198 | 2026-09-12 01:03:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8c399447-0a3b-3455-8223-113e9c0fc3c6 | -20.7258 | -54.625401 | 2026-09-12 01:03:00 | METOP-B | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d6bb23c7-8a5c-3fb8-a697-90993c499142 | -2.7133 | -57.619202 | 2026-09-12 01:03:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 96c18990-0b24-3b64-9696-bca26970d6be | -14.56 | -52.6423 | 2026-09-12 01:03:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5ad689b0-4a68-310a-bd89-6d7092b6da5d | -3.3405 | -59.431599 | 2026-09-12 01:03:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 22a4c02d-cac2-392d-8b01-1f32a8d90f14 | -8.2068 | -55.240601 | 2026-09-12 01:03:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f88df8c2-0fce-31e0-97e1-a62aeff06c5e | -12.1603 | -64.126801 | 2026-09-12 01:03:00 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 511d8cb6-8862-329f-beaa-5bde20891bf3 | -6.094 | -55.642601 | 2026-09-12 01:03:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2eb95daa-f466-3cd6-ae8d-86fec5a13cf1 | -3.7277 | -61.739201 | 2026-09-12 01:03:00 | METOP-B | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3ae8dac7-24cf-3425-8bf2-41f9bc1ff5a2 | -14.5649 | -52.660999 | 2026-09-12 01:03:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cca21651-9965-357c-aa88-5ea76ddbdfe9 | -5.9656 | -57.764301 | 2026-09-12 01:03:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8723aa6-f846-3a2c-9cab-9db470c26cfe | -6.28287 | -59.93303 | 2026-09-12 01:05:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 867ecc13-c6f8-3ced-9020-8c3156646451 | -2.72018 | -57.62854 | 2026-09-12 01:05:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 6f1ab6b9-dcc1-3b3f-b764-d4e2625c3617 | -3.37106 | -57.70308 | 2026-09-12 01:05:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 31.2 |
| e7ac44bc-89de-33c8-9183-3a283f3f2c3f | -2.72397 | -57.6554 | 2026-09-12 01:05:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 30.3 |
| edf859b9-abbd-3627-a4bc-f553399340f8 | -5.9814 | -57.77364 | 2026-09-12 01:05:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 896aa6b7-cfce-3e96-ad4e-cbd23a11f461 | -3.73728 | -61.75694 | 2026-09-12 01:05:00 | TERRA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |


[Clique aqui para ver as próximas entradas](README5.md)
