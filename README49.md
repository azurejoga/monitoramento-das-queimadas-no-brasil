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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8dd18bb4-3f8f-3fbf-bd5d-6ec217da068c | -6.90905 | -59.1493 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea0832d1-c86d-30a2-aca7-0e0d06e0f328 | -7.53339 | -61.33677 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 02d3bdf5-28cb-3506-84c6-6a18b2e5c7e0 | -7.88291 | -61.81882 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03c2374d-c54a-35ea-8a77-fb2276dd1d7c | -6.91382 | -59.54191 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98d45391-4175-313f-8afc-a518b0842206 | -6.69805 | -58.82596 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6ad1c268-b533-3ce7-9f5a-aa607c826393 | -6.78694 | -58.7853 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf885f4a-2488-3667-b3e9-5099b94882b5 | -13.46827 | -43.75725 | 2025-08-15 04:51:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c67212cc-56fa-3b94-8347-45e2f87ad82e | -10.11557 | -57.76396 | 2025-08-15 04:51:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 966c7d83-3a36-3bcf-b313-796ddab8a545 | -14.01997 | -52.04041 | 2025-08-15 04:51:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0cf5a59f-2af4-3fc3-b524-337168bc37e5 | -9.21082 | -59.66167 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aca1e29e-9a33-3084-ab81-24af1904cf8f | -7.5328 | -61.33553 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 472e7252-c49f-3cca-b826-c4afa726d8f0 | -7.52531 | -61.37698 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 035d9d72-d000-3f1d-8e32-44b2cf03d8ce | -8.29881 | -45.00414 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3008eda2-09c3-3715-9572-704e012e4ecb | -9.50355 | -60.52025 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| be2195e0-3983-367d-810c-36420e166ee6 | -9.50495 | -60.5446 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ca234db5-1111-3d08-8cce-33384852977d | -7.08237 | -59.21889 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 77951cf5-c16e-341f-8440-d92b46a17e6f | -11.35818 | -55.42722 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2a8c45c5-9f56-3d48-b38f-96877cefed57 | -7.27881 | -64.69832 | 2025-08-15 04:51:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 317937b9-9aff-327e-86eb-3bb6edb95891 | -9.21338 | -45.33813 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 42650128-e4ca-3cc2-9377-e0cad5759632 | -6.94799 | -59.99935 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c1ff8f67-3183-32cd-9843-712590ae5ef8 | -8.51795 | -43.32515 | 2025-08-15 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| fab165b4-02cc-3530-8760-69913527d367 | -6.89519 | -59.15121 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d422fb4-35da-39c5-a42b-cc413fc14f26 | -7.52425 | -61.38281 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b7c4d55-0d99-3177-a033-0dc15c82daa6 | -6.66182 | -58.81729 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cde2d1cb-a5d4-31da-a374-589977a6c735 | -11.02563 | -45.06975 | 2025-08-15 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bbbc2b81-b1a9-383c-a654-e1b9a7fe5fa1 | -9.50955 | -60.5455 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ce1a50d6-5843-37e8-98f8-4691c1fe59d7 | -6.90395 | -59.15281 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9956912-3d0b-3951-b7ec-5edfd39bcae5 | -13.31631 | -45.22766 | 2025-08-15 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 74c784dd-5c71-3a80-90b4-d3688273faa1 | -7.46066 | -59.89398 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f03a579-4cd8-3185-baa9-9c6e5e9a5dc1 | -13.32198 | -45.22504 | 2025-08-15 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e694a22a-6140-3ad2-b02d-e99ec53a16a7 | -9.17807 | -59.66874 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| cecb0a0e-1942-3398-b584-55ad770500d4 | -13.57374 | -46.96701 | 2025-08-15 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 475a0c64-58b0-30b4-84fe-22b3683f48e1 | -7.87662 | -61.8241 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53253ca7-e59d-3176-883d-a723ad9f1b96 | -9.54045 | -63.57615 | 2025-08-15 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b571c557-5de0-3f9f-9fe7-5d55eaa3531b | -9.39616 | -60.54668 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a143eb2d-6c7a-3e41-aa60-92314f7847a2 | -6.06929 | -59.96125 | 2025-08-15 04:51:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac739bf0-b780-3524-ba02-2519bd5724fc | -6.78625 | -58.7893 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62835e66-0109-3407-8631-a5ecd392710d | -9.20935 | -59.67019 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b171594-a128-3193-8459-730747b1c41f | -7.01076 | -59.82729 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6a8b883-e838-3735-ba30-028c06d89250 | -6.67042 | -58.81879 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b7384cef-c89b-38bb-84c4-8bf7adc0b21f | -7.07725 | -59.22239 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b796c820-a654-3e12-a74c-6a8292d97940 | -7.58471 | -63.46664 | 2025-08-15 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6dc7a88-b3c7-31a6-b006-83405c00c2d2 | -6.69524 | -58.84235 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d260778-7baf-3953-81cd-4482f46fe157 | -6.66865 | -58.81672 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cb5c561d-5ae5-3558-bdc2-19ca9f4dc762 | -6.90318 | -59.13065 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 320cc9fe-b598-3ddc-bc1e-8df9083fd1bb | -6.72023 | -58.82566 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47e6c853-13e0-3714-8c72-530bcf555b25 | -9.1612 | -59.68782 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6ad26e8-db0a-37e4-815f-6dbb1af30f1f | -7.52434 | -61.32909 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a711bde-9227-3ad7-a5e7-256a5e5bae74 | -7.53982 | -63.48354 | 2025-08-15 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31170b27-13c9-3da2-b52d-17405ad85c1a | -7.80293 | -61.35318 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a82f2912-ba96-3ee3-9bd5-620f2dfa6855 | -12.50862 | -47.00543 | 2025-08-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 917f22ab-9d7e-3de9-ac01-bdf2f924335d | -6.90539 | -59.14428 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 057de399-dad7-3f12-9054-2ff6fa4b5f63 | -12.58864 | -46.96879 | 2025-08-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 24eaa61f-c860-3d2d-85c9-7e9f603b80c9 | -13.11787 | -57.16607 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ed7205e-0125-3122-b0b4-b6a1afbdefb3 | -10.94634 | -56.18332 | 2025-08-15 04:51:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac66593c-117f-3b42-9999-56d8132d5944 | -13.58358 | -46.96478 | 2025-08-15 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97431b48-3e06-3a97-92e7-0303863d6abd | -13.47841 | -56.66058 | 2025-08-15 04:51:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 81dba3ce-6bc8-3b93-898b-173f934e29e5 | -7.31978 | -60.63004 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 60a6308a-ccfa-353f-98e3-d4904a4cdbcb | -12.59742 | -46.96639 | 2025-08-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9514862e-836c-3c27-828e-4fc3fffb8c42 | -12.59803 | -46.96156 | 2025-08-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 636a2787-ad23-3e44-897b-0f1c06a3ec8f | -7.08383 | -59.21038 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bba3d85e-7c8e-34ad-aadd-a9430557b4d5 | -11.34643 | -55.4139 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9ff2fb2c-d7d1-3588-9494-be57ec951261 | -12.57344 | -46.94117 | 2025-08-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0752315d-cce6-3fa7-a9c4-035dfece3b59 | -7.82307 | -61.32693 | 2025-08-15 04:51:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2aea418b-1237-369e-948a-82134c6be4c9 | -9.74783 | -48.57273 | 2025-08-15 04:51:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99246994-a064-3d9d-b7a9-2db82301e83c | -11.36037 | -55.43517 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8544edf8-cc7b-3609-912b-9077bb801ef9 | -6.9244 | -59.53426 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9976c7f7-adeb-3e98-92f9-5da9f0cf19c4 | -7.87372 | -61.81079 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d8a3d78-f872-3e4f-869a-2c53d90a40d1 | -7.07212 | -59.22594 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30bec700-8398-3fd7-a21c-1ed637b8d44f | -10.06387 | -61.22731 | 2025-08-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d6187c5-af27-39ad-8936-828a2a098cda | -7.88172 | -61.81717 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea75c283-cd13-3905-abbe-0bc2c81073c0 | -7.52569 | -61.38128 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb53d482-3eab-3a0a-b249-a6e2086ec5f0 | -9.15243 | -59.68636 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88122fa0-aade-30a6-94ad-35711d8b54bf | -6.87622 | -59.15663 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04b1b07f-56ab-37b8-8e09-7877da81d517 | -7.61556 | -63.52747 | 2025-08-15 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e1f0c17-cd59-3976-8512-315900a12525 | -7.53069 | -61.34721 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 28d37565-4a4b-3abd-bf6b-767e7d007f9d | -7.43264 | -60.02531 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70f43787-ba81-30e0-8846-4272929fa723 | -14.06765 | -46.31806 | 2025-08-15 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80c3899b-e934-386f-991b-2dd887d123b6 | -9.51039 | -60.54066 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6a937914-5de1-322a-8e67-25f28cd12b88 | -9.84095 | -45.33847 | 2025-08-15 04:51:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be6fd2d5-3af0-3104-aa29-54780750c8e2 | -6.65321 | -58.81585 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8cdaaa1b-c87b-36fa-bdc7-6ceb692b2416 | -7.3371 | -60.62184 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e474b3e-8e00-3795-9138-28a84cdc7777 | -14.41683 | -48.44023 | 2025-08-15 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b1fe108-6afd-3e31-b1a1-fd88e56e10c8 | -7.3112 | -60.62832 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2b3a567a-1fac-3ce2-8d29-a03809170b4d | -13.32238 | -45.22174 | 2025-08-15 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c679276-0bb7-3b42-99d1-3ed4c37d839d | -9.90586 | -60.43569 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13e38340-21eb-3b16-9b97-c7a04fe56741 | -7.8571 | -48.22905 | 2025-08-15 04:51:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 69f4ea09-90e3-312a-9c7f-7e461d96250c | -10.92193 | -55.00753 | 2025-08-15 04:51:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 724487b3-4d93-3f27-ac2f-08e11dfc47fa | -6.69736 | -58.83001 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ae0133ce-c281-3ba4-b8f2-4bcd2050740a | -7.53518 | -61.35111 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3e551e2e-74f5-306c-813e-5c6dee565271 | -6.9463 | -60.00916 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 82f945e0-acfa-3673-b60b-9e06efba7f56 | -7.52886 | -61.33292 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| e76752d1-7d64-3a31-a734-9fa2612a682e | -8.59887 | -62.65587 | 2025-08-15 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e98b132c-0aa2-3f75-a6e0-8b0ff85ff953 | -9.79042 | -61.50854 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7231da85-5f25-3f7d-990a-7381226ea650 | -7.2368 | -57.66893 | 2025-08-15 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22950a28-232e-3356-a191-5752b69372be | -9.17959 | -45.32783 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c07ac3d0-7546-3162-a0f0-5e9e0dd8a53f | -9.21518 | -59.66249 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b64bd99e-0bc6-3527-8a13-6c4bb35a40e5 | -6.6274 | -60.00233 | 2025-08-15 04:51:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e684491-1d25-3bb4-8c74-4a2dced3109e | -7.87602 | -61.81931 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 163f0c4b-91bb-386f-b02a-b9ed30c6be19 | -6.89444 | -59.12911 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README50.md)
