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
| 96c694d2-4389-341e-96a7-a77b7b752462 | 4.39817 | -60.54536 | 2026-02-07 06:09:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 193c4437-c084-3181-b172-dd53d0413523 | 4.39775 | -60.54563 | 2026-02-07 06:09:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce47e68c-bcb5-3336-9096-66e6fa5194ec | 4.25725 | -59.83963 | 2026-02-07 06:09:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 550bc661-3d0d-315f-985b-188e8f92f6f8 | 2.18549 | -61.92169 | 2026-02-07 06:09:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 04e1ee7b-a97d-346c-b274-81ed69640560 | 3.90824 | -60.85834 | 2026-02-07 06:09:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1ccf5f8-7b0d-3853-9fa2-8bd751512161 | 2.18637 | -61.92702 | 2026-02-07 06:09:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bb9ce188-dd66-36d1-abf9-889da73cbd1d | 3.90875 | -60.8614 | 2026-02-07 06:09:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b640703-8dd8-3313-892e-3d64df96e453 | 4.39194 | -60.543 | 2026-02-07 06:09:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b24bb74-f062-3601-893e-6f8015c85671 | 4.25782 | -59.84299 | 2026-02-07 06:09:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3b7da21-6961-328a-a0fa-905bfe2570c2 | 3.9099 | -60.86116 | 2026-02-07 06:09:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4715a921-c640-33f1-b291-54847fae62d8 | 4.39234 | -60.54273 | 2026-02-07 06:09:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfc3785b-9e25-33ce-a31e-fed511c64bdb | 4.26272 | -59.83869 | 2026-02-07 06:09:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f30e214-96ea-39be-ad2a-cd63d2944ba1 | 4.25667 | -59.8362 | 2026-02-07 06:09:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a873646e-5a61-3f17-b9c6-88bf0eb5b028 | 3.97586 | -59.61169 | 2026-02-07 06:09:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef2e11f4-8462-3fa8-a9e1-93e624c11459 | 4.39722 | -60.54248 | 2026-02-07 06:09:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d8a36bd-ed3d-3efc-93f7-91c9cced6cdf | -20.3541 | -40.44676 | 2026-02-07 11:17:00 | TERRA_M-M | VIANA | ESPÍRITO SANTO | Brasil | 3205101 | 32 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| b24a7b6e-f641-336a-ac09-4dd4f7592849 | -20.35616 | -40.43445 | 2026-02-07 11:17:00 | TERRA_M-M | VIANA | ESPÍRITO SANTO | Brasil | 3205101 | 32 | 33 | nan | nan | nan | Mata Atlântica | 31.5 |
| 2ff4861c-3886-3fc1-83cf-dfceed02b120 | -20.35626 | -40.44066 | 2026-02-07 11:17:00 | TERRA_M-M | VIANA | ESPÍRITO SANTO | Brasil | 3205101 | 32 | 33 | nan | nan | nan | Mata Atlântica | 42.0 |
| f0c7b11d-c07c-306f-9028-e40c9adcafbf | 3.3168 | -59.91516 | 2026-02-07 12:48:00 | TERRA_M-T | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.8 |
| f4a31fe5-5894-398f-9eba-767378ae1f88 | 3.0502 | -61.24273 | 2026-02-07 12:48:00 | TERRA_M-T | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 53babc92-78d1-351d-8f15-c2446688f66b | 3.03898 | -61.24421 | 2026-02-07 12:48:00 | TERRA_M-T | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 2d4c043f-bb13-3bd8-94ef-122247574d8f | 1.35393 | -60.07085 | 2026-02-07 12:50:00 | TERRA_M-T | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 3286bc2c-f491-3880-9fd0-bcb42caf21f6 | -11.18316 | -55.91872 | 2026-02-07 12:55:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 98e1651a-b1ee-35f4-89a6-78570b7c72da | -20.12076 | -52.77546 | 2026-02-07 12:55:00 | TERRA_M-T | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 438cce0d-8568-3c20-a160-fa9430367a67 | -18.79437 | -52.60748 | 2026-02-07 12:55:00 | TERRA_M-T | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 30.6 |
| efb64fe2-39a2-300d-9466-0bacbc1f1aec | -18.79465 | -52.61275 | 2026-02-07 12:55:00 | TERRA_M-T | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 6e31d908-a613-38bf-acc4-e0a091c75c17 | -20.93506 | -54.95577 | 2026-02-07 12:55:00 | TERRA_M-T | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 15.5 |
| af14d76c-cde8-3a89-b574-d95e668ff44f | -25.2914 | -54.23887 | 2026-02-07 12:57:00 | TERRA_M-T | SÃO MIGUEL DO IGUAÇU | PARANÁ | Brasil | 4125704 | 41 | 33 | nan | nan | nan | Mata Atlântica | 35.2 |
| dc9a7a75-9964-3650-b017-0be019ade1c7 | -25.27947 | -54.21012 | 2026-02-07 12:57:00 | TERRA_M-T | SÃO MIGUEL DO IGUAÇU | PARANÁ | Brasil | 4125704 | 41 | 33 | nan | nan | nan | Mata Atlântica | 61.9 |
| 95cb7acb-f4a3-352d-ab10-d1fabd9ca0f5 | -25.29379 | -54.21142 | 2026-02-07 12:57:00 | TERRA_M-T | SÃO MIGUEL DO IGUAÇU | PARANÁ | Brasil | 4125704 | 41 | 33 | nan | nan | nan | Mata Atlântica | 36.1 |
| cde39ad1-ceb8-3f13-a3a8-8f42925a762d | -25.27712 | -54.23747 | 2026-02-07 12:57:00 | TERRA_M-T | SÃO MIGUEL DO IGUAÇU | PARANÁ | Brasil | 4125704 | 41 | 33 | nan | nan | nan | Mata Atlântica | 76.9 |
| 41cf8e87-a9c0-3ea3-b680-7903e8460b70 | -19.3925 | -40.2024 | 2026-02-07 13:20:00 | GOES-19 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 129.0 |
| 9eee391b-4e23-31a5-bd30-50090626cf54 | -22.7222 | -53.963 | 2026-02-07 14:40:00 | GOES-19 | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 81.3 |


