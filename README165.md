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

## Dados Diários - Página 165

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f52679a-c44b-3c0c-b921-b170e211b2f6 | -2.88913 | -52.40405 | 2024-10-09 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 928a4643-5373-33ec-82fa-3a99721d7af2 | -2.88862 | -52.40044 | 2024-10-09 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e72154f-116b-3a26-b73c-9b6a7454bc08 | -2.87932 | -52.90536 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38854140-562f-3dee-b759-7b6176b788a7 | -2.87647 | -52.90107 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf84a796-86d4-3216-9f34-709d14abb5c0 | -2.87589 | -52.90481 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dda160f6-07b6-3eac-97bf-b2dd66293f64 | -2.87531 | -52.90855 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fe6ec47-dc28-33cd-9184-a953aaaf733f | -2.87473 | -52.91228 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d665ad3e-be4e-3f25-b05c-c3c012f34814 | -2.87246 | -52.90427 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17a5a136-c018-373c-b2d7-717c976a0555 | -2.86503 | -52.90689 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2be2b4d2-c1cd-35a0-a3d4-f9c6919fd88e | -2.86445 | -52.91063 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2a242af-6271-3241-9511-6ba02e6cee9c | -2.8536 | -53.31491 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1fa95e4-af4c-302e-a987-543ae8f3ae3f | -2.84626 | -53.31749 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 601ba993-5fe9-377a-b88d-526de227c922 | -2.8457 | -53.32111 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f027313f-5c48-3891-abd4-e2aed16e4a8b | -2.84288 | -53.31697 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9139db7-7e78-3af7-9303-e53da020b0fc | -2.84231 | -53.32059 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c11323b7-789a-3e66-9917-6e5144a565f9 | -2.84209 | -52.96431 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03ca8357-d06c-38eb-9e70-4708371b5185 | -2.84152 | -52.96801 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55863457-c552-3585-8751-4b3420249606 | -2.83924 | -52.96006 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09acf61b-fee4-33dc-810b-7daeae88905e | -2.83867 | -52.96376 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d48621bf-e4e0-3b3e-8142-6965030f420d | -2.8381 | -52.96745 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa76e9dd-9646-353e-be6f-c64f67a4431c | -2.83582 | -52.95951 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef435824-ec51-32d0-8203-270d2323293d | -2.83525 | -52.96321 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 669f740f-817f-306b-ad6c-77b5c289ee99 | -2.77621 | -53.21007 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85921cae-f147-3148-9bd6-aac287b44faa | -2.77282 | -53.20954 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e510bcd-ee7e-3dad-a42e-5079d1fa20fe | -2.77226 | -53.21317 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04b754f2-ec5c-30d3-a9e4-677c4d90824d | -2.73343 | -53.21068 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d21561d-cb14-3fa7-a5c8-4efb24ed852a | -3.90416 | -52.31546 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 391bcc36-4ea3-3680-bf6c-be418fe8e6bb | -3.90354 | -52.31954 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53ddb5d8-f007-3f52-88ee-829179b632d3 | -3.90086 | -52.38486 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d068cbd2-2105-39d8-837a-2f1f1334ad22 | -3.89724 | -52.4086 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6e2f84a0-276f-3f1c-989e-f25c0e130108 | -3.8846 | -53.53752 | 2024-10-09 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b3904d3-a8e6-3640-b2da-79539f02695b | -3.82884 | -52.40727 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6112661-c155-3368-bcae-5c2c251b70e6 | -3.82531 | -52.40669 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0a0fc22-08c6-3190-a41f-f51e5d55b3c4 | -3.79339 | -52.42612 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88b3da95-eb74-34db-a2c8-6b395e4116df | -3.78986 | -52.42558 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fb3e0a3-6716-3356-bf3d-7c1cdf98df1e | -3.74977 | -52.31002 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eaeb7753-75bb-349e-9fb2-f6de8c953e12 | -3.74915 | -52.31403 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70a8efea-3ea9-3036-805b-021f02e38823 | -3.74853 | -52.31801 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 10efaa40-7ba9-3abc-8c02-af1c6b2c3ed5 | -3.74561 | -52.31345 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a123ef9-46c2-30c7-894c-349aeba9d363 | -3.74144 | -52.31691 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9fe39196-74ea-3e6a-b53f-653608421beb | -3.61877 | -53.5154 | 2024-10-09 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d73c780c-b18b-3e39-af1a-6516ac903956 | -3.58323 | -53.26768 | 2024-10-09 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| c96b6f10-ffa3-30f3-b6ff-26991ec3197d | -6.09338 | -52.82741 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56d363dd-f370-3aba-a5d7-636c41abd0d6 | -6.09276 | -52.83153 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e3800c9-4f19-3320-88c7-2f704bca425c | -6.08983 | -52.8268 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92222cf3-062f-389c-bb80-bb47464dd634 | -5.86298 | -53.56578 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68a4f25d-eb2c-3feb-8559-d55efd33853a | -5.86241 | -53.56955 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe7ae9a9-31df-3a46-88cc-4cfdc76603b6 | -5.85996 | -53.56587 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9864b1b4-8d64-3285-bba5-f6eb7e33e076 | -5.85955 | -53.56527 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 522fb102-9305-3930-b4a9-8f3752f519b1 | -5.85938 | -53.56961 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f1a4eb9-83f4-3c53-b863-8923af54a009 | -5.85898 | -53.56902 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7bc8fe1-c6ba-38a2-b083-f590139169ef | -5.80163 | -53.39489 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 84e8d984-d0ac-3c2a-8be5-3fb3561ca29c | -5.79298 | -53.3586 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d207f08-f3d1-3623-afab-7b9c74794d23 | -5.78953 | -53.38136 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f06f531-25e1-3f6e-9b69-c1144de2c890 | -5.78896 | -53.38515 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0cf2288b-dbe3-3143-9015-f08666cd82f7 | -5.78895 | -53.36184 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7f0b7bf-3b82-3fd1-8810-0bb245c1b31b | -5.69019 | -53.75654 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 49b342f7-c774-33ae-b1f4-a5edd5f039ac | -5.68678 | -53.756 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d93023d-8416-3d1b-b8ff-388286d108f2 | -5.68394 | -53.75181 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72a6ee49-b204-3e8c-8c9d-0d196e21c507 | -5.64484 | -53.86996 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9972d7b-ef2a-3802-8fbd-21fbcf1ded15 | -5.62418 | -53.57242 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f21d6056-8f99-3606-bf97-d420ef3c8456 | -5.62361 | -53.57615 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c35c70f-3f33-306b-9e48-2955e7793d7c | -5.59892 | -53.73531 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55cdd038-be1e-3659-a01f-4ef199f79d38 | -5.59835 | -53.73898 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0163430d-058d-3e67-8f92-8e03851a5830 | -2.23544 | -53.65838 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62baeefc-6dea-3d14-a042-27e77b686b7a | -2.23265 | -53.65435 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f695f009-1a82-355a-9b47-e993f16d6e96 | -2.23209 | -53.65788 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ea7bd588-79e0-3448-9e15-85311f7d31b4 | -2.2293 | -53.65385 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b63d8750-f24f-30d5-9d4e-f73536b1f5f0 | -2.22875 | -53.65736 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 480626f4-2043-36e3-85bf-ec1f3d895184 | -2.03756 | -53.44654 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed0d2219-68b1-33be-9431-ccb65126e8e1 | -1.75958 | -53.54908 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9ceba7b-4cdb-302e-97ef-268428a99ca8 | -1.15939 | -53.7825 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5c5dd93-b388-34c1-95f3-b1a26cf1d0ef | -1.12816 | -53.6348 | 2024-10-09 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1459b4e-cc42-3b48-9593-083718249aad | -1.12428 | -53.63783 | 2024-10-09 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5f2bf1f-c6b3-3fe2-addf-5c2adb8caf21 | -1.12386 | -53.70559 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cc09535-0d48-3317-9c6b-9a6197761afc | -1.11758 | -53.61531 | 2024-10-09 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 061c000d-34ae-3054-a20f-40cf5acc7e42 | -1.11703 | -53.61883 | 2024-10-09 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 09c0a370-b622-326a-9d08-0ca12c4ee552 | -1.11648 | -53.62235 | 2024-10-09 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a475c528-c2dd-3592-83ac-a7940097a2e7 | -1.11425 | -53.61484 | 2024-10-09 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 0ceeda37-829a-3cd0-b6ac-31f673780a6f | -1.11369 | -53.61836 | 2024-10-09 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| c26e8e88-b224-382b-9e8c-3ca92fe2afb8 | -1.11314 | -53.62188 | 2024-10-09 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e1ff06b3-00d3-39bb-b64f-2886ca042c20 | -1.11092 | -53.61433 | 2024-10-09 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| ae7bf053-3a4c-3df8-923e-9f76840bdc97 | -1.11037 | -53.61784 | 2024-10-09 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 0c1a729d-6778-3f52-80c0-d1559fd75093 | -1.10982 | -53.62134 | 2024-10-09 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 39cdf4ba-14df-3dc3-9d7a-35360616d203 | -1.10704 | -53.61729 | 2024-10-09 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| a55ab264-32e3-3146-a7f0-0a0c823724ba | -1.03806 | -53.53853 | 2024-10-09 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ae40aa4-195d-35b0-958e-f58fe42c7f30 | -1.02894 | -53.72657 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1931d8fe-ee54-38ed-b750-3a69ce35b43b | -1.02839 | -53.73006 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecd200f3-c7e0-3964-b13e-28b690832094 | -1.02783 | -53.7336 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 758fa355-7dfd-392f-986e-9de1e49238bd | -1.02561 | -53.7261 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 560034ee-d380-35ff-9bd0-968e5ca2bf18 | -1.02506 | -53.72959 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cce83f41-85d3-3031-9a1d-3f31f50abffb | -1.02451 | -53.7331 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc7ea1c4-dd21-3edf-907d-5d6d651d036c | -1.02228 | -53.72563 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2ee6f83-4d66-3bd1-ac43-158dd9eb3593 | -1.02173 | -53.72911 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a35cf27-c738-3a3d-8d92-864abd0003ba | -1.74229 | -54.24773 | 2024-10-09 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d18d795-e7fc-3c1d-b3e1-fe719b07a237 | -1.58648 | -54.30828 | 2024-10-09 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c549863f-5ca4-368c-8012-a6ae078a6c5f | -1.26186 | -54.21155 | 2024-10-09 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8711bf75-212b-33cc-8fa0-792c52f19e6c | -1.19916 | -54.22286 | 2024-10-09 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d2a0bd97-29b2-30e4-bb29-f246d20e9d16 | -1.19586 | -54.22235 | 2024-10-09 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 977f33e6-76b0-3cc3-b1f2-050bb2e57765 | -1.17098 | -54.14158 | 2024-10-09 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README166.md)
