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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de3a20d9-e503-3cb2-9025-c05a02b5b019 | -16.95264 | -56.79357 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| bb2d0640-ea13-38e2-ba83-dbd6087e4a50 | -16.9524 | -56.798 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| e2ad872b-7b0f-300b-b792-942db3190472 | -16.95203 | -56.79887 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 5b4440a5-c906-33de-ba77-2d1d6ea983d3 | -16.94763 | -56.79739 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 15ad0bd5-b712-3834-ae6d-0cc8931e0af2 | -16.94726 | -56.79824 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 244a2fab-5815-3bf4-870f-54aec857a964 | -16.88651 | -56.74099 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1004ef20-2852-32a5-b01f-ad0985facbd7 | -16.73234 | -56.69668 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 3bd54436-698e-3f8f-a9cd-f230f30f7e99 | -17.17339 | -56.81408 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| d2bf1ca7-b58f-310a-99ff-6d303f05044e | -17.17337 | -56.80968 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| e4562492-0b2b-3ff0-9806-4ae362d5a694 | -17.17275 | -56.81499 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 2958d74b-256f-3f66-adfd-f7b7488b5b4a | -17.17274 | -56.81938 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 1893936c-7730-353c-8bf3-c93473d6ec2f | -17.17214 | -56.8203 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f8511c05-17a5-333a-9aa8-421787aac257 | -17.1703 | -56.83623 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 61ff94ea-7dc7-3ddf-922b-4b231b75be7c | -17.17013 | -56.84058 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 68d3f485-c52f-3909-b327-d8faf7889e6c | -17.16992 | -56.80286 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0d0d8ea7-d351-316f-85f2-bad71457b573 | -17.16969 | -56.84154 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 8ce60d99-dc6d-3cab-9ec5-8863777be5c3 | -17.16948 | -56.84588 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 60cc162a-b0da-32e3-ae25-817520ffc552 | -17.16927 | -56.80817 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 82697ad4-1754-3689-a0e2-34e0f8cbca25 | -17.1692 | -56.80375 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ae0cd550-ad92-31d9-8fe1-0f6310d79f52 | -17.16862 | -56.81346 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1a41738d-5616-3186-8244-f0504acc6758 | -17.16859 | -56.80906 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 7849eb31-10e6-36f9-8d23-df8ef649ae91 | -17.16731 | -56.82406 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1fce81b3-bcbe-3b95-aaff-f89d2bf246b6 | -17.16675 | -56.82499 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6396408a-0dea-358f-9d9d-ef55424cc5af | -17.16666 | -56.82936 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 63c65bd7-4e54-3dc3-94ee-bbe13013ce9d | -17.16614 | -56.8303 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 74f307a8-7846-39d4-b49b-05f135312fdb | -17.16536 | -56.83997 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ecac10b1-288c-3076-9f2c-bfb2a277a9ff | -18.66076 | -57.33207 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 409532ff-8e86-36d7-8186-f01c0f7530ab | 1.30559 | -60.41589 | 2024-10-17 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40df9db4-0bd7-36e7-8a48-90d097bd106c | 1.29856 | -60.42836 | 2024-10-17 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea8167a5-e78e-3a81-aa43-0490b2e3ad63 | 0.97467 | -60.40502 | 2024-10-17 05:50:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e82733c-4d3c-3ff9-8f3b-c38280ab8065 | 2.60295 | -61.31532 | 2024-10-17 05:50:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3d096cf-a5c5-3df9-8cc5-280b70c4669d | 1.94633 | -60.86335 | 2024-10-17 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6cc4462c-ed7b-3477-8ac7-d3db959b6d35 | 1.9457 | -60.85944 | 2024-10-17 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 484e67f6-57e3-3fde-a1ec-e0475201d12c | 1.94148 | -60.86007 | 2024-10-17 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3316c6fa-0446-348b-890f-dce53b24507b | -6.63397 | -58.72802 | 2024-10-17 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d78ac22d-6dd2-34a9-ad75-8d80d0765c7f | 0.68279 | -59.64469 | 2024-10-17 05:53:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8e453fc-bdec-3dae-8a47-9c19a9e27802 | -9.15821 | -61.90274 | 2024-10-17 05:53:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 395ac462-77a2-32cf-ad3e-5cc9c2ad3961 | -9.15756 | -61.90762 | 2024-10-17 05:53:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 13.7 |
| ecb93de0-b2c2-3923-95d9-ae2f6693097d | -9.15459 | -61.90585 | 2024-10-17 05:53:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 170bd870-842d-3008-93e7-eeddad30734a | -9.15994 | -61.9016 | 2024-10-17 05:53:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e6ab36fd-7bce-3c43-8164-b84a851dcfc4 | -9.15925 | -61.90649 | 2024-10-17 05:53:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0c09884c-fa53-3f5a-b886-9ff37798c80c | -9.15857 | -61.91132 | 2024-10-17 05:53:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3553051f-5422-3f06-aaab-94e0f3e9827b | -9.15529 | -61.90092 | 2024-10-17 05:53:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b7b7d9f7-8e87-3a16-aae3-6d3619cc42d8 | -9.15391 | -61.91068 | 2024-10-17 05:53:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 39eef362-c97c-32e1-bb82-4fd593abb3df | -9.15291 | -61.90695 | 2024-10-17 05:53:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97800d92-0b76-3f1c-9512-c778154ca79b | -11.72254 | -64.02324 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50ced243-64d2-3e9e-9275-0f818ab26e9b | -12.17491 | -64.40891 | 2024-10-17 05:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f968e4b-a170-37c2-bf60-d27ffd6da50b | -10.83012 | -65.03019 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 610729ab-52ec-350f-82eb-583d89cf8043 | -10.82835 | -65.01487 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b50d2203-ee55-3d9b-9fdf-45f72c4d8183 | -10.82625 | -65.02962 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 921c53ad-0351-3b28-864a-f5e282e3be5f | -10.82238 | -65.02908 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce1a7e20-2245-3acb-828c-eeb752b52b6b | -9.31071 | -65.807 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0f6fd4fd-7cd2-3257-afc6-3412ff18a189 | -10.91131 | -65.10902 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1ac46f2-830e-3413-8be6-7d96cbdc801b | -10.90745 | -65.10843 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7641dc30-227d-3d77-988a-f0f690a1ef57 | -11.88326 | -64.93601 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1b33427-114d-3bd5-8f3f-115ac2be3cfe | -11.88255 | -64.94116 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7ba1590-487e-3a21-bfdf-2aaccea75200 | -11.88184 | -64.9463 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18ea26ab-0f39-3770-9842-d5c4ed60e86c | -11.87931 | -64.93544 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8169b5c5-6514-38c3-837b-c3d726026456 | -11.8786 | -64.94058 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2beaf30d-805c-3381-8e89-e460f06bdf3c | -11.87789 | -64.94572 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66f2c877-e568-3942-9fda-069ded41dd23 | -11.87536 | -64.93487 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc554198-873a-37fa-a831-4e71b129fe8e | -11.87465 | -64.94 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9621a018-a1e3-3784-b2ff-038d4b173b8b | -11.87395 | -64.94514 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45675175-2ae9-3d51-bb97-9f82b212257a | -11.87263 | -64.93264 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4274358e-0b98-3d50-950b-6e0b891e14b0 | -11.87189 | -64.93777 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6d01a99-0646-381c-80a1-38e4a2756887 | -11.8714 | -64.9343 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a4430c3-e115-3419-9c3f-67b1a4264a9a | -11.87115 | -64.94291 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d16f4b3-b208-3d46-93b2-cc38f8eab89d | -11.8707 | -64.93944 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a236942e-2235-34e9-940c-c74dd5b57190 | -11.87041 | -64.94804 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6891307d-e276-328c-821d-c321010a2ef5 | -11.87 | -64.94458 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f6efa15-ca35-307c-bf52-8e47eadc3798 | -11.86929 | -64.94971 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ac487e1-f6ac-3288-ab3c-576b26d134c9 | -11.86794 | -64.9372 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8fa3708b-c1d8-36dc-b499-d2ff93b6eea4 | -11.86745 | -64.93373 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5e53d815-2493-3f5e-b1ec-6114ee49ae20 | -11.8672 | -64.94234 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21c34684-42eb-3839-bf48-9d882a2af257 | -11.86675 | -64.93887 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7556486-e8a4-329b-ae3c-cd89f2548995 | -11.86646 | -64.94747 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1810f4ac-1029-3a15-b9d8-1c4d8f77c763 | -11.86605 | -64.944 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 004cd877-0870-3d30-93d8-0ed113f4af0b | -11.86535 | -64.94913 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f9060f0-837a-312e-90fd-6a4a3f9b5a04 | -11.86399 | -64.93665 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cba4d4db-843e-3acc-bf1e-ac809319687e | -11.86325 | -64.94177 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84284923-d264-3173-92b1-80bbfa47fc44 | -11.8628 | -64.93829 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 47464307-29af-3e18-a3b4-cb089b2d70ec | -11.86252 | -64.9469 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f7aae53-afe9-3db9-9307-ff3a7a356287 | -11.8621 | -64.94344 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b1a016e-e478-3959-90c5-d3f912feabbb | -11.8614 | -64.94856 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| adafc030-b34b-30f2-a71f-e9bda700f848 | -11.8593 | -64.94121 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4157d3a6-4855-3d6c-be19-99c505a33a5d | -11.85857 | -64.94633 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83ee33af-8e93-3fd5-86cd-8978e7694603 | -11.85815 | -64.94286 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8a52dbbc-6629-37dd-9781-f848ef63d615 | -11.736 | -64.96285 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd911b97-a959-3923-8a56-6b5f874e7572 | -11.73528 | -64.9679 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fe8cc442-7f21-3168-861f-77143a94cbbe | -11.73456 | -64.97295 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d9217901-3fc8-3c2f-91fb-065a96bcdead | -11.73207 | -64.96229 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 343280d6-f6a3-3a63-a241-21d311b00c88 | -11.73134 | -64.96735 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5bba8d4d-04e9-375d-be95-4a49f23389f6 | -11.73062 | -64.97241 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 401b0e27-a56a-34c1-9d5f-057d639a0f57 | -11.71883 | -65.22076 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5490ac92-d8aa-322d-8e82-125bd3d6e949 | -11.71599 | -65.22283 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5fb0455-38ee-3f9c-ac4d-8351cdfbb95e | -11.71496 | -65.22019 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99332ff8-9781-38e8-be69-4440671585de | -11.71212 | -65.22225 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6589b530-285f-33d6-8de5-61d146d0c61c | -11.71009 | -65.23703 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 915e6142-2a72-306f-b67d-0f5073de650f | -11.70622 | -65.23645 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ae96e00-b5f3-3593-9456-7d8c276b206d | -11.70554 | -65.24137 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README59.md)
