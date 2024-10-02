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

## Dados Diários - Página 171

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77b70c63-aa1e-3ea5-9d8e-b02f5ce864f8 | -11.65378 | -64.22088 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 211dc596-b4c0-3581-9828-fab688aefe03 | -11.65156 | -64.21329 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0021ee9c-9066-34b1-bca0-73797e650c99 | -11.65101 | -64.21682 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c653c529-9bcf-32ad-a8b4-bd8be2850107 | -11.60397 | -64.19122 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d490853-0d0b-3b73-bd3f-16712ff2d3f3 | -11.6012 | -64.18716 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cfbe613-9f62-357c-a341-1a0889dd7618 | -10.90231 | -64.18439 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d73b9e17-fd1e-3649-bc36-360f407a608a | -10.90176 | -64.18791 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80ce95ce-0984-37c7-b0ce-be6ddd5e76c9 | -10.89896 | -64.18365 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e57ef95c-1d22-3b91-b903-1d43b4b65f69 | -10.88348 | -64.17404 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be9e41f1-24df-3f12-990a-31454362b211 | -10.84484 | -64.18233 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6df9e207-193d-3907-a688-3fcc0e2fc9dd | -10.8443 | -64.18581 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc4be510-3042-35ba-a4e7-0b1403e0abbf | -10.83989 | -64.19231 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed07f4f7-ddc7-3db1-9171-e126193ad5a1 | -10.83658 | -64.19179 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3141cda-e8af-31ad-be75-db864e6c434d | -10.83603 | -64.19531 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb739861-73e8-318c-934b-4670bfee0f9f | -10.83494 | -64.20235 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b724b944-eb21-3e44-989b-2767e5bc755a | -11.77679 | -64.28039 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7febd735-e16c-3760-9336-864b7eca52af | -11.77624 | -64.28392 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fde6eeb6-2532-3b8d-97cd-58ab33cf0190 | -11.77511 | -64.26927 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11115cb7-950f-3b28-9630-18e1569b1050 | -11.77393 | -64.23287 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 891bdb3a-37df-3d8a-946b-569815b3e29f | -11.77339 | -64.23641 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17c2cd48-ab41-3f4a-a509-5f5e894022f1 | -11.77293 | -64.2834 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f43278b5-1336-308c-a5ac-fecdee546226 | -11.77225 | -64.22173 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 056c8f4a-6699-3dbf-83be-19a89d715e16 | -11.76297 | -64.28182 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22332889-3aa8-3ead-8b4c-28223c0a6c62 | -11.75312 | -64.28007 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d58b78db-fb57-31d3-b252-6a9ce29de1d1 | -11.75026 | -64.18908 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69eff6eb-9501-33c4-a3da-47c4218ed70a | -11.74639 | -64.19209 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62e76070-af16-322a-abad-bd162aa5d9cc | -11.74152 | -64.28906 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eab7a6d1-4b88-35e9-81f7-9c50018b6d78 | -11.73698 | -64.18695 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fba230e-9cd9-3273-b20f-9f98ac7d90d4 | -11.7363 | -64.10337 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9348ecf-845c-3027-9b0b-515ec92c86cb | -11.73517 | -64.08865 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f97ed0b5-8b5c-30f8-9d86-30e9838831ad | -11.73243 | -64.10638 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e97957b4-f590-3cd0-802b-8d6b3a7f5974 | -11.73239 | -64.08459 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff6aacb5-1736-3e93-9d96-0ca240548206 | -11.72969 | -64.12411 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0a3c6236-2564-3c59-af30-2cf48fd35d52 | -11.72961 | -64.08052 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84d5ede3-5b37-3e4a-b737-22fac9e54c90 | -11.72907 | -64.08406 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14f81d64-0c16-31da-a1ee-912bdc8bd710 | -11.72629 | -64.07999 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b39cdaac-f7db-381a-b75d-5174a58d354f | -11.72073 | -64.07186 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd0dc1e0-1aef-32fd-abd7-9f3dd2a6d714 | -11.71753 | -64.1367 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 060b1f63-ce4a-3cc3-b6ef-8aaa4c8ec7fe | -11.71239 | -64.05961 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c2fefb64-1123-3a21-a622-de6f9ee29f86 | -11.71234 | -64.03779 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff69b873-12b9-3453-a7ee-97e4dbcde1ed | -11.7111 | -64.2661 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 135b0a96-9832-39bf-a837-a112bd954ba8 | -11.70629 | -64.055 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b467764-d88d-3af6-9885-70fd4b3567fd | -11.70574 | -64.05856 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4c99a9c-a753-34ed-8a9a-c31e53f0cbf5 | -11.70296 | -64.05448 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ac343ef-5845-3dc9-8394-76ce5a8e517c | -11.70241 | -64.05802 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6210d97-36d2-3446-b6c2-d8a3f5c79cf2 | -11.7006 | -64.26804 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e2bb0e4-fa74-345e-ac20-c107b519f8eb | -11.67738 | -64.04702 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8aa3944e-3f36-313c-9a63-affd01f3239b | -11.6735 | -64.05004 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9aef24e-e40e-39e5-89a5-4262718b695f | -11.67065 | -64.0024 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e60ad2c-9277-3534-912e-acaa0d35a82f | -11.98381 | -64.73878 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb2ca7ad-743f-3fc2-bfcc-35fc417abe7f | -11.97664 | -64.74123 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8aed9381-5877-3dac-969b-4b5d5327ee30 | -12.49476 | -63.95911 | 2024-10-02 05:36:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f4f205b-d3f1-3427-b088-bfc5c35f9182 | -12.47436 | -64.04778 | 2024-10-02 05:36:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdbcb551-c63d-3b84-b26a-6b2d24957b86 | -12.47381 | -64.05135 | 2024-10-02 05:36:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88a8b311-3403-39e7-808f-e52b276681da | -12.47326 | -64.05493 | 2024-10-02 05:36:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2ccba15-cbff-3da6-81fd-a499093737f5 | -12.46992 | -64.05441 | 2024-10-02 05:36:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0581268e-db98-3a1a-8fb3-7391c7532809 | -12.46987 | -64.03239 | 2024-10-02 05:36:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57d5063b-5873-3329-8e7b-e163cd5936a0 | -12.4638 | -64.04977 | 2024-10-02 05:36:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e226fa5-8eb5-32ff-a2b4-97e376300cae | -12.35149 | -64.3172 | 2024-10-02 05:36:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ce687eb-fd65-3f54-9ed0-913e86b05994 | -12.34817 | -64.31666 | 2024-10-02 05:36:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abbec660-f3de-3286-8b79-f24b3f0c7f6a | -11.66808 | -64.99769 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0aca4f15-d3e1-352d-9bdf-4754d1d1347b | -11.66753 | -65.00121 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 961a455e-be08-397f-90aa-32ec7f9c7d40 | -11.66698 | -65.00471 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 595bc1fb-be0d-30f0-91c7-62def4576b10 | -11.66678 | -65.1992 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6bec782b-50e1-342a-9634-3210249de12e | -11.66587 | -65.01173 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b85b0c90-5870-3fb8-95da-bf349b069350 | -11.66642 | -65.00822 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a85864b4-6eaa-31a7-8159-eba27b66daa0 | -9.96796 | -67.20453 | 2024-10-02 05:36:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 02bf12e5-294b-3822-90c9-fccae0e06ae1 | -9.96729 | -67.20857 | 2024-10-02 05:36:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d004c89-1656-3bbd-a9bd-19b4928c55a1 | -9.96376 | -67.20796 | 2024-10-02 05:36:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df83a0b8-ba06-38da-9bc2-b13840fa1047 | -9.93559 | -66.75784 | 2024-10-02 05:36:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a1dca8a-f0fb-3332-9f19-47e3e7423e1b | -9.91825 | -66.84267 | 2024-10-02 05:36:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ab562f3d-3717-3794-b976-a36075e8c591 | -9.91164 | -67.30335 | 2024-10-02 05:36:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae860ffb-5bc5-3084-9dbb-12774ffa46e7 | -9.91096 | -67.30743 | 2024-10-02 05:36:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebbe8c62-a247-3d13-bc4a-a15daf71011b | -9.90894 | -67.31968 | 2024-10-02 05:36:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef1d59ec-09f3-37f1-bec6-3a011e7a1657 | -9.87405 | -67.30959 | 2024-10-02 05:36:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8477f28-bb07-3035-96df-c9b5d00facda | -9.8685 | -66.9716 | 2024-10-02 05:36:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 760c830b-2ff1-3ca8-9743-844e31f0c757 | -9.86499 | -66.97102 | 2024-10-02 05:36:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3cd0a29-e17e-3352-b13d-e7c0fd15cf3f | -9.85025 | -66.43838 | 2024-10-02 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47806545-fdf0-376e-98fe-7fb60f10bc25 | -9.81397 | -66.63949 | 2024-10-02 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d05473a-7adb-36a9-8705-62b97997adce | -9.70271 | -66.85296 | 2024-10-02 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea7835ae-a667-3e01-a87c-dc01a4fc1d75 | -9.69922 | -66.85238 | 2024-10-02 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 396f5bc9-8ae4-3b50-8af2-68392f947e98 | -17.21973 | -56.16675 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8e211434-dd70-3ed3-a82c-ac451940bf55 | -17.21931 | -56.17051 | 2024-10-02 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 685d82b8-1db2-33ff-9ab1-f34b782b49f9 | -10.7203 | -69.10191 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbda8b50-2b3a-3df2-b60e-145c183a444b | -10.70965 | -69.02421 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eace6076-b8bc-35c5-8ca3-fe062081b1e7 | -10.70579 | -69.02353 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1d4d5f9-85b3-39c5-8afa-b5749e857c41 | -10.60859 | -69.04983 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e1652fd-69cb-335c-b8c4-ee2fc8385fb8 | -10.4942 | -69.1298 | 2024-10-02 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2db7f72-8bf3-3b4e-a6b3-eaf0c7489031 | -10.49031 | -69.1291 | 2024-10-02 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8198aad-8df6-3972-908e-46ae1c09b356 | -10.85815 | -68.28434 | 2024-10-02 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ebd9de20-4e25-3d67-99a5-a5b337c31b33 | -10.72599 | -68.88248 | 2024-10-02 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0125e2b5-ce88-3e9d-ae46-24034328a067 | -10.71728 | -68.77318 | 2024-10-02 05:36:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b558ca21-d3e5-36c1-9823-c36eac0e43fd | -10.68441 | -68.89498 | 2024-10-02 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb9cb8b8-9273-3211-816a-3eb7640502e5 | -10.68187 | -68.89737 | 2024-10-02 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc2c8828-fb0e-3e77-b07a-694ca6e9d3b8 | -10.68138 | -68.64382 | 2024-10-02 05:36:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e912631-f1da-3d35-aea3-6de3195f9152 | -10.67839 | -68.63853 | 2024-10-02 05:36:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40481d77-a5d8-3d3c-826b-8f8b9f722b6b | -10.62964 | -68.67345 | 2024-10-02 05:36:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a10d98f-4341-3809-bda9-1723bf21d3b0 | -10.62586 | -68.6728 | 2024-10-02 05:36:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 359b57e9-89ed-3029-8ef1-65b6e127fffd | -10.61198 | -67.87197 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ca97349c-4b06-3cbe-91ad-00933e05c59b | -10.60765 | -67.8756 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README172.md)
