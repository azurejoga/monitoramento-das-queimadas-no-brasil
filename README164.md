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

## Dados Diários - Página 164

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa5fba30-71f2-31ca-94c4-6fd4180a51fc | -9.2828 | -65.6526 | 2026-10-05 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 26b6d09e-aeeb-3739-b48f-b5207850e975 | -9.2367 | -67.8665 | 2026-10-05 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 6968e51a-d37e-30e9-acfa-bdbed3e794d0 | -4.8081 | -42.1577 | 2026-10-05 18:40:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 182.4 |
| b7af59dc-364f-3ed9-98c3-22003bc02596 | -9.1072 | -67.8326 | 2026-10-05 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| f2ca3c7a-c7e0-3be0-b541-9241ae0aef33 | -9.1222 | -64.3843 | 2026-10-05 18:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 3f4570d9-2b30-3227-bf5b-da743b049a38 | -9.0585 | -66.0887 | 2026-10-05 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 4b8eb728-bac8-3b34-93ba-9960e3acb00b | -5.4727 | -41.2463 | 2026-10-05 18:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 131.2 |
| 945eae9c-e0f0-37db-ae0f-11fb3ea1713a | -9.4958 | -63.9562 | 2026-10-05 18:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 89.2 |
| a6c29c95-12f7-3814-8c85-6a5073d07882 | -9.1253 | -67.9432 | 2026-10-05 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 734fe994-2d3c-374b-abe0-65a22e0af14a | -8.8519 | -66.8012 | 2026-10-05 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 129.1 |
| 4cfa795f-831e-3590-b363-cf94c7e756f9 | -9.0584 | -66.1073 | 2026-10-05 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 1225a42e-463f-3601-861e-f3949ee6eaf4 | -9.0429 | -65.4361 | 2026-10-05 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 146.2 |
| ff2bcc64-4b9b-3c87-836d-1cba324f8be4 | -9.0983 | -65.4717 | 2026-10-05 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 11d2d08a-8a4b-30b2-ad9c-f4403adbbeec | -8.5929 | -66.8266 | 2026-10-05 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 142.8 |
| ba83394e-8f8c-3272-baef-936f05e6afe9 | -8.852 | -66.7827 | 2026-10-05 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 8894c6c2-47dc-3dd3-bd64-769da554d7e8 | -9.1257 | -67.8322 | 2026-10-05 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 09386132-9b34-3412-be26-37b04e5799f7 | -9.0769 | -66.1068 | 2026-10-05 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 520caa4f-f951-373b-a74b-61e56bc25b85 | -9.4783 | -67.6752 | 2026-10-05 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| efc8e50d-ace4-36dd-b959-6bd7ba8c2c6c | -9.393 | -65.8918 | 2026-10-05 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 00d4451f-d8f4-3795-abc0-61a125d2a8d7 | -8.5745 | -66.8086 | 2026-10-05 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 9830f37b-4048-3d25-956e-670fd4836415 | -7.4257 | -63.5595 | 2026-10-05 18:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 94.4 |
| c73f5238-f394-3353-b59d-cda04a4b26a0 | -9.1072 | -67.8141 | 2026-10-05 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 166.2 |
| a3f0fa1b-9b14-35f0-847c-ffecbb19e692 | -9.077 | -66.0881 | 2026-10-05 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 2631a3d9-6bd9-3565-be20-ca58abf95fd0 | -9.1442 | -67.8317 | 2026-10-05 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 0d4709bd-1c3a-3f3a-a82d-8d4dec3acf33 | -9.3816 | -68.8615 | 2026-10-05 18:40:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 1aa99b15-1f49-39ef-a27a-b664d8fbbbeb | -8.8704 | -66.8007 | 2026-10-05 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 96dbcd47-96ba-3327-baf3-d17e65652155 | -2.5353 | -65.8635 | 2026-10-05 18:40:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 7cc8144c-4f36-30f9-815c-cadd2f18c9b8 | -7.6696 | -67.1451 | 2026-10-05 18:40:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 91df0da9-3466-398c-ac26-35ebfa71f018 | -10.6087 | -68.6852 | 2026-10-05 18:40:00 | GOES-19 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 64.2 |
| a3c9f97a-f06c-3338-ac7d-5dfa20fb7c16 | -5.4729 | -41.2221 | 2026-10-05 18:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 131.5 |
| 9142fdb9-93da-38d8-ac80-e87cf23a4b2b | -9.4565 | -64.3344 | 2026-10-05 18:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 76e0e5e2-8d57-340b-aad8-e7997d5e5a87 | -9.2199 | -67.3852 | 2026-10-05 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| e067cbad-2e55-3ddb-b9bd-39c09655502b | -4.9051 | -41.7457 | 2026-10-05 18:40:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 103.0 |
| 8d96ab52-d0dc-3b86-91c3-b5bb031dcb51 | -9.7126 | -65.0951 | 2026-10-05 18:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 2a358e7e-b928-3182-a86b-db986922f390 | -9.0889 | -67.759 | 2026-10-05 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 243e7102-60dd-3757-8a3b-d67d118d47a0 | -8.871 | -66.6521 | 2026-10-05 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 22e3f674-2923-396c-b288-88c2cb6a4f30 | -8.8895 | -66.6516 | 2026-10-05 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 8d78283e-2816-3c6d-9c9f-43f76292d121 | -8.593 | -66.8081 | 2026-10-05 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 211.5 |
| 85ac7e26-9679-31a4-894d-9a3daa3959f8 | -8.6665 | -66.936 | 2026-10-05 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 7023960c-6a03-3eef-9a19-d082ca16d09d | -8.3341 | -62.8309 | 2026-10-05 18:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 92.8 |
| b0a98191-898b-3218-990f-46d9b9124571 | -9.1241 | -68.2946 | 2026-10-05 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| adb6b182-53b4-373d-b591-6f23fabf9a00 | -8.8705 | -66.7822 | 2026-10-05 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 5b0457d0-594a-3674-a982-360938a04453 | -9.1072 | -67.8141 | 2026-10-05 18:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 135.1 |
| be149e7c-7945-3052-a872-795adb2538f8 | -9.5004 | -66.7831 | 2026-10-05 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| f1306dab-1753-347a-af3d-c605813afbd9 | -9.1072 | -67.8326 | 2026-10-05 18:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 5eb5d893-e045-3151-9621-61de30151d9b | -9.2251 | -66.1209 | 2026-10-05 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| cc410e63-ef24-3ada-86ad-58ac1c10313b | 3.4155 | -51.3229 | 2026-10-05 18:50:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 61.5 |
| dab4d04c-7671-3959-8814-8552251cacb2 | -8.7521 | -68.985 | 2026-10-05 18:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 6eac4f2d-f31b-34a3-841a-24afa0f23f2d | -9.0429 | -65.4361 | 2026-10-05 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 10ddfb4e-4c72-31fe-b995-e0b975d2638a | -10.6087 | -68.6852 | 2026-10-05 18:50:00 | GOES-19 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 793c131b-db1f-38b2-a769-d9257f16734b | -9.0045 | -65.7174 | 2026-10-05 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 3c9136b1-e772-3f23-a6a9-2c79c85ca613 | -9.6672 | -66.834 | 2026-10-05 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| a99e083d-85d0-3d1f-b8fa-f7880a3f4190 | -8.593 | -66.8081 | 2026-10-05 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 191.3 |
| 3b935e42-0784-3311-8485-4e5a56369420 | -9.1253 | -67.9432 | 2026-10-05 18:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 40a59d6f-61c1-3d34-88e8-54db51e970ba | -8.3526 | -62.8302 | 2026-10-05 18:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 5375720f-99a3-3193-a952-60050aa65b06 | -4.8081 | -42.1577 | 2026-10-05 18:50:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 178.3 |
| b7d5ffea-a7a2-38d2-8ad0-0ac9248d5817 | -10.2546 | -68.7494 | 2026-10-05 18:50:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 6bc6fab8-364f-310d-8b77-3546cafc5508 | -9.2828 | -65.6526 | 2026-10-05 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 710fabde-b30a-318e-b650-90379b19d886 | -9.1168 | -65.4711 | 2026-10-05 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 992e5026-fc39-331b-ac1e-e3573104abaa | -9.1536 | -65.5447 | 2026-10-05 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 4d06bbcc-6ebf-384c-a3ad-c3a8eda868b8 | -5.7536 | -43.3601 | 2026-10-05 18:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 1ab7e23c-6fb9-388a-988e-2417f40fb041 | -5.9155 | -44.0894 | 2026-10-05 18:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| cfd539c3-1c83-3d14-9207-643f1e8c19d9 | -9.1174 | -65.359 | 2026-10-05 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 111.8 |
| d4f4965a-6c06-3c84-b8b6-66c4fc3cad47 | -9.0769 | -66.1068 | 2026-10-05 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 12213415-592d-3ce6-850f-53fe36dbd04b | -6.4279 | -43.4686 | 2026-10-05 18:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 1257a67e-1017-3449-a741-cac0fc269bd8 | -8.8704 | -66.8007 | 2026-10-05 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 07b81000-519d-3e72-847c-254213cbb28b | -9.4819 | -66.7836 | 2026-10-05 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 58c5d3f4-1e06-38a4-b49e-f23e2cea1268 | -9.7312 | -65.0944 | 2026-10-05 18:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 54fe2d54-17c4-327a-a540-10869e3d7696 | -9.1257 | -67.8137 | 2026-10-05 18:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 1d748601-cf5b-3fbc-97d6-ffcc4a7b8d95 | -8.8895 | -66.6516 | 2026-10-05 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| bea2b318-94d2-34b6-9d45-cc7369b75135 | -9.1259 | -67.7581 | 2026-10-05 18:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 7984794f-85bf-365e-89e1-1ed727790afc | -9.1076 | -67.703 | 2026-10-05 18:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 7a15b14e-10c7-3b89-ac08-f9dc4e83b411 | -9.3629 | -68.8988 | 2026-10-05 18:50:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 8e5ec0c1-ea03-302b-8a75-ba9a6b024044 | -11.257 | -43.5095 | 2026-10-05 18:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 68242ca8-ae10-33e5-97c5-9fc192ad409d | -9.4958 | -63.9562 | 2026-10-05 18:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 87.5 |
| b1c57ba5-ba49-340a-8088-cbb55391bd94 | -8.8519 | -66.8012 | 2026-10-05 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 115.1 |
| dfd8cbae-6319-3552-ba21-1685241377c2 | -9.1241 | -68.2946 | 2026-10-05 18:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| a822540c-184f-3148-bf89-676d387faa7b | -8.5929 | -66.8266 | 2026-10-05 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 9408b9a9-34b1-3ad8-9b6f-6825a6566f48 | -9.1334 | -65.9 | 2026-10-05 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 25774963-e2e7-3db5-a3b4-a8b8514b282c | -7.4889 | -42.8059 | 2026-10-05 18:50:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 106.0 |
| 7774fe64-bff8-3e4e-92b6-3d88818893b6 | -8.871 | -66.6521 | 2026-10-05 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.5 |
| d2ce7d5d-a1bd-332d-980d-30ffe9a5cc4a | -10.6463 | -68.5914 | 2026-10-05 18:50:00 | GOES-19 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 1bc20ef5-f173-3dfd-994c-c10cf573587b | -8.882 | -68.8166 | 2026-10-05 18:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| fb983a0c-863b-3dd9-b29e-813844c758d5 | -4.9051 | -41.7457 | 2026-10-05 18:50:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 99.2 |
| 6fb5dd47-2344-399c-bc34-16e182165440 | -8.5554 | -66.9759 | 2026-10-05 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 28246fce-37d7-3c92-a030-53855ee2d98f | -8.3341 | -62.8309 | 2026-10-05 18:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 95.7 |
| b14e5262-6905-3e2b-ac51-845c477a4f4f | -6.8132 | -39.2982 | 2026-10-05 18:50:00 | GOES-19 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 88.8 |
| d9f0e9c5-e9ec-3bde-9981-404a863b770a | -8.537 | -66.9764 | 2026-10-05 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.2 |
| b08587b6-c005-3fae-b61d-7e6753c56d60 | -5.9417 | -41.3524 | 2026-10-05 18:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 174.7 |
| a9556351-35d6-37f9-aa43-455d51d29c60 | -9.1438 | -67.9428 | 2026-10-05 18:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 9ec2d196-ec59-3d2d-9e05-6153761581f0 | -9.1243 | -68.2391 | 2026-10-05 18:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 44745fd1-ab79-3788-ace1-26d29a027803 | -9.7126 | -65.0951 | 2026-10-05 18:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 147.9 |
| e33d6cf9-5339-313c-b541-1da48ae5b2b2 | -9.4751 | -64.3336 | 2026-10-05 18:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 14ec8717-6f59-3bdf-af45-ec3c75b852e6 | -9.4783 | -67.6752 | 2026-10-05 18:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 9bf2da62-e422-3d1b-b060-e7f812a2fb3e | -8.852 | -66.7827 | 2026-10-05 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 4acd85de-62be-3e25-b851-7d118447484b | -9.1535 | -65.5634 | 2026-10-05 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| e4b065a8-faa1-3099-90ae-64a66e188411 | -9.1257 | -67.8322 | 2026-10-05 18:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| d907fca3-c354-3397-add5-d31d61408f46 | -4.8083 | -42.134 | 2026-10-05 18:50:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 193.6 |
| eac2aa2a-3822-32e0-8e4b-46866eca6a3b | -9.3431 | -64.7143 | 2026-10-05 18:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 49ca933f-84eb-3356-a336-156df1df6b31 | -9.4565 | -64.3344 | 2026-10-05 18:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 101.8 |


[Clique aqui para ver as próximas entradas](README165.md)
