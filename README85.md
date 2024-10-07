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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ff10170-e4e6-3c33-821b-67534a8f060c | -11.24956 | -51.38288 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a01ccde4-145f-3e11-b83b-48ca40097c87 | -11.24839 | -51.36682 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d039d906-3721-36a9-8f29-63395bcea317 | -11.24781 | -51.3707 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06f674bf-1909-3d58-9fbe-4ef8da4dc808 | -11.24724 | -51.37458 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83d06f78-8523-3f10-9112-0e39de783de3 | -11.24667 | -51.37846 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfa400e1-ee46-3142-97c1-e7ad74892b2d | -11.24549 | -51.3624 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 101f5dbc-1dee-3d5b-802f-a38cdd4fbf66 | -11.24492 | -51.36629 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 53c8bfed-8c85-3350-96fd-19d5144986d6 | -11.24435 | -51.37017 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8f4eb40a-a49c-3583-ab8d-64192601b1d9 | -11.20555 | -51.88905 | 2024-10-07 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6c18a03-cf84-33a9-9911-e1c5f065ad41 | -11.20215 | -51.88852 | 2024-10-07 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7b5dea7c-a9b8-3770-bbd5-95608a9b10f0 | -11.19875 | -51.88797 | 2024-10-07 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c9c6a7f5-06ed-3073-a6a8-26c612a7a623 | -15.01648 | -52.06123 | 2024-10-07 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c640292-923e-3ec1-9875-cdf1d3266f6f | -15.01298 | -52.06069 | 2024-10-07 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 34839193-6030-337a-85e1-1c3788786262 | -15.0095 | -52.06014 | 2024-10-07 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8b6007b7-4108-32fc-a6f2-875b79babdff | -16.25217 | -52.39328 | 2024-10-07 04:53:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| beb319a3-3dc8-3d9e-8cf7-34e314df9674 | -15.91973 | -52.24529 | 2024-10-07 04:53:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f1d7e821-2a5f-386e-a246-edca8bc47e6a | -10.92469 | -52.39674 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31623477-83ea-3c64-95db-e39643123035 | -10.90804 | -52.43829 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2de6415-2338-3857-b665-0a4001d26831 | -10.90749 | -52.44189 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a032d737-0064-34c8-ab9d-bbe87f051f4d | -10.90694 | -52.44549 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c54a51b7-2531-3ce9-b3f3-b44b005facfd | -10.89341 | -52.37707 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d85c3748-534b-3bef-9198-a3b426254415 | -10.89116 | -52.36932 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c33ece4b-c6b9-3661-8aa5-fee23956da98 | -10.89061 | -52.37293 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7e0004c-6272-3168-a71a-6c9acaa1b769 | -10.89006 | -52.37654 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b14224b-ae5d-3c53-8d63-b70f8d4b34c8 | -10.88671 | -52.37601 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a88968ed-7ce2-3946-87f7-35312b828a09 | -10.88336 | -52.37548 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e05384fb-301c-3417-8598-84dd61b5e87e | -10.88281 | -52.37909 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f54d6b38-076a-3284-ac69-20124ced2ded | -10.87946 | -52.37857 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3381f2b7-c492-3d16-8658-e1b57a22a943 | -10.87891 | -52.38218 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ebc2cca-7afe-3f99-a3ad-725488262a1f | -10.87837 | -52.38579 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcaede03-d0be-3983-a525-03c7c35108a7 | -10.87782 | -52.3894 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c2bff60-629d-3162-aea7-c0642383a2e0 | -10.87727 | -52.39299 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c552fcd-c9f3-35d6-93c0-b1e575f1a676 | -10.87672 | -52.39658 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9664429d-d9ff-3ef8-ae29-3f0e949c31ac | -10.87563 | -52.40376 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7131e714-315d-3e6b-930a-95cdf4f6daed | -10.87338 | -52.39605 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9eec3143-f992-3270-9b49-60d78ef71c7b | -10.87283 | -52.39964 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 126c2f7b-b76c-3d35-83a0-0147a927e805 | -10.87229 | -52.40322 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fec4bca-2ac0-3fb8-bd80-0bb94e8021a6 | -10.7702 | -52.47136 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9bc62bd-ba71-39b1-80a7-dfbcceb12624 | -10.76686 | -52.47084 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f224cb55-21ca-37d4-8da4-fca99fc5b59a | -10.76631 | -52.47442 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d0f19dd-67a4-3c7c-807e-763836b8d752 | -10.76576 | -52.478 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c18e053-9d13-333b-af5d-f61feed098b6 | -10.76242 | -52.47749 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55dc6334-3c61-330a-b669-38cb2d4c6e98 | -10.75963 | -52.47338 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1fe71b00-e80d-35db-a378-03a25c4a5839 | -10.75908 | -52.47697 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8b8cc79-135e-37c2-a750-985490f2e8ec | -10.70012 | -53.0367 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8fc38d76-4442-3647-8d7c-6b0b68938a32 | -10.69681 | -53.03618 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5de16f2-f129-39ed-895d-fe5182ae764e | -10.95703 | -52.38707 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4af964b3-7ab3-3019-89b4-e74eee5e1009 | -10.95368 | -52.38655 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f523dc64-fde0-3584-8369-4267f9e6759c | -10.95313 | -52.39016 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38625d18-cc2d-3181-8e7d-a620e9af64fe | -10.95257 | -52.39376 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 528ae8dd-7e9b-3392-abfe-e97d4445fec7 | -10.95202 | -52.39735 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71aeb458-1b5c-3a65-9dfd-5647cfcbd527 | -10.95089 | -52.38242 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d5f4b72-457c-34e7-9baa-9b9c66b0dd6a | -10.95033 | -52.38604 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27aa2758-1168-3936-a391-1860488a3366 | -10.94978 | -52.38964 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cddfc754-21cf-39a9-8873-3f25eeb836b5 | -10.94922 | -52.39324 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e409a1b0-47dc-3556-b339-cb78f06f26ea | -10.94754 | -52.3819 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2613487-d5ac-325b-9e4e-da3e57409894 | -10.94698 | -52.38552 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94811d9c-0394-3271-b4a6-de336c38f6e6 | -10.94643 | -52.38912 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05492948-2af4-3149-9c58-64a7daff1b1f | -10.94363 | -52.38499 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4630c9f3-0f05-3f76-ace1-4302d97516f5 | -10.94308 | -52.38858 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eab7778f-28e3-3174-98df-e192503d232e | -10.93918 | -52.39165 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3096a46-b301-3730-8925-619a78757cf2 | -10.93863 | -52.39524 | 2024-10-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 653910d3-3e02-3def-be2a-69c3d7bb6b57 | -14.81786 | -53.89448 | 2024-10-07 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81dd68e5-dba4-3906-81d4-f42671de0a6c | -14.81621 | -53.9052 | 2024-10-07 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31fd1499-1629-3a0b-8e95-843a53f338f4 | -14.81455 | -53.89393 | 2024-10-07 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b35093f2-995f-36df-9f83-aa406cdad418 | -14.814 | -53.8975 | 2024-10-07 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06b94d95-25e3-3cc5-97f3-cc2e26b2247d | -14.81013 | -53.90053 | 2024-10-07 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e59b0f7-2277-33bf-b23b-0d33354933e1 | -14.80682 | -53.89998 | 2024-10-07 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8dcecbe1-1f94-393b-b3a0-0d9bd3ca6a36 | -14.79579 | -53.92746 | 2024-10-07 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a60eb8f-eba2-38c7-b3b2-45b282473698 | -14.79248 | -53.92691 | 2024-10-07 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11346f23-1596-3e46-8fc0-bac4e26954f2 | -14.79081 | -53.89368 | 2024-10-07 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e286f1b-0809-3321-84d2-0467c82b40f8 | -14.78807 | -53.93351 | 2024-10-07 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 14578597-919e-3f0d-8ba3-9fd555fe8b82 | -14.78586 | -53.92583 | 2024-10-07 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 689ef79a-6f8b-3845-81b9-89f3f07c85d1 | -15.39819 | -53.74525 | 2024-10-07 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8f908c5-1487-3f0f-af2a-3ea9342aaaa8 | -15.3505 | -53.74488 | 2024-10-07 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef4314b5-3c7e-3a49-9516-fba1b54bf472 | -15.3494 | -53.75212 | 2024-10-07 04:53:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6f320b1b-4d24-3817-bdfd-5b8e5db8cb07 | -11.09318 | -54.0246 | 2024-10-07 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7486ee7b-93e3-399a-ba8c-d12b18e297d7 | -11.08932 | -54.02757 | 2024-10-07 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fbf9dc13-f8e6-3e50-b73b-45cb40c7aee6 | -11.08547 | -54.03053 | 2024-10-07 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d3f147ab-6b10-3266-8725-5c548137bec6 | -15.70259 | -55.76918 | 2024-10-07 04:53:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac3e80d7-b490-3669-a591-e9d31f425d60 | -21.70865 | -42.28836 | 2024-10-07 04:55:00 | AQUA_M-M | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 7af6fab1-37e4-3740-9af2-df1567bd7313 | -20.2655 | -42.92279 | 2024-10-07 04:55:00 | AQUA_M-M | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| a7581a92-affa-3743-a6f9-95043574ab9c | -20.22381 | -42.89598 | 2024-10-07 04:55:00 | AQUA_M-M | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 217114c6-d5cc-38b2-bb3c-720c7b8a2b13 | -19.98576 | -42.45919 | 2024-10-07 04:55:00 | AQUA_M-M | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.3 |
| 8547378d-94eb-3e23-a61f-c220d869629e | -19.97688 | -42.45769 | 2024-10-07 04:55:00 | AQUA_M-M | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 1accc1db-3aff-3271-8383-5ba4d840697d | -19.96695 | -42.45888 | 2024-10-07 04:55:00 | AQUA_M-M | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| c56a6864-8215-30f2-8f3c-ab57c9f14110 | -19.96553 | -42.46831 | 2024-10-07 04:55:00 | AQUA_M-M | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| c79780c9-2806-3d02-8ee7-0afb6b41e849 | -19.90411 | -42.63212 | 2024-10-07 04:55:00 | AQUA_M-M | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 71a266c3-ce6a-397e-889d-1b3b7cf83e4c | -19.90267 | -42.64156 | 2024-10-07 04:55:00 | AQUA_M-M | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| c491a43f-ce2d-35ce-90fa-0ebd6bea4279 | -19.90122 | -42.65102 | 2024-10-07 04:55:00 | AQUA_M-M | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 45.4 |
| 2fc03b54-1d50-3e5a-b8aa-958c0f82e616 | -19.89977 | -42.66047 | 2024-10-07 04:55:00 | AQUA_M-M | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| d9fd1642-687e-3bd5-8547-fae9f46ea84b | -19.89521 | -42.63062 | 2024-10-07 04:55:00 | AQUA_M-M | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| eb17cd7c-62b0-36a2-a707-290a771eb229 | -19.89376 | -42.64005 | 2024-10-07 04:55:00 | AQUA_M-M | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 37c23c69-e07b-35d8-971b-2d1272afac7f | -19.89232 | -42.6495 | 2024-10-07 04:55:00 | AQUA_M-M | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 5b2854e6-c6d3-3726-bf8d-4cec6598c848 | -19.89087 | -42.65894 | 2024-10-07 04:55:00 | AQUA_M-M | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| a305d5b5-3bdc-33ec-9c25-2d38961bc2ad | -19.8503 | -42.37563 | 2024-10-07 04:55:00 | AQUA_M-M | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 989d3082-04f7-336a-ae03-df0a6dd9bfa1 | -19.84887 | -42.3851 | 2024-10-07 04:55:00 | AQUA_M-M | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.7 |
| 4fbf9306-b19b-34c0-a916-a5df7daeb118 | -19.84143 | -42.37412 | 2024-10-07 04:55:00 | AQUA_M-M | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| d04ed6b9-452c-376b-a7b9-63e02ac404e8 | -19.83399 | -42.3632 | 2024-10-07 04:55:00 | AQUA_M-M | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| de97f780-3317-3174-a755-2e609c8632a0 | -19.83256 | -42.37262 | 2024-10-07 04:55:00 | AQUA_M-M | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |


[Clique aqui para ver as próximas entradas](README86.md)
