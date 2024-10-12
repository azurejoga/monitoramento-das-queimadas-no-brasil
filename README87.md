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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d1292c5-434a-3c8c-8fcb-fddd6e1402e4 | -10.54944 | -49.94761 | 2024-10-12 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34c2154a-a64c-3e14-a150-3276eba06cb0 | -10.54894 | -49.95124 | 2024-10-12 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ebfb8c6-a985-3dc5-98c9-b41c7a99f0a5 | -10.54538 | -49.94702 | 2024-10-12 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20bf92f7-4e90-3130-9d87-26552c9fd501 | -10.53811 | -49.10709 | 2024-10-12 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89c0de5a-befd-3ea8-b393-004a4c7b80ea | -10.53514 | -49.10844 | 2024-10-12 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab649f1e-5bf5-3a84-95ba-175858b12eee | -10.53382 | -49.10649 | 2024-10-12 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95c7a41c-06e4-3c81-af0b-3d55dd7849a1 | -10.53085 | -49.10785 | 2024-10-12 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 612fdc60-f620-379f-9ea7-e5e166ec594a | -10.5141 | -49.7826 | 2024-10-12 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84625131-01f0-3839-b5ae-d880e8b17362 | -10.51358 | -49.7863 | 2024-10-12 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b9e748b-90b0-3a75-8a6a-7fee5e6a754d | -10.51306 | -49.79 | 2024-10-12 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a5acbad-e8b8-3cc9-87e9-16b27e08415b | -10.5081 | -49.97205 | 2024-10-12 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec20fc70-9b12-3b8c-a2c5-a0d8015f3d11 | -10.32648 | -50.56775 | 2024-10-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb8794d8-7dd1-3438-afab-aadb156c7501 | -9.94196 | -50.06427 | 2024-10-12 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 767b2503-577f-3d49-a3c0-a8d11edb45a4 | -9.84195 | -49.56349 | 2024-10-12 04:59:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 991ec194-d7da-3869-8a31-e699f1a96e81 | -9.84144 | -49.5672 | 2024-10-12 04:59:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 151c63ee-de86-3406-9235-5c38c1e1126a | -9.84093 | -49.57092 | 2024-10-12 04:59:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a058dc05-2964-3c63-963d-e4330a60ceba | -9.83733 | -49.56659 | 2024-10-12 04:59:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1aa77ae3-59dc-355b-a355-3138963964be | -9.83682 | -49.57032 | 2024-10-12 04:59:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba728dae-008e-3757-b6a3-3a0c9149fffa | -9.8327 | -49.56971 | 2024-10-12 04:59:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1a9e9cc-fb9d-3edb-984e-3e7ebc1958da | -11.92872 | -50.80239 | 2024-10-12 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd4a8ee4-b8f4-3ca1-a46f-0dafa35be9f5 | -11.92857 | -50.80106 | 2024-10-12 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9b403d1-1661-3605-a432-670b9dc70aa1 | -11.20746 | -49.93478 | 2024-10-12 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99d2c6a8-485d-3f90-a25d-001051f54b34 | -11.15703 | -49.72898 | 2024-10-12 04:59:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41355fd9-234b-3bac-8437-c55cfa28f205 | -11.15651 | -49.73278 | 2024-10-12 04:59:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95937a55-397e-3a55-ac50-d078a8c0fa4f | -10.87368 | -49.7407 | 2024-10-12 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3b35fea-5644-3e4a-8ed1-ba2413d27848 | -10.87008 | -49.73631 | 2024-10-12 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d4841eb-e9ad-3a9c-91bb-4bde6e98e50f | -10.86955 | -49.74009 | 2024-10-12 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b41af523-5844-3f10-a91b-b93c62cfae82 | -10.86902 | -49.74387 | 2024-10-12 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edec16e6-abcc-385c-a856-996e8705d2a8 | -10.53891 | -51.04803 | 2024-10-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26bdc82c-458c-398a-84bb-55f0d2840859 | -10.53512 | -51.04747 | 2024-10-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b6eb17ce-9a86-36d2-9ff2-32842fbb70e1 | -11.98491 | -51.93154 | 2024-10-12 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d81a723-c7ef-3bc2-b8ac-6e2add4c485a | -11.98861 | -51.93048 | 2024-10-12 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a1d2800-9f15-3e8d-9de4-55717db22a48 | -11.32575 | -50.90035 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 49dcaef2-f4f6-38c1-9d84-5f846109f144 | -11.32505 | -50.90524 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| a3862969-e662-380b-ab22-a4db677e4304 | -11.32436 | -50.91013 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 57d077a8-3ec7-3b0f-bcf1-145ccefe2073 | -11.32119 | -50.90466 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 824435ca-c3be-381c-b5e3-a9c57931e36b | -11.3205 | -50.90954 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8aa77e43-ae07-3f5d-a22e-42d959055e81 | -11.26511 | -51.43139 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 624c453b-8c0b-3e91-9ee5-9d7c547ce476 | -11.26204 | -51.42626 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8950eb2-911f-32ee-9a8f-e214f65feb1c | -11.26138 | -51.43083 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e8e25e15-aa1a-3c71-8e40-40bd8e08e143 | -11.25764 | -51.43027 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2fb567d8-53e3-39d3-82f8-989ccd3c5caa | -11.15893 | -50.95336 | 2024-10-12 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 15c4deb0-9074-364c-b6a9-a7c4f985d62e | -8.85778 | -53.01403 | 2024-10-12 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0de3e2d5-86e1-3bdb-8456-c0057ec5a8f7 | -8.85722 | -53.01772 | 2024-10-12 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a5dc49a-7fc5-3de2-b4e2-07c2e8d2b5d6 | -8.85495 | -53.00982 | 2024-10-12 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14764aae-7244-3f56-bff7-8c935eb39fa7 | -8.85438 | -53.01355 | 2024-10-12 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61330572-4bae-389d-8676-75a90a2b1dce | -9.82054 | -53.16299 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0306b2fb-73f1-370c-a3d3-7daceea80f14 | -9.80864 | -53.17256 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f2aaf8c-dc49-3e97-95d0-cf61b3c5471c | -9.8058 | -53.16833 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94e3b9af-68a5-3d10-90b8-afe72b7d9485 | -9.78028 | -53.15305 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61e71518-b460-36f7-8930-c0a3e0300255 | -9.77744 | -53.1488 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d6812f9-7655-3638-aae8-dd0dde910ccb | -9.77688 | -53.15251 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 217b3845-59af-38da-9718-84e91af2d97b | -9.74684 | -53.144 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebfda404-210f-3581-8c29-349a0fc78b2f | -9.74344 | -53.14347 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cb1ff32-b1ae-3129-8f48-db4249c1a57b | -9.74288 | -53.14718 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab69094a-a4e1-3c52-8b7c-38f9acea3f02 | -9.73893 | -53.15033 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb80d08b-b023-3024-a6dd-54e15b5e0031 | -9.71118 | -52.84401 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5233e7d0-d6a0-3d2b-8da9-6fcfe3c95cdb | -9.71057 | -52.82459 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2132e1cf-b751-36dd-b984-3e7083fe1bfc | -9.67177 | -53.10629 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23151cd3-ebf8-35ca-816f-0c431f4e761a | -9.66952 | -53.12117 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e00b9a07-f03a-3dba-944f-4f35fd8611d3 | -9.66896 | -53.12488 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f687dad8-9f5e-3ed9-b961-35aa09d5b94d | -9.66836 | -53.10577 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31d162c1-069e-31ee-a106-dc510c7d2adf | -9.66612 | -53.12068 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d53b478-0b95-344c-80d4-3cbf5d446364 | -9.66556 | -53.12438 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4241d62-c444-34f2-9de6-8fecac6b6899 | -9.66216 | -53.12387 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 521c92a7-f043-388e-9d85-5a18336b9483 | -9.65363 | -53.11114 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 51ef3cab-d71c-32b4-beb3-d69a93a2fe94 | -9.65307 | -53.11485 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 120d9f59-bb22-3f85-a361-048d4890f10c | -9.65251 | -53.11855 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7b3f03f-8901-39b4-b4ca-5235678b28c4 | -9.41662 | -53.21859 | 2024-10-12 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd0e93f7-8f73-31d6-8da5-bbe893134e65 | -10.0803 | -53.37207 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7ccbecb-3c4a-307c-a5c1-497176cbe06a | -10.07635 | -53.37521 | 2024-10-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f756af08-dc21-3f75-8400-606c5671098e | -10.87352 | -52.37585 | 2024-10-12 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84987b09-ae4f-3849-95bf-62d43b95775f | -10.86406 | -52.39095 | 2024-10-12 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab3b73ab-ce2a-3914-b0f4-eecafab1bd6e | -10.71018 | -53.0308 | 2024-10-12 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ae7278d3-10a9-3527-a543-549879856ed1 | -10.70616 | -53.0341 | 2024-10-12 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 153c12a4-666f-3099-bedd-d6e321d15799 | -10.70099 | -53.02166 | 2024-10-12 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c37e1887-1660-32a0-8fdd-728fd9124735 | -10.69755 | -53.02114 | 2024-10-12 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| acb7644f-29d3-3994-8b56-ea51ea5a481f | -10.69411 | -53.02062 | 2024-10-12 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 61589e9f-64e6-30a2-a5ff-5efe95aa81a4 | -10.69009 | -53.02391 | 2024-10-12 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 888a1a9d-e581-3c73-bbe5-14ed7cc2788d | -10.68952 | -53.02772 | 2024-10-12 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35c219ac-c442-3501-811a-60cb683e9ace | -10.68722 | -53.01957 | 2024-10-12 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c24bc567-e8b4-3dd5-aca0-e7cdd280347a | -10.68665 | -53.02338 | 2024-10-12 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47333491-591b-31d3-8442-43314fc13cee | -10.68551 | -53.03098 | 2024-10-12 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c170b111-e78f-306b-bc05-5b6ccc73e12c | -10.61431 | -52.82867 | 2024-10-12 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddcecfdf-674f-3997-aa1c-20ca1da1bbe8 | -10.61142 | -52.82426 | 2024-10-12 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37daf6f6-c281-37ec-8128-8154f4d85b6e | -10.61085 | -52.82812 | 2024-10-12 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c384283b-5de5-3fcd-b01c-2aa93ac5ea25 | -10.43898 | -52.92004 | 2024-10-12 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d298005c-eb3a-36e8-91bc-88e8cc6873f1 | -10.24162 | -52.7143 | 2024-10-12 04:59:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18c3e20d-d46e-33e9-abfc-e3c98069382c | -10.23953 | -52.71434 | 2024-10-12 04:59:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 316baf02-c60c-3fdd-a719-31938b9daae5 | -10.23815 | -52.71377 | 2024-10-12 04:59:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4353b7bb-71f9-3b22-bce7-b67fc6190874 | -10.87411 | -52.37176 | 2024-10-12 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e778c1e1-ed0c-32a7-b2f8-ad3815e76db5 | -10.86287 | -52.39905 | 2024-10-12 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e82bd94-2468-3b98-a69e-bdafaa81cbb9 | -10.86228 | -52.40313 | 2024-10-12 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4377f8b9-7974-3e36-b2bf-a83294015551 | -10.71247 | -53.03894 | 2024-10-12 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d278e6ff-e072-3ec1-955f-07fa868666cb | -10.7096 | -53.03461 | 2024-10-12 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9c52395-c1a9-320c-a219-b9cb1a35f6b9 | -10.70444 | -53.02216 | 2024-10-12 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1ab7867-e443-3efb-817e-d12cf63b7664 | -10.69353 | -53.02444 | 2024-10-12 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73ef708c-5725-383c-9832-591448c0abe8 | -10.69066 | -53.0201 | 2024-10-12 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c8be253-3b13-31a6-8ed0-793efec58007 | -11.66665 | -52.61576 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b3eac05-384c-3d95-8409-ec1575b83b6e | -11.66618 | -52.61726 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README88.md)
