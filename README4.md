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
| 7d41d79a-bde9-36fc-9ad5-4cf79a481e5d | -11.83407 | -58.03818 | 2026-02-26 05:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 86fe8ad2-37ae-373e-90ce-ead5a79780da | -11.8347 | -58.03335 | 2026-02-26 05:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a390686-2109-3503-aacc-1e113fed88cc | 1.5046 | -59.9306 | 2026-02-26 05:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 3352ae1e-2940-384d-97e9-c443f781db7e | 1.4864 | -59.9308 | 2026-02-26 05:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 153.9 |
| de8e0bbb-7e05-308c-b1f9-57c39117b07c | 1.4864 | -59.9498 | 2026-02-26 05:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 929da1e1-1a23-3dfe-8cb5-4b9271fa248b | 1.5046 | -59.9497 | 2026-02-26 05:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 37.5 |
| f05e52e9-f1bc-3b26-8f9a-d8ddcaca80a3 | 1.4681 | -59.9309 | 2026-02-26 05:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 41.3 |
| a1746e45-bfe9-3c54-88d4-b02213798b86 | 1.5046 | -59.9306 | 2026-02-26 06:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 5a40c746-2ff3-3380-b093-25c0c04f0d60 | 1.5046 | -59.9497 | 2026-02-26 06:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 35862d9c-ca4c-33cf-acdf-3826591a7f24 | 1.4864 | -59.9308 | 2026-02-26 06:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 103.3 |
| c2e694de-836f-3fd0-89a1-c1e3ebefff43 | 1.4864 | -59.9498 | 2026-02-26 06:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 73.9 |
| b754a659-1495-3a8a-8f78-e94a8dde8577 | 1.4864 | -59.9308 | 2026-02-26 06:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.9 |
| d6125ae8-792d-3f81-8802-d38d57708e16 | 1.5046 | -59.9306 | 2026-02-26 06:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 3f890507-a309-37f1-af52-b39dcb7cd1ff | 1.4864 | -59.9498 | 2026-02-26 06:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 059f976b-fc30-3d10-b20f-75791fa197d8 | 1.4864 | -59.9498 | 2026-02-26 06:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.6 |
| dc4caa26-6d4b-3748-ba8c-b6082c77dde2 | 1.4864 | -59.9308 | 2026-02-26 06:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.5 |
| d80f9bae-7bfb-300a-8851-b4cfddff5795 | 4.27603 | -61.32876 | 2026-02-26 06:24:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9c76ec56-e9f6-3ddc-bab8-367a4344e06e | 1.5046 | -59.9306 | 2026-02-26 06:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 69d7014c-6e13-333d-ada4-31db074ca05f | 1.4864 | -59.9498 | 2026-02-26 06:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 82.0 |
| bef10cc1-1a55-3cc1-9af4-becde89d22c7 | 1.4681 | -59.95 | 2026-02-26 06:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 39.2 |
| b93399a4-f85a-380b-aec7-3e0ef2fc0dbe | 1.4864 | -59.9308 | 2026-02-26 06:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 562a386a-2160-3882-b045-e2b440081621 | 1.4864 | -59.9308 | 2026-02-26 06:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 143.3 |
| fb4adb17-40a8-34ba-b0e6-86b3ead492c0 | 1.5046 | -59.9306 | 2026-02-26 06:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 8365e20d-6f19-36a9-a143-d396b15bf40b | 1.4864 | -59.9498 | 2026-02-26 06:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 66e7b9cd-0537-3de6-93cf-64a36d34fb92 | 1.4681 | -59.9309 | 2026-02-26 06:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 5e8c6c91-2d87-321c-97a7-c0cdb068c2fb | 1.4681 | -59.95 | 2026-02-26 06:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 96782689-c1ca-35b6-b709-6aed38b0cc7d | 1.5046 | -59.9497 | 2026-02-26 06:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 79da2762-3147-34ed-a110-adbb37aca760 | -11.20281 | -55.91624 | 2026-02-26 06:41:00 | AQUA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 144c36df-94b8-313b-974f-8e7362322100 | -23.75753 | -54.58068 | 2026-02-26 06:44:00 | AQUA_M-M | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 82d9ec8e-dc3e-35b8-a86c-bb52f8f43d04 | 1.4681 | -59.9309 | 2026-02-26 06:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 44.5 |
| efbd0fbf-6b08-3734-af09-d1517eb8e67f | 1.4864 | -59.9498 | 2026-02-26 06:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 76.1 |
| a88b5091-48b3-3eaf-a8a4-38b673729c09 | 1.4864 | -59.9308 | 2026-02-26 06:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 6953e2a0-cd01-3bb3-9a9a-d1ba2a2842fe | 1.5046 | -59.9306 | 2026-02-26 06:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 46785864-906b-3536-8d36-02c31353ef61 | 1.5046 | -59.9497 | 2026-02-26 06:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 41.5 |
| b1f8af85-fcc2-3b76-b361-68da46088c5f | 1.4864 | -59.9308 | 2026-02-26 07:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 46.1 |
| f2d20da9-628f-3792-8a0a-79c25b0089c9 | 1.4681 | -59.9309 | 2026-02-26 07:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 1caa2df6-9180-3abd-8679-3ba2207fb848 | 1.4864 | -59.9308 | 2026-02-26 07:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 10666ded-600a-3c8b-ad7f-15c1ed208802 | 1.4864 | -59.9498 | 2026-02-26 07:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 21a96a2c-4644-3a13-bb2d-f10620b99557 | 1.4864 | -59.9308 | 2026-02-26 07:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 731fd435-e7ff-3716-8535-112124ef0fce | 1.4864 | -59.9308 | 2026-02-26 07:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 7b3e8ef8-786e-32b4-9b79-b5b05e363496 | 1.4864 | -59.9308 | 2026-02-26 07:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.5 |
| a11314fd-b17b-3a02-b2f4-58703774dcb1 | 1.4864 | -59.9308 | 2026-02-26 08:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 36.1 |
| dfe1ef2e-a470-3f30-999c-44576f2e7965 | 1.4681 | -59.9309 | 2026-02-26 08:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.1 |
| f0b5e9a0-0286-332e-a1b3-e23c17241110 | 1.4864 | -59.9308 | 2026-02-26 08:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 5757015e-2534-34b8-a35b-bcea901d48fb | 1.4864 | -59.9498 | 2026-02-26 08:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 991ec0e6-e200-364f-b7f6-143b4dbd2f91 | 1.4681 | -59.95 | 2026-02-26 08:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 43.3 |
| db0864b6-b0f4-337a-a0a3-6e93226498c2 | 1.5046 | -59.9306 | 2026-02-26 12:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 89.5 |


