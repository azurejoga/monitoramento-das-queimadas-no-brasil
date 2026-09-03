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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b5f6b10-48dd-334f-8370-3e22193b1778 | -3.6215 | -60.566 | 2026-09-03 14:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 3b4e9051-46fd-363d-a860-301ce18b4c20 | -6.6015 | -58.9651 | 2026-09-03 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 9df746fe-1951-3701-bd0e-9435abfe45ce | -1.8019 | -47.9586 | 2026-09-03 14:30:00 | GOES-19 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 14c43eff-ebaf-3ffd-bc7e-92d8ce721cc4 | -11.5373 | -50.9576 | 2026-09-03 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 42fe8c03-c28b-35c4-ae07-753c98e9aeeb | -9.6676 | -47.9429 | 2026-09-03 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 287bd67e-a657-3a0e-bbb6-72f15f84b218 | -10.2214 | -50.3089 | 2026-09-03 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 5b282b19-d406-3736-bef2-c1fa4f894730 | -8.4677 | -54.6429 | 2026-09-03 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 181.8 |
| 0e58be62-76f2-3070-8862-65ff6c271cee | -8.4675 | -54.6631 | 2026-09-03 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |
| aea05517-8d9b-3327-ae30-49064fb53774 | -9.5964 | -47.6204 | 2026-09-03 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 2bd38c08-a6a8-3330-b0fe-179091eb3713 | -5.3448 | -60.1424 | 2026-09-03 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| e33e2a3b-cf7a-3a3c-8db7-da00ede8a36b | -7.5138 | -60.7728 | 2026-09-03 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 1e830e9f-5ec7-3691-aa84-a03d609fd1d7 | -10.2025 | -50.3109 | 2026-09-03 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 9d9acad6-a4b1-31ca-ba8a-b3789a9fd8e1 | -7.1187 | -42.2264 | 2026-09-03 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| ff20c40e-2947-34a7-938b-2d95f6bdef60 | -9.6839 | -48.1386 | 2026-09-03 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| fa3365fd-37a0-3bad-aaf4-ff3ef6864b23 | -5.8887 | -51.9412 | 2026-09-03 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 30d1ea46-09a5-3cb5-8184-5afecc83dfc6 | -6.6883 | -59.9436 | 2026-09-03 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 155.1 |
| d194d46f-5841-357f-ac46-a35a6f66301a | -10.7856 | -50.5066 | 2026-09-03 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 123ba4a4-7b49-3e47-9fac-b4dc15550333 | -6.6697 | -59.9635 | 2026-09-03 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 9166470c-2db5-3f37-977f-ec05e16a0a0f | -8.449 | -54.6442 | 2026-09-03 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 5bea5bf2-411d-37a4-ad2a-880e7c2f6f31 | -8.6694 | -49.5369 | 2026-09-03 14:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 423b6f1d-094b-3449-ad15-2d8f67c7ed21 | -5.3264 | -60.143 | 2026-09-03 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 0ea9bb1b-2041-3f94-8434-282b4071328d | -11.2126 | -46.1066 | 2026-09-03 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| b79ed5a4-8ca5-304e-80c2-8db399d56b8f | -7.2252 | -42.7852 | 2026-09-03 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| 59b0e997-6210-3a3a-b463-3f28fc22b9a3 | -10.1273 | -50.2971 | 2026-09-03 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| c530872d-bfea-32f2-a5b2-71d4fe04613d | -1.4752 | -54.8157 | 2026-09-03 14:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| bb64e50e-61c5-30ba-b1ec-9b61796874c9 | -7.9905 | -46.54 | 2026-09-03 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 8a4f67d1-159d-3d3f-8490-2cb717a092f8 | -10.767 | -50.4872 | 2026-09-03 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 60810c66-93b1-3b3b-995b-cf609f71c7e8 | -11.062 | -49.7045 | 2026-09-03 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| a75209dc-766d-3478-81c5-c4163a03c985 | -10.2028 | -50.2895 | 2026-09-03 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 35aed0b2-081f-31ec-bee0-019ba8190e99 | -11.0623 | -49.6829 | 2026-09-03 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 4855e215-e4fb-38ce-a570-5ef40f880140 | -6.6357 | -59.4459 | 2026-09-03 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 3814a1eb-e760-3016-910e-c72fbf4134fd | -9.4532 | -45.6682 | 2026-09-03 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 51.6 |
| ab82bf08-c8e8-3492-912b-45c77fde24b9 | -11.5479 | -45.4676 | 2026-09-03 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| afd00c6f-81ec-3dcb-b258-756c1c170365 | -9.4345 | -45.6477 | 2026-09-03 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| f2ad766d-c746-32bd-85b7-5862f9341435 | -11.1307 | -51.5728 | 2026-09-03 14:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 48c90e92-9286-3d3d-a73a-8f2c4d880838 | -15.3061 | -53.8592 | 2026-09-03 14:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 14cdac19-9eee-3dd9-bc14-107c8b44bb02 | -7.6458 | -47.1479 | 2026-09-03 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| ea0753c5-91e9-3f86-b9d6-591cba787a9d | -11.2879 | -54.0317 | 2026-09-03 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 26d03ad5-18c3-3547-a51a-8db0f24e3b4f | -11.1117 | -51.5748 | 2026-09-03 14:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 5144b531-c30e-36ff-a201-33472a7fe29f | -7.2255 | -42.7616 | 2026-09-03 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 82.5 |
| 98c4c44d-d48e-3994-84ca-196dbd99df29 | -8.4046 | -44.9869 | 2026-09-03 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| d63f99e0-d3bd-3283-a196-72eab45c2485 | -5.565 | -60.1739 | 2026-09-03 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 32facb16-fcdb-3ea7-bb02-a96b78e62ffc | -10.7859 | -50.4852 | 2026-09-03 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| fdff76c6-f491-3d2d-88d2-19847abf0b8e | -12.1269 | -44.1755 | 2026-09-03 14:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 8deb693b-eb66-3c13-a674-4a75d4565df2 | -3.8603 | -44.0815 | 2026-09-03 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 925b247b-313f-3f76-a513-b7f8cf780dcd | -11.0054 | -49.6893 | 2026-09-03 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| c04d9fba-f300-3542-8990-395965a067c4 | -5.5098 | -60.1947 | 2026-09-03 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 173cb878-ed2c-3618-9692-0b83259c82e7 | -11.3224 | -51.4049 | 2026-09-03 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 34670c84-3144-3ed2-87c7-fb2609f4b8f8 | -13.3625 | -51.359 | 2026-09-03 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 21e46ebf-9767-3b91-8076-9c0a7cdca837 | -11.0247 | -49.6656 | 2026-09-03 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| c82850d9-9568-3b3b-bfcd-ec020e1a6e0d | -6.8172 | -59.9578 | 2026-09-03 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| e2d6fffa-c54e-3cb9-805f-9ec0121ba410 | -7.5139 | -60.7537 | 2026-09-03 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 576f8e04-856b-3b06-baf4-72056baf5168 | -6.7463 | -59.4416 | 2026-09-03 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 157.7 |
| 70b87b93-e53c-34b2-956a-260a457eed66 | -7.3487 | -60.5883 | 2026-09-03 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 6eb27136-cee4-32d7-b7fb-60691f86424b | -7.5325 | -60.7338 | 2026-09-03 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 1960f4e2-af34-38d8-bdaf-705a38165116 | -8.4669 | -54.7237 | 2026-09-03 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| faa36dad-c4ad-36f1-99c6-ee3ecb33a792 | -5.4737 | -60.0621 | 2026-09-03 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 100.6 |
| c9b8c95f-4c1d-3bc6-9c65-881eb139dda4 | -7.9907 | -46.5177 | 2026-09-03 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| c0d9949b-83b0-35c1-b306-31d0162b7315 | -11.3579 | -45.4027 | 2026-09-03 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 98d39dd2-e129-3503-bd52-7b913f045e33 | -11.0752 | -51.4731 | 2026-09-03 14:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 126608ec-df29-3aff-b876-5fb3b9db1c3b | -10.3583 | -49.9528 | 2026-09-03 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 01c34fa5-d5b7-3ea9-a39e-2c0b150ff56e | -7.5139 | -60.7537 | 2026-09-03 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| eacb9408-835c-36c5-8e73-f6a71af4fcd3 | -12.3626 | -48.1459 | 2026-09-03 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| db444a42-0840-353c-86b4-b25f72eebb8b | -12.1265 | -44.199 | 2026-09-03 14:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 16b4f07e-0b5b-3545-96c3-16499eb3554d | -11.5283 | -45.4933 | 2026-09-03 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 57e38d9e-148f-3952-adf5-ce2b0b2c2388 | -3.6215 | -60.566 | 2026-09-03 14:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| ce3834a2-e2b5-3fdc-bebd-036d0f1a2d0e | -10.7271 | -50.6405 | 2026-09-03 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 0e9177f8-df28-37e5-bf19-2b3db227c2b6 | -3.3872 | -59.3692 | 2026-09-03 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 5ac31428-310a-3c9b-b464-63e8b0a886d4 | -7.3487 | -60.5883 | 2026-09-03 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| db886a19-2dc0-3763-a122-65481bf22dff | -8.449 | -54.6442 | 2026-09-03 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| dc841785-67d6-353c-ba85-07d4dec0aef5 | -5.5098 | -60.1947 | 2026-09-03 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| c13c14eb-20a3-30ee-9419-0df68f8be8f0 | -12.1269 | -44.1755 | 2026-09-03 14:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| b940ead7-7f7d-3e21-abea-0d6bada6d64f | -1.4752 | -54.8157 | 2026-09-03 14:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| f96aa68f-1928-32b7-9532-6a0c8033829a | -3.1996 | -61.2177 | 2026-09-03 14:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| dba64e95-2f6f-3ce3-9617-081b1f01cbec | -7.5661 | -61.3239 | 2026-09-03 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 802ff3ff-d0b1-3dca-a1ec-fb1b7f305d04 | -6.6698 | -59.9443 | 2026-09-03 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 129.1 |
| 3547c373-4cf2-3415-a233-31d83b0f4f2d | -9.668 | -50.8723 | 2026-09-03 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| df479251-bffb-3ce8-89ee-be4a698d9c84 | -7.0058 | -59.2382 | 2026-09-03 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| d64ced9f-cafd-32bc-a522-2336fab172e9 | -7.3117 | -60.6089 | 2026-09-03 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 06eab3c9-f621-32e6-9e7a-c7efde45dae1 | -10.1087 | -50.2776 | 2026-09-03 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| d66dbba8-dcf4-3d16-a6ab-c1ff50dbdad1 | -11.0063 | -49.6245 | 2026-09-03 14:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 808d008d-e404-33da-8b73-c084707021b7 | -8.9111 | -62.353 | 2026-09-03 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 1ca014cb-44cc-32da-948e-5663e00a16f0 | -10.3394 | -49.9547 | 2026-09-03 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| cc044427-5803-31a7-a842-2a4e7520c1e9 | -12.1508 | -47.1058 | 2026-09-03 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 8d05cc1e-b1b2-3517-8634-1ba59e15f429 | -9.5967 | -47.5983 | 2026-09-03 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| e84f9234-cf1e-3d00-b6ed-26a35185d56a | -11.006 | -49.6461 | 2026-09-03 14:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| bc4e5742-e192-3f4e-9f9a-15a2a023b95d | -13.6236 | -51.8158 | 2026-09-03 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| b1e4cdc3-c11b-3c77-8ccb-7739bd74df11 | -9.5964 | -47.6204 | 2026-09-03 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| a6c7d036-3c02-32d0-9f74-249952014376 | -6.9657 | -59.7791 | 2026-09-03 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 2659ae27-c20c-3347-88d8-1e01c7b08962 | -3.0164 | -61.4848 | 2026-09-03 14:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 31623b76-8317-3305-a0f2-6b2121f98d36 | -7.5138 | -60.7728 | 2026-09-03 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 227ca942-80a4-38f9-9025-008278264127 | -6.7463 | -59.4416 | 2026-09-03 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.7 |
| 80eb0bf8-c285-3c47-9039-9b2fe1aac32b | -5.565 | -60.1739 | 2026-09-03 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| fe3515a3-a0dc-3eb6-9c71-3693a37ffcd7 | -6.6357 | -59.4459 | 2026-09-03 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 20024ae6-a69d-3aaa-ad08-6fb3375b1d2e | -7.4954 | -60.7736 | 2026-09-03 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 32ebba06-0770-34d4-b31a-acacc8c53384 | -6.6697 | -59.9635 | 2026-09-03 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 73b81b06-10a3-3052-96a7-61f7b13df020 | -8.4049 | -44.964 | 2026-09-03 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 61.4 |
| c63fabfa-9733-33d8-a802-51c2e51bb697 | -11.0247 | -49.6656 | 2026-09-03 14:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 4168afbf-249b-3fdd-811d-b328e7f5cb7f | -3.0347 | -61.4846 | 2026-09-03 14:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 9941fee8-9f3e-37a0-a174-04b9514360bb | -12.094 | -47.0688 | 2026-09-03 14:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |


[Clique aqui para ver as próximas entradas](README62.md)
