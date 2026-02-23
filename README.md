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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9dfc658e-5ce2-3a67-a067-7beb581b63a2 | 4.1901 | -60.1161 | 2026-02-23 00:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 2d643f43-4ad1-3683-9ba2-239964214acc | 2.2333 | -60.7018 | 2026-02-23 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 4a8e3299-1106-3f13-98ee-dac43f96267a | 4.2793 | -60.7988 | 2026-02-23 00:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 07684513-8b08-3073-ba8e-4d808b305a38 | 4.2084 | -60.1156 | 2026-02-23 00:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 48.9 |
| d4c28a5b-64ee-38c4-8ac8-b9f2d2cb184f | 2.2333 | -60.7018 | 2026-02-23 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 4ec158d4-528b-348f-83d6-de7a6870296b | -9.9741 | -36.009 | 2026-02-23 00:20:00 | GOES-19 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 145.5 |
| b5e0749b-dd99-3095-9ea1-848c1b670841 | 2.2333 | -60.7018 | 2026-02-23 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 48.3 |
| e7449cd5-c274-3451-b41c-602fa05c0f45 | 2.2333 | -60.7018 | 2026-02-23 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 26f57952-341f-37f3-9e38-f2cb3a55b8ba | 2.2333 | -60.7018 | 2026-02-23 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 430c7b39-d6c9-3ee7-b2b7-705c968e6d8e | 2.2333 | -60.7018 | 2026-02-23 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 37.9 |
| c69ce4e9-d5f6-3922-a128-a6e6aa052495 | 1.43028 | -59.95105 | 2026-02-23 01:09:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5a9ac1ca-9128-3ab0-b8d9-a2409a0bf0eb | 2.8596 | -60.73561 | 2026-02-23 01:09:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e9e63b17-f5ca-3cf1-b105-146dff2a77b4 | 4.28899 | -60.79887 | 2026-02-23 01:09:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 051d603b-e825-3283-a4f9-7fad85c35554 | 4.09801 | -61.17815 | 2026-02-23 01:09:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9d3884bb-2942-3a9b-8dfd-03c3f573e779 | 2.7093 | -60.23411 | 2026-02-23 01:09:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 2c16d0a7-a980-3683-a312-a4fdbd3e8898 | 2.97121 | -60.26772 | 2026-02-23 01:09:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c5ab9a9d-4618-381d-a055-5d50b6d226f1 | 4.11501 | -61.18994 | 2026-02-23 01:09:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 83c0a755-4698-3cd3-8e08-aeeb8bebbb0f | 4.05942 | -61.12807 | 2026-02-23 01:09:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| af5de833-ee21-3513-b5ef-70f119050ebb | 4.17812 | -60.86619 | 2026-02-23 01:09:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8aa41f9a-1a76-3650-a526-016223068461 | 2.23934 | -60.69511 | 2026-02-23 01:09:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 14.8 |
| e49b8d86-35c7-3881-888e-f0d846d20dd4 | 3.20879 | -59.95277 | 2026-02-23 01:09:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e8f36fc3-ad00-3d77-ae7b-9092451de4f3 | 4.17683 | -60.87565 | 2026-02-23 01:09:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6c004112-08f6-3651-a043-9bbdb6723c7f | 2.0009 | -61.4283 | 2026-02-23 01:09:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| afe6956b-7aab-313e-8f6c-31e2fa060d2a | 2.83468 | -60.78114 | 2026-02-23 01:09:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e15741ed-b1bf-34e6-b74f-3af277a4b052 | 1.20526 | -59.96888 | 2026-02-23 01:09:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4b46bf2f-b636-320e-874d-3968c514c033 | 1.42889 | -59.96112 | 2026-02-23 01:09:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d0b912cd-6872-3b6c-9128-098ab8791938 | 4.16093 | -60.92277 | 2026-02-23 01:09:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5e3e62f5-754b-32f6-9e5a-b99350de7de9 | 2.96036 | -60.27658 | 2026-02-23 01:09:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 8e9b3f3a-4568-33fa-9ab4-cc263e25e487 | 2.95896 | -60.28677 | 2026-02-23 01:09:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 6ddc03c6-bebe-3c87-b117-54326b1f8298 | 3.94098 | -60.97842 | 2026-02-23 01:09:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 8269886a-a936-3b01-bebd-bc184d9e38e9 | 1.20852 | -60.61954 | 2026-02-23 01:09:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4a66152a-7164-3a8a-819d-1540c3a25723 | 4.29035 | -60.78899 | 2026-02-23 01:09:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 11.9 |
| b43ab828-0b92-31fe-8dd2-c7f33ff8d08b | 4.08887 | -61.17691 | 2026-02-23 01:09:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 10a2eeb3-2232-3539-af4d-e47008835d73 | 2.71525 | -60.23048 | 2026-02-23 01:09:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 245f1843-f945-3b32-a406-1ad2f13a85b3 | 2.32024 | -61.71049 | 2026-02-23 01:09:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| eda66075-53ef-3ad7-a78b-5b7093ffa9d3 | 4.09672 | -61.18764 | 2026-02-23 01:09:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 15.6 |
| a86305e5-b852-3097-8464-347c659beeaf | 1.2805 | -60.43571 | 2026-02-23 01:09:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0a005ec7-5128-3abc-9b36-c20631f84718 | 2.23016 | -60.69385 | 2026-02-23 01:09:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 33736ee8-c5df-321f-8223-5df2363a008b | 3.42274 | -59.90263 | 2026-02-23 01:09:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9bdf795b-c576-3b1a-83f6-78673c0bf798 | 2.71071 | -60.22398 | 2026-02-23 01:09:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 14d1b596-370b-3b0d-9be1-52e5c7c54c84 | 2.3126 | -61.70035 | 2026-02-23 01:09:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b0f76f93-ffb2-3931-b4cf-ebd9251f4f0b | 3.54053 | -60.88278 | 2026-02-23 01:09:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 754120c9-7cc4-380d-b9ca-f84b39099127 | 2.9698 | -60.2779 | 2026-02-23 01:09:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8163a22d-4230-35dd-b3a7-4a6c9643279c | 2.94953 | -60.28544 | 2026-02-23 01:09:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 23ebd36a-7108-3470-a0b8-e01dea0c078e | 4.11631 | -61.18045 | 2026-02-23 01:09:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 275c8496-4879-30a3-98b0-c8028f0eed2b | 2.22886 | -60.70337 | 2026-02-23 01:09:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 72be108a-c0c7-3ec6-a020-28c8bb3dd22a | 2.23804 | -60.70462 | 2026-02-23 01:09:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 4a744c88-13f6-380c-a7e7-dc4eff115abe | 4.0929 | -61.21573 | 2026-02-23 01:09:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0f5ae3ac-412c-3e94-b9d6-430bc0b2a634 | 4.07594 | -61.20373 | 2026-02-23 01:09:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 400efaee-682c-33bc-818b-cdfae71ac0e9 | 4.21962 | -60.13368 | 2026-02-23 01:09:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| dab7623a-ea87-3330-9a30-9d726e8a1394 | 4.08634 | -61.1956 | 2026-02-23 01:09:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fedc93c4-7146-36c9-9df4-99dfb459322a | 2.32148 | -61.70158 | 2026-02-23 01:09:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f2b505ae-0ce7-3f50-8a0a-78193f9d7447 | 4.16752 | -60.94342 | 2026-02-23 01:09:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bff701c6-8e16-359e-b6d0-e559b0e1d3de | 3.4213 | -59.91342 | 2026-02-23 01:09:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0e3af6b9-8d70-38c6-b434-7912af44ba56 | 2.00213 | -61.4193 | 2026-02-23 01:09:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ae9a7d20-206f-3fb0-96e2-30bbc1dabeee | 4.0876 | -61.18631 | 2026-02-23 01:09:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 1e4a3702-7441-3c88-982f-21de031e1561 | 1.8666 | -60.45221 | 2026-02-23 01:09:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9f0e8a78-b214-3bda-932b-995c369e7739 | 4.24132 | -60.93995 | 2026-02-23 01:09:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 435eed34-b375-3e19-8517-d72811b8e512 | 4.0952 | -61.1818 | 2026-02-23 01:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 23c5af46-525d-3e7e-9b4b-a197ca1ac015 | 4.0952 | -61.1818 | 2026-02-23 01:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 0f977d2c-0f4f-321b-9190-97ae7cb66ded | -10.1765 | -36.5121 | 2026-02-23 01:50:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 93.7 |
| 1d26594f-82cf-38a1-8aa8-429d5ed6ecfc | -9.66129 | -37.04007 | 2026-02-23 03:14:00 | NOAA-20 | JARAMATAIA | ALAGOAS | Brasil | 2703700 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c6c597f5-01e0-35e8-bea5-d77514e39b8c | -9.66071 | -37.0432 | 2026-02-23 03:14:00 | NOAA-20 | JARAMATAIA | ALAGOAS | Brasil | 2703700 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9f9c2cb6-2cd8-3dba-a8c1-7192bb3c7b98 | 3.3488 | -60.0386 | 2026-02-23 03:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 59.2 |
| b7ba9f78-43ed-3e76-8dd8-b52718f6be18 | 3.3488 | -60.0386 | 2026-02-23 03:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 3bdada1b-c675-3b1b-a944-d6e99712e7ab | 3.3487 | -60.0577 | 2026-02-23 03:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 627e706d-20b8-398d-9040-f73a4ee30155 | -9.9063 | -36.34177 | 2026-02-23 04:01:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 116d4314-f062-3612-a876-474b91ce8b6d | -5.82494 | -35.64803 | 2026-02-23 04:01:00 | NOAA-21 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e7e5bcdf-3e52-301b-be2c-f1dd3dd07b3b | -6.72319 | -38.54902 | 2026-02-23 04:01:00 | NOAA-21 | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bb1a5981-54b4-3aa4-897a-9e6e3821edad | -3.28477 | -40.60721 | 2026-02-23 04:01:00 | NOAA-21 | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cf1473e8-dea8-38af-9c5c-6cfcfe3152e3 | -4.6085 | -38.2845 | 2026-02-23 04:01:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8992a834-617b-3e19-8c5d-01abbcd7f7ae | -6.46976 | -38.41072 | 2026-02-23 04:01:00 | NOAA-21 | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 794fbe2c-22ea-34ef-b2f6-3235255661d2 | -9.66354 | -37.04145 | 2026-02-23 04:01:00 | NOAA-21 | JARAMATAIA | ALAGOAS | Brasil | 2703700 | 27 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 153c5473-f2ed-33e4-98c3-06cafbd6ab3a | -5.27726 | -37.67595 | 2026-02-23 04:01:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9f1c96a0-d0dc-3472-a059-4f976fd11869 | -10.60157 | -37.0242 | 2026-02-23 04:04:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4f999be5-84b7-3d8b-96d3-20c934e0b1ed | -30.37632 | -50.29507 | 2026-02-23 04:10:00 | NOAA-21 | PALMARES DO SUL | RIO GRANDE DO SUL | Brasil | 4313656 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| bcf1092a-684c-3de8-81ad-0b80a18e6d5c | -30.38002 | -50.29601 | 2026-02-23 04:10:00 | NOAA-21 | PALMARES DO SUL | RIO GRANDE DO SUL | Brasil | 4313656 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| e29340ac-f24a-34a5-a60a-6751352a201b | -3.28653 | -40.60909 | 2026-02-23 04:31:00 | NPP-375D | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ae4c375a-9d20-303c-a108-ef576c0db32c | -3.50147 | -48.04001 | 2026-02-23 04:31:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1f7d8f12-88c4-3ce3-8270-c379695245b5 | -6.03082 | -47.98575 | 2026-02-23 04:31:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 475a1555-3539-3548-b561-c818eafe71df | -3.49797 | -48.03947 | 2026-02-23 04:31:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fa937a23-effc-34c4-9fa1-a41dd4ee3d60 | -4.28554 | -48.25839 | 2026-02-23 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afb03cc2-5f98-3365-a484-a79dec9c3a02 | -13.66202 | -57.20774 | 2026-02-23 04:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.0 |
| 77205047-fdef-3e89-94f0-b59dd04e4284 | -30.3768 | -50.29389 | 2026-02-23 04:40:00 | NPP-375D | PALMARES DO SUL | RIO GRANDE DO SUL | Brasil | 4313656 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| fa740f1a-310b-3e81-b293-b2945c0846d1 | 4.20944 | -60.10942 | 2026-02-23 04:50:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fd364747-29c4-3a65-8899-6121b3649701 | 4.09733 | -61.21387 | 2026-02-23 04:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3bf06c6-19a8-3539-9e91-413e5fc32c98 | 4.09252 | -61.18119 | 2026-02-23 04:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f93fa4c2-f2e8-3a6a-b112-b5005275230a | 4.11533 | -59.88909 | 2026-02-23 04:50:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64ea7904-4a8a-3f81-82dd-ad6a85176ef4 | 4.09191 | -61.1771 | 2026-02-23 04:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4dbbf803-146c-3531-be79-a8c6dab4904c | 4.11487 | -59.88601 | 2026-02-23 04:50:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1bf7200-206d-3668-8034-bfb69aafa121 | 4.21426 | -60.10347 | 2026-02-23 04:50:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e9ecda7f-9303-31fa-870a-a46ab0008794 | 4.09319 | -61.18575 | 2026-02-23 04:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ec9004a-70cc-3354-9564-05c2d446d7c6 | 4.09667 | -61.20944 | 2026-02-23 04:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63101e5f-09af-3221-8635-dd9233673440 | 4.10988 | -59.89007 | 2026-02-23 04:50:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e69011ee-affd-39cf-9c51-f0cbebbc7877 | 4.21485 | -60.10756 | 2026-02-23 04:50:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dfa0f55c-cf00-354b-b4ed-f8026ff95a73 | 3.21649 | -59.94535 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 770ded0b-1907-36f3-ae63-e8c47c391050 | 1.86862 | -60.61977 | 2026-02-23 04:53:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12538af7-f7a3-3039-9039-f178bdd6d133 | 3.20175 | -59.95825 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a4c3376-13e9-3f34-bb35-24f4a7892a6e | 3.53308 | -60.89009 | 2026-02-23 04:53:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c5ae560-7c0e-338a-a26c-e3c838593059 | -3.49995 | -48.03553 | 2026-02-23 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README2.md)
