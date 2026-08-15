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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 823bd65e-99fd-3d08-b802-9c90de0cf0a6 | -8.49132 | -44.74104 | 2026-08-15 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bb0ba99f-a48f-3caa-aabc-5ef0216c28cb | -12.23535 | -46.99811 | 2026-08-15 04:14:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f1acbad-9b90-3593-8b9c-6072da35616d | -12.03315 | -47.81431 | 2026-08-15 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4375666b-baa0-37a3-b133-f2a6cd811e12 | -6.93454 | -52.78456 | 2026-08-15 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7fcbfbc-83db-39b5-8dc5-fbda384312cf | -11.4038 | -46.32895 | 2026-08-15 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e17bbe8-093e-328a-9d0a-e53ddadfbc05 | -6.91007 | -43.63539 | 2026-08-15 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8e17ff9-a8e3-3d08-8113-711adf7e7337 | -7.81843 | -44.11274 | 2026-08-15 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| feb71f65-ca4e-3442-b0e3-e974a9603187 | -12.02541 | -46.42586 | 2026-08-15 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 539315e4-1dd3-3a2f-a467-ba7762158886 | -11.58477 | -54.69619 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b98610e2-0382-31af-9fba-f10b7842debc | -12.08104 | -43.17846 | 2026-08-15 04:14:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bcf4a81e-5da3-3a3f-822f-856de6d35d00 | -8.0698 | -49.71996 | 2026-08-15 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 40bf9695-e003-342d-9e24-8198c4c5b222 | -10.51764 | -50.16199 | 2026-08-15 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e5503be-de6f-3dda-bc09-ff3156eb3c8b | -8.01979 | -55.13358 | 2026-08-15 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1768c686-e716-324b-9df9-48a72b764b48 | -12.3068 | -49.98978 | 2026-08-15 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77240d63-c8e2-3b63-bea3-96b4ed8c7683 | -9.10887 | -46.40417 | 2026-08-15 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 85aafac7-42c6-3c99-8c79-61c5c0a9bea4 | -12.69331 | -48.45116 | 2026-08-15 04:14:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6971505b-aaf1-369b-ba10-b465b1667abf | -6.36553 | -51.74122 | 2026-08-15 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5a68d304-7a6f-32e3-9703-7a350f70d50b | -7.72361 | -46.24472 | 2026-08-15 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ed5eeb6e-b4e2-3104-a77e-1b9169fd2566 | -13.8576 | -43.64865 | 2026-08-15 04:14:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| bd4db27a-6805-34a5-b80c-437f02b72ffb | -11.39718 | -46.32595 | 2026-08-15 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a540c25b-02e8-31f1-be0d-3bc618e8b4de | -8.64954 | -54.71439 | 2026-08-15 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 417200e2-6997-396f-afab-9e33c2b644aa | -6.785 | -55.83804 | 2026-08-15 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd866d10-e60e-3266-a869-1d1d8ec7f559 | -14.25885 | -42.18052 | 2026-08-15 04:14:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c934bb4b-6aec-3959-82d3-a80ba7c75b96 | -11.50341 | -54.63042 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea522406-db0f-3138-aff2-63ba5083be1a | -6.99786 | -44.82799 | 2026-08-15 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a2ac92f-02da-399e-a1bf-e1c2152cf837 | -11.08296 | -47.21306 | 2026-08-15 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09a3f32f-2214-3b6c-95c3-db8e99f9e9fc | -6.36495 | -51.74443 | 2026-08-15 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 137ea1ef-1ca9-36ed-b141-9d0bb0320e91 | -10.65465 | -49.20162 | 2026-08-15 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 825d308d-f8f7-3cb3-b2c3-07739fa2cacf | -11.58582 | -54.69106 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f69d6268-9daf-3ced-bb0a-47b67b99bff5 | -8.44864 | -45.11316 | 2026-08-15 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe6af6b9-5d6d-3c89-abd7-68a3d295a2b9 | -7.07809 | -41.47688 | 2026-08-15 04:14:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 57713f1f-5df4-3350-95bf-26d54939f9d3 | -11.57959 | -54.69 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4aa5bd3f-5a0f-3303-a688-d810201b3481 | -11.41327 | -46.33945 | 2026-08-15 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a8bf6ba1-7c72-3696-8ee6-1f97de60d74a | -12.45811 | -46.52926 | 2026-08-15 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2aeab66b-2955-38e0-9eba-5d478188fbe7 | -6.24381 | -47.71272 | 2026-08-15 04:14:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b617bc7c-0b07-3383-b2f2-8e4c4084f638 | -6.93112 | -43.63497 | 2026-08-15 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 56433a45-394d-3498-83c2-0947023844a3 | -9.1179 | -46.39823 | 2026-08-15 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e2851e2a-9777-3770-b129-7101f880aa53 | -11.13993 | -49.0405 | 2026-08-15 04:14:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e69cab5c-e6b5-39af-91d0-55e58e705e30 | -9.13694 | -46.39948 | 2026-08-15 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 779d7215-d596-3a3b-9b75-fa95ddcef5d6 | -7.78271 | -47.31967 | 2026-08-15 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be9ae051-e4fb-3124-a61e-d24590bccf5c | -6.79186 | -55.85564 | 2026-08-15 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5a22168-3924-3ff0-bfb5-f1a91156ab1c | -7.2794 | -44.70589 | 2026-08-15 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f35e157a-ed53-3018-9f75-a79a7b3f2c24 | -8.95141 | -42.71243 | 2026-08-15 04:14:00 | NOAA-20 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 931f0f19-6d35-3c36-b0ba-fd098fce2c3d | -6.54391 | -55.18177 | 2026-08-15 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 958e170a-16b1-3b3d-92dc-975d0cbcf5ec | -6.94021 | -44.54145 | 2026-08-15 04:14:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3e1d575f-6b0e-34ec-96f1-a94df484b078 | -14.31582 | -41.75274 | 2026-08-15 04:14:00 | NOAA-20 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c063b8f1-dbda-31bb-ba47-4084180e107f | -11.41771 | -46.33558 | 2026-08-15 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 758e1911-2ee3-3123-a6eb-ec7ee010f5af | -11.07654 | -47.22714 | 2026-08-15 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5c517fc-71ee-308c-b577-34081f0bb432 | -12.73909 | -48.42947 | 2026-08-15 04:14:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88aa8808-28f5-3c90-a7ec-afc31d9544f8 | -9.51445 | -48.56795 | 2026-08-15 04:14:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c478fea-5b1a-33b0-aeca-6650d1c44c93 | -7.68613 | -55.16338 | 2026-08-15 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80ab0980-bca7-3f78-ad63-9bfc274702e1 | -6.53698 | -55.18052 | 2026-08-15 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9157a09-5366-3862-b964-ddc6e1cec23c | -7.81781 | -44.11657 | 2026-08-15 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 843a336d-a3c7-374f-bbec-78d8f55e1cb8 | -11.49624 | -54.63398 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 94f6a44e-5c72-3f60-a248-a940ea319237 | -13.54172 | -46.24938 | 2026-08-15 04:14:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c62ccf9-1bb5-3bc0-9239-faff1950fe97 | -11.93885 | -46.31568 | 2026-08-15 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 04629dc7-7a9c-3c5e-b5f1-ff0f2b3cc4f0 | -9.06221 | -45.78147 | 2026-08-15 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b77dd6f-5dff-3b48-a80e-7b850ed6a3e2 | -6.99429 | -44.8274 | 2026-08-15 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb6880d2-2092-3a26-9fcb-181d5dc51b10 | -12.735 | -48.42896 | 2026-08-15 04:14:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| edbc9aa6-e42d-308a-b7a7-39012de51731 | -7.45865 | -55.30927 | 2026-08-15 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 16a81b87-3279-3659-90d6-9f7fbfaa8cfc | -12.6967 | -48.4556 | 2026-08-15 04:14:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5cad266b-af2b-3e9e-b970-b45d5e3db822 | -12.38643 | -46.42239 | 2026-08-15 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8358411a-b333-348f-93f2-e1a41ccbb80b | -8.60925 | -54.67834 | 2026-08-15 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cfa518c5-d927-3d1c-95f0-ebf3c9f0b3ec | -11.4125 | -46.34391 | 2026-08-15 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 33e0f447-9957-3f98-be35-749745397b63 | -7.00244 | -41.44013 | 2026-08-15 04:14:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| dd6e9391-a4b1-3ea0-89ce-a88a5babf983 | -8.45153 | -45.11789 | 2026-08-15 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9fbb8c85-54cd-3f8d-92e8-4370ee6bbcf9 | -11.58702 | -54.69494 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a773b77c-42ed-3033-b807-71e2d7a4c4d2 | -9.11802 | -46.39627 | 2026-08-15 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4486af4e-7698-3bef-ba1f-b9963983d9ea | -6.92311 | -43.64129 | 2026-08-15 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3ae8876-612d-3fe5-b47d-b7d7076ec0e6 | -13.76855 | -41.8359 | 2026-08-15 04:14:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5448c192-3e5a-3452-80a5-ad19bc2bfe69 | -11.48786 | -44.56985 | 2026-08-15 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5e59201-0bc8-3485-a025-bdeeaceac9eb | -17.90547 | -44.44646 | 2026-08-15 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe4cf0b2-093f-39ab-9d43-7381f91dc37d | -16.10119 | -49.85929 | 2026-08-15 04:17:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a1051116-e52b-3637-ac0d-c11db16769fe | -14.94607 | -46.63518 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e1bb918-9a13-34d0-9c17-65b622789eba | -14.05728 | -53.66542 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11f7849c-1bd5-35b7-aad5-f8085d404fb6 | -14.43059 | -51.92714 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cb072d3-6138-3112-bfc0-169b56541aff | -14.44755 | -45.68984 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 940eacfd-2aa4-3585-82b2-357b247da958 | -14.12449 | -53.67709 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f842d0e9-5450-3906-ade5-03387c9e20c5 | -18.45905 | -43.44036 | 2026-08-15 04:17:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ce141c26-1bf7-3bc6-b879-7cdda6fb1766 | -14.08262 | -53.71165 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f359080b-afc8-3960-9d52-f1e61d324499 | -14.43439 | -51.93396 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72362947-2241-300d-b52f-53aac861c188 | -18.15508 | -44.96951 | 2026-08-15 04:17:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 22f0c568-6ed9-3a54-a575-2aace8ab5e6b | -20.01432 | -43.89366 | 2026-08-15 04:17:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2a9085f3-ee12-3218-8078-f27eb7d93bc1 | -14.43839 | -51.85491 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cdb5fdef-c457-3bc9-985c-42f63e2b7ad6 | -15.15336 | -50.06166 | 2026-08-15 04:17:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0955d14-5174-3d7a-8565-4b011bc2c8a7 | -15.65227 | -48.20452 | 2026-08-15 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2070d403-74a6-301f-a63e-54968a543c75 | -14.44275 | -51.91762 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 96f7fd96-32f4-3aee-a3f2-3adc47a89369 | -14.43596 | -45.69574 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11ead8c8-19dc-3422-9383-79da7998c75f | -15.06689 | -46.58194 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0d15ae7-218d-3788-aea5-8379af9e9784 | -19.86448 | -43.87191 | 2026-08-15 04:17:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cd9b49d4-6bfc-362a-a453-9c4718f4bace | -19.96464 | -44.71732 | 2026-08-15 04:17:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6437553d-cccc-3724-8fd5-df47d39f3222 | -14.07961 | -53.67833 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc54c6cc-f7e6-35cd-8b58-0f9258a36a78 | -16.71233 | -46.40198 | 2026-08-15 04:17:00 | NOAA-20 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 415fc962-ba71-3e1e-b9c9-86ed7eaab4c1 | -20.93667 | -44.77573 | 2026-08-15 04:17:00 | NOAA-20 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b4493009-37bc-3867-b3a1-b3989d50d868 | -13.64545 | -48.51148 | 2026-08-15 04:17:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24248684-e987-3912-92c4-a58ae8381345 | -16.88821 | -54.15117 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 392db3c7-4688-382e-9eea-cf99f7b13593 | -15.54265 | -42.29854 | 2026-08-15 04:17:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aebbe457-922f-32c4-afe4-77a88346f356 | -13.8227 | -53.77913 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97c22258-f24c-39fa-a03e-e763271f136b | -16.89447 | -54.14851 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 962b6c65-ee75-3c6a-9f08-55150ce0ab61 | -14.25482 | -52.03209 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README17.md)
