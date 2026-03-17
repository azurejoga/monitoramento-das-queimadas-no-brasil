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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17377fa6-b2c9-3708-986d-c3f3fa53d452 | 1.70121 | -60.29477 | 2026-03-17 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea912be3-f2a8-3e9f-83f6-2e5c3ef7f4aa | 3.14616 | -60.71792 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79b0fb8b-9ac4-3e4a-8925-9b7217719b82 | 3.0861 | -60.77037 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 265c97e2-638b-3259-85d3-a7f5f52a682a | 3.13176 | -60.73433 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 476ef208-a77e-3148-bc27-73e7c2fd6ae5 | 3.7866 | -61.31651 | 2026-03-17 05:27:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d90955f-fe55-357f-b3ab-e84e1257a497 | 1.09832 | -59.27379 | 2026-03-17 05:27:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbb3e7d1-c728-3874-b3ab-3ad252161c3e | 1.33026 | -60.70727 | 2026-03-17 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ab55691-b72c-3bb8-acb8-ab908a8b2ee6 | 2.78796 | -60.71457 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 012be848-3684-34d3-810b-535b5b75629c | 0.83685 | -60.33943 | 2026-03-17 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7112c016-61ab-3738-9b44-bb57a3565f2f | 2.20712 | -60.1552 | 2026-03-17 05:27:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b00f2de5-985b-3566-bed4-f8665d7a6e51 | 3.12036 | -60.7509 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 79973667-d408-339e-9d37-4129c52ee55c | 3.17809 | -60.1177 | 2026-03-17 05:27:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0304a3ca-fba5-33b6-810b-5df67887a59d | 0.5807 | -59.90107 | 2026-03-17 05:27:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac2dfe87-416b-3b39-895f-2b34381185eb | 0.83248 | -60.33309 | 2026-03-17 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7db40c05-f3b0-34cc-a4f6-05114d57a53f | 2.37639 | -60.77873 | 2026-03-17 05:27:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c972edf-db69-362d-9021-4d4b487b5e1d | 3.12866 | -60.73899 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 17d15a34-8ddc-34f9-932c-c2820e21f21f | 3.19342 | -60.12936 | 2026-03-17 05:27:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a51eea8-173e-3163-afa7-a8719c09e5b8 | 0.83524 | -60.32915 | 2026-03-17 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1083000d-f9f7-326c-8eb4-7bacc129c0f6 | 1.20864 | -59.97539 | 2026-03-17 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab71df70-147e-3b68-8b44-da25d1000650 | 3.78549 | -61.30935 | 2026-03-17 05:27:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fabb7ed-2af3-3ec3-96ee-c73226f57495 | 0.83438 | -60.25917 | 2026-03-17 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc764aad-5e61-3b12-beb6-8c597093af3c | 3.14007 | -60.7224 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26e83bf1-5fba-3020-85a8-c1602f5faa9d | 3.08333 | -60.77434 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5894f4c7-e9a6-3a01-bad6-932355ba7a4c | 3.19066 | -60.13329 | 2026-03-17 05:27:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3aeacb3-df4a-3aaf-9911-b06afacd9d25 | 1.15119 | -60.91142 | 2026-03-17 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d1538f0-8bce-3385-926c-56d3534311d1 | 3.12313 | -60.74693 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c9c55896-2001-3f08-a894-f2e49dfdf104 | 3.84833 | -60.87928 | 2026-03-17 05:27:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30cb1e8c-a334-3b10-a9bb-d53f5becf838 | 3.08941 | -60.76987 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6720f14a-01f7-3fdf-854b-7bb76ef37f73 | 3.72573 | -61.29285 | 2026-03-17 05:27:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29df5383-7b39-3e26-9e78-6c892ce76613 | 3.11813 | -60.75834 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 939de1f7-b747-3a6c-b7d1-0dd1f7c95cb1 | 3.17863 | -60.12112 | 2026-03-17 05:27:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66b05a56-340b-3701-8cab-b309ec9fb4ca | 3.12644 | -60.74643 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fa238cb4-01e0-3ad7-80f0-02750f9cb450 | 1.55005 | -60.2833 | 2026-03-17 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7cd5cd16-0fcb-3447-a7f0-456331b4749c | 3.14446 | -60.72882 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 01d31c96-1c7e-3c9e-ae6d-e15dfe4aa08d | 1.04031 | -60.41983 | 2026-03-17 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76fdc595-d125-3b7d-9fd1-d7e5dad8049b | 3.12258 | -60.74347 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 067d9d0e-f8b4-382a-a434-2c64b2902dc3 | 3.1259 | -60.74296 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 999d76c6-2b74-32df-bfcf-56b72becdf5e | 3.12421 | -60.75386 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d456dba7-bf0a-3726-a566-e24af1b33a3e | 2.74094 | -60.43644 | 2026-03-17 05:27:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96e79872-ce80-314f-9d51-aab53b960baf | 3.05129 | -60.78637 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b392cde8-97ed-349a-8ded-c4acac5b1d34 | 1.9852 | -60.88954 | 2026-03-17 05:27:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8eaad1ef-ca57-3330-ab5b-b852489c56b3 | 2.8285 | -60.03612 | 2026-03-17 05:27:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fa3eb99-7c8b-3355-873f-82fe679e3380 | 3.0271 | -61.11134 | 2026-03-17 05:27:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b43a9a5-7534-3d73-a782-2e5ac54867e9 | 0.83739 | -60.34285 | 2026-03-17 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5343828a-ed23-3e4f-badf-930c1cf452df | 3.72629 | -61.29642 | 2026-03-17 05:27:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb934b7b-49c1-3a64-a110-0d39b11a65d3 | 3.14115 | -60.72934 | 2026-03-17 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d60ae30e-a5e6-3923-87e1-51b638f045a3 | 3.87481 | -60.11327 | 2026-03-17 05:27:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 99937523-3da6-36a2-9e62-eaf2dd5ee51e | 1.32918 | -60.70041 | 2026-03-17 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8e199904-6e2c-3ddb-bdfa-acc075264514 | -16.45289 | -58.17511 | 2026-03-17 05:33:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 3d2adc2a-fc06-3b0e-84d1-45a1f931b299 | -16.57971 | -57.80136 | 2026-03-17 05:33:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 6c54e094-a7f3-3b90-9a08-35cb6775075e | -16.57526 | -57.80075 | 2026-03-17 05:33:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d6bf8000-3f92-3fd3-928f-01d9e212980c | -16.44855 | -58.1745 | 2026-03-17 05:33:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 388dd249-583f-3bc8-9077-63acd1abdbb8 | -16.58991 | -58.22232 | 2026-03-17 05:33:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5e322447-5dca-356c-a2d9-38cccf0ba2cf | -16.44684 | -58.17559 | 2026-03-17 05:33:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d9087e4c-bc24-3a46-b4b7-d203c805152e | -16.45062 | -58.18054 | 2026-03-17 05:33:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9f869339-3b3f-3329-a2a2-cfaf0a274873 | -16.44802 | -58.17883 | 2026-03-17 05:33:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f0cbb42a-83f7-3dcd-8b56-d843ac12dfbf | -16.45118 | -58.1762 | 2026-03-17 05:33:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 86f3dc21-6e2b-3692-b2d7-7c51477236f7 | 3.72789 | -61.29817 | 2026-03-17 05:57:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34ab24fa-3508-33f5-93d4-72efd7b23b58 | 3.02845 | -61.11185 | 2026-03-17 05:57:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47f9c38a-7cf0-30ee-939c-0bfd27ca8118 | 3.14119 | -60.71831 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1f2cc195-6040-3bc0-bdf5-c7667a0f2306 | 3.13059 | -60.73457 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| dfc94223-d679-3d52-bdcf-e3803d140b29 | 3.72705 | -61.29303 | 2026-03-17 05:57:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6db84270-9c3b-3f9a-b245-7240fdb72506 | 1.9861 | -60.89185 | 2026-03-17 05:57:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7879d839-747f-3902-8368-dc84b2cb7b15 | 1.01183 | -60.23173 | 2026-03-17 05:57:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0eb5b2e-90fc-32fd-a956-47af0e1c955b | 1.63842 | -60.28155 | 2026-03-17 05:57:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 71c6ee82-61a2-3c20-ac06-965e132f7593 | 3.12235 | -60.76321 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 59336a2f-6436-3d62-80fc-ef30360d515a | 3.13473 | -60.73104 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05d204c5-4e2e-31da-9b2a-760d8e4a4a68 | 1.20916 | -60.16146 | 2026-03-17 05:57:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66d3b24f-9030-389d-a420-d98b9db9c72e | 3.1479 | -60.73281 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7c54da28-8286-3290-82a1-03cbd346dd54 | 0.90793 | -60.29807 | 2026-03-17 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76d7c013-6a27-3c27-b454-b2f037a62826 | 0.83845 | -60.33512 | 2026-03-17 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bad7cf37-d86b-313c-b279-ed40ab79b876 | 3.14727 | -60.72902 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4aa9a27f-a736-3dc7-81db-eb1a0222b429 | 3.11756 | -60.76009 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 86602d90-4201-351f-8c64-1527e5face62 | 3.75199 | -61.32059 | 2026-03-17 05:57:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 400b17fd-a0e7-3703-95e5-03c2cc7aad1d | 3.0848 | -60.76928 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 825dcb1f-6c3e-3b38-a00c-889d62dcc080 | 2.74089 | -60.43396 | 2026-03-17 05:57:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e77d680-7309-3762-b81a-88e5623f32df | 2.85871 | -60.73377 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 135d0757-f721-37b1-ae9d-674620522c3e | 3.18067 | -60.12085 | 2026-03-17 05:57:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9da461d8-e9b4-301e-b331-1b6bce152f22 | 3.13652 | -60.71799 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aebcdb28-6b5a-32e7-905e-1361ec5ddb87 | 3.12509 | -60.85935 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07b124a5-ade8-3fdc-bf31-95e850f0f071 | 3.18503 | -60.12016 | 2026-03-17 05:57:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c56a632-b6f0-346a-b028-84c457939f67 | 3.14246 | -60.7259 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c39d1f9f-57f1-3ffd-8bea-9ad7059dad4a | 3.14537 | -60.71765 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8835f50-c03a-3802-a34b-2dabfcf53712 | 1.33011 | -60.70731 | 2026-03-17 05:57:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6ef265ab-55cd-37d3-865b-b08222658733 | 3.12112 | -60.75562 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b2aa7649-6818-3f99-ae69-a3798b06c405 | 3.19579 | -60.13123 | 2026-03-17 05:57:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 121a3aa1-8a1d-3180-ba8f-8942c59737d4 | 0.83986 | -60.34385 | 2026-03-17 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e83ec48c-0ff6-3b6c-86f3-0590be1e3051 | 3.14313 | -60.73252 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eaafda78-9edb-3ccb-a904-ae3d7b608d2c | 3.12642 | -60.73524 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| beef5a39-3172-3dc7-b08a-1f9245d43b67 | 3.11818 | -60.76389 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 56e64ed0-98e8-35a4-865f-0e7cc4743198 | 3.12095 | -60.86001 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d54ba489-2371-301e-9208-d60fed5bc159 | 0.834 | -60.33584 | 2026-03-17 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8fad9d08-cd13-30e2-acc4-f9350206c986 | 1.32945 | -60.70326 | 2026-03-17 05:57:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e11f7f4-bc66-3cb1-ac21-daea45e49bc8 | 2.79023 | -60.71324 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0aa23086-61dd-3d39-99f2-aaba07b99688 | 0.95678 | -60.23183 | 2026-03-17 05:57:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d86c5515-d25c-3d66-9cf1-62620dde2ff1 | 3.12174 | -60.75942 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 14.4 |
| bedab541-9a03-3dc3-880d-4c1b939de910 | 3.14309 | -60.72969 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7a0b9150-18dd-3d3b-9973-3ab5a5b77589 | 1.08986 | -59.8945 | 2026-03-17 05:57:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29cd8e1c-7353-3bb7-8137-5b527dc656ee | 3.12764 | -60.74286 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 178eccf4-5adc-3fe4-af11-c2481c8c6361 | 1.01016 | -60.23425 | 2026-03-17 05:57:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README6.md)
