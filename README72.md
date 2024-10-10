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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3be1e1f3-47a1-39f5-ac97-bfe73c5e0917 | -13.84843 | -44.54805 | 2024-10-10 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb6f0578-54e6-3616-9a1b-6b9c25054b6a | -13.84502 | -44.54752 | 2024-10-10 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8882486-7a71-39e2-aa73-49ed35c20f96 | -13.84161 | -44.54698 | 2024-10-10 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f012da40-41f6-3e55-941b-93dd46620fe1 | -13.79524 | -44.62384 | 2024-10-10 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e79fec1b-dc03-335b-8d7c-af2ff518c156 | -13.79184 | -44.62331 | 2024-10-10 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61c4d251-84e8-348e-9c8b-ebdeeda74bc7 | -13.7915 | -44.62385 | 2024-10-10 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbd30547-6c41-363e-a4a6-fac0e1995907 | -6.52262 | -58.42287 | 2024-10-10 04:19:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46bde53b-ab55-33c3-bc09-8883b4057028 | -6.52255 | -58.40944 | 2024-10-10 04:19:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 889c61b5-6eb6-318f-9d8d-98d76e1b1105 | -6.51549 | -58.40779 | 2024-10-10 04:19:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 225988b6-d3dd-310a-993b-3c6252248edf | -6.48045 | -58.43732 | 2024-10-10 04:19:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9da6a595-9a88-3435-b596-a08d5e7d671d | -8.11501 | -58.03826 | 2024-10-10 04:19:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3731a292-441e-32aa-99c2-cd2e4b2a7891 | -8.11441 | -58.03897 | 2024-10-10 04:19:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 96114bd7-66dc-3627-bdbc-e6b2fbd26ffd | -8.11372 | -58.04491 | 2024-10-10 04:19:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 10330722-467f-34da-982e-4d2b4dfe4e1c | -8.11315 | -58.04567 | 2024-10-10 04:19:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 939189f8-43a6-3fd1-ba15-b9622410258b | -8.10821 | -58.037 | 2024-10-10 04:19:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f800cc67-6043-3a01-a512-3cc0b092fd82 | -8.1076 | -58.0377 | 2024-10-10 04:19:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 345dcfdf-5ba1-3f8a-8c5c-573c79056ee0 | -10.57428 | -59.50076 | 2024-10-10 04:19:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d03e512-cdeb-331e-99c3-31efa1f650ec | -10.40421 | -59.14544 | 2024-10-10 04:19:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1653e99c-dbca-3f08-a3c7-db4f55ca0035 | -10.40287 | -59.15203 | 2024-10-10 04:19:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 48ee7ab9-963b-3f53-8114-6c7d63ebbe55 | -10.39719 | -59.14423 | 2024-10-10 04:19:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53468e81-6129-3299-b82a-f5f0d288a037 | -10.39584 | -59.15089 | 2024-10-10 04:19:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be8084d7-6a05-3607-8528-ee2b1bbcef6c | -11.89246 | -59.45292 | 2024-10-10 04:19:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b79e690-2feb-3edb-af3a-4e4182a7525c | -11.89111 | -59.45945 | 2024-10-10 04:19:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 58985f4f-2d88-360a-bce4-8373c0080ef8 | -11.89018 | -59.45456 | 2024-10-10 04:19:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6064c073-dbc1-3ea7-b21a-f50f04a82c73 | -11.81803 | -58.84763 | 2024-10-10 04:19:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a4e53988-fa15-33fd-906e-841c79434694 | -11.81257 | -58.84031 | 2024-10-10 04:19:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cf9d893f-f4fd-3187-bbfd-e7e296c5bcfd | -11.81131 | -58.84634 | 2024-10-10 04:19:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 89b4eaab-d726-3e0e-8710-a42d60f504ed | -11.81062 | -58.84076 | 2024-10-10 04:19:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07ab7afb-0124-3279-8902-34c6ff03f5f2 | -11.81006 | -58.85236 | 2024-10-10 04:19:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ac1010ad-33ee-3873-9ba4-41cb24346719 | -11.8094 | -58.84676 | 2024-10-10 04:19:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4fc30246-3690-3cd5-b4b0-0fbcd93d7fba | -11.80819 | -58.85278 | 2024-10-10 04:19:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9cde0e0f-2854-36d1-af3a-375481eb9cec | -11.71227 | -59.29071 | 2024-10-10 04:19:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b1a6d49-3eaf-311c-a86e-f2761431b6f9 | -11.71141 | -59.28907 | 2024-10-10 04:19:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f9b847b9-6bab-32d0-ae0d-7e02ba96aea4 | -11.70544 | -59.28902 | 2024-10-10 04:19:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f33d0028-d6c6-3a34-aee2-fec8223505a8 | -10.60181 | -44.77414 | 2024-10-10 04:19:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 81bea9ed-1b13-3fe7-a9bf-b221f294fa06 | -11.67066 | -58.89975 | 2024-10-10 04:19:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e614f268-ed20-3e3d-80ac-7425216694e7 | -11.66678 | -58.89314 | 2024-10-10 04:19:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da6087f1-b830-3f8d-a090-9116e208804a | -11.6655 | -58.89922 | 2024-10-10 04:19:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f3a00fcd-202d-3958-89b6-1bb519218b37 | -11.66515 | -58.89232 | 2024-10-10 04:19:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 974f8880-bce5-3ae9-a49c-8f716da5912b | -11.66391 | -58.89839 | 2024-10-10 04:19:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 424fea29-48c0-345f-a087-5f3d9a2df67c | -7.19815 | -45.03839 | 2024-10-10 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79d9f5f1-f50c-3ee9-bca6-f0defb88765c | -7.13111 | -45.05275 | 2024-10-10 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28edce51-a0fc-32f4-a977-8b05c7fa3896 | -7.11543 | -44.70488 | 2024-10-10 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9557a007-23ed-3f46-a525-035dcf3e4892 | -7.11266 | -44.70088 | 2024-10-10 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07d640c8-4be8-3436-af24-90a7deaec969 | -7.10378 | -44.69236 | 2024-10-10 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 375f8f54-4219-3032-87bc-511a018e155a | -7.10046 | -44.69184 | 2024-10-10 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7792f034-4423-3875-8b2e-005dfb95e29e | -7.09991 | -44.69531 | 2024-10-10 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 326a659a-70c7-3268-8914-1ce5e70a3a9c | -7.0971 | -44.66994 | 2024-10-10 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73256cb4-03ca-3d0d-8b6e-c61cad0f69fc | -7.09377 | -44.66942 | 2024-10-10 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f1c8d3a-bc2a-39ef-a32b-4156fa7b7f22 | -7.08936 | -44.67585 | 2024-10-10 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 915b04c8-e873-3b5e-a2be-50164b1ea08a | -7.08881 | -44.67932 | 2024-10-10 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67ba2746-7eab-3a83-80ad-4e191e69fb5d | -7.04952 | -45.10071 | 2024-10-10 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d1a11ae-4f67-3ce8-b4bf-d94ecee81a70 | -7.04633 | -44.80073 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85ccaefc-6512-3500-8b72-d6d769709b85 | -6.98985 | -45.2235 | 2024-10-10 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94c4b53d-960c-3b1f-8a19-2d9c42e45bf7 | -6.94453 | -44.84159 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 735658ae-8baf-331f-bb04-659772a38317 | -6.94403 | -44.61337 | 2024-10-10 04:19:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6449270-b8f4-33cc-bffd-9020d03a0db5 | -6.94225 | -44.84082 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 785e2e9e-cc37-30d0-98a4-9367f4a1d507 | -6.9407 | -44.61285 | 2024-10-10 04:19:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4f7d87d-dbff-383c-8c58-39d7af1629d4 | -6.93893 | -44.84029 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| afe20259-90e2-3866-a921-1e669f93cb25 | -6.93738 | -44.61232 | 2024-10-10 04:19:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 660be5bc-c0ae-3825-bf19-cd951afe6332 | -6.92067 | -44.56699 | 2024-10-10 04:19:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b99351b-bdd6-3575-8b74-5c44cfc62ecc | -7.30719 | -44.96999 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 299f800f-1c4d-3417-a013-af05ef61daaf | -7.30664 | -44.97346 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ad0b4453-f7f3-308c-b7bc-f0c25ef61b1b | -7.30609 | -44.97694 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d1e975b6-1709-3e2c-8d12-af9f682ff34b | -7.30331 | -44.97293 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4c8a713a-49ef-3f6f-a48b-2eb6bf500649 | -7.30277 | -44.97641 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 49734598-47e7-3f9e-9420-af9fea1e2013 | -7.30222 | -44.97989 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 62e5ade6-f846-39af-a87b-2841beb5a355 | -7.29944 | -44.97588 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b0933291-cd11-3c56-bf5f-8e73866221e0 | -7.29889 | -44.97936 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dbd361d9-bd7c-32fb-857a-fbe387d53e6d | -8.34824 | -44.0924 | 2024-10-10 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 00535227-c252-391f-9b32-35018834c7a5 | -8.34434 | -44.09541 | 2024-10-10 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e2f2370-444d-3d8c-81c5-c843a368d830 | -8.34045 | -44.09842 | 2024-10-10 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c09cdb06-6df6-3f0f-be02-9cc23ff09429 | -8.3371 | -44.0979 | 2024-10-10 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92decacf-6e3d-3636-9ca9-90b2e41d2735 | -8.33376 | -44.09737 | 2024-10-10 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a39c657-3c3d-3f4e-935f-68550f85c7a6 | -8.3255 | -44.15036 | 2024-10-10 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c090c6fd-c71c-3952-9fc4-2978ba64b644 | -8.32496 | -44.15388 | 2024-10-10 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa2da10d-2f08-313e-a917-1d4de2e7fbad | -8.32216 | -44.14982 | 2024-10-10 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd28c673-963c-3204-b3e3-9b0bc2ea0a9a | -8.30197 | -44.08138 | 2024-10-10 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa6d7c42-3639-3a55-ab3a-6309875cca51 | -8.29882 | -44.16783 | 2024-10-10 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ed6fe76-adf9-3b15-b29d-122639e18de0 | -8.24779 | -44.8586 | 2024-10-10 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d504bb1-bf39-306a-9af0-690c3e4d7533 | -8.24724 | -44.86209 | 2024-10-10 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56fb2066-5d8d-3f77-b5bc-a2ed1f56d249 | -8.24446 | -44.85807 | 2024-10-10 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1169f40e-5e6b-3be5-9e41-177ad5155bb6 | -8.20885 | -44.39487 | 2024-10-10 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3d6f4ad-506e-3b6a-9f81-5f18b6c7a5af | -10.76335 | -44.99556 | 2024-10-10 04:19:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e59de70c-b0d4-32c8-ba2f-31b4f0e0e103 | -10.7628 | -44.99908 | 2024-10-10 04:19:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f076e2c-8cb6-362e-a1f2-f3c89002579a | -10.69868 | -44.99918 | 2024-10-10 04:19:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7a294fe-f590-3504-8696-913b26460549 | -10.60236 | -44.7706 | 2024-10-10 04:19:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 84700728-088c-3f82-82be-6879eb5642ef | -10.59903 | -44.77007 | 2024-10-10 04:19:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a82b5726-ab36-33a4-8360-248a8438e2d3 | -10.59848 | -44.77361 | 2024-10-10 04:19:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3f0687de-a598-37fb-b4e7-266a2d4ddd4f | -10.59793 | -44.77715 | 2024-10-10 04:19:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6162efc6-bb92-3afa-a5a5-a8ec8cc7a5c5 | -10.51165 | -44.85417 | 2024-10-10 04:19:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25c6ae61-f75e-3496-9b3a-0b2473aab8ee | -10.50831 | -44.85364 | 2024-10-10 04:19:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 203d9aaa-418c-3266-a042-77369b3efdab | -10.44927 | -45.12222 | 2024-10-10 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff2398e3-e670-3db0-bd0f-067bdc23cb0b | -10.44594 | -45.1217 | 2024-10-10 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87a9f5ae-d3be-337a-b008-c7a98c002b88 | -10.44539 | -45.12521 | 2024-10-10 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce948ff6-7803-3598-ac13-5b3f3e96fc0c | -10.44152 | -45.1282 | 2024-10-10 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef005450-3674-3612-a3e9-28a817b66f13 | -11.7853 | -45.20434 | 2024-10-10 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5dd017c4-405f-3876-b4c7-5b8f27676412 | -11.78141 | -45.20736 | 2024-10-10 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa3d8bd0-a053-3071-8c4a-b1acfe2ad97c | -11.67002 | -44.88345 | 2024-10-10 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 939d6844-6e0b-3cc4-9d89-901fceae90fa | -11.66667 | -44.88291 | 2024-10-10 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README73.md)
