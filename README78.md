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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae570827-5ec8-3270-a704-310c377bbb15 | -10.7719 | -46.2775 | 2026-09-14 15:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 4e0245f2-3a78-38e1-a983-317003fe5e58 | -5.2023 | -49.3348 | 2026-09-14 15:10:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 5470d384-4cab-3534-b274-25f4e6c60acb | -7.7824 | -46.6705 | 2026-09-14 15:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 5c890e52-e67a-35b3-b007-05b293e85c7b | -10.6417 | -46.0906 | 2026-09-14 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 7a45dfcc-4320-3816-b318-56c83eded7eb | -3.3871 | -59.4075 | 2026-09-14 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 93.7 |
| d741e833-7ee3-34ca-a743-dd8ea0c86c25 | -3.728 | -61.7367 | 2026-09-14 15:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 097ba6cb-a4e0-3f70-86e6-eff20a823d96 | -10.2929 | -45.2932 | 2026-09-14 15:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| eeee96bf-a0a8-38f9-a152-513db112fcf9 | -3.1816 | -61.1235 | 2026-09-14 15:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 9aeb717f-8ed3-349a-a8b8-e4b17339d310 | -6.1422 | -52.7711 | 2026-09-14 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 5dd34877-0544-3293-8d4f-93993a8c4995 | -10.6335 | -50.5651 | 2026-09-14 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 94b4e6ea-967d-3078-a45b-f3d4c0e67d83 | -3.3141 | -59.3515 | 2026-09-14 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 7e079bd6-a22c-3c43-9d7f-392b3ad688a1 | -10.2926 | -45.3161 | 2026-09-14 15:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 057609e8-d343-3439-b8ad-8779acec547b | -3.3306 | -54.1805 | 2026-09-14 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 9b3bea82-d8e5-30d4-ba44-51ccae4ed981 | -11.5984 | -47.0018 | 2026-09-14 15:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 41d0c3a1-4b3e-3655-b087-4954ac514518 | -6.1293 | -57.7028 | 2026-09-14 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| b0d0c68c-f095-3ba8-9c24-b303ab2ef304 | -10.6827 | -54.1679 | 2026-09-14 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 219.4 |
| d924ac6f-fb45-3cf6-8363-7804e560d110 | -2.6601 | -57.5702 | 2026-09-14 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 103.7 |
| eefe3bbf-66b0-3267-bef8-4a5ab5f33ae9 | -3.1514 | -58.644 | 2026-09-14 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| af0b1031-7638-311a-913d-c219c7599b34 | -9.9956 | -50.2675 | 2026-09-14 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| b8265d6a-c519-30cf-91a6-1bc653d4a4c8 | -11.3352 | -46.7674 | 2026-09-14 15:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 052a1acf-81d8-3ef4-bc60-6249ba4df3d3 | -3.1696 | -58.6629 | 2026-09-14 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 6cf5e4df-5e6b-3d13-9126-57ae937d3dfa | -3.3494 | -59.8097 | 2026-09-14 15:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| d1646dcc-8e19-3c49-b83b-47e7a5bde49f | -6.3434 | -55.8442 | 2026-09-14 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 7494126e-3aea-3237-9dcd-f99b65e929de | -2.6602 | -57.5119 | 2026-09-14 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| e0abc02d-6b5a-3065-96ef-054bf782aa3b | -3.3493 | -59.8288 | 2026-09-14 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 132.3 |
| 770a8304-7d28-3dbb-9984-8ca408674053 | -3.3677 | -59.8094 | 2026-09-14 15:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 5f7e65ec-bd1f-3def-a3ef-5e900466648a | -15.5572 | -48.7953 | 2026-09-14 15:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 63dc7a94-bfc4-345d-990e-8c44bdd7d5be | -6.6512 | -43.6587 | 2026-09-14 15:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 135.7 |
| ecb15693-2411-35f8-89fe-6676b12bf5d8 | -3.3305 | -54.2005 | 2026-09-14 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| da723203-6081-3ff1-9602-78ec159a1f32 | -11.354 | -46.7874 | 2026-09-14 15:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| c8d11595-9c5e-35cf-be45-13fccfff14ca | -13.5719 | -51.4605 | 2026-09-14 15:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 132.3 |
| cdeb41e5-72ae-3c15-acd1-30a70986df8b | -3.1814 | -61.1802 | 2026-09-14 15:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| bb8e6308-c006-3799-a986-e9c26047ac1e | -10.6525 | -50.5631 | 2026-09-14 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 05ca3885-5a33-3ae0-acb6-9ed0a282041d | -8.7634 | -46.4194 | 2026-09-14 15:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 114.9 |
| d5715898-cca2-33a4-8bc4-0afb6cf1dc7b | -3.3139 | -59.3898 | 2026-09-14 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 45ad5e79-cb5c-327a-b7b9-b6dbe84dfdfc | -9.1711 | -49.9835 | 2026-09-14 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 8a85c4d8-c1fa-3d90-aeb5-be84a00fa573 | -14.205 | -47.4039 | 2026-09-14 15:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 80.5 |
| f33ef184-3537-3271-9d1c-4b11c80db24d | -11.8365 | -50.0028 | 2026-09-14 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| d23b3b9f-ef66-304e-a8b5-abc398adffef | -8.6001 | -44.4609 | 2026-09-14 15:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 1f502ff0-588d-3f7d-ac45-630a84edf85e | 4.1884 | -60.63 | 2026-09-14 15:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 229ff3f8-1ec2-3d95-bdf8-c97d14f2223f | -10.7842 | -50.6133 | 2026-09-14 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| fb92c221-d954-3a73-a2c2-af3da96ebdaa | -9.6086 | -46.7311 | 2026-09-14 15:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 11b9bbad-670a-30d5-bfda-c898c2d72ff4 | -10.3116 | -45.3136 | 2026-09-14 15:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 0a555f16-a722-3057-86f0-adc1f1f061a3 | -10.312 | -45.2907 | 2026-09-14 15:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 117.1 |
| c77ad15a-cf59-3037-a4e7-3769ef44d2e0 | -8.8081 | -45.8753 | 2026-09-14 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 6461af39-fc29-3ccd-bc46-89d6e9576d9f | -10.7906 | -46.2977 | 2026-09-14 15:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 2c5155b5-3a2e-3706-af3b-cf25015b53ba | -10.6829 | -54.1475 | 2026-09-14 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 275.0 |
| f2791bd4-4b95-3a70-8824-cf64444863de | -14.1856 | -47.407 | 2026-09-14 15:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 1fe7cd49-8874-3a4f-ac4f-fc7b12f8506c | -3.4279 | -57.9816 | 2026-09-14 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| c9cee77e-fe3e-31e9-ae31-72202fdd50a0 | -6.1111 | -57.6645 | 2026-09-14 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 129.8 |
| c1929f19-a271-3088-8469-fbd5a447866c | -14.1657 | -47.4328 | 2026-09-14 15:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 86.4 |
| cdcf8977-d6ab-32ae-ab91-c4cc7471aa4d | -8.5417 | -54.6985 | 2026-09-14 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 82679528-5c7f-3e13-b74a-27d13204f198 | -10.7909 | -46.2751 | 2026-09-14 15:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 18238172-5eea-3d9b-b761-8f69e1bbb1f7 | -3.332 | -59.466 | 2026-09-14 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| fdfeff6e-1c44-368c-8ed7-e434a26d1b08 | -6.1109 | -57.684 | 2026-09-14 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 403.1 |
| 4924abf0-740e-3b3e-bdd4-5b706e5db383 | -14.1852 | -47.4296 | 2026-09-14 15:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 7a52cb51-b051-3ada-999a-bb12d571186b | -8.8137 | -46.905 | 2026-09-14 15:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 0222ee0f-e7dd-39f0-9b57-aa23329e78a6 | -3.314 | -59.3706 | 2026-09-14 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 188.2 |
| a5ace17f-891a-35a3-a549-bbdd6722d841 | -12.3919 | -44.391 | 2026-09-14 15:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 2f7211f7-8acb-3efd-8724-2f0b344f3c3f | -13.3059 | -51.3022 | 2026-09-14 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 1bd28f3c-0087-34c2-8805-f933a1435dbd | -2.88 | -50.4 | 2026-09-14 15:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2af35f1-25b1-3e9f-bbca-afc86e27eaee | -14.35 | -41.44 | 2026-09-14 15:15:00 | MSG-03 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a4e84cc0-2e5a-304a-aa75-7f504cabe115 | -2.91 | -50.4 | 2026-09-14 15:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afcfe652-8632-3a8d-9325-e6339c22a8d2 | -9.68 | -54.8393 | 2026-09-14 15:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| b5fdde03-7176-3e14-9881-9a18c5faca93 | -3.9707 | -60.0258 | 2026-09-14 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| df966f53-c15f-3dbf-9b10-213328007c3b | -10.2926 | -45.3161 | 2026-09-14 15:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 123.9 |
| c91ff5b3-c945-36f4-9366-40451032dfc5 | -3.7181 | -58.8823 | 2026-09-14 15:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| a9a1bc9a-9ead-3356-b745-504acc8078ef | -5.221 | -49.3125 | 2026-09-14 15:20:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 78768978-f446-376c-b2a6-675e1682f07a | -13.2867 | -51.3046 | 2026-09-14 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 948d2cf6-4996-3f18-9798-4a335c6c5eaa | -5.0688 | -56.2533 | 2026-09-14 15:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 64be1d5a-e510-3ccf-8ea1-1a8d8aeff59d | -11.383 | -43.9614 | 2026-09-14 15:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| f0b2cd5c-99b9-30fb-8b7d-2b693c42f9f5 | -10.6827 | -54.1679 | 2026-09-14 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 240.7 |
| 2fa54795-b8ca-3ea5-8b67-1f75583ed65d | -10.661 | -51.3465 | 2026-09-14 15:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 69d3d050-633c-342b-8812-79e015be265b | -7.8715 | -54.7016 | 2026-09-14 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 22b92e80-3807-3b81-aa13-774498ba167e | -3.314 | -59.3706 | 2026-09-14 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 68200324-c3b0-3a65-a7cc-d512aa5a3193 | -15.5572 | -48.7953 | 2026-09-14 15:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 124.8 |
| aeb59bcb-0640-3cd1-b108-921485f34567 | -3.1514 | -58.644 | 2026-09-14 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| aadb9fc8-1f7a-3f0d-a79a-8fb4b2492f41 | -10.6824 | -54.1884 | 2026-09-14 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| a944ffef-067d-3e1e-b7f7-99bac7923a7a | -13.5719 | -51.4605 | 2026-09-14 15:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 60aedcf3-25e3-3836-b1e4-a0306fc9def2 | -8.6194 | -44.4357 | 2026-09-14 15:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 145.7 |
| d0c84647-6195-32d1-b94b-6a6e13157ea8 | -10.312 | -45.2907 | 2026-09-14 15:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 159.2 |
| e363e6aa-50d3-3186-9cf6-caa59c934cb3 | -6.1109 | -57.684 | 2026-09-14 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 595.3 |
| 3e76eaec-911d-3923-bb58-5cc66243478c | -9.5126 | -45.4796 | 2026-09-14 15:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 066aa1f4-b42b-3452-a9e4-57b5a45aaf5b | -10.7535 | -46.2347 | 2026-09-14 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 28e918d8-8faa-3030-b1f1-d7fa79a5d7fa | -6.1108 | -57.7035 | 2026-09-14 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 163.1 |
| 5dd10e99-ac1d-399e-8d37-5a29a123d0dc | -10.3123 | -45.2678 | 2026-09-14 15:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| c4bb3ddc-3c70-35ce-a3f4-12f4b5a8549d | -9.1341 | -51.5718 | 2026-09-14 15:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 8d651deb-97d2-3e2a-b37c-62aff27c22b9 | -3.4058 | -59.2347 | 2026-09-14 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| bac8c572-8590-34c5-a415-2934099640fc | -2.6785 | -57.5115 | 2026-09-14 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 42fb33df-96ed-398e-adcd-3b5b4249813c | -6.5838 | -58.8304 | 2026-09-14 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 23bee0fe-48d2-387a-80c8-796fb95f1826 | -3.3306 | -54.1805 | 2026-09-14 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| beabd069-4004-3c81-a7cd-bfe2941c8489 | -3.1632 | -61.1805 | 2026-09-14 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 1a475705-7975-3b18-a346-497dcd510210 | -1.7133 | -54.9521 | 2026-09-14 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 7cde2bbd-510b-3230-88cb-317dc1928dff | -14.205 | -47.4039 | 2026-09-14 15:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 4a4e8908-9172-3167-87bd-5009b0c04b43 | -7.1048 | -41.7971 | 2026-09-14 15:20:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 308.2 |
| c4406302-39b6-38e9-8e13-30aacbbc2661 | -10.7719 | -46.2775 | 2026-09-14 15:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 7e22d1fc-4eef-373d-8e88-765cbce08e19 | -3.1816 | -61.1045 | 2026-09-14 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| c82edf48-748d-3b1a-8749-14522ba796cc | -13.5844 | -51.8632 | 2026-09-14 15:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 774d1fdd-595d-3486-8009-a11c79bb6c0a | -6.6512 | -43.6587 | 2026-09-14 15:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 3c173417-bba8-3182-a74c-34d4df219a77 | -14.1662 | -47.4102 | 2026-09-14 15:20:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 76.5 |


[Clique aqui para ver as próximas entradas](README79.md)
