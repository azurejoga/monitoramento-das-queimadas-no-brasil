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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d4a2fe1-bc0a-3a06-b361-d8d42190d969 | -15.83757 | -59.60036 | 2025-10-01 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67a8e421-cff8-3df0-a311-1c2778991a35 | -13.30618 | -50.66167 | 2025-10-01 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f06ecd0b-e7b0-3427-b029-6a814d690ef9 | -14.05128 | -47.97179 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2a896c72-ac14-34a3-b879-c7184ad9d8a9 | -13.93946 | -48.12617 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 83240d7c-57fe-3008-824f-35c1d64c1c72 | -14.17085 | -46.11605 | 2025-10-01 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4b5b42b3-6d89-3db2-a141-ce6a51282f01 | -13.77345 | -47.96746 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e0f3fec3-5b01-347d-a6eb-5a01f9446070 | -15.84533 | -59.59433 | 2025-10-01 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 788e7e07-f6ed-35be-8cf4-7dd59954dfbe | -16.76039 | -51.3412 | 2025-10-01 05:12:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d755f2e6-ff86-3c38-8216-6952628e13c8 | -13.76884 | -47.97842 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8f22378-c51e-3ed4-b265-d9a50294bf1e | -14.71617 | -48.27469 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f14a031d-f86e-382a-84c4-47c78c7ea5df | -13.70997 | -48.63647 | 2025-10-01 05:12:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25857dec-7ad9-354b-9158-ccd50c6912ad | -14.69965 | -48.22854 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c713e444-d03b-3fff-aa48-29598d4b60a5 | -13.94361 | -48.1263 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9247b89d-51fe-3b96-a4c3-881bff4a34d3 | -15.31966 | -46.41047 | 2025-10-01 05:12:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c0f29d5-fc42-396d-9a2a-bd8e7568f854 | -15.362 | -46.11874 | 2025-10-01 05:12:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 515e5619-97a5-3489-8fc9-c89aca7b9625 | -15.33247 | -46.28037 | 2025-10-01 05:12:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4d1588dc-778f-3144-a559-1abf95ac85b7 | -14.73178 | -46.83587 | 2025-10-01 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a53f38b4-b769-3935-a0a2-318d3c038e3d | -14.72414 | -48.14681 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2aeb26cd-8b85-37c2-a9c2-0495c468cb48 | -14.9755 | -50.78529 | 2025-10-01 05:12:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3514647a-5d56-3b33-9f8c-0fbd2a0829bc | -15.17358 | -49.08676 | 2025-10-01 05:12:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ae39e02-c7f2-32bf-9c7a-c40f38006e15 | -14.89233 | -48.13146 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cee3122f-6efc-3a94-ab33-6a4c0fc9ec26 | -14.92064 | -47.82236 | 2025-10-01 05:12:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e6f5324d-ceb0-3a09-8f63-dec8054a2bb7 | -14.8861 | -48.3283 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73cb1ad5-538d-370d-872e-83624e4921f7 | -14.72246 | -48.16221 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63c12610-2beb-35c8-8e62-c502df8e13aa | -14.18924 | -46.10282 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 661f3738-a2b7-3612-bea5-56f702153197 | -16.37857 | -47.06168 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4cd825ab-774d-36c9-a665-abd57e827870 | -15.85138 | -59.59903 | 2025-10-01 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72a24c92-3954-35ac-96d5-ac2bb052d62e | -13.71926 | -48.65636 | 2025-10-01 05:12:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61a1eb0b-1852-3672-b8bb-9421fa2e2d6d | -15.33555 | -56.63612 | 2025-10-01 05:12:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb05ab75-887b-394f-81bf-0a4954389845 | -13.98665 | -44.91618 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 94f1db4b-3a49-3760-b857-d48e413bf4bb | -14.9011 | -47.20967 | 2025-10-01 05:12:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9625aae3-089b-3ec1-9e36-eba5d17c056f | -14.19165 | -46.11197 | 2025-10-01 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3a4da529-e554-3e5c-9997-512f251fcf36 | -13.66087 | -48.08031 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1de81fec-977a-35fe-a941-81368c41dd74 | -14.01725 | -46.31728 | 2025-10-01 05:12:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae496f7f-7d73-3597-b521-91f47df4a46d | -13.92018 | -48.08508 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a71e9721-ba0e-3e04-9a8c-76e9acf8f125 | -13.82379 | -47.50875 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1cc14bf8-ca2f-3626-b8a5-697c87510a76 | -16.37731 | -47.07497 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6be6e32-e6aa-3292-bced-e85d9557f59e | -14.79843 | -45.80969 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43867676-5c42-3986-9adb-68295d589f9d | -14.98763 | -46.96544 | 2025-10-01 05:12:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 34d2e798-8c32-3cf0-9032-64bb7e69a53e | -13.30122 | -50.66101 | 2025-10-01 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d28daa3a-2094-3f4e-bbbe-82978df7cd8a | -14.06157 | -45.0334 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7dd06c39-8ffd-36c2-8a03-1fcd5633e159 | -15.27024 | -51.48047 | 2025-10-01 05:12:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80180c6f-ccb2-3bf6-9cb8-db08f1244930 | -14.72467 | -48.14201 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80046627-2a47-3710-8aa8-99d849fa08f3 | -14.14806 | -49.20115 | 2025-10-01 05:12:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b9df8b6-c52a-3df0-b30a-c34736664a8c | -14.60519 | -48.3225 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d11aa2dd-bc97-3ee6-b2d1-a56c3e62c570 | -15.23504 | -48.74673 | 2025-10-01 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 219635ab-d083-30a3-bcb9-a627fb89c345 | -18.70709 | -49.16963 | 2025-10-01 05:12:00 | NOAA-20 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd5731c9-b198-39c4-b2ae-b3746e314c9e | -13.62796 | -47.64816 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14fc9e1c-0f0c-3ed5-9e7a-972c3e1d5333 | -14.52628 | -53.1172 | 2025-10-01 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 35120523-32c5-362e-a099-fb8127f84b70 | -14.73127 | -46.83349 | 2025-10-01 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f1dbcd85-7d98-3ce2-a6ff-45ec314a323b | -14.52096 | -53.12482 | 2025-10-01 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a325b434-0848-3648-956c-b7b7d6c34152 | -14.99543 | -46.95316 | 2025-10-01 05:12:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7056a5f5-a721-3859-a8db-945d67220c5b | -14.68445 | -48.23537 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62aed7de-494e-3969-bae8-b99ffda4846f | -14.612 | -48.31488 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aef35fc7-8f72-31b7-a8bc-bf4961108661 | -15.84864 | -59.59489 | 2025-10-01 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c021f33-65d7-3747-b14c-1c4f1015e22a | -14.69883 | -48.13066 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce2b8408-3315-3ed8-9697-557c341cc9bf | -13.77288 | -47.97258 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ea092eea-6f3e-3807-b3ea-75b9fc7b1792 | -15.24872 | -56.8108 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5491509f-c18e-3bc8-b43b-b0a0d47db358 | -14.78741 | -45.78117 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae8e1241-2f1c-3313-9100-0aa2ccd22df5 | -14.67834 | -45.27906 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8b728a9-0cff-3056-a24c-85f8634f8813 | -13.72903 | -48.81944 | 2025-10-01 05:12:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1739752d-fb89-32e3-9382-b55d076a15a4 | -14.18365 | -46.12313 | 2025-10-01 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f34d28f2-26ea-3ed8-816a-ab5df064d000 | -14.88079 | -48.32194 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b87b631-1ddd-3078-af3a-3865c849691e | -15.33908 | -56.63668 | 2025-10-01 05:12:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5433c6aa-bd25-3be6-a99f-219f9ae7354d | -13.94028 | -48.10185 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc6e4b63-e06a-302d-a117-5be57196ee41 | -16.75893 | -51.34542 | 2025-10-01 05:12:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ad9cfc2-5680-3dfb-838d-f34293c7492c | -17.40466 | -47.17541 | 2025-10-01 05:12:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 69f49372-61aa-33b2-9ea4-8cb77be00ef6 | -14.89599 | -48.12159 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4c202b75-53e8-3fa9-b6d0-2df098ec0cba | -14.5171 | -48.37458 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb9c2834-a8d5-3498-9404-65953e268947 | -14.75992 | -48.09657 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b99619f1-f372-38b6-952a-30d3a1511a52 | -15.2867 | -56.79571 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9d72e07-e4d7-3329-9640-bd893d08e1ae | -17.89387 | -57.58975 | 2025-10-01 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| edae3e70-0fab-300b-b2fe-3efae7c65e8f | -16.76463 | -51.33997 | 2025-10-01 05:12:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcf326dc-4949-3d57-b465-8a64d881349b | -16.39998 | -47.04247 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66f11262-f525-3c91-8aa7-23ba903db023 | -14.76585 | -48.09779 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a3d72539-fbb7-3fce-bc4e-8fb465267390 | -16.92194 | -49.79308 | 2025-10-01 05:12:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d6ce46f-f645-3a6d-bd2a-fc9f3790d300 | -17.93153 | -57.57481 | 2025-10-01 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 3d314675-40ff-37d5-8fd6-ffd7c5caa9f6 | -15.34309 | -56.95376 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0823d4d-b999-3cce-bb3c-8ec1d142a791 | -14.35433 | -45.91469 | 2025-10-01 05:12:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 187436d6-e9d8-3590-9045-9ff2c5554c2f | -15.25398 | -56.84795 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6c789ea-be8f-30b1-85cc-1ddbbd1dfb0a | -14.35372 | -45.92058 | 2025-10-01 05:12:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 7e527282-60a8-3a41-8dff-4efed99fcc86 | -15.85082 | -59.6026 | 2025-10-01 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e030f2e-7939-3af2-a5b8-4937ae40106d | -14.90063 | -48.13503 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 46551dca-f004-3569-a2a7-7b0fde073f35 | -14.76251 | -45.75162 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3275f8e-c9df-3a36-b699-3358856a667d | -14.6762 | -45.2999 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dd25da06-ccdc-3db9-9cc1-0cc3bc88f187 | -14.70516 | -48.12815 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e13d7633-6691-3776-97a2-1b7d4e1d95fb | -14.68749 | -48.12404 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8361d0db-8e14-32ec-b17f-4e84fd516168 | -15.83622 | -56.38967 | 2025-10-01 05:12:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4efc3c5a-ace9-3d1c-8e41-d54efa52e019 | -14.49971 | -48.4237 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82e5c140-4dc7-3acd-8c48-e9ec1d6c6d72 | -14.55544 | -48.24677 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0be30744-9ff9-3c9e-af6e-fe82d1243130 | -13.76355 | -47.97203 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 12621360-f08a-3714-979b-a324a8540be8 | -15.94456 | -48.12583 | 2025-10-01 05:12:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 71dcb7cd-18b6-3fc9-90b3-c6fa161a98df | -14.98148 | -46.96201 | 2025-10-01 05:12:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a689bffc-6ab3-3d74-a194-8c30f505b3d5 | -14.90049 | -48.11279 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2eaa249c-dab9-3e90-a50a-c32a807024a8 | -14.66832 | -48.13322 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d18f6f52-290a-3dee-bc17-50f49d73d5e2 | -14.98848 | -46.95729 | 2025-10-01 05:12:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 577751ba-ed90-3f44-86bc-1d0784307d5a | -14.13737 | -49.19643 | 2025-10-01 05:12:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73af48eb-7616-32bb-8e9f-64c42ff51e70 | -14.5946 | -48.2192 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5a1b082c-74df-3278-8ca5-0d1fe4305130 | -17.86627 | -47.14942 | 2025-10-01 05:12:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7dacdf99-9eff-3458-b238-5869ac7e545a | -14.90743 | -47.2104 | 2025-10-01 05:12:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README136.md)
