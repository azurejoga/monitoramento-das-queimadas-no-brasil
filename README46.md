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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6db1638d-b8d0-35d5-9502-5fc02fb0b435 | -1.71971 | -51.96661 | 2024-10-30 04:19:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1262b99-c039-35bf-9ecf-65ac507e2296 | -1.68379 | -52.72312 | 2024-10-30 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ff2b13f-fe39-3340-8953-66695ce47504 | -1.5824 | -53.10335 | 2024-10-30 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e36c9b49-30a4-3cc3-980c-0a8003609f1d | -1.5816 | -53.10316 | 2024-10-30 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ef48834-6dc0-3021-8a5d-c6a81a9961d2 | -1.58104 | -53.10673 | 2024-10-30 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8330630c-9a60-34d4-a176-9df1d101d33c | -1.58047 | -53.11031 | 2024-10-30 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af31e7b2-945d-30c4-9fff-d00fcf1aa8e4 | -1.57633 | -53.106 | 2024-10-30 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d90271d-f852-3bd4-80f0-ae8dbc7b7093 | -1.57574 | -53.10958 | 2024-10-30 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b064d5b-79cc-31fd-85ad-daedb98035cb | -1.57556 | -53.10579 | 2024-10-30 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc9ae43d-90e1-3215-b46d-8a7fb1dcd283 | -1.575 | -53.10936 | 2024-10-30 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08f780b5-a5a5-3da8-b5a2-ba5213ca3713 | -1.54363 | -52.12896 | 2024-10-30 04:19:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 14d5f17d-9c64-3367-9873-6ee1895b6857 | -1.54313 | -52.13202 | 2024-10-30 04:19:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9da03192-7a03-37fe-8e3f-111b10ee0a35 | -1.54263 | -52.13507 | 2024-10-30 04:19:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dff49357-f132-3ecf-9883-912b058516a7 | -1.53122 | -52.10825 | 2024-10-30 04:19:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 058bc3c7-debd-3380-ae06-6e40af556588 | -1.46526 | -52.3408 | 2024-10-30 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd3f6c15-b564-3451-9800-5631a2b6afef | -1.46457 | -52.31151 | 2024-10-30 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80450329-73d1-32b1-97f3-932887a4b5f1 | -1.45936 | -52.31068 | 2024-10-30 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5bafbd9e-55da-35f8-aa1a-8da2e7491a59 | -1.23315 | -51.76629 | 2024-10-30 04:19:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d856924-ef8b-3283-8072-062da7584e78 | -1.23269 | -51.76921 | 2024-10-30 04:19:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2e0c5b0-6981-3b36-acdf-c2347fbb0ba9 | -2.15189 | -52.3672 | 2024-10-30 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4d97814-aeb7-391f-ac8b-700b219b5279 | -2.15136 | -52.37037 | 2024-10-30 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b127c050-807a-3e5c-8a6e-67e8cf456422 | -1.97781 | -52.08246 | 2024-10-30 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30f82b34-86fe-37b9-948f-0ab831de6929 | -1.76669 | -52.31214 | 2024-10-30 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b4c254e-c301-345c-a802-650fa7b22226 | -1.74502 | -52.34725 | 2024-10-30 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 150b549d-5647-384b-95c4-436029aa8920 | -1.74451 | -52.3504 | 2024-10-30 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 697c40eb-e3d4-34df-9dce-8913749b9872 | -1.73982 | -52.34644 | 2024-10-30 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56e757b4-1290-3a08-be2b-46b4c753f858 | -1.73931 | -52.34958 | 2024-10-30 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5223ad01-cfa7-3bd7-82af-3dd7816d807b | -1.71924 | -51.96954 | 2024-10-30 04:19:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c83d203-27cb-39e8-ba32-0e711c9e6892 | -3.00055 | -53.4332 | 2024-10-30 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 958fdac4-8bbb-3fd4-b557-e80d5b04b602 | -2.9951 | -53.43212 | 2024-10-30 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 781988d9-85a7-3cd6-a62a-24c26b56c579 | -2.97729 | -52.85432 | 2024-10-30 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1884cc9e-a452-3153-b8bc-3081b2cd77c4 | -2.94858 | -52.56707 | 2024-10-30 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d4cd2d7-56ca-3d8a-aba5-334c5f90876a | -2.94339 | -52.56633 | 2024-10-30 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74c62e7a-703a-34a9-8413-ba6a6513b793 | -2.91185 | -52.59656 | 2024-10-30 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5edce332-7074-3393-bd9f-d62f7e83d401 | -2.86837 | -53.34425 | 2024-10-30 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4847048-2e47-3018-9be4-9c37516e7e2c | -2.86709 | -53.35187 | 2024-10-30 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5566c377-5495-340c-91fa-7301ced73fd8 | -2.86236 | -53.34663 | 2024-10-30 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65290300-8ea0-3280-9e6f-10b491efa683 | -2.85692 | -53.34561 | 2024-10-30 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| acca1b1c-b5ef-35c5-a718-b183516b21a6 | -2.78372 | -52.09352 | 2024-10-30 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9584e21f-3e67-3b91-8384-6082cd9a0b26 | -2.99993 | -53.43694 | 2024-10-30 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd2f7170-8d1d-350b-9a42-a053967bf52f | -2.99447 | -53.43589 | 2024-10-30 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f14502dd-a572-3650-bfe2-44b6c9edc92e | -2.86296 | -53.34302 | 2024-10-30 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d0a1f97-4fde-39b1-834b-9eacd058bb8e | -2.86168 | -53.35065 | 2024-10-30 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f4804f81-9098-3580-9738-104214f59fc7 | -3.6282 | -52.30506 | 2024-10-30 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac5a5e66-7714-3932-8ab1-b69ae2f5ff53 | -3.62773 | -52.30797 | 2024-10-30 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e9fba8b0-19d0-3868-a4b0-9bc7306e3c54 | -3.45067 | -52.86143 | 2024-10-30 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a73b4464-cc39-39bd-b25b-4b1ecbab150f | -3.4501 | -52.86477 | 2024-10-30 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0aab19ac-4e0a-327d-b6fb-bf4a4d8cad89 | -3.45009 | -52.86375 | 2024-10-30 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10ac0bf2-b096-3c01-a405-000c9796b5b2 | -3.44954 | -52.86714 | 2024-10-30 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be0a1f15-16c4-33ff-930c-a5aecfdc37a4 | -3.22639 | -52.18411 | 2024-10-30 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2526037-bd87-3529-9869-3baafa9b9bb4 | -3.22628 | -52.18546 | 2024-10-30 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37441011-ddd2-36eb-b91b-9a4dbe7e4078 | -3.22587 | -52.18717 | 2024-10-30 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02898b83-c6ad-3697-ad21-e45f5271a7b8 | -2.91235 | -52.59354 | 2024-10-30 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7e11f6a6-c34f-3970-88ac-e9aa9af5b38c | -2.91134 | -52.59963 | 2024-10-30 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 11885626-f279-310b-a889-131558580755 | -2.78327 | -52.09631 | 2024-10-30 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a31d157e-ac43-3d75-b1e4-c18d14ec2718 | -2.77871 | -52.09263 | 2024-10-30 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27dbf11b-fe39-378f-829a-693fb2f0a3ed | -2.77826 | -52.09537 | 2024-10-30 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34e6347e-77cf-37ed-9e00-a84165138acc | -4.25492 | -53.6282 | 2024-10-30 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1936fdc7-57ae-3ad2-a1f5-07fa05fafe12 | -4.25433 | -53.63168 | 2024-10-30 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 932c9445-4bef-32b6-bcec-4ed0738f130d | -2.24221 | -53.73182 | 2024-10-30 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2f9dcd46-a0ad-3201-8d10-e7973a79358b | -2.2372 | -53.72705 | 2024-10-30 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0c78d0c-1f87-368f-b3e7-fb5b1f881984 | -2.21668 | -53.67694 | 2024-10-30 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ffec156-204e-37ab-8db5-6afadc9f5eb3 | -2.19052 | -53.7109 | 2024-10-30 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5fd855f5-5e51-365c-bcec-db9d86fd2a95 | -2.16868 | -53.66758 | 2024-10-30 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5ac6c8f6-ba29-39d0-b83c-d2659f5e5feb | -2.16805 | -53.67142 | 2024-10-30 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9f4d61f6-2d99-32ba-a892-7d68b66f32f6 | -2.16302 | -53.66679 | 2024-10-30 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7508b377-282d-35e5-874a-2f9c41792fa3 | -2.16238 | -53.67066 | 2024-10-30 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 483343f2-fbd1-329b-a70c-bb6b9ca7dfec | -1.45825 | -54.06732 | 2024-10-30 04:19:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3177088c-05b2-31b8-9366-0c22a7fe6783 | -1.45757 | -54.07145 | 2024-10-30 04:19:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6fee55a2-c2bd-3532-8119-91b6a2f4acc5 | -1.45692 | -54.07541 | 2024-10-30 04:19:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aad0753b-ddbf-3438-9851-e1d464159930 | -1.43488 | -54.2098 | 2024-10-30 04:19:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36536ee4-264c-3773-b37c-aeb3e4f25eae | -1.42901 | -54.20862 | 2024-10-30 04:19:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 79984af0-53fc-3c17-8a3e-e6f74c2637ac | -1.41586 | -54.21481 | 2024-10-30 04:19:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a715fa05-0d0e-3df6-a981-26aad053b758 | -1.41519 | -54.21888 | 2024-10-30 04:19:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a84e520-8946-34af-b08b-e66d0e38e445 | -1.41452 | -54.2229 | 2024-10-30 04:19:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91d581cd-c504-3256-b49b-23add98b78af | -1.34391 | -54.64982 | 2024-10-30 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3af577ac-5351-37fe-ac8b-47db203c5d03 | -1.34316 | -54.65434 | 2024-10-30 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3039b349-d2ca-382b-aa5c-93c0d498c47a | -1.21862 | -53.38417 | 2024-10-30 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6e548558-e4b9-3e7e-a1c6-faca1ccc1a78 | -1.21507 | -53.384 | 2024-10-30 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42fe24e8-ab2b-390c-9724-a78c47a32120 | -1.16823 | -53.38861 | 2024-10-30 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65124b41-4ccc-35ae-bfca-f754ac60a3d3 | -1.16262 | -53.3876 | 2024-10-30 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac29a440-5f59-32c2-b283-70075f71cb8a | -1.162 | -53.39147 | 2024-10-30 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2564aa70-c622-3461-ba93-0fa812b3eaf1 | -1.15004 | -54.05593 | 2024-10-30 04:19:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e004956-4fdb-3366-93d4-9cbb8d7b0b06 | -1.14418 | -54.0549 | 2024-10-30 04:19:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a5411e79-ebde-3983-8c35-aa5bdbb8b98b | -1.09005 | -53.65602 | 2024-10-30 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1f76a0e6-7984-3c6a-9f52-b5fcef0f320f | -1.08439 | -53.65472 | 2024-10-30 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d8e11301-0351-36be-b69a-98122a90993a | -1.08375 | -53.65861 | 2024-10-30 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4f29e63d-cba1-35fe-88a9-25e24823063b | -1.0665 | -53.65625 | 2024-10-30 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5fb0d74c-f1ca-3e9a-bab1-793e782c9b46 | -1.06589 | -53.65998 | 2024-10-30 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf0ef065-0302-31d4-98e0-b0f15aa7ed86 | -1.06469 | -53.65724 | 2024-10-30 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b1f661f-08d2-3b71-bca9-2735c59635d8 | -1.06408 | -53.66108 | 2024-10-30 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b86d1d4-4dc5-3d8a-a521-bed8580e32a1 | -0.98638 | -53.7051 | 2024-10-30 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 645e884f-1088-3df5-9463-49e9295142f8 | -0.98578 | -53.70879 | 2024-10-30 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 678c150c-f7c3-3be5-a265-bbebb6e75a8b | -0.98 | -53.70799 | 2024-10-30 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0672505-eb69-3660-b2f1-e7a9d0db4882 | -0.9794 | -53.7117 | 2024-10-30 04:19:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54bad3fb-64c8-353a-9e27-55bb3c1aa192 | -2.24286 | -53.72798 | 2024-10-30 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 41c7db31-8a3c-30db-9758-c9cdcf90ed1b | -2.23785 | -53.72321 | 2024-10-30 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c13ab903-ea52-329a-a83a-ad7d821390a1 | -2.21733 | -53.67307 | 2024-10-30 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6244154-e6cd-3068-b70d-1e70f56c3a17 | -2.17497 | -53.66458 | 2024-10-30 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4af34e24-d78c-3436-b40e-7c488cab91be | -2.16366 | -53.66294 | 2024-10-30 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README47.md)
