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

## Dados Diários - Página 169

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ac85822-e5b4-33ff-914e-de7095ab6d8c | -9.25831 | -60.70434 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54d48e98-73b4-3233-b203-182ed2ab3d34 | -9.21713 | -61.14088 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 726d2881-bfd6-3278-be11-c78bd263d066 | -9.21278 | -61.14022 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76cabbbe-95fe-3d2c-8bf9-a5c04fa4fe6d | -9.2122 | -61.14445 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fcf3679a-1430-388d-ad5a-a91a052b51c8 | -9.21162 | -61.14867 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fe3805b-9e3f-3dc0-94c0-734132f126a1 | -9.20886 | -60.90922 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92d803b2-05b2-3827-a191-52d03d93e60c | -9.20784 | -61.14381 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99fac363-b3f0-3752-875c-492aabd6ca4f | -9.39214 | -60.30328 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba9812c4-f7a6-31c2-9365-785bffe8bdcb | -9.39147 | -60.30815 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f36d951d-11b6-33e3-a7eb-962e05ec0e60 | -9.38819 | -60.29775 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c994b681-9e2c-39ec-a635-807a5d188ba7 | -9.38683 | -60.30753 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18dfdd3e-f45f-3b4e-a9ce-4f220c5f90ef | -9.38152 | -60.31179 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f76c77c9-e287-34bb-aaea-5fbc68924a69 | -9.34248 | -60.28651 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdf6f751-3502-3e89-803d-46ca103426e7 | -9.32451 | -60.48826 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7100f3f9-6f87-332a-8c23-a23b2b446020 | -9.91976 | -60.75162 | 2024-09-26 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d26c8613-54a0-3fb5-bd6c-d1ddb09bd26e | -9.91914 | -60.75621 | 2024-09-26 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e05dfe46-3ab3-3c10-a04b-2a67efec15da | -9.91852 | -60.76084 | 2024-09-26 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0c5943b-352e-33de-a229-25c9ca254824 | -9.90703 | -60.73277 | 2024-09-26 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e4bc39e-a3a9-3400-9c89-8683287dbdf0 | -9.89957 | -60.72996 | 2024-09-26 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad700e6d-d8cc-33eb-b559-4520ee999836 | -9.84636 | -60.77105 | 2024-09-26 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e4348e0-d1c3-3d9f-9dbe-585dba893126 | -9.84573 | -60.77562 | 2024-09-26 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36c7eb43-1388-36f7-b378-348d60491b8e | -9.36239 | -61.02874 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4e734d2-386d-36cf-a159-44be6d16c871 | -10.72948 | -60.73718 | 2024-09-26 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| abab7d4b-a00f-3c7a-9555-793f6fba7471 | -10.71701 | -60.72581 | 2024-09-26 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66362731-43ed-3894-b7d9-b6f225ef2ee9 | -10.71242 | -60.72522 | 2024-09-26 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a585de1b-b353-328e-9f90-5b50909001c6 | -10.70783 | -60.72459 | 2024-09-26 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8382bec4-e6ea-3bfa-8d65-5c98b57dfd43 | -10.70718 | -60.72938 | 2024-09-26 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 44ce1ce7-77ff-3766-b2d7-8a6e17584fb3 | -10.69089 | -60.74642 | 2024-09-26 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af0770f6-28ba-364f-af7d-bfc3ac9b6127 | -10.69025 | -60.75119 | 2024-09-26 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da19a988-174b-36ca-a4c4-9c56adea03ae | -10.68631 | -60.74577 | 2024-09-26 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bcd9b67-823e-3365-8412-94fc01af32d7 | -10.68568 | -60.75054 | 2024-09-26 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4737ef2-b4d4-371e-823c-b3c854839935 | -10.68174 | -60.74511 | 2024-09-26 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed551211-f917-3dc7-a9e3-9e8f07c42041 | -10.6811 | -60.74987 | 2024-09-26 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a4f9755-6027-3c47-a4c7-46e26889a1a0 | -10.68047 | -60.75464 | 2024-09-26 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d06ebb4-eb56-3b1b-8868-7c98899970f3 | -10.63141 | -61.12168 | 2024-09-26 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c6870ab-1247-37d5-b699-9ab3d4ba9201 | -9.82496 | -60.4859 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bc49136-25b7-350e-96ef-139a3295a691 | -9.82427 | -60.48665 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8c8a75d-816e-30ea-9f7d-ae97ac1d1511 | -9.81969 | -60.49006 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83fd8d33-ab19-3301-aada-88322556da3a | -9.81903 | -60.49083 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30630507-70c9-317c-82d9-d69b6410f22a | -9.57716 | -59.77417 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b317368c-cf4a-3101-ae89-ee6a10947076 | -9.57642 | -59.77954 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe75b76b-0974-37e5-b33c-0b000b1242c4 | -9.57308 | -59.76812 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 683d6fc2-5032-3afb-a720-80351e1914fe | -9.57235 | -59.77345 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aaa68a4a-5094-31db-86fb-425a30a8ca05 | -9.57163 | -59.77874 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25a79c1a-a844-3c12-8750-0be4fe468cb0 | -9.57091 | -59.78395 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 020ccdac-3cb3-3ecb-9cc4-a735f6a7edc1 | -9.56899 | -59.76211 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e8a3d43-516c-3b11-af6c-0b25ad66dfc9 | -9.56826 | -59.76744 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f929f15a-071b-3b36-ba5e-c51576abb2fa | -9.56754 | -59.77275 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3603cc5e-ae33-3589-a661-34d806e4d89c | -9.56682 | -59.77802 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9ff4eb0-85de-3f4e-be26-2ba92e896c64 | -9.5661 | -59.78328 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7afdaa0a-e667-3832-89b4-7a03013891e0 | -9.56272 | -59.77204 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 317eeb0c-5ce4-3b7d-bed8-1ae6786e2177 | -9.562 | -59.77732 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b919c0a9-efc9-3b27-9d5d-b35f331a92e6 | -9.56129 | -59.78259 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f63d2698-06a9-3f61-9812-d3982aa00701 | -9.56057 | -59.78788 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48976c19-3507-3931-9189-3a6ee6621c22 | -9.41598 | -60.30176 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1efeb55-e256-319b-a6e5-997e693ba852 | -9.4153 | -60.30656 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad745829-1d26-3add-b45f-0177b9faf0de | -9.41438 | -60.30349 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96e91e42-81ee-3f34-9537-87c9640101dc | -10.04154 | -60.44107 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5adcd66d-d015-39b3-abd7-157d1152f6d3 | -10.03999 | -60.44287 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec7a74a4-ecb8-39ba-a13d-4b10eac6c56a | -10.03623 | -60.44527 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a6592424-b1d5-3174-aa85-a9cfa247c4b9 | -10.03536 | -60.4422 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c4efee9-e6b8-325b-a948-93530136ef97 | -11.16056 | -60.72729 | 2024-09-26 05:48:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16489263-cfe9-3493-9763-3c673ddc52c6 | -10.92336 | -60.92578 | 2024-09-26 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 455ff8ba-2629-3a0c-80fa-c496ce7f2b38 | -11.00014 | -61.41173 | 2024-09-26 05:48:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53857de2-3ed6-3e7f-8a5e-05512f0de89d | -10.99956 | -61.41608 | 2024-09-26 05:48:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19b69a7e-cec9-339d-b307-280a51cf1875 | -11.61618 | -60.34894 | 2024-09-26 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3a847a88-ff72-306a-bd2b-474d14fa15a8 | -11.61137 | -60.34867 | 2024-09-26 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1a25b55-0b42-3654-92f5-46a0df32cccd | -11.60656 | -60.34827 | 2024-09-26 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| abca2df0-e416-3dc2-a0dd-d0e26363676f | -11.60587 | -60.35362 | 2024-09-26 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 620da30a-adb1-3d7a-9a8d-638525e1d22d | -11.60521 | -60.35866 | 2024-09-26 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7eee7a50-cf50-3f7d-a0d4-96cc1e463bbc | -11.60179 | -60.34766 | 2024-09-26 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8970a7ec-f4e0-3868-9f34-b4385fe53d08 | -11.6011 | -60.353 | 2024-09-26 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 16.1 |
| c81f4735-ae97-373b-98f9-dca8a526aadb | -11.60045 | -60.35799 | 2024-09-26 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 946ea413-4c9d-30de-982c-bfcde36c7f62 | -11.59982 | -60.36284 | 2024-09-26 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f7b67ecc-5174-3ec1-b48f-99ee8b76e9c7 | -11.56684 | -60.27884 | 2024-09-26 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbdf6b52-0223-3310-9e3b-22b8c5c14209 | -11.55178 | -60.17273 | 2024-09-26 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c90e7296-99be-35e5-b82c-b60ade5e53f3 | -11.54762 | -60.16703 | 2024-09-26 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 074f7ef9-0a9d-3341-9f0f-7d2792618c65 | -11.5342 | -60.41521 | 2024-09-26 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c53c9ff-c801-3a61-b025-a8644ae59c67 | -11.53352 | -60.4203 | 2024-09-26 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d273e325-b5cf-3d90-ac36-d3763d648032 | -11.53313 | -60.16522 | 2024-09-26 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| df33d68d-b724-361b-9f4f-37587bdeaaf8 | -11.49949 | -60.23581 | 2024-09-26 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5de3dd8-e0b8-3963-b7a8-f8eeab5b7378 | -11.49607 | -60.22443 | 2024-09-26 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43a8ab79-b9ed-3753-987e-86f3dda876ab | -11.49538 | -60.22982 | 2024-09-26 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38f0e9cf-bc1d-3d3c-a655-cbd238f503a5 | -11.49262 | -60.21324 | 2024-09-26 05:48:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcfd849a-ec7e-3a03-b72f-6c4ef48aefb2 | -10.9894 | -60.56788 | 2024-09-26 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5ff94bd-f84f-3c10-a330-5845bb6f9139 | -9.16685 | -61.17438 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6dab9903-d65f-37fa-90fe-a591e3e2c5a5 | -9.16251 | -61.17376 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7045ce75-d979-36ef-add3-739851736a24 | -9.14731 | -62.41731 | 2024-09-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a90ab06-7778-3617-8f48-067fff6d6324 | -17.10377 | -56.16605 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 97d8d215-99ed-3990-9300-58fde1a69bec | -17.1032 | -56.17215 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 1d78f648-0551-3e15-8e34-5199b835700e | -17.10262 | -56.17819 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| bb67dd6b-01be-3c0f-b6a4-d3914c67a8a3 | -17.10229 | -56.1449 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 375fce90-75fc-356a-b07b-45dae2e1d288 | -17.10204 | -56.18421 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| b1cbdb9f-d6ec-334f-9dce-d65a2890f191 | -17.10176 | -56.15093 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 34bb9e63-55a1-323a-9ea1-c927fb7bcd4f | -17.10122 | -56.15702 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 8292d63e-9372-3fc7-bcba-2249d5116d39 | -17.10068 | -56.16312 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| f433a133-8abf-3b76-bfe0-85e858d5d2ca | -17.10015 | -56.0612 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 864fd673-6840-3742-8a11-df41af386aeb | -17.10014 | -56.16919 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 51ff903a-3a2b-31de-a36c-a73a58ce26dc | -17.09961 | -56.17524 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 45.8 |
| 5fceea19-8e1a-3ad4-baca-d21c5dfa9425 | -17.09957 | -56.06732 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |


[Clique aqui para ver as próximas entradas](README170.md)
