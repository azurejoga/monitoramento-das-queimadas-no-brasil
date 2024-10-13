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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00a21be5-4414-39bb-b9f5-75505bff35c9 | -11.27243 | -60.44501 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b6a90f81-ae24-38bf-80ba-68b058386fd5 | -11.27038 | -60.36592 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 149b28ca-0996-3fc8-9e55-d82b0617d292 | -11.26951 | -60.41672 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7be50afb-3c98-3cc6-8cce-d70b5d334fdc | -11.26742 | -60.36083 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0ec2e91-3dc1-33fa-98cb-fe77bebdd064 | -11.26579 | -60.41618 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8d2ffdde-4fc5-3c84-9459-43cac789ea6c | -11.26298 | -60.36461 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35695a0d-eeee-3eb8-9640-a205ddfb1172 | -11.26206 | -60.41563 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| adf257a6-e332-339b-abd5-64c74d5e7635 | -11.25928 | -60.36402 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54e98fc3-8cf8-3774-b6f8-346e4090b4fe | -11.19335 | -60.6178 | 2024-10-13 05:04:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89a70ecd-d2c4-34ef-964d-1378b0adde95 | -11.16849 | -60.62749 | 2024-10-13 05:04:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f271354-5020-389d-bffb-42b7b24a3c73 | -11.16472 | -60.6269 | 2024-10-13 05:04:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f13f1f69-3dbe-38f8-866a-2c28442e4dab | -11.16017 | -60.63086 | 2024-10-13 05:04:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a5c9c1cb-2b1c-3989-be24-9a7dc7bb4da0 | -11.10991 | -60.46978 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bea1006e-a148-35ba-a839-08b11ff61e04 | -11.10913 | -60.47432 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f5188a3-e62c-366a-97d6-665d4bd683de | -11.0958 | -60.59831 | 2024-10-13 05:04:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de9ffaa6-0f99-3210-9a68-0a21cb62c9f2 | -11.08187 | -60.40948 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 121ae3b3-35b6-312d-93ef-18a4dacd4353 | -11.06159 | -60.43832 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 087ba477-b312-3a77-a989-e00c6bf30c28 | -11.05708 | -60.44219 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63993ed8-10f7-3d82-9c18-8e1034d3a126 | -11.55914 | -60.15507 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e690aa67-e5b3-3470-8dd0-2e1ad5bee0ca | -11.55897 | -60.28861 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8dc70a2-1b9d-33c8-8ff1-6b345f36167b | -11.5555 | -60.15438 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 839a16a2-a0a8-37e5-8c2b-03fc42dc94a7 | -11.55531 | -60.28791 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 626cedc6-b4b7-3f12-a6b0-731be89217eb | -11.55186 | -60.15374 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac1f7ad6-0705-38ca-ad13-a80947f5394f | -11.55164 | -60.28728 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4f55f4a6-3833-39af-92df-603da43e75d3 | -11.54722 | -60.29108 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5a3dd027-ebe2-30f5-928a-73738db092fb | -11.54491 | -60.15376 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98220094-3e90-39f5-b7d0-83f683495c69 | -11.54429 | -60.28608 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15440aa0-c476-311b-8c72-cb83736edf4b | -11.50645 | -60.24928 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11a7336c-1007-37bd-bc5f-3f6ef9c34945 | -11.50279 | -60.24859 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a62518a2-4246-3a60-b1e8-a580cc3a7b16 | -11.50056 | -60.23941 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53e95e95-f1eb-3369-b66d-971543b98247 | -11.49985 | -60.24365 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 459d4ad0-3594-3323-b0be-9c60e362a9db | -11.49912 | -60.24798 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a670962-651b-3b18-9af7-0aa7183d6236 | -11.45607 | -60.45901 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e08b4525-5877-396c-85fa-8f95005c7ac5 | -11.43023 | -60.43134 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b2107b4-2505-35aa-a834-a9604e5f82e0 | -11.42945 | -60.43591 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7316fdb3-9ba2-3a22-bf8f-aa0c45246b88 | -11.42653 | -60.4307 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cedb2780-588f-3077-a682-ddf62af81b30 | -11.42575 | -60.43526 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddb64aef-f55f-316f-9dea-e9160f3c5b1d | -11.42282 | -60.43011 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c6022ca-e54c-3c3f-a231-8093f5a020e0 | -11.41988 | -60.42498 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b613900e-529c-3607-868a-81eb3c70a65c | -11.4163 | -60.40135 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a378e37-34f7-3b86-b43f-a2c2bb52003e | -11.41261 | -60.40065 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7360df96-fb13-3321-87f0-51edadc143dd | -11.41185 | -60.40509 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8f04cbb3-b6b7-384a-8dc0-7de12357216a | -11.41107 | -60.40961 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 31d843df-4aae-390d-8da2-91b3969edb8b | -11.40303 | -60.38993 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7f43962d-b0b2-32ae-840f-acca0600cad7 | -11.40228 | -60.39431 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 31d551b1-4ab4-3d94-a5e8-3775219dd2eb | -12.33906 | -60.73072 | 2024-10-13 05:04:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aac70c90-03f8-3a6a-81ce-e805475f09a2 | -9.09431 | -61.18445 | 2024-10-13 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d7c63dc8-83ae-3382-9351-139ac4ef36a6 | -9.09431 | -61.17726 | 2024-10-13 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e242d245-2b50-3c5a-95fa-2c2a2a310381 | -9.09313 | -61.1843 | 2024-10-13 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cebf1a87-9b69-3891-b0de-3fb3f89d460b | -9.09168 | -61.17587 | 2024-10-13 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b13fa805-6556-3aaf-9559-d14ab051c249 | -10.69021 | -63.46895 | 2024-10-13 05:04:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d2ec4c0-dd90-3150-99fb-f7941e57bd6c | -10.64273 | -64.43582 | 2024-10-13 05:04:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ca7664c5-cb7f-3fe1-9df5-e33c5164d9d3 | -10.63795 | -64.43456 | 2024-10-13 05:04:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7a4812f2-3171-3a3c-996a-d8de8a28c729 | -10.63708 | -64.43932 | 2024-10-13 05:04:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1e06feed-c10d-342d-b408-f7bd20d3e86f | -10.63226 | -64.43831 | 2024-10-13 05:04:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b26c5b50-d13f-34bf-ad0e-9926e34f8a63 | -10.63116 | -64.44435 | 2024-10-13 05:04:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e28de6c-1ecf-3b4c-9363-2d12af1ff3ea | -10.59005 | -64.50419 | 2024-10-13 05:04:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89cfda7e-39d2-3ae5-a034-e3ab73aa4512 | -10.57964 | -64.47892 | 2024-10-13 05:04:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 214773f1-b716-31e0-940d-d8f810f4bca7 | -11.75201 | -63.83788 | 2024-10-13 05:04:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6956bf0-2744-3429-843b-50a643bc7369 | -11.74751 | -63.83668 | 2024-10-13 05:04:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d91ebbf-664f-390e-9370-5ab01f57f4c4 | -11.74667 | -63.8414 | 2024-10-13 05:04:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ba69270-e98d-34d1-b122-d6e328926d6b | -11.74298 | -63.83568 | 2024-10-13 05:04:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06a60c6c-83f0-3bf6-a673-1f5e7259c396 | -11.74212 | -63.84048 | 2024-10-13 05:04:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdceca3d-6ab2-37d4-95d1-5c73e9e92096 | -11.73843 | -63.83475 | 2024-10-13 05:04:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f94b8ff1-29ba-318d-87ac-aaf7fe547716 | -11.66721 | -64.04398 | 2024-10-13 05:04:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5734ce52-47b1-3ac5-90b3-a5da3afb6d96 | -11.62659 | -63.96032 | 2024-10-13 05:04:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a390770a-f05d-303a-b840-c099052558e5 | -11.62572 | -63.96519 | 2024-10-13 05:04:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a8f4f3f-b477-38ef-803b-ac5b0ab840c2 | -11.62531 | -63.83528 | 2024-10-13 05:04:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87bbfc2c-d739-3f8a-960e-767dcf32a8bd | -10.99701 | -63.89891 | 2024-10-13 05:04:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fbd8a14-4c2d-3835-9b56-57b012a832d6 | -10.86211 | -63.92702 | 2024-10-13 05:04:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26383237-af33-3c59-9a8d-07a6aa18d8e5 | -10.85826 | -63.92167 | 2024-10-13 05:04:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a57174a0-bcf1-356a-a1cd-6db23b9424f4 | -10.85702 | -63.90173 | 2024-10-13 05:04:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| acb8b30a-3079-3f92-9770-9acb8699fa92 | -10.85617 | -63.90644 | 2024-10-13 05:04:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 497ddc6a-6995-3d2e-bc72-8b606397bac7 | -10.85355 | -63.92105 | 2024-10-13 05:04:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa5096fa-4465-3336-9a22-98ebc22e3c5f | -10.85154 | -63.9055 | 2024-10-13 05:04:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79b453f6-9b21-3458-83cb-7a3510afcb56 | -9.40562 | -64.46284 | 2024-10-13 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.6 |
| ddccffa9-9510-3997-b53d-1ab49e86d229 | -10.74761 | -65.07111 | 2024-10-13 05:04:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b1db779-af86-3ef9-aec4-28029e754ed8 | -10.74708 | -65.07395 | 2024-10-13 05:04:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2448635e-8714-3327-a541-bd4cfa22ef7e | -10.74152 | -65.07581 | 2024-10-13 05:04:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8712c7b2-dc60-3bbe-af85-64e050848178 | -10.73647 | -65.07494 | 2024-10-13 05:04:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d288458a-0366-33c8-ba96-31ed221f3079 | -10.73596 | -65.0777 | 2024-10-13 05:04:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88c8362c-3824-3f5c-9627-61910628814d | -10.7354 | -65.08073 | 2024-10-13 05:04:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1ba13a1-2d7e-339e-abe3-d008c74a1a9b | -9.92313 | -64.77892 | 2024-10-13 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 537b7731-0ffd-3157-af65-aa9325510c71 | -9.9181 | -64.77804 | 2024-10-13 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 246ad7ae-f543-351c-9777-680a8d900188 | -9.89972 | -64.82171 | 2024-10-13 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb3315b9-cafd-38e3-8693-3d6411c7b161 | -9.89917 | -64.82465 | 2024-10-13 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3cd4a3e-f023-3c20-87b7-14010ea9c725 | -9.89074 | -64.81395 | 2024-10-13 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7023813f-f34b-3088-a143-e3a719dd79d4 | -9.88624 | -64.81013 | 2024-10-13 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 174a61f0-f2fb-3a9f-9b1c-b1308bbe27e7 | -9.87449 | -64.9305 | 2024-10-13 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2219b55d-9986-3546-bcc5-f82672b34af8 | -9.87393 | -64.93348 | 2024-10-13 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85fadf47-76d3-3cae-bdc0-835c772f3cd0 | -9.83517 | -65.05758 | 2024-10-13 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46accb9a-96c6-3e58-958c-f6877052c0d2 | -9.73133 | -65.06602 | 2024-10-13 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2f0a6a9-0f5c-3364-a371-2f4432ea26c2 | -9.73077 | -65.06905 | 2024-10-13 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1470345-62c4-3db1-a9fc-680e47eecab6 | -9.72833 | -64.88385 | 2024-10-13 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d7ec9a6-0b3b-33ef-9109-0d2a164f014c | -9.72676 | -65.06207 | 2024-10-13 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ace04fae-8639-3650-9bcb-02489793089f | -9.7262 | -65.06509 | 2024-10-13 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9201e546-37b8-30d0-a6ad-8817c755d91a | -9.72563 | -65.06812 | 2024-10-13 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9160e7bd-b9fe-318b-b88c-a6215d821b7f | -9.64582 | -64.94373 | 2024-10-13 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0f1a1bd5-3bfd-3e62-a5de-821d2c533c92 | -9.64526 | -64.94675 | 2024-10-13 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2e9324d9-96ec-31fa-a059-61969285dd4b | -9.64358 | -64.95589 | 2024-10-13 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README89.md)
