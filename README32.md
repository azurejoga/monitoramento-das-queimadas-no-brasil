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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3640bfd4-8a6c-380e-b35c-ba75cb40efe2 | -4.67309 | -45.81104 | 2025-10-31 04:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc02c9c9-395c-3f23-9eda-edd2a486c8d1 | -3.53081 | -47.54679 | 2025-10-31 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e07329b6-ebcc-3fb5-8ea5-781a4fc41c8b | -4.68321 | -50.44445 | 2025-10-31 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a4d6f4fb-02e4-3faa-ba9d-331fc68e62d4 | -6.20282 | -42.51778 | 2025-10-31 04:55:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 148ec5c3-1fbd-31af-8132-2e830334adb5 | -6.13253 | -41.68777 | 2025-10-31 04:55:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 589436e6-48de-3120-b293-ff965e540b57 | -5.45048 | -50.90038 | 2025-10-31 04:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 70e7a4db-7ece-385a-891f-7bc3d2095f1b | -4.47298 | -46.56199 | 2025-10-31 04:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 562e110c-dc49-3f26-822b-0f20053b28aa | -3.1066 | -51.28391 | 2025-10-31 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cb60914-a367-3554-9a29-3253ba56780f | 1.01402 | -51.29816 | 2025-10-31 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3437a925-357d-3169-898e-991221734dc4 | -3.71331 | -53.69159 | 2025-10-31 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57dbad40-b9d8-3b0f-80dc-9ccdcaff7c58 | -6.09367 | -47.22045 | 2025-10-31 04:55:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cd424ca5-47ab-3e2b-9c12-b56a8e3c1cda | -3.56893 | -45.35157 | 2025-10-31 04:55:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41e670d9-01ff-3477-9ddd-fb53eb0727c0 | -5.58964 | -48.04716 | 2025-10-31 04:55:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7a462493-9aa0-3a2e-a9d9-055ea665dc75 | -3.54913 | -46.43341 | 2025-10-31 04:55:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddf15880-23b7-352f-acc5-be2d53d87d10 | -5.2322 | -45.47666 | 2025-10-31 04:55:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ff0d200-07dc-345e-aad6-1bcef7e620b3 | -3.33155 | -54.08332 | 2025-10-31 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27587d20-13ca-334f-aa74-0c617b78a289 | -4.996 | -44.73082 | 2025-10-31 04:55:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2a7bf38c-522a-3ccd-93b5-8f28c6ecdd7e | -6.13759 | -41.69976 | 2025-10-31 04:55:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 42dfd714-fb63-3e81-acb6-cf9415514303 | -6.25479 | -42.55509 | 2025-10-31 04:55:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 34934237-7b8f-3608-93f1-e1d97d337612 | -4.24396 | -55.87725 | 2025-10-31 04:55:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a774157c-9606-3b59-9bae-efc0a73574f6 | -3.16766 | -48.60798 | 2025-10-31 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9af4994a-7822-33df-b0a9-f5761696a3f9 | -3.5878 | -50.26142 | 2025-10-31 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e86f403e-b96f-37ec-a89d-db1e408d6b15 | 0.21366 | -51.44807 | 2025-10-31 04:55:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4f7ad75-08c1-3ff2-a1f1-9c7d8d2072eb | -1.95399 | -47.85459 | 2025-10-31 04:55:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| adce0bca-091a-34f0-8978-67a2203b2a8e | -3.40741 | -52.72794 | 2025-10-31 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 813de728-2c4d-378d-985d-738b2a9c6b7d | -5.78862 | -40.81592 | 2025-10-31 04:55:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 29e11778-80e8-314c-9f0d-26da2f941e38 | 0.30738 | -51.08888 | 2025-10-31 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4776ed29-ae1d-33ef-9134-7f0325d75072 | -4.47747 | -43.44053 | 2025-10-31 04:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75422390-f0eb-3242-b173-6b07de473c15 | -4.42239 | -55.42253 | 2025-10-31 04:55:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4834355d-c8a3-3327-8cb5-87a56af487f1 | -4.34208 | -50.34944 | 2025-10-31 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35076e1e-24dc-353a-9a35-99f04091aba4 | -4.31539 | -48.08621 | 2025-10-31 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8ecdfac-c8b5-372e-9c7b-358e7a61b141 | -3.14635 | -49.42548 | 2025-10-31 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d7b00fd3-987d-3653-868a-c5af4c232367 | -4.85528 | -45.56817 | 2025-10-31 04:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| de789b92-f7f3-3f4d-a038-b5bd249bd5af | -3.54017 | -58.64995 | 2025-10-31 04:55:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09936275-6a9b-3fb3-8612-daf893d0ef3f | -4.63688 | -49.49151 | 2025-10-31 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 39c44fe2-ba32-32a5-9c5d-217825282497 | -3.35477 | -52.80467 | 2025-10-31 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db1ccf01-cf17-3b73-b9e5-2a6a7082622b | -2.90529 | -53.95906 | 2025-10-31 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73d7b811-f576-3a6e-82a1-8410c8497e2a | -4.94227 | -44.92014 | 2025-10-31 04:55:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d70cd832-c26e-35ce-a824-41ecc6e151ae | -4.22996 | -55.65872 | 2025-10-31 04:55:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 493d9b58-5f4f-312b-b0f8-0a33f443a6e6 | -2.04925 | -52.07872 | 2025-10-31 04:55:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2b79dcbc-6bdf-3f24-87cd-fa402511a276 | -4.89889 | -49.16666 | 2025-10-31 04:55:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1eabc412-1db7-3285-bd9d-6f883ff7dec1 | -2.67074 | -49.95862 | 2025-10-31 04:55:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a15197b-045e-3e4b-a767-314aabaea2d5 | -3.5008 | -51.55096 | 2025-10-31 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc126eeb-acc1-346f-937f-6cb6fb81446e | -1.20155 | -54.1677 | 2025-10-31 04:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 203cbfb9-a588-3a04-adef-58841dc2cc53 | -3.49325 | -52.35247 | 2025-10-31 04:55:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f8b93ece-8c9f-39b9-9dbc-8414c446ab5b | -3.5484 | -54.69147 | 2025-10-31 04:55:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c10c811-f63e-3c52-8f52-1199e1e09545 | -3.66844 | -51.71095 | 2025-10-31 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11f85da8-e1b0-33f8-8e2b-d03ed05a1a3d | -5.71888 | -44.53796 | 2025-10-31 04:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60058f1f-eb40-3da5-8d04-b38a572ceb5e | -4.48225 | -46.56314 | 2025-10-31 04:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| added4da-3b50-3d67-b77a-d33125f36ee4 | -4.56685 | -45.68018 | 2025-10-31 04:55:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bcbb6a36-d417-324b-8991-ac6c227768de | -2.99082 | -54.17201 | 2025-10-31 04:55:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f26e9be-3178-3640-b825-e1221c810954 | -5.28525 | -45.42342 | 2025-10-31 04:55:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcd741cd-704a-3a15-b0b5-500e16fd997d | -3.20914 | -51.02991 | 2025-10-31 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7503d19-1fcf-37fa-927d-5f7258121750 | -6.06786 | -47.28384 | 2025-10-31 04:55:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 76c4b35a-03ce-35dc-9533-9f81e505deac | -3.3321 | -54.07985 | 2025-10-31 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e4d8de1-1a9f-3945-ab2c-5d41bc81c5a2 | 1.53969 | -50.96373 | 2025-10-31 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ef6f5f3-fd15-3852-8363-ac43162ef5d7 | -5.61151 | -47.12229 | 2025-10-31 04:55:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b68ec650-ab20-3bd9-8ce8-536c72f7e541 | -3.46934 | -50.93886 | 2025-10-31 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55893e22-b8ed-3cbf-b804-d2f7934a1962 | -4.86065 | -45.56617 | 2025-10-31 04:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23020fbf-5408-3476-b997-53ea4b2aae3f | -3.5842 | -50.26085 | 2025-10-31 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3800a7bd-187f-38ff-9f18-55893dca7c42 | -5.20122 | -49.65291 | 2025-10-31 04:55:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea6bcebf-8d8a-33d7-ab13-6fb0c62c730f | -3.30436 | -51.92874 | 2025-10-31 04:55:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57c3de1d-22c8-3816-8d0a-3ef919cd6cb3 | -2.87195 | -53.97495 | 2025-10-31 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| adb8a632-4c83-3485-b7e3-7c74bd935592 | -3.40795 | -52.72449 | 2025-10-31 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81cc78c3-cbca-3006-aa1a-8960ae0c7929 | -3.52595 | -47.55015 | 2025-10-31 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 86491b85-b25e-3b0e-ba48-b114055e7480 | -2.42404 | -49.30236 | 2025-10-31 04:55:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d781564e-704f-338a-9003-5c62ac1d32ab | -5.02992 | -51.00041 | 2025-10-31 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 88d196a1-db6f-3b84-bb51-e03cb2d65f07 | -6.46753 | -43.56205 | 2025-10-31 04:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2400a85b-5b60-3195-b527-88b9929340f5 | -5.74392 | -45.5843 | 2025-10-31 04:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f3a240f-b623-3c5a-a009-aba275227e06 | -3.11474 | -53.22781 | 2025-10-31 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d76e93a-5cd1-31a2-b33d-c5b02e1c906e | -3.60519 | -50.6261 | 2025-10-31 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4c4bb2f2-f501-349b-850c-177533327d5b | -3.60227 | -50.62158 | 2025-10-31 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d5883136-bdbd-3aa1-879d-dd54c81f8aed | -5.6145 | -45.98152 | 2025-10-31 04:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff52d955-f37e-39c7-9889-07f73b5b754e | -3.1426 | -49.4249 | 2025-10-31 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a640e133-5a58-3a44-a802-617ac5e98015 | -3.86861 | -48.03568 | 2025-10-31 04:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c942a0a-abde-3e82-ba22-5b5fad42ca87 | -0.42868 | -52.06094 | 2025-10-31 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59ba3e94-57ee-344c-bc84-414b148e7751 | -5.95809 | -45.55309 | 2025-10-31 04:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c10cc96-562a-3e3c-bef6-61ee51cb4c08 | -6.10799 | -41.72264 | 2025-10-31 04:55:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3fcbc91f-47f5-38f3-b87c-9527955906c9 | -2.90969 | -53.95266 | 2025-10-31 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1380118-b695-3e55-a3a6-c6adc25bc3ab | -4.25448 | -50.66972 | 2025-10-31 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f476792-ac9d-3587-bbe8-b7fef8e3e92f | -3.59332 | -51.53887 | 2025-10-31 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61f825a6-3043-356d-83b2-0e51385ec717 | -2.05189 | -52.78003 | 2025-10-31 04:55:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1ddb84a-c082-3003-9b30-701ebf25bad4 | -3.1433 | -49.42035 | 2025-10-31 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 01a8a6a8-c973-3be6-bdb3-ffc612039298 | -5.71167 | -48.88627 | 2025-10-31 04:55:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 668a2ee8-ba1e-3e6a-a664-49606e0ac520 | -5.02732 | -44.81213 | 2025-10-31 04:55:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f342f2f6-9cd3-31bb-802d-a497b4be6e96 | -5.25744 | -45.51192 | 2025-10-31 04:55:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 084dded1-e788-3778-b7a1-907fa4ea5e03 | -3.4566 | -51.10509 | 2025-10-31 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3163f24e-154f-3bc9-96fa-b4e89f92011c | -4.67629 | -46.5253 | 2025-10-31 04:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01ccfd01-76b1-3a18-ac84-5928b12e57e8 | -3.60581 | -50.62213 | 2025-10-31 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f700762e-86cb-309a-bfc0-df6a2d00da91 | -2.89511 | -54.19584 | 2025-10-31 04:55:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8baa6e8-6a54-3f07-9c6b-b8cb363b3080 | -3.59673 | -51.53939 | 2025-10-31 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 692ce850-3a46-3eb6-97b4-3b70ff002074 | -4.47379 | -43.43777 | 2025-10-31 04:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 10c7b58f-20fb-3c03-8acc-4c170223ab7a | -4.67896 | -50.44814 | 2025-10-31 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5a510e6-d2f1-3d2e-a7de-f03fc0ede076 | -5.96315 | -45.55393 | 2025-10-31 04:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4eb4296-18cf-3c55-b977-5fe954a32a23 | -3.597 | -51.54248 | 2025-10-31 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04c6f535-7376-3565-ac7f-7591a08e40ee | -2.32 | -48.58519 | 2025-10-31 04:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| eb036e86-584e-324d-b747-ff649d62eaea | -4.8386 | -45.33138 | 2025-10-31 04:55:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2efd09c1-1b70-35fe-a6c7-d4f917a12059 | -5.95726 | -45.55899 | 2025-10-31 04:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f9e90d2-d00a-370b-9dfc-26a54b562b56 | -2.63821 | -48.50039 | 2025-10-31 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 3c12ca42-362f-3174-b935-6a0db829b437 | -4.53306 | -56.11023 | 2025-10-31 04:55:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README33.md)
