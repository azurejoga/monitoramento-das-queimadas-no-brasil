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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eded643a-8562-3d4d-8b4a-fc54e44bc18f | -9.5575 | -50.21665 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 54da5d5a-84d3-3d9a-afa2-4f6bab31837f | -9.49619 | -50.19745 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c3a350b-426d-3347-82c8-1ab80d912ffa | -9.49573 | -50.20016 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 095a0f78-e705-3d04-809f-aad6c613d597 | -9.49549 | -50.20247 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62ae8156-c602-3d86-8b4f-22f3686007fd | -9.36006 | -50.28006 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5728408f-e482-3b61-bfaf-a441b50da48c | -10.52236 | -49.1265 | 2024-10-04 04:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 74a5b49e-673e-31cd-8421-7d4512aac56e | -9.62878 | -50.11341 | 2024-10-04 04:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 825977df-a8a7-3f07-954c-12599da55796 | -9.59546 | -50.09295 | 2024-10-04 04:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2de13952-3663-3715-9855-5affe8d48808 | -9.59941 | -50.17648 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25e118cc-5414-3975-bbd8-6c76644c5784 | -9.59621 | -50.17086 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be52c582-eff9-3e4a-82cb-d65c30aa2101 | -9.59547 | -50.17591 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6d011303-8bb1-3c1b-90b2-b06bece959b1 | -9.59474 | -50.18097 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 57608f69-6d12-327e-ab4f-f842284531e9 | -9.59228 | -50.1703 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4fac1b2-092c-397f-87aa-4d9a8578976c | -9.59154 | -50.17535 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f164cf93-379a-39ed-be20-c196f6ea5a42 | -9.59007 | -50.18546 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0ae7ac1-a1b9-3aad-b369-753a698ac2a9 | -9.58761 | -50.17479 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4f7d4b0-6917-34e7-be43-07c20db1f2aa | -9.58614 | -50.18488 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc027f8e-2d92-3600-80a1-0d851d322435 | -9.58221 | -50.18431 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0fc3d1d2-c431-35af-a176-ec47078ac4d6 | -9.57901 | -50.17869 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7b94ff4d-059d-3ade-b5d8-581648e11321 | -9.57755 | -50.18879 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3ea39055-d56d-30b8-abb6-e2a47a00c25d | -9.57637 | -50.22454 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2fc7e2dd-dddb-368b-9f11-2ff2a8bf7616 | -9.57245 | -50.22397 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 51c2887e-a07a-38ce-85ca-014929b291f7 | -9.57172 | -50.229 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2f853bfa-eb40-33e6-9661-5dd66ec83dc8 | -9.56853 | -50.2234 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1da108ea-73b1-3c61-bb95-ba5f037edda6 | -9.56534 | -50.21779 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31fc52c6-0a3f-3474-94ab-a15e2a840ab5 | -9.56462 | -50.22281 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ef88de3-2b36-3706-af47-9706e8bc2614 | -9.55678 | -50.22166 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 398b823e-3faf-34d5-a6fa-0c83524a751b | -9.55358 | -50.21608 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 63352ab0-8cf8-32cc-bfda-0ec32f9dda90 | -9.55286 | -50.22109 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e276278d-6308-37b2-8f29-2bf5706849c4 | -9.54574 | -50.21494 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f96ae9bc-9cce-3120-89b8-2bed3cfcf4f4 | -9.54254 | -50.20935 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84bd2d0d-012b-3bcf-8c57-9f609c173caa | -3.5653 | -49.44867 | 2024-10-04 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9085be3b-219c-34a6-9d28-ed85e963a130 | -3.56151 | -49.44809 | 2024-10-04 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdb515f6-121d-3613-872e-dd93c75ce689 | -3.31289 | -50.45041 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3bc8b6ca-1ddf-388b-921b-a6d4166fafe2 | -3.31227 | -50.45449 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e9b89c1-84e4-32a9-b0bc-4c0045d36a29 | -3.30932 | -50.44984 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc8f39fd-7b7b-3ace-af38-645efe88586e | -3.3087 | -50.45391 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59c49a8c-228a-3da3-94e0-e053835bc2a9 | -3.30808 | -50.45795 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ad14b83-7753-390e-a473-65ad4de53e0e | -3.30747 | -50.46198 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93c737a7-40e9-3f0b-8432-d62c7f25e643 | -3.30574 | -50.44928 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f7d38a68-14b2-3eb1-9149-8ce7d1fedb30 | -3.30513 | -50.45333 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| a1d7441f-c685-3b87-9cfa-3375f898df62 | -3.3039 | -50.46143 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 138.9 |
| 67b27877-8fee-3c2d-8ec9-7e158962ffac | -3.30328 | -50.4655 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc2362e4-cd9a-3d91-aae4-60cd7780b111 | -3.30217 | -50.44872 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 911ddd88-9520-3a24-aa1b-db1f3cff796e | -3.30155 | -50.45278 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 7a724c1f-0d4e-31f9-a025-d2566b09da99 | -3.30094 | -50.45683 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 138.9 |
| f6754d33-01fc-3ad1-89fc-617c3cc99166 | -3.30032 | -50.46087 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 138.9 |
| 0165ec82-be43-3247-a624-681d9c47babc | -3.29971 | -50.46494 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32e1895d-438d-3021-87ee-134c6744025b | -3.2986 | -50.44815 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3ca39b1b-fd9d-3c59-a73d-5641f78994e6 | -3.29798 | -50.45224 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 226b11c7-0205-3979-8bcc-32c5659285dc | -3.29736 | -50.4563 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 0ae67674-1ca5-34e5-8f08-668acbb29068 | -3.29675 | -50.46033 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 917c0e87-5a96-3247-a998-08db15bde3d6 | -3.29502 | -50.44759 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8b3c7a44-eb44-3709-ad8a-93214d58e323 | -3.2944 | -50.45169 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ad64e51d-12ad-3ad2-8873-d554bddaa895 | -3.29379 | -50.45576 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 8a2635f2-5845-374e-8e82-6230907a03d2 | -3.29317 | -50.45981 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| d112e629-281a-3e0a-a525-456439d1dfff | -3.2926 | -50.44838 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| adcfb04f-31f9-3f3b-b653-f6edad6ec2de | -3.29196 | -50.45247 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 678d11d3-bf11-3671-9cc7-7c4c2fead6fd | -3.29145 | -50.44704 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 09910d87-e3ef-3c74-be79-e292cdab9e49 | -3.29132 | -50.45653 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 49cd2dbe-c1de-3403-8f84-c466a632b4da | -3.29083 | -50.45114 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| fbc549c9-d8f8-3987-8323-ce17bb01f202 | -3.29068 | -50.46058 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 4e61599c-df07-3f13-b275-46027d4e4fac | -3.29021 | -50.45522 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| ad26523a-6652-3e4a-9353-51193ca86652 | -3.2896 | -50.45928 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| e24500af-9e39-36cb-9d5c-03582994d9a7 | -3.28903 | -50.44783 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| d2e9f62e-ffb7-3aa7-8198-7a1e5edfc1fc | -3.28838 | -50.45192 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 612a0828-3c7d-3573-a707-3f74256ba3e1 | -3.28787 | -50.4465 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 2636e3d3-2e6b-3f26-a068-efc21feb01c3 | -3.28774 | -50.45599 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| ed294e9f-b2cd-34d9-90b5-448d44c5483e | -3.28726 | -50.45059 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 609b845c-49be-3b6c-a64f-d5d8a2160be3 | -3.28711 | -50.46006 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 1587a1ff-8332-300b-9e0e-4616d01c47f4 | -3.28664 | -50.45468 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 9a1da5c9-665d-3701-849d-9bedaee92fb7 | -3.28602 | -50.45874 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| db2fbd11-8898-32db-bb2b-392677318d43 | -3.28481 | -50.45138 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa4aa493-f3f0-3a1e-b23c-927b56526e8c | -3.28417 | -50.45547 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3c6f838-71df-3699-b3a9-9cd284ca99ad | -3.24701 | -50.48291 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e69445b8-49f3-300e-b9bc-35a5d0446d8f | -3.11088 | -50.47203 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4797112d-1fc7-36c8-ae37-d118f822eaf8 | -3.11026 | -50.47604 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b58daea1-cf05-390d-baa9-b013ca72c486 | -3.10731 | -50.47149 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a57159bb-e925-342c-ae4a-7d31fbf00f98 | -3.1067 | -50.47549 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b2f19237-d9f2-364e-aa6a-031fa676b52c | -3.10437 | -50.46688 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80caf93e-b4a8-3a61-9931-228996544bde | -3.10375 | -50.47094 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a155fa65-d001-34fc-ac38-bf7e35c14ff3 | -3.03811 | -50.45372 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e0c90df-3af5-3a53-b8f0-ead9711d4423 | -3.03454 | -50.45318 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a6074a4-c831-3238-89c9-9f0d3a8e804f | -3.27087 | -49.11392 | 2024-10-04 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bfe9f10f-9b5b-3aee-9cba-db4dfddc62f2 | -3.2694 | -49.11147 | 2024-10-04 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d0d7af1-7842-3156-8fbb-e28c7e31ffa1 | -3.26555 | -49.11088 | 2024-10-04 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af40b90a-0da8-39e9-a5ee-552b6d91662c | -3.41387 | -50.33062 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d26b34ed-4b4c-31ad-aacb-d0e9b2d6bb98 | -3.41206 | -50.33127 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1d9374e-2f41-316c-ab88-c45ca85848de | -3.32133 | -50.07487 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 39a04e96-517e-3b67-a860-086075c83f75 | -3.31769 | -50.07431 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a51b0eed-cdea-309a-ac06-ce176c05a93c | -3.28642 | -49.52509 | 2024-10-04 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04583e9c-bee4-3cf1-8a7f-85aba4029fb9 | -3.28573 | -49.52958 | 2024-10-04 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fe699adb-9bbb-34f3-90aa-04d89c01d046 | -3.25677 | -49.44173 | 2024-10-04 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 73814e5a-59c4-3234-8efd-def79ef75c57 | -3.25659 | -50.10833 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d89ac9a-0324-3b49-a4c1-0b294c310467 | -3.2551 | -50.14256 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8a6722ed-17ec-3025-a171-4f7fc5afa282 | -3.2536 | -50.10354 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2b88ecd-018d-313e-8d36-be9b012b260b | -3.25295 | -50.10777 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d28b8e5d-c8ff-351e-aa94-9eb5494704d5 | -3.25211 | -50.13779 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ece142f-de64-389b-b270-cb15b128bbde | -3.25147 | -50.14201 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e8dffb1-508e-323d-9f4c-a4848fd563bd | -3.24784 | -50.14145 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README144.md)
