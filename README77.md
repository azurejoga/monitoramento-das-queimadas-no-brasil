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
| b7c77aef-b8cd-3125-95a4-e2fff9f752e1 | -8.89998 | -62.42896 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 740e6a68-0eae-3f27-8dc7-c348bc2027cc | -9.19544 | -59.61929 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7810fdeb-6ae3-33ec-9f25-eff4fdccd838 | -11.11037 | -62.66768 | 2025-08-23 05:42:00 | NOAA-20 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25d32733-08cf-3b57-95bd-df5780215fa4 | -6.83382 | -59.88813 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1c20c38-cbc2-366f-9146-48f70ada2279 | -9.20261 | -59.46803 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b145222c-d9ed-3851-9af1-6b3bc2090a2d | -5.74367 | -57.60337 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 83c7b3ac-9cf8-3b15-96a6-cec3049b84d4 | -10.46766 | -59.13034 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e5f8710-fffa-31ea-99b9-d7e894a5a3bd | -7.10484 | -59.77786 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6d3c578-39dd-3f41-b269-2e1adf2b37cb | -9.21189 | -59.63041 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3efa5f45-e57b-306f-b7ed-e03702fe19e0 | -7.44031 | -60.62556 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e79ece45-be79-3f4e-84b8-1191864c0637 | -9.95819 | -60.17436 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ecb90b80-18a0-31ee-9752-839c0b2f37ac | -6.25282 | -53.68183 | 2025-08-23 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2989376-2b0b-320f-acdf-e91d739ecc20 | -9.19753 | -59.45129 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f5625ae7-f46e-3db9-8ad7-2ba8093b1d0a | -9.17018 | -59.60659 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 96ccfa9d-0818-3f6a-a15d-bd6d1767b55e | -9.19997 | -59.45406 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 778711f7-bad1-3c50-9019-de8498e3b6e7 | -6.87342 | -59.82327 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dfdc2ccc-3ae5-3a9a-99f5-6812151c34bc | -7.81584 | -63.56035 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57388606-058f-37d7-9931-51c31d41a4f1 | -8.87119 | -62.42017 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc73604d-953a-3203-8023-233085cf0113 | -9.18602 | -59.62232 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a982b0dc-2d55-38b1-9359-17efe10ea82a | -7.78054 | -61.5779 | 2025-08-23 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a89ee3b7-3fce-3674-9f50-1250e361a0ad | -9.95443 | -60.18356 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8ff64b90-6c9c-3523-9883-f5cdbeacd3da | -9.16199 | -59.50938 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2c195af-7903-3390-ade4-aa1615fa844f | -5.75 | -57.59362 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 2c1d1f92-41c3-3039-8fa0-ec61ae9ee5b3 | -9.92943 | -65.00774 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 815034d3-1da1-3e21-bb99-4437b16064b3 | -9.96136 | -60.1832 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| b0508387-5f51-3520-925d-6cfdfa98d13c | -8.61901 | -62.64031 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| caddfd41-ecff-309d-b9e0-a2400f5a0417 | -9.22575 | -59.75489 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2049b549-bb8c-3a2a-8ad9-3d79b94e5212 | -7.02922 | -59.91133 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d13ffc53-afd8-3698-9ecc-0f22dced581b | -6.25351 | -53.6769 | 2025-08-23 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e00123b-d643-3ea2-bcdf-9d54231e0127 | -9.95334 | -60.17785 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 843a625c-66f4-3d0f-a7e8-d36fd2cc9c54 | -8.60358 | -62.61331 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3809fd09-2ac8-30be-b318-d0f29d09157a | -9.50937 | -60.55304 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b73e418f-6e94-310b-90cf-3ec168da15de | -8.87614 | -62.41198 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb16a501-2a10-3fae-b93f-70f6e0205e98 | -5.73712 | -59.88568 | 2025-08-23 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2faf5d0f-055a-3a52-bcbf-7a58980f05b6 | -9.21738 | -60.80059 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d12408b8-8412-3519-90fa-115ad6b7c09a | -9.08826 | -61.43242 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e57bd9f-5d6e-31f6-9ec3-2c443f20fa3d | -9.51783 | -60.52316 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0065df32-4d1c-3074-80a8-31fdb18d0437 | -9.51984 | -60.53901 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 634f0f80-a3eb-35d2-97b8-63fd0c9c2cf0 | -9.16635 | -59.60162 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 69079214-e606-3fe4-b7ae-9ac945086b38 | -6.68625 | -58.86164 | 2025-08-23 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a6a88090-6c9f-382a-8359-e8f9a97817a0 | -7.50797 | -63.832 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2947f2c-278c-3182-8e50-edab5ed1a959 | -9.10071 | -61.42916 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 702a2ff8-fb93-3ee0-aad7-c06d27419aac | -9.71782 | -65.71666 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acc0e6a2-9e94-3c45-88dc-6d1e1841c2b2 | -5.44015 | -60.17986 | 2025-08-23 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0e4a4b7-b587-3cb0-b858-4db7ee12b067 | -8.59996 | -62.61275 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0d116be9-aa9a-3f62-a42a-592abfc1f895 | -5.44118 | -60.17284 | 2025-08-23 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 416e379a-78ed-3c98-a879-46359b1ef10c | -9.22138 | -59.7543 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aee38588-7a93-3994-82d7-d59d38c0a2ae | -9.23864 | -60.48088 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f12e215f-0a99-3045-ad6b-acfb530a5816 | -5.88172 | -57.76182 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d80aa342-c07d-3200-b4bd-629565ad4b23 | -10.4624 | -59.13425 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad5bf653-8012-32d2-b27a-2e14ddef5c0e | -5.80079 | -59.21669 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d301a58-8268-3a1c-8f21-e44ba66ac848 | -8.89199 | -62.43221 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0b7a57d-f14d-35e9-9ab0-7f20b8f0c1d2 | -6.58556 | -59.87597 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9cda8a31-c1ba-39a0-ba03-d35cbfce3182 | -7.29477 | -59.62912 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f2d2434-5534-3749-bd7d-a91db42b2294 | -8.89934 | -62.43331 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4bcf8dfc-031f-398c-923e-b4be6c0e4186 | -6.68337 | -58.86441 | 2025-08-23 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 913a267e-3695-3050-86d3-172f9b0af6ba | -9.25822 | -59.77727 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8ea8d60f-2731-35be-914c-899d8071a209 | -9.5083 | -60.56063 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe4ff406-1e9d-34ca-8ad8-046cb9a5794f | -11.90032 | -55.89842 | 2025-08-23 05:42:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e27fcdeb-3a50-3b32-b02c-6d7150607276 | -9.21402 | -60.79229 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec30b44d-c27d-385f-972d-e7f17a02fa38 | -9.20952 | -59.45079 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f81c6f16-ea42-3280-a348-092283471da0 | -6.83326 | -59.89193 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7713d927-f4f8-3232-924a-3ff586b6a3b4 | -5.81 | -59.21393 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0835008d-fdc2-3917-bcba-9a9fd833b99e | -7.62779 | -63.4866 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d9adeb1-e11d-3d1f-ad6f-141e46d7b855 | -9.17194 | -59.59362 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b726213-bd36-3f4a-9b7d-2fbae795e483 | -8.85744 | -62.41584 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4eacc8ce-0d90-33a2-b82e-512afb7dd452 | -7.79265 | -61.57497 | 2025-08-23 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3f9a71e-6212-34df-81da-91e80accd6da | -5.44066 | -60.17635 | 2025-08-23 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e577e5bd-7f42-3f6c-a7bf-aa116676c6a6 | -9.20383 | -59.45913 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d040019a-7efa-382d-9eba-feba2f47e23d | -6.87822 | -59.81991 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5018e675-5d59-3036-bf27-023b44a72254 | -9.21369 | -59.61745 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38fed3fd-61ec-3e12-8334-b6022c8906c9 | -9.19985 | -59.61988 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6411142b-bbb7-3629-b2a1-300a4d8fbea2 | -10.71229 | -62.7445 | 2025-08-23 05:42:00 | NOAA-20 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2eed2dd-55ec-359a-9b52-08cafbbf9e55 | -9.51245 | -60.56126 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33758137-4615-31e9-bbc2-bb146c7bc55a | -5.733 | -59.88506 | 2025-08-23 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29464f4f-4871-3925-8827-200f08bb3013 | -8.59805 | -62.62541 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7cb666a7-29f0-350a-a1d1-68c896ba691e | -9.18662 | -59.618 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5e5192ab-3edb-3d1a-8871-e0328cb2c67d | -11.11474 | -62.66374 | 2025-08-23 05:42:00 | NOAA-20 | URUPÁ | RONDÔNIA | Brasil | 1101708 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb5872f0-483d-38bb-a310-5ec911ed9dcb | -11.19001 | -55.03323 | 2025-08-23 05:42:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3af1007a-593a-3b5b-a5f0-f092601ccf9c | -9.51299 | -60.55745 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1384b92e-3aab-3a89-8344-af4227075425 | -8.61853 | -62.63712 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0a1fdf9-ca13-32c6-8456-e354e5c538ca | -9.21081 | -60.7886 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0be1eb5-3824-3cdb-8776-974f777f3d07 | -7.8101 | -63.55171 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb45cb81-aa8e-34fd-b766-ea4963e30b26 | -9.50638 | -60.51374 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 726c2dd0-d87f-3dab-b066-43076f3edbb2 | -5.8002 | -59.22076 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bc19679-6d1a-3a16-bb8d-9f9b275c6846 | -7.39127 | -62.30496 | 2025-08-23 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83ca07be-cfd1-32db-813c-9abc15c049ac | -9.1698 | -59.61277 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23ef3063-85ba-3851-a78e-ea301dfa094c | -6.87401 | -59.81936 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 66f55227-3918-36fc-b873-d1d7290be968 | -9.16222 | -59.60285 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| adbd3518-a4b0-3c4c-8c62-2d7403525226 | -9.95483 | -60.19905 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 4f7d6e29-6758-3f48-bbc0-0b347ad8d00c | -9.25968 | -63.3417 | 2025-08-23 05:42:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c90df6e-d305-32fc-aaba-66c33ee48b50 | -7.78364 | -61.58314 | 2025-08-23 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 695a1861-add5-3d6a-bd57-024924e4e510 | -6.57778 | -59.87083 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0e70d3d3-8697-3e53-8a83-04ade58b0e30 | -9.5267 | -60.52057 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 81fc8069-44fc-3ebc-8eef-8736e18f8dec | -9.17253 | -59.58928 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c650bd62-a062-3e31-99a1-2ff833c0d52c | -9.94954 | -60.18707 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| ccca5737-625f-3329-9f7c-3c3a9133eea6 | -6.56292 | -60.06015 | 2025-08-23 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 250adeb0-bed8-392e-9fac-02bbb71b4c3f | -6.57972 | -59.88687 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b860854-25d8-3d92-9f4d-f3ae84ffcab7 | -9.95165 | -60.19025 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 7f46421d-aca0-353a-bf65-8124fb934399 | -9.20118 | -59.44515 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README78.md)
