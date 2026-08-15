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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 511f1274-9fea-3a87-839d-e9c26f8a777b | -13.75599 | -53.43225 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4af1fcb-879d-3993-8663-f5df04063452 | -14.49393 | -52.02781 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71c9e8a1-9e59-3b24-b432-0bf37cc94678 | -14.48418 | -53.08579 | 2026-08-15 05:36:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0bd5bd9-794b-33b7-8c41-29f009926bd9 | -11.50903 | -54.63893 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab78d1d1-21f3-364c-9b80-3d5906bce3d6 | -14.11055 | -53.70833 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8daa5d39-6eaf-351c-a96b-190434cd3c56 | -11.48534 | -54.61929 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44eaa164-3f1a-3a22-8e09-48daf75f536b | -14.41858 | -51.91254 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 28679ae1-9c68-3511-83e6-079423e5f557 | -13.80764 | -53.79475 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76cf0ed2-21d1-32a7-b0c0-a8d1302b6e5e | -14.74976 | -48.24778 | 2026-08-15 05:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5a1e449d-c8d9-35f5-87f1-4c2e5d2fd5d2 | -13.75152 | -53.42525 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a31154bb-5fc3-3857-9971-c1bf6fcbae65 | -8.89387 | -60.55658 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| fb724e50-679b-3fd0-9f47-6a613970a4ff | -10.49323 | -50.15678 | 2026-08-15 05:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5639006-5eb8-3ebb-a6a7-c152ccda1cd3 | -11.98326 | -53.45355 | 2026-08-15 05:36:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6b6f2e0-35fb-38f7-b756-6df6c5dcaf5c | -13.80843 | -53.78828 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f175a5d3-7260-345c-b68b-c601046cf2da | -15.03921 | -52.69405 | 2026-08-15 05:36:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc582408-bf8a-3269-b6c9-a573200ae192 | -12.35324 | -51.20965 | 2026-08-15 05:36:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 88fb110c-f89b-3942-a53c-af58d7f848ad | -9.58564 | -60.5063 | 2026-08-15 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d40993a7-2273-3802-8151-b94b9aa8b562 | -8.64918 | -54.69175 | 2026-08-15 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae2153ae-dcec-351a-9373-731018828b7b | -14.43514 | -51.92316 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f1e24ad-3370-3098-8475-908a83a30731 | -8.61299 | -54.67513 | 2026-08-15 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3044819f-41af-3b14-8e77-d105b0dd2e63 | -14.4198 | -51.90683 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba8303f7-5438-3213-b0b9-f99e071de65f | -8.9646 | -60.5135 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 075edbc8-7435-3359-9879-161105259614 | -11.49002 | -54.61991 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67e7fdc1-611a-3293-a8e7-f2f290de990e | -10.48702 | -50.15596 | 2026-08-15 05:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d1bfb0a-b387-378c-8761-dd68c367c732 | -13.26 | -54.19501 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6529b316-0b78-315a-b98e-0aa4b943a3f9 | -14.44681 | -51.92463 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc4b8111-fd7a-353e-bea2-2cfe7a239cfe | -9.19168 | -60.2914 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5dd4eef9-ecf7-3183-81f4-9c5a5b017ca2 | -13.4208 | -57.05408 | 2026-08-15 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3410f918-1d67-388c-aaf8-2666529cc305 | -8.76352 | -63.75221 | 2026-08-15 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ad8974dc-56f9-3f8c-a48e-2a3ac108e948 | -8.96236 | -60.50591 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b37e9a6-6559-3076-802f-33053ed728df | -11.59582 | -54.66635 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e594d38-cae4-353f-973f-ce9964f85662 | -14.44397 | -51.94981 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 070fd0d5-4f82-348a-a878-f6bc474f2bb7 | -11.50607 | -54.64199 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa580aca-06fc-36ff-8c85-3a3d0abee56a | -14.43846 | -51.89361 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c0469499-bc1f-380c-b93d-eca4f5be5b82 | -14.30333 | -53.07144 | 2026-08-15 05:36:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0d513f3-908b-368b-8e06-0b44f8d5f765 | -14.44192 | -51.91548 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8b06ee23-3a5e-3f26-9c7f-989d718a05ab | -13.91438 | -53.95601 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd6569f3-9b0c-339d-a32c-94ce390d91aa | -8.78442 | -63.97644 | 2026-08-15 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf4db2ba-07e8-3058-af44-6d809b6dc916 | -8.9713 | -60.53622 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 488ba37f-62a9-36fe-b372-fce5b73f5dfc | -14.42441 | -51.91329 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 35d29286-86a8-3f44-9ef1-7a51b4556361 | -14.09937 | -53.62534 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c6b8e554-e545-3406-8a6e-e5bbabcfbe94 | -13.24242 | -54.17527 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7f60c07d-6620-3b2a-b957-d8d6f06738da | -8.60661 | -54.68772 | 2026-08-15 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 75bc5ce0-bd97-3cab-91d5-1cf1ced7ba37 | -8.96071 | -60.51649 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 49951885-ce4b-369d-a40f-1cd378fb3f1a | -12.13512 | -57.20744 | 2026-08-15 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 650c53f7-46bd-3f6b-bc83-4d7c2bf8d655 | -10.48886 | -50.15794 | 2026-08-15 05:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ba7197cd-e369-3a93-9d6b-a84421914298 | -14.4342 | -51.93155 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7285a08b-ff80-3291-9eb8-eb02bcf8bdca | -14.1038 | -53.62937 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 194937ce-ce50-369f-93d8-e588be1264a9 | -9.47411 | -60.50652 | 2026-08-15 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e1e8158-cc48-354e-9b45-632959a39090 | -11.5885 | -54.68529 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5e5ebd63-ec52-36ca-8549-914a80bf0629 | -11.21141 | -54.81887 | 2026-08-15 05:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0b37a30-2c08-3f09-b1be-2fcd2b3922b3 | -13.42947 | -57.0517 | 2026-08-15 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 787859fa-f926-35ec-b8d8-9352fe1c1f39 | -11.59116 | -54.66563 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2991feff-aa2a-31dc-9c32-1eaf2c54c288 | -14.44872 | -51.90775 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f358340-caa7-3e5c-b5be-9d0a24d6ecfd | -13.2417 | -54.18093 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4f7eb26c-25d2-30e5-b543-de05f5ae2347 | -13.92018 | -53.95077 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a3a0c6d-e5da-3477-9011-a3793d69b1cc | -13.27064 | -54.19051 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd19f74d-0982-3a91-ae86-6871db13dc64 | -14.3091 | -53.06907 | 2026-08-15 05:36:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a09d41c-712e-33e1-b7bf-67958d01197b | -14.42978 | -51.91822 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5d79078f-ab4d-3114-8551-c1036d098523 | -8.97908 | -60.53024 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b26db481-a428-30d9-86b6-dd8855608eae | -10.39981 | -47.97274 | 2026-08-15 05:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dde074e3-3e0b-3e2f-afd5-d7ee50b33627 | -14.41396 | -51.90612 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30b7e360-dd2d-3d88-a510-e007383590d0 | -12.6919 | -48.45591 | 2026-08-15 05:36:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d73e702f-0f2d-39fd-b34e-44c7f570a708 | -12.6926 | -48.44931 | 2026-08-15 05:36:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f4a80e91-40a8-39c1-a6e9-36e4594c933a | -9.58285 | -60.50222 | 2026-08-15 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c611d3a-ae0a-389c-90b8-2aaf969c1945 | -15.1559 | -50.05754 | 2026-08-15 05:36:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 527b2fad-b474-37ce-a8c7-ddc24559f79e | -14.49237 | -52.03606 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d685baf-63d4-319b-a505-c959aa213bee | -8.95404 | -60.51543 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56190122-eff0-39a2-9334-5498b9e82312 | -14.43148 | -51.84976 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4ad3e2f-1ffb-30ac-8e9d-2d1c8b1a5b5a | -13.24099 | -54.18652 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ea4451b-5a80-3a4e-9ba4-b43bc4345d8c | -14.49283 | -52.03193 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc86e4a7-cdeb-3b11-977c-e2fa0a5b0fb8 | -14.09416 | -53.62475 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 259c4a30-e8eb-3899-88a6-f0b393b7aad9 | -8.98575 | -60.5313 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3550fe08-9c8b-3397-8184-8072992dc62b | -7.58434 | -61.22378 | 2026-08-15 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e45afd0-ec44-397a-a161-ced3fc474bed | -11.49738 | -54.63589 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9a4a657-654f-3ca5-ab21-45d69ad7710a | -9.70839 | -69.0666 | 2026-08-15 05:36:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a79e0b7-21b8-3b97-8788-562ec31ed4c9 | -14.43861 | -51.9449 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52b1baee-f04f-3c12-a5aa-d754335c948f | -8.26342 | -57.34821 | 2026-08-15 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 670d492b-9167-370f-a664-b12f6127ae29 | -14.43356 | -51.88437 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| adbedfe1-cfd7-373d-83c8-fea005a5480d | -8.96405 | -60.51702 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ac59081-717a-33af-a265-8b79f96e4c0c | -11.50562 | -54.62845 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80f80222-6408-321a-ba53-bde41b6b2e8c | -14.4424 | -51.91126 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5c6fbf80-7cea-3a44-858e-eb26652140a0 | -13.75676 | -53.42599 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3379a39-b93a-33b4-9ac9-d460f2ba7cc9 | -12.13743 | -57.20645 | 2026-08-15 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1be63750-d12a-38b4-bba1-335f64c238bf | -9.19503 | -60.29193 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 350e3688-3b6c-3d12-9ad4-9250437c103f | -14.41446 | -51.90191 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a6e201d-76f5-3ae1-b731-202dd0b34693 | -9.19559 | -60.28836 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c899c51-925d-3be9-85d2-7c4c06093225 | -14.43119 | -51.90559 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 352230de-9d36-3e52-8f48-fe33a2c9976d | -11.98636 | -53.45217 | 2026-08-15 05:36:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 154b9fbb-841f-3623-9d29-c4fde2a3dd19 | -14.43261 | -51.89289 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| db822136-dace-3734-9c40-843f2b4e4f8a | -11.48935 | -54.62483 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f8ddf9aa-8f91-3b4d-a81c-197fbbf43f30 | -11.48601 | -54.6143 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9934914-7ce7-3cdb-be7f-7d096cd77635 | -11.5034 | -54.62666 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34ca11df-00bf-3f29-9658-b818b1ccc0ee | -13.23748 | -54.17455 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd3346ce-869e-3cbb-8f06-75dfc50141ba | -12.69408 | -48.4571 | 2026-08-15 05:36:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ed602a9a-6258-3764-b590-e5438b273d25 | -14.09352 | -54.52221 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6bf1720a-933d-3ddc-b13c-86430f63e26a | -8.60343 | -54.67823 | 2026-08-15 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f46f91fe-ec45-3373-a7fb-654813091986 | -13.914 | -53.95902 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44c7fc12-b3d5-3ba6-8fe9-f566274f901f | -13.23677 | -54.18018 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4bbc0b87-a602-3fe3-82d7-f6f89ac54e2b | -14.07575 | -53.60021 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README41.md)
