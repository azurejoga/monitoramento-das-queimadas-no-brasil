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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbfcec08-f442-3339-92cf-467fad083733 | -8.7254 | -62.3987 | 2026-09-09 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 46103ff9-4718-30ba-8c13-f4b6c3991c26 | -5.8021 | -53.8061 | 2026-09-09 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 8184dac3-2fba-39bb-a4a9-7149bcb274ee | -8.7438 | -62.4169 | 2026-09-09 00:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 6dcf086d-a3bf-3dcd-bf6a-8fc166a07f77 | -10.5504 | -47.0903 | 2026-09-09 00:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| d5d14cd8-f67d-3eda-b6cc-5eb9a5f346f0 | -3.9603 | -59.342602 | 2026-09-09 00:25:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b8aba31-0dcf-335b-a9e4-cea6fa4e3ca0 | -6.1568 | -44.6381 | 2026-09-09 00:25:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cec899f5-602b-3f79-a522-0f2234e59a4b | -10.7341 | -45.958199 | 2026-09-09 00:25:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7d95fd0d-6d1a-36fa-b97b-d8a5ed7d4506 | -1.3155 | -54.6506 | 2026-09-09 00:25:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28b46818-0835-3713-8dce-151abfb32e10 | -1.317 | -54.657398 | 2026-09-09 00:25:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f10b3449-1536-3a4e-984d-61c6af12dd55 | -5.8208 | -53.797298 | 2026-09-09 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94b3ed31-144b-3e63-a9bb-56f5290b6a45 | -3.7931 | -52.401901 | 2026-09-09 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f643fdf2-3ccf-350d-8372-183ee6b2123c | -6.3404 | -43.560101 | 2026-09-09 00:25:00 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6bc61f8c-87c1-38c7-921b-0f65789c9e1b | -4.2937 | -49.084202 | 2026-09-09 00:25:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd85ea95-2d3d-3ca1-8e4c-5319256671bb | -3.4373 | -59.248501 | 2026-09-09 00:25:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9001e811-df73-35a3-a9f4-0cfd93a7fc52 | -2.1195 | -54.3787 | 2026-09-09 00:25:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0a90b8d-ca64-3d34-b2b2-6a3e39778b7c | -10.2921 | -46.887901 | 2026-09-09 00:25:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4427ead7-d262-30a2-8a7c-f7ea82482798 | -6.3617 | -43.6045 | 2026-09-09 00:25:00 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aeb7aa0c-62cd-3584-ac99-8fffcf91fa39 | -3.8143 | -53.763401 | 2026-09-09 00:25:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac75d4e1-344a-3eeb-8066-85bb50cdbc5c | -6.2426 | -51.666199 | 2026-09-09 00:25:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c1972bb-7c00-351f-a78e-8849057ab123 | -6.8632 | -46.012001 | 2026-09-09 00:25:00 | METOP-B | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ddd055b8-0b87-31d8-8b0b-c26c6352ff2b | -3.1598 | -60.6334 | 2026-09-09 00:25:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7229c2f7-fac7-3944-9a05-1b4a941bfc05 | -3.2611 | -50.087898 | 2026-09-09 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c122628-b249-35e7-8085-bc3182818169 | -8.746 | -62.3633 | 2026-09-09 00:25:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3b0bfe0c-cfa2-351c-a465-01f99878b13c | -3.8281 | -59.393299 | 2026-09-09 00:25:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d40fa29a-c68b-31cd-a701-276e90697782 | -10.3019 | -46.885502 | 2026-09-09 00:25:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 879ecbc6-cb1a-34fa-88f7-189f00c897bd | -5.7733 | -45.081699 | 2026-09-09 00:25:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 51022a13-769f-3755-b346-5f8dcc5cef45 | -4.9013 | -55.894901 | 2026-09-09 00:25:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f16a4a36-5cda-3e9e-9b8c-0ecbd7cc7fc1 | -1.1133 | -54.076302 | 2026-09-09 00:25:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da8a8726-0397-3baa-aa17-6be352177130 | -6.3462 | -43.5835 | 2026-09-09 00:25:00 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf83ef00-895e-387f-aeee-9e51ec94f607 | -6.8535 | -46.014301 | 2026-09-09 00:25:00 | METOP-B | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f6999ba4-55cd-3e93-9be0-662a78c8eff8 | -1.619 | -55.127102 | 2026-09-09 00:25:00 | METOP-B | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 502ae35b-2c7e-3830-9f87-31d2721fe226 | -10.6572 | -58.742901 | 2026-09-09 00:25:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b6e7819a-a65b-3181-9c22-c4a4071fd354 | -3.7751 | -58.828999 | 2026-09-09 00:25:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f0a6e6e8-b227-3111-84a9-715c9d227e5c | -10.5308 | -47.104599 | 2026-09-09 00:25:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8c47e1dd-06da-3199-b3c8-6fa0da04ae53 | -5.8178 | -53.7836 | 2026-09-09 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02f41b81-3cee-3faa-8fe8-0810be70e3f7 | -8.7403 | -62.3853 | 2026-09-09 00:25:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e211fa5b-09b1-3f89-9c73-2960581d5e6d | -5.8012 | -53.801701 | 2026-09-09 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cad66b47-9afd-3c20-a893-0cb365c2de23 | -10.997 | -45.069199 | 2026-09-09 00:25:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 63a67d04-e0a6-3199-8ad3-cabe0dd6f50a | -2.7925 | -49.5746 | 2026-09-09 00:25:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 809b5157-7293-3707-a913-2721db84dc69 | -6.7605 | -58.945499 | 2026-09-09 00:25:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0062fe3f-f56f-3eca-856b-dc5177625c4a | -3.243 | -50.812801 | 2026-09-09 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ebee223-deb6-31c8-9608-1a4816d3534f | -9.7684 | -43.479 | 2026-09-09 00:25:00 | METOP-B | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2d8d2eab-3341-3ebf-9a43-4133d473a35f | -4.4869 | -45.909302 | 2026-09-09 00:25:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5b97da94-6106-317b-bfe3-b28ac6ada5f9 | -5.5913 | -44.840401 | 2026-09-09 00:25:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 749777dc-2e17-3e11-9b96-0972adc9ccce | -7.0883 | -59.809601 | 2026-09-09 00:25:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9a201f86-a880-3506-9f26-3bfe9286312b | -8.7266 | -62.367199 | 2026-09-09 00:25:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 51eb0850-fab8-3cdd-8c0d-7ccc53cfa750 | -5.7494 | -45.0676 | 2026-09-09 00:25:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd55d744-14a0-3b2a-bc0a-e3aaff6803b4 | -3.8257 | -59.382702 | 2026-09-09 00:25:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 32ebb05b-c472-3b21-ba45-9621fabe205f | -3.1528 | -60.647999 | 2026-09-09 00:25:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4498670d-7f66-36c7-ad36-cd691dd0e7ce | -3.9025 | -59.591801 | 2026-09-09 00:25:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c1e4a800-9111-3f3b-ba8a-a30b907aaf9b | -10.7273 | -45.930801 | 2026-09-09 00:25:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b3a68fd3-e94e-3e96-bb91-20eaf6a61ce5 | -5.3169 | -56.098202 | 2026-09-09 00:25:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67d9f7fc-d60d-30ab-9f02-539488b5fdfc | -3.1445 | -60.6105 | 2026-09-09 00:25:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bd358e3b-1d83-3182-bf8c-ab2ce69a4468 | -2.9349 | -50.458698 | 2026-09-09 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fb76430-6bc2-38a4-b01b-4a8cd915a217 | -3.3716 | -59.414902 | 2026-09-09 00:25:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4e1e890f-0207-3c8a-b1e2-3aedb4e8bf57 | -10.7569 | -45.9669 | 2026-09-09 00:25:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7dda0345-285c-34e9-a9cd-ff15ea0ac74a | -8.0836 | -45.660301 | 2026-09-09 00:25:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a08d6001-a24c-3c71-bb3e-5c983bb32d6d | -5.7637 | -45.084099 | 2026-09-09 00:25:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f06b1346-37e0-34d9-a68a-1d2bbd2af4af | -3.8928 | -59.593899 | 2026-09-09 00:25:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4f621f74-6045-3b8e-8068-8c701df2f631 | -6.8594 | -45.9963 | 2026-09-09 00:25:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc70815a-43c0-3da6-840b-a551051bb4bc | -3.6642 | -58.8839 | 2026-09-09 00:25:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a5e6c0b1-c0f4-3f95-b0f0-cd38386e0a71 | -3.2356 | -47.247002 | 2026-09-09 00:25:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd0dd217-1e9f-3630-acb8-887f855b11a6 | -1.3139 | -54.643799 | 2026-09-09 00:25:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38ff1b7d-7de8-3e6d-86dc-8b69d30cfb47 | -3.6858 | -58.517799 | 2026-09-09 00:25:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e209c01d-144d-35c4-9a85-2e70cd960d03 | -3.6809 | -54.540199 | 2026-09-09 00:25:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c41eab63-1d9f-350d-971f-741174d068da | -5.369 | -56.008499 | 2026-09-09 00:25:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d048a01-9bc2-38ec-9165-3b438d04e354 | -10.5279 | -47.092999 | 2026-09-09 00:25:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bdd61e8a-2b54-3976-ae02-1c39605b15b9 | -6.7703 | -58.943401 | 2026-09-09 00:25:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f9c62ba3-df7d-3c18-af5c-7fdb40621cec | -8.0971 | -45.673698 | 2026-09-09 00:25:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 625c0d8c-54be-3f37-ab35-437c53f06ded | -10.7472 | -45.969398 | 2026-09-09 00:25:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 89a07cce-0fca-3504-bee0-ee52c53bad7e | -8.75 | -62.3834 | 2026-09-09 00:25:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7f646d15-f967-3dfb-a619-857a1ee02cef | -9.6848 | -43.4338 | 2026-09-09 00:25:00 | METOP-B | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 09e21d51-8e91-39fc-bad3-eff8f6b1241b | -5.2201 | -55.986801 | 2026-09-09 00:25:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f74b4cbc-77f1-3648-bf36-864da885a9f3 | -2.9251 | -50.460899 | 2026-09-09 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebc513b1-145e-3513-8ab4-e75bc03ad81a | -3.3595 | -59.406502 | 2026-09-09 00:25:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 252e91a4-1662-3ea4-86ac-e712755b5425 | -3.5361 | -48.176701 | 2026-09-09 00:25:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56c66d45-900f-3be0-829f-85952d5bacfa | -6.1569 | -44.680199 | 2026-09-09 00:25:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e559888b-d814-3e58-99dd-c6d231c9d9fe | -3.8127 | -53.756599 | 2026-09-09 00:25:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ea59a7a-d5ae-33f9-a220-7edd48a2c48c | -5.6712 | -50.087799 | 2026-09-09 00:25:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac899cfd-db1c-30b0-9eee-2536859dcb96 | -4.022 | -50.439602 | 2026-09-09 00:25:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2900ae1-9950-31d4-ada6-c9a0bc6767f1 | -2.8448 | -53.987099 | 2026-09-09 00:25:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c745c4e-7b80-39b0-8485-89e312877bfc | -10.3048 | -46.897598 | 2026-09-09 00:25:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 824962c4-9258-3a40-81ab-96567042b91b | -3.5585 | -58.545502 | 2026-09-09 00:25:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 989a6ead-dc5a-3993-a34f-d8233b020788 | -3.852 | -54.294102 | 2026-09-09 00:25:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4abce574-77d3-36bf-88b0-ad8816e0c993 | -5.7545 | -45.046299 | 2026-09-09 00:25:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1852acb2-fbfb-30fc-bb0e-08a662a71984 | -7.1237 | -56.509602 | 2026-09-09 00:25:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d78b4074-56e5-3cfb-a930-0792de2c079f | -3.245 | -50.821499 | 2026-09-09 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34944d35-7aec-39a0-8b42-4ea5bc06bf75 | -2.9293 | -50.479198 | 2026-09-09 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 970e440f-1249-3610-aca6-59d44c82957f | -4.5388 | -54.919201 | 2026-09-09 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54a15b2e-0879-323b-aef1-ad9a677682fc | -5.7687 | -45.062801 | 2026-09-09 00:25:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ba79f50-720c-3267-bc75-1fdd7bf01f88 | -5.8126 | -53.806301 | 2026-09-09 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2de43cb5-70f8-301f-a8cf-14b97a995874 | -3.2589 | -50.0783 | 2026-09-09 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15d1f343-fdf6-39ec-ad25-f1d9902d272b | -6.3521 | -43.606899 | 2026-09-09 00:25:00 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab411863-c59e-34a3-aeb2-59c3c88a6520 | -10.7375 | -45.971901 | 2026-09-09 00:25:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1b6f47ea-0fc5-3871-b25e-0f0cfc3e18dc | -2.9468 | -50.465599 | 2026-09-09 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1427732-e660-33ba-8aa8-c7783e0c0749 | -6.8497 | -45.998699 | 2026-09-09 00:25:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4745208-142d-3a63-830d-2f5beedf1a2d | -6.7973 | -58.926201 | 2026-09-09 00:25:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 60ca7b9f-64b6-36b0-ad01-6271e4c6b4dc | -8.0933 | -45.657902 | 2026-09-09 00:25:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aecfed92-2578-362b-adae-fb3c9bbd0745 | -2.8041 | -54.763699 | 2026-09-09 00:25:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4461fc2c-2195-31d0-b1a5-a1d14ac2c5ac | -3.435 | -59.238201 | 2026-09-09 00:25:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
