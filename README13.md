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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3108bc35-5705-3558-a9c6-68226d5003f8 | -9.95106 | -55.20493 | 2025-07-05 05:12:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ba7a7e9-7698-3a37-8d37-6fc93e114390 | -9.33389 | -58.84896 | 2025-07-05 05:12:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6d77d375-de91-31f9-82a0-c8f430920458 | -7.89931 | -61.52335 | 2025-07-05 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7b509ae-82af-36cd-888c-326154783bcd | -10.32277 | -49.93155 | 2025-07-05 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d962a83d-f464-30b2-818d-be1b7376f3e9 | -10.55749 | -49.13126 | 2025-07-05 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e752ba99-78e5-3771-b46b-4a2686ba70d6 | -11.87393 | -44.87778 | 2025-07-05 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| df5f58c8-2dfa-3327-9d56-0f8532bced83 | -8.99775 | -47.45271 | 2025-07-05 05:12:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 829cd930-51f5-3feb-8508-2b00bc34fd0d | -7.88999 | -63.04551 | 2025-07-05 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| faec198c-8c6a-3ac5-bbfa-a628a38d501c | -7.89524 | -63.03898 | 2025-07-05 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a01241b-76b2-3e24-b03c-b2a11342c338 | -9.63324 | -61.4586 | 2025-07-05 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9df2d945-f099-376d-8a1d-a463bb918491 | -10.30704 | -57.13852 | 2025-07-05 05:12:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3d096e40-e0af-3aa3-856a-eb59a840f91b | -7.89076 | -63.04302 | 2025-07-05 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3bcc53d-83d6-38b4-a144-fb90f00b744e | -10.6182 | -46.39456 | 2025-07-05 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 87bbf4f7-e600-3cb3-95a9-9e5cd9a1c8f0 | -11.02151 | -56.25714 | 2025-07-05 05:12:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4972a8f3-1c6c-32e4-8853-dfbad348453a | -11.48348 | -60.65702 | 2025-07-05 05:12:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a37b653a-d94d-3600-b2b0-dc27f59f432f | -10.61459 | -46.42636 | 2025-07-05 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 176c9e05-1391-311d-84f0-b454b30d4412 | -9.51027 | -65.58498 | 2025-07-05 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62e8693b-e8e2-341e-b1a1-3c1402934226 | -7.89606 | -63.03649 | 2025-07-05 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4554693d-ed84-37d3-91e0-925768378f90 | -12.58303 | -56.99136 | 2025-07-05 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a66ac202-5922-3e20-9308-63dfe2b6f59b | -7.89014 | -63.04662 | 2025-07-05 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fd43112-bccd-3ce4-9de8-b32c3c9bd54d | -9.61456 | -49.0236 | 2025-07-05 05:12:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 25df9353-25b9-3780-b9b6-843115e2119e | -9.61499 | -49.02029 | 2025-07-05 05:12:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 77a00d00-e024-38d0-b451-a1c297fb2868 | -9.51227 | -65.58691 | 2025-07-05 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95a78133-05d6-30e3-8d9c-05fd97599f10 | -9.50985 | -55.96148 | 2025-07-05 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| edb03a12-fbc9-3b1a-9486-68f4a2659919 | -11.05423 | -56.73937 | 2025-07-05 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 039fc22a-751d-3713-886f-075e204ecd14 | -10.60583 | -46.42858 | 2025-07-05 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a20c73cc-248a-3e48-a1bd-20bcf9c301ea | -11.80989 | -57.35483 | 2025-07-05 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c8c39ce-6974-3f3b-9609-d0083ef09ff9 | -7.89577 | -55.41991 | 2025-07-05 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d5afdac-ec9c-39be-aab5-d462eb1fce92 | -10.22415 | -59.41634 | 2025-07-05 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3f34b5b-d8ff-3700-a8b9-66558aa064e9 | -10.10184 | -58.22896 | 2025-07-05 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 73fb4b1c-585c-33a0-8394-5c45822cfca4 | -10.89056 | -56.45335 | 2025-07-05 05:12:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 713354df-9120-3046-9590-b673a545905f | -10.60821 | -46.42544 | 2025-07-05 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bd49fe34-d0c2-3b12-9110-b4fe3b7705ad | -8.99831 | -47.44839 | 2025-07-05 05:12:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad7f111c-e676-3ed6-b912-64c148fa79e3 | -9.00419 | -47.44917 | 2025-07-05 05:12:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed9ed067-9fe4-37af-a351-5ca98e8af924 | -9.58393 | -44.60956 | 2025-07-05 05:12:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b30a9296-c30a-3b9d-9aac-823407e47bfb | -9.58587 | -44.60888 | 2025-07-05 05:12:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 11bebffe-b2b9-347f-bcce-750ac469b3cb | -10.64956 | -46.40472 | 2025-07-05 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 871f00a6-22b7-3dd8-ab26-71d88046b2f6 | -12.01759 | -63.7824 | 2025-07-05 05:12:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e8dce50-a90a-3ea8-a2cf-628401501b13 | -11.45387 | -45.11863 | 2025-07-05 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b94a31ac-d30e-361d-9d07-61def55a1abd | -12.0124 | -62.81314 | 2025-07-05 05:12:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1afad8f-030d-308e-aab1-e4a3f7eb53e6 | -10.32238 | -49.93455 | 2025-07-05 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 638f7249-f60e-30c5-9472-3bf4f435c187 | -10.56328 | -49.12867 | 2025-07-05 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cc89b2c9-a53b-3877-a36f-480af40e1627 | -10.64799 | -46.40255 | 2025-07-05 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b827231c-f010-355f-becf-520b49deac49 | -10.61985 | -46.42004 | 2025-07-05 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efe479d0-a201-3933-b6bc-b60eceb173fb | -10.61283 | -46.42439 | 2025-07-05 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ddb45e10-c1a5-34a5-b704-7dba7bac2c9d | -10.61409 | -46.41393 | 2025-07-05 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f41c3bc0-63da-3a2f-a39c-f7aef26058e0 | -9.96507 | -57.50806 | 2025-07-05 05:12:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f01d337c-cdaa-3ff3-9102-410f2af38ed6 | -10.67294 | -56.54803 | 2025-07-05 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e20ecba5-1fbc-3b57-8c16-a3586946344f | -7.89583 | -63.03536 | 2025-07-05 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82e23725-84bb-3c2e-8c22-04d2e0e292ec | -10.65596 | -46.40569 | 2025-07-05 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0bf90075-eac2-35d3-9bc1-d64798f30a75 | -10.29644 | -57.14058 | 2025-07-05 05:12:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 872a97dd-a819-3f58-afa0-bb06b1432108 | -10.60939 | -46.41495 | 2025-07-05 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3c7e65d-bc82-3265-be54-4413edef13dc | -10.36166 | -48.72164 | 2025-07-05 05:12:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd9e1119-3eaa-3505-bc1c-29702531f511 | -10.36979 | -57.50637 | 2025-07-05 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1ddce8b-dc5b-38d6-80c3-73d544f50cda | -10.89342 | -56.45769 | 2025-07-05 05:12:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0df0014-71e6-3a7d-acf4-18921d32e07a | -12.02095 | -63.78662 | 2025-07-05 05:12:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c081a7c7-8a7d-3554-9543-f0a41bc98358 | -10.56825 | -49.13263 | 2025-07-05 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| be0751b9-1a3a-32b8-8f50-8b161e0e649c | -10.36123 | -48.72178 | 2025-07-05 05:12:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a745f0ef-340d-3945-9fad-4260b89d29d5 | -10.13099 | -58.21572 | 2025-07-05 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fba1e100-795a-3232-acbb-0db5c6efcd88 | -12.57954 | -56.96758 | 2025-07-05 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f10603b-6cf2-39da-8311-5eca2091d740 | -10.23052 | -56.76566 | 2025-07-05 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 387e189a-1dd4-34e5-8db6-8b00e74d57ef | -7.92015 | -61.55865 | 2025-07-05 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fc40f5f-22a2-3ed7-80e5-fb0a6f0afaa2 | -10.60645 | -46.42339 | 2025-07-05 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1e3e747-26e9-37ef-a2e9-c2cce65fcb0d | -11.87948 | -58.73709 | 2025-07-05 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e07a8958-c214-3a6d-a515-58366993c811 | -12.01696 | -63.78592 | 2025-07-05 05:12:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 063e926b-f335-382a-b391-cabd69fea403 | -10.30369 | -57.13801 | 2025-07-05 05:12:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e10d76a8-6a6a-35c0-9583-53749fbca206 | -10.36211 | -48.7179 | 2025-07-05 05:12:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56d405a2-1b62-3928-a683-5fedfa611c39 | -11.02094 | -56.26101 | 2025-07-05 05:12:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65b6a11a-0fd8-3c8c-ad55-340bc79eed99 | -10.61667 | -46.39246 | 2025-07-05 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 56d6d01a-00f2-3fc0-96ab-418bdf093588 | -8.52563 | -54.77117 | 2025-07-05 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cb430441-f59a-30ee-9eb0-cdbb4df5044b | -10.2339 | -56.76618 | 2025-07-05 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ff3c882-3093-3139-87a9-360a637ffcdf | -12.5824 | -56.9719 | 2025-07-05 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 92d0035d-b250-33b9-b245-7a9d8a345c61 | -10.61222 | -46.42943 | 2025-07-05 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 528fe54c-3b9c-310d-b2c8-f2e44319a7b2 | -9.63185 | -61.46699 | 2025-07-05 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8edcd0e7-1b32-3ee4-82cf-4221a0bae3a8 | -10.65438 | -46.40351 | 2025-07-05 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4215710a-f001-31c5-9b26-ddbe9b86e445 | -10.62158 | -46.42205 | 2025-07-05 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fee1363e-2b93-3e39-ae79-4985c7644ddc | -11.04742 | -56.7383 | 2025-07-05 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29adb4df-6540-3fb3-abc0-275a6819f45d | -7.89058 | -63.04191 | 2025-07-05 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6393fe6f-2194-32c5-80f8-b16d0d822923 | -9.95465 | -55.20549 | 2025-07-05 05:12:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2dcaab08-a4ac-3084-bb6c-f8d5ecb1fac8 | -10.56286 | -49.132 | 2025-07-05 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0a1d2d14-d518-3466-9c16-062fa6dab5e2 | -11.87672 | -58.73305 | 2025-07-05 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b9679d5-6001-308d-ada4-b0ad558e8851 | -11.05366 | -56.74309 | 2025-07-05 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 958c0e9c-7d64-32e1-bf77-8d9d0cecdc5a | -9.63254 | -61.46279 | 2025-07-05 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2b0fbef-3fe9-32bc-9425-623189626218 | -18.65678 | -55.74116 | 2025-07-05 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f9c8ec91-aa55-3504-8d0d-a84419cd9931 | -18.85445 | -47.49237 | 2025-07-05 05:14:00 | NOAA-21 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03fb5534-b662-3b39-b232-4e810220ed3d | -15.70488 | -48.30251 | 2025-07-05 05:14:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13fed28b-5a14-3976-970d-d0feeb4359ec | -18.33197 | -52.05093 | 2025-07-05 05:14:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5bc9e027-3883-3181-a8b8-cd52de7fe356 | -19.75026 | -53.99961 | 2025-07-05 05:14:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 158dd745-5670-319b-964f-ab31ebbd4aeb | -18.84911 | -47.49313 | 2025-07-05 05:14:00 | NOAA-21 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8f82bdb-df60-3b70-adf0-e33f61dd084c | -19.08639 | -56.05363 | 2025-07-05 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a11f9e33-bcb8-3581-8a76-96375aa481d6 | -19.12978 | -52.6924 | 2025-07-05 05:14:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75f7814e-d7fb-39aa-b33d-320f1d25fc97 | -18.66455 | -55.7423 | 2025-07-05 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| a42c8c2c-193b-393a-a97a-5d875db397b8 | -18.84964 | -47.48729 | 2025-07-05 05:14:00 | NOAA-21 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d2983f51-4f81-381d-8b85-55bec11982da | -20.73022 | -56.65402 | 2025-07-05 05:14:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de0561bd-6411-3153-b8f9-7e9801405edc | -20.72591 | -56.65698 | 2025-07-05 05:14:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d9b23f27-f8b2-3db9-83bd-7de7b6b8d2d9 | -18.33261 | -52.04517 | 2025-07-05 05:14:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1ea1f973-0b2f-3eaa-bf54-9c1da38f9078 | -18.84831 | -47.48639 | 2025-07-05 05:14:00 | NOAA-21 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 459bdc91-a00f-365a-bbc0-93b5a0ff09b0 | -20.72215 | -56.65625 | 2025-07-05 05:14:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1301c27f-9a87-3f9c-b751-318465a612c5 | -19.74971 | -54.00418 | 2025-07-05 05:14:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 863da0c4-f011-3c91-9c1e-07d2c1188913 | -17.76641 | -52.4488 | 2025-07-05 05:14:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README14.md)
