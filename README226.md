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

## Dados Diários - Página 226

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dbe826e8-3f2b-382c-8bc8-76b53ded3c2b | -3.74703 | -59.47818 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d511f080-3dc8-331b-ba7d-c0c088567f41 | -3.18899 | -58.63732 | 2026-10-09 06:08:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6355db2c-9392-3656-bec6-12955ae3c55f | -8.44932 | -67.69955 | 2026-10-09 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b701b775-9160-381b-a393-f4cfa27082cb | -6.08912 | -62.51172 | 2026-10-09 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8c9bb12-ef07-3567-af28-c3a6df8c5b98 | -3.73421 | -59.45594 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 78354b0c-235f-3fe8-a787-71f87501b663 | -3.53865 | -59.40163 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 614b5381-0877-3e09-815f-cee89e017360 | -6.49325 | -62.85286 | 2026-10-09 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bf701bd7-f5fb-3e67-8732-f3afbf649da3 | -9.25305 | -62.30904 | 2026-10-09 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c2f01507-b202-309f-8a1e-dd5bf99e5597 | -3.98376 | -59.35299 | 2026-10-09 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c06248ca-a91b-3c48-878b-8613faabfb9c | -3.74054 | -59.45691 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6939a905-e745-3393-b5d6-3a9a7d5f808b | -3.89844 | -58.96087 | 2026-10-09 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fc56552c-85ea-3569-b7b1-9f3ee713f480 | -3.59946 | -61.63794 | 2026-10-09 06:08:00 | NOAA-21 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d790a9b3-9753-3625-8487-0aa5d578ae22 | -3.98449 | -59.34772 | 2026-10-09 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 850825ff-7bcb-3c27-9456-fd9e2de19507 | -5.265 | -60.18002 | 2026-10-09 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13c5ab32-71f7-3b59-9779-9c1d59ffe7ca | -6.73535 | -63.04212 | 2026-10-09 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 619cebf4-9756-3872-acd6-8b8ca7912c14 | -9.29273 | -67.6303 | 2026-10-09 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0130e61c-ca92-37d1-b843-9feda99907e8 | -3.96209 | -60.00212 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 00fd0b9d-645a-3e61-9739-0d56b606dbe9 | -8.70105 | -62.41225 | 2026-10-09 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 911f3518-f3cf-3294-9129-1d02535d0dc9 | -3.73987 | -59.37246 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fcc3f0f3-62b3-38ab-9455-482b85840604 | -9.20523 | -67.82417 | 2026-10-09 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b05d3e4-8beb-3df0-a7e9-fc7ce3e67acf | -6.08609 | -62.5112 | 2026-10-09 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5baba416-27b6-3ab5-b81a-4ed7e8185496 | -8.83913 | -61.46355 | 2026-10-09 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 152e406b-a66a-3bf8-9998-360245de18e2 | -9.28876 | -67.62971 | 2026-10-09 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b72d678b-f495-340d-96c6-ba29520722a3 | -8.7113 | -62.42143 | 2026-10-09 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38e23c20-b33b-36fd-b17f-e45487730c27 | -3.98848 | -59.35147 | 2026-10-09 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 667294db-5255-3074-88b6-b9aa9c2f897e | -4.07862 | -59.84347 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 458e7f9a-4804-3131-9986-43131d0efc65 | -3.7125 | -60.54053 | 2026-10-09 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d24e195d-ceb9-3be9-b4a3-f253655c08e7 | -3.63262 | -60.6333 | 2026-10-09 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10950b1e-751d-38c7-8b12-1ed9ed4b5873 | -3.46804 | -60.25246 | 2026-10-09 06:08:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c978dc51-d0a7-3152-a484-d84743b03c4f | -3.46907 | -59.26417 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb7a78f6-e583-36c9-8154-144479529aad | -3.53398 | -59.57204 | 2026-10-09 06:08:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b99ce229-b1db-3bcd-b421-5990a1918b68 | -3.18238 | -58.63631 | 2026-10-09 06:08:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 91c10f1b-79cd-39db-8d90-edc0683f54ad | -3.77939 | -58.58087 | 2026-10-09 06:08:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cbe738ab-7d43-3dee-a58a-cc1f1bbcbae1 | -3.89926 | -58.96125 | 2026-10-09 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a76f2c0b-c40f-3779-aaac-7109d6ebe9ec | -8.52062 | -67.02891 | 2026-10-09 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d5ba9c0f-caf7-344f-92fc-fe9926b41a63 | -3.60706 | -61.62435 | 2026-10-09 06:08:00 | NOAA-21 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d1a37d9-b1b6-30a3-b44f-28118e9db705 | -3.99015 | -59.35397 | 2026-10-09 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8f5ccc55-a61e-3853-bd0e-99814376a440 | -4.31016 | -60.87423 | 2026-10-09 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 853f0d5c-dbb7-3fa1-8310-7e113ebc4f63 | -9.20839 | -60.86763 | 2026-10-09 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe22a2ca-56e8-302f-968e-b6e3ae201e15 | -6.49236 | -62.85944 | 2026-10-09 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92c9d6ed-3929-38c2-82bd-a873e4f56d5c | -4.07309 | -59.83776 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9eb2d1c-d1de-3e16-85b4-8e748e1b2c7a | -3.46985 | -59.25898 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7cd2eceb-aa57-3d70-894e-9aad56d05f6c | -3.71609 | -59.65364 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4c8d9ea6-f645-388e-bd2d-4e4c312d043c | -3.71249 | -59.64848 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 96fa19c0-1d50-3c7f-85ac-718d0fd72401 | -3.53328 | -59.57702 | 2026-10-09 06:08:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f39747c0-66f7-3ab8-8467-0cc00aef3e4b | -6.48619 | -62.86525 | 2026-10-09 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9c75961-bf4c-33b4-9e31-27eb851e2707 | -3.70581 | -61.32931 | 2026-10-09 06:08:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e18ea952-f809-3453-bde7-8c5dfca3b38a | -7.44156 | -63.55428 | 2026-10-09 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c842d87e-5303-3858-b2ae-cfc1ba1063a5 | -3.50355 | -59.26402 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8a3ca909-c8d4-3df6-a25b-5d051f31a221 | -7.45038 | -63.55187 | 2026-10-09 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79740ce0-6360-33e6-950e-4c0e4e1dfe06 | -3.39908 | -60.85075 | 2026-10-09 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d5388b91-02aa-3b64-a5ec-102de007278b | -3.89921 | -58.95525 | 2026-10-09 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7da39bc9-0dc2-3df3-98a5-4769a1ac1e6c | -4.2997 | -60.94894 | 2026-10-09 06:08:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06f7ceaf-7c68-3293-905d-d7d23937c2f2 | -9.29224 | -67.63378 | 2026-10-09 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0b97894-4713-3d52-a8dd-df36f24c12cd | -6.7349 | -63.04538 | 2026-10-09 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 303ecf00-1789-3031-87fd-d9c8df837dff | -6.48663 | -62.86196 | 2026-10-09 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec71c20f-73f5-3556-ae5c-9ec7f006cf70 | -9.1649 | -61.40825 | 2026-10-09 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1b50424b-3b34-37ee-9c9a-631406b4c281 | -3.54427 | -59.40776 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 05ab1134-f1f8-3e66-a0e6-b91bf18619f0 | -9.21266 | -60.86892 | 2026-10-09 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ca9f1400-6a82-354e-a182-01fb042259d5 | -3.53538 | -59.57734 | 2026-10-09 06:08:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 459c5349-981a-3ef1-8b73-79e667c88f81 | -8.70571 | -62.42049 | 2026-10-09 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 012d7975-ebb4-32cf-818f-38a8cb2501ad | -7.44198 | -63.55125 | 2026-10-09 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04d6b93c-c218-34bf-85d6-f57039c02db5 | -3.53793 | -59.40675 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9039c4aa-3725-3e17-aa53-4e439f719419 | -8.84511 | -61.46437 | 2026-10-09 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2982397-1e6e-328f-8469-c4ef96614869 | -3.47584 | -59.50162 | 2026-10-09 06:08:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| baac05e9-3deb-3a9c-8e73-a841006de004 | -3.47234 | -59.25398 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bcddca17-061a-3c62-9a8f-eac0395ff418 | -8.6959 | -62.40781 | 2026-10-09 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d5047ed-9fd9-3648-bfc2-d96130eaf545 | -3.17082 | -58.6228 | 2026-10-09 06:08:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be8e31ae-d7ea-31e2-9719-8e05f85ed0db | -6.99726 | -59.10657 | 2026-10-09 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c60f0f63-b772-3f5b-9c90-35b3c34e7d1c | -3.71185 | -60.54487 | 2026-10-09 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cee72b5c-60ad-34d4-bb3a-ded54aecd9a2 | -4.12809 | -59.8958 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9d396bc9-f132-3a93-b595-f1163fabfa24 | -3.77855 | -58.58695 | 2026-10-09 06:08:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 61b02cdb-d9e5-33da-8b3c-cf88056e9a2c | -4.07794 | -59.84822 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cf1d9384-dda1-3ebc-94d4-bc02e001a741 | -7.45177 | -63.55576 | 2026-10-09 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7dd2bdb5-1570-3418-a9a2-93484c35cb93 | -9.11294 | -67.82578 | 2026-10-09 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a013eef-5cf6-354e-946f-73d77dc2997c | -6.926 | -59.26151 | 2026-10-09 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 84b3e78a-3afd-3c92-9910-38350969ce27 | -9.25509 | -60.88495 | 2026-10-09 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7822ec4f-b5fb-3d76-a1a0-3cf31410407e | -3.60442 | -61.64241 | 2026-10-09 06:08:00 | NOAA-21 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0d43742-0f99-3eca-a80e-b4f897292ca0 | -9.25572 | -60.87994 | 2026-10-09 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c5848c8b-e0f6-3f3e-b452-6a658856e5d0 | -3.60653 | -61.62799 | 2026-10-09 06:08:00 | NOAA-21 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 780858c5-9c21-3118-a5c0-0e2df6a6188b | -3.5412 | -59.40755 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f2d2cde9-05b0-3db4-8dd4-b2f8872693cc | -3.47062 | -59.25379 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d62b3458-3bc9-316b-b15c-e996e93c21e6 | -3.79402 | -59.37468 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3231573d-d3f1-3850-9480-2e14998e9a2d | -3.39139 | -61.0771 | 2026-10-09 06:08:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c114ef96-3a4e-3bb6-91e7-55ade7a934fa | -6.68388 | -63.02801 | 2026-10-09 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 75785945-6804-3789-9ef9-c5210be826df | -8.52419 | -67.03318 | 2026-10-09 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ff32058e-4a0c-3098-9bc3-3c624aa4bbd3 | -7.5744 | -61.54667 | 2026-10-09 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8a7f2eaf-25d2-3c67-a083-dce9f54a8dae | -6.48708 | -62.85867 | 2026-10-09 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e967a2f6-045c-3426-b7a4-abfeb3870e9b | -6.49147 | -62.86602 | 2026-10-09 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f201eda-85fe-3f89-be71-f64b17e659b1 | -3.16339 | -58.62743 | 2026-10-09 06:08:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9006fe32-1b95-32c0-b723-90bbcfd6b126 | -3.52753 | -59.34178 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 17134426-c9cb-3d30-b10f-4ca48dd42622 | -7.5023 | -70.04909 | 2026-10-09 06:08:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6364a55e-6d14-3d39-832e-6e347f8eb791 | -8.54756 | -67.07402 | 2026-10-09 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee416172-2216-31fb-bc73-ce3e75b019cc | -5.23923 | -60.1903 | 2026-10-09 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5e598be-4472-36dd-9a3e-f354a5614dcc | -3.60156 | -61.62352 | 2026-10-09 06:08:00 | NOAA-21 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42bf8dd3-c113-3076-84d7-3d1a7dc0770d | -7.57496 | -61.54248 | 2026-10-09 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d9b02092-6e61-39b0-9e62-e3cd8ef3b31b | -3.18732 | -58.64874 | 2026-10-09 06:08:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 846259bb-d2d4-371a-af9e-7b2019d815bf | -3.08553 | -58.09402 | 2026-10-09 06:08:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9624a854-a687-3326-a975-b60f231bea30 | -3.70635 | -61.32547 | 2026-10-09 06:08:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ed1feac-a85e-35ff-8bb9-a908ccc6e3b0 | -3.67055 | -60.6102 | 2026-10-09 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README227.md)
