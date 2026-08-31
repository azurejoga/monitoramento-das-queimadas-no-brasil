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

## Dados Diários - Página 190

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d2d924a-daab-368f-895c-aeaee9e565e8 | -8.8207 | -71.243 | 2026-08-31 18:50:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 5779e266-019f-316c-ae65-3d5157788e27 | -9.2081 | -65.7857 | 2026-08-31 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 1ce35bfe-fd41-3f1f-bff7-70a695146f8d | -10.3394 | -49.9547 | 2026-08-31 18:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 516a9e9e-1159-3907-a0b5-de54b629f6f1 | -3.1083 | -61.238 | 2026-08-31 18:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| e7b647d4-889e-34de-80fc-af7a02126bdb | -3.1839 | -60.1559 | 2026-08-31 18:50:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 28a510ef-d7f2-3f9e-9234-e7ae9571da4e | -11.2503 | -54.0146 | 2026-08-31 18:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 110.1 |
| fce75cac-f398-30b2-9984-a5b1e05082c2 | -11.4828 | -58.5159 | 2026-08-31 18:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 110.1 |
| dba641dc-cbae-3db2-935c-cfbbe09950b7 | -10.5719 | -57.495 | 2026-08-31 18:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 5a840a95-7b2a-3b99-ad66-82a9555b9daf | -15.0049 | -48.1721 | 2026-08-31 18:50:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 99.1 |
| b5a66706-60b4-3831-83c9-7d154c73a717 | -10.7407 | -54.0401 | 2026-08-31 18:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 215.5 |
| 2156c0f4-ee24-3269-ad33-910984d312a6 | -9.2099 | -59.4027 | 2026-08-31 18:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 4a63285b-3ce0-3d2f-b141-83d1b752b3ca | -15.6142 | -56.3898 | 2026-08-31 18:50:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| e4252744-1c12-3a87-88fb-8483299ebfca | -11.1809 | -55.0821 | 2026-08-31 18:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 59248fdf-40a8-3eb8-92b1-45bde8855e9e | -14.1456 | -52.8082 | 2026-08-31 18:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 57b8a5ab-39d2-3ef1-9a69-25326d14d808 | -3.1083 | -61.2191 | 2026-08-31 18:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 60aff69a-85bc-31b1-bec6-aee2201f80f3 | -9.0059 | -65.4186 | 2026-08-31 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 81a9aa6c-9aad-31e9-9de8-a33cd2ee9396 | -8.6154 | -54.7945 | 2026-08-31 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 42696e55-ad49-3ff7-9571-c5a449044101 | -5.9636 | -57.6704 | 2026-08-31 19:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 043136dd-9af6-3185-983c-c10de3085201 | -3.4002 | -61.3276 | 2026-08-31 19:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 7a70fbc2-71a3-3976-bf3b-90e11e5b1cea | -7.699 | -55.3544 | 2026-08-31 19:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 429f9521-2c5b-3cef-ac57-5b9e963aa1c5 | -9.2081 | -65.7857 | 2026-08-31 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 73662d8e-2fda-37fd-b737-d0661e3ffc10 | -7.6251 | -55.2987 | 2026-08-31 19:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 268.2 |
| acb01644-6e16-3630-ac37-78af5a4aa516 | -9.0431 | -65.3988 | 2026-08-31 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| ce2e42a5-e483-3c43-a80f-df7b16dc5cf4 | -7.0517 | -52.7187 | 2026-08-31 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 07b145aa-a44f-3264-9347-87ab8ece5085 | -17.3228 | -42.6878 | 2026-08-31 19:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 649.6 |
| acdec1ad-cd97-3e9b-9d1f-8f3d88ea94e7 | -3.1267 | -61.1811 | 2026-08-31 19:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 153.9 |
| 62c11658-7359-3186-9ffa-3766ff7ad257 | -6.4054 | -49.9441 | 2026-08-31 19:00:00 | GOES-19 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 132.1 |
| 1f8e454c-835f-373d-97c1-f61a60706989 | -3.1449 | -61.1808 | 2026-08-31 19:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 143.0 |
| 8024da31-471b-3b25-8c9d-a16a961cc3e6 | -8.0381 | -62.8608 | 2026-08-31 19:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.2 |
| f76b1153-4edb-3a82-8096-e8f99a5a0ef5 | -9.6049 | -68.5979 | 2026-08-31 19:00:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 97.1 |
| a4ad467b-e73a-3686-9354-657083b044ef | -8.8705 | -66.7822 | 2026-08-31 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 252.7 |
| a04e3429-253b-3a45-bbd5-8677d2e73852 | -10.572 | -57.4752 | 2026-08-31 19:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 22fe90a5-a2a2-3667-998f-817c7659c805 | -20.2982 | -47.8378 | 2026-08-31 19:00:00 | GOES-19 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 5ba134fa-59bb-38d4-91ba-8df62550bc01 | -6.9121 | -59.4734 | 2026-08-31 19:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 08e1923e-5b7f-3dee-b51d-b4683427551a | -3.6847 | -64.6138 | 2026-08-31 19:00:00 | GOES-19 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| ec77cf76-c179-3216-bfd2-cc952bff8c8d | -2.7118 | -47.0649 | 2026-08-31 19:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 677c52d9-b82d-3569-9ec0-632ce79f6d3f | -8.2605 | -62.758 | 2026-08-31 19:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 82a0003d-e900-33d9-b7ab-1ae669c01bcd | -10.7271 | -50.6405 | 2026-08-31 19:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| b0ed0c32-c97e-34e7-9f2a-f294f328f709 | -3.0894 | -61.5214 | 2026-08-31 19:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 71f2c5cd-88f8-3a57-8caf-fc964c321170 | -6.6542 | -59.426 | 2026-08-31 19:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| dc599238-2112-3d19-8f4c-6dd4bc0e2a9e | -11.5479 | -45.4676 | 2026-08-31 19:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 20e123ed-6984-3d46-9bd5-01363fe0f859 | -12.0925 | -44.996 | 2026-08-31 19:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 34420f49-7879-3888-b71c-bc8df36f808f | -9.208 | -65.8044 | 2026-08-31 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 0920ab8a-04bd-3115-864a-074498fde132 | -15.2275 | -56.3716 | 2026-08-31 19:00:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 46418d10-e563-3bd7-9f5a-f84e62b9ee27 | -15.3628 | -52.8192 | 2026-08-31 19:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 133.7 |
| e20355bc-d6a3-31c4-9db8-c48e3d70afb1 | -5.4876 | -57.1416 | 2026-08-31 19:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| a23993a5-8e00-3904-8c51-250364c84db9 | -7.905 | -44.2346 | 2026-08-31 19:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 272.8 |
| e820945d-1150-35af-a771-96b09cd62646 | -14.444 | -53.4016 | 2026-08-31 19:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| aceb5f2f-18a7-3995-86b0-46df352c8d26 | -11.2503 | -54.0146 | 2026-08-31 19:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| a079dd96-7f88-3a9f-a373-a571dbae0413 | -8.8521 | -66.7641 | 2026-08-31 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 48f589f2-168f-302b-a5a4-a3d0aa528155 | -9.0612 | -65.4916 | 2026-08-31 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 19e2d7c4-817d-3987-8767-1b86254285ff | -8.5971 | -54.7553 | 2026-08-31 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 761b7993-3e5e-3990-931e-0028d312b705 | -3.4185 | -61.3273 | 2026-08-31 19:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 48a55ee1-2b27-34ca-880c-f8d119a9a462 | -7.0292 | -55.6511 | 2026-08-31 19:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| e310c8a4-1531-3972-8555-7701f553712c | -11.7973 | -47.6672 | 2026-08-31 19:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| a7152daa-325e-3848-98db-6907b2b49bc5 | -11.4828 | -58.5159 | 2026-08-31 19:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 8dc1d229-1b1a-39ad-b467-a4f3a82934d3 | -9.9708 | -53.9419 | 2026-08-31 19:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 0a942146-a0de-34b4-9d3e-5e5fc3973d90 | -5.8692 | -52.0868 | 2026-08-31 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 61e84b38-68e8-3f1b-ba79-5f802f321b2e | -3.6399 | -60.5466 | 2026-08-31 19:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| f4dfa99e-ed3c-343e-afe8-895f5b41586e | -9.6676 | -47.9429 | 2026-08-31 19:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 5e808eab-badc-3b73-8919-2a6aea406ee5 | -8.8207 | -71.2797 | 2026-08-31 19:00:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 77.5 |
| d3e9096b-e5fb-3fe7-b5f3-9fcc3e163bf5 | -8.5363 | -67.1617 | 2026-08-31 19:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 82c0a4de-a34f-382b-a1b3-ae946bedf610 | -3.1266 | -61.2 | 2026-08-31 19:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 4baf3576-3398-3b7b-a666-a7ace9bea1e1 | -6.8217 | -43.5271 | 2026-08-31 19:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| ae5ff553-fb40-324c-9fcc-a8c09750d396 | -8.9873 | -65.4379 | 2026-08-31 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| ed04aa3b-a396-3a6a-9c57-2e4e0b394400 | -9.2144 | -47.99 | 2026-08-31 19:00:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 8ec62eea-18db-3df2-b7cd-d2399f5c1eb9 | -15.6336 | -56.3876 | 2026-08-31 19:00:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 150.6 |
| b6f33393-f35c-31dd-9825-a132def5daca | -4.1515 | -60.7257 | 2026-08-31 19:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 0aa1622b-6d52-3c1c-842a-88856c219f7a | -10.0677 | -59.412 | 2026-08-31 19:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| f0b05357-62eb-371e-86dc-ff45aa1811d3 | -6.0743 | -57.6465 | 2026-08-31 19:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| c3fb4046-c67e-31ed-8278-f66580593ae7 | -19.2347 | -57.3456 | 2026-08-31 19:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.6 |
| 14ba178a-1f82-3a19-8682-46c7f886fb98 | -10.4634 | -46.5638 | 2026-08-31 19:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| dd4ac5cb-1853-39ac-9de3-9500bc1c0ffb | -9.1895 | -59.6364 | 2026-08-31 19:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 9a1c931a-a8f3-365c-94fa-bc561fb67512 | -10.5906 | -57.4936 | 2026-08-31 19:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 32ad6e57-7b35-3e54-8453-f846cd19e6d5 | -11.2317 | -46.1041 | 2026-08-31 19:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 1560e0c9-6ca9-3fdc-8d2b-ebcd0212a6cf | -5.9451 | -57.6906 | 2026-08-31 19:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 129.4 |
| 825cce56-88a1-3c6b-b8a2-0877b76d2b00 | -9.6939 | -65.1145 | 2026-08-31 19:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.5 |
| f45bd195-19aa-30b5-803e-67411e5427d3 | -3.3871 | -59.3883 | 2026-08-31 19:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 211d6fdc-927a-370c-b4cf-093b0753411f | -17.8861 | -52.0988 | 2026-08-31 19:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 396a83a1-0a99-3496-b1b4-fdaa1860088e | -9.6683 | -50.8511 | 2026-08-31 19:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 54a0f5b1-06fd-3d41-8e7c-08729a598ce0 | -5.8879 | -52.0652 | 2026-08-31 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 76a7f235-5808-3dd9-b2c8-445c75d7a471 | -8.8706 | -66.7636 | 2026-08-31 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 254.3 |
| 4d9622ce-e1e9-36d2-81ed-227349f0ae24 | -11.1809 | -55.0821 | 2026-08-31 19:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 8b59f8cf-2149-30c2-8e58-5abe61243e26 | -5.8537 | -57.5576 | 2026-08-31 19:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 430ed3c3-e356-389d-a0f1-cefb11ed3e96 | -6.1294 | -57.6833 | 2026-08-31 19:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 3a0e14e3-82cc-3c8a-99c2-346550f8175e | -3.4002 | -61.3465 | 2026-08-31 19:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 6d7dbcc5-9b5a-3db3-be21-b50f4b149bd6 | -12.9225 | -45.8352 | 2026-08-31 19:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| bf7c9213-b985-38c3-80d3-22bd79ad35f5 | -7.3453 | -72.9539 | 2026-08-31 19:00:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 5ba0dcf1-9593-35df-9afe-2a187eb0515d | -15.2278 | -56.3512 | 2026-08-31 19:00:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 111.6 |
| d4c489cd-c0ea-3ac9-b357-76b819176627 | -3.6398 | -60.5656 | 2026-08-31 19:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 128.7 |
| ece98a87-4df3-349a-afae-054e87e1e97d | -6.9177 | -55.6967 | 2026-08-31 19:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 95442008-3e6c-3570-9152-a0e6aea9cf7e | -7.3119 | -60.5706 | 2026-08-31 19:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 20a006d3-5039-3c9d-bd80-0ed0f4130634 | -15.6139 | -56.4103 | 2026-08-31 19:00:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 6af9eded-2692-3c1b-bb5c-66595fcce265 | -6.8193 | -59.5734 | 2026-08-31 19:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| cb91bbf6-507d-3982-bc1b-4f66e06ba699 | -9.0058 | -65.4373 | 2026-08-31 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.2 |
| ebfc1edd-280f-370f-ba61-9561ec081d60 | -8.6852 | -62.9496 | 2026-08-31 19:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| b70c8973-6c8b-3273-a451-e81058dcfd7b | -7.0243 | -59.2181 | 2026-08-31 19:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| a0addc40-7479-3129-8245-82d3c28a579f | -10.7591 | -54.0794 | 2026-08-31 19:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 798ecb79-5f1b-3eb6-818f-5e6c00debc06 | -15.6333 | -56.4081 | 2026-08-31 19:00:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 26853a26-7dca-3288-bed1-15334626a4f6 | -9.908 | -67.0131 | 2026-08-31 19:00:00 | GOES-19 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 74.6 |


[Clique aqui para ver as próximas entradas](README191.md)
