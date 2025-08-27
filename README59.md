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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bfc98822-dc6a-319a-b3b5-036c8c6e031c | -8.92798 | -65.91969 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 68c315a8-3e1a-3502-9438-cfb8daf8a74d | -8.58126 | -63.91849 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f542ea3-f1bd-3196-867f-062a38f4c895 | -9.28283 | -56.90891 | 2025-08-27 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2f22763-28aa-3c4d-b581-3407850c4e02 | -9.16935 | -60.76886 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 58c1f30f-0b49-31cd-9563-77ebccc79347 | -5.4561 | -60.1538 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29004890-e542-3a5c-8148-4c618d334647 | -9.17062 | -59.46149 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 857badae-476f-3867-82f1-ea9053c10cb8 | -9.27407 | -59.78114 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9057da65-0258-3991-97ed-320508d1eb81 | -7.41681 | -60.61868 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bfaca20-0a80-3b44-9910-cfbf25c522f5 | -9.52632 | -60.51191 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 603ac53f-27a5-3871-a240-a6cf523b1bee | -7.5641 | -47.48888 | 2025-08-27 05:18:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 12cc8363-7a2c-3ba3-8332-5da5e6336d51 | -9.40239 | -62.48519 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19fb76b8-026c-3870-bb39-686644ed9d14 | -6.78126 | -59.66786 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 691c7aee-08bd-3e4a-840d-1e1fd134c25a | -6.7004 | -58.55221 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f99d036-2ef4-3d5c-a4ec-892e0aa6d485 | -9.41964 | -60.5416 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39deaa18-e75e-3937-9da9-484e9b3b8be2 | -6.81323 | -58.96385 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f804f0a5-3b46-3142-94e6-02a7b06276cc | -9.06618 | -66.05996 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e3dd21ad-8e35-3a57-bfb6-76393efcc9d8 | -10.49583 | -51.59488 | 2025-08-27 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38785744-9804-3b79-b10f-e94d5e7d80fd | -9.1942 | -60.80195 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| a3bc933f-152a-3e25-9097-966405b75494 | -7.47667 | -61.34248 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 443ad9f8-d28b-343d-82e0-73e65cb313a3 | -9.17926 | -59.51696 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afaef0b6-a724-30bc-9fbe-ae611c52785c | -9.01979 | -65.69386 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2fc1105-fa0d-36ff-8cae-4e6dc6831b77 | -9.41468 | -60.50839 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 91bf70f8-60f5-354f-9e21-ebaed1f249ab | -9.26567 | -56.90207 | 2025-08-27 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afba3149-fe33-3110-86a4-bc4c1f70301f | -8.33953 | -62.94402 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f04e361-280b-3892-be8b-3811a4e4c750 | -6.25598 | -60.01989 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4148bf16-49c8-3bf8-aa24-fac5f11111ec | -9.16669 | -59.55413 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| cc5a427d-4cc9-333a-9fa0-4891dbb8cfb8 | -6.941 | -59.64671 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2dfefe2b-fc8c-396a-84d4-4aefd51af79d | -9.57217 | -55.37976 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8631a3c1-432f-33e0-b68a-5f9f04d65a4b | -8.95472 | -65.94597 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6e2fbc7e-e0b6-3512-a6bf-04f9021f4708 | -9.19665 | -59.64436 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be4992c3-8dd4-3235-96c4-d07d2efe2bdf | -10.76898 | -60.78585 | 2025-08-27 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef0fbd2f-5b96-30f1-add7-a30d4172d3fe | -5.42648 | -60.16737 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a501c5a2-617f-3ea1-9d28-79052a1503fa | -7.44147 | -60.03329 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efb6a73a-08a4-328f-a66b-7de327b8cdbd | -9.39887 | -62.48461 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f93ce55c-2d8d-3d72-ad06-36fb4a823b08 | -7.58995 | -61.18187 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55d2c103-4a34-384f-a2a1-670409e7601c | -8.89073 | -60.76383 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cbfab639-eae1-347e-8c61-07c3880a4aa8 | -8.93231 | -65.92045 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 682feb28-32a7-32d6-ad43-401676c217da | -8.92291 | -65.92316 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c46b15ec-924f-351c-9e1d-70e177dba502 | -6.71265 | -58.56123 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e2023fd-2525-369d-9343-9449f4b1ffd7 | -8.56693 | -63.89412 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d09e569a-ffed-3a6c-880d-982821707b2a | -8.23766 | -61.45941 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 638b5a3c-230b-3f9f-861e-200f5d20d40e | -7.35362 | -59.66264 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f43f1650-ec2b-3e91-96e9-934ab1ae0dbb | -9.27217 | -56.90727 | 2025-08-27 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a36a6e62-1dde-358b-b67c-5a6fa15ab5ee | -6.69099 | -58.54717 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c05f9dc-c69d-3538-a1c9-3fd769e9ce45 | -7.0532 | -59.8215 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7a562c5-c84a-3176-a8b3-b7529fd2d341 | -8.95979 | -65.9686 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 4365a646-34c5-313a-a501-db32c5f35568 | -5.45275 | -60.15327 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4ed1940-2b80-3f44-ab53-53c67de2a02e | -9.17325 | -60.76585 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89281de7-055e-3ce4-94f9-cdebe0321b0d | -8.34024 | -62.93974 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2fc6ad65-afa3-33d7-9767-58856c40ae8c | -9.08707 | -65.72997 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 78ad38f8-21d8-3c5f-a9f0-1fa4e4dcecfb | -9.61171 | -57.37847 | 2025-08-27 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3afc2d1c-4f8d-3035-a218-98d9bb968548 | -6.7027 | -58.55968 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce655c45-9a1c-38ef-99cd-58eeea9131fa | -6.56711 | -60.05503 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff3fe854-6768-3cac-9457-4f21e50b1e9d | -8.25072 | -61.46535 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 790e3106-55b2-3b90-b624-ff15880d6030 | -6.64846 | -59.08327 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74a41493-1587-3af7-ad51-b1acf6ebb4ca | -8.88348 | -60.76631 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b0426b0-0591-32a4-9d00-ccbc3e2c5d8e | -9.17269 | -60.76939 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16b308ac-a749-304f-a721-4e951cab97ee | -9.15737 | -59.57048 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 53a7b1a4-7d70-318f-a755-5a6d516383c3 | -9.16338 | -59.55361 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 66641c1e-e015-30ef-9e97-84fa2d0d62ed | -6.81654 | -58.96437 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 04ecabee-7c22-3e08-a76b-e36f31ba3564 | -8.99828 | -65.41318 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77af45a8-e65b-3fc7-b6d1-a1a075d5b85a | -9.1784 | -60.85774 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf270f64-1974-3965-ad10-6c9536ccae00 | -10.76864 | -47.03374 | 2025-08-27 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83b34365-8f13-3547-af3b-89c178850109 | -10.08995 | -62.89576 | 2025-08-27 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 85b797a5-f947-3ccb-9002-e674622c9663 | -6.23421 | -60.00915 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d85ea9d-ae06-3807-8f1d-a7ae571a01f4 | -6.91171 | -59.3586 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68a89984-016a-3a01-8153-0db0726fe508 | -9.11967 | -67.71051 | 2025-08-27 05:18:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94ae6e01-dffc-33ce-bfb4-19a3665d5109 | -7.40697 | -64.35033 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fafb6045-8c1b-37bd-a79a-4d3de60ee936 | -10.79778 | -47.08078 | 2025-08-27 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| a96b212f-ae7f-3d6c-9f6e-a50752e38810 | -6.24531 | -60.00369 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4553233c-c7ee-317f-a313-ebac88dec65f | -8.24168 | -61.45619 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e371f73-e73a-3f78-8011-cdd156f92786 | -9.16602 | -60.76833 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d27d117c-7a23-3b7f-9d71-4f3e42c8ee08 | -9.59002 | -55.37404 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 14f4438e-e085-3d2f-811b-45f383e94658 | -10.10279 | -62.90655 | 2025-08-27 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d8ae272a-c4de-3f0d-9e18-f04efcc30ad1 | -8.30186 | -46.32717 | 2025-08-27 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6895e311-45c8-3dfa-ac35-e551fae13ab1 | -9.23475 | -60.82671 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20bf0b15-756a-35b6-8ba7-40e609a24838 | -10.59993 | -54.89471 | 2025-08-27 05:18:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba108736-d57b-36bc-9b80-34646bbfbb70 | -9.78719 | -64.24114 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82d4625f-171c-3c3a-954e-ebbcc42ff8eb | -5.61045 | -60.22894 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a77610c-dddb-3755-a551-ee7379cc63cf | -9.17449 | -60.86076 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c56996c-e7f2-3981-bc62-001d546fbd0d | -9.1623 | -59.56056 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f0210bc3-8872-35a6-abcf-64ccc8e31242 | -9.17108 | -59.54769 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c99ffb33-96a4-337d-94e9-8e09f9be8c3e | -5.79462 | -59.2129 | 2025-08-27 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b2e49e1-5a60-39cb-b174-5b817fcebc27 | -9.16176 | -59.56404 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 12226c69-b3d5-34d0-9eaf-85a5ee392e01 | -7.47828 | -61.35423 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18ec9cc2-24aa-3de1-9ced-c7b6ad910ced | -9.28269 | -64.55777 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bb2fe626-d170-308a-a1cb-0beeab6ea6d7 | -7.74267 | -51.13797 | 2025-08-27 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 868dc458-9935-3aaa-8d7b-d3ec8dfbaf64 | -6.70548 | -58.56367 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6f616dd-e362-3bd6-aa9e-cd661c297a32 | -8.90372 | -62.47187 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bf039e7-2260-3c7e-9f41-5a2137be286e | -8.07978 | -61.54562 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fa31faa3-e6f1-30d0-b243-fdf85ba5d457 | -9.1743 | -60.8024 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a2e93dc-e285-316e-8049-6699d5d3ddb6 | -7.04526 | -59.8268 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a382a52-a931-3157-b4aa-afb5521b34a0 | -9.41081 | -60.51137 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c6242159-6f20-37ff-8812-ec3874e08478 | -8.72056 | -64.01853 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 960d04b8-41ed-33ba-bf86-aceadad574d1 | -8.86734 | -47.17225 | 2025-08-27 05:18:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cc1940a3-a248-306a-8913-7daef4df7b16 | -8.07412 | -61.53696 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b9b0aef-c7ca-319f-ae76-eb0f19d3ae49 | -8.93589 | -65.95146 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8341b684-18d2-3f36-95d0-0c7c5d017571 | -6.57799 | -60.07111 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28d5126f-5118-36f4-91c0-deb267bb0032 | -6.67632 | -58.86112 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 937507e4-e58d-31e2-8530-a3080caec9b7 | -9.26855 | -59.77315 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README60.md)
