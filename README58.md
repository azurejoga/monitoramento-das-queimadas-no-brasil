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
| ed77c4dc-9d75-3ae3-8510-460f2eecde2b | -10.07476 | -46.01463 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 9bcc472a-ed77-3b3c-ac55-16ca257ea51b | -10.28208 | -49.96722 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f37b3c5e-2d95-30af-89b2-1e33a824b4a7 | -11.93726 | -38.29567 | 2026-09-24 04:46:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| bf7d50e1-f401-3849-8871-586f793bb812 | -12.20804 | -47.12482 | 2026-09-24 04:46:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 415c2353-ec54-3e1f-afa8-a7864afb6d77 | -13.17547 | -51.54125 | 2026-09-24 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 396c744b-43f0-3a13-ba48-a7a6c9e6d385 | -13.92046 | -46.90476 | 2026-09-24 04:46:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58952fe0-db3f-3156-90e3-4de9a80167b6 | -5.86525 | -60.16275 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75a40859-1314-3ae8-b149-b82af04dc769 | -8.25204 | -48.21167 | 2026-09-24 04:46:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 873a7817-834f-3ca6-8d6e-fb40dcce26c0 | -12.41548 | -46.95832 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d34ba57d-e718-3e1f-b4d1-33634ef4c8bd | -8.26879 | -54.77195 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 120c9917-58aa-3f70-85ca-1ff68792309b | -6.08876 | -57.62592 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c25299b4-3abd-34b0-a61f-512ebc69e9e3 | -10.61219 | -54.00122 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c57dec11-17cb-328b-90aa-c3cd00b1d1b0 | -6.6417 | -59.92822 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5c41646a-cb87-3078-8bf0-d67c48541aa6 | -11.91747 | -50.73714 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16c36940-bbfe-355f-ad55-cc2922506813 | -11.3946 | -47.36439 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30baa5ed-c9e6-3dba-a19d-c0ab454222a4 | -10.41952 | -49.37016 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b9dae0f-f168-3ac0-8496-32a212a26c60 | -10.08064 | -46.02385 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 487a70e2-dd9b-3f80-942b-5c7cffbf65c5 | -10.27314 | -49.95832 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4658e01-f2d4-38e8-a24a-81f825a4dc51 | -12.04342 | -50.28685 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17608ff5-d46a-33a8-aeee-af5ac1c96eec | -10.44554 | -46.28007 | 2026-09-24 04:46:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d5c81c9-8f89-3762-a7a6-6842c2fcc8f7 | -11.48681 | -47.33246 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f027d94-be5d-33fb-a190-9a41d0a4431e | -10.61969 | -54.00325 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28fd2d77-ec67-3e93-bb96-e1e7d11f3117 | -9.54123 | -45.36883 | 2026-09-24 04:46:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86477da6-a7c6-3860-bc2d-22fc4bc3f295 | -6.73197 | -59.42913 | 2026-09-24 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eadb0d06-7349-3c8c-9254-de79fbfd9bfe | -12.14081 | -50.71729 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 948b27f3-973e-3699-accf-43fd846f3999 | -13.38564 | -41.32526 | 2026-09-24 04:46:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e8fe8ec9-0208-35b6-89db-a6837e057bbb | -11.86091 | -49.95003 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 831d673a-780f-3d8d-aafa-c61d2c25e24f | -12.12017 | -50.73662 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c7709b9-a23c-3103-968c-c16932310a05 | -6.06919 | -57.8049 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 082df20e-678d-3d45-9e52-366748bbd963 | -11.43831 | -44.204 | 2026-09-24 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b434d14-63a4-300d-adda-5f73f7f34557 | -11.44114 | -47.40231 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7517b660-5c4e-3f68-b30c-c2885fc2033d | -7.44234 | -49.83441 | 2026-09-24 04:46:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03120462-2379-3ea6-97c6-af1bb939dae1 | -6.67036 | -58.58033 | 2026-09-24 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e8d9c3a9-6d15-337e-9b1d-3a6701bc3feb | -11.94433 | -55.92148 | 2026-09-24 04:46:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a181c5ab-7c55-36c1-b42b-32a4c7c97cbf | -6.03993 | -57.77208 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f076fb09-0f1e-3464-a29a-a894d007b080 | -6.61602 | -59.92648 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| adfff70a-de2e-3a02-8a40-e73dc776c8de | -11.39288 | -47.37581 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d972b40a-5df9-31a5-a991-bf7b5f7d3f07 | -10.88776 | -45.07862 | 2026-09-24 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59aa7093-9775-3caa-8d0a-e225446f6d1c | -6.88967 | -59.21517 | 2026-09-24 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 367928a9-0cff-32cf-86cf-6266317ef66d | -6.08252 | -57.62864 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f95a63d6-a02e-3055-8790-289576e24827 | -10.27651 | -49.95888 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0fc5bcea-624c-3d1a-a1ef-45e928b1d5c2 | -12.13038 | -50.73835 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4a9aca48-02f8-3e62-8a3f-4acec648851a | -13.07975 | -47.40042 | 2026-09-24 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdaec9bf-30cb-3123-b368-a79b9c2c0be0 | -6.6406 | -59.93672 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6cb93b25-9cad-3490-b2a8-239b038c53c6 | -8.00078 | -45.02394 | 2026-09-24 04:46:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9390308-282b-3853-aefc-0057121ab4bd | -6.61959 | -59.94053 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b7b23d1a-2ec0-3d61-8c82-50f5971074cd | -6.7299 | -59.42732 | 2026-09-24 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73144e1f-397f-3204-b3ff-911813917725 | -11.39859 | -47.36108 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2576f97e-dc56-37df-b4f3-01202c3f7444 | -12.77458 | -52.85144 | 2026-09-24 04:46:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4263931c-a315-30c3-a71a-65b95020c01b | -10.08831 | -46.04538 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6f2c1b61-d03e-34d0-9389-509fd1a37ebd | -6.67191 | -58.57162 | 2026-09-24 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 176289d2-75d4-3591-9ad5-00ba7bce85dc | -8.29048 | -55.10479 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43c5b83e-b251-3814-b543-74e235ac357c | -8.26065 | -54.76606 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a5a19d2b-e465-382e-bb85-73e35e119932 | -11.23774 | -51.38129 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac35f13a-fd8f-33a4-a4f7-05a0012dd895 | -11.40028 | -47.3959 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8c6665e5-e5f2-3704-a249-df36654e9ee5 | -9.24961 | -47.34722 | 2026-09-24 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 302b3ee9-5803-3b59-a156-3d03e1043704 | -7.4163 | -49.86462 | 2026-09-24 04:46:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff562a3c-eda5-3464-bb9c-d6c2b7549f55 | -6.01282 | -59.94078 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c1ed8c71-fd43-394b-89ff-f74fe69cccc7 | -11.62684 | -50.61256 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26aa871e-7d21-312d-88be-035861adcdf4 | -11.39628 | -47.37635 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19e679fb-d7ac-3321-b624-c7626627e16b | -7.5841 | -57.66086 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 685342d4-e9d2-3afa-bed0-bc5a2579dca7 | -6.61803 | -59.91589 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9bf4642a-41c2-3ad5-bf1f-4991c0fd2280 | -11.94102 | -50.74041 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0adae785-4e71-3803-ad41-a694a75bd79b | -11.70763 | -44.49921 | 2026-09-24 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21d45d45-3138-36fb-ab28-a059c644cef9 | -12.15543 | -47.35746 | 2026-09-24 04:46:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2107cd68-4089-30e0-ac03-b6d2d086b127 | -12.92602 | -50.91583 | 2026-09-24 04:46:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ad3efc0-1b4d-388c-915d-cdd6ce158b03 | -11.69827 | -43.47165 | 2026-09-24 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0cf17787-7239-39ab-afa1-db940819dea6 | -11.4207 | -47.39918 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f78f8ec-afa7-3f85-90e0-d28db97b9807 | -9.25353 | -47.34415 | 2026-09-24 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5635fc39-9cd3-3f6f-9d31-4b18ad8dacf9 | -8.93065 | -45.94611 | 2026-09-24 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 06ef2dce-2d34-38e3-bbf8-077d1f400669 | -12.12977 | -50.74206 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3a1ef060-960d-325e-93cc-d6f2f005f1be | -10.11373 | -46.0206 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb173119-66f9-3193-b4ba-c0f0b58b33d7 | -10.23747 | -49.98584 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 316b660f-9283-35a6-812a-a35fe34a463d | -10.62033 | -54.00267 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fdc0f289-95ee-3a82-ac1a-8c04ee4db7f5 | -6.67703 | -58.57702 | 2026-09-24 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e9b67683-6b6d-39b4-ba63-a9f663fa7082 | -10.9082 | -53.95079 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fede13cc-0730-3008-be24-1a0de1755114 | -10.24759 | -49.98752 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e894b0a5-3633-3c5f-868d-76e6d450e37b | -10.71428 | -48.72869 | 2026-09-24 04:46:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e434763-3c6b-3c84-bccf-975253e3468e | -11.39519 | -47.3605 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 837b8b4c-b8d1-334b-b0ae-c80ad7f60103 | -6.44273 | -59.96016 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3ecb4342-5432-37b6-bd54-a2f00a8fd54c | -11.23358 | -51.38463 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd67756b-5b7b-377d-95b7-b6d7a9e7616d | -10.20918 | -44.14235 | 2026-09-24 04:46:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| afcacb1d-96ab-370d-9190-9231e64eedcd | -9.59147 | -47.77629 | 2026-09-24 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3e201d3b-f6bd-3138-ad53-e8ca75906387 | -11.58137 | -47.73814 | 2026-09-24 04:46:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a922933-8c0b-348d-9183-b18224d4742d | -6.34427 | -57.77224 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0782335f-8070-31a6-b50c-981fa175f385 | -11.64538 | -43.48368 | 2026-09-24 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 796c5129-4c4e-315e-b596-36439deb3d0d | -8.30472 | -48.22366 | 2026-09-24 04:46:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 662ce4ae-6c5c-3ca9-9e66-e7b462155654 | -12.01392 | -50.31915 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aaac9f40-b12b-3510-8925-97dcd350b8a1 | -8.59759 | -54.61679 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3588d715-6f75-3cbc-94bc-6ab6c43d9d3d | -9.14781 | -49.96181 | 2026-09-24 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44fdee69-c5a7-3e90-a63f-98ba16ac6ad0 | -10.90479 | -53.9465 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9cd167cc-7d37-3bf1-943e-28f07dd2f932 | -12.41837 | -46.96276 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| bf8e457a-693d-3008-a386-332f308b872e | -14.63052 | -50.59662 | 2026-09-24 04:46:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a6a91ce-b28c-3a66-a9e1-cbeb72aee676 | -10.45317 | -51.30099 | 2026-09-24 04:46:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 349cc4ae-c057-3582-8199-840a5d987117 | -8.93007 | -45.94995 | 2026-09-24 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9aa004c2-0087-3100-8ed0-fc29e6abdd8d | -11.40369 | -47.39643 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 54ea6ab3-9a79-3222-b0dc-d302766ef85b | -12.13777 | -47.36228 | 2026-09-24 04:46:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ae73b22-029f-3eef-916b-d55a04a051b2 | -7.87934 | -61.18243 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8b177759-68d4-3d68-a0e4-79840f10ae3a | -11.6275 | -50.60913 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 278eef53-3868-3ad1-9a45-dc30796a867c | -8.29723 | -49.90686 | 2026-09-24 04:46:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README59.md)
