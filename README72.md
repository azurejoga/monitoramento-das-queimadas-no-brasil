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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b5de76d-3703-3629-9781-bb65d7a11bee | -1.52372 | -52.11309 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb2160e5-1504-3f0d-8998-474fc6d05ad9 | -1.52311 | -52.11698 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7aa2239-cc16-30b4-b68a-3b146b7f80a5 | -1.52251 | -52.12088 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67af5d6c-206f-3d70-80e7-9e728d1e17c0 | -1.52144 | -52.10476 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa82fd1e-4b52-3214-af7b-675f456083de | -1.50681 | -52.10653 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9a99a85-68fa-38a4-946f-b176a11c967a | -1.5062 | -52.11043 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a043817-7538-3ece-bedf-57042107164f | -1.4202 | -52.22797 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c1c252d2-0bb4-3841-bf0a-a17b26b15b45 | -1.41961 | -52.23182 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b73cee6c-4840-3979-beac-275462c9bc72 | -1.41713 | -52.21285 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bb2ea0eb-f1f9-321f-a58c-0b028942fd93 | -1.41546 | -52.20076 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 771ab631-a2d6-3134-a0cc-e6affab8b499 | -1.41425 | -52.20846 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e543d96b-fe60-366e-b8ff-f8c1f656826d | -1.41365 | -52.21231 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1cc59be7-79b5-358e-be88-5cb3a1ef46f3 | -1.41197 | -52.20023 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6dac7477-74d7-397e-943a-c32b4f836093 | -1.37951 | -52.17943 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c1eecd15-ac3f-3ab6-b0bd-4033b5deb08e | -1.37891 | -52.18329 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a33d2b11-4a99-37a4-8c03-c59ff117dee5 | -1.3376 | -52.19669 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c5c8f7c-c18f-3699-a487-65a3ff69ab67 | -1.91868 | -52.04608 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6565b95d-363b-3c00-923f-5bfcd1540807 | -1.90618 | -52.08064 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad5c8675-7692-3fdb-a056-b13586a6e92d | -1.80524 | -52.02942 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcb56ceb-e41a-3bc2-a133-b663c5cce2ee | -1.78288 | -52.03405 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27e88366-796d-36cf-9d42-7a789b260bbe | -1.7828 | -52.05825 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fad0f84-2216-39aa-ad75-85ace63ab703 | -1.68723 | -51.9962 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a83288ab-b052-314b-9aba-f0d0838e1909 | -1.63463 | -51.93644 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2455223-ce12-3143-8d61-b08ba6659fa5 | -1.60732 | -51.97287 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14c52491-092e-3fbc-9125-8a2a1bc290de | -1.6044 | -51.96837 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 08c9db68-4ce7-3d4b-a3c3-decac953dfb2 | -1.56828 | -52.03951 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 251fd6ea-70fa-3e7b-8da4-a35e99a7a156 | -1.56708 | -52.04736 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0fa904df-9513-3d7b-8d7a-79fa94a380ff | -1.56648 | -52.05129 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06329cac-4e29-3650-8a8d-2f77e23bfbd3 | -1.56356 | -52.04682 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d727b800-3f77-3918-86b7-5def4af65dd7 | -1.5599 | -52.09442 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c4f3e438-2b49-38b5-b644-60e9eb66cf89 | -1.55759 | -52.08604 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b31a5c5c-cb6b-3e56-9181-081787817440 | -1.55699 | -52.08995 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55defdbd-150c-34c2-8645-95ea11eff2e8 | -1.5564 | -52.09386 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d553a355-0423-3735-9e5f-ef0cb3da2291 | -1.55236 | -52.07321 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7dcfd2a-114b-3a31-89e6-ec33602879fd | -1.55148 | -52.07339 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 26478f61-cd60-390f-92e1-bc8a89fa3111 | -1.54944 | -52.06874 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2be02716-b04c-34a6-9398-0eda04f29c66 | -1.54885 | -52.07267 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| accd06e7-0bcd-3a87-aaf0-73194ca5b1e8 | -1.54859 | -52.06894 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c3f3f58-ede4-3773-8b7a-168ae39d773a | -1.54542 | -52.02024 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d9b8b94-40a4-37e6-afba-c9a88f4ee594 | -1.5448 | -52.02417 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 362b5624-2002-37cf-92ad-8ee78f25397a | -1.53548 | -52.01468 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53997801-751b-342e-b0c8-a42721422064 | -1.53196 | -52.01414 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e2df24f-68ab-31b1-b164-8a7ef450388c | -1.52844 | -52.0136 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba948826-6e4b-3f20-a504-48c5d7cccaed | -1.52798 | -51.99336 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4efbca05-cd31-3a8e-bdb0-ebd06cf70900 | -1.52321 | -51.90755 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 727fd2c2-0e0f-3944-91c8-b6868d41ae51 | -1.48853 | -52.01553 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36ccda6d-09df-365a-82d7-1dc721b421cc | -1.46845 | -52.0526 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b792db5f-13b1-34d9-86c0-b73c71122596 | -1.40095 | -52.08744 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8928896b-7d4d-3449-bf8d-46be78356b98 | -1.39757 | -52.06298 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f38169bc-1498-3f6a-ad21-57a95e20d8d3 | -1.37805 | -51.97967 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b29290a-1b25-333e-933e-3bd7ba228799 | -2.12248 | -52.70537 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbb86586-8815-335f-a5c6-c9ab9b2678ae | -2.10459 | -52.68732 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd4d7ce8-69b3-3655-9d20-e64015b46851 | -2.10401 | -52.69103 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 478cb796-d356-3d06-aceb-5f7d8557979b | -2.10136 | -52.27275 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6883d52-3b49-3a4f-9534-01fd9dee21c2 | -2.09965 | -52.26056 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 06349755-ffee-38d0-9b1e-b9532e8229e9 | -2.09838 | -52.29218 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0d42343-7daa-307e-97a6-678f90bda3c8 | -2.09317 | -52.27943 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1448d062-2425-3a69-b26b-29f53ef2e824 | -2.09265 | -52.25946 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5b07291c-0892-3226-a5ea-0d7798cb32c6 | -2.09205 | -52.26337 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2adcc5c-0299-3a69-be3b-76a169c5d830 | -2.0845 | -52.47516 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ef278b58-ad91-30c9-bed6-de6cc146272b | -2.06331 | -52.35806 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 670e691f-9ac6-31a5-bacd-9613495a86c3 | -2.03871 | -52.63491 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| acd051d9-eb91-382c-8c58-abb8d21e8a00 | -1.26359 | -51.947 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b675077-9a03-3197-8dad-38aaaec0a776 | -1.26007 | -51.94645 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f56fdb9-4fb9-35a1-abdb-460e30f356a6 | -1.22939 | -51.76818 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a452231b-c4fb-31c5-82ac-07945390762b | -1.22877 | -51.77219 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f3c9d9a-f510-30d0-9131-6e82b2cd6a65 | -1.22646 | -51.76363 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ff8f005b-c099-3f6a-8a29-7415105f49dd | -1.13419 | -52.15145 | 2024-11-02 05:04:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83a547a9-ea4e-3c07-b462-2e85778a7701 | -1.05864 | -53.16832 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e55d2eaa-12a1-3806-a1ff-49948020933a | -0.98548 | -52.98129 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9edefb70-6d80-3970-80a3-a9927b8b1eee | -0.98492 | -52.98489 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7574751d-7a6d-38ab-a688-2025a7b1a6af | -0.97275 | -51.78752 | 2024-11-02 05:04:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a2e39c6-f2ef-32b8-b265-d768f3b10cdc | -0.96983 | -51.78299 | 2024-11-02 05:04:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18bebcd8-547b-3022-91c9-5c4eca124afa | -0.96921 | -51.78697 | 2024-11-02 05:04:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76408c71-ec2a-39db-b2c2-8865a02e88d7 | -0.90616 | -51.65576 | 2024-11-02 05:04:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f6f3d32-9cc1-3575-9710-bd4185df9a2c | -0.88092 | -52.00372 | 2024-11-02 05:04:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8182515c-d5c6-314f-a01a-6e472e59aa29 | -0.87864 | -51.99541 | 2024-11-02 05:04:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4f86530-32d6-3cba-ab72-55c6ff418a1c | -0.87803 | -51.99931 | 2024-11-02 05:04:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5cfb5e1b-a2a0-324e-b6e2-d3d050d3c5d4 | -0.85967 | -52.83606 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44ac2a99-5a29-3cc9-be8c-37f19735ff05 | -0.85686 | -52.83188 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b874c3e-093a-3592-8e79-e1780a4f0e9c | -0.83758 | -52.19019 | 2024-11-02 05:04:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee36a266-18a5-3754-ae6a-014c54eedb26 | -0.75168 | -52.76411 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02618bd2-4afc-3fe8-9f2f-102d3a64ccd1 | -1.59392 | -53.20218 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a146882c-402d-33a0-842a-c561ced3b83a | -1.59205 | -53.20222 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fd159de7-c7fa-3d70-b37d-935f95796c49 | -1.58193 | -53.20075 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1968d7fe-6822-3c4d-b48a-347087d8bb8e | -1.86802 | -52.32985 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3cb7bb65-09ff-3aca-a432-5640d84aea59 | -1.86742 | -52.33372 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6dcfc984-94f9-3525-b6ca-00ae19a016ff | -1.86513 | -52.32545 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a0c49988-7e81-3755-92af-6883ab5dddac | -1.86454 | -52.32931 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aa68263e-f4eb-3e4e-b839-817abde59723 | -1.86394 | -52.33318 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c4350a87-2c6b-366b-b6f1-9500a8f43779 | -1.86164 | -52.32491 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee6bba75-9a71-3d1e-84a9-fb0c629706de | -1.86105 | -52.32877 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95f0a8e2-8c9a-3e1e-bb6b-d0e7cdfaf7ca | -1.85698 | -52.33209 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9de1f3a-adb3-3e5b-9e7e-48566ff58e79 | -1.82395 | -52.28015 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3fc6300d-ade0-3124-a84d-30422285b945 | -1.82335 | -52.284 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6cd477f5-e021-3087-a785-19732d9fceb0 | -1.82227 | -52.26802 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b6ad646e-a725-3e46-ac85-d51b7a2965dd | -1.82166 | -52.27189 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15011d09-e4fd-349e-bb32-4a3005816e31 | -1.82096 | -52.41327 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21ccb300-35a3-31a2-8c74-5af81d16c28b | -1.82046 | -52.27961 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72a96d7f-4baf-3d71-85f8-e17b3fda5748 | -1.81749 | -52.41273 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README73.md)
