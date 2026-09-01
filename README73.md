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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab5e3e10-f128-376f-b141-192ee13c393e | -3.63264 | -60.55372 | 2026-09-01 05:33:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65e8eaea-afc8-3683-a4e1-bf85bf40c197 | -3.50341 | -59.04937 | 2026-09-01 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f311a8c-3fa3-33d1-89e3-ff629298831e | -3.54635 | -54.7183 | 2026-09-01 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d64d58b8-c90c-39ba-ab3b-d5c933a3501d | -3.41407 | -61.33968 | 2026-09-01 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b53dbc33-2b1c-349d-a360-268b4fdcbdc0 | 0.01258 | -60.5999 | 2026-09-01 05:33:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a34da6da-057c-3433-a4c8-ddaf44ee67bc | -4.15589 | -60.72495 | 2026-09-01 05:33:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecff3184-f166-33bb-8ded-873097958f6f | 0.00873 | -60.59698 | 2026-09-01 05:33:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82a19ab6-1574-3f82-9ec1-dedb8673d383 | -3.6226 | -60.55215 | 2026-09-01 05:33:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 686d51af-a798-3765-9b63-500472559246 | -3.34463 | -59.43564 | 2026-09-01 05:33:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5abd947-805e-39c9-9ca6-8c953da6ae76 | -3.62709 | -60.56733 | 2026-09-01 05:33:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e77a1f17-7f24-30fc-93d0-4e14c223c787 | -5.25658 | -55.91205 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee03330b-195f-3647-9d2c-3980dc2610b0 | -1.44477 | -54.23463 | 2026-09-01 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92e3262e-79ed-3632-8875-4e43c857494a | -5.25535 | -55.89046 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8c8ca4f-a517-3a00-8bf9-ee12a0da2613 | -3.09615 | -61.15931 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e521c5bd-0080-3dcc-bf38-fd6a3c697a59 | -3.45315 | -61.7164 | 2026-09-01 05:33:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76c63620-4964-31ca-8d05-6d95b9e42218 | -5.25471 | -55.89472 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bf5bacf-3546-3e3f-9afc-f9e62a337c1b | -3.63544 | -60.55777 | 2026-09-01 05:33:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fd154c9-097a-37ad-a4c2-37cce02fbfbe | 0.19963 | -51.5218 | 2026-09-01 05:33:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afc13ed6-0adc-3fc1-829f-38fa8c0b33b6 | -1.27678 | -60.33101 | 2026-09-01 05:33:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0479c7c6-c6e2-392f-95bc-134fb1747b81 | -4.96388 | -55.85224 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df48cc94-7410-3856-bc4a-2e51900cc25f | -3.62429 | -60.56328 | 2026-09-01 05:33:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7ac7ec38-6721-39da-9eb7-3548f52946a2 | -3.34177 | -59.43133 | 2026-09-01 05:33:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b75001e5-fbbc-3ef1-a56a-661988755b0e | -3.6131 | -59.06463 | 2026-09-01 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 633e4dc1-e06a-3155-8339-009bbeec4a5d | -4.85452 | -55.83294 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d075a484-93ba-3c2a-ac0e-131000830f99 | -3.62149 | -60.55922 | 2026-09-01 05:33:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 34ae8960-5440-3b7d-8e30-776d9759c826 | -1.46788 | -54.20819 | 2026-09-01 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 946345a9-b14c-3cbe-b57e-b396df8e5265 | -5.24973 | -55.89829 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5414601-7ef4-3d66-89e2-3f739291ab2c | -1.46296 | -54.23434 | 2026-09-01 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64d8abb7-5e55-32c3-a895-772045f3569f | -4.36339 | -60.9405 | 2026-09-01 05:33:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d669ff4-a9ab-3f5a-96e6-1def4254e9f1 | -3.40686 | -61.32089 | 2026-09-01 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b57487fb-136f-3a5f-a9fc-a18c1961da37 | -3.1864 | -60.1532 | 2026-09-01 05:33:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 667f387f-152e-347c-9603-216bbdd8c0b6 | -3.12654 | -61.18173 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7d79806-ca25-373c-9439-31870f337b67 | -3.50879 | -56.31859 | 2026-09-01 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b0f082c-e6a4-3342-9bc9-ca645af3d6dd | -3.11838 | -61.23345 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 71a3bad8-cec2-3598-a00a-b0ac7ac50a9c | 0.19344 | -60.49718 | 2026-09-01 05:33:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66533011-b7db-3986-9801-5d0620309540 | -4.21424 | -48.60803 | 2026-09-01 05:33:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b193128f-9676-31d7-ae58-95a2fefe3ad5 | -4.20728 | -48.6073 | 2026-09-01 05:33:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce91ab7d-5dcb-343b-a54e-774b8d8a6d65 | 0.19675 | -60.49667 | 2026-09-01 05:33:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 528d91b8-dac3-3cc2-b5eb-b938f757b910 | -2.91466 | -54.12 | 2026-09-01 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 530d4890-2cc5-323d-ad4b-6ea92a6ed8c2 | -4.96887 | -55.84864 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 377ecc7b-9f57-3a25-b01c-99419d498167 | -3.50403 | -59.04543 | 2026-09-01 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75c04bab-d0af-32d5-9269-d59e0da6fdb1 | -3.40355 | -61.32037 | 2026-09-01 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93307298-bc50-3653-b746-05739352c5dc | -3.65842 | -58.91264 | 2026-09-01 05:33:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76ef78b3-942f-3d8c-aefc-f07322eeb8c0 | -3.11784 | -61.2369 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 194a2ff4-794c-3d87-b43d-bce31af3aad5 | -5.24724 | -55.91507 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 94a699ce-e4b9-3499-a109-6c2db126f82b | -5.24476 | -55.90182 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdcdb638-6d22-33b1-92d7-3572ff5e6e25 | -3.62539 | -60.55621 | 2026-09-01 05:33:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 19fe0264-cbe9-3e25-8f75-3a306dd816bb | -3.2082 | -61.13742 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8e3ff1ec-54ac-3ed7-b9ed-18fe0f17308b | -3.62764 | -60.5638 | 2026-09-01 05:33:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96f5cbf6-9799-3074-aa59-dab0c793bf36 | -3.83421 | -55.56427 | 2026-09-01 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a738c960-f874-3d18-8ed5-1b4212027dd5 | -4.22241 | -59.8698 | 2026-09-01 05:33:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d94f2204-8415-394a-80b7-455fcb47c963 | -5.24785 | -55.91093 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 895e1ca1-0fde-3789-87aa-9936926b4f17 | -5.24848 | -55.90669 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 65c7e113-d9a0-33a4-9eba-bd5aa8d21b4d | -3.90607 | -59.65035 | 2026-09-01 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff72c7bb-5e34-35c8-b9d5-506f30f00433 | 0.97776 | -59.39745 | 2026-09-01 05:33:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1e0d3aa-c3c1-37d2-abbb-879e1f8002a2 | -4.15305 | -60.6992 | 2026-09-01 05:33:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c181dea-7322-3eb2-aa27-cadd63e5a325 | -5.88733 | -52.15473 | 2026-09-01 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| be41db7b-bcb3-3ff5-9a6c-cc17beb5f006 | -4.15475 | -60.71032 | 2026-09-01 05:33:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8b971c9-443e-3829-9f7e-5154b7c1e3dd | -3.55628 | -59.03576 | 2026-09-01 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 155b2fa9-67ca-398b-aacb-c2b50956136a | -1.50444 | -54.96666 | 2026-09-01 05:33:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42089d60-92e9-37d2-8ab8-ea27c520a603 | -3.62205 | -60.55569 | 2026-09-01 05:33:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 13a39a92-c66f-349b-b343-59194e94c21f | -3.39639 | -61.32278 | 2026-09-01 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99491a95-6d8a-3471-80eb-1a81785d50a9 | -3.83324 | -55.56575 | 2026-09-01 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f0065cb-7036-3815-8676-dfbc81778d35 | -5.25284 | -55.90734 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4238de8c-c13a-31ea-b483-29570ba24cbc | -4.15195 | -60.70626 | 2026-09-01 05:33:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 608bb073-b223-3999-a102-c562f50efed1 | -3.62315 | -60.54862 | 2026-09-01 05:33:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 828ba5d3-aea4-3afd-b00a-6b078f9f4a48 | -3.20716 | -61.16556 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f39909f9-9537-30d7-882a-2be29fc61137 | -3.09625 | -61.20174 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 836ed92f-c496-3983-9f38-55b4a1ab4eac | -3.79265 | -59.34969 | 2026-09-01 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2420fa95-7bb3-39e5-b417-d7338b7c18bc | -3.61477 | -59.07696 | 2026-09-01 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4113f668-e236-3331-a844-37c589ff44c0 | -3.61249 | -59.06856 | 2026-09-01 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 268f37f7-6238-3c4a-b9bb-c79e56ca9fc1 | -3.61925 | -60.55164 | 2026-09-01 05:33:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2be0ec7-b43a-3cb7-a020-8166345a5989 | -5.25221 | -55.91158 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5152cca5-a4f6-37d5-8c8d-ae8016e924f8 | -4.96325 | -55.8564 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dcd2084f-b0e4-3065-ba00-bdf335cdd631 | 0.31453 | -60.44617 | 2026-09-01 05:33:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc603c18-a5f2-37bc-baa5-bdb60ae284fd | -3.09031 | -61.5182 | 2026-09-01 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 61c09600-499f-3596-ae0a-be4550ddcebd | -4.84585 | -55.83152 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12190b41-d1ce-3e34-a178-11ca3e5ad71b | -3.30314 | -64.83713 | 2026-09-01 05:33:00 | NOAA-20 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fc6ba631-80e1-3140-b722-b28dfb6e90f3 | -4.96824 | -55.85283 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e58fd584-b9b6-32e5-9655-bdfa58dbd0a7 | -4.96514 | -55.84387 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9ce30f5-1953-3986-adcd-8f9803d27afd | -2.66452 | -59.36865 | 2026-09-01 05:33:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18b745be-6654-3050-b272-c4cba71ce6c5 | -4.6486 | -55.85459 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25e85631-f7ae-372f-891f-06e9e42c9d9f | -4.85018 | -55.83224 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2ab41d6-fa29-3085-9c4a-c2d0a6333729 | -3.63099 | -60.56432 | 2026-09-01 05:33:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74546f72-69b0-30bf-80e2-43d525a64d83 | -3.21048 | -61.16608 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6458ecd7-a440-35d7-ab8d-ba3579243c6a | 0.19068 | -60.50113 | 2026-09-01 05:33:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df19b4df-168e-3058-93cb-e06a559fd3b5 | -4.97014 | -55.84024 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4ec1ad64-c4e1-39fa-9362-105636d4ea66 | -2.67081 | -59.37352 | 2026-09-01 05:33:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b52369c-e304-3a8e-a447-f3f06d14e9f3 | -1.6207 | -55.16969 | 2026-09-01 05:33:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6d20c11-c7f2-3c27-9b57-f3e849579e67 | -3.16341 | -58.7925 | 2026-09-01 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3574107f-d474-3a38-96e9-89d235f1104c | -4.95952 | -55.85165 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16f170cb-f0e7-3d79-85b5-7d937f73be24 | -4.29243 | -49.10112 | 2026-09-01 05:33:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7ffa57dd-d226-3a1f-98a8-59b05cb6740c | -4.18409 | -63.16011 | 2026-09-01 05:33:00 | NOAA-20 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b451eba-861c-3ebf-9e26-bfa1b442e352 | -4.95516 | -55.85108 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58861106-ebc6-3ba8-8342-c1e08f116616 | -3.62374 | -60.56681 | 2026-09-01 05:33:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 80986f46-e0c5-319e-9e69-78c8873e4c4b | -3.26315 | -58.24212 | 2026-09-01 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a11a9d6-7794-3220-b66b-d84e628add1d | -4.96451 | -55.84803 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b074592-b438-3a52-8494-9ed9e042dd74 | 0.14721 | -60.39878 | 2026-09-01 05:33:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7609ef8c-fe8d-3214-b287-860f3d7d971c | -4.96262 | -55.86053 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e763c31-5f6a-3964-b23d-f1e37aa55ba9 | 0.97441 | -59.39798 | 2026-09-01 05:33:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README74.md)
